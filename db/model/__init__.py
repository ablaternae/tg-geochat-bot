####
##
#
#

# распаковка словаря
# books = [Model(**json_item) for json_item in json_data]

from pydantic import Field
from pydantic import ValidationError
from pydantic import ValidationError as FieldValidationError
from pydantic import validator, root_validator
from pydantic.fields import FieldInfo

from db import types

from db import BaseModel
from .stat import Statistical

# from .user.user import User

# from .user.profile import Profile

# from odetam import DetaModel
# from odetam.async_model import AsyncDetaModel as DetaModel
# https://github.com/rickh94/ODetaM
