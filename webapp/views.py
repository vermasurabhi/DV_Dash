from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GraphData
from .serializers import graphDataSerializer
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
## for login and logout messages
from django.contrib import messages
from .forms import SignUpForm

from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = "main.html"

def main(request):
    return render(request, 'main.html', {})

def map(request):
    return render(request, 'mapping.html', {})


def datechart(request):
    return render(request, 'datechart.html', {})

def experiment(request):
    return render(request, 'experiment.html', {})

def home(request):
    # check to see if logging in
    if request.method=="POST":
        username = request.POST['username'] #username inside the POST is the name inside the input tag of home.html
        password = request.POST['password'] #password inside the POST is the name inside the input tag of home.html
        # Authenticate
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an error Loggin In, Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def register_user(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()  #we are not posting the request here this else is just for the displaying of registration form which will definetely take the SignUpForm class for the registration form style displaying
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out...")
    return redirect('home')




def register_user(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()  #we are not posting the request here this else is just for the displaying of registration form which will definetely take the SignUpForm class for the registration form style displaying
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

class dataVisual(APIView):
    def post(self, request):
        serializer=graphDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        result=GraphData.objects.all()
        serializers=graphDataSerializer(result, many=True)
        return Response({'status':'success','students':serializers.data}, status=200)
    
    def delete(self, request, id=None):
        result=get_object_or_404(GraphData,id=id)
        result.delete()
        return Response({"status": "success","data":"Record Deleted"})