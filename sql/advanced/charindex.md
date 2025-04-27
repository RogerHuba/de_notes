<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 CHARINDEX or SUBSTRING_INDEX

`CHARINDEX` (SQL Server) and `SUBSTRING_INDEX` (MySQL) are functions used to find the position of a substring within a string.  
They help locate specific parts of a text based on content.

---

## 🛠️ Basic Syntax

**SQL Server (CHARINDEX):**

```sql
SELECT CHARINDEX('substring', column_name)
FROM table_name;
```

**MySQL (SUBSTRING_INDEX):**

```sql
SELECT SUBSTRING_INDEX(column_name, 'delimiter', count)
FROM table_name;
```

- `CHARINDEX` returns the starting position of the substring.
- `SUBSTRING_INDEX` returns part of a string before or after a specified number of occurrences of the delimiter.

## Example

**Using CHARINDEX (SQL Server):**

```sql
SELECT CHARINDEX('Smith', last_name) AS position
FROM employees;
```

- This query finds where 'Smith' starts in the `last_name`.

**Using SUBSTRING_INDEX (MySQL):**

```sql
SELECT SUBSTRING_INDEX(email, '@', 1) AS username
FROM users;
```

- This query extracts everything before the `@` in the email address.

## Key Points

- `CHARINDEX` returns an integer position; 0 if not found.
- `SUBSTRING_INDEX` can return left or right parts of a string based on positive or negative `count`.
- These functions are database-specific — check your SQL flavor!

## Additional Example

**CHARINDEX Example:**

```sql
SELECT CHARINDEX('a', product_name) AS first_a_position
FROM products;
```

**SUBSTRING_INDEX Example:**

```sql
SELECT SUBSTRING_INDEX(full_address, ',', 1) AS city
FROM customers;
```

[⬅️ Previous: SUBSTRING](substring.md)   [Next ➡️ TRIM](trim.md)
