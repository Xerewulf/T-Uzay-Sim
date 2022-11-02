from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    template_name = "index.html"
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)


    def POST(self,request,*args,**kwargs):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return render(request,"index.html")
        c=''
        try:
            if request.method == "POST":
                n1 = eval(request.POST.get("num1"))
                n2 = eval(request.POST.get("num2"))
                opr = request.POST.get("opr")

                if opr == "+":
                    res=n1+n2
                elif opr == "-":
                    res=n1-n2
                elif opr == "*":
                    res=n1*n2
                elif opr == "/":
                    res=n1/n2 

            c=res
            print(c)
        except:
            print("hatali secim")
        


        return render(request, self.template_name, {"c":c})



