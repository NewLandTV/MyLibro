import json
import path
import socketserver
from threading import Thread

class APIServerInfo:
    def __init__(self, use_api_server = False):
        self.use_api_server = use_api_server

    def save(self, filename="api_server.json"):
        data = {
            "use_api_server": self.use_api_server
        }
        with open(path.join(path.data_dir, filename), "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False)
        print("API 서버 정보를 로컬 파일에 저장했습니다.")

    def load(self, filename="api_server.json"):
        pth = path.join(path.data_dir, filename)
        if not path.exists(pth):
            print(f"'{filename}' 파일을 찾을 수 없어 API 서버 정보를 불러오지 못했습니다.")
            return
        
        with open(pth, "r", encoding="utf8") as f:
            data = json.load(f)
            self.__dict__.update(data)
        print("API 서버 정보를 로컬 파일에서 불러왔습니다.")

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"{self.client_address}에서 API 서버와 연결되었습니다.")

        while True:
            data = self.request.recv(1024)
            if data.decode() == "/exit":
                print("해당 클라이언트가 서버와 연결이 종료되었습니다.")
                self.request.close()
                break
            self.request.send(data)

class APIServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

started = False
server = None

def run_api_server():
    global started, server
    if started:
        shutdown_api_server()
    started = True
    server = APIServer(("", 8230), ClientHandler)
    print("API 서버가 구동되고 있습니다...")

    thread = Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    print("API 서버가 연결을 기다리고 있습니다...")

def shutdown_api_server():
    global started, server
    if not started:
        return
    started = False
    server.shutdown()
    print("API 서버가 종료되고 있습니다...")
    server.server_close()
    print("API 서버가 종료되었습니다.")