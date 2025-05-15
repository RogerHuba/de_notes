<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 GROUP BY

The `GROUP BY` clause is used in SQL to arrange identical data into groups.  
It is commonly used with aggregate functions like `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN` to perform calculations on each group.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

- `SELECT` specifies the columns you want to retrieve.
- Aggregate functions are applied to the grouped data.
- `GROUP BY` determines how the rows are grouped together.
- `HAVING` speciifiesin the `GROUP BY` to display specific values

---

## Example

```sql
SELECT department, AVY(salary) as average salary 
FROM employees
GROUP BY department;
HAVING AVG(salary) > 50000
```

- This will calculate the average salary for each department and include only those deparrments where the average salary is greater than 50,000

---

## Key Points

- Every column in the `SELECT` list that is **not** inside an aggregate function must appear in the `GROUP BY`.
- `GROUP BY` happens **after** the `WHERE` clause but **before** `ORDER BY`.
- `GROUP BY` can group by one or more columns.
- When using GROUP BY, be aware that NULL values are treated as a single group. If you want to exclude NULL values from grouping, you can use the WHERE clause to filter them before applying GROUP BY.

---

## Combining GROUP BY with ORDER BY

You can use the ORDER BY clause along with GROUP BY to sort the grouped data based on specific criteria, making it easier to analyze the results. For example:

```sql
SELECT product_category, COUNT(*) AS product_count 
FROM products 
GROUP BY product_category 
ORDER BY product_count DESC;
```

This query will group products by their categories and display the product count in descending order, showing the most popular categories first.

---

## Additional Example

```sql
SELECT city, AVG(salary)
FROM employees
GROUP BY city;
```

- This query calculates the average salary for each city.

---

### 📝 Problem Description

Retrieve the department and the total salary expenses (sum of salaries) as "TotalSalaryExpenses" for each department. Display the results in descending order based on the "TotalSalaryExpenses".

---

### DataBase Given

Table: employees

ColumnNames DataType
employee_id int
first_name  varchar
last_name   varchar  
department  varchar
salary      decimal
manager_id  int

---

### Sample Data

Sample Input:

| employees |
|-----------|

| employee_id | first_name | last_name | department | salary | manager_id |
|-------------|------------|-----------|------------|--------|------------|
| 1 | John | Doe | Sales | 65000.00| 3 |
| 2 | Jane | Smith | Finance | 75000.00| 4 |
| 3 | Mike | Johnson | Sales | 80000.00| 5 |
| 4 | Emily | Davis | IT | 70000.00| 5 |
| 5 | Robert | Brown | HR | 90000.00| NULL |
| 6 | Maria | Garcia | Finance | 78000.00| 4 |
| 7 | Alex | Lee | HR | 85000.00| 5 |

Constraints:
The input table employees contains valid data.

Output Format:
A result set with columns:
department (varchar)
TotalSalaryExpenses (decimal)

Sample Output:

| department | TotalSalaryExpenses |
|------------|----------------------|
| HR | 175000.00 |
| Finance | 153000.00 |
| Sales | 145000.00 |
| IT | 70000.00 |

---

#### 💻 My SQL Code

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SELECT department,SUM(salary) AS TotalSalaryExpenses
FROM employees
GROUP BY department
```

---

##### Explanation - Explain what you learned

The results include the department and the total salary expenses (sum of salaries) as "TotalSalaryExpenses" for each department. The output is ordered in descending order based on the "TotalSalaryExpenses."

---

[⬅️ Previous: LIMIT OFFSET](limitoffset.md)   [Next ➡️ COUNT OPERATOR](countoperator.md)
