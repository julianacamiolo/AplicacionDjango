from django.shortcuts import render, HttpResponse, redirect
from miaply.models import Article
from django.db.models import Q
from miaply.forms import FormArticle
# Create your views here.

layout = """
<h1>Sitio web con Django | Juliana Camiolo</h1>
<hr/>
<ul>
    <li>
       <a href="/inicio"> Inicio</a>
    </li>  
    <li>
       <a href="/viaje-seguro">viaje seguro</a>
    </li> 
    <li>
       <a href="/pagina-web">pagina web</a>
    </li> 
    <li>
       <a href="/contacto">Contacto</a>
    </li> 
</ul> 
</hr>   
"""

def index(request):
   
    lenguajes = ['Python', 'Flask', 'Fastapi', 'Django']

    return render(request,'index.html',{
        'title': 'Inicio',
        'lenguajes': lenguajes
    })

def viaje_seguro(request):
    return render(request,'viaje_seguro.html')

def pagina_web(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio')

    return render(request, 'pagina_web.html')

def contacto(request, nombre= "", apellidos=""):
    html = ""

    if nombre and apellidos:
        html = "<p>El nombre completo es:</p>"
        html = f"<h3>{nombre} {apellidos}<h3>"
    
    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):
     
    if request.method == 'POST':

        title = request.POST['title']

        if len(title) <= 5:
            return HttpResponse("formulario aqui")
        
        content = request.POST['content']
        public = request.POST['public']


        articulo = Article(
            title = title,
            content = content,
            public = public
    )

        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")



    

def create_article(request):
    return render(request,'create_article.html')

def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid(title,public,content):
            data_form = formulario.cleaned_data

            title= data_form.get('title')
            public = data_form['content']
            content = data_form['public']

            articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return redirect('articulos')
            
        #return HttpResponse(articulo.title + '' + articulo.content +''+ str(articulo.public))
    else:    
        formulario = FormArticle()

    return render(request, 'create_full_article.html',{
        'form': formulario
    })


def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse (response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = " Pelicula del 2017"
    articulo.public = True

    articulo.save()


    return HttpResponse(f"Articulo {articulo.id} editado: <strong> {articulo.title}</strong> - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all()
    articulos = Article.objects.filter(title= "Batman")
    articulos = Article.objects.all()

    
    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete(request)

    return redirect('articulos')
    