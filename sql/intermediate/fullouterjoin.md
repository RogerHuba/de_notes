<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 FULL OUTER JOIN

The `FULL OUTER JOIN` is used in SQL to return all records when there is a match in either the left or right table.  
If there is no match, `NULL` values are returned for the missing side.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name;
```

- `FULL OUTER JOIN` returns matching records from both tables.
- If there’s no match, it still returns the record with `NULL` for missing values.

## Example

```sql
SELECT employees.first_name, departments.department_name
FROM employees
FULL OUTER JOIN departments
ON employees.department_id = departments.department_id;
```

- This query lists all employees and departments, showing all records even if there is no match.

## Key Points

- Combines the results of `LEFT JOIN` and `RIGHT JOIN`.
- Rows without a match in one of the tables will have `NULL` values for that table's columns.
- Not all database systems (like MySQL) support `FULL OUTER JOIN` natively — workarounds like `UNION` may be required.

## Additional Example

```sql
SELECT customers.customer_name, orders.order_id
FROM customers
FULL OUTER JOIN orders
ON customers.customer_id = orders.customer_id;
```

- This query lists all customers and orders, even if a customer has no orders or an order has no customer.

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

[⬅️ Previous: INNER JOIN](innerjoin.md)   [Next ➡️ JOIN WITH WHERE](joinwithwhere.md)
