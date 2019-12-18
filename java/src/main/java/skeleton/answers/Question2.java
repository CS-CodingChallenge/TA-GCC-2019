package skeleton.answers;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
        // TODO Auto-generated method stub
        int bonus_value = 0;
        int temp;
        int n = bonus.length;
        int i,j;
        for (i = 0; i < n-1; i++) {
			for (j = 0; j < n-i-1; j++) {
    			if (bonus[j] > bonus[j+1]) {
            		temp = bonus[j];
            		bonus[j] = bonus[j+1];
            		bonus[j+1] = temp;
     				temp = risk[j];
     				risk[j] = risk[j+1];
     				risk[j+1] = temp;
        		}
    		}
        }  

        for (i = 0; i < trader.length; i++) {
        	for (j = 0; j < n; j++) {
        		if (trader[i] >= risk[j]) {
        			bonus_value += bonus[j];
        			break;
        		}
        	}
        }
    	return bonus_value;
    }
}
