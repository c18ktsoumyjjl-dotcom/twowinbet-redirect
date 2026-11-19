"""301-redirect 투윈평생주소.com -> 투윈벳평생주소.com, preserving path and query."""

DEST = "https://xn--tl3b69e9on9ortcdzvxwc.com"


def app(environ, start_response):
    path = environ.get("PATH_INFO") or "/"
    query = environ.get("QUERY_STRING") or ""

    if path == "/healthz":
        body = b"ok"
        start_response(
            "200 OK",
            [
                ("Content-Type", "text/plain; charset=utf-8"),
                ("Content-Length", str(len(body))),
            ],
        )
        return [body]

    if not path.startswith("/"):
        path = "/" + path
    while path.startswith("//"):
        path = path[1:]

    location = DEST + path
    if query:
        location += "?" + query

    start_response(
        "301 Moved Permanently",
        [
            ("Location", location),
            ("Content-Length", "0"),
            ("Cache-Control", "no-store"),
        ],
    )
    return [b""]
