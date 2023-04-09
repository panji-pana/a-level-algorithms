class Queue{
    constructor() {
        this.queue = []
        this.front = 0
        this.back = -1
    }

    enqueue(item){
        this.back++
        this.queue[this.back] = item
    }

    dequeue(){
        this.front++
        if(this.front > this.back){
            throw new Error("Queue underflow")
        }
    }

    peek(){
        return this.queue[this.front]
    }
}

module.exports = Queue
