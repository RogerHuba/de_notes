<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 ROW NUMBER

The `ROW_NUMBER()` function assigns a unique sequential integer to rows within a result set.  
It is often used for pagination, ranking, or ordering results uniquely.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, 
       ROW_NUMBER() OVER (PARTITION BY column2 ORDER BY column3) AS row_num
FROM table_name;
```

- `PARTITION BY` divides the rows into groups (optional).
- `ORDER BY` determines the sequence of row numbers within each partition.

## Example

```sql
SELECT employee_id, department_id, 
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
FROM employees;
```

- This query assigns a row number to each employee within their department, ordered by salary.

## Key Points

- Each row gets a unique number **starting from 1** within its partition.
- If `PARTITION BY` is omitted, the entire result set is treated as a single group.
- Useful for pagination by selecting ranges of rows.

## Additional Example

```sql
SELECT order_id, customer_id, 
       ROW_NUMBER() OVER (ORDER BY order_date) AS order_sequence
FROM orders;
```

- This query numbers all orders by order date, without partitioning.

[⬅️ Previous: WINDOW FUNCTION](windowfunction.md)   [Next ➡️ RANK](rank.md)
