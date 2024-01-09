# Generated by Django 4.1 on 2022-08-15 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_quesmodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200, null=True)),
                ('rightans', models.IntegerField()),
                ('wrongans', models.IntegerField()),
                ('no_of_attempt', models.IntegerField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quesmodel')),
            ],
        ),
    ]