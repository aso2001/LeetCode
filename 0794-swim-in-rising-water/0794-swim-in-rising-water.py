import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid) #getting len so to keep track of the last element
        heap=[(grid[0][0],0,0)]  #reprsenting the VALUE, ROW, COL
        d=[(1,0),(-1,0),(0,1),(0,-1)] #for out up, down, left, right element
        s=set() #this will help us keep track of visited elements
        mh=0 #the max height we have seen so far
        while heap:
            h,r,c=heapq.heappop(heap) #get top of the heap
            mh=max(mh,h)
            if r==(n-1) and c==(n-1): #if it is the last element 
                return mh
            if (r,c) in s: #if already seen
                continue
            s.add((r,c))
            for i,j in d: #add up, down, left, right elements
                nr=r+i #new elememts
                nc=c+j
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in s:
                    heapq.heappush(heap,(grid[nr][nc],nr,nc)) #push the element in the heap

            #key idea here is that we use min heap so least one would be at top
            #and we make sure element being checked are in a path
            #as we are only pushing the adjacent element up,down,left,right
            #these are automaticly in order in the min heap
        