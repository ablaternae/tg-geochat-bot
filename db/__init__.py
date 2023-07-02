####
##
#
#

# from settings import APP_PROD, DETA_BASE_KEY
import settings as sets

# if sets.APP_DEV:
#    from .base_model_local import BaseModel, Field
# else:
#    from .base_model import BaseModel, Field

from .base_model import BaseModel, Field


from sys import maxsize as MAX_INT

MIN_INT = -MAX_INT - 1

from pydantic import ValidationError
from pydantic import ValidationError as FieldValidationError
from pydantic import validator

from . import types

types.Field = Field
