class Solution:
    def numTeams(self, rating: List[int]) -> int:
        max_rating = 0
        for r in rating:
            max_rating = max(max_rating, r)

        left_BIT = [0] * (max_rating + 1)
        right_BIT = [0] * (max_rating + 1)

        for r in rating:
            self._update_BIT(right_BIT, r, 1)

        teams = 0
        for current_rating in rating:
            self._update_BIT(right_BIT, current_rating, -1)

            smaller_ratings_left = self._get_prefix_sum(
                left_BIT, current_rating - 1
            )
            smaller_ratings_right = self._get_prefix_sum(
                right_BIT, current_rating - 1
            )
            larger_ratings_left = self._get_prefix_sum(
                left_BIT, max_rating
            ) - self._get_prefix_sum(left_BIT, current_rating)
            larger_ratings_right = self._get_prefix_sum(
                right_BIT, max_rating
            ) - self._get_prefix_sum(right_BIT, current_rating)

            teams += smaller_ratings_left * larger_ratings_right
            teams += larger_ratings_left * smaller_ratings_right
            self._update_BIT(left_BIT, current_rating, 1)

        return teams

    def _update_BIT(self, BIT: List[int], index: int, value: int) -> None:
        while index < len(BIT):
            BIT[index] += value
            index += index & (-index)

    def _get_prefix_sum(self, BIT: List[int], index: int) -> int:
        sum = 0
        while index > 0:
            sum += BIT[index]
            index -= index & (-index)
        return sum