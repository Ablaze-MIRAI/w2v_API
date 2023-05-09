from typing import Union
from pydantic import BaseModel


class Prompt(BaseModel):
    positive: Union[list[str], list[None]]
    negative: Union[list[str], list[None]]
