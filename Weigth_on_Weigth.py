# This function first defines a helper function calculate_weight to compute the weight of a number.
# Then, it defines another helper function custom_sort_key to be used as the key function for sorting.
# Finally, it splits the input string, sorts the numbers based on their weights and values, and returns the ordered string.
def order_by_weight(string):
    def calculate_weight(num):
        return sum(int(digit) for digit in str(num))

    # the custom_sort_key function includes both the weight and the string
    # representation of the number in the tuple returned for sorting.
    # This ensures that when two numbers have the same weight, they will be sorted based on their string representation.
    def custom_sort_key(number):
        weight = calculate_weight(number)
        return (weight, str(number))

    if not string:
        return ""

    weights_list = sorted(string.split(), key=custom_sort_key)
    return " ".join(weights_list)


# Example usage:
# print(order_by_weight("103 123 4444 99 2000"))
print(order_by_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
