def merge_lists(original, add, remove):
    try:
        unsorted_result = list(set(original).union(set(add)) - set(remove))
        result = sorted(unsorted_result, key=lambda x: (len(x), x), reverse=True)
        return result
    except TypeError:
        print('Invalid input type.')
