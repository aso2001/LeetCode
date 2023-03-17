// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n){
      if(n==1){
        if(isBadVersion(1)) return 1;
        else return 2;
      }
      
      if(n==2){
        if(isBadVersion(2)){
          if(isBadVersion(1)) return 1;
          else return 2;
        }
        else return 3;
      }
      
      if(n==3){
        if(isBadVersion(3)){
          if(isBadVersion(2)){
            if(isBadVersion(1)) return 1;
            else return 2;
          }
          else return 3;
        }
        else return 4;
      }
      
      if(!isBadVersion(n)) return n+1;
      int m = n/2;
      if(isBadVersion(m)) return firstBadVersion(m-1);
      else return firstBadVersionRange(m+1,n-1);

      return 0;
    }
  
    int firstBadVersionRange(int j, int k){
      if(j==k){
        if(isBadVersion(k)) return k;
        else return k+1;
      }
      
      if((k-j)==1){
        if(isBadVersion(k)){
          if(isBadVersion(j)) return k-1;
          else return k;
        }
        else return k+1;
      }
      
      if(!isBadVersion(k)) return k+1;
      int m = (k-j)/2 + j;
      if(isBadVersion(m)) return firstBadVersionRange(j,m-1);
      else{
        if((k-m)==1) return k;
        return firstBadVersionRange(m+1,k-1);
      }
      return 0;
    }
};