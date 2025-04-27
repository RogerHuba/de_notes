<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 WINDOW FUNCTION

Window functions in SQL perform calculations across a set of table rows that are related to the current row.  
Unlike aggregate functions, they do not collapse the result set.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, 
       window_function() OVER (PARTITION BY column2 ORDER BY column3)
FROM table_name;
```

- `OVER` defines the window of rows to apply the function to.
- `PARTITION BY` divides the result set into groups.
- `ORDER BY` specifies the order of rows within each partition.

## Example

```sql
SELECT employee_id, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees;
```

- This query ranks employees by salary within each department.

## Key Points

- Common window functions: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `SUM()`, `AVG()`.
- `PARTITION BY` is optional — if omitted, the entire result set is treated as a single partition.
- `ORDER BY` inside the `OVER` clause controls the row order for the function.

## Additional Example

```sql
SELECT order_id, customer_id, 
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_sequence
FROM orders;
```

- This query numbers each customer's orders starting from 1.

[⬅️ Previous: SUBQUERY IN CONDITION](subqueryincondition.md)   [Next ➡️ ROW NUMBER](rownumber.md)
