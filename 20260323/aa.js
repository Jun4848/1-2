console.log("실행")
module.exports = {
    a : 10,
    b : 10,
    c : function(qq, ww){
        console.log("qq = " + qq)
        console.log("ww = " + ww)
        console.log("c 함수");
        return{
            dd: qq, ee: ww
        }
    }
}