from dataclasses import dataclass
import os


@dataclass
class DBConfigs:
    """
    General DB Configs
    Params:
        DB_URI (str): Connectionstring to the MongoDB
        DB_NAME (str): Name of the database of MongoDB
    """

    DB_URI = f"mongodb+srv://{os.environ['DB_READ_USERNAME']}:{os.environ['DB_READ_USER_PASS']}@dbandcloud.s1vklr4.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "DBAndCloud"
