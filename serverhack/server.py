import http.server
import socketserver

class MyHTTPServer:
    def __init__(self, port=8080):
        self.port = port

    def start_server(self):
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", self.port), handler) as httpd:
            print(f"Server started at port {self.port}")
            httpd.serve_forever()
