from sqlalchemy import create_engine
from __init__ import *
from settings import config, DSN
from db import meta


def create_tables(engine):
    meta.create_all(bind=engine)


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)
    print("You have just added all tables!")
