from sqlalchemy import MetaData, Table, Column, Integer, String, Sequence
from sqlalchemy.sql.expression import select, insert

meta = MetaData()

USER_ID = Sequence('user_id_seq', start=1)

users = Table(
    'users', meta,
    Column('id', Integer, USER_ID, primary_key=True, server_default=USER_ID.next_value()),
    Column('email', String(255), nullable=False, unique=True),
    Column('password', String(255), nullable=False),
)


def get_user_fields():
    user_columns_list = users.columns
    results = []
    for i in user_columns_list:
        results.append(i.name)
    if 'id' in results:
        results.remove('id')
    return results


async def get_user_by_email(conn, email):
    cursor = await conn.execute(
        select([users]).where(users.c.email == email)
    )
    result = await cursor.fetchall()
    return result

async def create_user(conn, user_data):
    cursor = await conn.execute(insert(users).values(user_data))
    result = await cursor.fetchall()[0][0]
    # todo: create token for user after creation
