#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	int numSpecial(vector<vector<int>>& mat) {
		int m = mat.size(), n = mat[0].size(), res = 0;
		vector<int> rowOnes(m, 0);
		vector<int> colOnes(n, 0);
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (mat[i][j] == 1) {
					rowOnes[i]++;
					colOnes[j]++;
				}
			}
		}
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++)
				if (mat[i][j] == 1 && rowOnes[i] == 1 && colOnes[j] == 1) res++;
		}
		return res;

	}
};

int main() {
	Solution sol;

	vector <vector<int>> input1 = { {1, 0, 0},{0, 0, 1},{1, 0, 0} };
	vector <vector<int>> input2 = { 
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 0, 0, 1, 0, 0, 0},
		{1, 0, 0, 1, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 1, 0, 0, 0, 1}
	};
	vector <vector<int>> input3 = { 
		{0,0,0,0,0,0,0,0},
		{0,1,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{1,0,0,0,0,0,0,1},
		{0,0,0,0,0,0,1,0},
		{0,0,0,0,0,0,0,1}
	};

	int result = sol.numSpecial(input3);

	cout << result << endl;

	return 0;
}