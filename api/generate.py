from http.server import BaseHTTPRequestHandler
from src.fauxid import Fauxid
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        fauxid = Fauxid()
        data = fauxid.result()
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        return
