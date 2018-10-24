from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from  django.urls import reverse_lazy

def actor_lista_view(request):
    lista = Actor.objects.all()
    if request.method=='GET':
        form = actor_form()
    if request.method=='POST':
        form = actor_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'ok':True}),content_type='application/json')
    return render(request,'actor.html',locals())

def listado_lista_view(request):
    lista = Listado.objects.all()
    return render(request,'listado.html',locals())

def cliente_lista_view(request):
    lista = Cliente.objects.all()
    mas_premiado = Cliente.objects.raw(''' 
        select * from
        cliente cl inner join (select al.`Cliente_id`'client',count(*) n_alquileres from
        `alquiler` al
        WHERE al.`Listado_id` = 2
        GROUP BY (al.`Cliente_id`))t_nuenva
        on (client=cl.`id`)
        Where cl.`id` = (select cliente_id  FROM
        (select al.`Cliente_id`'cliente_id',count(*) n_alquileres from
        `alquiler` al
        WHERE al.`Listado_id` = 2
        GROUP BY (al.`Cliente_id`))cuenta_premios
        Where n_alquileres =  (select max(n_alquileres) from
        (select al.`Cliente_id`'cliente',count(*) n_alquileres from
        `alquiler` al
        WHERE al.`Listado_id` = 2
        GROUP BY (al.`Cliente_id`)
        )cuenta_premios))
    ''')

    premiados = Cliente.objects.raw('''
        select *
        from `cliente` cl
        inner join (select al.`Cliente_id` client, count(al.`Listado_id`)cuenta_premios
        from `alquiler` al
        WHERE (al.`Listado_id`=(select lis.`id` from
        `listado` lis
        where lis.`tipo` = 'Premio'))
        GROUP BY al.`Cliente_id`)cuneta_premios
        on (cl.`id`=client);  
    ''')

    castigados = Cliente.objects.raw('''
        select *
        from `cliente` cl
        inner join (select al.`Cliente_id` client, count(al.`Listado_id`)cuenta_castigos
        from `alquiler` al
        WHERE (al.`Listado_id`=(select lis.`id` from
        `listado` lis
        where lis.`tipo` = 'Castigo'))
        GROUP BY al.`Cliente_id`)cuneta_premios
        on (cl.`id`=client);
    ''')
    return render(request,'cliente.html',locals())

def director_lista_view(request):
    lista = Director.objects.all()
    return render(request,'actor.html',locals())

def formato_lista_view(request):
    lista = Formato.objects.all()
    return render(request,'formato.html',locals())

def genero_lista_view(request):
    lista = Genero.objects.all()
    return render(request,'genero.html',locals())

def video_lista_view(request):
    #lista = Video.objects.all()

    lista = Video.objects.raw(''' 
        select videos.id,titulo,idioma,duracion,director,nacionalidad,formato,valor,veces
        from (
            select vi.`id`,vi.`titulo`,vi.`idioma`,vi.`duracion`,di.`nombre`'director',di.`nacionalidad`,fo.`nombre`'formato',fo.`valor`
            from `video` vi LEFT OUTER JOIN `director` di
            on (vi.`Director_id`=di.`id`)
            Inner JOIN formato fo
            ON (fo.`id` = vi.`Formato_id`)
        )videos
        LEFT OUTER JOIN (
            select al.`Video_id`'videio_id', count(al.`Video_id`)veces
            from `alquiler` al
            GROUP BY al.`Video_id`
        )conteo
        on(videos.id=conteo.videio_id);
    
    ''')


    lista3 = Video.objects.raw(''' 
        select vi.id,di.`nombre`'director',di.`nacionalidad`,vi.`titulo`,vi.`idioma`,vi.`duracion`,fo.`nombre`'format',fo.`valor`,veces
        from `video` vi LEFT OUTER JOIN `director` di
        on(vi.`Director_id`=di.`id`)
        LEFT OUTER JOIN (
            select al.`Video_id`'videio_id', count(al.`Video_id`)veces
            from `alquiler` al
            GROUP BY al.`Video_id`
        )conteo
        ON(conteo.videio_id=vi.`id`)
        inner join `formato`fo
        on(vi.`Director_id`=fo.`id`)


        WHERE (vi.`id` in (select Video_id
        from (select al.`Video_id`, count(al.`Video_id`)contador
        from `alquiler` al
        GROUP BY al.`Video_id`)t_nueva
        WHERE (contador>(select AVG(al.`Video_id`)promedio
        from `alquiler` al))));
    ''')

    return render(request,'video.html',locals())

def alquiler_lista_view(request):

    consulta = Alquiler.objects.raw(''' 
    SELECT * 
    FROM Video vi inner join Alquiler al 
    on (vi.id=al.video_id) inner join Cliente cl 
    on (cl.id = al.cliente_id) inner join Listado lis 
    on (lis.id = al.listado_id)
    ''')

    return render(request,'alquiler.html',locals())

def mas_premiada_view(request):
    return render(request,'mas_premiada.html',locals())

# Actor
# Listado
# Cliente
# Director
# Formato
# Genero
# Video
# Alquiler

def consulta_view(request):

    if request.method=='POST':
        f1 = request.POST.get('fecha1',None)
        f2 = request.POST.get('fecha2',None)

        if f1 and f2 and f1<f2:
            consulta = Director.objects.raw('''
            select *
            from `director` di
            WHERE id in (select director_id
            from (select vi.`Director_id`, count(*) veces
            from `alquiler` al inner join `video` vi
            on (al.`Video_id`=vi.`id`)
            where fecha_alquiler BETWEEN %s and %s
            GROUP BY vi.`Director_id`)contador
            where veces > (select AVG(veces) promedio
            from (select vi.`Director_id`, count(*) veces
            from `alquiler` al inner join `video` vi
            on (al.`Video_id`=vi.`id`)
            where fecha_alquiler BETWEEN %s and %s
            GROUP BY vi.`Director_id`)contador));
         ''',[f1,f2,f1,f2] )

    return render(request,'consulta.html',locals())


def eliminar_actor_view(request,pk):
    try:
        d = get_object_or_404(Actor,id=pk)
        d.delete()

        return redirect('/?ok')
    except:
        return redirect('/?err')

def agregar_actor_view(request):

    print('--------------------------------------------')
    print(data)

    return HttpResponse(json.dumps({'ok':True}),content_type='application/json')