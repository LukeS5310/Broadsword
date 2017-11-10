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


class WalletApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_wallet(self, character_id, **kwargs):
        """
        Get a character's wallet balance
        Returns a character's wallet balance  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_wallet_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_with_http_info(self, character_id, **kwargs):
        """
        Get a character's wallet balance
        Returns a character's wallet balance  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet_with_http_info(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: float
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
                    " to method get_characters_character_id_wallet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_wallet`")


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

        return self.api_client.call_api('/v1/characters/{character_id}/wallet/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='float',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_wallet_journal(self, character_id, **kwargs):
        """
        Get character wallet journal
        Retrieve character wallet journal  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet_journal(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdWalletJournal200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_wallet_journal_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_journal_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_journal_with_http_info(self, character_id, **kwargs):
        """
        Get character wallet journal
        Retrieve character wallet journal  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet_journal_with_http_info(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdWalletJournal200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'from_id', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_wallet_journal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_wallet_journal`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
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

        return self.api_client.call_api('/v2/characters/{character_id}/wallet/journal/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdWalletJournal200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_wallet_transactions(self, character_id, **kwargs):
        """
        Get wallet transactions
        Get wallet transactions of a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet_transactions(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show transactions happened before the one referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdWalletTransactions200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_wallet_transactions_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_transactions_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_transactions_with_http_info(self, character_id, **kwargs):
        """
        Get wallet transactions
        Get wallet transactions of a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_wallet_transactions_with_http_info(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show transactions happened before the one referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdWalletTransactions200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'from_id', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_wallet_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_wallet_transactions`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
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

        return self.api_client.call_api('/v1/characters/{character_id}/wallet/transactions/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdWalletTransactions200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets(self, corporation_id, **kwargs):
        """
        Returns a corporation's wallet balance
        Get a corporation's wallets  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWallets200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_wallets_with_http_info(corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_with_http_info(corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_wallets_with_http_info(self, corporation_id, **kwargs):
        """
        Returns a corporation's wallet balance
        Get a corporation's wallets  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets_with_http_info(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWallets200Ok]
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
                    " to method get_corporations_corporation_id_wallets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets`")


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

        return self.api_client.call_api('/v1/corporations/{corporation_id}/wallets/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdWallets200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets_division_journal(self, corporation_id, division, **kwargs):
        """
        Get corporation wallet journal
        Retrieve corporation wallet journal  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_journal(corporation_id, division, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWalletsDivisionJournal200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id, division, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id, division, **kwargs)
            return data

    def get_corporations_corporation_id_wallets_division_journal_with_http_info(self, corporation_id, division, **kwargs):
        """
        Get corporation wallet journal
        Retrieve corporation wallet journal  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id, division, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWalletsDivisionJournal200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'division', 'datasource', 'from_id', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_wallets_division_journal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_journal`")
        # verify the required parameter 'division' is set
        if ('division' not in params) or (params['division'] is None):
            raise ValueError("Missing the required parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`")

        if 'division' in params and params['division'] > 7:
            raise ValueError("Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value less than or equal to `7`")
        if 'division' in params and params['division'] < 1:
            raise ValueError("Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']
        if 'division' in params:
            path_params['division'] = params['division']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
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

        return self.api_client.call_api('/v1/corporations/{corporation_id}/wallets/{division}/journal/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdWalletsDivisionJournal200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets_division_transactions(self, corporation_id, division, **kwargs):
        """
        Get corporation wallet transactions
        Get wallet transactions of a corporation  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_transactions(corporation_id, division, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWalletsDivisionTransactions200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id, division, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id, division, **kwargs)
            return data

    def get_corporations_corporation_id_wallets_division_transactions_with_http_info(self, corporation_id, division, **kwargs):
        """
        Get corporation wallet transactions
        Get wallet transactions of a corporation  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id, division, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdWalletsDivisionTransactions200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'division', 'datasource', 'from_id', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_wallets_division_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_transactions`")
        # verify the required parameter 'division' is set
        if ('division' not in params) or (params['division'] is None):
            raise ValueError("Missing the required parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`")

        if 'division' in params and params['division'] > 7:
            raise ValueError("Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`, must be a value less than or equal to `7`")
        if 'division' in params and params['division'] < 1:
            raise ValueError("Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']
        if 'division' in params:
            path_params['division'] = params['division']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
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

        return self.api_client.call_api('/v1/corporations/{corporation_id}/wallets/{division}/transactions/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdWalletsDivisionTransactions200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
