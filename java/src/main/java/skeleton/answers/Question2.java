package skeleton.answers;
import java.io.*;
import java.util.*;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
        // TODO Auto-generated method stub
        Trade t[] = new Trade[risk.length];
        for(int i=0;i<risk.length;i++){
            t[i] = new Trade(risk[i],bonus[i]);
        }
		CompareTrade ct =new CompareTrade();
        Arrays.sort(t,ct);
        Arrays.sort(trader);
        int j=trader.length-1;
        int i=risk.length-1;
        int sum=0;
        while(j>=0&&i>=0){
            if(trader[j]>=t[i].risk){
		sum+=t[i].bonus;
		j--;
	    }
            else i--;
            
        }
        return sum;
    }
    static class Trade  {
        int risk;
        int bonus;
        public Trade(int r,int b){
            this.risk=r;
            this.bonus= b;
        }
    }
	public static class CompareTrade implements Comparator<Trade>{
		public int compare(Trade t1,Trade t2){
			return (t1.bonus==t2.bonus)?t2.risk-t1.risk:t1.bonus-t2.bonus;
		}
	}
}

