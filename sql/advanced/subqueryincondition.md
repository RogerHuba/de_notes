<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUBQUERY IN CONDITION

A subquery in a condition is used to compare a value from the main query to the result of a subquery.  
It allows dynamic filtering based on the results of another query.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE column_name operator (SELECT column_name FROM another_table WHERE condition);
```

- The operator can be `=`, `IN`, `NOT IN`, `>`, `<`, `>=`, `<=`, etc.
- The subquery must return a single value or a list depending on the operator used.

## Example

```sql
SELECT first_name, last_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```

- This query selects employees who work in departments located in New York.

## Key Points

- If using `=`, the subquery must return only one value.
- If using `IN`, the subquery can return multiple values.
- Always ensure your subquery returns the right number of results for the operator.

## Additional Example

```sql
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

- This query selects products that have a price greater than the average price of all products.

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

[⬅️ Previous: COALESCE](coalesce.md)   [Next ➡️ WINDOW FUNCTION](windowfunction.md)
