class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s.length()<=1){
            return s.length(); 
        }

       int max = 0; 
       int i=0; 
       int j=0;
       HashSet<Character> set = new HashSet<>();
       while(j<s.length()){
        char ch = s.charAt(j); 

        while(set.contains(ch)){
            set.remove(s.charAt(i));
            i++;
        }
        set.add(ch);
        max = Math.max(max, j-i+1);
        j++;

       }

       return Math.max(j-i, max);
    }
}
