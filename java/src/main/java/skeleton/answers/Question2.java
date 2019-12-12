package skeleton.answers;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
int maxProfit = 0;
		
		Map<String, Map<Integer,Integer>> map = new HashMap<String, Map<Integer,Integer>>();
		Map<String,Map<Integer,Integer>> mapRiskToBonus = new HashMap<String, Map<Integer,Integer>>();
		Map<String, Integer> mapMaxBonus = new HashMap<String, Integer>();
		
		/*	Makes the following
		 * 	
		 * 	6	-	
		 * 			0 1 2 3		- indexes
		 * 			5 4 3 1
		 * 
		 * 	7	-	
		 * 			0 1 2 3 	- indexes
		 * 			5 4 3 1
		 * 
		 *  2	- 	
		 *  		3			- indexes
		 *  		1
		 *  
		 *  8	-	
		 *  		0 1 2 3 4 	- indexes
		 *  		5 4 3 1 8
		 *  
		 *  1	- 	
		 *  		3		  	- indexes
		 *  		1
		 * 
		 */
		for(int i=0; i<trader.length; i++) {
			for(int j=0; j<risk.length; j++) {
				if(trader[i] >= risk[j]) {
					if(map.get(String.valueOf(i) + " " + String.valueOf(trader[i])) == null) {
						map.put(String.valueOf(i) + " " + String.valueOf(trader[i]), new HashMap<Integer,Integer>());
					}
					map.get(String.valueOf(i) + " " + String.valueOf(trader[i])).put(j,risk[j]);
				}
			}
		}
		
		Iterator<Entry<String, Map<Integer, Integer>>> parent = map.entrySet().iterator();
		while (parent.hasNext()) {
		    Entry<String, Map<Integer, Integer>> parentPair = parent.next();
		    //System.out.println("parentPair.getKey() :   " + parentPair.getKey() + " parentPair.getValue()  :  " + parentPair.getValue());
		    Iterator<Entry<Integer, Integer>> child = (parentPair.getValue()).entrySet().iterator();
		    
		    while (child.hasNext()) {
		        Entry<Integer, Integer> childPair = child.next();
		        //System.out.println("childPair.getKey() :   " + childPair.getKey() + " childPair.getValue()  :  " + childPair.getValue());
		        
		        for(int i=0; i<bonus.length; i++) {
		        	if(i == childPair.getKey()) {
		        		if(mapRiskToBonus.get(parentPair.getKey()) == null) {
		    		    	mapRiskToBonus.put(parentPair.getKey(), new HashMap<Integer,Integer>());	// gets max of risks that trader can do
		    		    }
		        		mapRiskToBonus.get(parentPair.getKey()).put(childPair.getKey(),bonus[i]);
		        	}
		        }
		    }
		    
		}
		
		Iterator<Entry<String, Map<Integer, Integer>>> parent1 = mapRiskToBonus.entrySet().iterator();
		while (parent1.hasNext()) {
		    Entry<String, Map<Integer, Integer>> parentPair = parent1.next();
		    //System.out.println("parentPair.getKey() :   " + parentPair.getKey() + " parentPair.getValue()  :  " + parentPair.getValue());
		    Iterator<Entry<Integer, Integer>> child = (parentPair.getValue()).entrySet().iterator();
		    int maxBonus = 0;
		    while (child.hasNext()) {
		        Entry<Integer, Integer> childPair = child.next();
		        //System.out.println("childPair.getKey() :   " + childPair.getKey() + " childPair.getValue()  :  " + childPair.getValue());
		        
		        if(maxBonus < childPair.getValue()) {
		        	maxBonus = childPair.getValue();
		        }
		        
		    }
		    
		    if(mapMaxBonus.get(parentPair.getKey()) == null) {
		    	mapMaxBonus.put(parentPair.getKey(),maxBonus);
		    } 
		    
		}
		
		Iterator<Entry<String, Integer>> entryIterator = mapMaxBonus.entrySet().iterator();
		 
		while (entryIterator.hasNext())
		{
		    Entry<String, Integer> entry = entryIterator.next();
		     
		    System.out.println("The key is :: " + entry.getKey() + ", and value is :: " + entry.getValue() );
		    
		    maxProfit += entry.getValue();
		}
		
		
		return maxProfit;
    }
}
