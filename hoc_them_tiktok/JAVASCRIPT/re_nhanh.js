var number = prompt("Please enter a number: ")

// condition =>number < 0

if(number >1){
    //code => condition =>True
    console.log("True")
}else if(number == 0){
    console.log("so 0")
}else{
    console.log("False")
}




// Cau lenh SWITCH
var day = "monday"
switch(day){
    case "monday":
        console.log("Hom nay la thu 2");
        break;

    case "tuesday":
        console.log("Hom nay la thu 3");
        break;
    
    default:
        console.log("Hom nay khong phai thu 2 hoac thu 3");
}

// If else long nhau
var number = prompt("Nhap mot so vo: ")

if (number >0){
    if(number %2===0){
        console.log(number + " La so duong chan")
    }else{
        console.log(number + " La so duong le")
    }
}else{
    console.log(number + " La so am")
}



var number = 4
switch(number){
    case "4":
        console.log()
}


// Toan tu 3 ngoi
if (number>2){
    console.log("so lon hon 2")
}else{
    console.log("so nho hon 2")
}

var a = number>2 ? "so lon hon 2" : number==2 ? "so bang 2" : "so nho hon 2";
console.log('=========== a',a)

var number = prompt("Nhap so vo: ")
var a = number < 0 ? "so am" : number %2==0 ? "so duong chan" : "so duong le";
console.log('============= a',a);