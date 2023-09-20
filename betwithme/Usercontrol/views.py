from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from rest_framework import generics
from .serializer import UserSerializer



from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


'abc' -
a-b a-c

class Login(LoginView):
    template_name='login/index.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))



class UserCreateAPIView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		
		serializer=self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		
		token, created = Token.objects.get_or_create(user=serializer.instance)
		return Response({'token': token.key,'message':"User logged in successfully"}, status=status.HTTP_201_CREATED)



def permutation(string):
	if len(string)<2:
		return [string]

	permute=[]

	for x in range(len(string)):
		fix=string[x]
		rest=permutation(string[:x]+string[x+1:])
		for x in rest:
			permute.append(fix+x)

	return permute





