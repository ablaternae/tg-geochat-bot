####
##
#
#

from pydantic import BaseModel, PrivateAttr

import db
from db import BotModel


class Statistical(BotModel):
    # key: str = PrivateAttr()
    value: db.Optional[db.Union[db.Json, db.Any, str, int, None]] = None
    # desc: db.Optional[str]

    def __init__(self, *args, **data):
        super().__init__(**data)
        # We generate the value for our private attribute
        self.key = data.pop("key", None)
        if "value" in data and len(data) == 1:
            # self.value = data.pop("value", {})
            self.value = data["value"]
        else:
            self.value = args if args else data

        #   str(randint(1, db.MAX_INT))

    @property
    def key(self):
        return self.__dict__["key"] if "key" in self.__dict__ else None

    #    @key.setter
    #    def key(self, data):
    #        print('key setter')
    #        self.__dict__["key"] = data

    @property
    def value(self):
        return self.__dict__["value"] if "value" in self.__dict__ else {}

    # return super().__getattr__("value")

    # @value.setter
    # def value(self, data):
    #    self.__dict__["value"] = data

    # def __getattr__(self, name: str):
    #    if name.lower() == "value":
    #        print("self.value == ", self.value)
    #        return self.value
    #    if name in self.value:
    #        return self.value[name]

    def __setattr__(self, name: str, data):
        print("__setattr__(self, name: str, data)", name, data)

        if name.lower() == "value":
            print("value==", data)
            self.__dict__["value"] = data
            # super().__setattr__("value", data)
            print("data=====", self)
            self.save()
            print("SAVE=====", self)
            return

        if name.lower() == "key":
            # если раньше не было
            if self.key is None and data:
                super().__setattr__("key", data)
                # далее читаем данные
                self.get_or_none(self.key)
            return

        print("self.key >>>", self.key, data, self.get)

        # быстрое синхронное обновление записи по ключу
        # s1 = self.get(self.key)
        #        s1 = self.__class__.__db__.get(self.key).pop('value', {})
        #
        #        s2 = {name: data}
        #
        #        print('s1==', s1, 's2==', s2)
        #        print('dict s1==', dict(s1))
        #
        #        s3 = {**s1, **s2}
        #        print('s3333333===', s3)
        #
        #        s4 = self.__class__.__db__.put({'value': s3}, key=self.key)
        #
        #        print('s444', s4)
        #
        #        return
        tmp = self.__class__.__db__.put(
            data={
                "value": dict(
                    self.__class__.__db__.get(self.key).pop("value", {}), **{name: data}
                )
            },
            key=self.key,
            # data={
            #     **(self.get(self.key) if self.key else {}),
            #     **{name: data},
            # },
        )
        self.key = tmp.pop("key", None)
        self.__dict__["value"] = tmp.pop("value", {})

        return

    pass
