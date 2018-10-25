

m = [2, 3, 3, 7, 3, 9, 9, 12, 6]
n = [1, 3, 4, 7, 10, 16, 12, 9, 17, 19]
a = m + n
n = len(a)

def bubble_sort():

    for i in range(0, n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = tmp

    print('new array:')
    print(a)

# a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]
def insert_sort():
    for i in range(1, n):
        tmp = a[i]
        j = i - 1
        
        while j > -1:
            if tmp < a[j]:
                a[j+1] = a[j]
                j -= 1
            else:
                break

        a[j+1] = tmp

    print('new array:')
    print(a)

# a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]
def select_sort():
    for i in range(0, n):
        min = a[i]
        t = i

        for j in range(i+1, n):
            if min > a[j]:
                min = a[j]
                t = j

        if t != i:
            a[t] = a[i]
            a[i] = min

    print('new array:')
    print(a)


def main():
    # bubble_sort()
    insert_sort()
    # select_sort()

if __name__ == '__main__':
    main()