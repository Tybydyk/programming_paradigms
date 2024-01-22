def sorting_declarative(list_nums):
    list_nums.sort()
    return list_nums

def sorting_imperative(list_nums):  # sorting by choice
    for i in range(0, len(list_nums)):
        current_min = list_nums[i]
        min_index = i
        for j in range(i, len(list_nums)):
            if list_nums[j] < current_min:
                current_min = list_nums[j]
                min_index = j
        list_nums[i], list_nums[min_index] = list_nums[min_index], list_nums[i]
    return list_nums


if __name__ == '__main__':
    list_numbers = [23, 13, 65, 22, 45, 1, 94, 2]

    print(sorting_imperative(list_numbers))
    print(sorting_declarative(list_numbers))
