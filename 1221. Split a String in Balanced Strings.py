def balancedStringSplit(s: str) -> int:
    balance = 0
    max_balanced_strings = 0
    
    for char in s:
        if char == 'R':
            balance += 1
        elif char == 'L':
            balance -= 1
        
        if balance == 0:
            max_balanced_strings += 1
    
    return max_balanced_strings

# Example usage
s = "RLRRLLRLRL"
print(balancedStringSplit(s))  # Output should be 2
