// To execute Go code, please declare a func main() in a package "main"

package main

import "fmt"

func main() {
  for i := 0; i < 5; i++ {
    fmt.Println("Hello, World!")
  }
}


QUE:1

// We have an array of elements. Each element has a unique integer id and a set of 64 flags represented by a single 64-bit integer named bit_flags. For example, an element has bit_flags = 5, meaning the element has flag 0 and flag 2. 
// 00000101
//.    3210
// Implement a function: given a list of such elements and a flag number, the function should find the last element that has the given flag number, and return the id of that element.

// Input:
// list = [
// 0  {id: 732, bit_flags: 3}, // 000…00011						
// 1  {id: 12, bit_flags: 10}, // 000…01010						12 ---> 01001 & 01010 ----> 01000 BIT 3 is ON
// 2  {id: 55, bit_flags: 4} // 000…00100
// ]
// BITNUMBER = 1  --> 00001

// BITNUMBER = 3			CREATE MASK --->  (1 << BITNUMBER)

// Output: 12 // both element 732 and element 12 have flag 1, but element 12 is the latest one


// ORDERING MATTERS (we only return LAST one, we don't care about previous ones) ---> Overwrite the result as we get a new one
//  GO OVER list
// BIGMASK = (1 << BITNUMBER)
// For each val 
// bit_flags  & BITMASK ----> ON or OFF
// if ON ---> Store result
// if another ON --> Overwrite prev result
 

// TIME Complexity --- O(N)
// Space - O(1)




QUE-2: 

// You're given an array of numbers like [5, 4, 9, 5, 6, 7], representing stock price ordered by time.  Compute the maximum profit one could have made by buying and then selling one share in that time range.


[5, 		4			, 9,			 5, 			6, 			7,      3,      8]
 BUY   <BUY    SELL.    SELL.    SELL.    SELL.  <BUY
				BUY																					BUY    	

				----> SELL
				---> RESET BUY onlly when I find <BUY
Profit          5        1.  															
MaxProfit


TIME O(N)
SPACE O(1)
 
// [5, 4, 3,2,1]
              BUY MAXPROFIT = 0
// [4, 2, 5, 1, 5] MaxProfit = 3
       BUY: 2 MAXPROFIT: at 5: 3
			BUY: 1	MAXPROFIT: at 5: 4

			BUY = num[0]
			RIGHT= 1

			for { RIGht --->

				if NEWPRICE-IS-LOWER:
							BUY
				else:
					// SELL at each point
					/// CAlculate profit
					// store global max profit

				 

					

				
				 

			}

			return MAXPROFIT

// GO OVER LIST , find minStockPrice ----- BUY: 4.  
// MaxProfit at each stock price.  starts from next index of buy: 4 MAXPROFIT = [5, 1, 2, 3]
// Keep track of MaxProfitONETXN. ---- MaxProfitONETXN 3 4 
// // Keep track of MaxProfit.  		-- GlobalMaxProfit
// CONTINUE



QUE 3: Parallel algorithms System design

// Now, shard the input so that K machines can work on the problem in parallel. Describe how you will shard the data, discuss if you would make any changes to the function you implemented for the last question, and show an implementation for the function that will consume the combined input from each shard to produce the global answer.
// 1. shard data									FIXED INDEXES, (0...3) (4...7).... CONSISTENT HASHING ( 
// 2. sharded data function 					MAP REDUCE LOCAL Profit for each Function at EACH PROCESSING UNIT
// 3. consolidation function						JOIN					All processing unit will send result..... MAXPROFIT out of all Local profits

// OPTIMIZE					 SEND BUY Prices to all shards.... 

// GLOBAL POOL of BUY Prices which every shard is looking at   SELL prices, maxprofit

    -----
SHARD1 SHARD2 


EACH SHARD ---> Sending absolute min, max of the range

AFTER JOIN ---> Calculate MAXPROFIT out of min and max range from each shard

// c = [4, 1, 5, 7, 9, 2]
// SHARDS [a, b, c, d]. 
// DRAWBACKS					