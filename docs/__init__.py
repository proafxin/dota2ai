"""
This module contains OpenAPI Documentation definition for the API.

It exposes a docs object that can be used to decorate request handlers with additional
information, used to generate OpenAPI documentation.
"""

from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

from docs.binders import set_binders_docs
from dota2ai.about import VERSION


def configure_docs(api: Application) -> None:
    docs = OpenAPIHandler(info=Info(title="Dota 2 AI", version=VERSION), anonymous_access=True)

    set_binders_docs(docs)
    docs.bind_app(api)
