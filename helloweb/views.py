from django.shortcuts import render

# Create your views here.
# 함수 만드는 곳

def hello(request):
    # model(CRUD)
    return render(request, 'helloweb/hello.html')

def tags(request):
    return render(request, 'helloweb/tags.html')