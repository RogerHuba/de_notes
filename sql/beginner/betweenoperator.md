<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 BETWEEN OPERATOR

The `BETWEEN` operator is used in SQL to filter the result set within a certain range.  
It selects values within a given minimum and maximum boundary.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column BETWEEN value1 AND value2;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows where the column is within the specified range.

## Example

```sql
SELECT * FROM users WHERE age BETWEEN 18 AND 30;
```

- This query selects all users whose `age` is between 18 and 30, inclusive.

## Key Points

- `BETWEEN` is **inclusive** — it includes the boundary values.
- You must use `AND` to specify the lower and upper bounds.
- Works with numbers, text, and dates.

## Additional Example

```sql
SELECT * FROM products
WHERE price BETWEEN 100 AND 500;
```

- This query selects all products with a `price` between 100 and 500.

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

[⬅️ Previous: IN OPERATOR](inoperator.md)   [Next ➡️ IS NULL](isnull.md)
