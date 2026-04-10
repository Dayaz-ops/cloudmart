from app.database import products_container

sample_products = [
    {"id": "1", "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": "2", "name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"id": "3", "name": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": "4", "name": "T-Shirt", "category": "Clothing", "price": 19.99},
    {"id": "5", "name": "Jeans", "category": "Clothing", "price": 49.99},
    {"id": "6", "name": "Book A", "category": "Books", "price": 14.99},
    {"id": "7", "name": "Book B", "category": "Books", "price": 24.99},
    {"id": "8", "name": "Sneakers", "category": "Clothing", "price": 89.99}
]

for product in sample_products:
    products_container.upsert_item(product)

print("Sample data inserted successfully!")
