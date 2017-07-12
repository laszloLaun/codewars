// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage){
    this.collection = collection;
    this.itemsPerPage = itemsPerPage;
}

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function() {
    console.log("number of items:");
    return this.collection.length;
};

// returns the number of pages
PaginationHelper.prototype.pageCount = function() {
    console.log("number of pages:", Math.floor(this.collection.length / this.itemsPerPage + 1));
    return Math.floor(this.collection.length / this.itemsPerPage + 1)
};

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function(pageIndex) {
    if(this.pageCount() - 1 < pageIndex) {
        console.log("-1");
        return -1;
    }
    else if (this.pageCount() - 1 !== pageIndex) {
        console.log("number of items on the current page:", this.itemsPerPage);
        return this.itemsPerPage;
    } else {
        console.log("number of items on the current page:", this.collection.length % this.itemsPerPage);
        return this.collection.length % this.itemsPerPage;
    }
};

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function(itemIndex) {
    if (this.collection.length <= itemIndex || 0 > itemIndex) {
        return -1;
    }
    console.log("what page an item is on:", Math.floor(itemIndex / Math.floor(this.collection.length / this.pageCount())))
    return Math.floor(itemIndex / Math.floor(this.collection.length / this.pageCount()));
};

var collection = [];
for (var i=1; i<25; i++) collection.push(i);
var helper = new PaginationHelper(collection, 10);
helper.pageIndex(8);