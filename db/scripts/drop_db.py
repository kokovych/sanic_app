from sqlalchemy import create_engine
from __init__ import *
from settings import config, DSN
from db import meta


def drop_tables(engine):
    meta.drop_all(bind=engine)


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    drop_tables(engine)
    print("All tables were successfully dropped!")
