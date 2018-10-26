
a = [1, 3, 5, 7, 11, 13, 13, 13, 13, 15, 17, 18, 20]

# find the first 
def binary_sort_first_one(data):

    low, high = 0, len(a)-1

    while low <= high:
        mid = low + (high - low) // 2

        if a[mid] >= data:
            high = mid - 1
        elif a[mid] < data:
            low = mid + 1
        # else:
        #     if mid == 0 or a[mid - 1] != data:
        #         return mid
        #     else:
        #         high = mid - 1

        if a[low] == data:
            return low
    else:
        return None
        
def binary_sort_last_one(data):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if a[mid] > data:
            high = mid - 1
        elif a[mid] <= data:
            low = mid + 1
        # else:
        #     if (mid == len(a)-1) or a[mid + 1] != data:
        #         return mid
        #     else:
        #         low = mid + 1

        if a[high] == data:
            return high
    
    return None

def binary_sort_first_big_than(data):
    low, high = 0, len(a)-1

    while low <= high:
        mid = low + (high - low) // 2

        if a[mid] >= data:
            # if mid == 0 or a[mid - 1] < data:
            #     return mid
            # else:
            #     high = mid - 1

            high = mid - 1

        elif a[mid] < data:
            low = mid + 1

        if a[low] >= data:
            return low
        
    return None

def binary_sort_last_less_than(data):
    low, high = 0, len(a) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if a[mid] > data:
            high = mid - 1
        elif a[mid] <= data:
            low = mid + 1

            if (mid == (len(a) - 2)) or a[mid + 1] > data:
                return mid
            else:
                low = mid + 1

        # if a[high] <= data:
        #     return high

    return None
        

def main():
    ret = binary_sort_last_less_than(13)
    print(ret)

if __name__ == '__main__':
    main()