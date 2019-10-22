import random
import copy


def timer(reps=1):
    def second_level(func):
        from time import perf_counter

        def last_level(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            agv_elapsed = total_elapsed/reps

            args_ = [str(i) for i in args]
            kwargs_ = [f'{k} = {v}' for (k, v) in kwargs.items()]
            arg_list = args_ + kwargs_
            args_str = ','.join(arg_list)

            print(
                f'{func.__name__} took {agv_elapsed:8f} second(s) to run. ({reps} reps has run)')
            return result
        return last_level
    return second_level


@timer()
def insertion_sort(n):

    for index, value in enumerate(n):
        temp_index = index

        while temp_index > 0 and n[temp_index] < n[temp_index-1]:
            n[temp_index], n[temp_index-1] = n[temp_index-1], n[temp_index]
            temp_index -= 1
    # print(n)
    # return n


@timer()
def selection_sort_boring(n):
    for index, value in enumerate(n):
        min_value = value
        temp_index = index
        for sub_index in range(index, len(n)):
            if min_value > n[sub_index]:
                min_value = n[sub_index]
                temp_index = sub_index

        n[index], n[temp_index] = min_value, n[index]
    return n
    # print(n)


@timer()
def bubble_sort(n):

    for i in range(len(n)):
        for index, value in enumerate(n):
            if index < len(n)-1:
                if value > n[index+1]:
                    n[index], n[index+1] = n[index+1], n[index]
    # print(n)
    return n


@timer()
def counting_sort(n):
    range_list = [0]*len(n)
    sorted_list = [0]*len(n)
    for _, value in enumerate(n):
        range_list[value] += 1
    for i in range(1, len(range_list)):
        range_list[i] += range_list[i-1]
    for i in n:
        sorted_list[range_list[i]-1] = i
        range_list[i] -= 1
    # print(sorted_list)
    return n


@timer()
def merge_sort(array):
    def merge(left, right, array):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    def divide(array):
        if len(array) < 2:
            return
        left = [item for item in array[:len(array)//2]]
        right = [item for item in array[len(array)//2:]]

        divide(left)
        divide(right)
        merge(left, right, array)
    divide(array)


random_array = [i for i in range(10000)]
random.shuffle(random_array)

r1 = copy.deepcopy(random_array)
r2 = copy.deepcopy(random_array)
r3 = copy.deepcopy(random_array)
r4 = copy.deepcopy(random_array)

# merge_sort(random_array)
# bubble_sort(random_array)
insertion_sort(r1)
selection_sort_boring(r2)
counting_sort(r3)
merge_sort(r4)
# print(random_array)
print(r3)
