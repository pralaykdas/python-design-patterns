"""
Intent:
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a
global access point to this instance.

In this example, let's create a DatabaseConnection class that ensures only one instance is created (Singleton pattern)
for all the database operations.

Mechanism:
Thread safe
"""

from threading import Thread, Lock

class SingletonMeta(type):
    """Metaclass that ensures only one instance of the class is created."""
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                # A single instance is created
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, host:str, port:int):
        if not host or not port:
            raise ValueError("Both host and port must be provided.")
        self.host = host
        self.port = port

    def connect(self):
        """
        A connect method to simulate a connection.
        This method can be replaced with a business logic for other cases.
        """
        print(f"Connecting to database at {self.host}:{self.port}")

    def __str__(self):
        return f"DatabaseConnection({self.host}, {self.port})"


def test_singleton(host: str, port:int) -> None:
    singleton = DatabaseConnection(host, port)
    print(singleton)


if __name__ == '__main__':
    print("If the values are same, then singleton was reused.\n"
          "If the values are different, then 2 singletons were created.\n\n"
          "RESULT:\n")
    # First instantiation: creates the instance
    thread1 = Thread(target=test_singleton, args=("localhost", 5432))
    # Second instantiation: creates the instance
    thread2 = Thread(target=test_singleton, args=("remotehost", 3306))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()