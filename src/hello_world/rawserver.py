from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Get Python version
        message = f'Hello World from Raw Python!'
        self.wfile.write(message.encode())


def run_raw(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000) -> None:
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting Raw Python server on port {port}...')
    httpd.serve_forever()