from django.urls import path,include
from .views import*
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('post',PostView,basename='post'),
# router.register(r'posts', PostView, basename='post')

urlpatterns=[
    path('registration/',RegistrationView),
    path('login/',LoginView),
    path('profile/',profile),
    path('update/',UpdateProfile),
    path('home/',HomeView),
    path('create/', PostView.as_view({'post': 'create'})),
    path('update_post/<int:pk>/', PostView.as_view({'post':'update_post'})),
    #  path('create/',PostView.as_view(), name='create_post'),


     path('', include(router.urls)),
    
   

] 

