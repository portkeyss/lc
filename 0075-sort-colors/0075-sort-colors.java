public class Solution {
    public void sortColors(int[] nums) {
        int i = 0, j = nums.length - 1;
        int k = 0;
        while(k <= j){
            if(i <= k && nums[k] == 0) swap(nums,i++,k);
            else if(nums[k] == 2) swap(nums, j--, k);
            else k++;
        } 
    }
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}