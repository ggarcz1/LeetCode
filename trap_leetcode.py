# https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150

def trap(height):
    area = 0
    distance = 0
    for i in range(len(height)):
        startHeight = height[i]
        endHeight = 0

        # inside the "bucket"
        if height[i] == 0:
            distance += 1
        # end of the "bucket"
        # need case here for if end is > top
        # take the min value
        # need case here for it end is < top
        # take the min value each time
        elif startHeight <= height[i]:
            endHeight == height[i]
            # print(startHeight, endHeight, distance)
            # print(startHeight * distance)
            area += startHeight * distance
            startHeight = endHeight
            distance = 0

    return area

# case works 
height1 = [2,0,0,0,2,3,0,0,3]
# case does not work 
height2 = [2,0,0,0,2,0,3,0,0,3]
height3 = [0,1,0,2,1,0,1,3,2,1,2,1]
height4 = [4,2,0,3,2,5]

print(trap(height=height1) if 12 != trap(height=height1) else True)
print(trap(height=height2) if 6 != trap(height=height1) else True)
print(trap(height=height3) if 9 != trap(height=height1) else True)
print(trap(height=height4) if 8 != trap(height=height1) else True)
