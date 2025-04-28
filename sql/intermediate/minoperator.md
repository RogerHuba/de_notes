<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 MIN OPERATOR

The `MIN` function is used in SQL to return the lowest value in a specified column.  
It is useful for finding the smallest number, earliest date, or alphabetically first string.

---

## 🛠️ Basic Syntax

```sql
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

- `MIN(column_name)` returns the minimum value from the specified column.
- Can be combined with `GROUP BY` to find minimum values within groups.

## Example

```sql
SELECT MIN(salary)
FROM employees;
```

- This query returns the lowest salary from the employees table.

## Key Points

- Works with numeric, date, and text columns (for text, it returns the alphabetically first value).
- Ignores `NULL` values.
- Can be used inside a subquery or with `GROUP BY`.

## Additional Example

```sql
SELECT department, MIN(salary)
FROM employees
GROUP BY department;
```

- This query shows the lowest salary for each department.

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

[⬅️ Previous: MAX OPERATOR](maxoperator.md)   [Next ➡️ SUM OPERATOR](sumoperator.md)
