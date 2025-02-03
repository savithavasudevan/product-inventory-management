from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from product.forms import Productform

from product.models import Productmodel


class ProductView(View):

    def get(self,request):

        form=Productform

        return render(request,'productadd.html',{'form':form})
    
    def post(self,request):

        form=Productform(request.POST)

        if form.is_valid():

            Productmodel.objects.create(**form.cleaned_data)

            form=Productform

            return render(request,'productadd.html',{'form':form})
        
class Productall(View):

    def get(self,request):

        form=Productform

        data=Productmodel.objects.all()

        return render(request,'allproduct.html',{'data':data})
    

class Productupdate(View):

    def get(self,request,**kwargs):
        
        id=kwargs.get("pk")

        data=Productmodel.objects.get(id=id)

        form=Productform(instance=data)

        return render(request,'productupdate.html',{'form':form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")

        data=Productmodel.objects.get(id=id)

        form=Productform(request.POST,instance=data)

        if form.is_valid():

            form.save()

        return render(request,'productupdate.html',{'form':form})
    
class Productdelete(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        Productmodel.objects.get(id=id).delete()

        return render(request,'productdelete.html')








 

    

