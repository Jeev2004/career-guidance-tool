# Generated by Django 4.2.5 on 2023-09-22 20:23

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
            name='cs1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_base', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_architecture', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cyber_security', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networking', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_development', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ai_ml', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphics_designer', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cs8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_science', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Default Author', max_length=100)),
                ('Circuit_Design', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab_View', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Control_Systems', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Power_Electronics', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Analog_Communication', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_F', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_P_P', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Electrical_System', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_A_D', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_C_B', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
