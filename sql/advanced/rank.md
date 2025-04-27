<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 RANK

The `RANK()` function assigns a rank to each row within a partition of a result set.  
Rows with equal values receive the same rank, and the next rank(s) are skipped.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, 
       RANK() OVER (PARTITION BY column2 ORDER BY column3) AS rank
FROM table_name;
```

- `PARTITION BY` divides rows into groups (optional).
- `ORDER BY` determines the ranking order within each partition.

## Example

```sql
SELECT employee_id, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees;
```

- This query ranks employees by salary within each department.  
- Employees with the same salary receive the same rank.

## Key Points

- If two rows tie for a rank, the next rank will be skipped (e.g., 1, 1, 3).
- `RANK()` differs from `ROW_NUMBER()` because it allows ties.
- Useful for finding top performers, highest values, or competitive rankings.

## Additional Example

```sql
SELECT order_id, customer_id, 
       RANK() OVER (ORDER BY order_total DESC) AS order_rank
FROM orders;
```

- This query ranks orders by total amount, highest to lowest.

[⬅️ Previous: ROW NUMBER](rownumber.md)   [Next ➡️ LEAD](lead.md)
