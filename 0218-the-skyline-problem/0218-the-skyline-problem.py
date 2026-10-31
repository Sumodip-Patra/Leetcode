class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))  # building enters
            events.append((R, 0, None))  # building leaves
        # Sort events: by x, then by height
        events.sort()

        # Max-heap: (-height, end)
        result = []
        heap = [(0, float('inf'))]  # (neg_height, end_x)
        prev_height = 0

        for x, negH, R in events:
            # Remove buildings from heap whose end <= x
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            if negH != 0:
                # Add new building
                heapq.heappush(heap, (negH, R))
            curr_height = -heap[0][0]
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height
        return result 
        