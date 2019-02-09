from http.server import HTTPServer, BaseHTTPRequestHandler

class NetSuiteProviderBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "version" in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'text/xml')
            self.end_headers()
            self.wfile.write(bytes("<version>2.2.12</version>", 'UTF-8'))

def Run(server_class=HTTPServer, handler_class=NetSuiteProviderBaseHTTPRequestHandler):
    port = 8000
    server_address = ('', port)
    print("Server Running on port {}".format(port))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    Run()