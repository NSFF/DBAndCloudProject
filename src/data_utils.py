from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import Any


class DataUtils:
    def connectToDBClient(self, db_uri: str) -> Any:
        """
        Return the connected MongoDB client

        Args:
            db_uri: (String) Connection string that will
                    be used to connect to the external
                    MongoDB client

        Returns:
            Connected MongoDB client
        """
        # Set the Stable API version when creating a new client
        return MongoClient(db_uri, server_api=ServerApi("1"))

    def connectToDB(self, db_name: str, db_uri: str) -> Any:
        """
        Return the connected MongoDB client

        Args:
            db_name: (String) name of the database to connect to
            db_uri: (String) Connection string that will
                    be used to connect to the external
                    MongoDB client

        Returns:
            Connected MongoDB client in the given database
        """
        client = self.connectToDBClient(db_uri)
        return client[db_name]

    def data_operation(self, data: Any) -> Any:
        """
        Execute an operation on the given mongoDB data

        Args:
            data: (Cursor object) list of documents in the mongoDB collection

        Returns:
            Connected MongoDB client in the given database
        """
        # for doc in data:
        #    pprint(doc)
        # print(float(str(debt)) + 5)
        # cloning so the cursor object does not get consumed
        data_lst = list(data.clone())
        result = 0
        i = 0
        for doc in data_lst:
            result += float(str(doc["debt"]))
            i += 1
        print("executed operation over", i, "documents")
        return result
