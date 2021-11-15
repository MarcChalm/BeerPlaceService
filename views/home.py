import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from services import review_service

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()

@router.get('/')
async def index(request: Request):
    events = await review_service.get_reviews()
    data = {'request': request, 'events': events}
    
    return templates.TemplateResponse('home/index.html', data)

@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')