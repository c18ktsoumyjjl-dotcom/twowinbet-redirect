# twowinbet-redirect

Render web service that 301-redirects every request on
`투윈평생주소.com` (`xn--9g4bomz9kg7b63s3kc.com`) and `www` to the same
path and query on `https://xn--tl3b69e9on9ortcdzvxwc.com`
(`투윈벳평생주소.com`).

`GET /healthz` returns 200 and is not redirected, for Render health checks.
