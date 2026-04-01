document.getElementById("check").onclick = function(){
    const test = document.getElementById("num").value;
    //console.log("test = "+test);

    if (test == ''){
        console.log("숫자를 입력해주세요");
        document.getElementById("print").textContent = '값을 입력하셈';
        return;
    }

    if(test<3){
        console.log(test + "은 3보다 작다");
    } else if(test==3){
        console.log(test + "은 3과 같다");
    } else {
        console.log(test + "은 3보다 크다");
    }
}   