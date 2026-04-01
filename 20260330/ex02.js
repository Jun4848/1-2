const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
//함수 선언 옛날 방법
//function aa(){}
//최근
//const  = () => {}

rl.question('숫자 입력 : ', (data) =>{
    let num = 1
    for (;num <= 9;num = num + 1){
        console.log(`${data} * ${num} = ${data * num} `);
        rl.close();
    }
})