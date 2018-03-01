def print_multiple_list(items):
    for item in items:
        if isinstance(item, list):
            print_multiple_list(item)
        else:
            print(item)


