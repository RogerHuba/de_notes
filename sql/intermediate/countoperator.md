<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 COUNT OPERATOR

The `COUNT` function is used in SQL to return the number of rows that match a specified condition.  
It is often used with `GROUP BY` to count rows within each group.

---

## 🛠️ Basic Syntax

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

- `SELECT` specifies what you want to retrieve.
- `COUNT(column_name)` returns the number of non-null values in that column.
- `COUNT(*)` counts **all rows**, including rows with `NULL` values.

---

## Example

```sql
SELECT COUNT(*) as count_result
FROM employees 
WHERE department = 'Sales';
```

- This query counts the number of employees who work in the Sales department.
- count_result is what will be displayed

---

## Key Points

- `COUNT(*)` counts all rows regardless of `NULL` values.
- `COUNT(column_name)` counts only rows where the column is **not NULL**.
- Commonly used with `GROUP BY` for group-level counts.

---

### Handling NULL Values

By default, the COUNT function includes NULL values in its calculation. However, you can exclude NULL values by using the COUNT(column_name) function on a specific column that does not contain NULL values. For example:

```sql
SELECT COUNT(salary) AS non_null_salaries 
FROM employees;
```

This query will count the number of non-NULL salary values in the "employees" table.

---

### Counting Distinct Values

To count distinct (unique) values in a column, you can use the COUNT(DISTINCT column_name) syntax. This allows you to obtain unique occurrence counts. For example:

```sql
SELECT COUNT(DISTINCT department) AS distinct_departments 
FROM employees;
```

This query will count the number of unique departments in the "employees" table.

---

## Additional Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

- This query shows the number of employees in each department.

---

### 📝 Problem Description

Retrieve the department and the count of employees as "EmployeeCount" in each department. Display the results in descending order based on the "EmployeeCount".

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

Sample Input:

| employees                                     |
|-----------------------------------------------|

| employee_id | first_name | last_name | department | salary | manager_id |
|-------------|------------|-----------|------------|--------|------------|
| 1           | John       | Doe       | Sales      | 65000.00| 3          |
| 2           | Jane       | Smith     | Finance    | 75000.00| 4          |
| 3           | Mike       | Johnson   | Sales      | 80000.00| 5          |
| 4           | Emily      | Davis     | IT         | 70000.00| 5          |
| 5           | Robert     | Brown     | HR         | 90000.00| NULL       |
| 6           | Maria      | Garcia    | Finance    | 78000.00| 4          |
| 7           | Alex       | Lee       | HR         | 85000.00| 5          |

Constraints:
The input table employees contains valid data.

Output Format:
A result set with columns:
department (varchar)
EmployeeCount (int)

Sample Output:

| department | EmployeeCount |
|------------|---------------|
| Sales      | 2             |
| HR         | 2             |
| Finance    | 2             |
| IT         | 1             |

---

#### 💻 My SQL Code

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SELECT department, COUNT(*) as EmplyeeCount
FROM employees
GROUP BY department ASC
```

---

#### Explanation

The results include the department and the count of employees in each department. The output is ordered in descending order based on the "EmployeeCount."

---

[⬅️ Previous: GROUP BY](groupby.md)   [Next ➡️ SUBQUERIES](subqueries.md)
