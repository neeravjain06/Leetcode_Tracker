// Last updated: 06/07/2026, 21:55:47
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        int k=0;
        int j=0;

        for(int i=0;i<n;i++){
            if(nums[i]!=val){
            nums[k]=nums[i];
            k++;
            j++;
            }else{
                nums[i]=0;
            }
        }
        return j;
    }
};