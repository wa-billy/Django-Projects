
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', HomeView, name='Home'),
    path('about/', AboutView, name='About'),
    path('menu/', MenuView, name='Menu'),
    path('book/', BookTableView, name='Book_Table'),
    path('feedback', FeedbackView, name='Feedback_Form'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView, name='signup'),
    path('logout/', LogoutView, name='logout'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
