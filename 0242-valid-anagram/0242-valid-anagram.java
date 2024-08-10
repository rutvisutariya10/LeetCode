// class Solution {
//     public boolean isAnagram(String s, String t) {
//         if(s.length()!=t.length()){
//             return false;
//         }
//         Map<Character,Integer> s_map = new HashMap<Character,Integer>();
//         Map<Character,Integer> t_map = new HashMap<Character,Integer>();
//         for(int i= 0; i< s.length(); i++){
//             if(s_map.containsKey(s.charAt(i))){
//                 s_map.put(s.charAt(i), 1 + s_map.get(s.charAt(i)));
//             } else{
//                 s_map.put(s.charAt(i), 1);
//             }
//             if(t_map.containsKey(t.charAt(i))){
//                 t_map.put(t.charAt(i), 1 + t_map.get(t.charAt(i)));
//             } else{
//                 t_map.put(t.charAt(i), 1);
//             }
//         }
//         for(Character c: s_map.keySet()){
//             if(s_map.get(c) != t_map.get(c)){
//                 System.out.println(c);
//                 System.out.println(s_map);
//                 System.out.println(t_map);
//                 System.out.println(s_map.get(c));
//                 System.out.println(t_map.get(c));
//                 return false;
//             }
//         }
//         return true;
//     }
// }

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        
        Map<Character, Integer> s_map = new HashMap<>();
        Map<Character, Integer> t_map = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++){
            s_map.put(s.charAt(i), s_map.getOrDefault(s.charAt(i), 0) + 1);
            t_map.put(t.charAt(i), t_map.getOrDefault(t.charAt(i), 0) + 1);
        }
        
        for(Character c : s_map.keySet()){
            if(!t_map.containsKey(c) || !s_map.get(c).equals(t_map.get(c))){
                return false;
            }
        }
        
        return true;
    }
}
