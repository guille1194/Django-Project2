from django.conf.urls import url, include
from .views import error, home, RegistrarPromovido, login_app, RegistroPromotor, ReportesUsuarios, ReportesEstadisticos, Reporte_VotoSi,Reporte_VotoNo,Reporte_Promotores,Reporte_Promovidos,csv_No_Votaron, csv_Si_Votaron
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^registrop$', RegistrarPromovido.as_view(), name = "registropromovido"),
    url(r'^error$', error, name='error'),
    url(r'^login/$', login_app, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^registro/$', RegistroPromotor.as_view(), name = 'registropromotor'),
    url(r'^reporteusuarios/$', ReportesUsuarios, name = 'ReportesUsuarios'),
    url(r'^reportesestadisticos/$', ReportesEstadisticos, name = 'ReportesEstadisticos'),
    url(r'^reporteusuarios/reporte_promotores/$', Reporte_Promotores.as_view(), name = 'reporte_promotores'),
    url(r'^reporteusuarios/reporte_promovidos/$',Reporte_Promovidos.as_view() , name = 'reporte_promovidos'),
    url(r'^reportesestadisticos/reporte_si/$',Reporte_VotoSi.as_view() , name = 'reporte_si'),
    url(r'^reportesestadisticos/reporte_no/$', Reporte_VotoNo.as_view(), name = 'reporte_no'),
    url(r'^imprimir_csv_no/$', csv_No_Votaron, name='csv_No_Votaron'),
    url(r'^imprimir_csv_si/$', csv_Si_Votaron, name='csv_Si_Votaron'),
]
