def largestRect(hist):
    stack = list()
    maxArea = 0

    # Go through the hist once
    i = 0

    while i < len(hist):

        if (not stack) or (hist[i] >= hist[stack[-1]]):
            # Increasing sequence so keep adding indexes on stack
            stack.append(i)
            print(("Push index: {0}, currentEle: {1}, stackEle: {2}".format(i, hist[i], hist[stack[-1]])))
            i += 1

        else:
            top_of_stack = stack.pop()

            # Calc area
            #width = i - top_of_stack       # MOST TRICKY to find the width
            width = abs(i - stack[-1] - 1) if stack else i
            height = hist[top_of_stack]
            area = height * width

            maxArea = max(maxArea, area)
            print(("Pop index: {0}, currentEle: {1}, stackEle: {2} MaxArea: {3}".format(top_of_stack, hist[i], hist[top_of_stack], maxArea)))

    # Remaining elements on stack
    print("Remaining...")
    while stack:
        top_of_stack = stack.pop()

        # Calc area
        width = abs(i - stack[-1] - 1) if stack else i
        height = hist[top_of_stack]
        area = height * width

        maxArea = max(maxArea, area)
        print(("Pop i: {0}, stackEle: {1}, MaxArea: {2}".format(top_of_stack, hist[top_of_stack], maxArea)))


    return maxArea

hist = [2, 3, 4, 5, 3, 3, 1]
#print ("Maximum rectangle area in histogram is: ", largestRect(hist))
hist = [2, 1, 2]
#print ("Maximum rectangle area in histogram is: ", largestRect(hist))
hist = [5,4,1,2]
#print ("Maximum rectangle area in histogram is: ", largestRect(hist))
hist = [4,2,0,3,2,5]
print(("Maximum rectangle area in histogram is: ", largestRect(hist)))