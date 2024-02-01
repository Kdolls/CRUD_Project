# sort according to id numbers
# sort alphabetically

# take in sequence of unsorted values:
#     length of the values
#
#     specific the beginning of the values:
#         if length <= 1:
#             return values
#
#         else use pop?
#
# once compared to the pivot point move values into these list:
#     values greater list
#     values lower list

# logic:
#         if values > pivot, move to greater list, otherwise
#             move to lower

# return all of the above finding:
# lower values + pivot point + greater values

def quick_sort(name):
    if len(name) <= 1:
        return name
    else:
        pivot = name[0]
        lower_value = []
        greater_value = []
        equal_value = []

    for letters in name:
        if letters < pivot:
            lower_value.append(letters)
        elif letters > pivot:
            greater_value.append(letters)
        else:
            equal_value.append(letters)
    return quick_sort(lower_value) + equal_value + quick_sort(greater_value)
print(quick_sort([1,2,5,7,9,4,3,2]))
