# Generated by Django 3.1.6 on 2022-02-10 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_auto_20220210_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses_app.category'),
        ),
        migrations.AlterField(
            model_name='courseimage',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_images', to='courses_app.course'),
        ),
        migrations.AlterField(
            model_name='courseinstructor',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instructors', to='courses_app.insturctor'),
        ),
        migrations.AlterField(
            model_name='coursevideo',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_videos', to='courses_app.course'),
        ),
    ]
