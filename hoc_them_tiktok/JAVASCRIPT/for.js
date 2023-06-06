// // // Vong lap for
// for (var i =1; i<=10; i+=3){
//     console.log(i);
// }

// // // Vong lap while 
// // // Bat nguoi dung nhap lai den khi nao dung thi chuong trinh moi duoc chay
// var value =  prompt("Moi ban nhao mat khau")


// while (value != "123") {
//     var value = prompt("Moi ban nhao mat khau vo: ");

// }

// alert("Dang nhap thanh cong")


// // // Vong lap do while
// var i = 0;
// while(i<=10){
//     console.log(i);
//     i++;
// }

// do{
//     console.log(i);
//     i++;
// }while(i<=5);



// // // for
// for (var i = 1; i<=10; i+=1){
//     console.log(i);
// }

// // while
// var i = 0;
// while(i<=10){
//     console.log(i);
//     i+=1;
// }

// // do while
// do{
//     console.log(i);
//     i+=1;
// }while(i<=5)



// // // Tinh dien tich hinh chu nhat
// var a =5 ; b = 10;
// sum = a*b;
// console.log(sum)

// // Viet chuong tirnh kiem tra 1 so co phai la so chan hay khong
// var input = prompt("Nhap so can nhap");
// while(input%2==0){
//     // var input = prompt("Nhap so vo day: ")
//     alert("Day la so le :( ")
// }
// alert("Do la so chan :)")

// // // BT3
// for (var i = 1; i<=10;i++){
//     console.log(i);
// }

// // BT4
// // while
// var i = 1;
// while(i<=10){
//     console.log(i);
//     i+=1;
// }

// // do while
// do{
//     console.log(i);
//     i+=1;
// }while(i<=9)


// // // BT5

// var value =  prompt("Moi ban nhap mat khau")


// for (let i = 1; i<=value; i++){
//     var value = prompt("Nhap so value vo: ")
//     console.log(i)
// }

// var value =  prompt("Moi ban nhap mat khau")
// let i = 1;
// while(i<=value){
    
//     console.log(i)
//     i++
// }


// var value =  prompt("Moi ban nhap mat khau")
// do{
//     console.log(i)
//     i++
// }while(i<value-1)


// // BT6
// var value = prompt("Nhap so value vo: ")
// let sum =0 
// for (let i = 1; i<=value; i++){
//     sum +=i
//     // var value = prompt("Nhap so value vo: ")
// console.log(sum)
// }

var number  = prompt("Nhap so vo: ")

while(number%2!==0){
    console.log(number + "La so le");
    break;
}

while(number%2===0){
    console.log(number + "La so chan")
    break;
}
