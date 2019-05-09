from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def ability(request):
    return render(request, 'personal/ability.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['필요한게 있으시다면 다음의 이메일과 전화번호로 연락해주세요.','gentacle00@gmail.com', '010 5806 5513']})
