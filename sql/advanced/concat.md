<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 CONCAT

The `CONCAT` function is used in SQL to join two or more strings into a single string.  
It is commonly used to combine columns or add text into results.

---

## 🛠️ Basic Syntax

```sql
SELECT CONCAT(string1, string2, ...) AS combined_column
FROM table_name;
```

- `CONCAT` joins multiple strings or columns into one.
- The result is returned as a single string.

## Example

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;
```

- This query combines `first_name` and `last_name` with a space in between to create a `full_name`.

## Key Points

- If any argument is `NULL`, the result will also be `NULL` (unless using `CONCAT_WS()` in some databases).
- Use single quotes `' '` to add spaces, commas, or other separators.
- Some databases also have `CONCAT_WS(separator, string1, string2, ...)` to specify a separator automatically.

## Additional Example

```sql
SELECT CONCAT(city, ', ', state) AS location
FROM customers;
```

- This query combines `city` and `state` into a single `location` string separated by a comma and space.

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

[⬅️ Previous: DATA TYPES](datatypes.md)   [Next ➡️ CAST](cast.md)
