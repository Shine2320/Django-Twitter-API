# Generated by Django 4.0.4 on 2022-05-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0004_streak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadfeeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_id', models.CharField(blank=True, max_length=256, null=True)),
                ('Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Username', models.CharField(blank=True, max_length=256, null=True)),
                ('Created_at', models.CharField(blank=True, max_length=256, null=True)),
                ('Url_section_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Description_section_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Location', models.CharField(blank=True, max_length=256, null=True)),
                ('Description', models.TextField(blank=True, max_length=700, null=True)),
                ('Status', models.CharField(blank=True, max_length=256, null=True)),
                ('Status_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Friends_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Followers_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Favourites_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Blocked_by', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Blocking', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Contributors_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Default_profile', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Default_profile_image', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Follow_request_sent', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Following', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Geo_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Has_extended_profile', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_id_str', models.CharField(blank=True, max_length=256, null=True)),
                ('Is_translation_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Is_translator', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Listed_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Live_following', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Muting', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Notification', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_background_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_image_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_image_url_https', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_title', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_image_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_image_url_https', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_link_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_slidebar_border_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_slidebar_fill_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_text_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_use_background_image', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Protected', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Traslator_type', models.CharField(blank=True, max_length=256, null=True)),
                ('Verified', models.BooleanField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pipedrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_id', models.CharField(blank=True, max_length=256, null=True)),
                ('Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Username', models.CharField(blank=True, max_length=256, null=True)),
                ('Created_at', models.CharField(blank=True, max_length=256, null=True)),
                ('Url_section_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Description_section_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Location', models.CharField(blank=True, max_length=256, null=True)),
                ('Description', models.TextField(blank=True, max_length=700, null=True)),
                ('Status', models.CharField(blank=True, max_length=256, null=True)),
                ('Status_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Friends_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Followers_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Favourites_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Blocked_by', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Blocking', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Contributors_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Default_profile', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Default_profile_image', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Follow_request_sent', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Following', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Geo_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Has_extended_profile', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_id_str', models.CharField(blank=True, max_length=256, null=True)),
                ('Is_translation_enabled', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Is_translator', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Listed_count', models.CharField(blank=True, max_length=256, null=True)),
                ('Live_following', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Muting', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Notification', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_background_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_image_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_image_url_https', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_background_title', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Profile_image_url', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_image_url_https', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_link_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_slidebar_border_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_slidebar_fill_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_text_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Profile_use_background_image', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Protected', models.BooleanField(blank=True, max_length=256, null=True)),
                ('Traslator_type', models.CharField(blank=True, max_length=256, null=True)),
                ('Verified', models.BooleanField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='cal',
        ),
        migrations.AlterField(
            model_name='calend',
            name='Blocked_by',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Blocking',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Contributors_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Created_at',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Default_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Default_profile_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Description',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Description_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Favourites_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Follow_request_sent',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Followers_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Friends_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Geo_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Has_extended_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Is_translation_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Is_translator',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Listed_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Live_following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Muting',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Notification',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_background_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_background_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_background_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_background_title',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_id_str',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_link_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_slidebar_border_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_slidebar_fill_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_text_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Profile_use_background_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Protected',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Status_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Traslator_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Url_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Username',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calend',
            name='Verified',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Blocked_by',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Blocking',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Contributors_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Created_at',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Default_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Default_profile_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Description',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Description_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Favourites_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Follow_request_sent',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Followers_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Friends_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Geo_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Has_extended_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Is_translation_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Is_translator',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Listed_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Live_following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Muting',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Notification',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_background_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_background_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_background_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_background_title',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_id_str',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_link_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_slidebar_border_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_slidebar_fill_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_text_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Profile_use_background_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Protected',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Status_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Traslator_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Url_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Username',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='calendly',
            name='Verified',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Blocked_by',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Blocking',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Contributors_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Created_at',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Default_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Default_profile_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Description',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Description_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Favourites_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Follow_request_sent',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Followers_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Friends_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Geo_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Has_extended_profile',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Is_translation_enabled',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Is_translator',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Listed_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Live_following',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Muting',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Notification',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_background_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_background_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_background_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_background_title',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_id_str',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_image_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_image_url_https',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_link_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_slidebar_border_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_slidebar_fill_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_text_color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Profile_use_background_image',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Protected',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Status_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Traslator_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Url_section_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Username',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='streak',
            name='Verified',
            field=models.BooleanField(blank=True, max_length=256, null=True),
        ),
    ]
