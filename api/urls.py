from django.urls import path
from .views import SwiftRetrieveDestroyAPIView, SwiftCreateAPIView

urlpatterns = [
    path("swift-codes/<str:swift_code>", SwiftRetrieveDestroyAPIView.as_view(), name="swift_code_detail"),
    path("swift-codes", SwiftCreateAPIView.as_view(), name="swift_code_create"),
]