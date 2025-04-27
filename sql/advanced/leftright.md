<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 LEFT & RIGHT

The `LEFT` and `RIGHT` functions are used in SQL to extract a specific number of characters from the start or end of a string.  
They are useful for isolating prefixes, suffixes, or parts of codes.

---

## 🛠️ Basic Syntax

```sql
SELECT LEFT(column_name, number_of_characters)
FROM table_name;

SELECT RIGHT(column_name, number_of_characters)
FROM table_name;
```

- `LEFT(column_name, n)` returns the first `n` characters from the left.
- `RIGHT(column_name, n)` returns the last `n` characters from the right.

## Example

```sql
SELECT LEFT(first_name, 3) AS name_start
FROM employees;
```

- This query extracts the first three letters of each employee's first name.

```sql
SELECT RIGHT(phone_number, 4) AS last_digits
FROM customers;
```

- This query extracts the last four digits of each customer's phone number.

## Key Points

- Useful for slicing fixed-format strings (like IDs, phone numbers, or zip codes).
- Combined with `TRIM`, they can clean and then extract portions of strings.
- Make sure the column has enough characters to avoid unexpected empty results.

## Additional Example

```sql
SELECT LEFT(product_code, 5) AS category_code
FROM products;
```

- This query extracts the first five characters from each product code to get the category code.

[⬅️ Previous: TRIM](trim.md)   [Next ➡️ UPPER & LOWER](upperlower.md)
