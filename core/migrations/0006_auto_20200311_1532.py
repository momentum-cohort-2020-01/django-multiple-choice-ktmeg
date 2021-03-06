# Generated by Django 3.0.4 on 2020-03-11 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_snippet_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='core.Language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snippet',
            name='tag',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='core.Tag'),
            preserve_default=False,
        ),
    ]
