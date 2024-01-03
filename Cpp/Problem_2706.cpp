#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	int buyChoco(vector<int>& prices, int money) {
		int min = INT_MAX, second_min = INT_MAX;

		for (int price : prices) {
			if (price < min) {
				second_min = min;
				min = price;
			}
			else if (price < second_min)
				second_min = price;
		}

		return min + second_min <= money ? money - min - second_min : money;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 1,2,2 };
	cout << sol.buyChoco(input, 3) << endl;

	input = { 3, 2, 3 };
	cout << sol.buyChoco(input, 3) << endl;

	return 0;
}