from __future__ import print_function

from oauth2client.client import OAuth2WebServerFlow

import gmusicapi

from mopidy import commands


class GMusicCommand(commands.Command):
    def __init__(self):
        super(GMusicCommand, self).__init__()
        self.add_child('login', LoginCommand())


class LoginCommand(commands.Command):
    def run(self, args, config):
        oauth_info = gmusicapi.Mobileclient._session_class.oauth
        flow = OAuth2WebServerFlow(**oauth_info._asdict())
        print()
        print('Go to the following URL to get an initial auth code, then ' +
              'provide it below: ' + flow.step1_get_authorize_url())
        print()
        try:
            initial_code = raw_input('code: ')
        except NameError:
            # Python 3
            initial_code = input('code: ')
        credentials = flow.step2_exchange(initial_code)
        refresh_token = credentials.refresh_token
        print('\nPlease update your config to include the following:')
        print()
        print('[gmusic]')
        print('refresh_token =', refresh_token)
        print()
