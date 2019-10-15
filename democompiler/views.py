
from random import random
from django.shortcuts import render
import os,subprocess,time
from subprocess import STDOUT

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def submit(request):
    language = request.POST['language']
    code = request.POST['code']
    input = request.POST['input']
    seconds = 5.00
    with open('out.txt','w') as file:
        pass
    with open('in.txt','w') as file:
        file.write(input)
    with open('code.cpp','w') as file:
        file.write(code)

    check = subprocess.call('g++ code.cpp -o code.exe',shell=True)
    subprocess.call('g++ code.cpp 2> error.txt',shell=True)

    with open( 'error.txt', 'r' ) as file:
        run = file.read()

    if check == True:
        output = "Compilation Error"
        seconds = 0.0
    else:
        if run != "":
            output = "Runtime Error"
            seconds=0.0
        else:
           start_time = time.time()/10
           try:
            check = subprocess.run( 'code.exe < in.txt > out.txt',shell=True,stderr=STDOUT,timeout=5)
           except Exception:
               output="Time limit Error"
               os.system('taskkill /F /IM code.exe')
               os.system( 'del /f code.cpp' )
               os.system( 'del /f in.txt' )
               os.system( 'del /f out.txt' )
               os.system( 'del /f error.txt' )
               os.system( 'del /f code.exe' )
               return render( request, 'submit.html',
                              {'input': input, 'language': language, 'code': code, 'output': output, 'seconds': seconds} )

           end_time = time.time()/10
           seconds = (end_time - start_time);
           seconds=round(seconds,2)
           if check.returncode !=0 :
              output = "Runtime Error"
           else:
              with open('out.txt','r') as file:
                 output = file.read()
    os.system( 'del /f code.cpp' )
    os.system( 'del /f in.txt' )
    os.system( 'del /f out.txt' )
    os.system( 'del /f error.txt' )
    os.system( 'del /f code.exe' )

    return render( request, 'submit.html', {'input' : input,'language': language, 'code': code ,'output' :output,'seconds' : seconds } )

