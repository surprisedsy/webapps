from django.shortcuts import render

# Create your views here.
# 함수 만드는 곳

def hello(request):
    # model(CRUD)
    return render(request, 'helloweb/hello.html')

def tags(request):
    return render(request, 'helloweb/tags.html')

def join(request):
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    byear = request.POST['birth-year']
    hobbies = request.POST.getlist('hobby')         # 리스트 일때는 getlist를 꼭 붙여준다.
    selfintro = request.POST['self-intro']

    data = {
        "email_value":email,
        "password_value":password,
        "gender_value":gender,
        "byear_value":byear,
        "hobby_values":hobbies,
        "selfintro_value":selfintro,
    }

    return render(request, 'helloweb/join_result.html', data)