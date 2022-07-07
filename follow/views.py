import csv
import zlib
import django
import geopy
import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
import tweepy
import requests
import urllib3
from django.conf import settings

# Create your views here.

from geopy import Nominatim

from follow.models import Calend, Calendly, Streak, Leadfeeder, pipedrive, calpipelead


def home(request, null=None):
    consumer_key = settings.API_KEY
    consumer_secret = settings.API_KEY_SECRET
    access_token = settings.ACCESS_TOKEN
    access_secret = settings.ACCESS_TOKEN_SECRET
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    data = [x._json for x in tweepy.Cursor(api.get_followers, screen_name='Leadfeeder', count=200).items(4400)]
    for x in data:

        ma = Leadfeeder()
        ma.Profile_id = x['id']
        ma.Name = x['name']
        ma.Username = x['screen_name']
        ma.Created_at = x['created_at']
        ma.Url_section_url = x['url']
        try:
            y = x['entities']
            y = y['description']
            qp = []
            for key, val in y.items():
                if val:
                    b = val[0]
                    t = (len(val))
                    try:
                        for y in range(t):
                            p = y
                            # print(p)
                            r = val[p]
                            pp = r['expanded_url']
                            # pp=[pp]
                            # print(pp)
                            qp.append(pp)
                        ma.Description_section_url = qp
                    except IndexError:
                        k = b['expanded_url']
                        ma.Description_section_url = k
                else:
                    ma.Description_section_url = null
        except KeyError:
            ma.Description_section_url = null

        ma.Location = x['location']
        ma.Description = x['description']
        try:
            d = x['status']
            d = d['created_at']
            ma.Status = d

        except KeyError:
            ma.Status = null
        ma.Status_count = x['statuses_count']
        ma.Friends_count = x['friends_count']
        ma.Followers_count = x['followers_count']
        ma.Favourites_count = x['favourites_count']
        ma.Blocked_by = x['blocked_by']
        ma.Blocking = x['blocking']
        ma.Contributors_enabled = x['contributors_enabled']
        ma.Default_profile = x['default_profile']
        ma.Default_profile_image = x['default_profile_image']
        ma.Follow_request_sent = x['follow_request_sent']
        ma.Following = x['following']
        ma.Geo_enabled = x['geo_enabled']
        ma.Has_extended_profile = x['has_extended_profile']
        ma.Profile_id_str = x['id_str']
        ma.Is_translation_enabled = x['is_translation_enabled']
        ma.Is_translator = x['is_translator']
        ma.Listed_count = x['listed_count']
        ma.Live_following = x['live_following']
        ma.Muting = x['muting']
        ma.Notification = x['notifications']
        ma.Profile_background_color = x['profile_background_color']
        ma.Profile_background_image_url = x['profile_background_image_url']
        ma.Profile_background_image_url_https = x['profile_background_image_url_https']
        ma.Profile_background_title = x['profile_background_tile']
        ma.Profile_image_url = x['profile_image_url']
        ma.Profile_image_url_https = x['profile_image_url_https']
        ma.Profile_link_color = x['profile_link_color']
        ma.Profile_slidebar_border_color = x['profile_sidebar_border_color']
        ma.Profile_slidebar_fill_color = x['profile_sidebar_fill_color']
        ma.Profile_text_color = x['profile_text_color']
        ma.Profile_use_background_image = x['profile_use_background_image']
        ma.Protected = x['protected']
        ma.Traslator_type = x['translator_type']
        ma.Verified = x['verified']
        ma.save()
    return render(request, 'fol.html')


def purl(request):
    puu = calpipelead.objects.values('Url_section_url', 'Profile_id')
    puu = list(puu)

    # purl = puu[0]['Url_section_url']
    # print(purl)
    t = len(puu)

    for x in range(t):
        purl = puu[x]['Url_section_url']
        idu = puu[x]['Profile_id']
        print(idu)
        print(purl)
        p = str(purl)
        pu = calpipelead.objects.get(Profile_id=idu)
        p = p.replace(",", "")
        p = p.replace("'", "")
        p = p.replace("(", "")
        p = p.replace(")", "")
        # p=p.replace(',','')
        try:

            r = requests.get(p, allow_redirects=False, timeout=(10, 20))

            try:
                z = r.headers['location']
                print(z)
                pu.Url_section_url = z
                pu.save()
            except KeyError:
                pu.Url_section_url = p
                pu.save()
        except requests.exceptions.ConnectionError:
            pu.Url_section_url = p
            pu.save()
        except requests.exceptions.MissingSchema:
            pu.Url_section_url = p
            pu.save()
        except requests.exceptions.ReadTimeout:
            pu.Url_section_url = p
            pu.save()
        except urllib3.exceptions.ReadTimeoutError:
            pu.Url_section_url = p
            pu.save()
        except TimeoutError:
            pu.Url_section_url = p
            pu.save()
        except UnicodeDecodeError:
            pu.Url_section_url = p
            pu.save()
        except requests.exceptions.ContentDecodingError:
            pu.Url_section_url = p
            pu.save()
        except urllib3.exceptions.DecodeError:
            pu.Url_section_url = p
            pu.save()
        except zlib.error:
            pu.Url_section_url = p
            pu.save()
    return render(request, 'fol.html')


def cur(request):
    puu = calpipelead.objects.values('Location', 'Profile_id')
    puu = list(puu)

    # purl = puu[0]['Url_section_url']
    # print(purl)
    t = len(puu)
    for x in range(t):
        purl = puu[x]['Location']
        idu = puu[x]['Profile_id']

        p = str(purl)
        pu = calpipelead.objects.get(Profile_id=idu)
        # p = p.replace(",", "")
        # p = p.replace("'", "")
        # p = p.replace("(", "")
        # p = p.replace(")", "")
        # print(p)
        if purl is None:
            pu.Location = None
        try:

            geolocator = Nominatim(user_agent="geoapiExercises")
            loc = geolocator.geocode(purl, timeout=20)
            print(loc)
            pu.Location = loc
        except TimeoutError:
            pu.Location = purl
        except urllib3.exceptions.ReadTimeoutError:
            pu.Location = purl
        except urllib3.exceptions.MaxRetryError:
            pu.Location = purl
        except requests.exceptions.ConnectionError:
            pu.Location = purl
        except geopy.exc.GeocoderUnavailable:
            pu.Location = purl
    return render(request, 'fol.html')


def durl(request):
    puu = calpipelead.objects.values('Description_section_url', 'Profile_id')
    puz = list(puu)
    # p = pu['Description_section_url']
    # print(p)
    t = len(puu)
    print(t)

    for x in range(t):
        try:
            z = []
            purl = puz[x]['Description_section_url']
            idu = puz[x]['Profile_id']
            pu = calpipelead.objects.get(Profile_id=idu)

            if purl is None:
                print('no')

            else:
                p = purl
                p = p.replace(" ", "")
                p = p.replace("'", "")
                p = p.replace("[", "")
                p = p.replace("]", "")
                h = p.split(',')
                n = list(h)

                j = len(n)
                # print(j)
                print(n)
                for f in range(j):

                    k = (n[f])
                    try:

                        r = requests.get(k, allow_redirects=False, timeout=(10, 20))

                        try:
                            z.append(r.headers['location'])
                            print(z)
                            pu.Description_section_url = z
                            pu.save()

                        except KeyError:
                            pu.Description_section_url = n

                            pu.save()
                    except requests.exceptions.ConnectionError:
                        pu.Description_section_url = n
                        pu.save()
                    except requests.exceptions.MissingSchema:
                        pu.Description_section_url = n
                        pu.save()
                    except requests.exceptions.ReadTimeout:
                        pu.Description_section_url = n
                        pu.save()
                    except urllib3.exceptions.ReadTimeoutError:
                        pu.Description_section_url = n
                        pu.save()
                    except TimeoutError:
                        pu.Description_section_url = n
                        pu.save()
                    except UnicodeDecodeError:
                        pu.Description_section_url = n
                        pu.save()
                    except requests.exceptions.ContentDecodingError:
                        pu.Description_section_url = n
                        pu.save()
                    except urllib3.exceptions.DecodeError:
                        pu.Description_section_url = n
                        pu.save()
                    except zlib.error:
                        pu.Description_section_url = n
                        pu.save()
                    except psycopg2.errors.StringDataRightTruncation:
                        pu.Description_section_url = n
                        pu.save()
                    except django.db.utils.DataError:
                        pu.Description_section_url = n
                        pu.save()

        except TypeError:
            print('noz')
    return render(request, 'fol.html')


def comp(request):
    pu = Calendly.objects.values('Profile_id')
    puu = list(pu)
    jj = Leadfeeder.objects.values('Profile_id')
    zuu = list(jj)
    kk = pipedrive.objects.values('Profile_id')
    yuu = list(kk)
    t = (len(puu))
    g = (len(zuu))
    o = (len(yuu))
    for x in range(t):
        ab = puu[x]['Profile_id']
        for y in range(g):
            ac = zuu[y]['Profile_id']
            if ab == ac:
                for r in range(o):
                    ad = yuu[r]['Profile_id']
                    if ab == ad:
                        print(ab)
                        mb = Calendly.objects.get(Profile_id=ab)
                        ma = calpipelead()
                        ma.Profile_id = mb.Profile_id
                        ma.Name = mb.Name
                        ma.Username = mb.Username
                        ma.Created_at = mb.Created_at
                        ma.Url_section_url = mb.Url_section_url
                        ma.Description_section_url = mb.Description_section_url
                        ma.Location = mb.Location
                        ma.Description = mb.Description
                        ma.Status = mb.Status
                        ma.Status_count = mb.Status_count
                        ma.Friends_count = mb.Friends_count
                        ma.Followers_count = mb.Followers_count
                        ma.Favourites_count = mb.Favourites_count
                        ma.Blocked_by = mb.Blocked_by
                        ma.Blocking = mb.Blocking
                        ma.Contributors_enabled = mb.Contributors_enabled
                        ma.Default_profile = mb.Default_profile
                        ma.Default_profile_image = mb.Default_profile_image
                        ma.Follow_request_sent = mb.Follow_request_sent
                        ma.Following = mb.Following
                        ma.Geo_enabled = mb.Geo_enabled
                        ma.Has_extended_profile = mb.Has_extended_profile
                        ma.Profile_id_str = mb.Profile_id_str
                        ma.Is_translation_enabled = mb.Is_translation_enabled
                        ma.Is_translator = mb.Is_translator
                        ma.Listed_count = mb.Listed_count
                        ma.Live_following = mb.Live_following
                        ma.Muting = mb.Muting
                        ma.Notification = mb.Notification
                        ma.Profile_background_color = mb.Profile_background_color
                        ma.Profile_background_image_url = mb.Profile_background_image_url
                        ma.Profile_background_image_url_https = mb.Profile_background_image_url_https
                        ma.Profile_background_title = mb.Profile_background_title
                        ma.Profile_image_url = mb.Profile_image_url
                        ma.Profile_image_url_https = mb.Profile_image_url_https
                        ma.Profile_link_color = mb.Profile_link_color
                        ma.Profile_slidebar_border_color = mb.Profile_slidebar_border_color
                        ma.Profile_slidebar_fill_color = mb.Profile_slidebar_fill_color
                        ma.Profile_text_color = mb.Profile_text_color
                        ma.Profile_use_background_image = mb.Profile_use_background_image
                        ma.Protected = mb.Protected
                        ma.Traslator_type = mb.Traslator_type
                        ma.Verified = mb.Verified
                        ma.save()
    return render(request, 'fol.html')


def csvs(request):
    ma = calpipelead.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=F.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['ID', 'Profile_id', 'Name', 'Username', 'Created_at', 'Url_section_url', 'Description_section_url', 'Location',
         'Description', 'Status', 'Status_count', 'Friends_count', 'Followers_count', 'Favourites_count', 'Blocked_by',
         'Blocking', 'Contributors_enabled', 'Follow_request_sent', 'Following', 'Profile_id_str', 'Listed_count',
         'Live_following', 'Notification', 'Protected', 'Traslator_type', 'Verified'])
    studs = ma.values_list('id', 'Profile_id', 'Name', 'Username', 'Created_at', 'Url_section_url',
                           'Description_section_url', 'Location', 'Description', 'Status', 'Status_count',
                           'Friends_count', 'Followers_count', 'Favourites_count', 'Blocked_by', 'Blocking',
                           'Contributors_enabled', 'Follow_request_sent', 'Following', 'Profile_id_str', 'Listed_count',
                           'Live_following', 'Notification', 'Protected', 'Traslator_type', 'Verified')
    for std in studs:
        writer.writerow(std)
    return response
