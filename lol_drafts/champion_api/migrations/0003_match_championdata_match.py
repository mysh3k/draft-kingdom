# Generated by Django 4.0.4 on 2023-10-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('champion_api', '0002_remove_championdata_match_delete_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_str', models.CharField(max_length=64)),
                ('data_version', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='championdata',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='champion_api.match'),
            preserve_default=False,
        ),
    ]
