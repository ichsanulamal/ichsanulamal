---
Created: 2021-07-01T07:59
tags:
  - Software-Engineering
Last edited time: 2024-01-07T00:11
---
  
```Python
python -m venv .env
venv .env
1. activate virtual environment
**start project
		django-admin startproject [name]
**run app
		python manage.py runserver
**create superuser
		python manage.py createsuperuser
**buat app
		- python manage.py startapp [nama]
		- tambahin app di setting 
		## Edit app di model
		- python manage.py makemigrations
		- python manage.py migrate
	di admin:
		from .models import [class yang dibuat di model]
		admin.site.register([class yang dibuat di model])
**Edit model
		buat class inherit models.model
**buat object di shell
		python manage.py shell
		from [nama app].models import [class yang dibuat di model]
		[class yang dibuat di model].objects.create(fieldnya apa aja yg di class)		
		
		[class yang dibuat di model].objects.all() \#nampilin semua objek di model 
**Nampilin di view
	ada template html di templates. bisa diedit directorynya di setting templates
	go to views.py	
		def homebebas(request):
			return render(request, "nama.html", {})
	go to urls.py
		from [nama app].views import fungsi atau class di view	
		masukkin ke urlpatterns
			path("urlnya dr host", fungsi/class, name="bebas")
**Edit html
	di base html buat block content yang bakal diubah2 di template yg lain
		{% block content %}
		{% endblock %}
		{% include "file_html_yang_static.html" %}
	di template lain 
		{% extends "namabase.html %}
		
		{% block content %}
			Isi yang mau diganti disini
		{% endblock %}
**render context
	**biasa
	go to views, isi fungsi pake dictionary, render(request, html, dictionary)
		contoh
		dictionary = {mylist:1,2,3}
	go to html
		^^looping:
		<ul>
		{% for item in mylist %} # {%forloop.counter %} nampilin angka loop
			<li> {{ item }} </li>
		{% endfor %}
		</ul>
		^^if statement:
		<ul>
		{% for item in mylist %} # {%forloop.counter %} nampilin angka loop
			{% if item == 123 %}
				<li> {{ item|add:22 }} </li>
			{% endif %}
		{% endfor %}
		</ul>
	***pake model
		go to views
			from app.models import class atau fungsi [nama]
			di fungsi: 
				object = [nama].objects.all()
				context = {"title" : object.title,
					   "post" : object.post}
				return render(request, html, context}
		go to html
			di loop 
			{{ title }}
			{{ post }}
form 
	from .models import kelas
	kalo udah buat model, contoh:
	class ProductForm(forms.ModelForm):
		class Meta:
			model = kelas
			fields = { apaaja yg di model }
	
	go to views
		from .forms import ProductForm
	def prodysdfsdyfb(request):
		form = ProductForm(request.POST or None)
		if form.is_valid():
			form.save()
		context = { 'form': form }
		
		return render(request, "products.html", context)
	go to html
	<form
		{{ form.as_p }}
		<input type='submit' value='Save' />

	<form
	go to url 
		import views
		make path
		
cara lain form
	go to html
	go to views
	def prodysdfsdyfb(request):
		if request.method == "POST":
			title = request.POST.get("title")
			Product.objects.create(title) # udah direquest trs buat objek diclass
		
		return render(request, "products.html", context)
	# html action='' 
		input -> placeholder="Your search"
pure model from django
	go to forms
	class raw(forms.Form):
** Form Validation method
** Dynamic URL rooting
	
	2:51:43
	go to views 
		from django.shortcuts import get_object_or_404 \#Buat handle doesnt exist
		def fungsi(request, my_id):
			obj = get_object_or_404(Class, id=id)
	go to urls
		path("dsf/<int/slug/str:my_id>
**DetailView 3:10
** Handle doesnt exist
** Views listView dsb 3:13	
python manage.py migrate --run-syncdb
python manage.py migrate --fake appname	

3:00:
'''
\#from selenium import webdriver
\#from selenium.webdriver.common.keys import Keys 
\#from selenium.webdriver.chrome.options import Options 
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(Story7_Functional_Test, self).setUp()
    def tearDown(self):
        self.selenium.quit()
        super(Story7_Functional_Test, self).tearDown()
 
 
    def test_change_theme_header(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/story-6/')
        time.sleep(5);
        css = selenium.find_element_by_tag_name('header')
        background1 = css.value_of_css_property('background')
        button = selenium.find_element_by_id('theme')
        button.click()
        background2 = css.value_of_css_property('background')
        self.assertNotEqual(background1, background2)
    def test_change_theme_background(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/story-6/')
        time.sleep(5);
        button = selenium.find_element_by_id('theme')
        button.click()
        css = selenium.find_element_by_tag_name('body')
        background = css.value_of_css_property('background-color')
        self.assertEqual(background, 'rgba(20, 38, 52, 1)')
    def test_accordion(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/story-7')
        time.sleep(5);
        accs = selenium.find_element_by_class_name('accordion')
        panel = selenium.find_element_by_class_name('panel')
        disp = panel.value_of_css_property('display')
        self.assertEqual(disp, 'none')
        accs.click()
        disp = panel.value_of_css_property('display')
        self.assertEqual(disp, 'block')
  
'''
coverage run --source='./cerita9/' manage.py test cerita9	
coverage report -m
coverage run --source='./Kantor/' manage.py test Kantor
coverage report -m
coverage run --source="Jobseeker,Kantor,Perawat,RumahSakit,VolunteerNonPerawat" --omit="VolunteerNonPerawat/migrations/*,VolunteerNonPerawat/__init__.py,VolunteerNonPerawat/admin.py,Jobseeker/migrations/*,Jobseeker/__init__.py,Jobseeker/admin.py,Kantor/migrations/*,Kantor/__init__.py,Kantor/admin.py,RumahSakit/migrations/*,RumahSakit/__init__.py,RumahSakit/admin.py,Perawat/migrations/*,Perawat/__init__.py,Perawat/admin.py" manage.py test

''''
Backup
pg_dump ...other...options... -Fc -n B >dump.dmp
Restore the dump file:
pg_restore -d somedb dump.dmp
```