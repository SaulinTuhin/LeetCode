#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <unordered_map>

using namespace std;

class FoodRatings {
private:
	unordered_map<string, set<pair <int, string>>> cuisines_food;
	unordered_map <string, pair<string, int>> cuisines_ratings;

public:
	FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
		for (int i = 0; i < foods.size(); i++) {
			cuisines_food[cuisines[i]].emplace( -ratings[i], foods[i] );
			cuisines_ratings[foods[i]] = { cuisines[i], ratings[i] };
		}
	}

	void changeRating(string food, int newRating) {
		cuisines_food[cuisines_ratings[food].first].erase({ -cuisines_ratings[food].second, food });
		cuisines_food[cuisines_ratings[food].first].emplace( -newRating, food );

		cuisines_ratings[food].second = newRating;
	}

	string highestRated(string cuisine) {
		return cuisines_food[cuisine].begin()->second;
	}
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */

int main() {
	vector <string> food = { "kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi" };
	vector <string> cuisine = { "korean", "japanese", "japanese", "greek", "japanese", "korean" };
	vector <int> rating = { 9, 12, 8, 15, 14, 7 };

	FoodRatings *fr = new FoodRatings(food, cuisine, rating);

	cout << fr->highestRated("korean") << endl;
	cout << fr->highestRated("japanese") << endl;
	fr->changeRating("sushi", 16);
	cout << fr->highestRated("japanese") << endl;
	fr->changeRating("ramen", 16);
	cout << fr->highestRated("japanese");


	return 0;
}