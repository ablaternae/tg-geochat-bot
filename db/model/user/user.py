####
##
#
#
# from typing import ForwardRef
from db.model import (
    BaseModel,
    Field,
    FieldInfo,
    FieldValidationError,
    validator,
    root_validator,
)
from db.model.user import *
from db.types import *

# https://stackoverflow.com/questions/72702693/how-to-get-separately-column-from-sqlalchemy-relationship-using-pydantic-schema


class User(BaseModel):
    class Config(BaseModel.Config):
        underscore_attrs_are_private: bool = True
        # property_set_methods = {"profiles": "set_profiles"}

    # id: Union[str, int] = Field(alias="key", default=None)
    info: Union[Json, Dict, List] = None
    added_to_attachment_menu = None
    can_join_groups = None
    can_read_all_group_messages = None
    first_name: str = None
    id: Union[str, int] = None
    is_bot: bool = None
    is_premium: bool = None
    language_code: str = None
    last_name: str = None
    supports_inline_queries = None
    username: str = None  # @username

    # @root_validator()
    # def validate_all(cls, values):
    #    print('validator', values)
    #    return values

    @classmethod
    def add_tg_user(cls, tguser):
        cls(key=tguser.id, info=tguser.to_dict(), **(tguser.to_dict())).save()

        pass
