####
##
# для сбора статистики быстро
#

import settings as sets
from db import BaseModel
from db.types import *
from peewee import CharField, BareField

print(Field)

ttt = Field(default=None, null=True)
# ttt.db_value(Json)


class Statistical(BaseModel):
    class Meta:
        # db_table: str = "statistical"
        only_save_dirty: bool = True
        pass

    value: Json = Field(default=None, null=True)
    # charfield: str = CharField(default=None, null=True)

    def __setattr__(self, name, data):
        super().__setattr__(name, data)
        # if self.is_dirty():
        if not name.startswith("_") and name not in ("key", "id", "_id"):
            print("stat attr change")
            # self.save(only=self.dirty_fields)
            self.save()

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


if sets.APP_DEV:
    Statistical.drop_table(safe=sets.APP_DEV)
    Statistical.create_table(safe=sets.APP_PROD)
