####
##
#
#
from datetime import datetime, timedelta, timestamp

from pydantic import UUID4 as UUID
from pydantic import Any, List, Optional

from db import BaseModel


class Counter(BaseModel):
    from .user import User

    name: str

    joined: timestamp
    user_id: Optional[List[User]]

    def __init__(self, params):
        """
        Constructor
        """
