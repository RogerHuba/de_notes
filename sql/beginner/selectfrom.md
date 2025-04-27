<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SELECT FROM

The `SELECT` statement is used to retrieve data from a database.  
The `FROM` clause specifies the table you want to select from.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

- `SELECT` defines which columns to retrieve.
- `FROM` specifies the table containing the data.

## Example

```sql
SELECT first_name, last_name
FROM employees;
```

- This query retrieves the first name and last name columns from the employees table.

## Key Points

- You can select one, multiple, or all columns (using `*`).
- Column order in `SELECT` matters for the output.
- Queries can include expressions (e.g., `SELECT salary * 1.1`).

## Additional Example

```sql
SELECT *
FROM customers;
```

- This query retrieves all columns from the customers table.

---

### 🎥 Video Notes

---

#### 📝 Problem Description

_Describe the problem, challenge, or topic discussed in a video related to `SELECT FROM`._  
_What concept was explained or what exercise was solved?_

---

#### 💻 SQL Code

```sql
-- Write your SQL code attempt or solution related to SELECT FROM
SELECT column1, column2
FROM table_name
WHERE condition;
```

---

#### 🧠 Solution Explanation

_Explain what you learned, any key takeaways, or how you solved the problem related to `SELECT FROM`._

---

[Main ⬅️](../../README.md)   [Next ➡️ WHERE CONDITION](wherecondition.md)
