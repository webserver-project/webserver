import http.server
import socketserver

class processing_request():

	def navigate(self):
		if self.path.endswith('/post'):
			self.path = 'postindex.html'
			return http.server.SimpleHTTPRequestHandler.do_GET(self)

		if self.path.endswith('/get'):
			self.send_response(200)
			self.path = 'getindex.html'
			return http.server.SimpleHTTPRequestHandler.do_GET(self)

		if self.path.endswith('/test'):
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			html = "<html><head></head><body><h1>Make it as dynamix</h1></body></html>"
			self.wfile.write(bytes(html, 'utf8'))
			return

		if self.path == '/':
			print("testing")
			self.path = 'index.html'
			return http.server.SimpleHTTPRequestHandler.do_GET(self)	