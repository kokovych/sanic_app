from sanic.response import json, text
from sanic.views import HTTPMethodView

from .validators import create_user_validation


async def main_page(request):
    return text("Hello, world!")


class UserView(HTTPMethodView):
    async def post(self, request):
        db_conn = request.app.config.get('db')
        data = request.json
        is_valid = create_user_validation(data)
        if is_valid:
            async with db_conn.acquire() as conn:
                print(conn)
            return json({
                "data": 1
            })
        return json({
            'data': "error"
        })

