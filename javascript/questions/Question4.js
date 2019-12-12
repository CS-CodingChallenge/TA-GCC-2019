// Use this file to answer question 4

function answer04(v, c, mc) {
    var number = 0;
    var index = [];
    for (var i = c.length - 1; i >= 0; i--) {
        number += c[i];
        if (number <= mc) {
            index[index.length] = i;
        } else {
            number -= c[i];
        }
    }
    var answer = 0;
    for (var i = 0; i < index.length; i++) {
        answer += v[index[i]];
    }
    return answer;
}

module.exports = answer04

git push
