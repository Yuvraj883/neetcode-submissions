class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length ==0){
            return 0; 
        }
        

        HashSet <Integer> set = new HashSet<>(); 

        for(int i=0; i<nums.length; i++){
            set.add(nums[i]);
        }
        int longestSequence = 1; 
        for(int x: set){
            int num = x;
            int sequence = 1;
            if(!set.contains(x-1)){
                while(set.contains(num+1)){
                    sequence++; 
                    longestSequence = Math.max(longestSequence, sequence);
                    num = num+1;  
                }
            }

        }
            return longestSequence; 

    }
}
