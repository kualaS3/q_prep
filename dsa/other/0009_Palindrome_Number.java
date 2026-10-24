''' avoiding conversion to string '''
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int n = x;
        int rev = 0;
        while (n>0) {
            int last_digit = n % 10;
            rev = (rev*10) + last_digit;
            n = n / 10;
        }
        return x == rev;
    }
}
