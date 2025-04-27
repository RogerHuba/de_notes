<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUBQUERIES

A subquery is a query nested inside another SQL query.  
It is often used to perform intermediate calculations or filter results based on another set of data.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE column_name IN (SELECT column_name FROM another_table WHERE condition);
```

- A subquery is placed inside parentheses `()`.
- Subqueries can appear in `SELECT`, `FROM`, or `WHERE` clauses.
- The result of the subquery is used by the outer query.

## Example

```sql
SELECT first_name, last_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```

- This query selects employees who work in departments located in New York.

## Key Points

- Subqueries must be enclosed in parentheses `()`.
- A subquery can return a single value, a list of values, or a complete table.
- Subqueries are executed **before** the outer query.

## Additional Example

```sql
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

- This query selects products that have a price **higher than the average price**.

[⬅️ Previous: COUNT OPERATOR](countoperator.md)   [Next ➡️ MAX OPERATOR](maxoperator.md)
