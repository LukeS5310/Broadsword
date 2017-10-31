# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FittingsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_characters_character_id_fittings_fitting_id(self, character_id, fitting_id, **kwargs):
        """
        Delete fitting
        Delete a fitting from a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param int fitting_id: ID for a fitting of this character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, **kwargs)
        else:
            (data) = self.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, **kwargs)
            return data

    def delete_characters_character_id_fittings_fitting_id_with_http_info(self, character_id, fitting_id, **kwargs):
        """
        Delete fitting
        Delete a fitting from a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param int fitting_id: ID for a fitting of this character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'fitting_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_characters_character_id_fittings_fitting_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `delete_characters_character_id_fittings_fitting_id`")
        # verify the required parameter 'fitting_id' is set
        if ('fitting_id' not in params) or (params['fitting_id'] is None):
            raise ValueError("Missing the required parameter `fitting_id` when calling `delete_characters_character_id_fittings_fitting_id`")


        collection_formats = {}

        resource_path = '/v1/characters/{character_id}/fittings/{fitting_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']
        if 'fitting_id' in params:
            path_params['fitting_id'] = params['fitting_id']

        query_params = {}
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'user_agent' in params:
            query_params['user_agent'] = params['user_agent']

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

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_fittings(self, character_id, **kwargs):
        """
        Get fittings
        Return fittings of a character  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_fittings(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdFittings200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_characters_character_id_fittings_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_fittings_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_fittings_with_http_info(self, character_id, **kwargs):
        """
        Get fittings
        Return fittings of a character  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_fittings_with_http_info(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdFittings200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_fittings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_fittings`")


        collection_formats = {}

        resource_path = '/v1/characters/{character_id}/fittings/'.replace('{format}', 'json')
        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = {}
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'user_agent' in params:
            query_params['user_agent'] = params['user_agent']

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

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdFittings200Ok]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_characters_character_id_fittings(self, character_id, **kwargs):
        """
        Create fitting
        Save a new fitting for a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_characters_character_id_fittings(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param PostCharactersCharacterIdFittingsFitting fitting: Details about the new fitting
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: PostCharactersCharacterIdFittingsCreated
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_characters_character_id_fittings_with_http_info(character_id, **kwargs)
        else:
            (data) = self.post_characters_character_id_fittings_with_http_info(character_id, **kwargs)
            return data

    def post_characters_character_id_fittings_with_http_info(self, character_id, **kwargs):
        """
        Create fitting
        Save a new fitting for a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_characters_character_id_fittings_with_http_info(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param PostCharactersCharacterIdFittingsFitting fitting: Details about the new fitting
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: PostCharactersCharacterIdFittingsCreated
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'fitting', 'token', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_characters_character_id_fittings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `post_characters_character_id_fittings`")


        collection_formats = {}

        resource_path = '/v1/characters/{character_id}/fittings/'.replace('{format}', 'json')
        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = {}
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'user_agent' in params:
            query_params['user_agent'] = params['user_agent']

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fitting' in params:
            body_params = params['fitting']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PostCharactersCharacterIdFittingsCreated',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
