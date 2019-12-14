// Use this file to answer question 3

function answer03(scores, alice) {
    var rankings = [];
    var rankingsIndex = 0;
    var index = [];
    var c = 0;
    var d = 0;
    scores[scores.length] = 0;
    for (var a = alice.length - 1; a >= 0; a--) {
        for (var b = 0; b < scores.length; b++) {
            if (alice[a] > scores[d]) {
                rankings[rankingsIndex] = alice[a];
                index[c] = rankingsIndex;
                c++;
                b = scores.length;
            } else {
                if (scores[d] <= rankings[rankingsIndex - 1] || scores[d] === 100) {
                    rankings[rankingsIndex] = scores[d]
                    d++;
                }
            }
            rankingsIndex++;
        }
    }
    var rankingsNumber = [];
    var rank = 1;
    for (var a = 0; a < rankings.length; a++) {
        if (rankings[a] === rankings[a - 1] && a !== 0) {
            rankingsNumber[a] = rankingsNumber[a - 1];
        } else {
            rankingsNumber[a] = rank;
            rank++;
        }
    }
    var ranks = [];
    for (var a = 0; a < index.length; a++) {
        ranks[a] = rankingsNumber[index[a]];
    }
    var count = 0;
    var mode;
    for (var b = 0; b < ranks.length; b++) {
        var otherCount = 0;
        for (var c = 0; c < ranks.length; c++) {
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
}

module.exports = answer03

git push
