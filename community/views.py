import json
import requests
from urllib import parse, request
from os import close
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse

from community.models import EnlacesAPI, Community_info

from urllib import parse, request


class SearchPrivate(TemplateView):
    template_name = 'searchchannel.html'

    def get_context_data(self, **kwargs):
        context = super(SearchPrivate, self).get_context_data(**kwargs)
        context = {}
        buscador = self.kwargs.get('name')
        context['name'] = self.kwargs.get('name')

        url_link = 'https://youtube.googleapis.com/youtube/v3/search'
        part = 'snippet'
        maxResults = 10
        q = buscador
        key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'
#
        url = requests.get(
            f'{url_link}?part={part}&maxResults={maxResults}&q={q}&type=channel&type=playlist&key={key}')
        api = url.json()
        items = api['items']
        #context = dict(items)
        prueba = {
            'items': items
        }

        context = prueba
        print(context)
        return context


class YoutubeView(TemplateView):
    template_name = 'youtube.html'
    api_key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        url_link = 'https://youtube.googleapis.com/youtube/v3/search'
        url_linkPlayList = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
        part = 'snippet'
        maxResults = 2
        q = 'Programación ATS'
        channelId = 'UC7QoKU6bj1QbXQuNIjan82Q'
        #playlistId = 'PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj'
        type = 'playlist'
        key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

        #urlPLaylist = f'{url_linkPlayList}?part={part}&playlistId={playlistId}&key={key}'

        url = requests.get(
            f'{url_link}?part={part}&channelId={channelId}&maxResults={maxResults}&q={q}&type={type}&key={key}')
        api = url.json()
        items = api['items']
        context['data'] = api
        context['items'] = items

        for i in items:
            ides = i['id']
            playlistId = ides['playlistId']
            title = i['snippet']
            channelTitle = title['channelTitle']
            print(playlistId)

        context['snippet'] = title
        context['channelTitle'] = channelTitle
        context['id'] = ides
        context['playlistId'] = playlistId

        context = self.channelData()
        return {'context': context}

    def channelData(self):
        url_link = 'https://youtube.googleapis.com/youtube/v3/search'

        CHANNEL_NAME = 'Programación ATS'

        params_channel = {
            'key': self.api_key,
            'part': 'snippet',
            'q': CHANNEL_NAME,
            'type': 'channel',
            'maxResults': 2
        }
        url_values = parse.urlencode(params_channel)
        with request.urlopen(url_link + '?' + url_values) as response:
            json_response = json.loads(response.read())
        channel_items = json_response['items']

        channels = []
        channel_ids = []

        for channel_item in channel_items:
            channel_id = channel_item['snippet']['channelId']
            channel = {
                'id': channel_item['snippet']['channelId'],
                'title': channel_item['snippet']['title'],
                'description': channel_item['snippet']['description'],
                'image': channel_item['snippet']['thumbnails']['default']['url'],
                'playlists': []
            }
            print(channel_id)
            playlist_data = self.playlistData(channel_id)
            channel['playlists'] = playlist_data
            channels.append(channel)

        return channels

    def playlistData(self, channel_id):
        url_linkPlayList = 'https://youtube.googleapis.com/youtube/v3/playlists'
        api_key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

        params_playlist = {
            'key': api_key,
            'part': 'snippet',
            'channelId': channel_id,
            'maxResults': 3
        }
        url_values = parse.urlencode(params_playlist)
        with request.urlopen(url_linkPlayList + '?' + url_values) as response:
            json_response = json.loads(response.read())
        playlists_items = json_response['items']

        playlists = []

        for playlists_item in playlists_items:
            playlist = {
                'id': playlists_item['id'],
                'title': playlists_item['snippet']['title'],
                'publishedAt': playlists_item['snippet']['publishedAt'],
                'image': playlists_item['snippet']['thumbnails']['default']['url']
            }
            playlists.append(playlist)

        return playlists


class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context


class ChannelYTView(TemplateView):
    template_name = 'channelYoutube.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        with open('community/channels.json', 'r') as f:
            context['channel'] = json.load(f)
            print(context)
            return context
