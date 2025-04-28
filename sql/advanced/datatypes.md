<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# 📚 DATA TYPES

Data types in SQL define the kind of data that can be stored in a table column.  
Choosing the correct data type ensures data accuracy, optimizes storage, and improves performance.

---

## 🛠️ Basic Syntax

```sql
CREATE TABLE table_name (
    column1 INT,
    column2 VARCHAR(255),
    column3 DATE
);
```

- `INT` is used for integers.
- `VARCHAR(n)` is used for variable-length text up to `n` characters.
- `DATE` is used for storing calendar dates.

## Example

```sql
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    hire_date DATE
);
```

- This creates an `employees` table with an integer ID, a string for first name, and a date for hire date.

## Key Points

- Always choose the smallest data type that fits your data to save space.
- Text fields are typically `VARCHAR`, while fixed-length text can be `CHAR`.
- Dates and times should use specific types like `DATE`, `TIME`, or `DATETIME`.

## Additional Example

```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
```

- This creates a `products` table where `price` allows numbers with up to 10 digits total and 2 after the decimal.

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

[⬅️ Previous: UNION](../intermediate/union.md)   [Next ➡️ CONCAT](concat.md)
