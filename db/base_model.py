####
##
#
#

from odetam import DetaModel
from odetam.field import DetaField
from pydantic import Field

# from odetam.async_model import AsyncDetaModel as DetaModel

from settings import DETA_BASE_KEY
from .types import Union

# from pydantic import BaseModel, OrmModel
# class BaseModel(OrmModel):
#    class Config(DetaModel.Config):
#        orm_mode: bool = True


class BaseModel(DetaModel):
    class Config(DetaModel.Config):
        arbitrary_types_allowed: bool = True
        deta_key: str = DETA_BASE_KEY
        orm_mode: bool = True
        underscore_attrs_are_private: bool = False
        # validate_assignment: bool = True

    def __init__(self, *args, **data):
        # print("__init__", self.key)
        # print("args", args)
        # print("data", data)

        k = data.pop("key", None) or (args[0] if args else None)
        k = str(k) if k is not None else None
        # print("key", k)
        # print("key", ({"key": k} if k else {}))
        # print("__read", self.__read__(k))

        init = {}
        if k:
            init.update(self.get_by_id(k) or {"key": k})
            init.update(**data)
        # print("__init__", init)

        # print('SELF GET', self.__read__(k))
        super().__init__(**init)

        # print(self)
        # print(self.__dict__)

        # self.save() if not k else ...

        pass

    @classmethod
    def get_by_id(cls, key: Union[str, int]):
        return DetaModel.get(cls, str(key))

    def __setattr__(self, name: str, data):
        print("setatr base model", self.__class__, name, data)

        if name in ("key", "id", "_id"):
            print("setattr KEY", self.key)
            if self.key == data:
                return
            if self.key is None:
                print("self.__setattr__")
                super().__setattr__(name, str(data))
            else:
                raise ValueError("`key` change is prohibited")
                return data

        method = (
            self.Config.property_set_methods.get(name)
            if (
                hasattr(self.Config, "property_set_methods")
                and isinstance(self.Config.property_set_methods, (list, dict))
            )
            else None
        )
        # print('method', method)
        if method is not None:
            print("getattr(self, method)(data)", data)
            data = getattr(self, method)(data)
        #   метод-сеттер должен возвращать данные, которые вносим в текущую модель

        try:
            super().__setattr__(name, data)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        return data

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

    pass
