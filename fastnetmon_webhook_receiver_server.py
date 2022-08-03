#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer

import socketserver
import random
import socket

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())
        
    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        print("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()
        print("Got POST data: " + str(self.data_string))
        #data = simplejson.loads(self.data_string)
        #with open("test123456.json", "w") as outfile:
        #    simplejson.dump(data, outfile)
        #print "{}".format(data)
        #f = open("for_presen.py")
        #self.wfile.write(f.read())
        return
        
class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6
  
# To enable IPv6 mode replace HTTPServer by HTTPServerV6 and replace '' by '::'
def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
