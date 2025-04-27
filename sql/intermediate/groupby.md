<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 GROUP BY

The `GROUP BY` clause is used in SQL to arrange identical data into groups.  
It is commonly used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN` to perform calculations on each group.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

- `SELECT` specifies the columns you want to retrieve.
- Aggregate functions are applied to the grouped data.
- `GROUP BY` determines how the rows are grouped together.

## Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

- This query counts how many employees are in each department.

## Key Points

- Every column in the `SELECT` list that is **not** inside an aggregate function must appear in the `GROUP BY`.
- `GROUP BY` happens **after** the `WHERE` clause but **before** `ORDER BY`.
- `GROUP BY` can group by one or more columns.

## Additional Example

```sql
SELECT city, AVG(salary)
FROM employees
GROUP BY city;
```

- This query calculates the average salary for each city.

[⬅️ Previous: LIMIT OFFSET](limitoffset.md)   [Next ➡️ COUNT OPERATOR](countoperator.md)
