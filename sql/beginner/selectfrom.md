<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SELECT FROM

The `SELECT` statement is used to retrieve data from a database.  
The `FROM` clause specifies the table you want to select from.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

- `SELECT` defines which columns to retrieve.
- `FROM` specifies the table containing the data.

## Example

```sql
SELECT first_name, last_name
FROM employees;
```

- This query retrieves the first name and last name columns from the employees table.

## Key Points

- You can select one, multiple, or all columns (using `*`).
- Column order in `SELECT` matters for the output.
- Queries can include expressions (e.g., `SELECT salary * 1.1`).

## Additional Example

```sql
SELECT *
FROM customers;
```

- This query retrieves all columns from the customers table.

---

### 🎥 Video Notes

* No Video for this command!

---

#### 📝 Problem Description

Retrieve the email of customers with aliases "Customer_Email".

### DataBase Given

```database
Table: customers

ColumnName          Datatype           
customer_id         int 
customer_name       varchar
age                 int 
city                varchar
email               varchar
address             varchar
```

Sample Input:
Table: customers

| customer_id | customer_name | age | city | email                | address              |
|-------------|---------------|-----|------|----------------------|----------------------|
| 1           | John Doe      | 30  | NYC  | john.doe@email.com   | 123 Main Street      |
| 2           | Jane Smith    | 25  | LA   | jane.smith@email.com | 456 Oak Avenue       |
| 3           | Mike Johnson  | 35  | CHI  | mike.johnson@email.com| 789 Pine Boulevard  |

---

#### 🧠 Solution Code / Explanation

```sql
SELECT email 
FROM customers
```

---

#### DE Notes

Introduction:
The SQL SELECT statement is a fundamental command used to retrieve data from a database. Understanding this statement is essential for anyone working with databases. In this document, we will explore the basic syntax of the SELECT statement and learn how to retrieve data from a database table.

Basic Syntax:
The SELECT statement begins with the keyword "SELECT," followed by a list of columns from which data will be retrieved. It is structured as follows:

SELECT column1, column2, column3, ... FROM table_name;

Retrieving All Columns:
To retrieve all columns from a table, you can use an asterisk (*) as a wildcard character. The syntax for this is:

SELECT * FROM table_name;

Keep in mind that while retrieving all columns might be useful in some scenarios, it can lead to inefficiencies when dealing with large tables or unnecessary data.

Retrieving Specific Columns:
To select specific columns, simply list their names after the "SELECT" keyword, separated by commas. For example:

SELECT column1, column2 FROM table_name;

Selecting only the necessary columns can optimize data retrieval, reduce network traffic, and improve query performance.

Aliasing Columns:
Aliases are used to provide temporary names for columns in the result set. You can assign an alias using the "AS" keyword. The syntax is as follows:

SELECT column1 AS alias1, column2 AS alias2 FROM table_name;

Aliases are helpful for providing more descriptive names or shortening lengthy column names in the output.

Practical Examples:
Let's look at some practical examples of using the SQL SELECT statement:

Example 1: Simple SELECT

SELECT * FROM employees;

Example 2: Selecting Specific Columns

SELECT employee_id, first_name, last_name FROM employees;

Example 3: Aliasing Columns

SELECT product_name AS "Product", unit_price AS "Price" FROM products;

Conclusion:
In summary, the SQL SELECT statement is used to retrieve data from a database table. It allows you to specify the desired columns and apply aliases for better readability. Understanding and using the SELECT statement effectively is crucial for working with databases and extracting the necessary information.

Question:
Retrieve the email of customers with aliases "Customer_Email".

Table: customers

ColumnName          Datatype
customer_id         int
customer_name       varchar
age                 int
city                varchar
email               varchar
address             varchar

Constraints:
The input table customers contains valid data.

Sample Input:
Table: customers

| customer_id | customer_name | age | city | email                | address              |
|-------------|---------------|-----|------|----------------------|----------------------|
| 1           | John Doe      | 30  | NYC  | john.doe@email.com   | 123 Main Street      |
| 2           | Jane Smith    | 25  | LA   | jane.smith@email.com | 456 Oak Avenue       |
| 3           | Mike Johnson  | 35  | CHI  | mike.johnson@email.com| 789 Pine Boulevard   |

Output Format:
A result set with columns:
Customer_Email (varchar)

Sample Output:

| Customer_Email        |
|-----------------------|
| john.doe@email.com    |
| jane.smith@email.com  |
| mike.johnson@email.com|

---

[Main ⬅️](../../README.md)   [Next ➡️ WHERE CONDITION](wherecondition.md)
