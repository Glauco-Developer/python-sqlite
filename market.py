import sqlite3

# Path to the SQLite database file
DATABASE = "C:\\Users\\Path\\to\\the\\SQLite\\database\\file\\market.db"

try:
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    print("Database connected")
    
    # Create the cursor and execute the query
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    records = cursor.fetchall()
    
    # List to store the products
    products = []
    for record in records:
        product_id = int(record[0])
        name = record[1]
        price = float(record[2])
        quantity = int(record[3])
        # Add as a dictionary
        products.append({"id": product_id, "name": name, "price": price, "quantity": quantity})
    
    # Display the products
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

except sqlite3.Error as ex:
    print(f"Error connecting to the database: {ex}")
finally:
    # Close the connection if it's open
    if 'conn' in locals() and conn:
        conn.close()
        print("Database disconnected")