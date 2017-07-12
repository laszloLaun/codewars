def most_frequent_item_count(collection):
    max_count = 0
    for i in collection:
        if collection.count(i) > max_count:
            max_count = collection.count(i)
    print(max_count)
    return max_count
most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])
