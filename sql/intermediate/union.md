<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 UNION

The `UNION` operator is used in SQL to combine the result sets of two or more `SELECT` statements.  
It removes duplicate rows between the combined result sets by default.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table1
WHERE condition

UNION

SELECT column1, column2, ...
FROM table2
WHERE condition;
```

- Each `SELECT` statement must have the same number of columns.
- Columns must have compatible data types and appear in the same order.

## Example

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'Sales'

UNION

SELECT first_name, last_name
FROM employees
WHERE department = 'Marketing';
```

- This query returns a combined list of employees from the Sales and Marketing departments, without duplicates.

## Key Points

- `UNION` removes duplicate rows by default.
- If you want to include duplicates, use `UNION ALL`.
- The column names in the final result come from the first `SELECT` statement.

## Additional Example

```sql
SELECT city
FROM customers

UNION

SELECT city
FROM suppliers;
```

- This query returns a distinct list of cities from both customers and suppliers.

[⬅️ Previous: SELF JOIN](selfjoin.md)   [Back to Main](../../README.md)
