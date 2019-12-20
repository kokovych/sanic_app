from aiopg.sa import create_engine
from sanic import Sanic

from common.settings import config
from common.urls import setup_routes


app = Sanic(name=__name__)
setup_routes(app)


@app.listener('before_server_start')
async def prepare_db(app, loop):
    conf = config['postgres']
    engine = await create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app.config['db'] = engine


@app.listener('after_server_stop')
async def close_connection(app, loop):
    db = app['db']
    async with db.acquire() as conn:
        await conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,
            access_log=True, debug=True)
