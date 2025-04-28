<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 RIGHT JOIN

The `RIGHT JOIN` is used in SQL to combine rows from two tables.  
It returns all records from the **right** table and the matching records from the **left** table.  
If there is no match, the result is `NULL` on the left side.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

- `RIGHT JOIN` keeps all records from the **right** table.
- If no matching record exists in the **left** table, `NULL` values are returned for the left table’s columns.

## Example

```sql
SELECT employees.first_name, departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id;
```

- This query returns all departments and their employees.  
- If a department has no employees, the employee fields will be `NULL`.

## Key Points

- `RIGHT JOIN` is also known as **RIGHT OUTER JOIN**.
- All records from the right table appear in the result set.
- Only matching records from the left table are included.
- Useful for finding records that exist in the right table but not necessarily in the left.

## Additional Example

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.customer_id;
```

- This query lists all customers and any associated orders, even if the customer has no orders.

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

[⬅️ Previous: LEFT JOIN](leftjoin.md)   [Next ➡️ INNER JOIN](innerjoin.md)
