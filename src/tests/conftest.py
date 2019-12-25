from sanic import Sanic
import pytest
from aiopg.sa import create_engine
from sqlalchemy import create_engine as create_engine_sa

from src.settings import test_config, DSN
from src.db.scripts.drop_db import drop_tables
from src.urls import setup_routes


@pytest.yield_fixture(scope='module')
def app_test():
    print('start app_test')
    app_test = Sanic(name=__name__)
    setup_routes(app_test)
    conf = test_config['postgres']
    engine = create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )
    app_test.config['test_db'] = engine
    yield app_test
    db = app_test.config.get('test_db')
    if db:
        print('closing db...')
        db.close()


@pytest.fixture()
def drop_test_db():
    db_url = DSN.format(**test_config['postgres'])
    engine = create_engine_sa(db_url)
    drop_tables(engine)
