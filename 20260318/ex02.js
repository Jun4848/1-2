//값의 변경이 불가능 한데
//원시형 자료형타입은 변경이 불가능 한데
//오브젝트형 자료형 타입은 변경이 가능하다
//오브젝트형 자료형 타입은 

const person = {
    "name":"홍길동", 
    hi:function(){
        console.log("안녕하세요");}
    };
person.name = "김철수";
console.log(person.name);
// console.log(person.hi);
person.hi();