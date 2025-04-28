<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUM OPERATOR

The `SUM` function is used in SQL to return the total sum of a numeric column.  
It is useful for calculating totals such as total sales, total salaries, or any other cumulative value.

---

## 🛠️ Basic Syntax

```sql
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

- `SUM(column_name)` adds together all the values in the specified column.
- Can be combined with `GROUP BY` to calculate sums for different groups.

## Example

```sql
SELECT SUM(salary)
FROM employees;
```

- This query returns the total of all salaries from the employees table.

## Key Points

- Only works with numeric columns.
- Ignores `NULL` values.
- Often paired with `GROUP BY` to calculate sums across groups.

## Additional Example

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

- This query shows the total salary expense for each department.

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

[⬅️ Previous: MIN OPERATOR](minoperator.md)   [Next ➡️ AVG OPERATOR](avgoperator.md)
