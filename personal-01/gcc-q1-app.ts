import { print } from "introcs";

export let main = async () => {
    print(calculateTotalPayment(1000, 5, 10));
};

let calculateTotalPayment = (debt: number, interest: number, repayment: number): number => {
    let cost = 0;
    interest /= 100;
    repayment /= 100;
    cost = debt * .1;
    debt -= cost;
    let payment: number;
    while (debt > 0) {
        payment = debt * repayment;
        if (payment < 50) {
            payment = 50;
        }
        debt = debt * (1 + interest);
        if (payment - debt < 0) {
            payment = 50;
        }
        debt -= payment;
        cost += payment;
    }
    return cost;
};

main();