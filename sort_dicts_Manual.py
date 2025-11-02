# Manual implementation: sort a list of dictionaries by a specific key

def sort_dict_list(data, key):
    """
    Sorts a list of dictionaries based on the given key.
    """
    return sorted(data, key=lambda x: x[key])

# Example usage
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 23}
]

sorted_students = sort_dict_list(students, "age")
print(sorted_students)
