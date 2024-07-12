from typing import Any

from robyn import Request, SubRouter

router: SubRouter = SubRouter(file_object=__name__, prefix="/heroes")


@router.get(endpoint="/populate")  # type: ignore
async def populate(request: Request, global_dependencies: dict[str, Any]) -> str:
    print(global_dependencies["mongo_client"])
    return "Hello world"
