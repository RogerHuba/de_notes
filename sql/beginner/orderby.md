<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 ORDER BY

The `ORDER BY` clause is used in SQL to sort the result set by one or more columns.  
By default, it sorts the results in ascending order unless specified otherwise.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `ORDER BY` defines how to sort the results.

## Example

```sql
SELECT * FROM users ORDER BY last_name ASC;
```

- This query selects all users and sorts them by `last_name` in ascending order.

## Key Points

- `ASC` = Ascending order (smallest to largest, A to Z).
- `DESC` = Descending order (largest to smallest, Z to A).
- You can sort by multiple columns.
- The default sort order is `ASC` if you don't specify.

## Additional Example

```sql
SELECT * FROM products
ORDER BY price DESC, product_name ASC;
```

- This query sorts products by `price` in descending order, and for products with the same price, by `product_name` in ascending order.

---

### 🎥 Video Notes

---

#### 📝 Problem Description

_Describe the problem, challenge, or topic discussed in a video related to `SELECT FROM`._  
_What concept was explained or what exercise was solved?_

---

### DataBase Given

---

#### 🧠 Solution Code / Explanation

```sql
-- Write your SQL code attempt or solution related to SQL COMMAND
SQL COMMAND
```

---

[⬅️ Previous: NOT OPERATOR](notoperator.md)   [Next ➡️ LIMIT OFFSET](limitoffset.md)
