from django.urls import path,include
from .views import AddServiceProvider,Serviceproviderdetail,Listserviceprovider,Deleteserviceprovider,Updateserviceprovider

urlpatterns = [
    path('add/',AddServiceProvider.as_view(), name = 'add_serviceprovider'),
    path('view/',Listserviceprovider.as_view(), name = 'list_serviceprovider'),
    path('<int:pk>view/',Serviceproviderdetail.as_view(), name = 'detail_serviceprovider'),
    path('<int:pk>delete/',Deleteserviceprovider.as_view(), name = 'delete_serviceprovider'),
    path('<int:pk>update/',Updateserviceprovider.as_view(), name = 'update_serviceprovider'),
]
