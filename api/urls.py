from django.urls import path
from .views import SwiftRetrieveDestroyAPIView

urlpatterns = [
    path("swift-codes/<str:swift_code>", SwiftRetrieveDestroyAPIView.as_view(), name="swift_code_detail")
]