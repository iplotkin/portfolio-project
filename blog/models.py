from django.db import models

# Create a blog model
class Blog(models.Model):
    # title
    title = models.CharField(max_length=300)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to='images/')

# Add the blog app to settings

# Create migration

# Migrate

# Add to admin
