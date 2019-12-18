package skeleton.answers;
import java.util.*; 

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
       HashMap<Integer, Integer> map 
            = new HashMap<>(); 
 Arrays.sort(trader); 

      
       for(int i=0;i<risk.length;i++)
       {
         if(map.containsKey(bonus[i]))
         {
           if(map.get(bonus[i])>risk[i])
           map.put(bonus[i],risk[i]);
         }
         else
         {
            map.put(bonus[i],risk[i]);
         }
       }

        ArrayList<Integer> keys = new ArrayList<Integer>(map.keySet());
        int i=keys.size()-1;
        int j=trader.length-1;
        int sum=0;
        while(i>=0 && j>=0)
        {
           if(trader[j]>=map.get(keys.get(i)))
           {
           sum=sum+keys.get(i);
          j--;
           }
           else
           {
             i--;
           }
           
        }
        
       return sum;
    }
}
