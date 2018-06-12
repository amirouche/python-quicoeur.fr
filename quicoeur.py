from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_jinja2 import render_template as render


ROOT = Path(__file__).parent.resolve()


def pk(*args):
    print(args)
    return args[-1]


async def index(request):
    messages = request.app['messages']
    return render('index.jinja2', request, dict(messages=messages))


async def new_get(request):
    return render('new.jinja2', request, dict())


async def new_post(request):
    data = await request.post()
    assert data.get('title')
    assert data.get('body')
    request.app['messages'].append(data)
    raise web.HTTPFound('/')


app = web.Application()
app['messages'] = list()

aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(ROOT / 'templates'))
)


app.add_routes([web.get('/', index)])
app.add_routes([web.get('/new', new_get)])
app.add_routes([web.post('/new', new_post)])
app.add_routes([web.static('/static', str(ROOT / 'static'), show_index=True)])
web.run_app(app)
