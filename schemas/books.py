from pydantic import BaseModel, ConfigDict, Field
from starlette.config import Config


class SBookBase(BaseModel):
    title: str
    year: int
    author: str
    pages: int = Field(gt=10)
    is_read: bool = False
class SBookAdd(SBookBase):
    pass

class RegisterUser(BaseModel):
    username: str
    password: int

class SBooks(SBookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)





