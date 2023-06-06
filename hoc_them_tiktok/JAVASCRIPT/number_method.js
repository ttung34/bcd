// toFixed lam tron den so thap phan thu
var a = 3.2567
var newNumber = a.toFixed();
console.log('============= newNumber',newNumber)

// toPrecision 
var a = 3.54325342
var newNumber = a.toPrecision(4);
console.log('============= newNumber',newNumber)

// toString chuyen doi so thanh chuoi
var a = 3.2567
var newNumber = a.toString();
console.log(a)
console.log('============= newNumber', typeof newNumber)

// number chuyen chuyen thanh so tuong ung
var a = Number("10.33")
console.log('============= a',a)


// parseInt bien doi chuoi day thanh mot so nguyen
// chap nhan khoang trang va lay so dau tien de xu ly
var a = parseInt('10  33')
console.log('============= a  ',a  )

// parseFloat chuyen vao mot chuoi de chuyen doi thanh mot 
// chap nhan khoang trang va lay gia tri dau tien de xu ly
var a = parseFloat("10")
console.log('============= a ',a )

// isNaN kiem tra xem du lieu co phai NaNl hay khong 
var check = isNaN(a)
console.log('============= check',check)

// Number.isInteger kiem tra gia tri nay co phai so nguyen kh
var check = Number.isInteger(10.19)
console.log('============= check',check)