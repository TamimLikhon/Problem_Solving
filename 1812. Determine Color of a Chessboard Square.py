class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter_to_number = ord(coordinates[0]) - ord('a') + 1
        number = int(coordinates[1])
        sum_indices = letter_to_number + number
        return sum_indices % 2 != 0