<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 INNER JOIN

The `INNER JOIN` is used in SQL to return only the rows that have matching values in both tables.  
It excludes records where no match is found between the two tables.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

- `INNER JOIN` returns rows when there is a match in both tables.
- Only matched records appear in the result set.

## Example

```sql
SELECT employees.first_name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

- This query lists employees along with their department names, but only for employees assigned to a department.

## Key Points

- `INNER JOIN` is the most commonly used join type.
- If there is no match between the tables, the row is **not included** in the result.
- Multiple joins can be combined in one query to join more than two tables.

## Additional Example

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

- This query lists orders along with the corresponding customer names where a customer has actually placed an order.

[⬅️ Previous: RIGHT JOIN](rightjoin.md)   [Next ➡️ FULL OUTER JOIN](fullouterjoin.md)
