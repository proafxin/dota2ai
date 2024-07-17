from blacksheep import Application
from rodi import Container

from api.auth import configure_authentication
from api.dependencies import client, configure_dependencies
from api.errors import configure_error_handlers
from api.routers.heroes import all as all_heroes
from api.routers.heroes import images as all_hero_images
from api.routers.heroes import populate_details as populate_hero_details
from docs import configure_docs


def configure_routes(app: Application) -> None:
    app.router.add_post("/populate/details", populate_hero_details)
    app.router.add_get("/heroes", all_heroes)
    app.router.add_get("/heroes/images", all_hero_images)


def shut_down(app: Application) -> None:
    client.close()


def configure_application(services: Container) -> Application:
    app = Application(services=services, show_error_details=True)

    configure_error_handlers(app)
    configure_authentication(api=app)
    configure_docs(api=app)
    configure_routes(app=app)

    return app


app = configure_application(services=configure_dependencies())
app.on_stop += shut_down
