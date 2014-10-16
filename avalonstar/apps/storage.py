# -*- coding: utf-8 -*-
from django.contrib.staticfiles.storage import ManifestFilesMixin

from storages.backends.s3boto import S3BotoStorage


class ManifestStaticS3Storage(ManifestFilesMixin, S3BotoStorage):
    pass
