#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
	int findSpecialInteger(vector<int>& arr) {
		int tarCount = ceil(arr.size() / 4);

		int last = INT_MIN;
		for (int i = 0; i < arr.size(); ++i) {
			if (arr[i] == last)
				continue;

			last = arr[i];
			if (arr[i] == arr[i + tarCount])
				return arr[i];
		}
		return INT_MIN;
	}
};

int main() {
	Solution solution;

	vector <int> input1 = { 1,2,2,6,6,6,6,7,10 };
	vector <int> input2 = { 1,1 };

	int output = solution.findSpecialInteger(input2);

	cout << output << endl;

	return 0;
}