# Generated by Django 4.0.6 on 2022-07-22 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('correct_choice', models.IntegerField(default=0)),
                ('question_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=400)),
                ('correct_choice', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='javna_uprava_vss_brcko.question')),
            ],
        ),
    ]