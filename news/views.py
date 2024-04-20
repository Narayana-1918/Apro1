from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def sports(request,id):
    if id==1:
        return render(request,'s1.html')
    elif id==2:
        return render(request,'s2.html')
    elif id==3:
        return render(request,'s3.html')
    return render(request,'sports.html')
def politics(request,id):
    if id==1:
        return render(request,'p1.html')
    elif id==2:
        return render(request,'p2.html')
    elif id==3:
        return render(request,'p3.html')
    return render(request,'politics.html')
def cinema(request,id):
    if id==1:
        return render(request,'c1.html')
    elif id==2:
        return render(request,'c2.html')
    elif id==3:
        return render(request,'c3.html')
    return render(request,'cinema.html')