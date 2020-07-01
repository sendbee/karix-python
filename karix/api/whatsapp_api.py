from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from karix.api_client import ApiClient


class WhatsappApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_whatsapp_templates(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_templates_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'whatsapp_account_uid', 'category',
                      'name', 'language_code', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'whatsapp_account_uid' in params:
            query_params.append(('whatsapp_account_uid', params['whatsapp_account_uid']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/template/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_templates_by_id(self, uid, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_templates_by_id_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_templates_by_id_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_templates_by_id_with_http_info(self, uid, **kwargs):  # noqa: E501
        all_params = ['uid', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_templates_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_whatsapp_templates_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/template/{uid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_whatsapp_template(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_whatsapp_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_whatsapp_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_whatsapp_template_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'category', 'whatsapp_account_uid',
                      'name', 'language_code', 'attachment', 'text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_whatsapp_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = {}
        if 'category' in params:
            body_params['category'] = params['category']
        if 'whatsapp_account_uid' in params:
            body_params['whatsapp_account_uid'] = params['whatsapp_account_uid']
        if 'name' in params:
            body_params['name'] = params['name']
        if 'language_code' in params:
            body_params['language_code'] = params['language_code']
        if 'attachment' in params:
            body_params['attachment'] = params['attachment']
        if 'text' in params:
            body_params['text'] = params['text']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/template/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_accounts(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_accounts_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'karix_account_uid', 'name', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'karix_account_uid' in params:
            query_params.append(('karix_account_uid', params['karix_account_uid']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/account/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2015',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_account_by_id(self, uid, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_account_by_id_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_account_by_id_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_account_by_id_with_http_info(self, uid, **kwargs):  # noqa: E501
        all_params = ['uid', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_whatsapp_account_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/account/{uid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
