from pydantic import BaseModel


class SERPResult(BaseModel):

    rank: int
    url: str
    title: str
    snippet: str