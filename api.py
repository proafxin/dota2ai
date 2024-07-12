from robyn import Robyn

from backend.db.connect import client
from backend.routers.heroes import router as heroes_router

api = Robyn(__file__)


def inject_dependencies(api: Robyn) -> None:
    api.inject_global(mongo_client=client)  # type: ignore


def include_routers(api: Robyn) -> None:
    api.include_router(router=heroes_router)  # type: ignore


async def startup_handler() -> None:
    inject_dependencies(api=api)
    include_routers(api=api)


async def shutdown_handler() -> None:
    client.close()


api.startup_handler(handler=startup_handler)
api.shutdown_handler(handler=shutdown_handler)

if __name__ == "__main__":
    api.start(port=8000, host="0.0.0.0")
