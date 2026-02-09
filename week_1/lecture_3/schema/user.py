from pydantic import BaseModel
class UserSchema(BaseModel):
    username: str
    password: str
    is_enabled: bool

class UserschemaResponse(BaseModel):
    username: str
    