import urllib.request
import socketserver
import http.server

PORT = 9098


class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)


httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print("Now serving at ", str(PORT))
httpd.serve_forever()
