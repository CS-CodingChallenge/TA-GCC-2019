package skeleton.answers;

import java.util.ArrayList;

public class Question5 {
    public static int selfpreservation(Integer[] input) {
        int numberOfThreats = input[0];
        int currentTime = input[1];
        ArrayList<Integer> frequencies = new List<>();
        frequencies.add(input[2]);
        
        for(int i = 3; i < input.length; i += 2){
            int requiredFrequency = input[i+1];
            int needX = needNewX(requiredFrequency, frequencies, currentTime, input[i]);
            if(needX == -1) {
                currentTime = input[i];
            } else if(needX == -2) {
                frequencies.add(input[i+1]);
                currentTime = input[i];
            } else {
                frequencies.remove(needX);
                frequencies.add(input[i+1]);
                currentTime = input[i];
            }
        }
        return frequencies.size();
    }
    
    private static int needNewX(int requiredFrequency, ArrayList<Integer> frequencies, int currentTime, int nextTime) {
        
        if(frequencies.contains(requiredFrequency)){
            return -1;
        } else {
            int difference = nextTime - currentTime;
            // Compute least time taken to change. 
            int timeTakenToChange = 1000000;
            int indexToBeRemoved = 1000000;
            for(int i = 0; i < frequencies.size(); i++){
                if(Math.abs(frequencies.get(i) - requiredFrequency) < timeTakenToChange) {
                    timeTakenToChange = Math.abs(frequency - requiredFrequency);
                    indexToBeRemoved = i;
                }
            }
            if(difference > timeTakenToChange) {
                return indexToBeRemoved;
            } else {
                return -2;
            }
            
        }
    
    }
}
