import os
from azure.cosmos import CosmosClient

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "cloudmart"

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)

products_container = database.get_container_client("products")
cart_container = database.get_container_client("cart")
orders_container = database.get_container_client("orders")
