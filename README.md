# 🧠 Python Practice Exercises

A progressive set of hands‑on challenges—**simple → intermediate → advanced**—to sharpen your Python fundamentals before **[Python_For Pentesters_Basics](https://github.com/DairHX/Python_For_Pentesters_Basics)** and beyond.

---

## ✅ Simple Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 1 | **[Calculate the Factorial of a Number](./simple_exercises/ex01_factorial.py)** | Ask the user for a positive integer → use a loop to compute `n!` → return & print the result. |
| 2 | **[Sum of Digits of a Number](./simple_exercises/ex02_sum_of_numbers.py)** | Ask for an integer → treat it as a string → loop & sum the digits → print the total. |
| 3 | **[Find the Minimum and Maximum in a List](./simple_exercises/ex03_min_max_list.py)** | Ask for a list → use `min()` / `max()` → display both values. |
| 4 | **[Average of Several Numbers](./simple_exercises/ex04_average_list.py)** | Ask for numbers → compute `sum / len` → print the average. |
| 5 | **[Generate a Multiplication Table](./simple_exercises/ex05_multiplication_table.py)** | Ask for a base number & limit → loop and print `n × i` for each `i`. |
| 6 | **[Solve a First‑Degree Equation (ax + b = 0)](./simple_exercises/ex06_solve_linear_equation.py)** | Ask for `a`, `b` → if `a ≠ 0`, solve `x = −b/a`; else decide **no** / **infinite** solutions. |
| 7 | **[Sum of Squares in a List](./simple_exercises/ex07_sum_of_squares.py)** | Ask for a list → square each → sum & print. |
| 8 | **[Average of Even Numbers in a List](./simple_exercises/ex08_average_of_even_numbers.py)** | Ask for a list → filter evens → average them or report none. |
| 9 | **[Check if a List is Increasing](./simple_exercises/ex09_check_if_list_is_increasing.py)** | Verify each element is ≤ the next → print whether ascending. |

---

## ⚙️ Intermediate Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 10 | **[Find Prime Numbers in a List](./intermediate_exercises/ex10_primes_in_list.py)** | Write `is_prime()` → apply to the list → display primes. |
| 11 | **[Find Multiples in a Range](./intermediate_exercises/ex11_multiples_of_n_in_range.py)** | Given `n`, `a`, `b` → loop `a…b` → collect numbers divisible by `n`. |
| 12 | **[Calculate the GCD (Euclid’s Algorithm)](./intermediate_exercises/ex12_gcd_euclidean_algorithm.py)** | Ask for two integers → use Euclid’s method → print the GCD. |
| 13 | **[Generate Fibonacci Sequence](./intermediate_exercises/ex13_fibonacci_sequence.py)** | Ask for `n` → loop to build the sequence → print it. |
| 14 | **[Find Perfect Numbers in a List](./intermediate_exercises/ex14_perfect_numbers.py)** | Sum proper divisors → keep numbers equal to that sum → display them. |
| 15 | **[Celsius ↔ Fahrenheit Converter](./intermediate_exercises/ex15_celsius_fahrenheit_converter.py)** | Ask conversion direction → apply `C → F` or `F → C` formula → print result. |

---

## 🔬 Advanced Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 16 | **[Implement Selection Sort](./advanced_exercices/ex16_selection_sort_min_only.py)** | Repeatedly find the smallest element & move it front using `list.remove()` → print sorted list. |
| 17 | **[Check if a String is a Palindrome](./advanced_exercices/ex17_check_palindrome.py)** | Ignore spaces / punctuation / case → state if it’s a palindrome. |
| 18 | **[Solve a Quadratic Equation](./advanced_exercices/ex18_solve_quadratic_equation.py)** | Ask for `a`, `b`, `c` → compute `Δ = b² − 4ac` → output real or complex roots. |

---

### How to Run

```bash
# clone the repo
git clone https://github.com/your-username/python_practice.git
cd python_practice

# run any exercise
python ex01_factorial.py

