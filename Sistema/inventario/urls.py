from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
path('login', views.Login.as_view(), name='login'),
path('panel', views.Panel.as_view(), name='panel'),
path('salir', views.Salir.as_view(), name='salir'),
path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),

path('listarProductos', views.ListarProductos.as_view(), name='listarProductos'),
path('agregarProducto', views.AgregarProducto.as_view(), name='agregarProducto'),
path('editarProducto/<int:p>', views.EditarProducto.as_view(), name='editarProducto'),

path('listarProveedores', views.ListarProveedores.as_view(), name='listarProveedores'),
path('agregarProveedor', views.AgregarProveedor.as_view(), name='agregarProveedor'),
path('editarProveedor/<int:p>', views.EditarProveedor.as_view(), name='editarProveedor'),

path('agregarPedido', views.AgregarPedido.as_view(), name='agregarPedido'),
path('listarPedidos', views.ListarPedidos.as_view(), name='listarPedidos'),
path('detallesPedido', views.DetallesPedido.as_view(), name='detallesPedido'),
path('verPedido/<int:p>',views.VerPedido.as_view(), name='verPedido'),
path('validarPedido/<int:p>',views.ValidarPedido.as_view(), name='validarPedido'),
path('generarPedido/<int:p>',views.GenerarPedido.as_view(), name='generarPedido'),
path('generarPedidoPDF/<int:p>',views.GenerarPedidoPDF.as_view(), name='generarPedidoPDF'),

path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),

path('emitirFactura', views.EmitirFactura.as_view(), name='emitirFactura'),
path('detallesDeFactura', views.DetallesFactura.as_view(), name='detallesDeFactura'),
path('listarFacturas',views.ListarFacturas.as_view(), name='listarFacturas'),
path('verFactura/<int:p>',views.VerFactura.as_view(), name='verFactura'),
path('generarFactura/<int:p>',views.GenerarFactura.as_view(), name='generarFactura'),

path('crearUsuario',views.CrearUsuario.as_view(), name='crearUsuario'),
path('listarUsuarios', views.ListarUsuarios.as_view(), name='listarUsuarios'),

path('configuracionGeneral', views.ConfiguracionGeneral.as_view(), name='configuracionGeneral'),

path('verManualDeUsuario/<str:pagina>/',views.VerManualDeUsuario.as_view(), name='verManualDeUsuario')
]

