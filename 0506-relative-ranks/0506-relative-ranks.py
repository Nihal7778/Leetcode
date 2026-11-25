class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        max_heap = []
        result = [""]*n


        for index,num in enumerate(score):
            heapq.heappush(max_heap,(-num,index))


        current = 1

        while max_heap:
            neg_score,index = heapq.heappop(max_heap)

            if current == 1:
                result[index] = "Gold Medal"

            elif current == 2:
                result[index] = "Silver Medal"

            elif current == 3:
                result[index] = "Bronze Medal"

            else:
                result[index] = str(current)


            current+=1

        return result

