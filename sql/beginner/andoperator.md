<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 AND OPERATOR

The `AND` operator is used in SQL to combine multiple conditions in a `WHERE` clause.  
All conditions combined with `AND` must be true for a row to be included in the result set.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows where **both** conditions are true.

## Example

```sql
SELECT * FROM users WHERE age > 18 AND city = 'New York';
```

- This query selects all users who are older than 18 **and** live in New York.

## Key Points

- All conditions connected by `AND` must be **true** for a row to be included.
- You can combine more than two conditions using multiple `AND`s.
- Use parentheses `()` to group complex conditions for clarity.

## Additional Example

```sql
SELECT * FROM products
WHERE price > 100 AND stock > 0;
```

- This query selects all products where the `price` is greater than 100 **and** the `stock` is greater than 0.

---

### 🎥 Video Notes

---

#### 📝 Problem Description

_Describe the problem, challenge, or topic discussed in a video related to `SELECT FROM`._  
_What concept was explained or what exercise was solved?_

---

### DataBase Given

---

#### 💻 My SQL Code

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SQL COMMAND
```

---

#### 🧠 Solution Code / Explanation

```sql
SQL COMMAND
```

Explanation - Explain what you learned, any key takeaways, or how you solved the problem related to `COMMAND`._

---

[⬅️ Previous: IS NULL](isnull.md)   [Next ➡️ OR OPERATOR](oroperator.md)
