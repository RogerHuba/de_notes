<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 COUNT OPERATOR

The `COUNT` function is used in SQL to return the number of rows that match a specified condition.  
It is often used with `GROUP BY` to count rows within each group.

---

## 🛠️ Basic Syntax

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

- `SELECT` specifies what you want to retrieve.
- `COUNT(column_name)` returns the number of non-null values in that column.
- `COUNT(*)` counts **all rows**, including rows with `NULL` values.

## Example

```sql
SELECT COUNT(*) 
FROM employees 
WHERE department = 'Sales';
```

- This query counts the number of employees who work in the Sales department.

## Key Points

- `COUNT(*)` counts all rows regardless of `NULL` values.
- `COUNT(column_name)` counts only rows where the column is **not NULL**.
- Commonly used with `GROUP BY` for group-level counts.

## Additional Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

- This query shows the number of employees in each department.

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

[⬅️ Previous: GROUP BY](groupby.md)   [Next ➡️ SUBQUERIES](subqueries.md)
