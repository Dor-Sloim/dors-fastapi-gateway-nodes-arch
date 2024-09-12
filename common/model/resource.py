from pydantic import BaseModel


class Resource(BaseModel):
    message: str
