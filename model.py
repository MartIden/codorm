from contracts import BaseModel


class Article(BaseModel):
    title: str
    description: str
    content: str


class Category(BaseModel):
    name: str
    description: str
