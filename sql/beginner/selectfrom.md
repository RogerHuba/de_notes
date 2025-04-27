<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SELECT FROM

The `SELECT` statement is used to **retrieve data** from a database.  
It allows you to choose specific columns or entire rows from a table.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

- `SELECT` specifies the columns you want to retrieve.
- `FROM` specifies the table you want to pull the data from.

## Example

```sql
SELECT first_name, last_name
FROM employees;
```

- This query retrieves the `first_name` and `last_name` columns from the `employees` table.

## Key Points

- `SELECT *` retrieves **all columns** from a table.
- Always separate multiple columns with **commas**.
- SQL statements are **not case-sensitive**, but using uppercase for keywords (`SELECT`, `FROM`) improves readability.
- You can retrieve one, several, or all columns from a table.

## Additional Example

```sql
SELECT *
FROM customers;
```

- This retrieves **every column** from the `customers` table.

[⬅️ Back to Main](../../README.md)   [Next ➡️ WHERE CONDITION](wherecondition.md)
