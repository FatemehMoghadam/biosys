from __future__ import absolute_import, unicode_literals, print_function, division

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_bulk import ListBulkCreateAPIView
from dry_rest_permissions.generics import DRYPermissions

from main import models
from main.api import serializers


class BulkModelViewSet(
    ListBulkCreateAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """ A model ViewSet that allows the bulk creation of object through list
    """
    pass


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, DRYPermissions)
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'title',)


class SiteViewSet(BulkModelViewSet):
    permission_classes = (IsAuthenticated, DRYPermissions)
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'code')


class DatasetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, DRYPermissions)
    queryset = models.Dataset.objects.all()
    serializer_class = serializers.DatasetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'project')


class GenericRecordViewSet(BulkModelViewSet):
    permission_classes = (IsAuthenticated, DRYPermissions)
    queryset = models.GenericRecord.objects.all()
    serializer_class = serializers.GenericRecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'site', 'dataset__id', 'dataset__name')


class ObservationViewSet(GenericRecordViewSet):
    queryset = models.Observation.objects.all()
    serializer_class = serializers.ObservationSerializer
    filter_fields = GenericRecordViewSet.filter_fields + ('datetime',)


class SpeciesObservationViewSet(ObservationViewSet):
    queryset = models.SpeciesObservation.objects.all()
    serializer_class = serializers.SpeciesObservationSerializer
    filter_fields = ObservationViewSet.filter_fields + ('input_name', 'name_id',)
