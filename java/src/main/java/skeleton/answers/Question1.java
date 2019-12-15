package skeleton.answers;

public class Question1 {

    public static double calculateTotalPayment(double initialLevelOfDebt, double interestPercentage, double repaymentPercentage) {
        // TODO Auto-generated method stub
        			double debt = initialLevelOfDebt;
			double rdebt=debt;
			int count = 0;
			
			while(rdebt>=50)
			{
				debt = rdebt+ rdebt*interestPercentage/100;
				rdebt= debt -repay;
				count++;
				
			}
			double res;
			
			res = (count*repay)+(initialLevelOfDebt*0.1)+rdebt;
			
			return res;
    }

}
