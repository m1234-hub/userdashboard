from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'register.html')


def post(self,request):
    data=request.POST  

    print(data)

    return render(request, 'register.html', contexr={'data':data}) 