from datetime import datetime

from aiohttp import web


async def index_handler(request):
    return web.Response(text='Time: {}'.format(datetime.now()))


app = web.Application()
app.router.add_route('GET', '/', index_handler)


if __name__ == '__main__':
    web.run_app(app)
