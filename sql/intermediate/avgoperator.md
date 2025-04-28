<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 AVG OPERATOR

The `AVG` function is used in SQL to return the average value of a numeric column.  
It is useful for finding the mean value of data, such as average salary or average sales.

---

## 🛠️ Basic Syntax

```sql
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

- `AVG(column_name)` calculates the average of the values in the specified column.
- Can be combined with `GROUP BY` to find averages within different groups.

## Example

```sql
SELECT AVG(salary)
FROM employees;
```

- This query returns the average salary of all employees.

## Key Points

- Only works with numeric columns.
- Ignores `NULL` values when calculating the average.
- Commonly used with `GROUP BY` to calculate averages per group.

## Additional Example

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

- This query shows the average salary for each department.

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

[⬅️ Previous: SUM OPERATOR](sumoperator.md)   [Next ➡️ HAVING CLAUSE](havingclause.md)
