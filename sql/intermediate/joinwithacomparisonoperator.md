<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 JOIN WITH COMPARISON

A `JOIN` with a comparison operator allows you to join tables based on more complex relationships than simple equality.  
You can use operators like `>`, `<`, `>=`, `<=`, `<>`, or even `BETWEEN` in the `ON` clause.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.column_name operator table2.column_name;
```

- `JOIN` combines rows based on a specified condition, not just equality.
- The `operator` could be `=`, `>`, `<`, `>=`, `<=`, `<>`, or others.

## Example

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

- In this basic example, a standard equality operator is used to join orders to their customers.

## Key Points

- Comparisons other than `=` are less common but useful for advanced queries.
- You can join tables based on date ranges, value comparisons, or custom logic.
- Always ensure that your comparison condition makes logical sense to avoid unexpected results.

## Additional Example

```sql
SELECT employees.first_name, projects.project_name
FROM employees
JOIN projects
ON employees.experience_years >= projects.required_experience_years;
```

- This query matches employees to projects where their experience is greater than or equal to the project's required experience.

[⬅️ Previous: JOIN WITH WHERE](joinwithwhere.md)   [Next ➡️ DISTINCT](distinct.md)
