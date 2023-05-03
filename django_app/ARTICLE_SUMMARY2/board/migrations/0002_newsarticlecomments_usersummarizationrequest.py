# Generated by Django 3.2.18 on 2023-05-03 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticleComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('content', models.CharField(blank=True, max_length=300, null=True)),
                ('sympathycount', models.IntegerField(db_column='sympathyCount')),
                ('antipathycount', models.IntegerField(db_column='antipathyCount')),
            ],
            options={
                'db_table': 'news_article_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSummarizationRequest',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.myuser')),
                ('userid', models.IntegerField(unique=True)),
                ('url', models.CharField(max_length=100)),
                ('request_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_summarization_request',
                'managed': False,
            },
        ),
    ]
