# Generated by Django 4.0.4 on 2022-04-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_id', models.CharField(max_length=256)),
                ('Name', models.CharField(max_length=256)),
                ('Username', models.CharField(max_length=256)),
                ('Created_at', models.CharField(max_length=256)),
                ('Url_section_url', models.CharField(max_length=256)),
                ('Description_section_url', models.CharField(max_length=256)),
                ('Location', models.CharField(max_length=256)),
                ('Description', models.TextField(max_length=700)),
                ('Status', models.CharField(max_length=256)),
                ('Status_count', models.CharField(max_length=256)),
                ('Friends_count', models.CharField(max_length=256)),
                ('Followers_count', models.CharField(max_length=256)),
                ('Favourites_count', models.CharField(max_length=256)),
                ('Blocked_by', models.BooleanField(max_length=256)),
                ('Blocking', models.BooleanField(max_length=256)),
                ('Contributors_enabled', models.BooleanField(max_length=256)),
                ('Default_profile', models.BooleanField(max_length=256)),
                ('Default_profile_image', models.BooleanField(max_length=256)),
                ('Follow_request_sent', models.BooleanField(max_length=256)),
                ('Following', models.BooleanField(max_length=256)),
                ('Geo_enabled', models.BooleanField(max_length=256)),
                ('Has_extended_profile', models.BooleanField(max_length=256)),
                ('Profile_id_str', models.CharField(max_length=256)),
                ('Is_translation_enabled', models.BooleanField(max_length=256)),
                ('Is_translator', models.BooleanField(max_length=256)),
                ('Listed_count', models.CharField(max_length=256)),
                ('Live_following', models.BooleanField(max_length=256)),
                ('Muting', models.BooleanField(max_length=256)),
                ('Notification', models.BooleanField(max_length=256)),
                ('Profile_background_color', models.CharField(max_length=256)),
                ('Profile_background_image_url', models.CharField(max_length=256)),
                ('Profile_background_image_url_https', models.CharField(max_length=256)),
                ('Profile_background_title', models.BooleanField(max_length=256)),
                ('Profile_image_url', models.CharField(max_length=256)),
                ('Profile_image_url_https', models.CharField(max_length=256)),
                ('Profile_link_color', models.CharField(max_length=256)),
                ('Profile_slidebar_border_color', models.CharField(max_length=256)),
                ('Profile_slidebar_fill_color', models.CharField(max_length=256)),
                ('Profile_text_color', models.CharField(max_length=256)),
                ('Profile_use_background_image', models.BooleanField(max_length=256)),
                ('Protected', models.BooleanField(max_length=256)),
                ('Traslator_type', models.CharField(max_length=256)),
                ('Verified', models.BooleanField(max_length=256)),
            ],
        ),
    ]
