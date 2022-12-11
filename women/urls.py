# noqa: I001, I005
"""Django-func path"""
from django.urls import path, include
from rest_framework import routers
from .views import WomenHome, about, AddPage, ContactFormView, LoginUser, logout_user, RegisterUser, ShowPost, \
    WomenCategory, WomenViewSet

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('api/v1/', include(router.urls)),
    # path("api/v1/womenlist/", WomenViewSet.as_view({'get': 'list'})),
    # path("api/v1/womenlist/<int:pk>/", WomenViewSet.as_view({'put': 'update'}))
]
