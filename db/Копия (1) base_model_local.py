####
##
#
#
from peewee import Model as pwModel
from peewee import SqliteDatabase

db = SqliteDatabase("db.sqlite")


class BaseModel(pwModel):
    class Meta:
        database = db
        pass

    class Config:
        orm_mode: bool = True
        underscore_attrs_are_private: bool = False
        # validate_assignment: bool = True
        pass

    def __init__(self, *args, **data):
        k = data.pop("key", None) or (args[0] if args else None)
        k = str(k) if k is not None else None
        init = {"key": k, **(self.__read__(k) if k else {}), **data}

        print("__init__", args, data, init)
        # print("__init__", self)
        # print('SELF GET', self.__read__(k))

        # super().__init__(self, **init)
        self.save() if bool(k) else ...

        pass

    def __setattr__(self, name: str, data):
        print("setatr base model", self.__class__, name, data)
        method = (
            self.__config__.property_set_methods.get(name)
            if (
                hasattr(self.__config__, "property_set_methods")
                and isinstance(self.__config__.property_set_methods, (list, dict))
            )
            else None
        )
        if method is None:
            # print('super().__setattr__(name, data)', name, data)
            # print('super().__dict__', super().__dict__)
            if name not in super().__dict__:
                super().__dict__.setdefault(name, data)
            else:
                super().__dict__["name"] = data
                # super().__setattr__(name, data)

            self.__reread__(name, data)
        else:
            getattr(self, method)(data)

        pass

    @classmethod
    def __read__(cls, key: str):
        return cls.__db__.get(key=key)

    def __reread__(self, name: str, data):
        print(" __reread__(self, key, val):", name, data, "self >>", self)

        if "key" == name:
            if isinstance(self.key, (str, int)) and self.key != data:
                raise ValueError("`key` change is prohibited")
                return
            else:
                super().__setattr__(name, str(data))

        if self.key:
            super().__dict__.update(
                **self.__class__.__db__.put(
                    {
                        **super().__dict__,
                        **(self.__class__.__db__.get(key=self.key)),
                        **{name: data},
                    },
                    key=self.key,
                )
            )
        else:
            #   для читабельности поделили на две части
            super().__dict__.update(
                **self.__class__.__db__.put({**super().__dict__, **{name: data}})
            )

        return


db.connect()
