<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 UPPER & LOWER

The `UPPER` and `LOWER` functions are used in SQL to convert the case of text.  
They are helpful for standardizing data for searches, comparisons, or presentation.

---

## 🛠️ Basic Syntax

```sql
SELECT UPPER(column_name)
FROM table_name;

SELECT LOWER(column_name)
FROM table_name;
```

- `UPPER(column_name)` converts all letters to uppercase.
- `LOWER(column_name)` converts all letters to lowercase.

## Example

```sql
SELECT UPPER(first_name) AS uppercase_name
FROM employees;
```

- This query returns each employee's first name in all uppercase letters.

```sql
SELECT LOWER(email) AS normalized_email
FROM users;
```

- This query returns user emails in all lowercase.

## Key Points

- Useful for case-insensitive searches or comparisons.
- Original data in the database remains unchanged unless an `UPDATE` is performed.
- Some databases have functions like `INITCAP()` to capitalize the first letter of each word (e.g., PostgreSQL).

## Additional Example

```sql
SELECT LOWER(CONCAT(first_name, last_name)) AS combined_name
FROM customers;
```

- This query combines first and last names and converts the result to lowercase.

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

[⬅️ Previous: LEFT & RIGHT](leftright.md)   [Next ➡️ EXTRACT](extract.md)
