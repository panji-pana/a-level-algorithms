// const Queue = require("./queue")

// let queue = new Queue()

// queue.enqueue("Hello")
// queue.enqueue("World")
// console.log(queue.peek())
// queue.dequeue()
// console.log(queue.peek());

const Hash = require("./hash_table")

let hash = new Hash()

hash.insert("Hello")
hash.insert("World")
console.log(hash.search("Hello"))
console.log(hash.search("World"))
console.log(hash.search("wORLD"))
console.log(hash.table);
hash.remove("Hello")
console.log(hash.search("Hello"))
console.log(hash.search("World"));
console.log(hash.table);
