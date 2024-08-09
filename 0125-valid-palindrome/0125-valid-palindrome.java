class Solution {
    public boolean isPalindrome(String s) {
        String pali_s = "";
        for(int i = 0; i < s.length(); i++){
            if(Character.isLetterOrDigit(s.charAt(i))) {
                pali_s += Character.toLowerCase(s.charAt(i));
            }
        }

        int start = 0, end = pali_s.length() - 1;
        while(start <= end){
            if(pali_s.charAt(start) != pali_s.charAt(end)) {
                return false;
            }
            start += 1;
            end -= 1;
        }
        return true;
    }
}
