from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return self.title
	
	def summary(self):
		return self.body[:100]
		
	def pub_date_mo_yr(self):
		return self.pub_date.strftime('%B %e, %Y')

# Create a Blog Model
	# title
	# pub_date
	# body (blog text)
	# image
	
# Add the Blog app to the settings file
	
# Create a migration
	
# Do the Migrate
	
# Add the model to the admin file
