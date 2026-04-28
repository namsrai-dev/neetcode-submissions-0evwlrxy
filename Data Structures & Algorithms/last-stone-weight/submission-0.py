class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            x = heapq.heappop(max_heap) * (-1)
            y = heapq.heappop(max_heap) * (-1)

            if x != y:
                heapq.heappush(max_heap, (x-y) * -1)


            # print(x)
            # print(y)

        if len(max_heap) == 0:
            return 0

        return max_heap[0] * -1
