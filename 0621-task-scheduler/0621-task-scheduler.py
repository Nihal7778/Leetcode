class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hashmap = {}

        for task in tasks:
            if task in hashmap:
                hashmap[task]+=1

            else:
                hashmap[task]=1


        maxHeap = []

        for freq in hashmap.values():
            maxHeap.append(-freq)

        heapq.heapify(maxHeap)

        cooldown = deque()
        time = 0


        while maxHeap or cooldown:
            time+=1

            if cooldown and cooldown[0][1]<=time:
                freq,available_time = cooldown.popleft()
                heapq.heappush(maxHeap,freq)


            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq+=1

                if freq:
                    cooldown.append((freq,time+n+1))

        return time



        