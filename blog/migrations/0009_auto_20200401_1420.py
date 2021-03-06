# Generated by Django 3.0.4 on 2020-04-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='priority',
            field=models.CharField(choices=[('4 - Low', '4 - Low'), ('3 - Averege', '3 - Averege'), ('2 - High', '2 - High'), ('1 - Critical', '1 - Critical')], default='Priority 4', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Work in progress', 'Work in progress'), ('Pending customer', 'Pending customer'), ('Pending vendor', 'Pending vendor'), ('Closed', 'Closed')], default='In Progress', max_length=50),
        ),
    ]
