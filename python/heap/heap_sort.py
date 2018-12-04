class Heap:
    def heaplify(self, nums : list, length : int):
        for i in range(length//2-1, -1, -1):
            self.__compare(nums, length, i)

    def __compare(self, nums, length, i):
        while True:
            min_pos = i
            if (i*2 + 1) <= length-1 and nums[i] > nums[i*2 + 1]:
                min_pos = i*2 + 1
            if (i*2 + 2) <= length-1 and nums[min_pos] > nums[i*2 + 2]:
                min_pos = i*2 + 2

            if min_pos == i:
                break
            
            tmp = nums[i]
            nums[i] = nums[min_pos]
            nums[min_pos] = tmp
            i = min_pos

    def sort(self, nums : list, length : int):
        # heaplify the list
        self.heaplify(nums, length)

        for i in range(length-1, -1, -1):
            tmp = nums[0]
            nums[0] = nums[i]
            nums[i] = tmp

            self.heaplify(nums, i)

nums = [2, 4, 7, 4, 1, 9]
# nums = [9, 2, 7, 4, 4]
heap = Heap()
# heap.heaplify(nums, len(nums))
heap.sort(nums, len(nums))

for num in nums:
    print(num)


