const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
rl.question;('입력하세요\n', function(ans){
    console.log(ans);
    if (60<= ans, ans <= 100){
        console.log("합격")
    }else{
        console.log("불합격")
    }
    rl.close();
});