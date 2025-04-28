<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 TRIM

The `TRIM` function is used in SQL to remove unwanted spaces (or other characters) from the beginning and end of a string.  
It is helpful for cleaning up messy or inconsistent data.

---

## 🛠️ Basic Syntax

```sql
SELECT TRIM(column_name)
FROM table_name;
```

- `TRIM` removes leading and trailing spaces by default.
- Some databases allow you to specify which characters to trim.

## Example

```sql
SELECT TRIM(first_name) AS cleaned_first_name
FROM employees;
```

- This query removes any extra spaces at the start or end of each employee's first name.

## Key Points

- In MySQL and PostgreSQL, you can trim specific characters using `TRIM('x' FROM column_name)`.
- SQL Server uses `LTRIM()` for leading spaces and `RTRIM()` for trailing spaces separately.
- Cleaning data before comparisons or reports can prevent hidden errors.

## Additional Example

```sql
SELECT TRIM('   Hello World   ') AS trimmed_text;
```

- This query returns `'Hello World'` without the extra spaces.

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

[⬅️ Previous: CHARINDEX or SUBSTRING_INDEX](charindex.md)   [Next ➡️ LEFT & RIGHT](leftright.md)
