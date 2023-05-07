from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from core.models import Formulario
from core.forms import FormularioForm

def add_formulario(request):
    submitted = False
    if request.method == 'POST':
        form=FormularioForm(request.POST)
        if form.is_valid():
            form.save(form)
            return HttpResponseRedirect('/add_formulario?submitted=True')
    else:
        form=FormularioForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render (request, 'add_formulario.html', { 'form':form, 'submitted': submitted })

def formulario_busqueda(request):
    return render (request,'formulario_busqueda.html',{})
  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')

def index(request): 
    return render(request, 'IndexView')
   
def signout(request):
    logout(request)
    return redirect('/')

# Create your views here.

class IndexView(TemplateView):
    model = Formulario
    template_name = 'index.html'
    

    
    
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tittle'] = 'Formularios'
        context['listaFormulario'] = Formulario.objects.all()
        
   
        
        return context