# -*- coding:utf-8 -*-
"""
@Des: 中间件
"""

import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from core.Utils import random_str


class BaseMiddleware:
    """
    Middleware
    """

    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":  # 非http协议
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        req = Request(scope, receive, send)
        if not req.session.get("session"):
            req.session.setdefault("session", random_str())

        async def send_wrapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)
