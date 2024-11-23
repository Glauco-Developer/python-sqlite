# SQLite Database Example with Python

This project demonstrates how to interact with a SQLite database using Python. It connects to a database, retrieves records from a `produtos` (products) table, and displays the results in a formatted output.

## Prerequisites

1. Python installed on your system.
2. SQLite installed and configured.
3. A SQLite database file (`market.db`) with a table named `produtos` containing the following fields:
   - `id_produto`: Integer, primary key.
   - `nome`: String, name of the product.
   - `preco`: Real, price of the product.
   - `quantidade`: Integer, quantity of the product.

## Table Schema

Run the following SQL commands to create and populate the `produtos` table if it doesn't exist:

```sql
CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    quantidade INTEGER
);

INSERT INTO produtos (nome, preco, quantidade) VALUES
('Product 1', 4.99, 100),
('Product 2', 5.99, 200),
('Product 3', 14.99, 300),
('Product 4', 122.99, 400);
