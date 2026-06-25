func twoSum(nums []int, target int) []int {
    list := make(map[int]int)

    for i, n := range nums{
        list[n] = i
    }
    for i, n  := range nums {
        difference := target - n
        if j, found := list[difference] ; found && j != i {
            return []int{i,j}
        }
    }
     return []int{}
}
