####
##
#
#
from peewee import Model as pwModel
from peewee import SqliteDatabase

# from pydantic import Field
from peewee import Field
from pydantic.types import Any, Union

dbh = SqliteDatabase("db.sqlite")


class BaseModel(pwModel):
    class Meta:
        database = dbh
        only_save_dirty: bool = True
        pass

    class Config:
        orm_mode: bool = True
        underscore_attrs_are_private: bool = False
        # validate_assignment: bool = True
        pass

    # key: Any = Field(alias="id", default=None)

    @property
    def id(self):
        return self.id if "id" in self.__dict__ else None

    @property
    def key(self):
        return self.key if "key" in self.__dict__ else None

    def __setattr__(self, name: str, data):
        print("setatr base model", self.__class__, name, data)

        if name in ("key", "id", "_id"):
            if self.key:
                raise ValueError("`key` change is prohibited")
                return data
            else:
                print("self.__setattr__")
                super().__setattr__(name, str(data))

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

        super().__setattr__(name, data)

        return data

    @classmethod
    def __read__(cls, key: Union[str, int]):
        return cls.get_by_id(key)

    def __reread__(self, name: str, data):
        print("LOCAL MODEL __reread__(self, key, val):", name, data, "self >>", self)
        ...  #   needs to be implemented
        return


dbh.connect()


__all__ = ("dbh", "BaseModel")
