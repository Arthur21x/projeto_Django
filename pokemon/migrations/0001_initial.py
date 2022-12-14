# Generated by Django 4.1.4 on 2022-12-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonAbilitis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ability1', models.CharField(max_length=255)),
                ('Ability2', models.CharField(blank=True, max_length=255)),
                ('Ability3', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Evolution1', models.CharField(max_length=255)),
                ('Evolution2', models.CharField(blank=True, max_length=255)),
                ('Evolution3', models.CharField(blank=True, max_length=255)),
                ('Evolution4', models.CharField(blank=True, max_length=255)),
                ('Evolution5', models.CharField(blank=True, max_length=255)),
                ('Evolution6', models.CharField(blank=True, max_length=255)),
                ('Evolution7', models.CharField(blank=True, max_length=255)),
                ('Evolution8', models.CharField(blank=True, max_length=255)),
                ('Evolution9', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonSprite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_default', models.CharField(max_length=255)),
                ('shiny', models.CharField(max_length=255)),
                ('front_shiny', models.CharField(max_length=255)),
                ('front_default', models.CharField(max_length=255)),
                ('dream_world', models.CharField(max_length=255)),
                ('official_artwork', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type1', models.CharField(max_length=255)),
                ('Type2', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('Ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ability', to='pokemon.pokemonabilitis')),
                ('Evolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolution', to='pokemon.pokemonsprite')),
                ('Sprite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprite', to='pokemon.pokemonsprite')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='pokemon.pokemontype')),
            ],
        ),
    ]
