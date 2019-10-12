package skeleton.answers;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
    	int arrayLength = trader.length;
 	   int maxBonus = 0, totalBonus = 0,maxIndex = 0, minRisk = 10000;
 		//Finding the maximum bonus in the bonus array
 		for(int i = 0; i < arrayLength; i++)
 		{
 			if(bonus[i] >= maxBonus)
 			{
 				maxBonus = bonus[i];
 				
 				//Checking the risk associated with maximum bonus
 				if(risk[i] < minRisk)
 				{
 					//Taking the index of minimum risk
 					minRisk = risk[i];
 					maxIndex = i;
 				}
 				
 			}
 		}
 		//Finding the total maximum bonus	
 		for(int j = 0; j < arrayLength; j++)
 		{
 			if(trader[j] >= risk[maxIndex])
 			{
 				totalBonus += maxBonus; 
 			}
 		}
 		return totalBonus;
     
    }
}
