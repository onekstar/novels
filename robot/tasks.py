#coding:utf-8
from novels import celery_app

@celery_app.task(bind=True)
def parse_catalog(self):
    import time
    time.sleep(3)
    return 'accept {}'.format(self.request.id)

