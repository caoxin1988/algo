class Heap:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.count = 0
        self.data = [None] * (capacity + 1)

    def insert_heap(self, data : int):
        if self.count >= self.capacity:
            print('heap is full')
            return  # heap is full

        self.count += 1
        cnt = self.count

        self.data[cnt] = data

        while (cnt // 2) >= 1 and self.data[cnt//2] > self.data[cnt]:
            tmp = self.data[cnt]
            self.data[cnt] = self.data[cnt//2]
            self.data[cnt//2] = tmp

            cnt = cnt // 2

    def remove_heap_top(self):
        if self.count == 0:
            print('heap is empty')
            return

        data = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        
        cnt = 1
        while True:
            min_pos = cnt
            if cnt * 2 <= self.count and self.data[cnt] > self.data[cnt * 2]:
                min_pos = cnt * 2
            if (cnt * 2 + 1) <= self.count and self.data[min_pos] > self.data[cnt * 2 + 1]:
                min_pos = cnt * 2 + 1

            if min_pos == cnt: 
                break
            else:
                tmp = self.data[cnt]
                self.data[cnt] = self.data[min_pos]
                self.data[min_pos] = tmp

                cnt = min_pos

        return data




heap = Heap(5)
heap.insert_heap(4)
heap.insert_heap(2)
heap.insert_heap(5)
heap.insert_heap(1)
heap.insert_heap(7)

for i in heap.data[1:heap.count+1]:
    print(i)

print('==' * 5)
print(heap.remove_heap_top())
print('==' * 5)
for i in heap.data[1:heap.count+1]:
    print(i)