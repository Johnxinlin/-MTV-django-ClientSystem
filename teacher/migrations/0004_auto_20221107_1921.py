# Generated by Django 3.2.16 on 2022-11-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_student_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
