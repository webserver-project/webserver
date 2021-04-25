import http.server
import socketserver
import process_request
from process_request import processing_request
from socketserver import ThreadingMixIn
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        #Process Request
        data=processing_request.navigate(self)
        process_response(data)


    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
    

    def do_POST(self):
        # Gets the size of data
        content_length = int(self.headers['Content-Length']) # Gets the size of data
        # Gets the data itself
        post_data = self.rfile.read(content_length) 
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        

# Create an object of the above class
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('0.0.0.0', 8000), MyHttpRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    run()