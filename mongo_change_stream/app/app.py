import pymongo
from pymongo import UpdateOne, ReplaceOne
import pandas as pd
import click

@click.group(chain=True)
def cli():
    pass

def get_database():
    db_name = "database"
    mongo_uri = "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"
    client = pymongo.MongoClient(mongo_uri,
                                 serverSelectionTimeoutMS=2000)

    database = client.get_database(db_name)
    return database

@cli.command("drop_collection")
def drop_collection_of_mongo():
    get_database().drop_collection("main_resource")


@cli.command("load_resource")
def load_resource_to_mongo():
    print("loading resource...")
    df = pd.read_csv("resource.csv")
    df.columns = ["ticker", "description", "sector", "pe_ratio", "px_last"]
    database = get_database()
    collection = database.get_collection("main_resource")
    records = df.to_dict(orient="records")
    updates = [ReplaceOne({"_id": record["ticker"]}, record, upsert=True) for record in records ]
    collection.bulk_write(updates)


@cli.command("change_stream")
def change_stream():
    print("change_stream started...")
    database = get_database()
    pipeline = []
    with database.watch(pipeline) as stream:
        for insert_change in stream:
            print(insert_change)


if __name__=="__main__":
    cli()
