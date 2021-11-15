from models.reviews import ReviewSubmittal
from models.reviews import Review
import fastapi
from typing import Optional, List
from models.location import BeerPlace, Location
from services import review_service, beerplace_service

router = fastapi.APIRouter()

@router.get('/api/random_beerplace')
async def random_beerplace():
    try:
        return await beerplace_service.get_random_beerplace_async()
    except Exception as x:
        return fastapi.Resoponse(content=str(x), status_code=500)


@router.get('/api/beerplaces', name='all_beerplaces')
async def beerplaces_get() -> List[BeerPlace]:
    return await beerplace_service.get_beerplaces_async()


@router.post('api/beerplaces', name='add_beerplaces', status_code=201)
async def beerplaces_post(location: Location, name: str) -> BeerPlace:
    # SOME THINGS 
    return await beerplace_service.add_beerplace(location, name)


@router.get('/api/reviews', name='all_reviews')
async def reports_get() -> List[Review]:
    return await review_service.get_reviews_async()


@router.post('api/reviews', name='add_review', status_code=201)
async def reviews_post(review_subittal: ReviewSubmittal) -> Review:
    # SOME THINGS 
    description = review_subittal.description
    beerplace = review_subittal.beerplace
    rating = review_subittal.rating
    return await review_service.add_review(description, beerplace, rating)