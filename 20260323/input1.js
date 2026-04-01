const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
rl.question('입력하세요\n', function(ans){
    console.log(ans);
    //나누엇을때 0이면 짝수ㅜ
    if (ans%2 == 0){
        console.log("짝수")
    }else{
        console.log("홀수")
    }
    rl.close();
});