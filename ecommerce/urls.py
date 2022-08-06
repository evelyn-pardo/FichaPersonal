"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ventas.views import inicio,articulo,cliente,crearCliente,venta
from ventas.views import FichaPersonal,empleado,crearEmpleado,eliminarEmpleado,editarEmpleado,\
    datosMedicos,crearDatosMedicos,eliminarDatosMedicos,editarMedico,\
    contactoEmergencias,crearContactoEmergencias,eliminarContactoEmergencia,editarContactoEmergencias,\
    infoAcademica,crearInfoAcademica,eliminarInfoAcademica,editarInfoAcademica,\
    capacitaciones,crearCapacitaciones,eliminarCapacitaciones,editarCap,\
    cargo,crearCargo,eliminarCargo,editarCar,\
    departamento,crearDepartamento,eliminarDepartamento,editarDepartamento,\
    sueldo,crearSueldo,eliminarSueldo,editarSueldo
from django.conf.urls.static import static
from ecommerce import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),

    path('fichaPersonal/', FichaPersonal, name='FichaPersonal'),

    path('empleado/', empleado, name='empleado'),
    path('crearEmpleado', crearEmpleado, name='crearEmpleado'),
    path('eliminarEmpleado', eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado', editarEmpleado, name='editarEmpleado'),

    path('datosMedicos/', datosMedicos, name='datosMedicos'),
    path('crearDatosMedicos/', crearDatosMedicos, name='medic'),
    path('eliminarDatosMedicos/', eliminarDatosMedicos, name='eliminarDatosMedicos'),
    path('editarMedico/', editarMedico, name='medic'),

    path('contactoEmergencias/', contactoEmergencias, name='contactoEmergencias'),
    path('crearContactoEmergencias/', crearContactoEmergencias, name='crearContactoEmergencias'),
    path('eliminarContactoEmergencias/', eliminarContactoEmergencia, name='eliminarContactoEmergencia'),
    path('editarContacto/', editarContactoEmergencias, name='editarContactoEmergencias'),

    path('infoAcademica/', infoAcademica, name='infoAcademica'),
    path('crearInfoAcademica/', crearInfoAcademica, name='crearInfoAcademica'),
    path('eliminarInfoAcademica/', eliminarInfoAcademica, name='eliminarInfoAcademica'),
    path('editarInformacion/', editarInfoAcademica, name='editarInfoAcademica'),

    path('capacitaciones/', capacitaciones, name='capacitaciones'),
    path('crearCapacitaciones/', crearCapacitaciones, name='crearCapacitaciones'),
    path('eliminarCapacitaciones/',eliminarCapacitaciones, name='eliminarCapacitaciones'),
    path('editarCap/', editarCap, name='cap'),

    path('cargo', cargo, name='cargo'),
    path('crearCargo', crearCargo, name='crearCargo'),
    path('eliminarCargo', eliminarCargo, name='eliminarCargo'),
    path('editarcar/', editarCar, name='car'),

    path('departamento', departamento, name='departamento'),
    path('crearDepartamento', crearDepartamento, name='crearDepartamento'),
    path('eliminarDepartamento', eliminarDepartamento, name='eliminarDepartamento'),
    path('editarDepart', editarDepartamento, name='editarDepartamento'),

    path('sueldo', sueldo, name='sueldo'),
    path('crearSueldo', crearSueldo, name='crearSueldo'),
    path('eliminarSueldo', eliminarSueldo, name='eliminarSueldo'),
    path('editarSueldo', editarSueldo, name='editarSueldo'),

    path('venta/', venta, name='venta'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)