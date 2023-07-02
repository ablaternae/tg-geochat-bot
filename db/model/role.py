####
##
#
#
from datetime import datetime, timedelta, timestamp

from pydantic import UUID4 as UUID
from pydantic import Any, List, Optional

from db import BaseModel


class Role(BaseModel):
    pass


class RoleList(BaseModel):
    pass
