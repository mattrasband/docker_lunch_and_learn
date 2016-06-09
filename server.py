#!/usr/bin/env python

from datetime import datetime

from aiohttp import web


app = web.Application()


async def date_handler(request):
    now = datetime.now().isoformat()
    return web.Response(text='Time Is Now: {}'.format(now))


app.router.add_route('GET', '/', date_handler)


if __name__ == '__main__':
    web.run_app(app)
