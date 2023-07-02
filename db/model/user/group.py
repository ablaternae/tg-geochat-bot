####
##
#
#
from datetime import datetime, timedelta

from db import UUID, Any, BaseModel, List, Optional


class Group(BaseModel):
    from .user import User

    name: str
    joined: datetime.timestamp
    user_id: Optional[List[User]]

    def __init__(self, params):
        """
        Constructor
        """
