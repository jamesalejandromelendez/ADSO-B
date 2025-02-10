from django.shortcuts import render, redirect
from boards.forms import *
from boards.models import *
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
     return render(request,'base2.html')

#Crud Usuarios
@never_cache
@login_required
def crud_usuario(request):
    usuarios = Usuarios.objects.all()
    return render(request,'Usuarios/show_usuario.html', {'usuarios':usuarios})

@never_cache
@login_required
def addnew_usuario(request):
    tipos_usuarios = TipoUsuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return redirect('/crud_usuario')
            except:
                pass
    else:
        form = UsuarioForm()
    return render(request, 'Usuarios/index.html', {'form': form, 'tipos_usuarios': tipos_usuarios})

@never_cache
@login_required
def edit_usuario(request, documento):
    usuario = Usuarios.objects.get(documento=documento)
    tipos_usuarios = TipoUsuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/crud_usuario')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'Usuarios/edit_usuario.html', {'form': form, 'usuario': usuario, 'tipos_usuarios': tipos_usuarios})

@never_cache
@login_required
def update_usuario(request, documento):
    usuario = Usuarios.objects.get(documento=documento)
    tipos_usuarios = TipoUsuario.objects.all()
    form = UsuarioForm(request.POST, request.FILES, instance = usuario)
    if form.is_valid():
        if 'foto' in request.FILES:
            usuario.foto = request.FILES['foto']
        form.save()
        return redirect('/crud_usuario')
    else:
        print(form.errors)
    return render(request, 'Usuarios/edit_usuario.html', {'usuario':usuario})

@never_cache
@login_required
def destroy_usuario(request, documento):   
    usuario = Usuarios.objects.get(documento=documento)
    usuario.delete()    
    return redirect('crud_usuario')

#Login
def signup(request):
    tipos_usuarios = TipoUsuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                # messages.success(request, '¡Usuario registrado exitosamente!')
                return redirect('/habitaciones_disponibles/?documento={}'.format(user.documento))  
            except Exception as e:
                print(f"Error al registrar usuario: {e}")
                return render(request, 'Usuarios/signup.html', {'form': form, 'error_message': 'Error al registrar usuario'})
        print(form.errors)
    else:
        form = UsuarioForm()
    
    return render(request, 'Usuarios/signup.html', {'form': form, 'tipos_usuarios': tipos_usuarios})

def signin(request):
    if request.method == 'GET':
        return render(request, 'Usuarios/signin.html', {'form': CustomAuthenticationForm()})
    else:
        form = CustomAuthenticationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['Nombre']
            password = form.cleaned_data['password']

            try:
                user = Usuarios.objects.get(Nombre=username)
                if check_password(password, user.password):
                    login(request, user)
                    if user.is_superuser or user.tipo_id == 101:
                        return redirect('/crud_usuario')
                    elif user.tipo_id == 102:
                        return redirect('/recepcionista')
                    else:
                        return redirect('/habitaciones_disponibles/?documento={}'.format(user.documento))   
                else: 
                    messages.error(request, 'password incorrecta.')
            except Usuarios.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
        
        print(form.errors)
        return render(request, 'Usuarios/signin.html', {'form': form})
        

@never_cache
@login_required
def signout(request):
    logout(request)
    return redirect('/signin')


# Crud habitaciones
@never_cache
@login_required
def habitaciones(request):
    documento_usuario = request.GET.get('documento', None)
    habitaciones_disponibles = Habitacion.objects.filter(estado='Disponible')
    tipos_habitacion = TipoHabitacion.objects.all()
    context = {'habitaciones_disponibles': habitaciones_disponibles, 'tipos_habitacion': tipos_habitacion, 'documento_usuario': documento_usuario}
    return render(request, 'Habitaciones/habitaciones.html', context)

def filtrar_habitaciones(request):
        fecha_inicio = request.GET.get('fechaInicio')
        fecha_fin = request.GET.get('fechaFin')
        tipo = request.GET.get('tipo')
        habitaciones_filtradas = Habitacion.objects.filter(tipo=tipo)
        html = render_to_string('Habitaciones\habitaciones_filtradas.html', {'habitaciones_disponibles': habitaciones_filtradas})
        return JsonResponse({'html': html})

@never_cache
@login_required
def addnew_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                hab = form.save(commit=False)
                hab.save()
                return redirect('/crud_habitacion')
            except:
                pass
    else:
        form = HabitacionForm()
    return render(request, 'Habitaciones/addnew_habitacion.html', {'form': form})

@never_cache
@login_required
def detalle_hab(request, numero):
    documento_usuario = request.user.documento
    habitacion = Habitacion.objects.get(numero=numero)
    context = {'documento_usuario': documento_usuario, 'habitacion': habitacion}
    return render(request, 'Habitaciones/habitacion.html', context)

@never_cache
@login_required
def crud_habitacion(request):
    habitacion = Habitacion.objects.all()
    return render(request, 'Habitaciones/show_habitacion.html', {'habitacion': habitacion})

@never_cache
@login_required
def edit_habitacion(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    tipos_habitacion = TipoHabitacion.objects.all()
    return render(request, 'Habitaciones/edit_habitacion.html', {'habitacion':habitacion, 'tipos_habitacion': tipos_habitacion})

@never_cache
@login_required
def update_habitacion(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    form = HabitacionForm(request.POST, request.FILES, instance=habitacion)
    usuario = request.user.tipo.rol if request.user.tipo else None
    if form.is_valid():
        if 'imagen' in request.FILES:
            habitacion.imagen = request.FILES['imagen']
        form.save()
        if usuario == 101:
            return redirect('/crud_habitacion')
        else:
            return redirect('/habitacion_recepcionista')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'Habitaciones/edit_habitacion.html', {'habitacion': habitacion, 'form': form})

@never_cache
@login_required
def destroy_habitacion(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    habitacion.delete()
    return redirect('/crud_habitacion')


#Crud Tipo Habitacion
@never_cache
@login_required
def crud_tipohabitacion(request):
    tipohabitacion = TipoHabitacion.objects.all()
    return render(request, 'T_habitaciones/show_habitacion.html', {'tipohabitacion': tipohabitacion})

@never_cache
@login_required
def addnew_tipohabitacion(request):
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST)
        if form.is_valid():
            try:
                tip_hab = form.save(commit=False)
                tip_hab.save()
                return redirect('/crud_tipohabitacion')
            except:
                pass
    else:
        form = TipoHabitacionForm()
    return render(request, 'T_habitaciones/addnew_habitacion.html', {'form': form})

@never_cache
@login_required
def edit_tipohabitacion(request, id):
    tipohabitacion = TipoHabitacion.objects.get(id=id)
    return render(request, 'T_habitaciones/edit_habitacion.html', {'tipohabitacion': tipohabitacion})

@never_cache
@login_required
def update_tipohabitacion(request, id):
    habitacion = TipoHabitacion.objects.get(id=id)
    form = TipoHabitacionForm(request.POST, request.FILES, instance=habitacion)
    if form.is_valid():
        if 'imagen' in request.FILES:
            habitacion.imagen = request.FILES['imagen']
        form.save()
        return redirect('/crud_tipohabitacion')
    else:
        form = TipoHabitacionForm(instance=habitacion)
    return render(request, 'T_habitaciones/edit_habitacion.html', {'tipohabitacion': habitacion})

@never_cache
@login_required
def destroy_tipohabitacion(request, id):
    tipohabitacion = TipoHabitacion.objects.get(id=id)
    tipohabitacion.delete()
    return redirect('/crud_tipohabitacion')


#crud servicios
@never_cache
@login_required
def crud_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/show_servicio.html', {'servicios': servicios})

@never_cache
@login_required
def addnew_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            try:
                servicio = form.save(commit=False)
                servicio.save()
                return redirect('/crud_servicio')
            except:
                pass
    else:
        form = ServicioForm()
    return render(request, 'Servicios/addnew_servicio.html', {'form': form})

@never_cache
@login_required
def edit_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    form = ServicioForm(instance=servicio)
    return render(request, 'Servicios/edit_servicio.html', {'form': form, 'servicio': servicio})

@never_cache
@login_required
def update_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    form = ServicioForm(request.POST, instance=servicio)
    
    if form.is_valid():
        form.save()
        return redirect('/crud_servicio')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'Servicios/edit_servicio.html', {'servicio': servicio})

def destroy_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('/crud_servicio')


#crud Productos
@never_cache 
@login_required
def crud_producto(request):
    producto = Producto.objects.all()
    return render(request, 'Productos/show_producto.html', {'producto': producto})

@never_cache
@login_required
def addnew_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            try:
                pro = form.save(commit=False)
                pro.save()
                return redirect('/crud_producto')
            except:
                pass
    else:
        form = ProductoForm()
    return render(request, 'Productos/addnew_producto.html', {'form': form})

@never_cache
@login_required
def edit_producto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    return render(request, 'Productos/edit_producto.html', {'form': form, 'producto': producto})    

@never_cache
@login_required
def update_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto')
        else:
            print(form.errors)
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'Productos/edit_producto.html', {'form': form, 'producto': producto})

@never_cache
@login_required
def destroy_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/crud_producto')


#crud tipo producto
@never_cache 
@login_required
def crud_tipoproducto(request):
    tipoproducto = TipoProducto.objects.all()
    return render(request, 'T_productos/show_producto.html', {'tipoproducto': tipoproducto})

@never_cache
@login_required
def addnew_tipoproducto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            try:
                tipo_prod = form.save(commit=False)
                tipo_prod.save()
                return redirect('/crud_tipoproducto')
            except:
                pass
    else:
        form = TipoProductoForm()
    return render(request, 'T_productos/addnew_producto.html', {'form': form})

@never_cache
@login_required
def edit_tipoproducto(request, id):
    tipoproducto = TipoProducto.objects.get(id=id)
    return render(request, 'T_productos/edit_producto.html', {'tipoproducto': tipoproducto})

@never_cache
@login_required
def update_tipoproducto(request, id):
    tipo_producto = TipoProducto.objects.get(id=id)
    form = TipoProductoForm(request.POST, instance=tipo_producto)
    if form.is_valid():
        form.save()
        return redirect('/crud_tipoproducto')
    else:
        form = TipoProductoForm(instance=tipo_producto)
    return render(request, 'T_productos/edit_producto.html', {'tipoproducto': tipo_producto})

@never_cache
@login_required
def destroy_tipoproducto(request, id):
    tipoproducto = TipoProducto.objects.get(id=id)
    tipoproducto.delete()
    return redirect('/crud_tipoproducto')


#crud tipo servicio
@never_cache
@login_required
def crud_tiposervicio(request):
    tipos_servicio = TipoServicio.objects.all()
    return render(request, 'T_servicios/show_servicio.html', {'tipos_servicio': tipos_servicio})

@never_cache
@login_required
def addnew_tiposervicio(request):
    if request.method == 'POST':
        form = TipoServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_tiposervicio')
    else:
        form = TipoServicioForm()
    return render(request, 'T_servicios/addnew_servicio.html', {'form': form})

@never_cache
@login_required
def edit_tiposervicio(request, id):
    tipo_servicio = TipoServicio.objects.get(id=id)
    form = TipoServicioForm(instance=tipo_servicio)
    return render(request, 'T_servicios/edit_servicio.html', {'form': form, 'tipo_servicio': tipo_servicio})

@never_cache
@login_required
def update_tiposervicio(request, id):
    tipo_servicio = TipoServicio.objects.get(id=id)
    form = TipoServicioForm(request.POST, instance=tipo_servicio)
    print("hola")
    if form.is_valid():
        form.save()
        return redirect('crud_tiposervicio')
    return render(request, 'T_servicios/edit_servicio.html', {'form': form, 'tipo_servicio': tipo_servicio})

@never_cache
@login_required
def destroy_tiposervicio(request, id):
    tipo_servicio = TipoServicio.objects.get(id=id)
    tipo_servicio.delete()
    return redirect('crud_tiposervicio')


#crud tipo usuario
@never_cache
@login_required
def crud_tipousuario(request):
    tipousuario = TipoUsuario.objects.all()
    return render(request, 'T_usuarios/show_usuario.html', {'tipousuario': tipousuario})

@never_cache
@login_required
def addnew_tipousuario(request):
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            try:
                tipo_user = form.save(commit=False)
                tipo_user.save()
                return redirect('/crud_tipousuario')
            except:
                pass
    else:
        form = TipoUsuarioForm()
    return render(request, 'T_usuarios/addnew_usuario.html', {'form': form})

@never_cache
@login_required
def edit_tipousuario(request, id):
    tipousuario = TipoUsuario.objects.get(id=id)
    return render(request, 'T_usuarios/edit_usuario.html', {'tipousuario': tipousuario})

@never_cache
@login_required
def update_tipousuario(request, id):
    tipousuario = TipoUsuario.objects.get(id=id)
    form = TipoUsuarioForm(request.POST, instance=tipousuario)
    if form.is_valid():
        form.save()
        return redirect('/crud_tipousuario')
    else:
        form = TipoUsuarioForm(instance=tipousuario)
    return render(request, 'T_usuarios/edit_usuario.html', {'tipousuario': tipousuario})

@never_cache
@login_required
def destroy_tipousuario(request, id):
    tipousuario = TipoUsuario.objects.get(id=id)
    tipousuario.delete()
    return redirect('/crud_tipousuario')


#crud reservas
@never_cache
@login_required
def crud_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'Reservas/show_reserva.html', {'reservas': reservas})

@never_cache
@login_required
def addnew_reserva(request):
    usuarios = Usuarios.objects.all()
    habitaciones = Habitacion.objects.all()
    user = request.user
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            fecha_ingreso = form.cleaned_data['fecha_ingreso']
            fecha_salida = form.cleaned_data['fecha_salida']
            habitacion = form.cleaned_data['nro_habitacion']
            if fecha_ingreso >= fecha_salida:
                messages.error(request, "La fecha de inicio debe ser anterior a la fecha de salida.")
                return redirect('addnew_reserva')
            reserva = form.save(commit=False)
            if check_availability(habitacion.numero, reserva.fecha_ingreso, reserva.fecha_salida):
                reserva.save()
                if user.tipo_id == 101:
                    return redirect('/crud_reserva')
                elif usuario == 105:
                    return redirect('/profile')
                else:
                    return redirect('/recepcionista')
            else:
                messages.error(request, "La habitación seleccionada no está disponible para las fechas elegidas.")
                return redirect('addnew_reserva')
    else:
        form = ReservaForm()
    return render(request, 'Reservas/addnew_reserva.html', {'form': form, 'usuarios': usuarios, 'habitaciones': habitaciones})

@never_cache
@login_required
def edit_reserva(request, id):
    usuarios = Usuarios.objects.all()
    habitacion = Habitacion.objects.all()
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(instance=reserva)
    return render(request, 'Reservas/edit_reserva.html', {'form': form, 'reserva': reserva, 'usuarios': usuarios, 'habitacion': habitacion})    

@never_cache
@login_required
def update_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            if user.tipo_id == 101:
                return redirect('/crud_reserva')
            else:
                return redirect('/recepcionista')
        else:
            print(form.errors)
    else:
        form = ReservaForm(instance=reserva)
    if usuario == 101:
        return render(request,'Reservas/edit_reserva.html', {'form': form, 'reserva': reserva})
    else:
        return render(request,'/Recepcionista/edit_reserva_recepcionista', {'form': form, 'reserva': reserva})

@never_cache
@login_required
def destroy_reserva(request, id):
    user = request.user
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    usuario = request.user.tipo.rol if request.user.tipo else None
    if user.tipo_id == 101:
        return redirect('/crud_reserva')
    else:
        return redirect('/recepcionista')

def check_availability(nro_habitacion, fecha_ingreso, fecha_salida):
    reservas_existentes = Reserva.objects.filter(
        nro_habitacion_id=nro_habitacion,
        fecha_ingreso__lte=fecha_salida,
        fecha_salida__gte=fecha_ingreso,
    ).exists()
    return not reservas_existentes

@never_cache
@login_required
def confirmacion_reserva(request, numero):
    user = request.user
    usuarios = Usuarios.objects.all()
    habitacion = Habitacion.objects.get(numero=numero)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            fecha_ingreso = form.cleaned_data['fecha_ingreso']
            fecha_salida = form.cleaned_data['fecha_salida']
            if fecha_ingreso >= fecha_salida:
                messages.error(request, "La fecha de inicio debe ser anterior a la fecha de salida.")
                return redirect('confirmacion_reserva', numero=habitacion.numero)
            reserva = form.save(commit=False)
            if check_availability(habitacion.numero, reserva.fecha_ingreso, reserva.fecha_salida):
                reserva.save()
                context = {'habitacion': habitacion}
                return redirect('reservas_x_usuario', user.documento)
            else:
                messages.error(request, "La habitación seleccionada no está disponible para las fechas elegidas.")
                return redirect('confirmacion_reserva', habitacion.numero)
    else:
        form = ReservaForm(initial={'documento': habitacion})
    return render(request, 'Reservas/confirmacion_reserva.html', {'form': form, 'habitacion': habitacion})


#Reservas por usuario
@never_cache
@login_required
def reservas_x_usuario(request, documento):
    usuario = Usuarios.objects.get(documento=documento)
    reservas_usuario = Reserva.objects.filter(documento=usuario)

    return render(request, 'Usuarios/reservas_x_usuario.html', {'usuario': usuario, 'reservas_usuario': reservas_usuario})


#crud Consumos
@never_cache 
@login_required
def crud_consumos(request):
    consumos = Consumos.objects.all()
    return render(request, 'Consumos/show_consumo.html', {'consumos': consumos})

@never_cache
@login_required
def addnew_consumo(request):
    if request.method == 'POST':
        form = ConsumosForm(request.POST)
        if form.is_valid():
            consumo = form.save(commit=False)
            consumo.save()
            return redirect('/crud_consumo')
    else:
        form = ConsumosForm()
    return render(request, 'Consumos/addnew_consumo.html', {'form': form})

@never_cache
@login_required
def edit_consumo(request, id):
    consumo = Consumos.objects.get(id=id)
    form = ConsumosForm(instance=consumo)
    return render(request, 'Consumos/edit_consumo.html', {'form': form, 'consumo': consumo})    

@never_cache
@login_required
def update_consumo(request, id):
    consumo = Consumos.objects.get(id=id)
    usuario = request.user.tipo.rol if request.user.tipo else None
    if request.method == 'POST':
        form = ConsumosForm(request.POST, instance=consumo)
        if form.is_valid():
            form.save()
            if usuario == 101:
                return redirect('/crud_consumo')
            else:
                return redirect('/consumo_recepcionista')
        else:
            print(form.errors)
    else:
        form = ConsumosForm(instance=consumo)

    return render(request, 'Consumos/edit_consumo.html', {'form': form, 'consumo': consumo})

@never_cache
@login_required
def destroy_consumo(request, id):
    usuario = request.user.tipo.rol if request.user.tipo else None
    consumo = Consumos.objects.get(id=id)
    consumo.delete()
    if usuario == 101:
        return redirect('/crud_consumo')
    else:
        return redirect('/consumo_recepcionista')

#crud factura
@never_cache
@login_required
def crud_factura(request):
    facturas = Factura.objects.all()
    return render(request, 'Facturas/show_factura.html', {'facturas': facturas})

#perfil del usuario
@never_cache
@login_required
def profile(request):
    user = request.user
    reservas = Reserva.objects.filter(documento=user)
    return render(request, 'Usuarios/profile.html', {'user': user, 'reservas': reservas})

@never_cache
@login_required
def profile_edit_usuario(request, documento):
    usuario = Usuarios.objects.get(documento=documento)
    tipos_usuarios = TipoUsuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            print(form.errors)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'Usuarios/profile_edit_usuario.html', {'form': form, 'usuario': usuario, 'tipos_usuarios': tipos_usuarios})

@never_cache 
@login_required
def confirm_destroy_usuario(request, documento):   
    usuario = Usuarios.objects.get(documento=documento)
    if request.method == 'POST':
        password = request.POST.get('password')
        if check_password(password, usuario.password):
            return render(request, 'Usuarios/confirm_delete_usuario.html', {'usuario': usuario})
        else:
            return HttpResponse('Contraseña incorrecta. No se pudo confirmar la eliminación de la cuenta.')
    return render(request, 'Usuarios/confirm_delete_usuario_form.html', {'usuario': usuario})
    return redirect('crud_usuario')


#Perfil de Recepcionista
@never_cache
@login_required
def perfil_recepcionista(request):
    usuario = request.user
    reservas = Reserva.objects.all()
    context = {'usuario': usuario,'reservas': reservas}
    return render(request, 'Recepcionista/recepcionista.html', context)

@never_cache
@login_required
def addnew_reserva_recepcionista(request):
    usuarios = Usuarios.objects.all()
    habitaciones = Habitacion.objects.all()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            return redirect('/recepcionista')
    else:
        form = ReservaForm()
    return render(request, 'Recepcionista/addnew_reserva_recepcionista.html', {'form': form, 'usuarios': usuarios, 'habitaciones': habitaciones})

@never_cache
@login_required
def edit_reserva_recepcionista(request, id):
    usuarios = Usuarios.objects.all()
    habitacion = Habitacion.objects.all()
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(instance=reserva)
    return render(request, 'Recepcionista/edit_reserva_recepcionista.html', {'form': form, 'reserva': reserva, 'usuarios': usuarios, 'habitacion': habitacion}) 

@never_cache
@login_required
def consumo_recepcionista(request):
    usuario = request.user
    consumos = Consumos.objects.all()
    context = {'usuario': usuario,'consumos': consumos}
    return render(request, 'Recepcionista/consumo_recepcionista.html', context)

@never_cache
@login_required
def addnew_consumo_recepcionista(request):
    if request.method == 'POST':
        form = ConsumosForm(request.POST)
        if form.is_valid():
            consumo = form.save(commit=False)
            consumo.save()
            return redirect('/consumo_recepcionista')
    else:
        form = ConsumosForm()
    return render(request, 'Recepcionista/addnew_consumo_recepcionista.html', {'form': form})

@never_cache
@login_required
def edit_consumo_recepcionista(request, id):
    consumo = Consumos.objects.get(id=id)
    form = ConsumosForm(instance=consumo)
    return render(request, 'Recepcionista/edit_consumo_recepcionista.html', {'form': form, 'consumo': consumo})  

@never_cache
@login_required
def habitacion_recepcionista(request):
    usuario = request.user
    habitacion = Habitacion.objects.all()
    context = {'usuario': usuario,'habitacion': habitacion}
    return render(request, 'Recepcionista/habitacion_recepcionista.html', context)

@never_cache
@login_required
def edit_habitacion_recepcionista(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    tipos_habitacion = TipoHabitacion.objects.all()
    return render(request, 'Recepcionista/edit_habitacion_recepcionista.html', {'habitacion':habitacion, 'tipos_habitacion': tipos_habitacion})

@never_cache
@login_required
def factura_recepcionista(request):
    usuario = request.user
    facturas = Factura.objects.all()
    context = {'usuario': usuario,'facturas': facturas}
    return render(request, 'Recepcionista/factura_recepcionista.html', context)