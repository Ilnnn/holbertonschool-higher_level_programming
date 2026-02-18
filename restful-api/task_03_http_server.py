#!/usr/bin/python3
"""
Simple API using Python's http.server module.
Endpoints:
- /         → Welcome message
- /data     → Returns sample JSON data
- /status   → Returns API status
Other endpoints → 404 Not Found
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API."""

    def _send_headers(self, status_code=200, content_type="text/plain"):
        """Helper to send HTTP headers."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""

        if self.path == "/":
            self._send_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            data = {"status": "OK"}
            self._send_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        else:
            data = {"error": "Endpoint not found"}
            self._send_headers(404, "application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))


def run_server():
    """Start the HTTP server."""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
