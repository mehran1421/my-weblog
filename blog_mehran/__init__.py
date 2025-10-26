from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# Only import celery if not running on Vercel
import os
if not os.environ.get('VERCEL'):
    try:
        from .celery import app as celery_app
        __all__ = ('celery_app',)
    except ImportError:
        # Celery not available (e.g., on Vercel)
        pass
else:
    # Running on Vercel, skip celery import
    pass