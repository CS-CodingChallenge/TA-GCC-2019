import { print } from "introcs";

export let main = async () => {
    let othersScores = [100, 90, 90, 80, 75, 60];
    let yourScores = [50, 77, 77, 90];
    print(modalRanking(othersScores, yourScores));
};

let modalRanking = (i: number[], j: number[]): number => {
    let rankings: number[] = [];
    let rankingsIndex = 0;
    let index: number[] = [];
    let c = 0;
    let d = 0;
    i[i.length] = 0;
    for (let a = j.length - 1; a >= 0; a--) {
        for (let b = 0; b < i.length; b++) {
            if (j[a] > i[d]) {
                rankings[rankingsIndex] = j[a];
                index[c] = rankingsIndex;
                c++;
                b = i.length;
            } else {
                if (i[d] <= rankings[rankingsIndex - 1] || i[d] === 100) {
                    rankings[rankingsIndex] = i[d]
                    d++;
                }
            }
            rankingsIndex++;
        }
    }
    let rankingsNumber: number[] = [];
    let rank = 1;
    for (let a = 0; a < rankings.length; a++) {
        if (rankings[a] === rankings[a - 1] && a !== 0) {
            rankingsNumber[a] = rankingsNumber[a - 1];
        } else {
            rankingsNumber[a] = rank;
            rank++;
        }
    }
    let ranks: number[] = [];
    for (let a = 0; a < index.length; a++) {
        ranks[a] = rankingsNumber[index[a]];
    }
    let count = 0;
    let mode: number;
    for (let b = 0; b < ranks.length; b++) {
        let otherCount = 0;
        for (let c = 0; c < ranks.length; c++) {
            if (ranks[c] === ranks[b]) {
                otherCount++;
            } 
        }
        if (otherCount >= count) {
            count = otherCount;
            mode = ranks[b];
        }
    }
    return mode;
};

main();