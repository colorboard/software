from multiprocessing import Process
from .server import app


class ThreadManager:
    def __init__(self):
        self.server = Process(
            target=lambda: app.run(debug=False)
        )

    def start(self):
        self.server.start()

    def stop(self):
        self.server.kill()


threads = ThreadManager()
