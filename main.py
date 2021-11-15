import json 
from pathlib import Path
from models.location import Location

import fastapi
import uvicorn
import asyncio
from starlette.staticfiles import StaticFiles

from api import beerplace_api
from views import home 
from services import beerplace_service, review_service

api = fastapi.FastAPI()

def config():
    config_routing()
    #config_api_keys()
    config_static_files()
    config_fake_data()


def config_routing():
    api.include_router(home.router)
    api.include_router(beerplace_api.router)


def config_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        raise Exception('settings.json file not found.')
    
    with open('settings.json') as f:
        settings = json.load(f)
        beerplace_service.api_key = settings.get('api_key')


def config_static_files():
    api.mount('/static', StaticFiles(directory='static'), name='static')


def config_fake_data():
    loop = None 
    try:
        loop = asyncio.get_running_loop()
        print('Got loop!', loop)
    except RuntimeError:
        pass

    if not loop:
        loop = asyncio.get_event_loop()
    
    try:
        location1 = Location(city='Stockholm',
                             street_name='StureP',
                             street_number=321)
        name1 = 'Sveriges baksida'
        location2 = Location(city='Göteborg',
                             street_name='Avenyyyyn',
                             street_number=123)
        name2 = 'Goa gubbar'
        beerplace1 = asyncio.run(beerplace_service.add_beerplace(location1, name1))
        beerplace2 = asyncio.run(beerplace_service.add_beerplace(location2, name2))
        description1 = 'Lyxigt skit ställe'
        description2  = 'Redigt hak'
        rating1 = 1
        rating2 = 100
        asyncio.run(review_service.add_review(beerplace1, description1, rating1))
        asyncio.run(review_service.add_review(beerplace2, description2, rating2))
        #asyncio.gather(beerplace_service.add_beerplace_rating(beerplace1, rating1))
        #asyncio.gather(beerplace_service.add_beerplace_rating(beerplace2, rating2))

    except RuntimeError as re:
        raise Exception(f'Runtime error: {re}')


if __name__ == '__main__':
    config()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    config()
