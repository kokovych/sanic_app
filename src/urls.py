from .api import main_page, UserView


def setup_routes(app):
    app.add_route(main_page, '/')
    app.add_route(UserView.as_view(), '/api/user/')
