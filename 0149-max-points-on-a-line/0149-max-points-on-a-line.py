class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        def get_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return (0, 1)  
            if dy == 0:
                return (1, 0)  
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            return (dx, dy)

        def divide_and_conquer(left: int, right: int) -> int:
            if right - left + 1 <= 2:
                return right - left + 1

            mid = (left + right) // 2

            max_left = divide_and_conquer(left, mid)
            max_right = divide_and_conquer(mid + 1, right)
            max_independent = max(max_left, max_right)

            max_cross = 0
            for i in range(left, mid + 1):
                slopes = defaultdict(int)
                duplicate = 1  
                current_max = 0
                
                for j in range(left, right + 1):
                    if i == j:
                        continue
                    if points[i] == points[j]:
                        duplicate += 1
                    else:
                        slope = get_slope(points[i], points[j])
                        slopes[slope] += 1
                        if slopes[slope] > current_max:
                            current_max = slopes[slope]
                
                max_cross = max(max_cross, current_max + duplicate)

            return max(max_independent, max_cross)

        return divide_and_conquer(0, n - 1)
        