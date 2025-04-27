<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUM OPERATOR

The `SUM` function is used in SQL to return the total sum of a numeric column.  
It is useful for calculating totals such as total sales, total salaries, or any other cumulative value.

---

## 🛠️ Basic Syntax

```sql
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

- `SUM(column_name)` adds together all the values in the specified column.
- Can be combined with `GROUP BY` to calculate sums for different groups.

## Example

```sql
SELECT SUM(salary)
FROM employees;
```

- This query returns the total of all salaries from the employees table.

## Key Points

- Only works with numeric columns.
- Ignores `NULL` values.
- Often paired with `GROUP BY` to calculate sums across groups.

## Additional Example

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

- This query shows the total salary expense for each department.

[⬅️ Previous: MIN OPERATOR](minoperator.md)   [Next ➡️ AVG OPERATOR](avgoperator.md)
