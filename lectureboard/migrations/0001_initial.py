# Generated by Django 3.2.12 on 2022-05-21 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lectureB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('titleL', models.CharField(choices=[('미선택', '미선택'), ('고전역학', '고전역학'), ('응용물리탐구', '응용물리탐구'), ('프로그래밍', '프로그래밍'), ('수학세미나', '수학세미나'), ('통합수학', '통합수학'), ('에너지환경과학', '에너지환경과학')], max_length=200)),
                ('titleT', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectureboard.lectureb')),
            ],
        ),
    ]
