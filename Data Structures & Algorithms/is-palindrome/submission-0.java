class Solution {
    public boolean isPalindrome(String s) {
    String str = s.replace(" ","").toLowerCase();
    int start = 0; 
    int end = str.length()-1; 

    while(start<=end){
        
        while(start<end && !Character.isLetterOrDigit(str.charAt(start))){
            start++;
        }
        while(start<end && !Character.isLetterOrDigit(str.charAt(end))){
            end--;
        }
        char c1 = str.charAt(start);
        char c2 = str.charAt(end);
        System.out.println(c1+" "+c2);
        if(c1!=c2){
            return false;
        }

        start++; 
        end--; 
    }        
    return true;
    }
}
