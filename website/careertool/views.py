from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10
from .forms import question
from .code import printf

def login(request):
    return render(request,'login.html')
def main(request):
    return render(request,'main.html')
def q1(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Circuit_Design = form.cleaned_data['category']
            print(Circuit_Design)
            printf(Circuit_Design)
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
            a.save()
            return redirect('q4')
    form = question()
    return render(request,'q3.html',{'form':form})
def q4(request):
    if request.method == 'POST':
        form = question(request.POST)
        if form.is_valid():
            Analog_Communication = form.cleaned_data['category']
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
            a = s10(Lab_View=Lab_View)
            a.save()
            return redirect('output')
    form = question()
    return render(request,'q10.html',{'form':form})
def output(request):
    return render(request,'output.html')



