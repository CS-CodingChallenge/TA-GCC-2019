package skeleton.answers;

public class Question6 {
  static int yourMethod(char start, char end, String s[])
    {
        int idx=-1;
        for(int i=s.length-1;i>=0;i++)
        {
          if(s[i].charAt(0)==start && s[i].charAt(s[i].length()-1)==end)
          {
              idx=i;
              break;
          }
        }
        return idx;
    }
    public static int startingAndEndingWell(String[] portfolio) {
        System.out.println(yourMethod('A', 'W', portfolio));
        return -5;
    }
}
