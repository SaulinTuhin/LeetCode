class Solution {
    public int buyChoco(int[] prices, int money) {
        int min = 101, second_min = 101;

        for (int price: prices){
            if (price < min){
                second_min = min;
                min = price;
            }
            else if (price < second_min){
                second_min = price;
            }
        }

        return money - min - second_min >= 0 ? money - min - second_min : money;
    }

    public static void main (String[] args){
        Solution sol = new Solution();

        System.out.println(sol.buyChoco(new int[]{1,2,2}, 3));
        System.out.println(sol.buyChoco(new int[]{3,2,3}, 3));
    }
}