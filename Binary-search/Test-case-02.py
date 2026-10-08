""" for repeating query """

from Binary_search import located_cards
import timeit

# Test data 
cards = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10]
query = 4

# Expected output
expected_result = 8

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