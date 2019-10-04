const Promise = require('bluebird')
const axios = require('axios');

const performance = require('performance-now')
const question01 = require('./questions/Question1')
const question02 = require('./questions/Question2')
const question03 = require('./questions/Question3')
const question04 = require('./questions/Question4')
const question05 = require('./questions/Question5')
const question06 = require('./questions/Question6')


describe('Coding Challenge Skeleton Tests', () => {

    describe('Q1', () => {

        it('runs question 1', async () => {
            return getTests(1)
                .then(tests => {
                    let promises = []
                    let output = []
                    for (let i = 0; i < tests.length; i++) {
                        try {
                            const testRunner = new Promise((resolve, reject) => {
                                const test = tests[i]
                                const runtest = runq1
                                runtest(test)
                                    .timeout(1000)
                                    .then(({answer, timeTaken}) => {
                                        console.log(test.input + " is " + correct)
                                        output.push({
                                            "questionNumber": 1,
                                            "testNumber": i,
                                            "correct": correct,
                                            "speed": timeTaken * 1000000
                                        })
                                    })
                                    .catch(Promise.TimeoutError, (e) => {
                                        console.log("A question 1 test has timed out. Each individual test has a maximum of one second to run.")
                                        resolve(output.push({
                                            "questionNumber": 1,
                                            "testNumber": i,
                                            "correct": "TIMED_OUT",
                                            "speed": -1
                                        }))
                                    })
                            })
                            promises.push(testRunner)
                        } catch (error) {
                            console.log(error)
                        }
                    }
                    return Promise.all(promises).then((response) => submitAnswers(response, 1))

                })
                .catch(() => "Something went wrong.");

        })

        describe('Q2', () => {

            it('runs question 2', () => {
                return getTests(2)
                    .then(tests => {
                        let promises = []

                        for (let i = 0; i < tests.length; i++) {
                            try {
                                const testRunner = new Promise((resolve, reject) => {
                                    const test = tests[i]
                                    const runtest = runq2
                                    runtest(test)
                                        .timeout(1000)
                                        .then(({answer, timeTaken}) => {
                                            const correct = answer === test["output"] ? "CORRECT" : "INCORRECT" ? "CORRECT" : "INCORRECT"
                                            resolve({
                                                "questionNumber": 2,
                                                "testNumber": i,
                                                "correct": correct,
                                                "speed": timeTaken * 1000000
                                            })
                                        })
                                        .catch(Promise.TimeoutError, (e) => {
                                            console.log("A question 2 test has timed out. Each individual test has a maximum of one second to run.")
                                            resolve({
                                                "questionNumber": 2,
                                                "testNumber": i,
                                                "correct": "TIMED_OUT",
                                                "speed": -1
                                            })
                                        })
                                })
                                promises.push(testRunner)
                            } catch (error) {
                                console.log(error)
                            }
                        }
                        return Promise.all(promises).then((response) => submitAnswers(response, 2))

                    })
            })
        })

        describe('Q3', () => {

            it('runs question 3', () => {
                return getTests(3)
                    .then(tests => {
                        let promises = []
                        for (let i = 0; i < tests.length; i++) {
                            try {
                                const testRunner = new Promise((resolve, reject) => {
                                    const test = tests[i]
                                    const runtest = runq3
                                    runtest(test)
                                        .timeout(1000)
                                        .then(({answer, timeTaken}) => {
                                            const correct = answer === test["output"] ? "CORRECT" : "INCORRECT"
                                            resolve({
                                                "questionNumber": 3,
                                                "testNumber": i,
                                                "correct": correct,
                                                "speed": timeTaken * 1000000
                                            })
                                        })
                                        .catch(Promise.TimeoutError, (e) => {
                                            console.log("A question 3 test has timed out. Each individual test has a maximum of one second to run.")
                                            resolve({
                                                "questionNumber": 3,
                                                "testNumber": i,
                                                "correct": "TIMED_OUT",
                                                "speed": -1
                                            })
                                        })
                                })
                                promises.push(testRunner)
                            } catch (error) {
                                console.log(error)
                            }
                        }
                        return Promise.all(promises).then((response) => submitAnswers(response, 3))

                    })
            })
        })

        describe('Q4', () => {

            it('runs question 4', () => {
                return getTests(4)
                    .then(tests => {
                        let promises = []
                        for (let i = 0; i < tests.length; i++) {
                            try {
                                const testRunner = new Promise((resolve, reject) => {
                                    const test = tests[i]
                                    const runtest = runq4
                                    runtest(test)
                                        .timeout(1000)
                                        .then(({answer, timeTaken}) => {
                                            const correct = answer === test["output"] ? "CORRECT" : "INCORRECT"
                                            resolve({
                                                "questionNumber": 4,
                                                "testNumber": i,
                                                "correct": correct,
                                                "speed": timeTaken * 1000000
                                            })
                                        })
                                        .catch(Promise.TimeoutError, (e) => {
                                            console.log("A question 4 test has timed out. Each individual test has a maximum of one second to run.")
                                            resolve({
                                                "questionNumber": 4,
                                                "testNumber": i,
                                                "correct": "TIMED_OUT",
                                                "speed": -1
                                            })
                                        })
                                })
                                promises.push(testRunner)
                            } catch (error) {
                                console.log(error)
                            }
                        }
                        return Promise.all(promises).then((response) => submitAnswers(response, 4))

                    })
            })

        })

        describe('Q5', () => {

            it('runs question 5', () => {
                return getTests(5)
                    .then(tests => {
                        let promises = []
                        for (let i = 0; i < tests.length; i++) {
                            try {
                                const testRunner = new Promise((resolve, reject) => {
                                    const test = tests[i]
                                    const runtest = runq5
                                    runtest(test)
                                        .timeout(1000)
                                        .then(({answer, timeTaken}) => {
                                            const correct = answer === test["output"] ? "CORRECT" : "INCORRECT"
                                            resolve({
                                                "questionNumber": 5,
                                                "testNumber": i,
                                                "correct": correct,
                                                "speed": timeTaken * 1000000
                                            })
                                        })
                                        .catch(Promise.TimeoutError, (e) => {
                                            console.log("A question 5 test has timed out. Each individual test has a maximum of one second to run.")
                                            resolve({
                                                "questionNumber": 5,
                                                "testNumber": i,
                                                "correct": "TIMED_OUT",
                                                "speed": -1
                                            })
                                        })
                                })
                                promises.push(testRunner)
                            } catch (error) {
                                console.log(error)
                            }
                        }
                        return Promise.all(promises).then((response) => submitAnswers(response, 5))
                    })
            })
        })

        describe('Q6', () => {

            it('runs question 6', () => {
                return getTests(6)
                    .then(tests => {
                        let promises = []
                        for (let i = 0; i < tests.length; i++) {
                            try {
                                const testRunner = new Promise((resolve, reject) => {
                                    const test = tests[i]
                                    const runtest = runq6
                                    runtest(test)
                                        .timeout(1000)
                                        .then(({answer, timeTaken}) => {
                                            const correct = answer === test["output"] ? "CORRECT" : "INCORRECT"
                                            resolve({
                                                "questionNumber": 6,
                                                "testNumber": i,
                                                "correct": correct,
                                                "speed": timeTaken * 1000000
                                            })
                                        })
                                        .catch(Promise.TimeoutError, (e) => {
                                            console.log("A question 6 test has timed out. Each individual test has a maximum of one second to run.")
                                            resolve({
                                                "questionNumber": 6,
                                                "testNumber": i,
                                                "correct": "TIMED_OUT",
                                                "speed": -1
                                            })
                                        })
                                })
                                promises.push(testRunner)
                            } catch (error) {
                                console.log(error)
                            }
                        }
                        return Promise.all(promises).then((response) => submitAnswers(response, 6))
                    })
            })
        })
    })
})

const getTests = (question) => {
    const uuid = process.env.travistestidentifier;
    let url = `https://cscc-gl.herokuapp.com/tests/run/${question}`
    if (uuid !== undefined) {
        url = `${url}/${uuid}`
    }
    return axios.get(url)
        .then(function (response) {
            // console.log(response);
            return response.data
        }).catch(function (response) {
            console.log(response)
        })
}

const submitAnswers = (answers, question) => {
    const uuid = process.env.travistestidentifier;
    if (uuid !== undefined) {
        const url = `https://cscc-gl.herokuapp.com/answer/contestant/${uuid}/${question}`
        return axios.post(url, answers).then(function (response) {
            console.log(response);
        }).catch(function (response) {
            console.log(response)
        })
    }
}

function runq1(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question01(input['initialLevelOfDebt'], input['interestPercentage'], input['repaymentPercentage'])
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}

function runq2(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question02(input['risk'], input['bonus'], input['trader'])
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}

function runq3(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question03(input['scores'], input['alice'])
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}

function runq4(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question04(input['v'], input['c'], input['mc'])
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}

function runq5(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question05(input)
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}

function runq6(test) {
    return new Promise((resolve, reject) => {
        const input = JSON.parse(test['input'])
        const t0 = performance()
        const answer = question06(input)
        const t1 = performance()
        const timeTaken = t1 - t0
        return resolve({
            answer,
            timeTaken
        })
    })
}