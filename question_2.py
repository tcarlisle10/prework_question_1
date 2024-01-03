def first_odds():
    """Count odd numbers to 100"""
    current_number = 0 
    while current_number < 100:
        current_number += 1
        if current_number % 2 == 0:
            continue

        print(current_number)
    
first_odds()