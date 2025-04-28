<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LEFT JOIN

The `LEFT JOIN` is used in SQL to combine rows from two tables.  
It returns all records from the **left** table and the matching records from the **right** table.  
If there is no match, the result is `NULL` on the right side.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

- `LEFT JOIN` keeps all records from the **left** table.
- If no matching record exists in the **right** table, `NULL` values are returned for the right table’s columns.

## Example

```sql
SELECT employees.first_name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

- This query returns all employees and their department names.  
- If an employee does not belong to any department, the department name will be `NULL`.

## Key Points

- `LEFT JOIN` is also known as **LEFT OUTER JOIN**.
- All records from the left table appear in the result set.
- Only matching records from the right table are included.
- Useful for identifying unmatched or orphan records.

## Additional Example

```sql
SELECT customers.customer_name, orders.order_id
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

- This query lists all customers and their corresponding order IDs, even if they haven't placed any orders.

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

[⬅️ Previous: CASE STATEMENT](casestatement.md)   [Next ➡️ RIGHT JOIN](rightjoin.md)
