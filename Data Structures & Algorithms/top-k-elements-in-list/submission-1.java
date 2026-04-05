class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if(nums.length==0 || k==0){
            return new int[0]; 
        }
        List<Integer> [] bucket = new ArrayList[nums.length+1]; 
        HashMap<Integer, Integer> freqCounter = new HashMap<>();
        int [] ans = new int[k];

        for(int i=0; i<nums.length; i++){
                
            freqCounter.put(nums[i], freqCounter.getOrDefault(nums[i],0)+1); 
        }


        for(Map.Entry<Integer, Integer> entry : freqCounter.entrySet()){
            // System.out.println(entry.getValue());
            // bucket[entry.getValue()] = entry.getKey(); 
           if(bucket[entry.getValue()]==null) bucket[entry.getValue()] = new ArrayList<>(); 
            bucket[entry.getValue()].add(entry.getKey());
            System.out.println(bucket[entry.getValue()]+" "+entry.getValue());
        }

        int i=bucket.length-1; 
        int j=0;
        while(k>0 && i>=0){

            if(bucket[i]==null){
                i--; 
            }
            else{

                for(int num : bucket[i]){
                  
                    ans[j] = num;
                    j++;
                    k--;
                   
                }
            
                i--; 
            }
        }
        return ans; 

    }
}
