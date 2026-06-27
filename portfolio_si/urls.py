from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("action_status.urls")),
    path("api/", include("afg_health_strategy.urls")),
    path("api/", include("area_coop.urls")),
    path("api/", include("data_source.urls")),
    path("api/", include("framework_funding.urls")),
    path("api/", include("ip_identifier.urls")),
    path("api/", include("list_1_5.urls")),
    path("api/", include("monitoring_technical_performance.urls")),
    path("api/", include("mou_indicators.urls")),
    path("api/", include("organisation_unit.urls")),
    path("api/", include("pop_district.urls")),
    path("api/", include("qualitative_analysis.urls")),
    path("api/", include("reporting.urls")),
    path("api/", include("risk_matrix.urls")),
    path("api/", include("sens.urls")),
    path("api/", include("strategic_alignment.urls")),
    path("api/", include("technical_area.urls")),
]
