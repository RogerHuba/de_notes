<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 NOT OPERATOR

The `NOT` operator is used in SQL to negate a condition in a `WHERE` clause.  
It returns rows where the condition is **false**.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows where the condition is **not true**.

## Example

```sql
SELECT * FROM users WHERE NOT city = 'New York';
```

- This query selects all users who do **not** live in New York.

## Key Points

- `NOT` reverses the result of the condition that follows it.
- `NOT` can be combined with `IN`, `BETWEEN`, `LIKE`, and other operators.
- Useful for finding records that do **not** match certain criteria.

## Additional Example

```sql
SELECT * FROM products
WHERE NOT price BETWEEN 100 AND 500;
```

- This query selects all products where the `price` is **not between** 100 and 500.

---

### 🎥 Video Notes

---

#### 📝 Problem Description

_Describe the problem, challenge, or topic discussed in a video related to `SELECT FROM`._  
_What concept was explained or what exercise was solved?_

---

### DataBase Given

---

#### 🧠 Solution Code / Explanation

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SQL COMMAND
```

---

[⬅️ Previous: OR OPERATOR](oroperator.md)   [Next ➡️ ORDER BY](orderby.md)
