#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
'''class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return
'''
#To run this code, replace the MyHandler in
#https://wiki.python.org/moin/BaseHttpServer With the following code,
from urlparse import urlparse, parse_qs
#class myHandler(BaseHTTPServer.BaseHTTPRequestHandler):
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
        except:
                delivery_receipt = {}

        """Check the is a delivery receipt"""
        if 'text' in delivery_receipt:
            print ("This is not a delivery receipt")
        elif delivery_receipt['status'] != "delivered":
            print "Fail:" + delivery_receipt['status']
            + ": " + delivery_receipt['err-code'] +  ".\n"
        else:
            print "success"
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', 8080), myHandler)
	print 'Started httpserver on port  , 8080'
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	