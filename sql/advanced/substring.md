<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 SUBSTRING

The `SUBSTRING` function is used in SQL to extract a part of a string starting at a specified position for a specified length.  
It is useful for isolating specific sections of text from a larger string.

---

## 🛠️ Basic Syntax

```sql
SELECT SUBSTRING(column_name, start_position, length)
FROM table_name;
```

- `start_position` specifies where to begin extraction (starting at 1).
- `length` defines how many characters to return.

## Example

```sql
SELECT SUBSTRING(first_name, 1, 3) AS short_name
FROM employees;
```

- This query returns the first three characters of each employee’s first name.

## Key Points

- Positions start at 1, not 0, in most SQL databases.
- If `length` exceeds the remaining characters, the function returns up to the end of the string.
- In some databases like MySQL, `SUBSTRING()` and `SUBSTR()` are interchangeable.

## Additional Example

```sql
SELECT SUBSTRING(product_name, 5, 10) AS partial_product
FROM products;
```

- This query extracts 10 characters from `product_name`, starting at the 5th character.

[⬅️ Previous: LENGTH](length.md)   [Next ➡️ CHARINDEX or SUBSTRING_INDEX](charindex.md)
