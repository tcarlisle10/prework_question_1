def first_odds():
    """Count odd numbers to 100"""
    odd_numbers = 0 
    while odd_numbers < 100:
        odd_numbers += 1
        if odd_numbers % 2 == 0:
            continue

        print(odd_numbers)
    
first_odds()