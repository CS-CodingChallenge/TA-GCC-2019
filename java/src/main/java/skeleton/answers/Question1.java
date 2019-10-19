package skeleton.answers;

public class Question1 {

    public static double calculateTotalPayment(double initialLevelOfDebt, double interestPercentage, double repaymentPercentage) {
        // TODO Auto-generated method stub
        double ild = initialLevelOfDebt;
		double ip = interestPercentage;
		double rp = repaymentPercentage;
		double d = 0.1 * ild;
		double r = (rp/100) * ild;
		int c = 0;
		while(ild > 50)
		{
			ild = (1 + ip/100) * ild;
			ild -= r;
			c++;
			
		}
		double res = c * r + ild + d;
        return res;
    }

}
