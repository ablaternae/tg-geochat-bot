####
##
#
#

import db
from db import BaseModel
from db.types import Optional, Any


class Statistical(BaseModel):
    class Config(BaseModel.Config):
        pass

    # key: str = PrivateAttr()
    # id: db.Optional[db.Union[str, None]]
    value: Optional[Any] = None

    # def __init__(self, *args, **data):
    #    super().__init__(**{"key": str(data.pop("key", args[0])), **data})
    #    return

    def __setattr__(self, name: str, data):
        # print(" __setattr__(self, key, val):", name, data, "self >>", self)

        if "key" == name:
            if self.key:
                raise ValueError("`key` change is prohibited")
                return
            else:
                self.__setattr__(name, str(data))

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

        return

    def val(self, name: str = None, data=None):
        if not name:
            return super().__dict__
        else:
            if data:
                self.__setattr__(name, data)
            else:
                if isinstance(name, dict):
                    super().__dict__.update(name)
                else:
                    raise LookupError

    # https://stackoverflow.com/questions/63264888/pydantic-using-property-getter-decorator-for-a-field-with-an-alias
    # https://github.com/pydantic/pydantic/issues/1577

    pass
