from __future__ import annotations

import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from src.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        request_id = getattr(
            request.state,
            "request_id",
            "N/A",
        )

        client_ip = (
            request.client.host
            if request.client
            else "Unknown"
        )

        logger.info("=" * 70)
        logger.info(f"Request ID : {request_id}")
        logger.info(f"Method     : {request.method}")
        logger.info(f"Endpoint   : {request.url.path}")
        logger.info(f"Client IP  : {client_ip}")
        logger.info(f"Status     : {response.status_code}")
        logger.info(f"Duration   : {elapsed:.2f} ms")
        logger.info(
            f"User-Agent : {request.headers.get('User-Agent','Unknown')}"
        )
        logger.info("=" * 70)

        return response