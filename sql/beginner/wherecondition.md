<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 WHERE CONDITION

The `WHERE` clause is used to **filter records** based on specific conditions.  
It allows you to retrieve only the rows that meet a certain criteria.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters the results based on a condition.

## Example

```sql
SELECT * FROM users WHERE age > 18;
```

- This query selects all columns from the `users` table where the `age` is greater than 18.

## Key Points

- `WHERE` filters rows, not columns.
- Text values in conditions must be enclosed in single quotes (`'...'`).
- You can use operators like `=`, `>`, `<`, `>=`, `<=`, and `<>` (not equal).
- Multiple conditions can be combined with `AND`, `OR`, and `NOT`.

## Additional Example

```sql
SELECT *
FROM products
WHERE price > 100;
```

- This query selects all columns from the `products` table where the `price` is greater than 100.

---

### 🎥 Video Notes

* No Video for command.

---

#### 📝 Problem Description

 Find out the employees working in 'finance' department with salary at least 70000. Display employee_id, first_name, last_name of the employee.

---

### DataBase Given

```database
Table: employees
 
ColumnNames  DataType
employee_id  int  
first_name   varchar
last_name    varchar  
department   varchar 
salary       decimal
manager_id   int
```

---

🧠 Solution Code / Explanation

```sql
SELECT employee_id, first_name, last_name
FROM employees
WHERE (department = 'finance' and salary >= 70000)
```

---

#### DE Notes

Introduction:
The SQL WHERE clause is a powerful tool that allows you to filter data based on specified conditions in SQL queries. It plays a crucial role in retrieving specific rows from a database table that meet certain criteria, enabling more precise and targeted data retrieval. In this document, we will explore the syntax and usage of the SQL WHERE clause to enhance your data filtering skills.


Basic Syntax:
The basic syntax of the SQL WHERE clause is as follows:

SELECT column1, column2, ... FROM table_name WHERE condition;


Filtering Data with WHERE Clause:
The WHERE clause filters data by applying conditions to the rows in a table. It allows you to specify one or more conditions that must be true for a row to be included in the result set. For example, to retrieve all employees with a salary greater than 50000 from a table called "employees," you would use the following query:

SELECT * FROM employees WHERE salary > 50000;


Logical Operators in WHERE Clause:
You can use logical operators (AND, OR, NOT) to create more complex conditions in the WHERE clause. For instance, to retrieve employees with a salary greater than 50000 and belonging to the "Sales" department, you can use the AND operator as follows:

SELECT * FROM employees WHERE salary > 50000 AND department = 'Sales';

Comparison Operators in WHERE Clause:
Comparison operators (e.g., =, <>, >, <, >=, <=) are used to compare values in the WHERE clause. For example, to retrieve products with a unit price less than 50, you can use the following query:

SELECT product_name, unit_price FROM products WHERE unit_price < 50;

Using Wildcards with WHERE Clause:
The WHERE clause can also be used with wildcard characters for pattern matching. For instance, to retrieve all customers with names starting with "Joh," you can use the LIKE operator and the '%' wildcard as follows:

SELECT * FROM customers WHERE customer_name LIKE 'Joh%';

Combining Conditions with Parentheses:
To create more complex conditions, you can use parentheses to group logical expressions. For example, to retrieve products with a unit price less than 50 or belonging to the "Electronics" category, you can use parentheses and the OR operator as follows:

SELECT product_name, unit_price, category FROM products WHERE (unit_price < 50 OR category = 'Electronics');

NULL Values and IS NULL/IS NOT NULL:
To filter rows based on NULL values, you can use the IS NULL or IS NOT NULL operators. For example, to retrieve employees with no assigned manager, you can use the following query:

SELECT * FROM employees WHERE manager_id IS NULL;

Conclusion:
The SQL WHERE clause is a critical component of SQL queries that allows you to filter data and retrieve specific information from a database table. By mastering the concepts and examples covered in this document, you can efficiently use the WHERE clause to perform precise data filtering, enabling more effective data analysis and reporting.

Question:
 Find out the employees working in 'finance' department with salary at least 70000. Display employee_id, first_name, last_name of the employee.

Table: employees

ColumnNames     DataType
employee_id     int
first_name      varchar
last_name       varchar  
department      varchar
salary          decimal
manager_id      int

Constraints:
The input table employees contains valid data.

Sample Input:
Table:employees

| employee_id | first_name | last_name | department | salary | manager_id |
|-------------|------------|-----------|------------|--------|------------|
| 1           | John       | Doe       | IT         | 60000.00| 3          |
| 2           | Jane       | Smith     | Finance    | 75000.00| 4          |
| 3           | Mike       | Johnson   | IT         | 80000.00| 5          |
| 4           | Emily      | Davis     | Finance    | 70000.00| 5          |
| 5           | Robert     | Brown     | HR         | 90000.00| NULL      |

Output Format:
A result set with columns:
employee_id (int)
first_name (varchar)
last_name (varchar)

Sample Output:

| employee_id | first_name | last_name |
|-------------|------------|-----------|
| 4           | Emily      | Davis     |

Explanation:
The employees working in the 'finance' department with a salary of at least 70000 are Emily (employee_id 4).

---

[⬅️ Previous: SELECT FROM](selectfrom.md)   [Next ➡️ COMPARISON OPERATORS](comparisonoperator.md)
