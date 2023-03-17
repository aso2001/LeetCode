class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Optimized solution using Monotonic Stack
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        heights.pop()
        return res

    
    def largestRectangleArea2(self, heights: List[int]) -> int:
        # Solution using Monotonic Stack
        stack = [(heights[0], 0)]
        maxa = heights[0]
        prev_idx = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                stack.append((heights[i], i))
            else:
                while stack:
                    tmp = stack[-1]
                    if tmp[0] >= heights[i]:
                        stack.pop()
                        prev_idx = tmp[1]
                        tmpa = heights[i]*(i - tmp[1] + 1)
                        tmpb = tmp[0]*(i - tmp[1])
                        maxa = max(maxa, tmpa, tmpb)
                    else:
                        stack.append((heights[i], prev_idx))
                        break
                if not stack:
                    stack.append((heights[i], prev_idx))
        while stack:
            tmp = stack.pop()
            tmpa = tmp[0]*(len(heights) - tmp[1])
            maxa = max(maxa, tmpa)
        return maxa


    def largestRectangleArea3(self, heights: List[int]) -> int:
        # Brute force O(n^2) TLE
        h = [0]*(len(heights) + 1)
        h[1:len(heights)] = heights

        maxa = 0
        for i in range(1, len(h) - 1):
            l, r = i - 1, i + 1
            area = h[i]
            while l > 0:
                if h[l] >= h[i]:
                    area += h[i]
                else: break
                l -= 1
            while r < len(h) - 1:
                if h[r] >= h[i]:
                    area += h[i]
                else: break
                r += 1
            maxa = max(area, maxa)
        return maxa