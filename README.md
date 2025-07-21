# 🧠 Python Practice Exercises

A progressive set of hands‑on challenges—**simple → intermediate → advanced**—to sharpen your Python fundamentals before **[Python_For Pentesters_Basics](https://github.com/DairHX/Python_For_Pentesters_Basics))** and beyond.

---

## ✅ Simple Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 1 | **[Calculate the Factorial of a Number](./factorial.py)** | Ask the user for a positive integer → use a loop to compute `n!` → return & print the result. |
| 2 | **[Sum of Digits of a Number](./sum_of_digits.py)** | Ask for an integer → treat it as a string to access each character → loop & sum the digits → print the total. |
| 3 | **[Find the Minimum and Maximum in a List](./min_max.py)** | Ask for a list of numbers → use built‑ins `min()` / `max()` → display both values. |
| 4 | **[Average of Several Numbers](./average.py)** | Ask for a list of numbers → compute `sum / len` → print the average. |
| 5 | **[Generate a Multiplication Table](./multiplication_table.py)** | Ask for a base number and an upper limit → loop and print `n × i` for every `i` up to the limit. |
| 6 | **[Solve a First‑Degree Equation (ax + b = 0)](./linear_equation.py)** | Ask for `a` and `b` → if `a ≠ 0`, solve `x = −b/a`; if `a = 0`, decide whether there’s **no** or **infinite** solutions. |
| 7 | **[Sum of Squares in a List](./sum_of_squares.py)** | Ask for a list of numbers → square each → sum and print the result. |
| 8 | **[Average of Even Numbers in a List](./average_even.py)** | Ask for a list → filter evens → compute average or print a “no even numbers” message. |
| 9 | **[Check if a List is Increasing](./is_increasing.py)** | Ask for a list → verify each element is ≤ the next → print whether it’s sorted ascendingly. |

---

## ⚙️ Intermediate Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 10 | **[Find Prime Numbers in a List](./find_primes.py)** | Implement an `is_prime()` helper → apply it to the user’s list → return & display all primes. |
| 11 | **[Find Multiples in a Range](./find_multiples.py)** | Given `n`, `a`, `b` → loop from `a` to `b` → collect numbers divisible by `n`. |
| 12 | **[Calculate the GCD (Euclid’s Algorithm)](./gcd.py)** | Ask for two integers → use Euclid’s iterative method → print the GCD. |
| 13 | **[Generate Fibonacci Sequence](./fibonacci.py)** | Ask for `n` terms → loop to build the sequence → return & print it. |
| 14 | **[Find Perfect Numbers in a List](./perfect_numbers.py)** | For each number, sum its proper divisors → if equal to the number, keep it → display all perfect numbers found. |
| 15 | **[Celsius ↔ Fahrenheit Converter](./temp_converter.py)** | Ask conversion direction → apply `C → F` or `F → C` formula → print the converted value. |

---

## 🔬 Advanced Exercises

| # | Exercise | Goal / Instructions |
|---|----------|---------------------|
| 16 | **[Implement Selection Sort](./selection_sort.py)** | Ask for a list → repeatedly find the smallest element and move it to the front using `list.remove()` → print the sorted list. |
| 17 | **[Check if a String is a Palindrome](./palindrome.py)** | Ask for a string → ignore spaces / punctuation / case → print whether it’s a palindrome. |
| 18 | **[Solve a Quadratic Equation](./quadratic_equation.py)** | Ask for `a`, `b`, `c` → compute the discriminant `Δ = b² − 4ac` → report real or complex roots. |

---

### How to Run

```bash
# clone the repo
git clone https://github.com/your‑username/python_practice.git
cd python_practice

# run any exercise
python factorial.py

