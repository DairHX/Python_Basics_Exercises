# 🧠 Python Practice Exercises

A progressive set of hands‑on challenges—**simple → intermediate → advanced**—to sharpen your Python fundamentals before **[Python_For Pentesters_Basics](https://github.com/DairHX/Python_For_Pentesters_Basics)** and beyond.

---

## ✅ Simple Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 1 | **[Calculate the Factorial of a Number](./simple_exercises/ex01_factorial.py)** | **Goal :** compute `n!` for a positive integer.<br>**Instructions :** prompt the user, reject non‑positive input, define a `factorial(n)` function that multiplies `1 × 2 × … × n` with a `for`‑loop, then print the result. |
| 2 | **[Sum of Digits of a Number](./simple_exercises/ex02_sum_of_numbers.py)** | **Goal :** add every digit of an integer.<br>**Instructions :** read an integer (may be negative; use its absolute value), convert to `str`, iterate through each character, cast back to `int`, accumulate the total, and display it. |
| 3 | **[Find the Minimum and Maximum in a List](./simple_exercises/ex03_min_max_list.py)** | **Goal :** identify the smallest and largest values.<br>**Instructions :** ask the user for a comma‑separated list, convert to `int`, then use built‑ins `min()` and `max()` and print both results. |
| 4 | **[Average of Several Numbers](./simple_exercises/ex04_average_list.py)** | **Goal :** calculate the arithmetic mean.<br>**Instructions :** read a list of numbers, ensure it is non‑empty, compute `sum(nums) / len(nums)` (floating‑point division), round if desired, and show the average. |
| 5 | **[Generate a Multiplication Table](./simple_exercises/ex05_multiplication_table.py)** | **Goal :** print `n × i` lines up to a limit.<br>**Instructions :** get a base number `n` and a maximum multiplier `m`, loop `1…m`, and print each line in the form `n × i = product`. |
| 6 | **[Solve a First‑Degree Equation (ax + b = 0)](./simple_exercises/ex06_solve_linear_equation.py)** | **Goal :** find `x` or state why none exists.<br>**Instructions :** prompt for `a` and `b`; if `a ≠ 0` output `x = −b / a`; if `a = 0` then `b = 0` ⇒ infinite solutions, else ⇒ no solution. |
| 7 | **[Sum of Squares in a List](./simple_exercises/ex07_sum_of_squares.py)** | **Goal :** return Σ `(num²)` for all items.<br>**Instructions :** read a list, square each element (e.g. list‑comprehension), sum them, and print the total. |
| 8 | **[Average of Even Numbers in a List](./simple_exercises/ex08_average_of_even_numbers.py)** | **Goal :** average only the even integers.<br>**Instructions :** filter numbers where `n % 2 == 0`; if none, print a friendly notice; otherwise, compute and show the average. |
| 9 | **[Check if a List is Increasing](./simple_exercises/ex09_check_if_list_is_increasing.py)** | **Goal :** verify ascending order (non‑decreasing).<br>**Instructions :** compare each element with the next (or compare to `sorted()` copy) and report `True`/`False`. |

---

## ⚙️ Intermediate Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 10 | **[Find Prime Numbers in a List](./intermediate_exercises/ex10_primes_in_list.py)** | **Goal :** return all primes found.<br>**Instructions :** implement `is_prime(n)` (handle `n < 2`), iterate over the user's list, collect primes, and print them (or “none found”). |
| 11 | **[Find Multiples in a Range](./intermediate_exercises/ex11_multiples_of_n_in_range.py)** | **Goal :** list every multiple of `n` between `a` and `b` (inclusive).<br>**Instructions :** prompt for `n`, `a`, `b`; loop through `range(a, b+1)`, test `x % n == 0`, append to a list, then output it. |
| 12 | **[Calculate the GCD (Euclid’s Algorithm)](./intermediate_exercises/ex12_gcd_euclidean_algorithm.py)** | **Goal :** compute the greatest common divisor.<br>**Instructions :** ask for two integers, repeatedly apply `a, b = b, a % b` until `b == 0`, then print `a` as the GCD. |
| 13 | **[Generate Fibonacci Sequence](./intermediate_exercises/ex13_fibonacci_sequence.py)** | **Goal :** produce the first `n` Fibonacci numbers.<br>**Instructions :** read `n`, start with `[0, 1]`, loop until the list has `n` items, append `prev + curr`, then print the sequence. |
| 14 | **[Find Perfect Numbers in a List](./intermediate_exercises/ex14_perfect_numbers.py)** | **Goal :** detect numbers equal to the sum of their proper divisors.<br>**Instructions :** for each number ≥ 2, find divisors up to `√n`, sum both divisors of each pair, compare to `n`, and collect perfect numbers. |
| 15 | **[Celsius ↔ Fahrenheit Converter](./intermediate_exercises/ex15_celsius_fahrenheit_converter.py)** | **Goal :** convert between scales accurately.<br>**Instructions :** ask the user which direction (C→F or F→C), read the temperature, apply `(C*9/5)+32` or `(F-32)*5/9`, and display the converted value formatted to one decimal place. |

---

## 🔬 Advanced Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 16 | **[Implement Selection Sort](./advanced_exercices/ex16_selection_sort_min_only.py)** | **Goal :** sort a list manually with selection sort.<br>**Instructions :** repeatedly find the minimum of the unsorted portion, remove it with `list.remove()`, append to a new list (or swap positions in‑place), then print the sorted result. |
| 17 | **[Check if a String is a Palindrome](./advanced_exercices/ex17_check_palindrome.py)** | **Goal :** test whether a phrase reads the same forward and backward.<br>**Instructions :** read a string, strip spaces, punctuation, convert to lower‑case, compare to its reverse, and print the verdict. |
| 18 | **[Solve a Quadratic Equation](./advanced_exercices/ex18_solve_quadratic_equation.py)** | **Goal :** find real or complex roots of `ax² + bx + c = 0`.<br>**Instructions :** prompt for `a`, `b`, `c`; compute `Δ = b² − 4ac`; if `Δ > 0` → two real roots, `Δ = 0` → one real root, `Δ < 0` → complex roots (use `cmath.sqrt`); print them clearly. |

---

### How to Run

```bash
# clone the repo
git clone https://github.com/your-username/python_practice.git
cd python_practice

# run any exercise
python simple_exercises/ex01_factorial.py
