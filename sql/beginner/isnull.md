<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 IS NULL

The `IS NULL` operator is used in SQL to test whether a column has a `NULL` value.  
It helps find rows where data is missing or undefined.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column IS NULL;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` checks if a column value is `NULL`.

## Example

```sql
SELECT * FROM users WHERE phone_number IS NULL;
```

- This query selects all users who do **not have** a phone number listed.

## Key Points

- `NULL` means **no value** or **unknown value**, not zero or empty string.
- Use `IS NULL` to find missing values.
- Use `IS NOT NULL` to find where values **do exist**.

## Additional Example

```sql
SELECT * FROM products
WHERE description IS NOT NULL;
```

- This query selects all products that **have a description**.

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

[⬅️ Previous: BETWEEN OPERATOR](betweenoperator.md)   [Next ➡️ AND OPERATOR](andoperator.md)
