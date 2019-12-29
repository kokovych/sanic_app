from sanic import Sanic
import pytest
from sqlalchemy import create_engine as create_engine_sa

from src.constants import POSTGRES_CONN_STR
from src.settings import test_config, DSN
from src.db.scripts.drop_db import drop_tables
from src.db.scripts.init_db import create_tables
from src.urls import setup_routes


@pytest.yield_fixture(scope="module")
def app_test():
    app = Sanic(name="test_app")
    setup_routes(app)

    db_url = DSN.format(**test_config['postgres'])
    engine_sa = create_engine_sa(db_url)
    create_tables(engine_sa)

    conf = test_config['postgres']

    connection = POSTGRES_CONN_STR.format(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host']
    )
    app.config['db_conn'] = connection

    yield app

    print("Dropping test tables...")
    drop_tables(engine_sa)


@pytest.fixture
def test_cli(loop, app_test,  sanic_client):
    return loop.run_until_complete(sanic_client(app_test))
