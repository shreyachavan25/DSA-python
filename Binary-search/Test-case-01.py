""" Binary search """

from Binary_search import located_cards
import timeit

# Test data 
cards = [10, 20, 30, 40, 50, 60, 70]
query = 30

# Expected output
expected_result = 2

# Actual output
actual_output = located_cards(cards, query)

# Measure execution time 
execution_time = timeit.timeit(lambda: located_cards(cards, query), number = 1000)

# Display the Test information 
print("----- Linear search Test case 01 -----")
print("cards             : ", cards)
print("query             : ", query)
print("Expected output   : ", expected_result)
print("Actual output     : ", actual_output)
print(" ")

# Check whether test passed 
if expected_result == actual_output:
    print("Test result       : PASSED")
else:
    print("Test result       : FAILED")


#  Display time execution
print("Time execution    : ",execution_time )