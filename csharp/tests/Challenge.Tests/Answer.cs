namespace Challenge.Tests
{
    public class Answer {
        public int questionNumber { get; set; }
        public int testNumber { get; set; }
        public string correct { get; set; }
        public double speed { get; set; }
        public int expected { get; set; }
        public int actual { get; set; }
        public string inputs { get; set; }
    }
}