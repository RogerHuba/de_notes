<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 CASE STATEMENT

The `CASE` statement is used in SQL to create conditional logic within a query.  
It allows you to return different values based on different conditions.

---

## 🛠️ Basic Syntax

```sql
SELECT column1,
  CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE result3
  END AS new_column
FROM table_name;
```

- `CASE` checks conditions in order and returns the first matching result.
- If no conditions match, the `ELSE` value is returned.
- `END` closes the `CASE` statement and assigns an alias if needed.

## Example

```sql
SELECT first_name, salary,
  CASE
    WHEN salary > 80000 THEN 'High'
    WHEN salary BETWEEN 50000 AND 80000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_level
FROM employees;
```

- This query categorizes employees based on their salary range.

## Key Points

- `CASE` can be used in `SELECT`, `ORDER BY`, and `WHERE` clauses.
- The `ELSE` part is optional; if omitted and no condition matches, `NULL` is returned.
- Useful for creating dynamic, readable results without needing multiple queries.

## Additional Example

```sql
SELECT product_name, price,
  CASE
    WHEN price > 500 THEN 'Expensive'
    WHEN price BETWEEN 100 AND 500 THEN 'Moderate'
    ELSE 'Cheap'
  END AS price_category
FROM products;
```

- This query classifies products into price categories.

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

[⬅️ Previous: SUBQUERY WITH AGGREGATE FUNCTIONS](subquerywithaggregatedfunctions.md)   [Next ➡️ LEFT JOIN](leftjoin.md)
