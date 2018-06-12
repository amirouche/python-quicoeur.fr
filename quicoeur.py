from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_jinja2 import render_template as render


def pk(*args):
    print(args)
    return args[-1]


ROOT = Path(__file__).parent.resolve()


async def hello(request):
    return render('index.jinja2', request, dict())


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(ROOT / 'templates')))

app.add_routes([web.get('/', hello)])
web.run_app(app)
