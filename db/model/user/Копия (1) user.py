####
##
#
#

from db.model import (BaseModel, Field, FieldInfo, FieldValidationError,
                      validator)
from db.types import *

# from .group import Group

# https://stackoverflow.com/questions/72702693/how-to-get-separately-column-from-sqlalchemy-relationship-using-pydantic-schema


class User(BaseModel):
    from . import Profile

    class Config(BaseModel.Config):
        underscore_attrs_are_private: bool = True
        property_set_methods = {"profiles": "set_profiles", "key": "set_key"}
        # property_set_methods = {"profiles": "set_profiles"}

    # id = Field(alias='key')
    name: str = None
    profile_id: Optional[List[Union[str, int]]] = list()
    _profiles: Optional[List[Profile]] = Field(alias="profiles", default=list())
    _accounts: Optional[List[Profile]] = Field(
        alias="accounts", alias_priority=1, default=list()  # , exclude=True
    )

    # @key.setter
    def set_key(self, data):
        # from collections.abc import Iterable
        # isinstance(self._profiles, Iterable)
        print("KEY setter", self.__class__, self.key, self._profiles, self._accounts)
        if data:
            # print(data, self.key)
            map(
                lambda elem: setattr(elem, 'user_id', data),
                (
                    self._profiles
                    if hasattr(self._profiles, '__iter__')
                    else self._profiles.default[:]
                ),
                (
                    self._accounts
                    if hasattr(self._accounts, '__iter__')
                    else self._accounts.default
                ),
            )

            for elem in self.profiles:
                elem.user_id = self.key
                print(elem)
            print('self._profiles', self._profiles)
        return

    # @validator("key", check_fields=False)
    def key_validator(cls, data, values, field, config):
        print("KEY validator >>>", data, field.default, super().__dict__['key'])
        if data:
            for elem in super()._profile:
                elem.user_id = data
            # map(lambda elem: (elem.user_id=data) or data, self._profile)
        # return data or field.default
        return data

    @validator("profiles", always=True, check_fields=False, pre=True)
    # , pre=True)  # , always=True)
    def profiles_validator(cls, data, values, field, config):
        print("profiles_validator", cls, data, values, field, config, "///end")
        ...
        # return data or (field.default if hasattr(values, "default") else list())
        return data or field.default

    @property
    def profiles(self):
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
