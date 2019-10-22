package skeleton.answers;

import java.util.Arrays;

public class Question3 {

    public static int whereDidIFinish(int[] scores, int[] alice) {
        Arrays.sort(alice);  //sorts scores in ascending order
        
        int[] myRanks = new int[alice.length];
        for(int i = 0; i < alice.length; i++) {
            int rank = scores.length;  // Firstly I am the last one, then check my actual position
            int j = 0;
            while(j < rank){
                if(myScore >= scores[j]){
                    rank = j;
                } else {
                    j++;
                }
            }
            myRanks[i] = rank + 1;   // Plus one because I want to count from 1 (not from 0)
        }
        
        int modalRank = myRanks[alice.length/2];  //Taking into account that scores are ascending order and index starts at 0. Oddity does not matter. 
        return modalRank;
    }
}
