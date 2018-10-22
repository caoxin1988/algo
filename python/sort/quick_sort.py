
a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]
# a = [2, 3, 3, 7, 7, 9, 10, 12, 20]
# b = [1, 3, 4, 7, 10, 12, 12, 16, 17, 19]
# t = a + b

def quick_sort(a, p, q):

    if p == q:
        return

    j = p
    pivot = a[q]
    print('q = ', q)
    for i in range(p, q+1):
        print('a[%s] = %s' % (i, a[i]))
        if a[i] < pivot:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

            j += 1

    tmp = a[j]
    a[j] = a[q]
    a[q] = tmp

    print('p = %s, q = %s, j = %s' % (p, q, j))

    quick_sort(a, p, j-1)
    quick_sort(a, j+1, q)


def main():
    quick_sort(a, 0, len(a)-1)
    print(a)

if __name__ == '__main__':
    main()