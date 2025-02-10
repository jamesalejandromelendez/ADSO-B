from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=20, null=True, default=None)
    class Meta:
        db_table = 'tbTipoUsuario'

    def __str__(self):
        return self.rol

class TipoHabitacion(models.Model):
    tipo = models.CharField(max_length=20)
    class Meta:
        db_table = 'tbTipoHabitacion'

    def __str__(self):
        return self.tipo

class TipoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=20, null=True)
    class Meta:
        db_table = 'tbTipoProducto'

    def __str__(self):
        return self.categoria

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = 'tbTipoServicio'

    def __str__(self):
        return self.nombre

class Usuarios(AbstractBaseUser, PermissionsMixin):
    documento = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200, unique=True)
    Apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    genero = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True, default='Activo')
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL, null=True, blank=True, default='105')
    foto = models.ImageField(upload_to='usuario_imagenes/', null=True, blank=True, default='usuario_imagenes/default.png')
    
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['Nombre'] 

    class Meta:
        db_table = 'tbUsuarios'

    def __str__(self):
        return str(self.documento)
        return Reserva.objects.filter(documento=self).count()

class Habitacion(models.Model):
    numero = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    caracteristicas = models.CharField(max_length=300, null=True, blank=True)
    costo_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    nro_cama_sencilla = models.IntegerField(null=True, blank=True)
    nro_cama_doble = models.IntegerField(null=True, blank=True)
    nro_camarotes = models.IntegerField(null=True, blank=True)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='habitacion_imagenes/', null=True, blank=True)

    class Meta:
        db_table = 'tbHabitacion'

    def __str__(self):
        return f'Habitación {self.numero}'
        self.fields['costo_base'].initial = 0.0

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_disponible = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=255, null=True)
    id_tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'tbProducto'

    def __str__(self):
        return self.nombre  

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    id_tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbServicio'

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, null=True)
    cantidad_adultos = models.IntegerField(null=True)
    cantidad_niños = models.IntegerField(null=True)
    fecha_ingreso = models.DateField(null=True)
    fecha_salida = models.DateField(null=True)
    nro_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=300, null=True, blank=True,)

    class Meta:
        db_table = 'tbReserva'

    def __str__(self):
        return f"Reserva {self.id}"
    
class Consumos(models.Model):
    id = models.AutoField(primary_key=True)
    id_Reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, null=True)
    id_Servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE, null=True)
    cantidad_s = models.IntegerField(null=True)
    id_Producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=True)
    cantidad_p = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    facturado = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbConsumos'

    def __str__(self):
        return f"Consumos {self.Id}"

class Factura(models.Model):
    Id = models.AutoField(primary_key=True)
    Fecha = models.DateField(null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    id_Reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'tbFactura'

class Reserva_Respaldo(models.Model):
    Id = models.AutoField(primary_key=True)
    Documento = models.IntegerField(null=True)
    Estado = models.CharField(max_length=20, null=True)
    CantidadAdultos = models.IntegerField(null=True)
    CantidadNiños = models.IntegerField(null=True)
    FechaIngreso = models.DateField(null=True)
    FechaSalida = models.DateField(null=True)
    Nro_habitacion = models.IntegerField(null=True)
    Comentarios = models.CharField(max_length=300, null=True, default='Sin comentarios por el cliente')

    class Meta:
        db_table = 'tbReserva_Respaldo'

class Factura_Respaldo(models.Model):
    Id = models.AutoField(primary_key=True)
    Fecha = models.DateField(null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ID_Consumo = models.IntegerField(null=True)

    class Meta:
        db_table = 'tbFactura_Respaldo'

class Usuarios_Respaldo(models.Model):
    Id = models.AutoField(primary_key=True)
    Documento = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=50, null=True)
    Apellido = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Telefono = models.CharField(max_length=15, null=True)
    Genero = models.CharField(max_length=20, null=True)
    Estado = models.CharField(max_length=20, null=True)
    Contraseña = models.CharField(max_length=255, null=True)
    Id_tipo = models.IntegerField(null=True)
    Fecha_Respaldo = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbUsuarios_Respaldo'