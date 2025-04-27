<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 DISTINCT

The `DISTINCT` keyword is used in SQL to return only **unique** values by removing duplicates from the result set.  
It ensures that each returned row is different from the others.

---

## 🛠️ Basic Syntax

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

- `SELECT DISTINCT` removes duplicate rows based on the specified columns.
- All columns listed after `DISTINCT` are considered when checking for duplicates.

## Example

```sql
SELECT DISTINCT department
FROM employees;
```

- This query returns a list of unique departments from the employees table.

## Key Points

- `DISTINCT` applies to all the columns listed in the `SELECT` statement.
- If you select multiple columns, `DISTINCT` keeps unique combinations of all selected columns.
- You can use `DISTINCT` with aggregate functions in some databases (e.g., `COUNT(DISTINCT column_name)`).

## Additional Example

```sql
SELECT DISTINCT city, state
FROM customers;
```

- This query returns unique combinations of city and state from the customers table.

[⬅️ Previous: JOIN WITH COMPARISON](joinwithacomparisonoperator.md)   [Next ➡️ JOIN WITH MULTIPLE KEYS](joinwithmultiplekeys.md)
