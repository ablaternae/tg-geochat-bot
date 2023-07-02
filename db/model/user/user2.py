####
##
#
#

from db.model import (BaseModel, Field, FieldInfo, FieldValidationError,
                      validator)
from db.types import *

# https://stackoverflow.com/questions/72702693/how-to-get-separately-column-from-sqlalchemy-relationship-using-pydantic-schema


class User(BaseModel):
    class Config(BaseModel.Config):
        underscore_attrs_are_private: bool = True
        property_set_methods = {"profiles": "set_profiles", "key": "set_key"}
        # property_set_methods = {"profiles": "set_profiles"}

    # id = Field(alias='key')
    name: str = None
    profiles_id: Optional[List[Union[str, int]]] = list()
    # _profiles: Optional[List['Profile']] = Field(default=[])
    # _profiles: Optional[List['Profile']] = Field(alias="profiles", default=[])
    # _accounts: Optional[List[Account]] = Field(alias="accounts", default=[])

    # @property
    # def key(self):
    #    return self.key

    # @key.setter
    def set_key(self, data):
        # from collections.abc import Iterable
        # isinstance(self._profiles, Iterable)
        # print("KEY setter", self.__class__, self.key, self._profiles, self._accounts)

        if data:
            # print(data, self.key)

            for elem in self.profiles:
                elem.user_id = self.key
                # print(elem)
            print("self._profiles", self._profiles)
        return

    # @validator("key", check_fields=False)
    def key_validator(cls, data, values, field, config):
        print("KEY validator >>>", data, field.default, super().__dict__["key"])
        if data:
            for elem in super()._profile:
                elem.user_id = data
            # map(lambda elem: (elem.user_id=data) or data, self._profile)
        # return data or field.default
        return data

    @validator("profiles_id", always=True, pre=True)
    def profiles_id_validator(cls, data, values, field, config):
        print("profiles ID", cls, data, values, field, "///end")
        if data:
            self._profiles = [Profiles.get_or_none(key) for key in data]
            return True

    @validator("profiles", always=True, check_fields=False, pre=True)
    # , pre=True)  # , always=True)
    def profiles_validator(cls, data, values, field, config):
        print("profiles_validator", cls, data, values, field, config, "///end")
        ...
        # return data or (field.default if hasattr(values, "default") else list())
        return data or field.default

    @property
    def profiles(self):
        from db.model.user import Profile

        print('profiles GET')
        return [Profile.get_or_none(i) for i in self.profiles_id]

        print(isinstance(self._profiles, FieldInfo))
        print(self._profiles)
        self._profiles = [Profile.get_or_none(i) for i in self.profiles_id]
        return (
            self._profiles
            if not isinstance(self._profiles, FieldInfo)
            else self._profiles.default
        )

    @profiles.setter
    def set_profiles(self, data):
        ...
        print("setprofile", data)
        return list()
