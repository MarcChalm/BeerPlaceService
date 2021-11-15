from typing import Optional, List
from pydantic import BaseModel 
import pydantic
import re


class Location(BaseModel):
    country: str = 'Sverige'
    city: str
    street_name: str
    street_number: int
    post_code: Optional[int] = None
    area: Optional[str] = None
    long: Optional[str] = None
    lat: Optional[str] = None


    @pydantic.validator('street_name')
    @classmethod
    def street_name_without_numbers(cls, street_name):
        not_valid_condition = re.findall(r'[^A-Öa-ö]', street_name.replace(' ', ''))
        if not_valid_condition:
            raise Exception('Street name must be only characters, no numbers ([A-Öa-ö]).')
        else:
            return street_name

    
    @pydantic.validator('street_number')
    @classmethod
    def street_numbers_bound(cls, street_number):
        if street_number < 0 or street_number > 10000:
            raise Exception('Unrealistic street number. Max set at 10000.')
        else:
            return street_number

    # TODO: Probably need some good way of validating long/lat..


class BeerPlace(BaseModel):
    id: str
    name: str
    location: Location
    ratings: List[int] = []
    average_rating: Optional[float] = None


    @pydantic.validator('average_rating')
    @classmethod
    def average_rating_boud(cls, average_rating):
        if average_rating:
            if average_rating < 0 or average_rating > 100:
                raise Exception('Average rating must be between 0-100. Some calculation went wrong')
            else:
                return average_rating
        else: 
            return None