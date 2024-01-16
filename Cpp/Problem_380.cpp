#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// Problem - 380: https://leetcode.com/problems/insert-delete-getrandom-o1/
// C++ Solution!
class RandomizedSet {
private:
    unordered_map<int, int> map;
    vector<int> list;

public:
    RandomizedSet() {

    }

    bool insert(int val) {
        if (map.find(val) != map.end())
            return false;

        list.push_back(val);
        map[val] = list.size() - 1;

        return true;
    }

    bool remove(int val) {
        if (map.find(val) == map.end())
            return false;

        auto idx = map.find(val);
        list[idx->second] = list.back();
        list.pop_back();
        map[list[idx->second]] = idx->second;
        map.erase(idx);

        return true;
    }

    int getRandom() {
        return list[rand() % list.size()];
    }
};

int main() {
    RandomizedSet rs = RandomizedSet();

    cout << rs.insert(1) << endl;
    cout << rs.remove(2) << endl;
    cout << rs.insert(2) << endl;
    cout << rs.getRandom() << endl;
    cout << rs.remove(1) << endl;
    cout << rs.insert(2) << endl;
    cout << rs.getRandom() << endl;

    return 0;
}