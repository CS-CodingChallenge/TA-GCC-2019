package skeleton.answers;

public class Question2 {

    public static int riskAndReward(int[] risk, int[] bonus, int[] trader) {
        
        Scanner sc=new Scanner(System.in);
	    int cnt1=trader.length;
        int cnt3=risk.length;
        int cnt2=bonus.length;
	//int tr[],rs[],bs[];
        
	
	//System.out.println("Number of entries:");
	//cnt=sc.nextInt();
	
	/*int tr[]=new int[cnt];
	System.out.println("Number of entries:1");
	int rs[]=new int[cnt];
	System.out.println("Number of entries:2");
	int bs[]=new int[cnt];
	System.out.println("Number of entries:3");
	*/
	/*for(int i=0;i<cnt;i++)
	{
		tr[i]=sc.nextInt();
		//System.out.println("Number of entries:11");
	}
	for(int i=0;i<cnt;i++)
	{
		//rs[i]=sc.nextInt();
	}
	for(int i=0;i<cnt;i++)
	{
		//bs[i]=sc.nextInt();
	}*/
        
        
	int bns=0;
	int bnsfnl=0;
	int tdr;
	for(int i=0;i<cnt1;i++)
	{
		tdr=trader[i];
		for(int j=0;j<cnt3;j++)
		{
			if(tdr>=risk[j])
			{
				if(bns<bonus[j])
				{
					bns=bonus[j];
				}
			}
		}
		bnsfnl=bnsfnl+bns;
		bns=0;
	}
	
	System.out.println(bnsfnl);
	
        // TODO Auto-generated method stub
        return -5;
    }
}
