<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 JOIN WITH MULTIPLE KEYS

A `JOIN` with multiple keys uses more than one column to match rows between two tables.  
This is useful when a relationship between tables depends on a combination of columns rather than just one.

---

## 🛠️ Basic Syntax

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.column1 = table2.column1
AND table1.column2 = table2.column2;
```

- `JOIN` matches rows where **both** (or more) column conditions are satisfied.
- `AND` connects multiple key comparisons.

## Example

```sql
SELECT orders.order_id, products.product_name
FROM orders
JOIN products
ON orders.product_id = products.product_id
AND orders.product_version = products.product_version;
```

- This query matches orders to products based on both `product_id` and `product_version`.

## Key Points

- Useful when a **composite key** defines the relationship between tables.
- All join conditions must be true for a match to occur.
- You can add even more conditions if needed with additional `AND`s.

## Additional Example

```sql
SELECT enrollment.student_id, students.student_name
FROM enrollment
JOIN students
ON enrollment.student_id = students.student_id
AND enrollment.school_year = students.school_year;
```

- This query matches students based on both their ID and school year.

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

[⬅️ Previous: DISTINCT](distinct.md)   [Next ➡️ SELF JOIN](selfjoin.md)
