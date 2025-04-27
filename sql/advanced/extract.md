<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 EXTRACT

The `EXTRACT` function is used in SQL to retrieve specific parts of a date or time value, such as the year, month, or day.  
It is useful for breaking down timestamps for reporting or filtering.

---

## 🛠️ Basic Syntax

```sql
SELECT EXTRACT(part FROM date_column)
FROM table_name;
```

- `part` can be `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, etc.
- `date_column` is the column containing the date or timestamp.

## Example

```sql
SELECT EXTRACT(YEAR FROM hire_date) AS hire_year
FROM employees;
```

- This query extracts the year from each employee’s hire date.

## Key Points

- Common parts you can extract: `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`.
- Some databases (like MySQL) use functions like `YEAR(date_column)` instead of `EXTRACT`.
- `EXTRACT` works with both `DATE` and `TIMESTAMP` data types.

## Additional Example

```sql
SELECT EXTRACT(MONTH FROM order_date) AS order_month
FROM orders;
```

- This query extracts the month from each order date.

[⬅️ Previous: UPPER & LOWER](upperlower.md)   [Next ➡️ COALESCE](coalesce.md)
