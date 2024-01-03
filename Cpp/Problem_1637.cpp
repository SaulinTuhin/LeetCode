#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
	int maxWidthOfVerticalArea(vector<vector<int>>& points) {
		/*
		Sort the 2D array, this will sort based on X value first, if x is same based on Y value.
		This is similar to sorting an vector of pairs: vector<pair<int, int>>
		*/
		sort(points.begin(), points.end());

		/*
		We can initialize the array with distance between first two points (X-axis).
		**Remember points vector is sorted by this point**
		This doesn't really matter.
		*/
		int max_gap = points[1][0] - points[0][0];
		// As we already have the distance between first two points, start from the third point.
		for (int i = 2; i < points.size(); i++) {
			/*if (points[i][0] - points[i-1][0] > max_gap) {
				max_gap = points[i][0] - points[i-1][0];
			}
			---
			If you are having trouble understanding the ternary operator below,
			it is same as the commented out if block above.
			---
			1. Check if the distance between current point and previous point is larger
			than the largest difference between two adjacent points in X-axis.
				1.a) If yes update max_gap to distance between current point and previous point.
			*/

			max_gap = (points[i][0] - points[i - 1][0]) > max_gap ? (points[i][0] - points[i - 1][0]) : max_gap;
		}

		// max_gap will have the largest difference between two adjacent points in X-axis.
		return max_gap;
	}
};

int main() {
	Solution sol;

	vector<vector<int>> input = { {8, 7},{9, 9},{7, 4},{9, 7} };
	cout << sol.maxWidthOfVerticalArea(input) << endl;

	input = { {3, 1},{9, 0},{1, 0},{1, 4},{5, 3},{8, 8} };
	cout << sol.maxWidthOfVerticalArea(input) << endl;

	return 0;
}