# Generated by Django 4.2.6 on 2023-10-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=500, null=True)),
                ('intensity', models.CharField(blank=True, max_length=500, null=True)),
                ('sector', models.CharField(blank=True, max_length=500, null=True)),
                ('topic', models.CharField(blank=True, max_length=500, null=True)),
                ('insight', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('region', models.CharField(blank=True, max_length=500, null=True)),
                ('start_year', models.CharField(blank=True, max_length=500, null=True)),
                ('impact', models.CharField(blank=True, max_length=500, null=True)),
                ('added', models.CharField(blank=True, max_length=500, null=True)),
                ('published', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('relevance', models.CharField(blank=True, max_length=500, null=True)),
                ('pestle', models.CharField(blank=True, max_length=500, null=True)),
                ('source', models.CharField(blank=True, max_length=500, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('likelihood', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
