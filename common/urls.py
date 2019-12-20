from .api import main_page


def setup_routes(app):
    app.add_route(main_page, '/')
