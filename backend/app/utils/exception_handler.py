from __future__ import annotations

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

from src.utils.logger import logger


def register_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):

        logger.error(
            f"{request.method} {request.url} -> {exc.detail}"
        )

        return JSONResponse(

            status_code=exc.status_code,

            content={

                "success": False,

                "error": exc.detail,

            },

        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):

        logger.exception(exc)

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "error": "Internal Server Error",

                "message": str(exc),

            },

        )