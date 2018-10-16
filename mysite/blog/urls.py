from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',views.Inicio.as_view(),name='Inicio'),
    url(r'^api/data/$',views.get_data,name='api-data'),
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
    url(r'^solcambios/new/$', views.CreateSolCambView.as_view(), name='solcamb_new'),
    url(r'^solcambios/$',views.SolCambListView.as_view(),name='solcamb_list'),
    url(r'^solcambioss/(?P<pk>\d+)$', views.SolCambDetailView.as_view(), name='solcamb_detail'),
    url(r'^appointment/$',views.appointmentCreate.as_view(),name='appointment_create'),
    url(r'^OCI/$',views.CreateOCIView.as_view(),name='OCI_create'),
    url(r'^csv/$',views.CargaCSV1, name='carga_csv_1'),
    url(r'^csv2/$',views.CargaCSV2, name='carga_csv_2'),
    url(r'^$',views.listaprodid,name='prodid_list'),
    url(r'^newcambios/$',views.solcambiosss,name='solicitud_cambio'),
    url(r'^book/$',views.create_book_normal,name='book_normal'),
    url(r'^book/$',views.create_book_model_form,name='book_normal_model'),
    url(r'^book/$',views.create_book_with_authors,name='book_authors_model'),
    url(r'^pruebaultimate/$',views.prueba_ultimate,name='prueba_ultimate'),
    url(r'^cargaprograma/$',views.carga_prog,name='carga_prog'),
    url(r'^cargaproduccion/$',views.carga_prod_real,name='carga_prod_real'),
    url(r'^resumenconversion/$',views.ResConvView.as_view(),name='res_conv'),
    url(r'^resconv/$',views.res_conv_v2,name='res_conv_v2'),
    url(r'^minutas/$',views.minutas,name='minutas'),
    url(r'^minuta/new/$',views.minuta_new,name='minuta_new'),
    url(r'^ordenprog/(?P<pk>\d+)$', views.OrdenProgDetailView.as_view(),name='ordenprog_detail'),
    url(r'^minuta/(?P<pk>\d+)$', views.minuta_detail,name='minuta_detail'),





]
