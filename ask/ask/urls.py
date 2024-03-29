
"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from qa import views
urlpatterns = [
    path('', views.new_questions_list, name='qa_new'),
    path('admin/', admin.site.urls),
    path('login/', views.test),
    path('signup/', views.test),
    path('ask/', views.test),
    path('popular/', views.popular_questions_list, name='qa_popular'),
    path('new/', views.test),
    path('question/<str:slug>/', views.question, name='qa_question'),
    path('ask//popular/', views.test),
    re_path(r'^', views.not_found),
]
