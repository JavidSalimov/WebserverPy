import http.server as hs
hs.HTTPServer(('127.0.0.1', 1989),hs.SimpleHTTPRequestHandler).serve_forever()


# python -c "import http.server as hs; hs.HTTPServer(('127.0.0.1', 8888), hs.SimpleHTTPRequestHandler).serve_forever()"