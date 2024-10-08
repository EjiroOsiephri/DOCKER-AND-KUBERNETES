from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Docker!")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), MyHandler)
    print("Starting server on port 80...")
    server.serve_forever()
