from urllib.parse import parse_qsl


def get_body_params(body: bytes) -> dict:
    """Parse a params string and return a dict."""
    body_string = body.decode()
    return dict(parse_qsl(body_string))
