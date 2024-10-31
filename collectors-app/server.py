from http.server import BaseHTTPRequestHandler, HTTPServer
from controllers.game_controller import GameController
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    controller = GameController()

    def do_GET(self):
        if self.path == '/games':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            games = self.controller.list_games()
            self.wfile.write(json.dumps(games).encode())

    def do_POST(self):
        if self.path == '/add_game':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            self.controller.add_game(
                data['name'], data['platform'], data['release_year'], data['developer'], data['condition']
            )
            self.send_response(201)
            self.end_headers()


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print("Server started on http://localhost:8000")
    httpd.serve_forever()
