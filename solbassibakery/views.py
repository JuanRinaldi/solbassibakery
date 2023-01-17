from django.shortcuts import render #importamos render para renderisar los html

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
