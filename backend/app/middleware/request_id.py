from __future__ import annotations

from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class RequestIDMiddleware(BaseHTTPMiddleware):

    async def dispatch(

        self,

        request: Request,

        call_next,

    ):

        request.state.request_id = str(

            uuid4()

        )

        response = await call_next(

            request

        )

        response.headers[

            "X-Request-ID"

        ] = request.state.request_id

        return response