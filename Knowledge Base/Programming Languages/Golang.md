# **Tipe Data**
## **Integer**
int8 16 32 64  
uint8  
float32 64  
complex64 128  
### **Alias**
byte : untuk uint8  
rune : int32  
int : int32  
uint : uint32  
## **Boolean**
true false
## **String**
len("string")
  
### Arary & Map
[]int {}
map[string]int
# Condition
```Go
var name = "A"
if name == "A" {
	fmt.Println("Hello A")
} else if {
} else {
}
```
  
# Loop
```Go
for conter := 1; counter <= 10; counter ++ {
	// statement
}

slice := []string{"aaaa"}
for index, name := range slice {
	// statement
}
```
  
# Function
```Go
func halo(name string) string {
	return "halo " + name
}
// multiple return
func getFullName() (string, string) {
	return "halo", "hola"
}
firstNmae, _ := getFullName()

	/**
	Variadic Function
	
	*/
func halo(name ...int) string {
	var total int
	for _, v := range name {
		total += v
	}
}
slice := []int{1,2,3,4}
halo(slice...)
// param or return any datatype
interface{}
```
  
# Defer, Panic, Recover
```Go
// manggil fungsi yang lain
defer function()
// mirip throw
panic 
// catch
recover
```
  
# Struct
```Go
type Customer struct {
	Name, NPM string
	Address string
	Age int
}
joko := Customer {
	Name := sss///sd//asd//asd/sad/a/sd
}

func (customer Customer) sayHi(name string) {
	
}
```
  
# Interface
```Go
type Animal interface {
	getID() string
}
nil
// Error
import "errors"
func Pembagi(nilai int, pembagi int) (int, error) {
	if pembagi == 0 {
		return 0, errors.New("gaboleh")
	} else {
		result := nilai / pembagi
		return result, nil
	}
}
```
  
# Type Assertions
```Go
var angka int = 1
var resultString string = angka.(int32)
```
  
# Pointer
- Golang defaultnya pass by value
- Pointer bisa buat data jadi pass by reference di golang
```Go
address1 := Address("Cimahi", "Jawabarat")
address2 := address1 // pass by value
address2 := &address1 // pass by reference
*address2 := address_baru // jadi berubah semua di memorynya
```
  
# GOPATH
src/golang/
  
func init() {}
  
import package tapi ga dipake : _
  
# Access Modifier
```Go
namaFunction() // mirip protect
NamaFunction() // mirip public
```
  
# Package
## os
```Go
import "os"
os.Args
os.Getenv
```
## flag
```Go
import "flag"
var host *string := flag.String("host", "localhost", "Put your database here")
flag.Parse()
// go run file.go -host="localhost2"
```
## strings and strconv
```Go
import "strings"
strings.Trim(string, cutset)
strings.ToLower(string)
strings.ToUpper(string)
strings.Split(string, separator)
strings.Contains(string, search)
strings.ReplaceAll(string, from, to)

import "strconv"
parseBool
parseFloat
parseInt
// to string
FormatBool
FormatFloat
FormatInt
Atoi
Itoa
```
## Math
```Go
import "math"
Round
Floor
Ceil
Max
Min
```
## List
```Go
import "container/list"
// linked list
list.New()
```
## Container/ring
```Go
import "container/ring"
//circular linked list
ring.New(5)
```
## Sort
```Go
 
Len
Less
Swap
```
## Time
```Go
impoer "time"
time.Now()
time.Date()
time.Parse(layout, string)
```
  
```Go
"reflect"
"regexp"
```
  
## Other Sources
### CRUD

> [!info] Generate CRUD Golang code from SQL | Compare db/sql, gorm, sqlx, sqlc  
> Welcome back to the backend master class!  
> [https://dev.to/techschoolguru/generate-crud-golang-code-from-sql-and-compare-db-sql-gorm-sqlx-sqlc-560j](https://dev.to/techschoolguru/generate-crud-golang-code-from-sql-and-compare-db-sql-gorm-sqlx-sqlc-560j)