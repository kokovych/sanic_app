from sanic.response import json, text


async def main_page(request):
    return text("Hello, world!")
