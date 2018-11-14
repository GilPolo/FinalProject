-- Drop the tables if they already exist in order to start with a fresh
-- database. You will lose any movies you added.

DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS LineItems;

-- Create tables

CREATE TABLE Products(
    productID   INTEGER PRIMARY KEY,
    name        TEXT                    NOT NULL UNIQUE,
    price       REAL                    NOT NULL,
    discount    REAL                    NULL
);

CREATE TABLE Orders(
    orderID     INTEGER PRIMARY KEY,
    status      INTEGER                 NOT NULL,
    date_added  TEXT                    NOT NULL
);

CREATE TABLE LineItems(
    orderID     INTEGER REFERENCES Orders (orderID),
    lineID      INTEGER                 NOT NULL,
    productID   INTEGER REFERENCES Products (productID),
    quantity    INTEGER                 NOT NULL,
    PRIMARY KEY (orderID, lineID, productID)
);

-- Populate the Products table

INSERT INTO Products (name, price, discount)
    VALUES ('hammer', 21.00, 5);

INSERT INTO Products (name, price, discount)
    VALUES ('saw', 25.00, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('door', 655.00, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('fertilizer', 19.99, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('shovel', 31.99, 15);

INSERT INTO Products (name, price, discount)
    VALUES ('bug killer', 50.00, 15);

INSERT INTO Products (name, price, discount)
    VALUES ('washer', 410.00, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('dishwasher', 439.44, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('refrigerator',625.00, 10);

INSERT INTO Products (name, price, discount)
    VALUES ('cement', 69.11, 10);
