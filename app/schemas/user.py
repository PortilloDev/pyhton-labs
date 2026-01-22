from pydantic import BaseModel

class UserListResponse(BaseModel):
    id: int
    name: str
    email: str