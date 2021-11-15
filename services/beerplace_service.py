from typing import Optional, Tuple, List
from uuid import uuid4
from models.location import BeerPlace, Location
import httpx
import random

api_key: Optional[str] = None
__beerplaces: List[BeerPlace] = []


async def get_beerplaces_async() -> List[BeerPlace]:
    return list(__beerplaces)

async def get_random_beerplace_async() -> BeerPlace:
    if __beerplaces:
        return __beerplaces[random.randrange(len(__beerplaces))]
    else: 
        return []

async def add_beerplace(location: Location, name: str):
    beerplace_exist = list(filter(lambda bp: bp.name==name, __beerplaces))
    if not beerplace_exist:
        beerplace = BeerPlace(id=str(uuid4()), name=name, location=location)
        # Saving localy unti I have a DB
        __beerplaces.append(beerplace)
    else:
        beerplace = beerplace_exist[0]
    return beerplace

async def add_beerplace_rating(name: str, rating: int):
    beerplace = list(filter(lambda bp: bp.name==name, __beerplaces))
    if beerplace:
        beerplace[0].ratings.append(rating)
        beerplace[0].average_rating = sum(beerplace[0].ratings)
    else:
        raise Exception('Found no beerplace with that name. Add it to the list first!')