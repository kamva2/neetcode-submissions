class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int maxLen = 0;
        int l = 0;
        HashMap<Character,Integer> map = new HashMap<>();

        for(int r=0;r<s.length();r++){

            char ch = s.charAt(r);
            map.put(ch,map.getOrDefault(ch,0)+1);

            while(map.get(ch)>1){
                char cLeft = s.charAt(l);
                map.put(cLeft,map.get(cLeft)-1);
                l++;
            }
            maxLen = Math.max(maxLen,r-l+1);
        }
        return maxLen;
    }
}
