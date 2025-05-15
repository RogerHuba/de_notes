<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 COMPARISON OPERATORS

Comparison operators are used in SQL to compare two values.  
They are commonly used in the `WHERE` clause to filter records based on specific conditions.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column operator value;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` applies a comparison operator between a column and a value.

## Example

```sql
SELECT * FROM users WHERE age >= 18;
```

- This query selects all columns from the `users` table where the `age` is greater than or equal to 18.

## Key Points

- `=` : Equal to
- `<>` or `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- Always enclose text values in single quotes (`'...'`).

## Additional Example

```sql
SELECT first_name, last_name
FROM employees
WHERE salary <> 50000;
```

- This query selects employees whose salary is **not equal to** 50,000.

---

### DE Academy Notes

Introduction:
The SQL Comparison Operators are essential tools for making data comparisons in SQL queries. They enable you to evaluate conditions and filter data based on specific comparisons between values. In this document, we will explore the most commonly used SQL Comparison Operators and learn how to apply them effectively to retrieve the desired data from a database.

Basic Syntax:
Comparison Operators in SQL are used in the WHERE clause to compare values. The basic syntax is as follows:

SELECT column1, column2, ... FROM table_name WHERE column_name operator value;

Commonly Used Comparison Operators: 
a. Equal To (=): The equal to operator is used to check if a value is equal to another value. For example:

SELECT * FROM products WHERE category = 'Electronics';

This query will retrieve all rows from the "products" table where the category is 'Electronics'.

b. Not Equal To (<> or !=): The not equal to operator checks if a value is not equal to another value. For example:

SELECT * FROM employees WHERE department <> 'Finance';

This query will retrieve all employees from departments other than 'Finance'.

c. Greater Than (>): The greater than operator checks if a value is greater than another value. For example:

SELECT * FROM orders WHERE order_amount > 1000;

This query will retrieve all orders with an order amount greater than 1000.

d. Less Than (<): The less than operator checks if a value is less than another value. For example:

SELECT * FROM products WHERE unit_price < 50;

This query will retrieve products with a unit price less than 50.

e. Greater Than or Equal To (>=): The greater than or equal to operator checks if a value is greater than or equal to another value. For example:

SELECT * FROM students WHERE age >= 18;

This query will retrieve all students who are 18 years old or older.

f. Less Than or Equal To (<=): The less than or equal to operator checks if a value is less than or equal to another value. For example:

SELECT * FROM employees WHERE years_of_service <= 5;

This query will retrieve employees with five or fewer years of service.


Combining Comparison Operators:
Comparison operators can be combined with logical operators (AND, OR, NOT) to create more complex conditions in the WHERE clause. For instance:

SELECT * FROM orders WHERE order_amount > 1000 AND order_status = 'Pending';

This query will retrieve orders with an order amount greater than 1000 and a status of 'Pending'.

 
Conclusion: 
SQL Comparison Operators are fundamental tools for data filtering and making precise data comparisons in SQL queries. By understanding and utilizing the examples and concepts covered in this document, you can effectively retrieve specific data from a database based on your desired comparisons.


Question:
Find out the product having unit price at least 150 and unit price not more than 700. Display the product_name.

Table: products

ColumnName      DataType
product_id      int
product_name    varchar
category        varchar
unit_price      decimal

Constraints:
The input table products contains valid data.

Sample Input:
Table: products  

| product_id | product_name | category  | unit_price |
|------------|--------------|-------------|----------|
| 1          | Laptop       | Electronics | 800.00   |
| 2          | Smartphone   | Electronics | 500.00   |
| 3          | Coffee Maker | Appliances  | 50.00    |
| 4          | Blender      | Appliances  | 200.00   |
| 5          | Headphones   | Electronics | 120.00   |

Output Format:
A result set with a single column:
product_name (varchar)

Sample Output:

| product_name |
|--------------|
| Smartphone   |
| Blender      |

Explanation:
The products with a unit price at least 150 and not more than 700 are "Smartphone" and "Blender".

---

#### 💻 My SQL Code

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SQL COMMAND
```

---

[⬅️ Previous: WHERE CONDITION](wherecondition.md)   [Next ➡️ LOGICAL OPERATORS](logicaloperator.md)
