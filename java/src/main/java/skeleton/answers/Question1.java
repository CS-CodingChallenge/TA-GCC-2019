package skeleton.answers;
import java.util.*;
public class Question1 {

    public static double calculateTotalPayment(double initialLevelOfDebt, double interestPercentage, double repaymentPercentage) {
        double fixedRe=repaymentPercentage*initialLevelOfDebt;
        double temp=initialLevelOfDebt;
        int count=0;
        while(temp>=50){
            temp=temp-(temp)*interestPercentage;
            temp=temp+fixedRe;
            count++;
        }
        double final=count*fixedRe+temp+fixedRe;
        return final;
    }

}
