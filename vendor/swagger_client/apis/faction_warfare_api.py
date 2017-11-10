# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class FactionWarfareApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_fw_stats(self, character_id, **kwargs):
        """
        Overview of a character involved in faction warfare
        Statistical overview of a character involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_fw_stats(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdFwStatsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_fw_stats_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_fw_stats_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_fw_stats_with_http_info(self, character_id, **kwargs):
        """
        Overview of a character involved in faction warfare
        Statistical overview of a character involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_fw_stats_with_http_info(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdFwStatsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_fw_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_fw_stats`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/characters/{character_id}/fw/stats/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetCharactersCharacterIdFwStatsOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_fw_stats(self, corporation_id, **kwargs):
        """
        Overview of a corporation involved in faction warfare
        Statistics about a corporation involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_fw_stats(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCorporationsCorporationIdFwStatsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_fw_stats_with_http_info(corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_fw_stats_with_http_info(corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_fw_stats_with_http_info(self, corporation_id, **kwargs):
        """
        Overview of a corporation involved in faction warfare
        Statistics about a corporation involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_fw_stats_with_http_info(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCorporationsCorporationIdFwStatsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_fw_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_fw_stats`")


        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/corporations/{corporation_id}/fw/stats/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetCorporationsCorporationIdFwStatsOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_leaderboards(self, **kwargs):
        """
        List of the top factions in faction warfare
        Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_leaderboards_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_leaderboards_with_http_info(**kwargs)
            return data

    def get_fw_leaderboards_with_http_info(self, **kwargs):
        """
        List of the top factions in faction warfare
        Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_leaderboards" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/leaderboards/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetFwLeaderboardsOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_leaderboards_characters(self, **kwargs):
        """
        List of the top pilots in faction warfare
        Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards_characters(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsCharactersOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_leaderboards_characters_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_leaderboards_characters_with_http_info(**kwargs)
            return data

    def get_fw_leaderboards_characters_with_http_info(self, **kwargs):
        """
        List of the top pilots in faction warfare
        Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards_characters_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsCharactersOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_leaderboards_characters" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/leaderboards/characters/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetFwLeaderboardsCharactersOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_leaderboards_corporations(self, **kwargs):
        """
        List of the top corporations in faction warfare
        Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards_corporations(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsCorporationsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_leaderboards_corporations_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_leaderboards_corporations_with_http_info(**kwargs)
            return data

    def get_fw_leaderboards_corporations_with_http_info(self, **kwargs):
        """
        List of the top corporations in faction warfare
        Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday.  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_leaderboards_corporations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetFwLeaderboardsCorporationsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_leaderboards_corporations" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/leaderboards/corporations/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetFwLeaderboardsCorporationsOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_stats(self, **kwargs):
        """
        An overview of statistics about factions involved in faction warfare
        Statistical overviews of factions involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_stats(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwStats200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_stats_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_stats_with_http_info(**kwargs)
            return data

    def get_fw_stats_with_http_info(self, **kwargs):
        """
        An overview of statistics about factions involved in faction warfare
        Statistical overviews of factions involved in faction warfare  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_stats_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwStats200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_stats" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/stats/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetFwStats200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_systems(self, **kwargs):
        """
        Ownership of faction warfare systems
        An overview of the current ownership of faction warfare solar systems  ---  This route is cached for up to 1800 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_systems(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwSystems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_systems_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_systems_with_http_info(**kwargs)
            return data

    def get_fw_systems_with_http_info(self, **kwargs):
        """
        Ownership of faction warfare systems
        An overview of the current ownership of faction warfare solar systems  ---  This route is cached for up to 1800 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_systems_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwSystems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_systems" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/systems/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetFwSystems200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_fw_wars(self, **kwargs):
        """
        Data about which NPC factions are at war
        Data about which NPC factions are at war  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_wars(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwWars200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fw_wars_with_http_info(**kwargs)
        else:
            (data) = self.get_fw_wars_with_http_info(**kwargs)
            return data

    def get_fw_wars_with_http_info(self, **kwargs):
        """
        Data about which NPC factions are at war
        Data about which NPC factions are at war  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fw_wars_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetFwWars200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fw_wars" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/v1/fw/wars/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetFwWars200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
