from sanic import Sanic

from src.settings import config
from src.urls import setup_routes
from src.constants import POSTGRES_CONN_STR


app = Sanic(name=__name__)
setup_routes(app)


@app.listener('before_server_start')
def prepare_db(app, loop):
    conf = config['postgres']
    connection = POSTGRES_CONN_STR.format(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host']
    )
    app.config['db_conn'] = connection

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,
            access_log=True, debug=False)
