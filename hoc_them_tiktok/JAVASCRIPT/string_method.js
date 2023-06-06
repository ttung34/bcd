// length dem do dai cua chuooi
var string = "thao nguyen"

var stringlength = string.length

console.log(stringlength) 


// indexOf tim kiem mot chuoi con trong mot chuoi cha va tra ve thwu tu cua no

// neu khong tim thay ta se tra ve la am mot
var string = "thao nguyen"

var index = string.indexOf("a")

console.log(index) 

// slice duoc su dung de trich xuat cua mot chuoi ra va 
// tra ve mot chuoi moi nhung khogn thay doi chuoi goc chi tra ve chuoi moi

var string = "thao nguyen"

var index = string.slice(2,6)

console.log(index) 


// replace tim kiem va thay the mot chuoi con va thay the bang mot chuoi moi nhung khong thay doi chuoi goc 

// Chi thay ket qua dung dau tien cua chuoi neu chuoi co 2 gia tri giong nhau

var string = "thao nguyen"

var index = string.replace("thao", "pham")

console.log(index) 

// toUpperCase viet hoa gia tri chuoi
var string = "thao nguyen"

var index = string.indexOf("a")

console.log(index) 

// concat tra ve chuoi da duoc noi voi nhau
var str1 = "Hello"
var str2 = "world"
var str3 = "1"
var result=str1.concat(str2, str3)
console.log(result)

// 
var string = "thao nguyen"

var index = string.split()

console.log(index) 

// chartAt tra ve gia tri cua mot chuoi day tai mot bi tri minh truyen vao
// neu gia tri truyen vao vuot qua chuoi thi tra vef chuoi rong 
var string = "thao nguyen"

var index = string.charAt(3)

console.log(index) 

// include tra ve gia tri do co ton tai trong chuoi do khong

var string = "thao nguyen"

var index = string.includes("a", 6)

console.log(index) 