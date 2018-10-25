# use loop instead of recursion

# a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]
m = [2, 3, 3, 7, 3, 9, 9, 12, 6]
n = [1, 3, 4, 7, 10, 16, 12, 9, 17, 19]
a = m + n

class Stack(object):
    def __init__(self, len):
        self.left = [None] * len
        self.right = [None] * len
        self.count = 0

    def push(self, left, right):
        
        print('push', self.count, left, right)

        self.left[self.count] = left
        self.right[self.count] = right
        self.count += 1

    def pop(self) -> tuple:
        self.count -= 1
        le = self.left[self.count]
        ri = self.right[self.count]

        return (le, ri)

    def not_empty(self):
        if self.count == 0:
            return False
        else:
            return True


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def partition(a, le, ri):
    j = le
    pivot = a[ri]

    for i in range(le, ri+1):
        if a[i] < pivot:
            swap(a, i, j)
            j += 1

    swap(a, j, ri)

    return j

# do insertig sort
def insert_sort(a, le, ri):
    for i in range(le+1, ri):
        tmp = a[i]
        for j in range(i-1, le-1, -1):
            if tmp < a[j]:
                a[j+1] = a[j]
            else:
                a[j+1] = tmp
                break


def quick_sort(a, p, q):

    stack = Stack(len(a))
    stack.push(p, q)

    while stack.not_empty():
        
        (le, ri) = stack.pop()
        print('pop', le, ri)

        if (ri - le) >= 3:
            insert_sort(a, le, ri)
            continue

        # do partition once
        j = partition(a, le, ri)

        print(a)

        stack.push(j+1, ri)
        stack.push(le, j-1)

def main():
    quick_sort(a, 0, len(a)-1)

    print(a)

if __name__ == '__main__':
    main()