from django.shortcuts import render

# Create your views here.
def view1(request):
    myName="Kishan"
    favPlayer="Cristiano"
    favAnimal="Leopard"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'subject':favSubject,'animal':favAnimal}
    return render(request,'staticApp1/1.html',d)