import { print } from "introcs";

export let main = async () => {
    let v = [6, 10, 12];
    let c = [30, 60, 90];
    let mc = 90;
    print(answerFour(v, c, mc));
};

let answerFour = (v: number[], c: number[], mc: number): number => {
    let number = 0;
    let index: number[] = [];
    for (let i = c.length - 1; i >= 0; i--) {
        number += c[i];
        if (c[i] === mc) {
            // Problem with this scenario because output would be 12 and not 16
        }
        if (number <= mc) {
            index[index.length] = i;
        } else {
            number -= c[i];
        }
    }
    let answer = 0;
    for (let i = 0; i < index.length; i++) {
        answer += v[index[i]];
    }
    return answer;
};

main();