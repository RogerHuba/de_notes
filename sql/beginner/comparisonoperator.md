<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 COMPARISON OPERATORS

Comparison operators are used in SQL to compare two values.  
They are commonly used in the `WHERE` clause to filter records based on specific conditions.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column operator value;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` applies a comparison operator between a column and a value.

## Example

```sql
SELECT * FROM users WHERE age >= 18;
```

- This query selects all columns from the `users` table where the `age` is greater than or equal to 18.

## Key Points

- `=` : Equal to
- `<>` or `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- Always enclose text values in single quotes (`'...'`).

## Additional Example

```sql
SELECT first_name, last_name
FROM employees
WHERE salary <> 50000;
```

- This query selects employees whose salary is **not equal to** 50,000.

[⬅️ Previous: WHERE CONDITION](wherecondition.md)   [Next ➡️ LOGICAL OPERATORS](logicaloperator.md)
