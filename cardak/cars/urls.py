from django.urls import path
from .views      import CarRegistryView

urlpatterns = [
    path('/registry', CarRegistryView.as_view()),
    # path('/signup', SignUpView.as_view()),
]