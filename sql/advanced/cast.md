<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 CAST

The `CAST` function is used in SQL to convert a value from one data type to another.  
It is useful when you need to change how data is interpreted or formatted.

---

## 🛠️ Basic Syntax

```sql
SELECT CAST(expression AS target_data_type)
FROM table_name;
```

- `expression` is the value you want to convert.
- `target_data_type` is the data type you want to convert to.

## Example

```sql
SELECT CAST(salary AS CHAR(10)) AS salary_text
FROM employees;
```

- This query converts the `salary` number into text format.

## Key Points

- Common conversions include `INT`, `CHAR`, `DATE`, `DECIMAL`, and `FLOAT`.
- If conversion fails (invalid format), an error may occur.
- Some databases support both `CAST()` and `CONVERT()` with slight differences.

## Additional Example

```sql
SELECT CAST(order_date AS DATE) AS simple_date
FROM orders;
```

- This query casts a datetime value into a plain date format.

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

[⬅️ Previous: CONCAT](concat.md)   [Next ➡️ LENGTH](length.md)
