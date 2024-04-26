# Generated by Django 5.0.4 on 2024-04-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_finch_description_alter_finch_habitat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(choices=[('Mating Song', 'Mating Song'), ('Warbling Song', 'Warbling Song'), ('Territory Song', 'Territory Song')], default='Mating Song', max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
        migrations.AlterField(
            model_name='finch',
            name='habitat',
            field=models.CharField(choices=[('Woodlands', 'Woodlands'), ('Mountains', 'Mountains'), ('Deserts', 'Deserts'), ('Unknown', 'Unknown')], max_length=100),
        ),
        migrations.AlterField(
            model_name='finch',
            name='subfamily',
            field=models.CharField(choices=[('Fringillinae', 'Fringillinae'), ('Carduelinae', 'Carduelinae'), ('Euphoniinae', 'Euphoniinae'), ('Unknown', 'Unknown')], max_length=100),
        ),
        migrations.AddField(
            model_name='finch',
            name='songs',
            field=models.ManyToManyField(to='main_app.song'),
        ),
    ]
