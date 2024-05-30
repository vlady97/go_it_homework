import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or quantity <= 0:
        return []
        
    if max - min + 1 < quantity:
       return []
    
    unique_numbers = set()
    
    while len(unique_numbers) < quantity:
      unique_numbers.add(random.randint(min, max))
    
    return sorted(unique_numbers)
