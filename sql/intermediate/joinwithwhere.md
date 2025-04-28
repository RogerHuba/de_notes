<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 JOIN WITH WHERE

Using a `JOIN` with a `WHERE` clause in SQL allows you to combine rows from multiple tables and then apply additional filters after the join.  
This approach helps narrow down the result set based on specific conditions.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;
```

- `JOIN` combines rows based on a related column between tables.
- `WHERE` filters the joined data based on specific criteria.

## Example

```sql
SELECT employees.first_name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.location = 'New York';
```

- This query lists employees who work in departments located in New York.

## Key Points

- The `JOIN` happens first, then `WHERE` filters the combined result.
- Filtering with `WHERE` is different from filtering by modifying the join itself (like `LEFT JOIN ... WHERE table2.column IS NULL`).
- Be cautious: a `WHERE` clause can turn an `OUTER JOIN` into an `INNER JOIN` if not written properly.

## Additional Example

```sql
SELECT customers.customer_name, orders.order_id
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id
WHERE orders.order_date >= '2024-01-01';
```

- This query returns customers and their orders placed on or after January 1, 2024.

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

[⬅️ Previous: FULL OUTER JOIN](fullouterjoin.md)   [Next ➡️ JOIN WITH COMPARISON](joinwithacomparisonoperator.md)
