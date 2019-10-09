from django.db import models
from django.urls import reverse

class Event(models.Model):
	scheduledDate = models.DateField()
	eventName = models.CharField(max_length=200)
	startTime = models.TimeField()
	endTime = models.TimeField()

	def __str__(self):
		return self.eventName

	def get_absolute_url(self):
		return reverse('event:event_edit', kwargs={'pk': self.pk})
