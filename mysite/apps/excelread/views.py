from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
import json


# Create your views here.
# for user entry
""" @method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.has_perm('main.excelread'),login_url='permission_not_granted'), name='dispatch') """
class IndexView(View):
    template_name = "index.html"

    def get(self,request,*args,**kwargs):
       
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        if request.POST["action"] == "getcalculate":

            response_data = {}
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))
            opr = (request.POST.get("opr"))
            
            if opr == '+':
                result = num1+num2
            elif opr == '-':
                result = num1-num2
            elif opr == '/':
                result = num1/num2
            else:
                result = num1*num2
            print(result)
            data = [{'resul': result}]
    
            response_data = result

        return HttpResponse(json.dumps(response_data), content_type="application/json")



