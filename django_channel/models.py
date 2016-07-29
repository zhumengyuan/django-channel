from django.db import models


class ChannelMessage(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    content = models.TextField()
    destroy_time = models.DateTimeField(db_index=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)
