import asyncio
import os

from aiohttp import web
from aiopg import create_pool


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

pool = loop.run_until_complete(create_pool(os.environ['DATABASE_URL']))


async def index_handler(request):
    with await pool.cursor() as cur:
        await cur.execute('SELECT 42')
        return web.Response(text=str(await cur.fetchone()))


app.router.add_route('GET', '/', index_handler)


if __name__ == '__main__':
    web.run_app(app)

