## Simple sanic application

Used python 3.5+ (3.7), postgres 11. 

#### Preparation

1. Create and activate virtual environment:

```sh 
$ virualenv -p python3 venv
$ source venv/bin/activate
```

2. Install requirements:
```
(venv)$ pip install  -r requirements.text
```

3. Create database and database user:

```
$ psql -U postgres -h localhost
> CREATE DATABASE <DB_NAME_HERE>;
> CREATE USER <USERNAME_HERE> WITH PASSWORD 'password_here';
> GRANT ALL PRIVILEGES ON DATABASE <DB_NAME_HERE> TO <USERNAME_HERE>;

```

#### Run

For start project:

```
(venv)$ python main.py
```

#### Database migration
1. You need to initialize database with next command:
```
(venv)$ python db/scripts/init_db.py
```
This step will create table(tables) from `db/db.py`

Additional. Alembic init: 
`alembic init alembic` - create dir `alembic` and some conf files.

2. For migration I used `alembic`. 


So, for a next step you need to say for alembic 
that you will make any changes in database from this state:

```
(venv)$ alembic stamp head
```

3. If you add(remove) fields from database table, 
need to create migration file and implement this migration.
- This command will create python file with database changes:
```
(venv)$ alembic revision --autogenerate -m "some msg here"
```

- This one implement database changes : 

```
(venv)$ alembic upgrade head
```


##### Run tests

```
(venv)$ pytest -vs
```

##### Check code style
```
(venv)$ flake8
```
