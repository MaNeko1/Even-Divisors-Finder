# Even Divisors of n  
> *Because odd numbers get too much attention.*

## About This Project  
This is a beginner-friendly Python script that takes an integer `n` as input and prints all of its **even divisors**.  
It’s a small and simple project—perfect for practicing loops, conditionals, and basic number logic in Python.

## How It Works  
The program loops through numbers from `1` to `n`, checks which numbers divide `n` evenly (`n % i == 0`), and filters out only the **even ones** (`i % 2 == 0`).  
It also calculates and prints the **sum** of these even divisors at the end.

## How to Use  
1. Open your terminal  
2. Run the script:
```bash
python even_divisors_finder.py
```
3.	Enter any positive integer when prompted
4.	See the list of even divisors and their total sum

## Example
```bash
n: 24  
2 divides 24 evenly and is even  
4 divides 24 evenly and is even  
6 divides 24 evenly and is even  
8 divides 24 evenly and is even  
12 divides 24 evenly and is even  
24 divides 24 evenly and is even  
Sum: 56
```

## Why This Is Useful
	•	Practice with for loops and if statements
	•	Learn how to use the modulo operator for checking divisibility
	•	Get comfortable with simple logic building blocks in Python
