from blacksheep import Application
from rodi import Container

from backend.auth import configure_authentication
from backend.dependencies import configure_dependencies
from backend.errors import configure_error_handlers
from backend.routers.heroes import populate_details
from docs import configure_docs


def configure_routes(api: Application) -> None:
    api.router.add_post("/populate/details", populate_details)


def configure_application(services: Container) -> Application:
    api = Application(services=services, show_error_details=True)

    configure_error_handlers(api)
    configure_authentication(api=api)
    configure_docs(api=api)
    configure_routes(api=api)

    return api


api = configure_application(services=configure_dependencies())
