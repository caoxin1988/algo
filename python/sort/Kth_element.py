
a = [1, 4, 7, 3, 11, 9, 2, 6, 4, 7]

def find_element(a, p, q, k):
    element = None

    j = p
    povit = a[q]
    for i in range(p, q+1):
        if a[i] < povit:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

            j += 1

    tmp = a[j]
    a[j] = a[q]
    a[q] = tmp

    print(a)
    print('j = %s, k = %s' % (j, k-1))

    if j == (k-1):
        print('find element')
        print(a)

    if j > (k-1):
        element = find_element(a, p, j-1, k)
    elif j < (k-1):
        element = find_element(a, j+1, q, k)
    else:
        element = a[j]

    if element:
        return element
    

def test():
    tmp = 1
    return tmp
    

def main():
    ret = find_element(a, 0, len(a)-1, 10)
    print(a)
    # ret = test()
    print('value = ', ret)

if __name__ == '__main__':
    main()