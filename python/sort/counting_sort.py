a = [2, 5, 3, 0, 2, 3, 0, 3]
N = 6
counting = [0] * N

class CountingSort(object):
    def counting_sort(self):

        b = [None] * a.__len__()

        for j in range(len(a)-1, -1, -1):
            tmp = a[j]
            i = counting[tmp]
            print(i)
            b[i-1] = tmp
            counting[tmp] -= 1

        print(b)


    def get_count(self):
        for i in range(0, len(a)):
            counting[a[i]] += 1

        for i in range(1, N):
            counting[i] = counting[i-1] + counting[i]


def main():
    sort = CountingSort()
    sort.get_count()
    sort.counting_sort()


if __name__ == '__main__':
    main()