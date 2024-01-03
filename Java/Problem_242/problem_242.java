package Problem_242;
import java.lang.String;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] hash = new int[26];
        for (int i = 0; i < s.length(); i++){
            hash[s.charAt(i) - 'a']++;
            hash[t.charAt(i) - 'a']--;
        }

        for (int x : hash){
            if (x != 0)
                return false;
        }
        
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        String s1 = "anagram", t1 = "nagaram";
        String s2 = "rat", t2 = "car";
	    String s3 = "aa", t3 = "bb";

        System.out.println(sol.isAnagram(s1, t1));
        System.out.println(sol.isAnagram(s2, t2));
        System.out.println(sol.isAnagram(s3, t3));
    }
}