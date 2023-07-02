####
##
#
#


from db.model import BaseModel, Field
from db.model.user import *
from db.types import *

# User = ForwardRef('user.User')


class Profile(BaseModel):
    class Config(BaseModel.Config):
        property_set_methods = {"user_id": "set_user_id"}

    name: str = None
    joined: Optional[datetime] = Field(
        default_factory=lambda: int(datetime.timestamp(datetime.utcnow()))
    )
    description: Optional[str] = None
    user_id: Optional[Union[str, int]] = None
    _user: Optional[User] = Field(alias="user", default=None)
    # _user: Optional[Any] = Field(alias="user", default=None)

    # @property
    def get_user_id(self):
        return self.user_id

    # @user_id.setter
    def set_user_id(self, data: str):
        print("set_user_id(self, data: str):", data)
        super().__dict__["user_id"] = str(data)
        super().__dict__["_user"] = User(key=self.user_id)


# User.update_forward_refs()
