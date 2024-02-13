import random

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
class Quick_Sort:
    def __init__(self):
        pass

    @staticmethod
    def sorted(name):
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
        return sorted(lower_value) + equal_value + sorted(greater_value)


# Loop to generate random numbers
# sortlist = []
# def randomise():
#     for i in range(100):
#         random_number = random.randint(0, 10)
#         sortlist.append(random_number)
#         print(sortlist)
#
#
# randomise()
