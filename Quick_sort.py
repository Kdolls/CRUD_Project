class Quick_Sort:
    """
    Implements quick sort algorithm in its classic form
    """

    def __init__(self):
        pass

    @staticmethod
    def sorted(value):
        """
        Executes quick sort algorithm
            :param value: passed in value Str
            :return: sorted value in form of lower,equal, higher
        """
        if len(value) <= 1:
            return value
        else:
            pivot = value[0]
            lower_value = []
            greater_value = []
            equal_value = []

        for letters in value:
            if letters < pivot:
                lower_value.append(letters)
            elif letters > pivot:
                greater_value.append(letters)
            else:
                equal_value.append(letters)
        return sorted(lower_value) + equal_value + sorted(greater_value)

    @staticmethod
    def search_me(value, key):
        """
        Perform linear search string.
        Parameters:
            value (str): String to be searched.
            key: The value to search for.
        Returns:
            int: The index of the key if found, otherwise return printed value.
        """
        for i, item in enumerate(value):
            if item == key:
                return i
        return print('result error')
