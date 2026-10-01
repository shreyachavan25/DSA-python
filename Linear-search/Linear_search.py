""" Linear search """

def located_cards(cards, query):

    if not cards:
        return -1

    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:

        # Check if element at the current position matche the quetry
        if cards[position] == query:
            
            # Answer found! Return and exit...
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array 
        if position == len(cards):
             
            # Number not found, return -1
             return -1



