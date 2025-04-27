<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 COALESCE

The `COALESCE` function is used in SQL to return the first non-NULL value in a list of expressions.  
It is helpful for handling missing or default values in queries.

---

## 🛠️ Basic Syntax

```sql
SELECT COALESCE(expression1, expression2, ..., default_value)
FROM table_name;
```

- `COALESCE` evaluates each expression in order and returns the first that is not `NULL`.
- If all expressions are `NULL`, it returns the specified default value.

## Example

```sql
SELECT first_name, COALESCE(phone_number, 'No Phone') AS contact_info
FROM employees;
```

- This query returns each employee’s phone number, or 'No Phone' if none exists.

## Key Points

- `COALESCE` is often used for data cleanup and display formatting.
- It can take two or more arguments.
- Useful in `SELECT` statements, `WHERE` clauses, or even `UPDATE` operations.

## Additional Example

```sql
SELECT customer_name, COALESCE(email, 'No Email Provided') AS email_contact
FROM customers;
```

- This query provides a fallback text if a customer’s email is missing.

[⬅️ Previous: EXTRACT](extract.md)   [Next ➡️ SUBQUERY IN CONDITION](subqueryincondition.md)
