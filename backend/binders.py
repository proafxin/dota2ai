"""
This module contains definitions of custom binders, used to bind request input
parameters into instances of objects, injected to request handlers.
"""

from blacksheep import FromHeader, Request
from blacksheep.server.bindings import Binder

from backend.domain.common import PageOptions


class IfNoneMatchHeader(FromHeader[str | None]):
    name = "If-None-Match"


class PageOptionsBinder(Binder):
    """
    Binds common pagination options for all endpoints implementing pagination of
    results. Collects and validates optional the following query parameters:

    - page, for page number
    - limit, for results per page
    - continuation_id, the last numeric ID that was read
    """

    handle = PageOptions

    async def get_value(self, request: Request) -> PageOptions:
        pages = request.query.get("page")
        limits = request.query.get("limit")
        continuation_ids = request.query.get("continuation_id")
        if pages is None or not isinstance(pages, list):
            page: str | int = 1
        else:
            page = pages[0]

        limit: int = 100
        if not limits or not isinstance(limits, list):
            limit = 100
        else:
            limit = int(limits[0])
        if isinstance(continuation_ids, list):
            continuation_id = int(continuation_ids[0])

        return PageOptions(page=page, limit=limit, continuation_id=continuation_id)
