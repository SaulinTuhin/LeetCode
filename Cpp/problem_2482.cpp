#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
		int row = grid.size(), col = grid[0].size();
		vector <int> rowOnes(row, 0);
		vector <int> colOnes(col, 0);

		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (grid[i][j]) {
					rowOnes[i]++;
					colOnes[j]++;
				}
				else {
					rowOnes[i]--;
					colOnes[j]--;
				}
			}
		}

		vector <vector <int>> diff(row, vector<int> (col, 0));
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				diff[i][j] = rowOnes[i] + colOnes[j];
			}
		}

		return diff;
	}
};

int main() {
	Solution sol;

	vector<vector<int>> input1 = { {0, 1, 1},{1, 0, 1},{0, 0, 1} };
	vector<vector<int>> input2 = { {1, 1, 1},{1, 1, 1} };

	vector<vector<int>> output = sol.onesMinusZeros(input2);

	for (int i = 0; i < output.size(); i++) {
		for (int j = 0; j < output[0].size(); j++) {
			cout << output[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}