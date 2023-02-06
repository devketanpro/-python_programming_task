import os
from dotenv.main import load_dotenv
import socketserver
import http.server
import jwt
import http.client

env = load_dotenv()  # load the env file
HTTP_PORT = 9098  # access port for do any post request
KEY = os.environ['PRIVATE_KEY']  # key to encode/decode token.


class MyProxy(http.server.CGIHTTPRequestHandler):
    def do_POST(self):
        # for payload
        req_user = self.headers['date']  # timestamp
        req_date = self.headers['user']  # username
        encoded = jwt.encode(
            {os.environ['USERNAME_KEY']: req_user, os.environ['DATE_KEY']: req_date}, KEY, algorithm=os.environ['ALGORITH'])
        self.send_response(http.client.OK)
        self.end_headers()
        print(f"JWT-token: {encoded}")


httpd = socketserver.ForkingTCPServer(('', HTTP_PORT), MyProxy)
print("Available port for making post request:- ", str(HTTP_PORT))
httpd.serve_forever()
