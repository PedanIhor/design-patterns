from threading import Lock, Thread

class SingletonMeta(type):
    """Thread-safe singleton metaclass."""
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'log_file'):
            self.log_file = open("log.txt", "a")

    def log(self, message):
        self.log_file.write(message + "\n")
        self.log_file.flush()


def test_singleton(msg: str) -> None:
    logger = Logger()
    print(f"Logger ID: {id(logger)}")
    logger.log(msg)


if __name__ == "__main__":
    # The client code.

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()