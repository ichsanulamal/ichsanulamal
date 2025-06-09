---
Created: 2021-06-29T21:28
tags:
  - Java
Last edited time: 2025-05-11T09:47
---
- Polymorphism: Berbagai macam bentuk, dengan nama sama namun bentuknya beda
- Dynamic binding : JVM nyari implementasi yang sesuai sesuai konteks secara dinamis
- Generic programming: method dapat dipakai secara umum untuk argumen objek berbeda
- Interface  
    semua datafield pasti : public final static  
    semua method pasti : public abstract  
    
- autoboxing: dari primitive jadi class
- unboxing: dari class jadi primitive
## form thymeleaf
  
form
```HTML
<form action='#' th:action="@{/tambahcoffe}" th:object="${coffee}" method="POST">
<input type="text" th:field="*{name}"
<input type="submit" value="submit form"/>
```
result.html
```HTML
<p th:text="'nama kopi :' + ${coffee.name}" />
<a href="/createcoffe lagi">Buat lagi </a>
```
  
```Java
// maincontroller
@GetMapping(/tambahcoffe)
public String coffeForm(Model model) {
model.addAttribute("coffee", new Coffee());
return "coffee";
}
@PostMapping(/tambahcoffe)
public String coffeesubmit(@ModelAttribute Coffee coffee) {
return "result"
}
```
```Java
// loop
<tr th:each="writer : ${writers}">
<td th:if="${writer.name == "appo}"> th:text="${writer.name}"/</td>	
</tr>
conditional
<tbody>
	<tr th:if="${coffeebeans.empty}">
		<td colspan="3"> No Coffee Beans Available </td>
	</tr>
	<tr th:each="bean : ${coffeebeans}">
		<td><span th:text="${bean.name}"></span></td>
		<td><span th:text="${bean.caffeineLevel}"></span></td>
		<td><span th:text="${\#strings.listJoin(bean.plantations, ', ')}"></span></td>
	</tr>
	</tbody>
```
[Part 6 - Java Programming](https://java-programming.mooc.fi/part-6)
# JavaFX
[[javafx]]