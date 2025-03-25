func twoSum(nums []int, target int) []int { 
    for i:=0; i< len(nums); i++{
		x := target - nums[i]
		if slices.Contains(nums,x){
                var index int = slices.Index(nums,x)
                if i != index{return []int{i,index}}
		}
	}
 return nil
}

