import java.util. *;

class MapMain{
    public static void main(String[] args) {
        char[] chars = {'a', 'b', 'b','b','b','b','b','b','b','b','b','b','b','b','b','b', 'b'};
        HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();
        for(char c : chars){
            if(!charMap.containsKey(c)){
                charMap.put(c, 0);
            }
            charMap.put(c, charMap.get(c) + 1);
        }
        
        int compressionCount = 0;
        
        for (int i : charMap.values()) {
            
            String str = String.valueOf(i);
            if(str.length() == 1){
                compressionCount += 1;
                continue;
            }
            compressionCount += str.length() + 1;
        }
        
        int i = -1;
        for(Map.Entry<Character, Integer> entry : charMap.entrySet()){
            if(entry.getValue()== 1){
                chars[++i] = entry.getKey(); 
                
                continue;
            }
            chars[++i] = entry.getKey(); 
            
            String str = String.valueOf(entry.getValue());
            System.out.println(str);
          
            for (int j = 0; j < str.length(); j++) {
                chars[++i] = str.charAt(j);
               
            }

        } 

for (int j = 0; j < compressionCount; j++) {
    System.out.print(chars[j]);
    
}
        
    }
}