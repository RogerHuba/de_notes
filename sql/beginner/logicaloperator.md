<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LOGICAL OPERATORS

Logical operators are used in SQL to combine multiple conditions in a `WHERE` clause.  
They control how multiple conditions are evaluated together.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 [AND/OR/NOT] condition2;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows based on one or more conditions.

## Example

```sql
SELECT * FROM users WHERE age > 18 AND city = 'New York';
```

- This query selects all users where the `age` is greater than 18 **and** the `city` is New York.

## Key Points

- `AND` requires **both** conditions to be true.
- `OR` requires **either** condition to be true.
- `NOT` negates a condition.
- Use parentheses `()` to group conditions when needed for clarity.

## Additional Example

```sql
SELECT * FROM products
WHERE price > 100 OR stock < 50;
```

- This query selects products where the `price` is greater than 100 **or** the `stock` is less than 50.

[⬅️ Previous: COMPARISON OPERATORS](comparisonoperator.md)   [Next ➡️ LIKE OPERATOR](likeoperator.md)
