### Variable
```JavaScript
var fillName // lawas
let fillName 
const fillName // constant : gabisa diubah2
```
  
### Console Method
```JavaScript
console.info()
console.warn()
console.error()
console.table()
```
### Formatting
```JavaScript
const name = "Ichsan";
console.log("Name : ${name}");
// dengan condition
console.log("Name : ${name == 'san'}");
const multiline = `sdsd
sdsd
sdsd
sdsd
`;
```
  
### Konversi
```JavaScript
parseInt("1")
parseFloat("1")
Number("2")
number.toString(1)

// NaN
isNaN()
```
  
### Object
```JavaScript
const person = {};
person["nama"] = "Ichsan";
person["nama2"] = "Ha";
delete person["nama2"];
const person {
	firs
	last
	get fullName() {return first + last};
	set fullName();
};
```
  
### Alert, Confirm,
  
### Undefined, Null
Undefined variabel belum terdefinisi
Null data kosong
```JavaScript
let nama;
if (nama == undefined) {
	// ini true
} else if (nama == null) {
	//ini false
}

// typeof 
typeof
// in hanya ngecek property
in 
// Nullish coalescing
data = parameter ?? "Nilai default"
// optional chaining
let country = person?.address?.country
```
  
### Looping
```JavaScript
// label
loopi:
for (let i = 0; i < 100; i++) {
	loopj:
	for (let j = 0; j < 10; j++ {
		if (j >10) {
			continue loopi;
		}
	}
}
// for in
for (const property in person) {
}
// for of
```
  
### With Statement
```JavaScript
// person is object with properties
with (person) {
	console.log(firstName);
}
```
### Function
```JavaScript
// Rest Parameter
function halo(nama, ...namaLain) {
	
}
let array = []; 
halo("isan", ...array);
// Anonymous Function
let fun = function (name) {
} // as variabel

```
### Function Generator
function*
  
### Arrow Function
```JavaScript
var a = (halo) => {
	return halo;
}
```