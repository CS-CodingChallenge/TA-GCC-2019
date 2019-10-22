package skeleton.answers;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
        int teamMaxScore = 0;
        for(int td : trader) {
            int max = 0;
            for(int i = 0; i < bonus.length; i++){
                if(td >= risk[i] && bonus[i] > max){
                    max = bonus;
                }
            }
            teamMaxScore += max;
        } 
        return teamMaxScore;
    }
}
