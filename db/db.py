from sqlalchemy import MetaData, Table, Column, Integer, String, Sequence

meta = MetaData()

USER_ID = Sequence('user_id_seq', start=1)

users = Table(
   'users', meta,
   Column('id', Integer, USER_ID,  primary_key=True, server_default=USER_ID.next_value()),
   Column('email', String(255), nullable=False, unique=True),
   Column('password', String(255), nullable=False),
)
