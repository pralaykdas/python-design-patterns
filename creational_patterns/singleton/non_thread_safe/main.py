"""
Intent:
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a
global access point to this instance.

In this example, let's create a DatabaseConnection class that ensures only one instance is created (Singleton pattern)
for all the database operations.

Mechanism:
Naive or non-thread safe
"""

class SingletonMeta(type):
    """Metaclass that ensures only one instance of the class is created."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
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


if __name__ == '__main__':
    # Testing the Singleton with Validation
    # First instantiation: creates the instance
    db1 = DatabaseConnection(host="localhost", port=5432)
    db1.connect()  # Output: Connecting to database at localhost:5432
    print(db1)
    # Second instantiation with different arguments: returns the same instance~
    db2 = DatabaseConnection(host="remotehost", port=3306)
    print(db2)

    # The singleton pattern ensures both db1 and db2 are the same instance
    print("ID of db1: {}".format(id(db1)))
    print("ID of db2: {}".format(id(db2)))
    print("Is db1 == db2? {}".format(db1 is db2))  # Output: True
    if id(db1) == id(db2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")