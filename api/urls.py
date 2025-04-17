from django.urls import path
from .views import SwiftRetrieveDestroyAPIView, SwiftCreateAPIView, SwiftCodesListForCountryAPIView

urlpatterns = [
    path("swift-codes/<str:swift_code>", SwiftRetrieveDestroyAPIView.as_view(), name="swift_code_detail"),
    path("swift-codes", SwiftCreateAPIView.as_view(), name="swift_code_create"),
    path("swift-codes/country/<str:country_iso_2>", SwiftCodesListForCountryAPIView.as_view(), name="swif_codes_for_country"),
]