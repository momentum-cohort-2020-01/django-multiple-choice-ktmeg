from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

Languages = (
	('CSS', 'CSS'),
	('HTML', 'HTML'),
	('JSON', 'JSON'),
	('AJAX', 'AJAX'),
	('JavaScript', 'JavaScript'),
	('Python', 'Python'),
	('Django', 'Django'),
	('Java', 'Java'),
	('React', 'React'),
	('Ruby', 'Ruby'),
	('.Net', '.Net'),
	('C', 'C')
	('C#', 'C#')


)

class Snippet
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	code = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	language = models.ForeignKey(
  		'Language', on_delete=models.SET_NULL, null=True, blank=True)
	
	def __str__)self:
		return f'Snippet title: {self.title} Description: {self.description} Code: {self.code} Language: {self.language}

	class Meta:
		ordering = ['-created_at']


class Tag 

class Library 