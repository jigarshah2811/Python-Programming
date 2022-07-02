// QUESTION
// # nums = [4, 1, 3, 2]
// # nums.sort() # [1, 2, 3, 4, 6]
// # [1, 2, 3, 4, 6]
// # [1, ..... ]
// # [1, 1, ....]
// # [1, 1,1, ...]

// # sum=100, all ways to make 98.... all ways to make 2.... all (100) = all(98)+all(2)

// # Dynamic Programming .... Bottom up approach
// # sum(1), sum(2), sum(3)......
// # input = 100

// # 1 2 3    3 bits, combinations: 8
// # 0 0 0 --> table
// # 0 0 1
// # 0 1 0
// # 0 1 1

// # Table: EQUATION.... 

// #    1 2  3 4 5 
// # 1  1 0  
// # 2  2 1
// # 3  3 
// # 4  4 2
// # 5  5
// # 6  6 3
// # 7  7
// # 8  8 4
// # 9  9
// # 10 10 5


// #  # begin  ---> End # util we find sum, or > sum .... shrink window begin++
// #  # recur(i)

// # [1, 3, 6, 10, 6]

// # sum = 5
// # # PREFIX SUM


// # sum = 100


// # Number can repeat itself to form a sum

// # How many ways, we can make sum from above numbers
// # nums can repeat many times
// # output: int (number of ways that we can make sum out of subarray )

TestBacktrack(testing.T) {
	// features i like in go
	defer
	go backtrack()
	panic -> recover
	channels
	select

	// Sychronize with channels
	input<- 
	>-output
}

func main() {
	nums := []int{1, 2, 3}
	target := 4


	//CACHING
	// for all targets:
	//  numOfWays
	//  Store in MEMO

	memo := make(map[int]int)	// {target: numOfWays}

	

	numOfWays = backtrack(nums, 0, target)
	fmt.Println("Total ways: ", numOfWays)

}
func backtrack([]int nums, begin int, curSum int) int {
	if curSum == target {
		numOfWays += 1
	} 

	
	// BREATH ---->  i ---> end
	for i, num := range (begin, len(nums)) {
		// Check if index is not OOB
		if isSafe(i, curSum) == -1 {
			
			return numOfWays
		} 

		curSum += num
		if curSum == target {
			memo[target] = numOfWays
			numOfWays += 1
		} 
		
		if curSum < target {
			// Recur by adding the same number again
			numOfWays += backtrack(nums, begin, curSum)
		} else if curSum > target {
			// Recur by adding the same number again
			curSum -= num
			numOfWays += backtrack(nums, begin+1, curSum)
		}
		

		// Remove the prev number
	
	}

	return numOfWays
}

func powerSet([]int nums) (int, error) {
	totalComb = pow(2, len(nums))

	for _, i : range totalComb {
		for j, num : range nums {
			// i is the number to multiple with
			if num & i {
				// Selection of nums
			}
		}
		

	}

}


