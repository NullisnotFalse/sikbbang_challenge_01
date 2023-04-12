# Generated by Django 4.2 on 2023-04-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mypage_test', models.ManyToManyField(blank=True, related_name='tests', to='testapp.testapp')),
            ],
            options={
                'db_table': 'my_page',
            },
        ),
    ]