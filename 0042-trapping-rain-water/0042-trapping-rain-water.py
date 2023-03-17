class Solution:
    def trap(self, h: List[int]) -> int:
        # Two pointers solution
        wtr = 0
        L, R = 0, len(h) - 1
        maxL, maxR = h[L], h[R]
        while L < R:
            if maxL <= maxR:
                L += 1
                maxL = max(maxL, h[L])
                wtr += maxL - h[L]
            else:
                R -= 1
                maxR = max(maxR, h[R])
                wtr += maxR - h[R]
        return wtr


    def trap2(self, h: List[int]) -> int:
        # Solution using stack
        stack = []
        wtr = 0
        for i in range(1, len(h)):
            if h[i - 1] < h[i]:
                prevIdx = i - 1
                while stack:
                    if stack[-1][0] <= h[i]:
                        prevH, idx = stack.pop()
                        wtr += (i - idx - 1)*(prevH - h[prevIdx])
                        prevIdx = idx
                    else:
                        idx = stack[-1][1]
                        wtr += (i - idx - 1)*(h[i] - h[prevIdx])
                        break
            elif h[i - 1] > h[i]:
                stack.append((h[i-1], i-1))
        return wtr


    def trap3(self, h: List[int]) -> int:
        stack = []
        wtr = 0
        for i in range(1, len(h)):
            if h[i -1] < h[i] and stack:
                stack.pop()
                if stack:
                    hl = stack.pop()
                    if hl[0] > h[i]:
                        wtr += (i - hl[1] - 1)*(h[i] - h[i-1])
                        stack.append(hl)
                        stack.append((h[i], i))
                    elif hl[0] == h[i]:
                        wtr += (i - hl[1] - 1)*(h[i] - h[i-1])
                        stack.append((h[i], i))
                    else: # hl[0] < h[i]:
                        wtr += (i - hl[1] - 1)*(hl[0] - h[i-1])
                        hlprev = hl[0]
                        while stack:
                            hl = stack.pop()
                            if hl[0] > h[i]:
                                wtr += (i - hl[1] - 1)*(h[i] - hlprev)
                                stack.append(hl)
                                stack.append((h[i], i))
                                break
                            elif hl[0] == h[i]:
                                wtr += (i - hl[1] - 1)*(h[i] - hlprev)
                                stack.append((h[i], i))
                                break
                            else: # hl[0] < h[i]:
                                wtr += (i - hl[1] - 1)*(hl[0] - hlprev)
                                hlprev = hl[0]
            elif h[i - 1] > h[i]:
                if not stack:
                    stack.append((h[i-1], i-1))
                else:
                    prevs = stack.pop()
                    if prevs[0] == h[i-1]:
                        stack.append((h[i-1], i-1))
                    else:
                        stack.append(prevs)
                        stack.append((h[i-1],i-1))
                stack.append((h[i], i))
            elif h[i] == h[i-1] and stack:
                prevs = stack.pop()
                if prevs[0] == h[i]:
                    stack.append((h[i], i))
                else:
                    stack.append(prevs)
                    stack.append((h[i], i))
        return wtr