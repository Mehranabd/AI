"""A dependency-free demo server for testing the cloud environment."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b'<!doctype html><html lang="en"><meta charset="utf-8"><title>Cloud demo</title><h1>It works!</h1><p>Your Python cloud environment is running.</p><a href="/health">Check health</a></html>'
            content_type = "text/html; charset=utf-8"
        elif self.path == "/health":
            body = json.dumps({"status": "ok"}).encode()
            content_type = "application/json"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("Starting demo on port 8000", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
