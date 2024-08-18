class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        sm = int(ord(coordinates[0]) - ord("a")) + 1 + int(coordinates[1])

        return sm % 2 != 0