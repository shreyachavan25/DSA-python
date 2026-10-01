# Linear Search

## 📌 Overview

Linear Search is a simple searching algorithm that checks each element of a list sequentially until the required element is found.

It is one of the fundamental searching algorithms and is useful for understanding basic searching logic and algorithmic complexity.

---

## 🎯 Objective

The objective of this implementation is to:

- Understand the working of Linear Search.
- Implement Linear Search using Python.
- Handle different input cases, including an empty list.
- Test the algorithm using multiple test cases.
- Analyze its best, average, and worst-case performance.

---

## ⚙️ Algorithm

1. Start from the first element of the list.
2. Compare the current element with the target value.
3. If the element matches the target, return its position.
4. If it does not match, move to the next element.
5. Continue until the target is found or the entire list is checked.
6. Return `-1` if the target is not present in the list.

---

## 💻 Implementation

The main implementation is available in:

`Linear_search.py`

The function used is:

`located_cards(cards, query)`

It returns:

- The index of the target element if it is found.
- `-1` if the target element is not found.

---

## 🧪 Test Cases

Multiple test cases are used to verify the implementation, including:

| Test Case | Scenario |
|-----------|----------|
| Test Case 01 | Best Case |
| Test Case 02 | Average Case |
| Test Case 03 | Worst Case |
| Test Case 04 | Element Not Found |
| Test Case 05 | Empty List |

Each test case checks:

- Input list
- Target value
- Expected output
- Actual output
- Test result
- Execution time

---

## ⏱️ Time Complexity

| Case | Time Complexity |
|------|-----------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

### Space Complexity

**O(1)** auxiliary space.

---

## 📊 Performance Measurement

Python's `timeit` module is used to measure the execution time of the search function.

The function is executed multiple times to obtain a more meaningful timing measurement.

Example:

```python
timeit.timeit(
    lambda: located_cards(cards, query),
    number=2000
)