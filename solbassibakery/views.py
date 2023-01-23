from django.shortcuts import render #importamos render para renderisar los html
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    return render(request,'index.html', {
        'saludo': "hola a todxs! Bienvenidos a SOL BASSI BAKERY",
        'consulta': 'En que podemos ayudarte?',
        'encabezado': 'Listado de productos',
        'titulo': 'Productos',
        'products': [
            {'titulo':'pepas' , 'precio':1000 , 'stock': True },
            {'titulo':'cookies' , 'precio': 1000 , 'stock':True },
            {'titulo': 'budin' , 'precio': 800 , 'stock':False },
            {'titulo': 'granola' , 'precio':1200 , 'stock': True },
            {'titulo': 'tortas' , 'precio':5000 , 'stock':False }
        ]
    } )


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password = password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, "usuario o contraseña no validos")
    return render(request, 'login.html', {

})

def logout_view(request):
    logout(request)
    messages.success(request, "sesion cerrada con exito")
    return redirect('login')

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {
        'form': form
    })
