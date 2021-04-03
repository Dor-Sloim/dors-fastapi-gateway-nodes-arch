from pydantic import BaseModel


class Node(BaseModel):
    hostname: str
    port: str
