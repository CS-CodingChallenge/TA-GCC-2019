package skeleton.answers;

public class Question1 {

    public static double calculateTotalPayment(double initialLevelOfDebt, double interestPercentage, double repaymentPercentage) {
        double currentDebt = initialLevelOfDebt;
        double fixedRepayment = ((repaymentPercentage * initialLevelOfDebt / 100) > 50)? (repaymentPercentage * initialLevelOfDebt / 100) : 50;
        double deposit = 0.10 * initialLevelOfDebt;
        double totalAmountSpent = 0;
        
        
        while(currentDebt > 0) {
            currentDebt = (1 + interestPercentage / 100) * currentDebt;
            if(currentDebt < fixedRepayment) {
                currentDebt = 0;
                totalAmountSpent += currentDebt;
            } else {
            currentDebt -= fixedRepayment;
            totalAmountSpent += fixedRepayment;
            }      
        }
        return totalAmountSpent + deposit;
    }

}
