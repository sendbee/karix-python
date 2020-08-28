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

    # Whatsapp Templates

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
        all_params = ['api_version', 'details']  # noqa: E501
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

        body_params = None
        if 'details' in params:
            body_params = params['details']

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

    # Whatsapp Accounts

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

    # Whatsapp Profile Photos

    def get_whatsapp_profile_photos(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profile_photos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profile_photos_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_profile_photos_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'offset', 'limit', 'number']  # noqa: E501
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
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
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
            '/whatsapp/profile/photo/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_profile_photo_by_number(self, number, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profile_photo_by_number_with_http_info(number **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profile_photo_by_number_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_profile_photo_by_number_with_http_info(self, number, **kwargs):  # noqa: E501
        all_params = ['number', 'api_version']  # noqa: E501
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
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `get_whatsapp_profile_photo_by_number_with_http_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

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
            '/whatsapp/profile/photo/{number}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_whatsapp_profile_photo(self, number, file, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_whatsapp_profile_photo_with_http_info(number, file, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_whatsapp_profile_photo_with_http_info(number, file, **kwargs)  # noqa: E501
            return data

    def upload_whatsapp_profile_photo_with_http_info(self, number, file, **kwargs):  # noqa: E501
        all_params = ['api_version', 'number', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_whatsapp_profile_photo" % key
                )
            params[key] = val
        del params['kwargs']

        if ('number' not in params) or (params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `upload_whatsapp_profile_photo`")
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_whatsapp_profile_photo`")

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/profile/photo/{number}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Whatsapp Profiles

    def get_whatsapp_profiles(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profiles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profiles_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_profiles_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'offset', 'limit', 'number']  # noqa: E501
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
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
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
            '/whatsapp/profile/business/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_profile_by_number(self, number, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profile_by_number_with_http_info(number **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profile_by_number_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_profile_by_number_with_http_info(self, number, **kwargs):  # noqa: E501
        all_params = ['number', 'api_version']  # noqa: E501
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
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `get_whatsapp_profile_photo_by_number_with_http_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

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
            '/whatsapp/profile/business/{number}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_whatsapp_profile(self, number, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_whatsapp_profile_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.update_whatsapp_profile_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def update_whatsapp_profile_with_http_info(self, number, **kwargs):  # noqa: E501
        all_params = ['api_version', 'number', 'details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_whatsapp_profile" % key
                )
            params[key] = val
        del params['kwargs']

        if ('number' not in params) or (params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `update_whatsapp_profile`")

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'details' in params:
            body_params = params['details']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/profile/business/{number}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Whatsapp Profile About

    def get_whatsapp_profile_about(self, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profile_about_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profile_about_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_profile_about_with_http_info(self, **kwargs):  # noqa: E501
        all_params = ['api_version', 'offset', 'limit', 'number', 'text']  # noqa: E501
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
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501
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
            '/whatsapp/profile/about/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_profile_about_by_number(self, number, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_profile_about_by_number_with_http_info(number **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_profile_about_by_number_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_profile_about_by_number_with_http_info(self, number, **kwargs):  # noqa: E501
        all_params = ['number', 'api_version']  # noqa: E501
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
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `get_whatsapp_profile_photo_by_number_with_http_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

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
            '/whatsapp/profile/about/{number}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_whatsapp_profile_about(self, number, **kwargs):  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_whatsapp_profile_about_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.update_whatsapp_profile_about_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def update_whatsapp_profile_about_with_http_info(self, number, **kwargs):  # noqa: E501
        all_params = ['api_version', 'number', 'details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_whatsapp_profile_about" % key
                )
            params[key] = val
        del params['kwargs']

        if ('number' not in params) or (params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `update_whatsapp_profile_about`")

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'details' in params:
            body_params = params['details']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/whatsapp/profile/about/{number}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
