# Happy Number Checker

This program checks whether a given number is a **happy number** or not.

## What is a Happy Number?

A happy number is a number which eventually reaches 1 when replaced by the sum of the squares of its digits repeatedly.
If this process results in an endless loop that does not include 1, the number is **not happy**.

## 🔥 How to Use

1. Run the script.
   ```python
   python main.py
  
3. Enter a number when prompted.
4. The program will output `True` if the number is happy, otherwise `False`.

## Examples

```python
>>> check_happy(7)
True

>>> check_happy(8)
False
