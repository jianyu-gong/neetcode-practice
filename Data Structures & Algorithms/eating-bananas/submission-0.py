class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        h_per_pile = h // len(piles)

        max_banana = max(piles)

        return (max_banana // h_per_pile) + 1 if max_banana % h_per_pile != 0 else max_banana // h_per_pile

