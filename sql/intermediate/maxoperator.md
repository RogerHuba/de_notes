<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 MAX OPERATOR

The `MAX` function is used in SQL to return the highest value in a specified column.  
It is often used to find the largest number, latest date, or alphabetically last string.

---

## 🛠️ Basic Syntax

```sql
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

- `MAX(column_name)` returns the maximum value from the specified column.
- Can be combined with `GROUP BY` to find maximum values within groups.

## Example

```sql
SELECT MAX(salary)
FROM employees;
```

- This query returns the highest salary from the employees table.

## Key Points

- Works with numeric, date, and text columns (for text, it returns the alphabetically last value).
- Ignores `NULL` values.
- Can be used inside a subquery to filter records.

## Additional Example

```sql
SELECT department, MAX(salary)
FROM employees
GROUP BY department;
```

- This query shows the highest salary for each department.

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

#### Explanation

---

[⬅️ Previous: SUBQUERIES](subqueries.md)   [Next ➡️ MIN OPERATOR](minoperator.md)
