import Kotlin.math.*

# Problem - 1614: Maximum Nesting Depth of the Parentheses
# Kotlin Solution!
class Solution {
    fun maxDepth(s: String): Int {
        var res = 0;
        var curDepth = 0;
        
        for (i in s){
            if (i == '(')
                curDepth++
            else if (i == ')')
                curDepth--;

            res = max(res, curDepth);
        }

        return res;
    }
}

fun main(){
    var sol = Solution();

    println(sol.maxDepth("(1+(2*3)+((8)/4))+1"));
    println(sol.maxDepth("(1)+((2))+(((3)))"));
}