<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LIKE OPERATOR

The `LIKE` operator is used in SQL to search for a specified pattern in a column.  
It is often used with wildcard characters to match partial values.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column LIKE pattern;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows based on a matching pattern.

## Example

```sql
SELECT * FROM users WHERE first_name LIKE 'J%';
```

- This query selects all users whose `first_name` starts with the letter "J".

## Key Points

- `%` matches **zero or more characters**.
- `_` matches **exactly one character**.
- Patterns are case-insensitive in many SQL systems, but not all.
- Always enclose the pattern in single quotes (`'...'`).

## Additional Example

```sql
SELECT * FROM products
WHERE product_name LIKE '%phone';
```

- This query selects all products whose name **ends with** "phone".

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

[⬅️ Previous: LOGICAL OPERATORS](logicaloperator.md)   [Next ➡️ IN OPERATOR](inoperator.md)
