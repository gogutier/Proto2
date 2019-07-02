from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',views.Inicio.as_view(),name='Inicio'),
    url(r'^api/data_inicio/$',views.get_data_inicio,name='api-data'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$' ,views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,name='post_publish'),
    url(r'^contact/$', views.ContactView, name='contact'),
    url(r'^appointment/$',views.appointmentCreate.as_view(),name='appointment_create'),
    url(r'^OCI/$',views.CreateOCIView.as_view(),name='OCI_create'),
    url(r'^csv/$',views.CargaCSV1, name='carga_csv_1'),
    url(r'^csv2/$',views.CargaCSV2, name='carga_csv_2'),
    url(r'^$',views.listaprodid,name='prodid_list'),
    url(r'^book/$',views.create_book_normal,name='book_normal'),
    url(r'^book/$',views.create_book_model_form,name='book_normal_model'),
    url(r'^book/$',views.create_book_with_authors,name='book_authors_model'),
    url(r'^pruebaultimate/$',views.prueba_ultimate,name='prueba_ultimate'),
    url(r'^cargaprograma/$',views.carga_prog,name='carga_prog'),
    url(r'^cargaorderinfo/$',views.carga_orderinfo,name='carga_orderinfo'),
    url(r'^cargaproduccion/$',views.carga_prod_real,name='carga_prod_real'),
    url(r'^resumenconversion/$',views.ResConvView.as_view(),name='res_conv'),
    url(r'^resconv/$',views.res_conv_v2,name='res_conv_v2'), #Lista de programas conversióno
    url(r'^rescorr/$',views.res_corr,name='res_corr'), #Lista programas corrugado
    url(r'^minutas/$',views.minutas,name='minutas'),
    url(r'^minuta/new/$',views.minuta_new,name='minuta_new'),
    url(r'^ordenprog/(?P<pk>\d+)$', views.OrdenProgDetailView.as_view(),name='ordenprog_detail'), #resumen de programas conversión cargados
    url(r'^ordenprogcorr/(?P<pk>\d+)$', views.OrdenProgCorrDetailView.as_view(),name='ordenprogcorr_detail'),
    url(r'^minuta/(?P<pk>\d+)$', views.minuta_detail,name='minuta_detail'),
    url(r'^cargamaestropadron/$',views.carga_maestrop,name='carga_maestrop'),
    url(r'^kpiconv/$',views.kpi_conv,name='kpi_conv'),
    url(r'^kpiconv_res/$',views.kpi_conv_res,name='kpi_conv_res'),
    url(r'^cargaprogcorr/$',views.carga_prog_corr,name='carga_prog_corr'),
    url(r'^cargaprodcorr/$',views.carga_prod_corr,name='carga_prod_corr'),
    url(r'^cargaproyeccion/$',views.carga_proyeccion,name='carga_proyeccion'),
    url(r'^cargainventario/$',views.carga_inventario,name='carga_inventario'),
    url(r'^res_pareados/$',views.res_pareados,name='res_pareados'),
    url(r'^res_inventario/$',views.resumen_inv,name='resumen_inv'),
    url(r'^cump_proto/$',views.cump_proto,name='cump_proto'),
    url(r'^placas_wip/$',views.placas_wip,name='placas_wip'),
    url(r'^api/data_wip/$',views.get_data_wip,name='api-data-wip'),
    url(r'^api/data_wip_2/$',views.get_data_wip_2,name='api-data-wip-2'),
    url(r'^qr_despacho/$',views.qr_despacho,name='qr_despacho'),
    url(r'^camion_detail/(?P<pk>\d+)$', views.CamionDetailView.as_view(),name='camion_detail'), #datos de cada camiòn con qr asociado

]
