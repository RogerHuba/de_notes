<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUBQUERY WITH AGGREGATE FUNCTIONS

A subquery with aggregate functions is used to perform a calculation in a subquery and then use that result in the main query.  
It allows for comparisons against computed values like averages, maximums, or minimums.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE column_name > (SELECT AGG_FUNC(column_name) FROM another_table WHERE condition);
```

- The subquery uses an aggregate function like `AVG()`, `MAX()`, or `SUM()`.
- The outer query uses the result of the subquery for filtering or comparison.

## Example

```sql
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

- This query selects employees who earn more than the average salary.

## Key Points

- Subqueries with aggregates must be enclosed in parentheses `()`.
- The subquery must return a **single value** when used in a comparison.
- Common aggregate functions: `AVG()`, `SUM()`, `MIN()`, `MAX()`, `COUNT()`.

## Additional Example

```sql
SELECT product_name, price
FROM products
WHERE price = (SELECT MAX(price) FROM products);
```

- This query selects the product with the highest price.

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

[⬅️ Previous: HAVING CLAUSE](havingclause.md)   [Next ➡️ CASE STATEMENT](casestatment.md)
