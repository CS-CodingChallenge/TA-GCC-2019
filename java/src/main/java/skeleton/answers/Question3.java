package skeleton.answers;

public class Question3 {

    public static int whereDidIFinish(int[] scores, int[] alice) {
        // TODO Auto-generated method stub
        Integer[] scores = new Integer[score.length];
	Integer[] alice = new Integer[alic.length];
	for(int i=0;i<alic.length;i++){
		alice[i] = (Integer)alic[i];
	}
	for(int i=0;i<score.length;i++){
		scores[i] = (Integer)score[i] ;
	}
	int[] ranks = new int[alice.length];
        Arrays.sort(scores, Collections.reverseOrder());
	    Arrays.sort(alice, Collections.reverseOrder());
		int i=0;
		int j=0;
		int rank=1;
		while(j<alice.length&&alice[j]>=scores[i]){
			ranks[j]=rank;
			j++;
		}
		rank++;
		i++;
		while(j<alice.length&&i<scores.length){
			if(alice[j]>=scores[i]){
				ranks[j]=rank;
				j++;
			}else if(scores[i]!=scores[i-1]){
				rank++;
				i++;
			}else{
				while(scores[i]==scores[i-1]&&i<scores.length)i++;
			}
		}
		while(j<alice.length){
			ranks[j]=rank;
			j++;
		}
		int ct=1,mode=1;
		rank=ranks[0];
		for(i=1;i<ranks.length;i++){
			if(ranks[i]!=ranks[i-1]){
				if(ct>mode){
					mode = ct;
					rank = ranks[i-1];
				}
				ct=1;
			}else{
				ct++;
			}
		}
		if(ct>mode){
			mode = ct;
			rank = ranks[i-1];
		}
        return rank;    }
}
