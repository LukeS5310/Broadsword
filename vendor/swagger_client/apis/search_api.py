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


class SearchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_search(self, categories, character_id, search, **kwargs):
        """
        Search on a string
        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_search(categories, character_id, search, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] categories: Type of entities to search for (required)
        :param int character_id: An EVE character ID (required)
        :param str search: The string to search on (required)
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param bool strict: Whether the search should be a strict match
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_search_with_http_info(categories, character_id, search, **kwargs)
        else:
            (data) = self.get_characters_character_id_search_with_http_info(categories, character_id, search, **kwargs)
            return data

    def get_characters_character_id_search_with_http_info(self, categories, character_id, search, **kwargs):
        """
        Search on a string
        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_search_with_http_info(categories, character_id, search, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] categories: Type of entities to search for (required)
        :param int character_id: An EVE character ID (required)
        :param str search: The string to search on (required)
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param bool strict: Whether the search should be a strict match
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['categories', 'character_id', 'search', 'datasource', 'language', 'strict', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'categories' is set
        if ('categories' not in params) or (params['categories'] is None):
            raise ValueError("Missing the required parameter `categories` when calling `get_characters_character_id_search`")
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_search`")
        # verify the required parameter 'search' is set
        if ('search' not in params) or (params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `get_characters_character_id_search`")

        if 'categories' in params and len(params['categories']) > 12:
            raise ValueError("Invalid value for parameter `categories` when calling `get_characters_character_id_search`, number of items must be less than or equal to `12`")
        if 'categories' in params and len(params['categories']) < 1:
            raise ValueError("Invalid value for parameter `categories` when calling `get_characters_character_id_search`, number of items must be greater than or equal to `1`")
        if 'search' in params and len(params['search']) < 3:
            raise ValueError("Invalid value for parameter `search` when calling `get_characters_character_id_search`, length must be greater than or equal to `3`")

        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'categories' in params:
            query_params.append(('categories', params['categories']))
            collection_formats['categories'] = 'csv'
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'language' in params:
            query_params.append(('language', params['language']))
        if 'search' in params:
            query_params.append(('search', params['search']))
        if 'strict' in params:
            query_params.append(('strict', params['strict']))
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

        return self.api_client.call_api('/v2/characters/{character_id}/search/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetCharactersCharacterIdSearchOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_search(self, categories, search, **kwargs):
        """
        Search on a string
        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_search(categories, search, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] categories: Type of entities to search for (required)
        :param str search: The string to search on (required)
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param bool strict: Whether the search should be a strict match
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_search_with_http_info(categories, search, **kwargs)
        else:
            (data) = self.get_search_with_http_info(categories, search, **kwargs)
            return data

    def get_search_with_http_info(self, categories, search, **kwargs):
        """
        Search on a string
        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_search_with_http_info(categories, search, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] categories: Type of entities to search for (required)
        :param str search: The string to search on (required)
        :param str datasource: The server name you would like data from
        :param str language: Language to use in the response
        :param bool strict: Whether the search should be a strict match
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['categories', 'search', 'datasource', 'language', 'strict', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'categories' is set
        if ('categories' not in params) or (params['categories'] is None):
            raise ValueError("Missing the required parameter `categories` when calling `get_search`")
        # verify the required parameter 'search' is set
        if ('search' not in params) or (params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `get_search`")

        if 'categories' in params and len(params['categories']) > 10:
            raise ValueError("Invalid value for parameter `categories` when calling `get_search`, number of items must be less than or equal to `10`")
        if 'categories' in params and len(params['categories']) < 1:
            raise ValueError("Invalid value for parameter `categories` when calling `get_search`, number of items must be greater than or equal to `1`")
        if 'search' in params and len(params['search']) < 3:
            raise ValueError("Invalid value for parameter `search` when calling `get_search`, length must be greater than or equal to `3`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categories' in params:
            query_params.append(('categories', params['categories']))
            collection_formats['categories'] = 'csv'
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'language' in params:
            query_params.append(('language', params['language']))
        if 'search' in params:
            query_params.append(('search', params['search']))
        if 'strict' in params:
            query_params.append(('strict', params['strict']))
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

        return self.api_client.call_api('/v1/search/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetSearchOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
