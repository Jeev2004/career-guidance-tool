from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,cs1,cs2,cs3,cs4,cs5,cs6,cs7,cs8,UserAnswer
from .forms import question
from .code import send,sendcs,get,cse,loop
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import logging
logger = logging.getLogger(__name__)
lst =[]
clst=[]
list1=[]
def loginpage(request):
    if request.method == 'POST':

        if request.POST.get("form_type") == "formOne":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1!= pass2:
                return HttpResponse("Your password is wrong")
            else:
                my_user = User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')

        if request.POST.get("form_type") == "formTwo":
            username = request.POST.get('username')
            pass1 = request.POST.get('password')
            user = authenticate(request,username=username,password=pass1 )
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                return HttpResponse("Username or Password is wrong")
    return render(request,'login.html')
def logoutpage(request):
    logout(request)
    return redirect('main')
def main(request):
    last_10_objects = UserAnswer.objects.order_by('-created_at')[:10]
    data_array = []

# Iterate through the QuerySet and append the desired attributes to the list
    for obj in last_10_objects:
        data_array.append(
        obj.answer_text,
        
        # Add more attributes as needed
    )
    print(data_array)
    f = loop(data_array)
    top = f 
    print(top) 
    
    a = top[0]
    b = top[1]
    c = top[2]
    d = top[3]
    e = top[4]
    list1.clear()
    list1.append(top[0])
    list1.append(top[1])
    list1.append(top[2])
    list1.append(top[3])
    list1.append(top[4])
    
    return render(request,'index.html',{'a':a,'b':b,'c':c,'d':d,'e':e})
    
def check(request):
    if request.method == 'POST':
        choice = request.POST.get('check')
        print(choice)
        if(choice == '1'):
            return redirect('q1')
        else:
            return redirect('c1')
    return render(request,'check.html')
def filter(request):
    if request.method == 'POST':
        choice = request.POST.get('check')
        print(choice)
        if(choice == '1'):
            return redirect('check')
        else:
            return redirect('checkschool')
    return render(request,'filter.html')
def checkschool(request):
    if request.method == 'POST':
        choice = request.POST.get('check')
        print(choice)
        if(choice == '1'):
            return redirect('check')
        else:
            return redirect('checkschool')
    return render(request,'checkschool.html')
def c1(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            data_base = form.cleaned_data['category']
            clst.append(data_base)
            a = cs1(data_base=data_base)
            a.save()
            return redirect('c2')
    form = question()
   
    return render(request,'c1.html',{'form':form})
def c2(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            c_architecture = form.cleaned_data['category']
            clst.append(c_architecture)
            a = cs2(c_architecture=c_architecture)
            a.save()
            return redirect('c3')
    form = question()
    return render(request,'c2.html',{'form':form})
    
def c3(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            cyber_security = form.cleaned_data['category']
            clst.append(cyber_security)
            a = cs3(cyber_security=cyber_security)
            a.save()
            return redirect('c4')
    form = question()
    return render(request,'c3.html',{'form':form})
def c4(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            networking = form.cleaned_data['category']
            clst.append(networking)
            a = cs4(networking=networking)
            a.save()
            return redirect('c5')
    form = question()
    return render(request,'c4.html',{'form':form})
def c5(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            software_development = form.cleaned_data['category']
            clst.append(software_development)
            a = cs5(software_development=software_development)
            a.save()
            return redirect('c6')
    form = question()
    return render(request,'c5.html',{'form':form})
def c6(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            ai_ml = form.cleaned_data['category']
            clst.append(ai_ml)
            a = cs6(ai_ml=ai_ml)
            a.save()
            return redirect('c7')
    form = question()
    return render(request,'c6.html',{'form':form})
def c7(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            graphics_designer = form.cleaned_data['category']
            clst.append(graphics_designer)
            a = cs7(graphics_designer=graphics_designer)
            a.save()
            return redirect('c8')
    form = question()
    return render(request,'c7.html',{'form':form})

def c8(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            data_science = form.cleaned_data['category']
            clst.append(data_science)
            a = cs8(data_science=data_science)
            a.save()
            print(clst)
            cs = sendcs(clst)
            clst.clear()
            print(clst)
            answers_with_usernames = [('admin',cs )]
            f =save_answers_with_usernames(answers_with_usernames)
            return render(request,'output.html',{'cs':cs,'f':f})
    form = question()
    return render(request,'c8.html',{'form':form})
    
def q1(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Circuit_Design = form.cleaned_data['category']
             #logger.error(c)
            lst.append(Circuit_Design)
            a = s1(Circuit_Design=Circuit_Design)
            a.save()
            return redirect('q2')
    form = question()
    return render(request,'q1.html',{'form':form})
    
def q2(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Control_Systems = form.cleaned_data['category']
            
            
            lst.append(Control_Systems)
            print(lst)
            a = s2(Control_Systems=Control_Systems)
            a.save()
            
            return redirect('q3')
    form = question()
    return render(request,'q2.html',{'form':form})
def q3(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Power_Electronics = form.cleaned_data['category']
            a = s3(Power_Electronics=Power_Electronics)
            lst.append(Power_Electronics)
            a.save()
            print(lst)
            return redirect('q4')
    form = question()
    return render(request,'q3.html',{'form':form})
def q4(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Analog_Communication = form.cleaned_data['category']
            lst.append(Analog_Communication)
            a = s4(Analog_Communication=Analog_Communication)
            a.save()
            return redirect('q5')
    form = question()
    return render(request,'q4.html',{'form':form})
def q5(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            R_F = form.cleaned_data['category']
            lst.append(R_F)
            a = s5(R_F=R_F)
            a.save()
            return redirect('q6')
    form = question()
    return render(request,'q5.html',{'form':form})
def q6(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            C_P_P = form.cleaned_data['category']
            lst.append(C_P_P)
            a = s6(C_P_P=C_P_P)
            a.save()
            return redirect('q7')
    form = question()
    return render(request,'q6.html',{'form':form})
def q7(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Electrical_System = form.cleaned_data['category']
            lst.append(Electrical_System)
            a = s7(Electrical_System=Electrical_System)
            a.save()
            return redirect('q8')
    form = question()
    return render(request,'q7.html',{'form':form})
def q8(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            C_A_D = form.cleaned_data['category']
            lst.append(C_A_D)
            a = s8(C_A_D=C_A_D)
            a.save()
            return redirect('q9')
    form = question()
    return render(request,'q8.html',{'form':form})
def q9(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            P_C_B = form.cleaned_data['category']
            lst.append(P_C_B)
            a = s9(P_C_B=P_C_B)
            a.save()
            return redirect('q10')
    form = question()
    return render(request,'q9.html',{'form':form})
def q10(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Lab_View = form.cleaned_data['category']
            lst.append(Lab_View)
            a = s10(Lab_View=Lab_View)
            a.save()
            print(lst)
            c = send(lst)
            lst.clear()
            context = {}
            context['c'] = c
            return render(request,'output.html',context)
            
    form = question()
    return render(request,'q10.html',{'form':form})
def output(request):
    if(request.GET.get('cs')):
        cs = int(request.GET.get('cs'))
        
        return render(request,'output.html',{'cs':cs})
    c = int(request.GET.get('c'))
    answers_with_usernames = [('admin',c )]
    save_answers_with_usernames(answers_with_usernames)
    return render(request,'output.html',{'c':c})
def map(request):
    data = request.GET.get('data')
    print("----")
    print(ml[0])
    a = ml[0]
    print(list1)
    if a in list1 :
        a = str(a)
        if int(data) not in list1:
            l=1
            return render(request,'map.html',{'data':data,'a':a,'l':l})
        return render(request,'map.html',{'data':data,'a':a})
    
    if data not in list1: 
        l=1
        return render(request,'map.html',{'data':data,'l':l})
    
def roles(request):
    return render(request,'roles.html')
def fieldC(request):
    return render(request,'fieldC.html')
def fieldE(request):
    return render(request,'fieldE.html')
def decision(request):
    d = request.GET.get('d')
    return render(request,'decision.html',{'d':d})
def process(request):
    a = request.GET.get('a')
    return render(request,'process.html',{'a':a})
def analyse(request):
    if (ext[0] == 0):
        print("ad")
        c = ext[0]
        a = ext[1]
        
        print("asdasd",a)
        
        answers_with_usernames = [('admin',a )]
        f =save_answers_with_usernames(answers_with_usernames)
        return render(request, 'analyse.html',{'c':c,'a':a,'f':f})
    else:
        print("ad")
        c = ext[0]
        a = ext[1]
        print("asdasd",a)
        answers_with_usernames = [('admin',a )]
        f =save_answers_with_usernames(answers_with_usernames)
        return render(request, 'analyse.html',{'c':c,'a':a,'f':f})

    #return render(request, 'analyse.html')

@csrf_exempt
def receive_history_data(request):
    if request.method == 'POST':
        try:
            history_data = json.loads(request.body.decode('utf-8'))
            ext.clear()
            a = get(history_data)  
            print(a)
            ext.append(a)
            a = cse(history_data)
            ext.append(a)
            print(ext)
            return redirect('analyse')
            
        except json.JSONDecodeError as e:
           
            return redirect('analyse')
    
    return render(request, 'extension.html')
ext = []

from .models import UserAnswer
from django.contrib.auth.models import User 
ml = []

def save_answers_with_usernames(answer_list):
    for username, answer_text in answer_list:
        try:
            user = User.objects.get(username=username)
            print(user)
            user_answers = UserAnswer.objects.filter(user__username=user)
            print("HELLO")
            for answer in user_answers:
                print(answer.answer_text)
            last_answer = UserAnswer.objects.filter(user=user).order_by('-created_at').first()
            if last_answer:
                print("________________")
                print(last_answer.answer_text)
                user_answer = UserAnswer(user=user, answer_text=answer_text)
                user_answer.save()
                a = " ".join(last_answer.answer_text)
                integer_value = int(a.strip('[] ').strip())
                ml.append(integer_value)
                print(a)  
                return last_answer.answer_text
            else:
                return "No answers found for this user."
        except User.DoesNotExist:
            print(f"User with username '{username}' does not exist.")



