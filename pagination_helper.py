# TODO: complete this class


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        print("number of items:", len(self.collection))
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        print("number of pages:", len(self.collection)//self.items_per_page + 1)
        return len(self.collection) // self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if self.page_count() - 1 < page_index:
            print('-1')
            return -1
        elif self.page_count() - 1 == page_index:
            print("number of items on the current page:", len(self.collection) % self.items_per_page)
            return len(self.collection) % self.items_per_page
        else:
            print("number of items on the current page:", self.items_per_page)
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > len(self.collection):
            return -1

        print("what page an item is on:", item_index // (len(self.collection) // self.page_count()))
        return item_index // (len(self.collection) // self.page_count())

collection = list(range(1, 25))
helper = PaginationHelper(collection, 10)
helper.item_count()
helper.page_count()
helper.page_item_count(2)
helper.page_index(8)
