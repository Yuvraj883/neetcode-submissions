class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
       if(strs.length==0){
        return new ArrayList<>(); 
       }

       HashMap <String, List<String>> map = new HashMap<>(); 
       for(int i=0; i<strs.length; i++){
        String temp = strs[i]; 
        char []arr = temp.toCharArray(); 
        Arrays.sort(arr);
        String sortedString = new String(arr); 

        if(map.containsKey(sortedString)){
            map.get(sortedString).add(strs[i]);
        }
        else{
            map.put(sortedString, new ArrayList<String>()); 
            map.get(sortedString).add(strs[i]);
        }


       }

       List<List<String>> ans = new ArrayList<>(); 

       for(Map.Entry<String, List<String>> entry: map.entrySet()){
        ans.add(entry.getValue());
       }
       return ans; 
    }
}
