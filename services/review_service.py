from datetime import datetime
from typing import List
from models.reviews import Review
from models.location import BeerPlace
from uuid import uuid4

__reports: List[Review] = []


async def get_reviews() -> List[Review]:
    return list(__reports)[::-1]


async def add_review(beerplace: BeerPlace, description: str, rating: int):
    review = Review(id=str(uuid4),
                    created_at=datetime.now(),
                    beerplace=beerplace,
                    description=description,
                    rating=rating)
    
    # Saving localy unti I have a DB
    __reports.append(review)
    return review
