from django.db import models

from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    usage = models.TextField()
    description = models.TextField(null=True, blank=True)  # Allow null values
    symptoms = models.TextField()  # ✅ Ensure symptoms field exists

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
