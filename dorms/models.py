from django.db import models
from django.contrib.auth.models import User

class Dorm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.CharField(max_length=50)  # e.g., single, double
    size = models.CharField(max_length=50)  # Room dimensions
    image_url = models.ImageField(upload_to='room_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.room_type} in {self.dorm.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()  # 1-5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.room}"
