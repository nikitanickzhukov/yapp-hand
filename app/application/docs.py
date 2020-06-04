from falcon_swagger_ui import register_swaggerui_app

from application.config import SWAGGER


def add_docs(url, schema_url, app):
    register_swaggerui_app(app, url, schema_url, **SWAGGER)


__all__ = ('add_docs',)
