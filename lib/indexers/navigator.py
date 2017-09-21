# -*- coding: utf-8 -*-

'''
    antares Add-on
    Copyright (C) 2016 antares

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt


sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[B][COLOR ffff0000]TOP MOVIES[/COLOR][/B]', 'playlistNavigator', 'top.png', 'DefaultMovies.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLISTS[/COLOR][/B]', 'customNavigator', 'playlist.png', 'DefaultMovies.png')

        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')

        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYears', 'years.png', 'DefaultMovies.png')
        self.addDirectoryItem('[B][COLOR ffff0000]ACTOR[/COLOR][/B]', 'moviePersons', 'actor.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[B][COLOR ffff0000]BY DIRECTORS[/COLOR][/B]', 'spikeNavigator', 'director.png', 'DefaultMovies.png')
		
        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem('[B][COLOR ffff0000]ACTOR SEARCH[/COLOR][/B]', 'moviePerson', 'actorsearch.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'mymovies.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem('[B][COLOR ffff0000]ACTOR SEARCH[/COLOR][/B]', 'moviePerson', 'actorsearch.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem('[B][COLOR ffff0000]ACTOR SEARCH[/COLOR][/B]', 'tvPerson', 'actorsearch.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'mytvshows.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'mytvshows.png', 'DefaultTVShows.png')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem('[B][COLOR ffff0000]ACTOR SEARCH[/COLOR][/B]', 'tvPerson', 'actorsearch.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()

		
    def custom(self, lite=False):		
	
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*1', 'movies&url=anime', '01.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*2', 'movies&url=avant', '02.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*3', 'movies&url=true', '03.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*4', 'movies&url=biker', '04.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*5', 'movies&url=bmovie', '05.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*6', 'movies&url=breaking', '06.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*7', 'movies&url=business', '07.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*8', 'movies&url=caper', '08.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*9', 'movies&url=car', '09.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*10', 'movies&url=char', '10.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*11', 'movies&url=chick', '11.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*12', 'movies&url=coming', '12.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*13', 'movies&url=competition', '13.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*14', 'movies&url=cult', '14.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*15', 'movies&url=cyber', '15.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*16', 'movies&url=drugs', '16.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*17', 'movies&url=dystopia', '17.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*18', 'movies&url=epic', '18.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*19', 'movies&url=espionage', '19.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*20', 'movies&url=expiremental', '20.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*21', 'movies&url=Existential', '21.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*22', 'movies&url=fairytale', '22.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*23', 'movies&url=farce', '23.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*24', 'movies&url=femme', '24.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*25', 'movies&url=futuristic', '25.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*26', 'movies&url=heist', '26.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*27', 'movies&url=highschool', '27.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*28', 'movies&url=remakes', '28.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*29', 'movies&url=bond', '29.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*30', 'movies&url=kidnapped', '30.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*31', 'movies&url=kungfu', '31.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*32', 'movies&url=monster', '32.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*33', 'movies&url=box', '33.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*34', 'movies&url=loners', '34.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*35', 'movies&url=racist', '35.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*36', 'movies&url=neo', '36.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*37', 'movies&url=parenthood', '37.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*38', 'movies&url=parody', '38.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*39', 'movies&url=apocalypse', '39.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*40', 'movies&url=private', '40.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*41', 'movies&url=remake', '41.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*42', 'movies&url=road', '42.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*43', 'movies&url=robot', '43.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*44', 'movies&url=satire', '44.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*45', 'movies&url=schiz', '45.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*46', 'movies&url=serial', '46.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*47', 'movies&url=slasher', '47.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*48', 'movies&url=sleeper', '48.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*49', 'movies&url=spiritual', '49.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*50', 'movies&url=spoof', '50.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*51', 'movies&url=star', '51.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*52', 'movies&url=steampunk', '52.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*53', 'movies&url=superhero', '53.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*54', 'movies&url=supernatural', '54.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*55', 'movies&url=tech', '55.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*56', 'movies&url=time', '56.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*57', 'movies&url=vampire', '57.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*58', 'movies&url=vr', '58.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*59', 'movies&url=wilhelm', '59.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]PLAYLIST[/COLOR][/B]*60', 'movies&url=zombie', '60.png', 'playlist.png')

        self.endDirectory()		


    def playlist(self, lite=False):		
	
        self.addDirectoryItem('[B][COLOR ffff0000]IMDB[/COLOR][/B]', 'movies&url=thousand', 'imdb.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]DOCUMENTARIES[/COLOR][/B]', 'movies&url=docs', 'docs.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]ACTION[/COLOR][/B]', 'movies&url=action', 'action.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]ANIMATED[/COLOR][/B]', 'movies&url=animated', 'animated.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]GANGSTER[/COLOR][/B]', 'movies&url=gangster', 'gangster.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]HORROR[/COLOR][/B]', 'movies&url=horror', 'horror.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]1960-1999[/COLOR][/B]', 'movies&url=action2', 'year.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]MISTERY[/COLOR][/B]', 'movies&url=horror2', 'mistery.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]SCI-FI[/COLOR][/B]', 'movies&url=scifi', 'scifi.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]WESTERNS[/COLOR][/B]', 'movies&url=western', 'western.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]COP[/COLOR][/B]', 'movies&url=cop', 'cop.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]WAR[/COLOR][/B]', 'movies&url=war', 'war.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]DIRECTED BY WOMEN[/COLOR][/B]', 'movies&url=women', 'women.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]POLITICAL[/COLOR][/B]', 'movies&url=political', 'political.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]ROMANTIC[/COLOR][/B]', 'movies&url=romance', 'romance.png', 'playlist.png')

        self.endDirectory()		
    def spike(self, lite=False):		
	
        self.addDirectoryItem('[B][COLOR ffff0000]S[/COLOR][COLOR white]*LEE[/COLOR][/B]', 'movies&url=spike', 'lee.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]A[/COLOR][COLOR white]*HITCHCOCK[/COLOR][/B]', 'movies&url=alfred', 'hitch.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]C[/COLOR][COLOR white]*EASTWOOD[/COLOR][/B]', 'movies&url=clint', 'east.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]S[/COLOR][COLOR white]*SPIELBERG[/COLOR][/B]', 'movies&url=steven', 'spiel.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]J[/COLOR][COLOR white]*CAMERON[/COLOR][/B]', 'movies&url=james', 'cameron.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]Q[/COLOR][COLOR white]*TARANTINO[/COLOR][/B]', 'movies&url=quentin', 'taran.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]M[/COLOR][COLOR white]*GIBSON[/COLOR][/B]', 'movies&url=mel', 'gibson.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]B[/COLOR][COLOR white]*AFFLECK[/COLOR][/B]', 'movies&url=ben', 'affleck.png', 'playlist.png')
        self.addDirectoryItem('[B][COLOR ffff0000]M[/COLOR][COLOR white]*SCORSESE[/COLOR][/B]', 'movies&url=martin', 'scorsese.png', 'playlist.png')	

		
        self.endDirectory()		
		
    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[B][COLOR ffff0000]ACTOR SEARCH[/COLOR][/B]', 'moviePerson', 'actorsearch.png', 'DefaultMovies.png')
        self.addDirectoryItem('[B][COLOR ffff0000]TV ACTOR SEARCH[/COLOR][/B]', 'tvPerson', 'actorsearch.png', 'DefaultTVShows.png')

        self.endDirectory()


    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()




    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


