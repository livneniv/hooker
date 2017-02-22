#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import urlparse, parse_qs
import pymongo

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

    def do_GET(s):
        """Tell Nexmo that you have recieved the GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        """Parse parameters in the GET request"""
        parsed_path = urlparse(s.path)

        try:
                delivery_receipt = dict(
                [p.split('=') for p in parsed_path[4].split('&')])
                for keys,values in delivery_receipt.items():
                        print(keys + "   "  + values)
                conn=pymongo.MongoClient("mongodb://34.250.224.143:27017")
                db = conn.nexmo
                collection = db.nexmologs
                doc = {
                        delivery_receipt.keys()[0] : delivery_receipt.values()[0],
                        delivery_receipt.keys()[1] : delivery_receipt.values()[1],
                        delivery_receipt.keys()[2] : delivery_receipt.values()[2],
                        delivery_receipt.keys()[3] : delivery_receipt.values()[3],
                        delivery_receipt.keys()[4] : delivery_receipt.values()[4],
                        delivery_receipt.keys()[5] : delivery_receipt.values()[5]
                 }
                collection.insert(doc)
        except:
                delivery_receipt = {}

try:
        server = HTTPServer(('', 8080), myHandler)
        print 'Started httpserver on 8080 port'

        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()

