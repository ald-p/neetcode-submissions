class DynamicArray {
    var array: [Int]
    var capacity: Int
    var size: Int

    init(_ capacity: Int) {
        self.array = [Int](repeating: 0, count: capacity)
        self.size = 0
        self.capacity = capacity
    }

    func get(_ i: Int) -> Int {
        return array[i]
    }

    func set(_ i: Int, _ n: Int) {
        array[i] = n
    }

    func pushback(_ n: Int) {
        if size == capacity {
            resize()
        }
        array[size] = n
        size += 1
    }

    func popback() -> Int {
        size -= 1
        return array[size]
    }

    private func resize() {
        capacity *= 2
        var newArray = [Int](repeating: 0, count: capacity)
        for i in 0..<size {
            newArray[i] = array[i]
        }
        array = newArray
    }

    func getSize() -> Int {
        return size
    }

    func getCapacity() -> Int {
        return capacity
    }
}
