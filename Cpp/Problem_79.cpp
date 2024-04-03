#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 79: Word Search
// C++ Solution!
class Solution {
private:
    vector<vector<char>> _board;
    string _word;
    int m, n;
    vector<int> rC = { 1, -1, 0, 0 }, cC = { 0, 0, 1, -1 };
public:
    bool dfs(int r, int c, int i) {
        if (i == _word.size())
            return true;
        if (r < 0 || c < 0 ||
            r >= m || c >= n ||
            _word[i] != _board[r][c] ||
            _board[r][c] == '1')
            return false;

        char cur = _board[r][c];
        _board[r][c] = '1';
        for (int j = 0; j < 4; j++) {
            if (dfs(r + rC[j], c + cC[j], i + 1))
                return true;
        }
        _board[r][c] = cur;

        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        _word = word;
        _board = board;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, 0))
                    return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;

    vector<vector<char>>input = { {'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'} };
    cout << sol.exist(input, "ABCCED") << endl;

    input = { {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };
    cout << sol.exist(input, "SEE") << endl;

    input = { {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };
    cout << sol.exist(input, "ABCB") << endl;

    return 0;
}