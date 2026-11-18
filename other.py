
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, Field, SecretStr


class User(BaseModel):
    id: Field
    username: Annotated(str, Field(min_length=3))
    password: SecretStr
    email: EmailStr
    phone: Annotated(str, Field(min_length=10))
    

class User(BaseModel):
    name:str 
    age: int | None = None
    hobby: list[str] = Field(default_factory=list)
    is_loyal: bool | None

