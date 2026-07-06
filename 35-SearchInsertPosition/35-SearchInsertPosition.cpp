// Last updated: 06/07/2026, 21:55:46
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size=nums.size();
        for(int i=0;i<size;i++){
            if(target==nums[i]){
                return i;
            }
        }
        for(int i=0;i<size;i++){
            if(nums[i]>target){
                return i;
            }
        }return size;
    }
};