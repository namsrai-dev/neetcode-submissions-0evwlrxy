class Solution:
    def get_distance(self, points: List) -> int:
        x, y = points[0], points[1]
        distance = (math.sqrt((math.pow(x, 2) + math.pow(y, 2))))
        return distance

    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = []
        for arr in points:
            dist = self.get_distance(arr)
            dist = self.get_distance(arr)
            min_heap.append([dist, arr[0], arr[1]])

        heapq.heapify(min_heap)

        while k > 0:
            popped = heapq.heappop(min_heap)
            res.append([popped[1],popped[2]])
            k = k - 1


        return res

