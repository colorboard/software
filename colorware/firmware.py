from subprocess import Popen


class FirmwareManager:
    def __init__(self, file='firmware.py', interpreter='python3'):
        self.log = list()
        self.file = file
        self.interpreter = interpreter
        open(file, 'w').close()
        self.run()

    def run(self):
        self.process = Popen([self.interpreter, self.file], stdout=-1)
        for line in self.process.stdout:
            self.log.append(line.decode('utf-8').replace('\n', ''))

    def update(self, content):
        self.process.kill()
        open(self.file, 'w').write(content)
        self.log.clear()
        self.run()
        print(content)


firmware = FirmwareManager()
