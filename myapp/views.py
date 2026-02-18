from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

def contact_list(request):
    contact=contact.objects.all()
    return render(request,'myapp/contact_list.html',{'contact':contact})
     

def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Message Has Been Sent Successfully!')
            return redirect('contact')
    else:
        form=ContactForm()
    return render(request,'myapp/contact.html',{'form':form})
def index(request):
    return render(request, 'myapp/index.html')
def contact(request):
    return render(request, 'myapp/contact.html')
def product(request):
    return render(request, 'myapp/product.html')
def service(request):
    return render(request, 'myapp/service.html')
def team(request):
    return render(request, 'myapp/team.html')
def testimonial(request):
    return render(request, 'myapp/testimonial.html')
def about(request):
    return render(request, 'myapp/about.html')
def error(request):
    return render(request, 'myapp/error.html')
