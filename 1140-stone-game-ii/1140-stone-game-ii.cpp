class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector dp(vector(n + 1, vector(n + 1, -1)));

        function<int(int, int)> dfs = [&](int i, int m){

            if (2*m >= piles.size() - i) {
                int ss = 0;
                for (int k = i; k < piles.size(); k++){
                    ss += piles[k];
                }
                return ss;
            } else if (dp[i][m] != -1)
                return dp[i][m];
            int res = 0;
            for (int j = 1; j <= 2*m; j++){
                int ss = 0;
                for (int k = i; k < piles.size(); k++){
                    ss += piles[k];
                }
                res = max(res, ss - dfs(i + j, max(j, m)));
                dp[i][m] = res;
            }
            return dp[i][m];
        };
        return dfs(0, 1); 
    }
};