class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
      Arrays.sort(nums); 
      List<List<Integer>> ans = new ArrayList<>(); 
      for(int i=0; i<nums.length-2; i++){
        int target = 0;

        if(i>0 && nums[i]==nums[i-1]){
            continue;
        }
        int start = i+1;
      int end = nums.length-1; 


        while(start<end){
            if(nums[start]+nums[end]+nums[i]<target){
                start++; 
            }
            else if(nums[start]+nums[end]+nums[i]>target){
                end--; 
            }

            else{
                List<Integer> temp = new ArrayList<>(); 
                temp.add(nums[i]); 
                temp.add(nums[start]); 
                temp.add(nums[end]); 
                ans.add(temp); 

                start++; 
                end--;
                while(start<end && nums[start]==nums[start-1]) start++; 
                while(start<end && nums[end]==nums[end+1]) end --; 

            }
        }
      }
      return ans;
    }
}
