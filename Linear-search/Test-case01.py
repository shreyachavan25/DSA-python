""" Best case """

from Linear_search import located_cards
import timeit

# Test data
cards = [7, 13, 11, 3, 4, 5, 11, 1 ]
query = 7

# Expected output
expected_result = 0

# Actual output
actual_output = located_cards(cards, query)

# Measure Execution time
execution_time = timeit.timeit(lambda: located_cards(cards, query), number = 1000)

# Display the Test information 
print("----- Linear search Test case 01 -----")
print("cards             : ", cards)
print("query             : ", query)
print("Expected output   : ", expected_result)
print("Actual output     : ", actual_output)
print(" ")

# Check Whether test passed
if expected_result == actual_output:
    print("Test result       : PASSED")
else:
    print("Test result       : FAILED")

# Display execution time 
print("Execution time    : ",execution_time / 1000,"second")

