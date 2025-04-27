<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 WITH STATEMENTS

The `WITH` statement, also known as a Common Table Expression (CTE), is used in SQL to define a temporary named result set.  
It makes queries easier to read, especially when dealing with complex subqueries.

---

## 🛠️ Basic Syntax

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

- `WITH` defines the CTE.
- You can reference the CTE just like a regular table in the following `SELECT`.

## Example

```sql
WITH SalesCTE AS (
    SELECT employee_id, SUM(sale_amount) AS total_sales
    FROM sales
    GROUP BY employee_id
)
SELECT employee_id, total_sales
FROM SalesCTE
WHERE total_sales > 10000;
```

- This query calculates total sales per employee, then selects only those with sales over 10,000.

## Key Points

- CTEs improve query readability by breaking down complex logic.
- You can define multiple CTEs by separating them with commas.
- CTEs exist only during the execution of the query — they are not stored.

## Additional Example

```sql
WITH RecentOrders AS (
    SELECT order_id, order_date
    FROM orders
    WHERE order_date >= '2024-01-01'
)
SELECT *
FROM RecentOrders;
```

- This query first creates a CTE for orders in 2024, then selects from it.

[⬅️ Previous: LEAD](lead.md)   [Back to Main](../../README.md)
