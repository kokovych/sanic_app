from aiopg.sa import create_engine
from sanic.response import json, text
from sanic.views import HTTPMethodView

from src.db.model import create_user
from .constants import (EMPTY_ERROR, USER_SUCCESS_CREATION)
from .validators import clean_user_data, registration_valid_data


async def main_page(request):
    return text("Hello, world!")


class UserView(HTTPMethodView):

    async def post(self, request):
        db_conn = request.app.config.get('db_conn')
        data = request.json
        if not data:
            return json(body=EMPTY_ERROR, status=400)
        data = clean_user_data(request.json)
        async with create_engine(db_conn) as engine:
            async with engine.acquire() as conn:
                error_data = await registration_valid_data(data, conn)
                if error_data:
                    return json({
                        "error": error_data
                    }, status=400)
                await create_user(conn, data)

        return json(body=USER_SUCCESS_CREATION, status=201)
