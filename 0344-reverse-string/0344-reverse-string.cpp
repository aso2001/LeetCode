class Solution {
public:
    void reverseString(vector<char>& s) {
        char c;
        for(int i=0; i<(int)(s.size()/2); ++i){
            c=s[i];
            s[i]=s[s.size()-i-1];
            s[s.size()-i-1]=c;
        }
    }
};