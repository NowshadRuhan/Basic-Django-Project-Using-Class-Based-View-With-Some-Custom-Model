from django.conf.urls import url
from django.urls import path
from cbv import views

# #settings added
from django.conf import settings
# # #static and static_url added
from django.conf.urls.static import static


app_name = 'cbv'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Home' ),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musicians'),
    path('add_musician/', views.AddMusician.as_view(), name='AddMusician'),
    path('update_musician/<pk>/', views.UpdateMusician.as_view(), name='UpdateMusician'),
    path('delete_musician/<pk>/', views.DeleteMusician.as_view(), name='DeleteMusician'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
