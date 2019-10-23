package skeleton.answers;

public class Question6 {

    public static int startingAndEndingWell(String[] portfolio, String starting, String ending) {
        int highestValue = 0;
        boolean found = false;
        for(i = 0; i < portfolio.length; i++){
            if(portfolio[i].startsWith(starting) && portfolio[i].endsWith(ending)){
                found = true;
                highestValue = i;
            }
        }
        
        if(!found){
            return -1;
        } else {
            return highestValue;
        }
    }
}
