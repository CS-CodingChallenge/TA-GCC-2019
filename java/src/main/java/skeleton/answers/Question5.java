package skeleton.answers;

public class Question5 {
    public static int selfpreservation(Integer[] input) {
        int instances = 1;
		
		for(int i = 1; i < threats.length; i += 2)
		{
			//Starting from the 2nd element, check if the element is greater or lesser than the next element.
			if(threats[i] < threats[i+1])
			{
				instances++;   		//Increment the instances if it is lesser
			}
			else
			{
				continue;		//Else continue to the for loop with next element
			}
		}
		
		return instances;
	}
}
