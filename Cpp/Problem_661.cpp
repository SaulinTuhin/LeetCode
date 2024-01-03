#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
		int row = img.size(), col = img[0].size();

		//vector <vector<int>> ret(row, vector<int>(col, 0));

		for (int r = 0; r < row; r++) {
			for (int c = 0; c < col; c++) {
				int total = 0, count = 0;

				for (int i = r - 1; i < r + 2; i++) {
					for (int j = c - 1; j < c + 2; j++) {
						if (i < 0 || i == row || j < 0 || j == col)
							continue;

						total += img[i][j] % 256;
						count++;
					}
				}

				img[r][c] |= (total / count) << 8;
			}
		}

		for (int r = 0; r < row; r++) {
			for (int c = 0; c < col; c++) {
				img[r][c] >>= 8;
			}
		}

		return img;
	}

	void printImage(vector <vector <int>> img) {
		for (int i = 0; i < img.size(); i++) {
			for (int j = 0; j < img[0].size(); j++) {
				cout << img[i][j] << " ";
			}
			cout << endl;
		}
	}
};

int main() {
	Solution sol;

	vector <vector<int>> input1 = { {1, 1, 1},{1, 0, 1},{1, 1, 1} };
	vector <vector<int>> input2 = { {100, 200, 100},{200, 50, 200},{100, 200, 100} };

	sol.printImage(sol.imageSmoother(input1));
	sol.printImage(sol.imageSmoother(input2));

	return 0;
}