// Last updated: 06/07/2026, 21:55:48
class Solution {
public:
    bool isPalindrome(int x) {
        long int digit=0,new_num=0;
        int org=x;
        while(x>0){
            digit=x%10;
            new_num=new_num*10+digit;
            x=x/10;
        }
        if (new_num==org){
            return true;
        }else{
            return false;
        }
    }
};
