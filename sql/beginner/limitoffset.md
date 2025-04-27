<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LIMIT OFFSET

The `LIMIT` and `OFFSET` clauses are used in SQL to control how many records are returned and where to start from.  
They are especially useful for pagination and managing large result sets.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number_rows OFFSET start_point;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `LIMIT` restricts the number of rows returned.
- `OFFSET` skips a specified number of rows before starting to return rows.

## Example

```sql
SELECT * FROM users LIMIT 5 OFFSET 10;
```

- This query skips the first 10 users and then returns the next 5 users.

## Key Points

- `LIMIT` is required to use `OFFSET`.
- `OFFSET 0` means start from the very first row.
- Useful for pagination (e.g., displaying 10 records per page).

## Additional Example

```sql
SELECT * FROM products
ORDER BY price ASC
LIMIT 10 OFFSET 20;
```

- This query sorts products by `price` ascending, skips the first 20 products, and returns the next 10 products.

[⬅️ Previous: ORDER BY](orderby.md) [➡️ Back to Main](../../README.md)
