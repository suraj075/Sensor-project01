# from pymongo.mongo_client import MongoClient
# import pandas as pd
import json

# # url
# uri = 'mongodb+srv://kumarsuraj07553:Kumar@12345@cluster0.d6ymnlj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'


# # create a new client and connect to server
# client = MongoClient(uri)

# # create database name and collection name
# DATABASE_NAME = 'pwskills'
# COLLECTION_NAME = 'waferfault'

# df = pd.read_csv('...//Notebooks/wafer_23012020_041211.csv')
# print(df.head())

from pymongo.mongo_client import MongoClient
import pandas as pd
import urllib.parse

# Properly escape username and password
username = urllib.parse.quote_plus("kumarsuraj07553")
password = urllib.parse.quote_plus("ZYybgBXJhB8r2rLm")

# Correctly format the URI
uri = f"mongodb+srv://{username}:{password}@cluster0.d6ymnlj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create database name and collection name
DATABASE_NAME = 'pwskills'
COLLECTION_NAME = 'waferfault'

# Use the correct file path for the CSV file
csv_file_path = r'C:\Users\ACER\ML Projects\Notebooks\wafer_23012020_041211.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Display the first 5 rows of the DataFrame
# print(df.head())

# drop the "Unnamed:0"
df = df.drop('Unnamed: 0',axis=1)
# print(df)

json_record = list(json.loads(df.T.to_json()).values())
# print(json_record,type(json_record))

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)