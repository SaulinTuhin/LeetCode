#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
	string destCity(vector<vector<string>>& paths) {
		unordered_set <string> hash;

		string start = paths[0][0];
		for (int i = 0; i < paths.size(); i++) {
			hash.insert(paths[i][0]);
		}

		for (int i = 0; i < paths.size(); i++) {
			if (hash.find(paths[i][1]) == hash.end()) {
				return paths[i][1];
			}
		}

		return "";
	}
};

int main() {
	Solution sol;

	vector <vector <string>> input1 = { {"London", "New York"},{"New York", "Lima"},{"Lima", "Sao Paulo"} };
	vector <vector <string>> input2 = { {"B", "C"},{"D", "B"},{"C", "A"} };
	vector <vector <string>> input3 = { {"A", "Z"} };

	string output1 = sol.destCity(input1);
	string output2 = sol.destCity(input2);
	string output3 = sol.destCity(input3);

	cout << output1 << endl;
	cout << output2 << endl;
	cout << output3 << endl;

	return 0;
}