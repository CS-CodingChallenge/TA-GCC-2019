// Use this file to answer question 2

function answer02(risk, bonus, trader) {
    var total = 0;
    for (var j = 0; j < trader.length; j++) 
    {
        var riskNumbers = [];
        for (var i = 0; i < risk.length; i++) 
        {
            if (trader[j] >= risk[i]) 
            {
                riskNumbers.push(i);
            }
        }
        var highest = 0;
        for (var i = 0; i < riskNumbers.length; i++) 
        {
            if (bonus[riskNumbers[i]] > highest) 
            {
                highest = bonus[riskNumbers[i]];
            }
        }    
        print(highest);
        total = total + highest;
    }
    return total;
}

module.exports = answer02

git push
