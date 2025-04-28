<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 IN OPERATOR

The `IN` operator is used in SQL to simplify multiple `OR` conditions.  
It allows you to specify multiple values in a `WHERE` clause.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column IN (value1, value2, ...);
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows where the column matches any value in the list.

## Example

```sql
SELECT * FROM users WHERE city IN ('New York', 'Los Angeles', 'Chicago');
```

- This query selects all users who live in **New York**, **Los Angeles**, or **Chicago**.

## Key Points

- The `IN` list must be enclosed in parentheses `()`.
- Each value inside the list must be separated by commas.
- Text values must be enclosed in single quotes (`'...'`).

## Additional Example

```sql
SELECT * FROM products
WHERE category IN ('Electronics', 'Furniture');
```

- This query selects all products that are in the **Electronics** or **Furniture** categories.

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

[⬅️ Previous: LIKE OPERATOR](likeoperator.md)   [Next ➡️ BETWEEN OPERATOR](betweenoperator.md)
