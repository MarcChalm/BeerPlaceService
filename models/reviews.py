from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import pydantic
from models.location import BeerPlace


class ReviewSubmittal(BaseModel):
    beerplace: BeerPlace
    description: str
    rating: int

    @pydantic.validator('rating')
    @classmethod
    def rating_boud(cls, rating):
        if rating < 0 or rating > 100:
            raise Exception('Rating must be between 0-100.')
        else:
            return rating


class Review(ReviewSubmittal):
    id: str
    created_at: datetime