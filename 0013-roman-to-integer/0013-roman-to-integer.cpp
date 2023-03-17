class Solution {
public:
  int romanToInt(string s){
    vector<int> v(15,0);
    for(int i=0; s[i]!='\0'; ++i){
      switch(s[i]){
        case 'I': v[i]=1; break;
        case 'V': v[i]=5; break;
        case 'X': v[i]=10; break;
        case 'L': v[i]=50; break;
        case 'C': v[i]=100; break;
        case 'D': v[i]=500; break;
        case 'M': v[i]=1000; break;
      }
      if(i>0 && v[i-1]<v[i]) v[i-1]*=-1;
    }
    int res=0;
    for(int i=0; s[i]!='\0'; ++i){
      res+=v[i];
    }
    return res;
  }
};