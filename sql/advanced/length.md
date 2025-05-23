<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LENGTH

The `LENGTH` function is used in SQL to return the number of characters (or bytes) in a string.  
It helps analyze string sizes or validate input lengths.

---

## 🛠️ Basic Syntax

```sql
SELECT LENGTH(column_name)
FROM table_name;
```

- `LENGTH(column_name)` returns the length of the text in characters (or bytes, depending on the database).

## Example

```sql
SELECT LENGTH(first_name) AS name_length
FROM employees;
```

- This query returns the number of characters in each employee's first name.

## Key Points

- In some databases (like MySQL), `LENGTH` returns **bytes**, while `CHAR_LENGTH` returns **characters**.
- For Unicode strings (e.g., UTF-8), the number of bytes may differ from the number of characters.
- Always check your database documentation if exact character count vs byte count matters.

## Additional Example

```sql
SELECT LENGTH(description) AS description_length
FROM products;
```

- This query measures the length of each product description.

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

[⬅️ Previous: CAST](cast.md)   [Next ➡️ SUBSTRING](substring.md)
