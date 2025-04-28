<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SELF JOIN

A `SELF JOIN` is a SQL operation where a table is joined with itself.  
It is useful for comparing rows within the same table.

---

## 🛠️ Basic Syntax

```sql
SELECT A.column1, B.column2
FROM table_name A
JOIN table_name B
ON A.common_column = B.common_column;
```

- You create table aliases (`A`, `B`) to differentiate between the two instances of the same table.
- The `ON` clause specifies how the rows are matched.

## Example

```sql
SELECT A.employee_id, A.first_name, B.manager_id, B.first_name AS manager_name
FROM employees A
JOIN employees B
ON A.manager_id = B.employee_id;
```

- This query lists employees along with the names of their managers.

## Key Points

- A `SELF JOIN` requires table aliases to avoid confusion.
- It behaves like a regular join but matches rows within the same table.
- Useful for hierarchical or relationship-based data (like employees and managers).

## Additional Example

```sql
SELECT A.customer_name AS referrer, B.customer_name AS referred
FROM customers A
JOIN customers B
ON A.customer_id = B.referrer_id;
```

- This query shows customers and the customers they referred.

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

[⬅️ Previous: JOIN WITH MULTIPLE KEYS](joinwithmultiplekeys.md)   [Next ➡️ UNION](union.md)
