from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from users.models import User


LANGUAGES = [
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
	('C', 'C'),
	('C#', 'C#'),
]

TAGS = [
    ('METHOD', 'METHOD'),
    ('FUNCTION', 'FUNCTION'),
    ('OPERATOR', 'OPERATOR'),
    ('HELPER FUNCTION', 'HELPER FUNCTION'),

]

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    code = models.TextField()
    libraries = models.ManyToManyField('Library')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name="languages")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE,related_name="tags", null=True, blank=True)
	
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Snippet title: {self.title} Description: {self.description} Code: {self.code} Language: {self.language}'


class Tag(models.Model): 
    name = models.CharField(max_length=100, choices=TAGS, default='code')
    slug = models.CharField(max_length=100, null=False, unique=True, default='code')

    def __str__(self):
        return f'{self.name}'

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            return super().save(*args, **kwargs)
    

class Language(models.Model):
    name = models.CharField(max_length=100, choices=LANGUAGES, default = 'english')
    slug = models.CharField(max_length=50, null=False, unique=True, default=name)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    



class Library(models.Model):
    name = models.CharField(max_length=50, default='my library')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libraries')

    def __str__(self):
        return f'{self.user} {self.name}'
    