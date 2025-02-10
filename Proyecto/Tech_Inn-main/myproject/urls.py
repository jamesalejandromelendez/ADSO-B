from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from boards import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
#Usuarios
    path('crud_usuario', views.crud_usuario, name='crud_usuario'),
    path('addnew_usuario', views.addnew_usuario, name='addnew_usuario'),
    path('edit_usuario/<int:documento>', views.edit_usuario, name='edit_usuario'),
    path('update_usuario/<int:documento>', views.update_usuario, name='update_usuario'),
    path('delete_usuario/<int:documento>', views.destroy_usuario, name='delete_usuario'),
    path('reservas_x_usuario/<int:documento>/', views.reservas_x_usuario, name='reservas_x_usuario'), 
#Habitaciones
    path('crud_habitacion', views.crud_habitacion, name='crud_habitacion'),
    path('addnew_habitacion', views.addnew_habitacion, name='addnew_habitacion'),
    path('edit_habitacion/<int:numero>', views.edit_habitacion, name='edit_habitacion'),
    path('update_habitacion/<int:numero>', views.update_habitacion, name='update_habitacion'),
    path('delete_habitacion/<int:numero>', views.destroy_habitacion, name='destroy_habitacion'),
    path('habitaciones_disponibles/', views.habitaciones, name='habitaciones'),
    path('filtrar-habitaciones/', views.filtrar_habitaciones, name='filtrar_habitaciones'), 
    path('habitacion/<int:numero>/', views.detalle_hab, name='detalle_hab'),
#Productos
    path('crud_producto', views.crud_producto, name='crud_producto'),
    path('addnew_producto', views.addnew_producto, name='addnew_producto'),
    path('edit_producto/<int:id>', views.edit_producto, name='edit_producto'),
    path('update_producto/<int:id>', views.update_producto, name='update_producto'),
    path('delete_producto/<int:id>', views.destroy_producto, name='destroy_producto'),
#Servicio
    path('crud_servicio/', views.crud_servicio, name='crud_servicio'),
    path('addnew_servicio/', views.addnew_servicio, name='addnew_servicio'),
    path('edit_servicio/<int:id>/', views.edit_servicio, name='edit_servicio'),
    path('update_servicio/<int:id>', views.update_servicio, name='update_servicio'),
    path('delete_servicio/<int:id>/', views.destroy_servicio, name='destroy_servicio'),
#Reservas
    path('crud_reserva/', views.crud_reserva, name='crud_reserva'),
    path('addnew_reserva/', views.addnew_reserva, name='addnew_reserva'),
    path('edit_reserva/<int:id>/', views.edit_reserva, name='edit_reserva'),
    path('update_reserva/<int:id>/', views.update_reserva, name='update_reserva'),
    path('delete_reserva/<int:id>/', views.destroy_reserva, name='destroy_reserva'),
    path('confirmacion_reserva/<int:numero>/', views.confirmacion_reserva, name='confirmacion_reserva'),
#Consumos
    path('crud_consumo/', views.crud_consumos, name='crud_consumos'),
    path('addnew_consumo/', views.addnew_consumo, name='addnew_consumo'),
    path('edit_consumo/<int:id>/', views.edit_consumo, name='edit_consumo'),
    path('update_consumo/<int:id>/', views.update_consumo, name='update_consumo'),
    path('delete_consumo/<int:id>/', views.destroy_consumo, name='delete_consumo'),
#tipo habitacion
    path('crud_tipohabitacion', views.crud_tipohabitacion, name='crud_tipohabitacion'),
    path('addnew_tipohabitacion', views.addnew_tipohabitacion, name='addnew_tipohabitacion'),
    path('edit_tipohabitacion/<int:id>', views.edit_tipohabitacion, name='edit_tipohabitacion'),
    path('update_tipohabitacion/<int:id>', views.update_tipohabitacion, name='update_tipohabitacion'),
    path('delete_tipohabitacion/<int:id>', views.destroy_tipohabitacion, name='destroy_tipohabitacion'),
#tipo producto
    path('crud_tipoproducto', views.crud_tipoproducto, name='crud_tipoproducto'),
    path('addnew_tipoproducto', views.addnew_tipoproducto, name='addnew_tipoproducto'),
    path('edit_tipoproducto/<int:id>', views.edit_tipoproducto, name='edit_tipoproducto'),
    path('update_tipoproducto/<int:id>', views.update_tipoproducto, name='update_tipoproducto'),
    path('delete_tipoproducto/<int:id>', views.destroy_tipoproducto, name='destroy_tipoproducto'),
#tipo usuario
    path('crud_tipousuario', views.crud_tipousuario, name='crud_tipousuario'),
    path('addnew_tipousuario', views.addnew_tipousuario, name='addnew_tipousuario'),
    path('edit_tipousuario/<int:id>', views.edit_tipousuario, name='edit_tipousuario'),
    path('update_tipousuario/<int:id>', views.update_tipousuario, name='update_tipousuario'),
    path('delete_tipousuario/<int:id>', views.destroy_tipousuario, name='destroy_tipousuario'),
#TipoServicio
    path('crud_tiposervicio/', views.crud_tiposervicio, name='crud_tiposervicio'),
    path('addnew_tiposervicio/', views.addnew_tiposervicio, name='addnew_tiposervicio'),
    path('edit_tiposervicio/<int:id>/', views.edit_tiposervicio, name='edit_tiposervicio'),
    path('update_tiposervicio/<int:id>/', views.update_tiposervicio, name='update_tiposervicio'),
    path('delete_tiposervicio/<int:id>/', views.destroy_tiposervicio, name='destroy_tiposervicio'),
#Login
    path('signup', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    
#profile
    path('profile/', views.profile, name='profile'),
    path('profile_edit_usuario/<int:documento>', views.profile_edit_usuario, name='profile_edit_usuario'),
    path('confirm_delete_usuario/<int:documento>', views.confirm_destroy_usuario, name='confirm_delete_usuario'),

#Perfil de recepcionista
    path('recepcionista/', views.perfil_recepcionista, name='perfil_recepcionista'),
    path('consumo_recepcionista/', views.consumo_recepcionista, name='consumo_recepcionista'),
    path('addnew_consumo_recepcionista/', views.addnew_consumo_recepcionista, name='addnew_consumo_recepcionista'),
    path('edit_consumo_recepcionista/<int:id>/', views.edit_consumo_recepcionista, name='edit_consumo_recepcionista'),
    path('habitacion_recepcionista/', views.habitacion_recepcionista, name='habitacion_recepcionista'),
    path('edit_habitacion_recepcionista/<int:numero>', views.edit_habitacion_recepcionista, name='edit_habitacion_recepcionista'),
    path('factura_recepcionista/', views.factura_recepcionista, name='factura_recepcionista'),
    path('addnew_reserva_recepcionista/', views.addnew_reserva_recepcionista, name='addnew_reserva_recepcionista'),
    path('edit_reserva_recepcionista/<int:id>/', views.edit_reserva_recepcionista, name='edit_reserva_recepcionista'),

#ResetPassword
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="autenticacion/password-reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="autenticacion/password-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

#Facturas
    path('crud_factura/', views.crud_factura, name='crud_factura'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)