# Generated by Django 3.2 on 2022-02-09 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_classmodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classmodel',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.lessonmodel', verbose_name='کلاسهای دروس'),
        ),
    ]