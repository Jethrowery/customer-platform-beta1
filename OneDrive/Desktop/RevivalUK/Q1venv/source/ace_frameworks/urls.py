"""ace_frameworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include
from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="Compliance Frameworks APIs Combo",
        default_version='v1',
        description="Early build phase",
        terms_of_service="https://www.aceallizon.com/brochures",
        contact=openapi.Contact(email="lfowowe@aceallizon.com"),
        license=openapi.License(name="Test License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    
    #Admin access
    path('admin/', admin.site.urls),
    
    #User access
    path('api/auth/', include('usermodel.urls')),
    
    #Plaform access
    path('api/platform/', include('customerplatform.urls')),
    #path('social_auth/', include(('social_auth.urls', 'social_auth'),
    #                                 namespace="social_auth")),
    
    #Social media access
    #path('api/api.json/', schema_view.without_ui(cache_timeout=0),
    #         name='schema-swagger-ui'),
    
    # Documentation dashboard
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
]
