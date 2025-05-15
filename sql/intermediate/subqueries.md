<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUBQUERIES

A subquery is a query nested inside another SQL query.  
It is often used to perform intermediate calculations or filter results based on another set of data.

The SQL Subqueries, also known as nested queries, are a powerful tool in database management that allows you to embed one query within another. Subqueries enable you to retrieve data from multiple tables, perform complex calculations, and filter results based on specific conditions. By mastering subqueries, you can elevate your data retrieval and analysis capabilities, facilitating efficient querying and gaining deeper insights. This document provides a comprehensive understanding of subqueries, their types, syntax, use cases, and practical examples to empower your data manipulation skills on your edtech platform.

---

## Introduction to Subqueries

A subquery is a query nested within another query, used to retrieve or manipulate data.
Subqueries can be placed in SELECT, FROM, WHERE, and HAVING clauses.

## Types of Subqueries

- Single Row Subqueries: Return a single value (usually for comparison).
- Multiple Row Subqueries: Return multiple values (usually for inclusion in a list).
- Correlated Subqueries: Reference values from the outer query within the subquery.
- Subqueries with EXISTS: Check for the existence of certain conditions.

## Common Use Cases

- Data Filtering: Filtering results based on conditions in another table.
- Aggregations: Using subqueries within aggregate functions like SUM, AVG, etc.
- Data Comparison: Comparing values within different datasets.
- Conditional Checks: Checking the existence of certain records.

## 🛠️ Basic Syntax

```sql
Example 1 - Single Row Subquery:
SELECT product_name, unit_price 
FROM products 
WHERE unit_price > (SELECT AVG(unit_price) 
                    FROM products);

Example 2 - Multiple Row Subquery:
SELECT order_id 
FROM orders 
WHERE customer_id IN (SELECT customer_id 
                      FROM customers 
                      WHERE country = 'USA');

Example 3 - Correlated Subquery:
SELECT employee_id, first_name, last_name 
FROM employees e 
WHERE salary > (SELECT AVG(salary) 
                FROM employees 
                WHERE department_id = e.department_id);

Example 4 - Subquery with EXISTS:
SELECT product_name 
FROM products 
WHERE EXISTS (SELECT 1 
              FROM order_details 
              WHERE product_id = products.product_id);
```

---

## Benefits of Subqueries 

- Enhanced Data Retrieval: Retrieve data from multiple tables in a single query.
- Complex Calculations: Perform calculations involving multiple levels of data.
- Granular Filtering: Filter data based on intricate conditions.

## Example

```sql
SELECT first_name, last_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```

- This query selects employees who work in departments located in New York.

---

## Key Points

- Subqueries must be enclosed in parentheses `()`.
- A subquery can return a single value, a list of values, or a complete table.
- Subqueries are executed **before** the outer query.
- Understand the correlation between outer and inner queries in correlated subqueries.
- Optimize subqueries for performance by using appropriate indexes.

---

## Additional Example

```sql
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

- This query selects products that have a price **higher than the average price**.

---

### 📝 Problem Description

Retrieve employee_id, first_name, last_name and salary who have a higher salary than the average salary across all employees.

---

### DataBase Given

Table: employees

ColumnNames DataType
employee_id int
first_name  varchar
last_name   varchar  
department  varchar
salary      decimal
manager_id  int

Sample Input:

| employees                                     |
|-----------------------------------------------|

| employee_id | first_name | last_name | department | salary | manager_id |
|-------------|------------|-----------|------------|--------|------------|
| 1           | John       | Doe       | Sales      | 65000.00| 3          |
| 2           | Jane       | Smith     | Finance    | 75000.00| 4          |
| 3           | Mike       | Johnson   | Sales      | 80000.00| 5          |
| 4           | Emily      | Davis     | IT         | 70000.00| 5          |
| 5           | Robert     | Brown     | HR         | 90000.00| NULL       |

Constraints:
The input table employees contains valid data.

Output Format:
A result set with columns:
employee_id (int)
first_name (varchar)
last_name (varchar)
salary (decimal)

Sample Output:

| employee_id | first_name | last_name | salary   |
|-------------|------------|-----------|----------|
| 2           | Jane       | Smith     | 75000.00 |
| 3           | Mike       | Johnson   | 80000.00 |
| 5           | Robert     | Brown     | 90000.00 |


---

#### 💻 My SQL Code

```sql
-- get employee id, fname, lname, and salary > avg salary
-- Need to get average salary

SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary)
                FROM employees)
```

---

### Explanation

Employees with employee_id 2, 3, and 5 have a higher salary than the average salary across all employees.

---

[⬅️ Previous: COUNT OPERATOR](countoperator.md)   [Next ➡️ MAX OPERATOR](maxoperator.md)
