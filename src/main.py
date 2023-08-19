from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import Any
from configs import DBConfigs
from data_utils import DataUtils


def main():
    dataUtils = DataUtils()
    client = dataUtils.connectToDB(DBConfigs.DB_NAME, DBConfigs.DB_URI)
    # Send a ping to confirm a successful connection
    try:
        print("Connected to MongoDB!")

        # get all debt of all documents
        data = client.Financials.find({}, {"_id": 0, "debt": 1})

        # execute a data operation on the debt data.
        # This could have been anything from data analysis to training of machine learning models
        result = dataUtils.data_operation(data)

        print("total debt is:", result, "Euro")
    except Exception as e:
        print(e)

    print("Script Ended!")


if __name__ == "__main__":
    main()
