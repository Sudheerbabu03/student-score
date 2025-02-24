from django.shortcuts import render # type: ignore

# Create your views here.
def home(request):
    return render(request,'index.html')
def grade(request):
    python=request.POST.get('p-marks')
    sql=request.POST.get('s-marks')
    django=request.POST.get('d-marks')
    result=''
    if request.method=='POST':
        op=request.POST.get('operation')
        if python is None or sql is None or django is None:
            result='Kindly enter your marks'
        try:
            if op=='Total':
                result=int(python)+int(sql)+int(django)
            elif op=='Percentage':
                result=((int(python)+int(sql)+int(django))/300)*100
            elif op=='Grade':
                result=((int(python)+int(sql)+int(django))/300)*100
                if result>=80:
                    result='A'
                elif result>=60  and result<80:
                    result='B'
                elif result>=40 and result<60:
                    result='C'
                else:
                    result='D'          
            elif op=='Status':
                result=int(python)+int(sql)+int(django)
                if result>=35:
                    result='PASS'
                else:
                    result='FAIL'
        except Exception:('provide marks kindly')            
    return render(request,'index.html',{'result':result})            

                




