// // Bai 1
// var number = prompt("Nhap mot so vo day: ")

// if (number %3 ===0){
//     console.log("So nay chia het cho 3")
// }else{
//     console.log("so nay khong chia het cho 3")
// }


// // Bai 2
// var number = prompt("Nhap mot so vo day: ")

// if (number %3 ===0){
//     console.log("So nay la so chan")
// }else{
//     console.log("so nay la so le")
// }

// // Bai 3
// var number = prompt("Nhap vao mot so tai day")
// var a = number >0 ? "So nay la so duong":"So nay la so am";
// console.log('============= a',a)

// // Bai 4
// var number = prompt("Nhap mot so vao day")
// var
// // bai 6
// var number =prompt("nhap diem trung binh cua hoc sinh: ")
// if(number>=8.0){
//     console.log("Hoc sinh nay la hoc sinh gioi")
// }else if(6.5<=number<8.0){
//     console.log("Hoc sinh nay la hoc sinh kha")
// }else if(5.0<=number<6.0){
//     console.log("Hoc sinh nay la hoc sinh trung binh")
// }else{
//     console.log("Hoc sinh nay la hoc sinh yeu")
// }

// // Bai tap 5
// var number = prompt("Nhap so ban can kiem tra vo day")
// var a = 0<= number<=100 ? "so nay nam trong khoang tu 0 den 100":"Sonay nam ngoai khaong tu 0 den 100"
// console.log('============= a',a)

// var number = prompt("Nhap so can tim vo day")
// // var value = number % 2 ===0
// switch(number%3){
//     case 0:
//         console.log("So nay la so chan");
//         break;
//     default:
//         console.log("So nay la so le");
// }

// // Bai4
// var  number  = prompt("nhap mot so vao day")
// var mang = []
// for (var i = 1; i <=3; i+=1){
//     if (number % i ===0){
//             mang.push(i)
//         if(mang.length>2){
//             console.log("Day khong phai so nguyen to")
//         }else{
//             console.log("Day la so nguyen to")
//         }
//     }
// }

// // Bai4
var number = prompt("nhap so can tim")
// for (var i=2; i<= number-1; i+=1){
//     if (number>1){
//         if(number%i==0){
//             console.log("Day khong phai so nguyen to")
//         }else{
//             console.log("Day la so nguyen to")
//         }
//     }
// }


var isPrime = true;

for (var i=2;i<number;i+=1){
    if(number%i==0){
        var isPrime=false;
        break
    }
}

if(isPrime){
    console.log(number + " "+"la so nguyen to")
}else{
    console.log(number+" "+"Khong phai la so nguyen to")
}
    