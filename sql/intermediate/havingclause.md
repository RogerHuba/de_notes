<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 HAVING CLAUSE

The `HAVING` clause is used in SQL to filter groups of rows after aggregation.  
It works like `WHERE`, but it operates on grouped data after `GROUP BY`.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

- `GROUP BY` groups the result set by one or more columns.
- `HAVING` filters the grouped records based on an aggregate function or condition.

## Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

- This query returns departments that have more than 5 employees.

## Key Points

- `WHERE` filters **before** grouping, `HAVING` filters **after** grouping.
- `HAVING` is typically used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN`.
- You can use both `WHERE` and `HAVING` together in a query.

## Additional Example

```sql
SELECT city, AVG(salary)
FROM employees
GROUP BY city
HAVING AVG(salary) > 70000;
```

- This query selects cities where the average salary is greater than $70,000.

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

[⬅️ Previous: AVG OPERATOR](avgoperator.md)   [Next ➡️ SUBQUERY WITH AGGREGATE FUNCTIONS](subquerywithaggregatedfunctions.md)
