<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 WHERE CONDITION

The `WHERE` clause is used to **filter records** based on specific conditions.  
It allows you to retrieve only the rows that meet a certain criteria.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters the results based on a condition.

## Example

```sql
SELECT * FROM users WHERE age > 18;
```

- This query selects all columns from the `users` table where the `age` is greater than 18.

## Key Points

- `WHERE` filters rows, not columns.
- Text values in conditions must be enclosed in single quotes (`'...'`).
- You can use operators like `=`, `>`, `<`, `>=`, `<=`, and `<>` (not equal).
- Multiple conditions can be combined with `AND`, `OR`, and `NOT`.

## Additional Example

```sql
SELECT *
FROM products
WHERE price > 100;
```

- This query selects all columns from the `products` table where the `price` is greater than 100.

[⬅️ Previous: SELECT FROM](selectfrom.md)   [Next ➡️ COMPARISON OPERATORS](comparisonoperator.md)
