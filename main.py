import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

os.chdir(os.path.dirname(os.path.abspath(__file__)))

server = ThreadingHTTPServer(("0.0.0.0", 1000), SimpleHTTPRequestHandler)
print("EmulatorJS: http://localhost:1000")
server.serve_forever()