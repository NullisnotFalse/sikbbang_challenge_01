# Generated by Django 4.2 on 2023-04-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chellenge_title', models.CharField(max_length=50)),
                ('challenge_name', models.CharField(max_length=50)),
                ('challenge_genre', models.CharField(max_length=50)),
                ('challenge_content', models.TextField()),
                ('challenge_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('challenge_created_at', models.DateTimeField(auto_now_add=True)),
                ('challenge_updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'challenges',
            },
        ),
    ]