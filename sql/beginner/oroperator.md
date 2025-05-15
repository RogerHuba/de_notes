<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 OR OPERATOR

The `OR` operator is used in SQL to combine multiple conditions in a `WHERE` clause.  
At least one of the conditions must be true for a row to be included in the result set.

---

## 🛠️ Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2;
```

- `SELECT` specifies the columns you want.
- `FROM` specifies the table.
- `WHERE` filters rows where **at least one** condition is true.

## Example

```sql
SELECT * FROM users WHERE city = 'New York' OR city = 'Los Angeles';
```

- This query selects all users who live in **New York** or **Los Angeles**.

## Key Points

- Only **one** of the conditions needs to be true for the row to be included.
- `OR` is useful when multiple acceptable values exist.
- Parentheses `()` can help organize complex logic when mixing `AND` and `OR`.

## Additional Example

```sql
SELECT * FROM products
WHERE category = 'Electronics' OR price < 100;
```

- This query selects all products that are in the **Electronics** category or have a `price` less than 100.

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

[⬅️ Previous: AND OPERATOR](andoperator.md)   [Next ➡️ NOT OPERATOR](notoperator.md)
