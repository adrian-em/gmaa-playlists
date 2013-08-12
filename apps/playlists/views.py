from django.shortcuts import render_to_response
from apps.playlists.models import Genre, Playlist, UserProfile
from apps.playlists.forms import PlaylistForm, FilterForm
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson


def index_page(request):
    """
    Index
    """
    try:
        profile = UserProfile.objects.get(user=request.user)
        favorites = profile.favorites.all()
    except TypeError:
        favorites = {}
    playlists_objects = Playlist.objects.all().order_by('-id')
    paginator = Paginator(playlists_objects, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        playlists = paginator.page(page)
    except (EmptyPage, InvalidPage):
        playlists = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'playlists': playlists,
                                             'favorites': favorites},
                              RequestContext(request))


def add_playlist_form(request):
    if request.method == "POST":
        playlist_form = PlaylistForm(request.POST)
        if playlist_form.is_valid():

            form = playlist_form.save(commit=False)
            form.user = request.user
            form.save()
            playlist_form.save_m2m()
            return HttpResponseRedirect('/')
    else:
        playlist_form = PlaylistForm()

    return render_to_response('addplaylist.html',
                              {'playlist_form': playlist_form},
                              RequestContext(request))


def user_playlists_page(request):

    playlists_objects = Playlist.objects.filter(user=request.user).order_by(
        '-id')
    paginator = Paginator(playlists_objects, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        playlists = paginator.page(page)
    except (EmptyPage, InvalidPage):
        playlists = paginator.page(paginator.num_pages)


    return render_to_response('user_playlists.html', {'playlists': playlists},
                              RequestContext(request))


def favorites_playlists_page(request):

    profile = UserProfile.objects.get(user=request.user)
    playlists_objects = profile.favorites.all().order_by('-id')
    paginator = Paginator(playlists_objects, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        playlists = paginator.page(page)
    except (EmptyPage, InvalidPage):
        playlists = paginator.page(paginator.num_pages)

    return render_to_response('favorite_playlists.html', {'playlists': playlists},
                              RequestContext(request))


@csrf_exempt
def favorite_unfavorite_playlist(request, fav, playlistid):

    print request.method
    if request.method == "POST":
        userprofile = UserProfile.objects.get(user=request.user)
        playlist = Playlist.objects.get(id=playlistid)
        if fav == 'add':
            userprofile.favorites.add(playlist)
        elif fav == 'remove':
            userprofile.favorites.remove(playlist)
        resp = simplejson.dumps(fav)
        return HttpResponse(resp, mimetype='application/json')


@csrf_exempt
def delete_playlist(request, playlistid):

    if request.method == "POST":
        playlist = Playlist.objects.get(id=playlistid)
        if playlist.user.id == request.user.id:
            playlist.delete()
            return HttpResponse('Deleted')
        else:
            return HttpResponse(status=403)


def browse_page(request):

    form = FilterForm()

    return render_to_response('browse.html', {'form': form},
                              RequestContext(request))


@csrf_exempt
def filter_page(request):

    if request.method == "POST":
        print request.POST
        try:
            profile = UserProfile.objects.get(user=request.user)
            favorites = profile.favorites.all()
        except TypeError:
            favorites = {}
        playlists_objects = Playlist.objects.filter(genre=int(request
        .POST['genre']))\
            .order_by(
            '-id')
        paginator = Paginator(playlists_objects, 9)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            playlists = paginator.page(page)
        except (EmptyPage, InvalidPage):
            playlists = paginator.page(paginator.num_pages)

        return render_to_response('filtered.html', {'playlists': playlists,
                                                 'favorites': favorites},
                                  RequestContext(request))





