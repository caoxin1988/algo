
a = [1, 3, 5, 7, 9, 13, 13, 13, 13, 15, 17, 18, 20]

def binary_search(value):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if a[mid] == value:
            return mid
        elif a[mid] < value:
            low = mid + 1
            pass
        else:
            high = mid - 1
    else:
        return None

def square_root(data):
    high, low = data, 0

    while True:
        mid = (high + low) / 2
        result = mid * mid

        if mid * 1000000 % 10 > 0:
            return mid

        if result < data:
            low = mid
        elif result > data:
            high = mid
        else:
            return round(mid, 6)

def main():
    # ret = square_root(100)
    ret = binary_search(13)
    print(ret)

if __name__ == '__main__':
    main()