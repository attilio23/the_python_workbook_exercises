##
# Perform the flattening of a list, which is convert
# a list that contains multiple layers of nested lists into a list that contains all the same elements without any nesting 
## Flatten the list
# @param data the list to flatten
# @return the flattened list
def flattenList(data):
    if not(data):
        return data
    if type(data[0]) == list:
        l1 = flattenList(data[0])
        l2 = flattenList(data[1:])
        return l1 + l2
    if type(data[0]) != list:
        l1 = [data[0]]
        l2 = flattenList(data[1:])
        return l1 + l2
# Demonstrate the flattenList function
def main():
    print("The result of the flattening of the list [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]] is:",flattenList([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
    print("The result of the flattening of the list [] is:",flattenList([]))
    print("The result of the flattening of the list [1, 3, 7, 8, 10, 20, 77, 6] is:",flattenList([1, 3, 7, 8, 10, 20, 77, 6]))
    print("The result of the flattening of the list [[1, 2], [[[3], 4, [5, 6]], [7]], [8], 9, [10, 11], 12, [[[13, 14], [15]]]] is:",flattenList([[1, 2], [[[3], 4, [5, 6]], [7]], [8], 9, [10, 11], 12, [[[13, 14], [15]]]]))
    print("The result of the flattening of the list [[1, [2]], [[3, 4], [5]], [6]] is:",flattenList([[1, [2]], [[3, 4], [5]], [6]]))
# Call the main function
main()            