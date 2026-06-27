from rest_framework import serializers
from .models import ReportingPeriod, Reporting
from framework_funding.serializers import FrameworkFundingSerializer
from strategic_alignment.serializers import StrategicAlignmentSerializer
from monitoring_technical_performance.serializers import MonitoringAlignmentSerializer
from qualitative_analysis.serializers import QualitativeAnalysisSerializer
from risk_matrix.serializers import RiskMatrixActionPlanSerializer


class ReportingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingPeriod
        fields = "__all__"


class ReportingSerializer(serializers.ModelSerializer):
    framework = FrameworkFundingSerializer(required=False)
    strategic_alignment = StrategicAlignmentSerializer(required=False)
    monitoring_alignment = MonitoringAlignmentSerializer(required=False)
    qualitative_analysis = QualitativeAnalysisSerializer(required=False)
    risk_matrix = RiskMatrixActionPlanSerializer(required=False)

    class Meta:
        model = Reporting
        fields = [
            "id",
            "ip_id",
            "report_period",
            "framework",
            "strategic_alignment",
            "monitoring_alignment",
            "qualitative_analysis",
            "risk_matrix",
        ]

    def _create_or_update_nested(self, instance, nested_data):
        if nested_data.get("framework") is not None:
            data = nested_data["framework"]
            data.pop("reporting", None)
            if hasattr(instance, "framework"):
                for attr, val in data.items():
                    setattr(instance.framework, attr, val)
                instance.framework.save()
            else:
                from framework_funding.models import FrameworkFunding
                FrameworkFunding.objects.create(reporting=instance, **data)

        if nested_data.get("strategic_alignment") is not None:
            data = nested_data["strategic_alignment"]
            data.pop("reporting", None)
            if hasattr(instance, "strategic_alignment"):
                for attr, val in data.items():
                    setattr(instance.strategic_alignment, attr, val)
                instance.strategic_alignment.save()
            else:
                from strategic_alignment.models import StrategicAlignment
                StrategicAlignment.objects.create(reporting=instance, **data)

        if nested_data.get("monitoring_alignment") is not None:
            data = nested_data["monitoring_alignment"]
            data.pop("reporting", None)
            if hasattr(instance, "monitoring_alignment"):
                for attr, val in data.items():
                    setattr(instance.monitoring_alignment, attr, val)
                instance.monitoring_alignment.save()
            else:
                from monitoring_technical_performance.models import MonitoringAlignment
                MonitoringAlignment.objects.create(reporting=instance, **data)

        if nested_data.get("qualitative_analysis") is not None:
            data = nested_data["qualitative_analysis"]
            data.pop("reporting", None)
            if hasattr(instance, "qualitative_analysis"):
                for attr, val in data.items():
                    setattr(instance.qualitative_analysis, attr, val)
                instance.qualitative_analysis.save()
            else:
                from qualitative_analysis.models import QualitativeAnalysis
                QualitativeAnalysis.objects.create(reporting=instance, **data)

        if nested_data.get("risk_matrix") is not None:
            data = nested_data["risk_matrix"]
            data.pop("reporting", None)
            if hasattr(instance, "risk_matrix"):
                for attr, val in data.items():
                    setattr(instance.risk_matrix, attr, val)
                instance.risk_matrix.save()
            else:
                from risk_matrix.models import RiskMatrixActionPlan
                RiskMatrixActionPlan.objects.create(reporting=instance, **data)

    def create(self, validated_data):
        nested_keys = ["framework", "strategic_alignment", "monitoring_alignment", "qualitative_analysis", "risk_matrix"]
        nested_data = {key: validated_data.pop(key, None) for key in nested_keys}
        instance = Reporting.objects.create(**validated_data)
        self._create_or_update_nested(instance, nested_data)
        return instance

    def update(self, instance, validated_data):
        nested_keys = ["framework", "strategic_alignment", "monitoring_alignment", "qualitative_analysis", "risk_matrix"]
        nested_data = {key: validated_data.pop(key, None) for key in nested_keys}
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        self._create_or_update_nested(instance, nested_data)
        return instance
