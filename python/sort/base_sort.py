a = ["13572", "15734", "14269", "15384", "15721"]

def base_sort():
    item_len = len(a[0])

    for i in range(item_len-1, -1, -1):
        count_sort(i)

def count_sort(n):
    count_num = 10
    counting = [0] * count_num
    tmp = [None] * len(a)

    for i in range(0, len(a)):
        value = int(a[i][n])
        counting[value] += 1

    for i in range(1, count_num):
        counting[i] += counting[i-1]

    for i in range(len(a)-1, -1, -1):
        value = int(a[i][n])
        j = counting[value]
        tmp[j-1] = a[i]
        counting[value] -= 1

    # print(counting)
    # print(tmp)
    for i in range(0, len(a)):
        a[i] = tmp[i]


def main():
    base_sort()

    print(a)

if __name__ == '__main__':
    main()