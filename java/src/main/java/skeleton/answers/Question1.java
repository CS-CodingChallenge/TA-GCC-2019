package skeleton.answers;

public class Question1 {

    public static double calculateTotalPayment(double initialLevelOfDebt, double interestPercentage, double repaymentPercentage) {
        // TODO Auto-generated method stub
        double debt = initialLevelOfDebt;

        double repay = repaymentPercentage/100*initialLevelOfDebt;

        if(repay<50)repay = 50;

        int ct =0;

        while(debt>=50){

            debt = debt*(1+interestPercentage/100)-repay;

            ct++;

        }

        

        return (repay*ct + debt + repay);

    }
}
