-- LC 1068 Product Sales Analysis I
SELECT product_name, year, price
FROM Product
JOIN Sales ON Product.product_id = Sales.product_id;
