"""Security helpers for NShare."""

from __future__ import annotations

import base64
import secrets
from functools import wraps
from typing import Callable, Optional


def generate_csrf_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def require_basic_auth(username: str, password: str):
    """Require HTTP Basic Authentication.

    Args:
        username: The required username
        password: The required password
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(handler, *args, **kwargs):
            # Get Authorization header
            auth_header = handler.headers.get("Authorization")

            if auth_header and auth_header.startswith("Basic "):
                # Decode base64 credentials
                try:
                    encoded_credentials = auth_header.split(" ", 1)[1]
                    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
                    provided_username, provided_password = decoded_credentials.split(":", 1)

                    # Check credentials
                    if (secrets.compare_digest(provided_username, username) and
                        secrets.compare_digest(provided_password, password)):
                        return func(handler, *args, **kwargs)
                except (ValueError, UnicodeDecodeError):
                    pass

            # Send 401 with WWW-Authenticate header to trigger browser login
            handler.send_response(401)
            handler.send_header("WWW-Authenticate", 'Basic realm="NShare Admin"')
            handler.send_header("Content-Type", "text/html; charset=utf-8")
            handler.end_headers()
            handler.wfile.write(b"<html><body><h1>401 Unauthorized</h1><p>Admin authentication required.</p></body></html>")
            return None

        return wrapper
    return decorator


def require_token(expected_token):
    """Require authentication token.

    Args:
        expected_token: Either a string token, None, or a callable that returns Optional[str]
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(handler, *args, **kwargs):
            # If expected_token is callable, call it to get the actual token
            if callable(expected_token):
                actual_token = expected_token(handler)
            else:
                actual_token = expected_token

            # If no token required, allow access
            if actual_token is None:
                return func(handler, *args, **kwargs)

            # Get provided token from request
            provided = handler.headers.get("Authorization")
            if provided and provided.startswith("Bearer "):
                token = provided.split(" ", 1)[1]
            else:
                token = handler.get_token_from_request()

            # Compare tokens
            if token and secrets.compare_digest(token, actual_token):
                return func(handler, *args, **kwargs)

            # Unauthorized
            handler.send_response(401)
            handler.send_header("WWW-Authenticate", "Bearer")
            handler.end_headers()
            handler.wfile.write(b"Unauthorized")

        return wrapper

    return decorator
