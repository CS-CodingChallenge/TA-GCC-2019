using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Challenge.Answers;
using Newtonsoft.Json;
using NUnit.Framework;

namespace Challenge.Tests
{
    [TestFixture]
    public class SkeletonTests
    {
       private static readonly HttpClient client = new HttpClient();
       private readonly string baseUrl = "https://cscc-gl.herokuapp.com/";

        [Test]
        public async Task TestQ1()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/1/" + travisUUID);
 
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Q1Object input = JsonConvert.DeserializeObject<Q1Object>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    Answer answer = await Task.Run(() => getFirstAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 1 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 1,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }

            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/1", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));

        }

        Answer getFirstAnswer(Q1Object input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question1.Answer(input.initialLevelOfDebt, input.interestPercentage, input.repaymentPercentage, test.output);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 1,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken,
                expected = (int)test.output,
                actual = answer,
                inputs = $"{input.initialLevelOfDebt}, {input.interestPercentage}, {input.repaymentPercentage}"

            };
        }

        [Test]
        public async Task TestQ2()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/2/" + travisUUID);
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Answer answer = new Answer();
                    Q2Object input = JsonConvert.DeserializeObject<Q2Object>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    await Task.Run(() => answer = getSecondAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 2 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 2,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }

            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/2", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));
        }

        Answer getSecondAnswer(Q2Object input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question2.Answer(input.risk, input.bonus, input.trader);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 2,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken
            };
        }

        [Test]
        public async Task TestQ3()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/3/" + travisUUID);
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Answer answer = new Answer();
                    Q3Object input = JsonConvert.DeserializeObject<Q3Object>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    await Task.Run(() => answer = getThirdAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 3 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 3,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }

            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/3", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));
        }

        Answer getThirdAnswer(Q3Object input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question3.Answer(input.scores, input.alice);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 3,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken
            };
        }

        [Test]
        public async Task TestQ4()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/4/" + travisUUID);
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Answer answer = new Answer();
                    Q4Object input = JsonConvert.DeserializeObject<Q4Object>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    await Task.Run(() => answer = getFourthAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 4 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 4,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }

            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/4", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));
        }

        Answer getFourthAnswer(Q4Object input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question4.Answer(input.v, input.c, input.mc);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 4,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken
            };
        }

        [Test]
        public async Task TestQ5()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/5/" + travisUUID);
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Answer answer = new Answer();
                    int[] input = JsonConvert.DeserializeObject<int[]>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    await Task.Run(() => answer = getFifthAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 5 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 5,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }


            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/5", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));
        }

        Answer getFifthAnswer(int[] input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question5.Answer(input);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 5,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken
            };
        }

        [Test]
        public async Task TestQ6()
        {
            var travisUUID = Environment.GetEnvironmentVariable("travis_uuid");
            if (travisUUID == null)
            {
                travisUUID = "";
            }

            string responseBody = await client.GetStringAsync(baseUrl + "tests/run/6/" + travisUUID);
            List<TestCase> testCases = JsonConvert.DeserializeObject<List<TestCase>>(responseBody);
            
            List<Answer> answers = new List<Answer>();

            foreach (var test in testCases)
            {
                try
                {
                    Answer answer = new Answer();
                    string[] input = JsonConvert.DeserializeObject<string[]>(test.input);
                    var cancellationToken = new CancellationTokenSource();
                    cancellationToken.CancelAfter(1000);
                    await Task.Run(() => answer = getSixthAnswer(input, test), cancellationToken.Token);
                    answers.Add(answer);
                }
                catch (TaskCanceledException _)
                {
                    Console.WriteLine("A test in Question 6 has timed out. Tests must complete within one second.");
                    answers.Add(new Answer()
                    {
                        questionNumber = 6,
                        testNumber = test.testNumber,
                        correct = "TIMED_OUT",
                        speed = -1
                    });
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace);
                }
            }


            if (travisUUID.Length > 0)
            {
                string ans = JsonConvert.SerializeObject(answers);
                await client.PostAsync(baseUrl + "answer/contestant/" + travisUUID + "/6", new StringContent(ans));
            }

            Assert.IsTrue(answers.All(x => x.correct == "CORRECT"));
        }

        Answer getSixthAnswer(string[] input, TestCase test)
        {
            var timer = new Stopwatch();

            timer.Start();

            var answer = Question6.Answer(input);

            timer.Stop();

            var timeTaken = ((double)timer.ElapsedTicks / Stopwatch.Frequency) * 1000000000;

            return new Answer()
            {
                questionNumber = 6,
                testNumber = test.testNumber,
                correct = answer == test.output ? "CORRECT" : "INCORRECT",
                speed = timeTaken
            };
        }
    }
}
