
# a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]
a = [2, 3, 3, 7, 7, 9, 10, 12, 20]
b = [1, 3, 4, 7, 10, 12, 12, 16, 17, 19]
t = a + b

def merge_sort(a, p, q):
    r = int((p + q) / 2)

    if p >= q:
        return

    merge_sort(a, p, r)
    merge_sort(a, r+1, q)
    merge(a, p, q, r)

# merge list m and n into a by ascending order
def merge(a, p, q, r):
    # i, j = p, r+1
    i = j = 0
    k = 0
    tmp = [None] * (q - p + 1)

    while i < (r-p+1) or j < (q-r):
        if (i == (r-p+1)):
            tmp[k] = a[r+1+j]
            j += 1
        elif (j == (q-r)):
            tmp[k] = a[p+i]
            i += 1
        else:
            if (a[p+i] < a[r+1+j]):
                tmp[k] = a[p+i]
                i += 1
            else:
                tmp[k] = a[r+1+j]
                j += 1

        k += 1

    print(tmp)

    for i in range(p, q+1):
        a[i] = tmp[i-p]

def main():
    # merge(t, 8, 9, 8)
    merge_sort(t, 0, len(t)-1)
    print(t)

if __name__ == '__main__':
    main()