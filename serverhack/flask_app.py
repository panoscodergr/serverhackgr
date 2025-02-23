from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class FlaskApp:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper

    def run(self, host='localhost', port=5000):
        server = HTTPServer((host, port), self.handle_request)
        print(f"Flask-like app running on {host}:{port}")
        server.serve_forever()

    def handle_request(self, request, client_address, server):
        method = request.command
        path = request.path
        response = self.routes.get(path, self.not_found)
        response(request)

    def not_found(self, request):
        request.send_response(404)
        request.end_headers()
        request.wfile.write(b"404 Not Found")
