from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>', views.category, name='category'),
    path('ebooks/', views.ebooks, name='ebooks'),
    path('ebook/<int:ebook_id>', views.ebook, name='ebook'),
    path('ebook/<int:ebook_id>/comment', views.comment, name='comment'),
    path('add', views.add, name='add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
