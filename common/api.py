from sanic.response import json, text
from sanic.views import HTTPMethodView

from .validators import clean_user_data, registration_valid_data
from db.db import create_user


async def main_page(request):
    return text("Hello, world!")


class UserView(HTTPMethodView):

    async def post(self, request):
        db_conn = request.app.config.get('db')
        data = clean_user_data(request.json)
        async with db_conn.acquire() as conn:
            error_data = await registration_valid_data(data, conn)
            if error_data:
                return json({
                    "error": error_data
                }, status=400)
            await create_user(conn, data)
        return json({
            'data': 'User was successfully created!'
        }, status=201)


