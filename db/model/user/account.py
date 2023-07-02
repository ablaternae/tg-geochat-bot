####
##
#
#
from db.model import *
from db.types import *


class Account(BaseModel):
    from .user import User

    name: str

    joined: datetime = None
    user_id: Optional[List[User]]

    def __init__(self, params):
        """
        Constructor
        """
