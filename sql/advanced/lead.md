<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LEAD

The `LEAD()` function is used in SQL to access data from the next row in the result set, without using a self-join.  
It is helpful for comparing a row to the row that follows it.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, 
       LEAD(column2, offset, default_value) OVER (PARTITION BY column3 ORDER BY column4) AS next_value
FROM table_name;
```

- `column2` is the column to look ahead.
- `offset` (optional) specifies how many rows forward to look (default is 1).
- `default_value` (optional) is returned if there is no next row.

## Example

```sql
SELECT employee_id, salary,
       LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_highest_salary
FROM employees;
```

- This query shows each employee’s salary and the salary of the next highest-paid employee.

## Key Points

- `LEAD()` is often used for gap analysis, trend comparisons, or sequential reporting.
- If there is no next row, it returns `NULL` unless a default value is specified.
- Works great in combination with `PARTITION BY` for grouped data.

## Additional Example

```sql
SELECT order_id, order_date,
       LEAD(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_order_date
FROM orders;
```

- This query shows each customer's next order date based on their current order.

[⬅️ Previous: RANK](rank.md)   [Next ➡️ WITH STATEMENTS](withstatements.md)
