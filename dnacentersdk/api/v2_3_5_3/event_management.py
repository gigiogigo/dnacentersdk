# -*- coding: utf-8 -*-
"""Cisco DNA Center Event Management API wrapper.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class EventManagement(object):
    """Cisco DNA Center Event Management API (version: 2.3.5.3).

    Wraps the DNA Center Event Management
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new EventManagement
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(EventManagement, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_auditlog_parent_records(self,
                                    category=None,
                                    context=None,
                                    description=None,
                                    device_id=None,
                                    domain=None,
                                    end_time=None,
                                    event_hierarchy=None,
                                    event_id=None,
                                    instance_id=None,
                                    is_system_events=None,
                                    limit=None,
                                    name=None,
                                    offset=None,
                                    order=None,
                                    severity=None,
                                    site_id=None,
                                    sort_by=None,
                                    source=None,
                                    start_time=None,
                                    sub_domain=None,
                                    user_id=None,
                                    headers=None,
                                    **request_parameters):
        """Get Parent Audit Log Event instances from the Event-Hub  .

        Args:
            instance_id(basestring): instanceId query parameter. InstanceID of the Audit Log. .
            name(basestring): name query parameter. Audit Log notification event name. .
            event_id(basestring): eventId query parameter. Audit Log notification's event ID.  .
            category(basestring): category query parameter. Audit Log notification's event category. Supported
                values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND,
                QUERY, CONVERSATION .
            severity(basestring): severity query parameter. Audit Log notification's event severity. Supported
                values: 1, 2, 3, 4, 5. .
            domain(basestring): domain query parameter. Audit Log notification's event domain. .
            sub_domain(basestring): subDomain query parameter. Audit Log notification's event sub-domain. .
            source(basestring): source query parameter. Audit Log notification's event source. .
            user_id(basestring): userId query parameter. Audit Log notification's event userId. .
            context(basestring): context query parameter. Audit Log notification's event correlationId. .
            event_hierarchy(basestring): eventHierarchy query parameter. Audit Log notification's event
                eventHierarchy. Example: "US.CA.San Jose" OR "US.CA" OR "CA.San Jose" Delimiter for
                hierarchy separation is ".". .
            site_id(basestring): siteId query parameter. Audit Log notification's siteId. .
            device_id(basestring): deviceId query parameter. Audit Log notification's deviceId. .
            is_system_events(bool): isSystemEvents query parameter. Parameter to filter system generated audit-logs.
                .
            description(basestring): description query parameter. String full/partial search (Provided input string
                is case insensitively matched for records). .
            offset(int): offset query parameter. Position of a particular Audit Log record in the data.  .
            limit(int): limit query parameter. Number of Audit Log records to be returned per page. .
            start_time(int): startTime query parameter. Start Time in milliseconds since Epoch Eg. 1597950637211
                (when provided endTime is mandatory) .
            end_time(int): endTime query parameter. End Time in milliseconds since Epoch Eg. 1597961437211 (when
                provided startTime is mandatory) .
            sort_by(basestring): sortBy query parameter. Sort the Audit Logs by certain fields. Supported values are
                event notification header attributes. .
            order(basestring): order query parameter. Order of the sorted Audit Log records. Default value is desc
                by timestamp. Supported values: asc, desc. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-audit-log-parent-records
        """
        check_type(headers, dict)
        check_type(instance_id, basestring)
        check_type(name, basestring)
        check_type(event_id, basestring)
        check_type(category, basestring)
        check_type(severity, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(source, basestring)
        check_type(user_id, basestring)
        check_type(context, basestring)
        check_type(event_hierarchy, basestring)
        check_type(site_id, basestring)
        check_type(device_id, basestring)
        check_type(is_system_events, bool)
        check_type(description, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'instanceId':
                instance_id,
            'name':
                name,
            'eventId':
                event_id,
            'category':
                category,
            'severity':
                severity,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'source':
                source,
            'userId':
                user_id,
            'context':
                context,
            'eventHierarchy':
                event_hierarchy,
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'isSystemEvents':
                is_system_events,
            'description':
                description,
            'offset':
                offset,
            'limit':
                limit,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/event/event-series/audit-log/parent-'
                 + 'records')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f8e3a0674c15fd58cd78f42dca37c7c_v2_3_5_3', json_data)

    def get_auditlog_summary(self,
                             category=None,
                             context=None,
                             description=None,
                             device_id=None,
                             domain=None,
                             end_time=None,
                             event_hierarchy=None,
                             event_id=None,
                             instance_id=None,
                             is_parent_only=None,
                             is_system_events=None,
                             name=None,
                             parent_instance_id=None,
                             severity=None,
                             site_id=None,
                             source=None,
                             start_time=None,
                             sub_domain=None,
                             user_id=None,
                             headers=None,
                             **request_parameters):
        """Get Audit Log Summary from the Event-Hub .

        Args:
            parent_instance_id(basestring): parentInstanceId query parameter. Parent Audit Log record's instanceID.
                .
            is_parent_only(bool): isParentOnly query parameter. Parameter to filter parent only audit-logs. .
            instance_id(basestring): instanceId query parameter. InstanceID of the Audit Log. .
            name(basestring): name query parameter. Audit Log notification event name. .
            event_id(basestring): eventId query parameter. Audit Log notification's event ID.  .
            category(basestring): category query parameter. Audit Log notification's event category. Supported
                values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND,
                QUERY, CONVERSATION .
            severity(basestring): severity query parameter. Audit Log notification's event severity. Supported
                values: 1, 2, 3, 4, 5. .
            domain(basestring): domain query parameter. Audit Log notification's event domain. .
            sub_domain(basestring): subDomain query parameter. Audit Log notification's event sub-domain. .
            source(basestring): source query parameter. Audit Log notification's event source. .
            user_id(basestring): userId query parameter. Audit Log notification's event userId. .
            context(basestring): context query parameter. Audit Log notification's event correlationId. .
            event_hierarchy(basestring): eventHierarchy query parameter. Audit Log notification's event
                eventHierarchy. Example: "US.CA.San Jose" OR "US.CA" OR "CA.San Jose" Delimiter for
                hierarchy separation is ".". .
            site_id(basestring): siteId query parameter. Audit Log notification's siteId. .
            device_id(basestring): deviceId query parameter. Audit Log notification's deviceId. .
            is_system_events(bool): isSystemEvents query parameter. Parameter to filter system generated audit-logs.
                .
            description(basestring): description query parameter. String full/partial search (Provided input string
                is case insensitively matched for records). .
            start_time(int): startTime query parameter. Start Time in milliseconds since Epoch Eg. 1597950637211
                (when provided endTime is mandatory) .
            end_time(int): endTime query parameter. End Time in milliseconds since Epoch Eg. 1597961437211 (when
                provided startTime is mandatory) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-audit-log-summary
        """
        check_type(headers, dict)
        check_type(parent_instance_id, basestring)
        check_type(is_parent_only, bool)
        check_type(instance_id, basestring)
        check_type(name, basestring)
        check_type(event_id, basestring)
        check_type(category, basestring)
        check_type(severity, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(source, basestring)
        check_type(user_id, basestring)
        check_type(context, basestring)
        check_type(event_hierarchy, basestring)
        check_type(site_id, basestring)
        check_type(device_id, basestring)
        check_type(is_system_events, bool)
        check_type(description, basestring)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'parentInstanceId':
                parent_instance_id,
            'isParentOnly':
                is_parent_only,
            'instanceId':
                instance_id,
            'name':
                name,
            'eventId':
                event_id,
            'category':
                category,
            'severity':
                severity,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'source':
                source,
            'userId':
                user_id,
            'context':
                context,
            'eventHierarchy':
                event_hierarchy,
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'isSystemEvents':
                is_system_events,
            'description':
                description,
            'startTime':
                start_time,
            'endTime':
                end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/event/event-series/audit-log/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea7c0220d55ae9e1a51d6823ce862_v2_3_5_3', json_data)

    def get_auditlog_records(self,
                             category=None,
                             context=None,
                             description=None,
                             device_id=None,
                             domain=None,
                             end_time=None,
                             event_hierarchy=None,
                             event_id=None,
                             instance_id=None,
                             is_system_events=None,
                             limit=None,
                             name=None,
                             offset=None,
                             order=None,
                             parent_instance_id=None,
                             severity=None,
                             site_id=None,
                             sort_by=None,
                             source=None,
                             start_time=None,
                             sub_domain=None,
                             user_id=None,
                             headers=None,
                             **request_parameters):
        """Get Audit Log Event instances from the Event-Hub  .

        Args:
            parent_instance_id(basestring): parentInstanceId query parameter. Parent Audit Log record's instanceID.
                .
            instance_id(basestring): instanceId query parameter. InstanceID of the Audit Log. .
            name(basestring): name query parameter. Audit Log notification event name. .
            event_id(basestring): eventId query parameter. Audit Log notification's event ID.  .
            category(basestring): category query parameter. Audit Log notification's event category. Supported
                values: INFO, WARN, ERROR, ALERT, TASK_PROGRESS, TASK_FAILURE, TASK_COMPLETE, COMMAND,
                QUERY, CONVERSATION .
            severity(basestring): severity query parameter. Audit Log notification's event severity. Supported
                values: 1, 2, 3, 4, 5. .
            domain(basestring): domain query parameter. Audit Log notification's event domain. .
            sub_domain(basestring): subDomain query parameter. Audit Log notification's event sub-domain. .
            source(basestring): source query parameter. Audit Log notification's event source. .
            user_id(basestring): userId query parameter. Audit Log notification's event userId. .
            context(basestring): context query parameter. Audit Log notification's event correlationId. .
            event_hierarchy(basestring): eventHierarchy query parameter. Audit Log notification's event
                eventHierarchy. Example: "US.CA.San Jose" OR "US.CA" OR "CA.San Jose" Delimiter for
                hierarchy separation is ".". .
            site_id(basestring): siteId query parameter. Audit Log notification's siteId. .
            device_id(basestring): deviceId query parameter. Audit Log notification's deviceId. .
            is_system_events(bool): isSystemEvents query parameter. Parameter to filter system generated audit-logs.
                .
            description(basestring): description query parameter. String full/partial search (Provided input string
                is case insensitively matched for records). .
            offset(int): offset query parameter. Position of a particular Audit Log record in the data.  .
            limit(int): limit query parameter. Number of Audit Log records to be returned per page. .
            start_time(int): startTime query parameter. Start Time in milliseconds since Epoch Eg. 1597950637211
                (when provided endTime is mandatory) .
            end_time(int): endTime query parameter. End Time in milliseconds since Epoch Eg. 1597961437211 (when
                provided startTime is mandatory) .
            sort_by(basestring): sortBy query parameter. Sort the Audit Logs by certain fields. Supported values are
                event notification header attributes. .
            order(basestring): order query parameter. Order of the sorted Audit Log records. Default value is desc
                by timestamp. Supported values: asc, desc. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-audit-log-records
        """
        check_type(headers, dict)
        check_type(parent_instance_id, basestring)
        check_type(instance_id, basestring)
        check_type(name, basestring)
        check_type(event_id, basestring)
        check_type(category, basestring)
        check_type(severity, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(source, basestring)
        check_type(user_id, basestring)
        check_type(context, basestring)
        check_type(event_hierarchy, basestring)
        check_type(site_id, basestring)
        check_type(device_id, basestring)
        check_type(is_system_events, bool)
        check_type(description, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'parentInstanceId':
                parent_instance_id,
            'instanceId':
                instance_id,
            'name':
                name,
            'eventId':
                event_id,
            'category':
                category,
            'severity':
                severity,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'source':
                source,
            'userId':
                user_id,
            'context':
                context,
            'eventHierarchy':
                event_hierarchy,
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'isSystemEvents':
                is_system_events,
            'description':
                description,
            'offset':
                offset,
            'limit':
                limit,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/event/event-series/audit-logs')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b0aa5a61f64a5da997dfe05bc8a4a64f_v2_3_5_3', json_data)

    def get_status_api_for_events(self,
                                  execution_id,
                                  headers=None,
                                  **request_parameters):
        """Get the Status of events API calls with provided executionId as mandatory path parameter .

        Args:
            execution_id(basestring): executionId path parameter. Execution ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-status-api-for-events
        """
        check_type(headers, dict)
        check_type(execution_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'executionId': execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/api-status/{executionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e1bd67a1a0225713ab23f0d0d3ceb4f6_v2_3_5_3', json_data)

    def update_email_destination(self,
                                 emailConfigId=None,
                                 fromEmail=None,
                                 primarySMTPConfig=None,
                                 secondarySMTPConfig=None,
                                 subject=None,
                                 toEmail=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Update Email Destination .

        Args:
            emailConfigId(string): Event Management's Required only for update email configuration .
            fromEmail(string): Event Management's From Email.
            primarySMTPConfig(object): Event Management's primarySMTPConfig.
            secondarySMTPConfig(object): Event Management's secondarySMTPConfig.
            subject(string): Event Management's Subject.
            toEmail(string): Event Management's To Email.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-email-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'emailConfigId':
                emailConfigId,
            'primarySMTPConfig':
                primarySMTPConfig,
            'secondarySMTPConfig':
                secondarySMTPConfig,
            'fromEmail':
                fromEmail,
            'toEmail':
                toEmail,
            'subject':
                subject,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_aaebb912125213b350d7423b4f01a4_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/email-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_aaebb912125213b350d7423b4f01a4_v2_3_5_3', json_data)

    def get_email_destination(self,
                              headers=None,
                              **request_parameters):
        """Get Email Destination .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-email-destination
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/email-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d5f08e8ff59e51d1a9ae56c3e20eae3c_v2_3_5_3', json_data)

    def create_email_destination(self,
                                 emailConfigId=None,
                                 fromEmail=None,
                                 primarySMTPConfig=None,
                                 secondarySMTPConfig=None,
                                 subject=None,
                                 toEmail=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Create Email Destination .

        Args:
            emailConfigId(string): Event Management's Required only for update email configuration .
            fromEmail(string): Event Management's From Email.
            primarySMTPConfig(object): Event Management's primarySMTPConfig.
            secondarySMTPConfig(object): Event Management's secondarySMTPConfig.
            subject(string): Event Management's Subject.
            toEmail(string): Event Management's To Email.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-email-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'emailConfigId':
                emailConfigId,
            'primarySMTPConfig':
                primarySMTPConfig,
            'secondarySMTPConfig':
                secondarySMTPConfig,
            'fromEmail':
                fromEmail,
            'toEmail':
                toEmail,
            'subject':
                subject,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c991ce0b0f058a08c863a4abdfc70a6_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/email-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c991ce0b0f058a08c863a4abdfc70a6_v2_3_5_3', json_data)

    def get_notifications(self,
                          category=None,
                          domain=None,
                          end_time=None,
                          event_ids=None,
                          limit=None,
                          namespace=None,
                          offset=None,
                          order=None,
                          severity=None,
                          site_id=None,
                          sort_by=None,
                          source=None,
                          start_time=None,
                          sub_domain=None,
                          tags=None,
                          type=None,
                          headers=None,
                          **request_parameters):
        """Get the list of Published Notifications .

        Args:
            event_ids(basestring): eventIds query parameter. The registered EventId should be provided .
            start_time(int): startTime query parameter. Start Time in milliseconds .
            end_time(int): endTime query parameter. End Time in milliseconds .
            category(basestring): category query parameter.
            type(basestring): type query parameter.
            severity(basestring): severity query parameter.
            domain(basestring): domain query parameter.
            sub_domain(basestring): subDomain query parameter. Sub Domain .
            source(basestring): source query parameter.
            offset(int): offset query parameter. Start Offset .
            limit(int): limit query parameter. # of records .
            sort_by(basestring): sortBy query parameter. Sort By column .
            order(basestring): order query parameter. Ascending/Descending order [asc/desc] .
            tags(basestring): tags query parameter.
            namespace(basestring): namespace query parameter.
            site_id(basestring): siteId query parameter. Site Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-notifications
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(category, basestring)
        check_type(type, basestring)
        check_type(severity, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(source, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(tags, basestring)
        check_type(namespace, basestring)
        check_type(site_id, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'category':
                category,
            'type':
                type,
            'severity':
                severity,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'source':
                source,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'tags':
                tags,
            'namespace':
                namespace,
            'siteId':
                site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/event-series')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c641f481dd285301861010da8d6fbf9f_v2_3_5_3', json_data)

    def count_of_notifications(self,
                               category=None,
                               domain=None,
                               end_time=None,
                               event_ids=None,
                               severity=None,
                               source=None,
                               start_time=None,
                               sub_domain=None,
                               type=None,
                               headers=None,
                               **request_parameters):
        """Get the Count of Published Notifications .

        Args:
            event_ids(basestring): eventIds query parameter. The registered EventId should be provided .
            start_time(int): startTime query parameter. Start Time in milliseconds .
            end_time(int): endTime query parameter. End Time in milliseconds .
            category(basestring): category query parameter.
            type(basestring): type query parameter.
            severity(basestring): severity query parameter.
            domain(basestring): domain query parameter.
            sub_domain(basestring): subDomain query parameter. Sub Domain .
            source(basestring): source query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!count-of-notifications
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(category, basestring)
        check_type(type, basestring)
        check_type(severity, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(source, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'category':
                category,
            'type':
                type,
            'severity':
                severity,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'source':
                source,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/event-series/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fd269fe156e4b5ad3f4210b7b168_v2_3_5_3', json_data)

    def get_snmp_destination(self,
                             config_id=None,
                             limit=None,
                             offset=None,
                             order=None,
                             sort_by=None,
                             headers=None,
                             **request_parameters):
        """Get SNMP Destination .

        Args:
            config_id(basestring): configId query parameter. List of SNMP configurations .
            offset(int): offset query parameter. The number of SNMP configuration's to offset in the resultset whose
                default value 0 .
            limit(int): limit query parameter. The number of SNMP configuration's to limit in the resultset whose
                default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-s-n-m-p-destination
        """
        check_type(headers, dict)
        check_type(config_id, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'configId':
                config_id,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/snmp-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e698d5a990a55158003a9f3250316a8_v2_3_5_3', json_data)

    def get_event_subscriptions(self,
                                event_ids=None,
                                limit=None,
                                offset=None,
                                order=None,
                                sort_by=None,
                                headers=None,
                                **request_parameters):
        """Gets the list of Subscriptions's based on provided offset and limit (Deprecated) .

        Args:
            event_ids(basestring): eventIds query parameter. List of subscriptions related to the respective
                eventIds .
            offset(int): offset query parameter. The number of Subscriptions's to offset in the resultset whose
                default value 0 .
            limit(int): limit query parameter. The number of Subscriptions's to limit in the resultset whose default
                value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-event-subscriptions
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d7d4e55d6bbb21c34ce863a131_v2_3_5_3', json_data)

    def delete_event_subscriptions(self,
                                   subscriptions,
                                   headers=None,
                                   **request_parameters):
        """Delete EventSubscriptions .

        Args:
            subscriptions(basestring): subscriptions query parameter. List of EventSubscriptionId's for removal .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-event-subscriptions
        """
        check_type(headers, dict)
        check_type(subscriptions, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'subscriptions':
                subscriptions,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a0e0b1772dfc5a02a96a9f6ee6e2579b_v2_3_5_3', json_data)

    def update_event_subscriptions(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Update SubscriptionEndpoint to list of registered events(Deprecated) .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-event-subscriptions
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_dfda5beca4cc5437876bff366493ebf0_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_dfda5beca4cc5437876bff366493ebf0_v2_3_5_3', json_data)

    def create_event_subscriptions(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Subscribe SubscriptionEndpoint to list of registered events (Deprecated) .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-event-subscriptions
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_fcc151af7615a84adf48b714d146192_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fcc151af7615a84adf48b714d146192_v2_3_5_3', json_data)

    def get_email_subscription_details(self,
                                       instance_id=None,
                                       limit=None,
                                       name=None,
                                       offset=None,
                                       order=None,
                                       sort_by=None,
                                       headers=None,
                                       **request_parameters):
        """Gets the list of subscription details for specified connectorType .

        Args:
            name(basestring): name query parameter. Name of the specific configuration .
            instance_id(basestring): instanceId query parameter. Instance Id of the specific configuration .
            offset(int): offset query parameter. The number of Email Subscription detail's to offset in the
                resultset whose default value 0 .
            limit(int): limit query parameter. The number of Email Subscription detail's to limit in the resultset
                whose default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-email-subscription-details
        """
        check_type(headers, dict)
        check_type(name, basestring)
        check_type(instance_id, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'name':
                name,
            'instanceId':
                instance_id,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription-details/email')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d420225889bb16f99ec7ba099a_v2_3_5_3', json_data)

    def get_rest_webhook_subscription_details(self,
                                              instance_id=None,
                                              limit=None,
                                              name=None,
                                              offset=None,
                                              order=None,
                                              sort_by=None,
                                              headers=None,
                                              **request_parameters):
        """Gets the list of subscription details for specified connectorType .

        Args:
            name(basestring): name query parameter. Name of the specific configuration .
            instance_id(basestring): instanceId query parameter. Instance Id of the specific configuration .
            offset(int): offset query parameter. The number of Rest/Webhook Subscription detail's to offset in the
                resultset whose default value 0 .
            limit(int): limit query parameter. The number of Rest/Webhook Subscription detail's to limit in the
                resultset whose default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-rest-webhook-subscription-details
        """
        check_type(headers, dict)
        check_type(name, basestring)
        check_type(instance_id, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'name':
                name,
            'instanceId':
                instance_id,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription-details/rest')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f278c72555e9a56f554b2a21c85_v2_3_5_3', json_data)

    def get_syslog_subscription_details(self,
                                        instance_id=None,
                                        limit=None,
                                        name=None,
                                        offset=None,
                                        order=None,
                                        sort_by=None,
                                        headers=None,
                                        **request_parameters):
        """Gets the list of subscription details for specified connectorType .

        Args:
            name(basestring): name query parameter. Name of the specific configuration .
            instance_id(basestring): instanceId query parameter. Instance Id of the specific configuration .
            offset(int): offset query parameter. The number of Syslog Subscription detail's to offset in the
                resultset whose default value 0 .
            limit(int): limit query parameter. The number of Syslog Subscription detail's to limit in the resultset
                whose default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-syslog-subscription-details
        """
        check_type(headers, dict)
        check_type(name, basestring)
        check_type(instance_id, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'name':
                name,
            'instanceId':
                instance_id,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription-details/syslog')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c0dcb335458a58fa8bc5a485b174427d_v2_3_5_3', json_data)

    def count_of_event_subscriptions(self,
                                     event_ids,
                                     headers=None,
                                     **request_parameters):
        """Returns the Count of EventSubscriptions .

        Args:
            event_ids(basestring): eventIds query parameter. List of subscriptions related to the respective
                eventIds .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!count-of-event-subscriptions
        """
        check_type(headers, dict)
        check_type(event_ids, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c538dc50a4555b5fba17b672a89ee1b8_v2_3_5_3', json_data)

    def create_email_event_subscription(self,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **request_parameters):
        """Create Email Subscription Endpoint for list of registered events. .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-email-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_e69d02d71905aecbd10b782469efbda_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/email')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e69d02d71905aecbd10b782469efbda_v2_3_5_3', json_data)

    def update_email_event_subscription(self,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **request_parameters):
        """Update Email Subscription Endpoint for list of registered events .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-email-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f8b4842604b65658afb34b4f124db469_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/email')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f8b4842604b65658afb34b4f124db469_v2_3_5_3', json_data)

    def get_email_event_subscriptions(self,
                                      category=None,
                                      domain=None,
                                      event_ids=None,
                                      limit=None,
                                      name=None,
                                      offset=None,
                                      order=None,
                                      sort_by=None,
                                      sub_domain=None,
                                      type=None,
                                      headers=None,
                                      **request_parameters):
        """Gets the list of email Subscriptions's based on provided query params .

        Args:
            event_ids(basestring): eventIds query parameter. List of email subscriptions related to the respective
                eventIds (Comma separated event ids) .
            offset(int): offset query parameter. The number of Subscriptions's to offset in the resultset whose
                default value 0 .
            limit(int): limit query parameter. The number of Subscriptions's to limit in the resultset whose default
                value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            domain(basestring): domain query parameter. List of email subscriptions related to the respective domain
                .
            sub_domain(basestring): subDomain query parameter. List of email subscriptions related to the respective
                sub-domain .
            category(basestring): category query parameter. List of email subscriptions related to the respective
                category .
            type(basestring): type query parameter. List of email subscriptions related to the respective type .
            name(basestring): name query parameter. List of email subscriptions related to the respective name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-email-event-subscriptions
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(category, basestring)
        check_type(type, basestring)
        check_type(name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'category':
                category,
            'type':
                type,
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/email')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bc212b5ee1f252479f35e8dd58319f17_v2_3_5_3', json_data)

    def create_rest_webhook_event_subscription(self,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **request_parameters):
        """Create Rest/Webhook Subscription Endpoint for list of registered events .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-rest-webhook-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f41eb48a0da56949cfaddeecb51ab66_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/rest')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f41eb48a0da56949cfaddeecb51ab66_v2_3_5_3', json_data)

    def get_rest_webhook_event_subscriptions(self,
                                             category=None,
                                             domain=None,
                                             event_ids=None,
                                             limit=None,
                                             name=None,
                                             offset=None,
                                             order=None,
                                             sort_by=None,
                                             sub_domain=None,
                                             type=None,
                                             headers=None,
                                             **request_parameters):
        """Gets the list of Rest/Webhook Subscriptions's based on provided query params .

        Args:
            event_ids(basestring): eventIds query parameter. List of subscriptions related to the respective
                eventIds (Comma separated event ids) .
            offset(int): offset query parameter. The number of Subscriptions's to offset in the resultset whose
                default value 0 .
            limit(int): limit query parameter. The number of Subscriptions's to limit in the resultset whose default
                value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            domain(basestring): domain query parameter. List of subscriptions related to the respective domain .
            sub_domain(basestring): subDomain query parameter. List of subscriptions related to the respective sub-
                domain .
            category(basestring): category query parameter. List of subscriptions related to the respective category
                .
            type(basestring): type query parameter. List of subscriptions related to the respective type .
            name(basestring): name query parameter. List of subscriptions related to the respective name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-rest-webhook-event-subscriptions
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(category, basestring)
        check_type(type, basestring)
        check_type(name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'category':
                category,
            'type':
                type,
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/rest')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee2008494d158e7bff7f106519a64c5_v2_3_5_3', json_data)

    def update_rest_webhook_event_subscription(self,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **request_parameters):
        """Update Rest/Webhook Subscription Endpoint for list of registered events .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-rest-webhook-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_b6581534bb321eaea272365b7_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/rest')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_b6581534bb321eaea272365b7_v2_3_5_3', json_data)

    def update_syslog_event_subscription(self,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """Update Syslog Subscription Endpoint for list of registered events .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-syslog-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_d8fc92ddeab597ebb50ea003a6d46bd_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/syslog')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d8fc92ddeab597ebb50ea003a6d46bd_v2_3_5_3', json_data)

    def create_syslog_event_subscription(self,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """Create Syslog Subscription Endpoint for list of registered events .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-syslog-event-subscription
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_fb5a8c0075563491622171958074bf_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/syslog')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fb5a8c0075563491622171958074bf_v2_3_5_3', json_data)

    def get_syslog_event_subscriptions(self,
                                       category=None,
                                       domain=None,
                                       event_ids=None,
                                       limit=None,
                                       name=None,
                                       offset=None,
                                       order=None,
                                       sort_by=None,
                                       sub_domain=None,
                                       type=None,
                                       headers=None,
                                       **request_parameters):
        """Gets the list of Syslog Subscriptions's based on provided offset and limit .

        Args:
            event_ids(basestring): eventIds query parameter. List of subscriptions related to the respective
                eventIds (Comma separated event ids) .
            offset(int): offset query parameter. The number of Subscriptions's to offset in the resultset whose
                default value 0 .
            limit(int): limit query parameter. The number of Subscriptions's to limit in the resultset whose default
                value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            domain(basestring): domain query parameter. List of subscriptions related to the respective domain .
            sub_domain(basestring): subDomain query parameter. List of subscriptions related to the respective sub-
                domain .
            category(basestring): category query parameter. List of subscriptions related to the respective category
                .
            type(basestring): type query parameter. List of subscriptions related to the respective type .
            name(basestring): name query parameter. List of subscriptions related to the respective name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-syslog-event-subscriptions
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(domain, basestring)
        check_type(sub_domain, basestring)
        check_type(category, basestring)
        check_type(type, basestring)
        check_type(name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'domain':
                domain,
            'subDomain':
                sub_domain,
            'category':
                category,
            'type':
                type,
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/subscription/syslog')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c7bed4b4148753e6bc9912e3be135217_v2_3_5_3', json_data)

    def update_syslog_destination(self,
                                  configId=None,
                                  description=None,
                                  host=None,
                                  name=None,
                                  port=None,
                                  protocol=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Update Syslog Destination .

        Args:
            configId(string): Event Management's Required only for update syslog configuration .
            description(string): Event Management's Description.
            host(string): Event Management's Host.
            name(string): Event Management's Name.
            port(string): Event Management's Port.
            protocol(string): Event Management's Protocol. Available values are 'UDP' and 'TCP'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-syslog-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'configId':
                configId,
            'name':
                name,
            'description':
                description,
            'host':
                host,
            'protocol':
                protocol,
            'port':
                port,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a9f5796226051218eac559ab5211384_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/syslog-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a9f5796226051218eac559ab5211384_v2_3_5_3', json_data)

    def get_syslog_destination(self,
                               config_id=None,
                               limit=None,
                               name=None,
                               offset=None,
                               order=None,
                               protocol=None,
                               sort_by=None,
                               headers=None,
                               **request_parameters):
        """Get Syslog Destination .

        Args:
            config_id(basestring): configId query parameter. Config id of syslog server .
            name(basestring): name query parameter. Name of syslog server .
            protocol(basestring): protocol query parameter. Protocol of syslog server .
            offset(int): offset query parameter. The number of syslog configuration's to offset in the resultset
                whose default value 0 .
            limit(int): limit query parameter. The number of syslog configuration's to limit in the resultset whose
                default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-syslog-destination
        """
        check_type(headers, dict)
        check_type(config_id, basestring)
        check_type(name, basestring)
        check_type(protocol, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'configId':
                config_id,
            'name':
                name,
            'protocol':
                protocol,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/syslog-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a170168de2ac55cc93571af1fbc02894_v2_3_5_3', json_data)

    def create_syslog_destination(self,
                                  configId=None,
                                  description=None,
                                  host=None,
                                  name=None,
                                  port=None,
                                  protocol=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Create Syslog Destination .

        Args:
            configId(string): Event Management's Required only for update syslog configuration .
            description(string): Event Management's Description.
            host(string): Event Management's Host.
            name(string): Event Management's Name.
            port(string): Event Management's Port.
            protocol(string): Event Management's Protocol. Available values are 'UDP' and 'TCP'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-syslog-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'configId':
                configId,
            'name':
                name,
            'description':
                description,
            'host':
                host,
            'protocol':
                protocol,
            'port':
                port,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_dece7a9b353b49084a8ffa4f18c91_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/syslog-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_dece7a9b353b49084a8ffa4f18c91_v2_3_5_3', json_data)

    def create_webhook_destination(self,
                                   description=None,
                                   headers=None,
                                   method=None,
                                   name=None,
                                   trustCert=None,
                                   url=None,
                                   webhookId=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Create Webhook Destination .

        Args:
            description(string): Event Management's Description.
            method(string): Event Management's Method. Available values are 'POST' and 'PUT'.
            name(string): Event Management's Name.
            trustCert(boolean): Event Management's Trust Cert.
            url(string): Event Management's Url.
            webhookId(string): Event Management's Required only for update webhook configuration .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-webhook-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'webhookId':
                webhookId,
            'name':
                name,
            'description':
                description,
            'url':
                url,
            'method':
                method,
            'trustCert':
                trustCert,
            'headers':
                headers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b8699619f95a24bd2d81f12f048235_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/webhook')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b8699619f95a24bd2d81f12f048235_v2_3_5_3', json_data)

    def update_webhook_destination(self,
                                   description=None,
                                   headers=None,
                                   method=None,
                                   name=None,
                                   trustCert=None,
                                   url=None,
                                   webhookId=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Update Webhook Destination .

        Args:
            description(string): Event Management's Description.
            method(string): Event Management's Method. Available values are 'POST' and 'PUT'.
            name(string): Event Management's Name.
            trustCert(boolean): Event Management's Trust Cert.
            url(string): Event Management's Url.
            webhookId(string): Event Management's Required only for update webhook configuration .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-webhook-destination
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'webhookId':
                webhookId,
            'name':
                name,
            'description':
                description,
            'url':
                url,
            'method':
                method,
            'trustCert':
                trustCert,
            'headers':
                headers,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d5c229546dc755f796dfcf34f1c2e290_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/webhook')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d5c229546dc755f796dfcf34f1c2e290_v2_3_5_3', json_data)

    def get_webhook_destination(self,
                                limit=None,
                                offset=None,
                                order=None,
                                sort_by=None,
                                webhook_ids=None,
                                headers=None,
                                **request_parameters):
        """Get Webhook Destination .

        Args:
            webhook_ids(basestring): webhookIds query parameter. List of webhook configurations .
            offset(int): offset query parameter. The number of webhook configuration's to offset in the resultset
                whose default value 0 .
            limit(int): limit query parameter. The number of webhook configuration's to limit in the resultset whose
                default value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-webhook-destination
        """
        check_type(headers, dict)
        check_type(webhook_ids, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'webhookIds':
                webhook_ids,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/event/webhook')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ddecdd64b34c5fdc910296fce09b2828_v2_3_5_3', json_data)

    def get_events(self,
                   tags,
                   event_id=None,
                   limit=None,
                   offset=None,
                   order=None,
                   sort_by=None,
                   headers=None,
                   **request_parameters):
        """Gets the list of registered Events with provided eventIds or tags as mandatory .

        Args:
            event_id(basestring): eventId query parameter. The registered EventId should be provided .
            tags(basestring): tags query parameter. The registered Tags should be provided .
            offset(int): offset query parameter. The number of Registries to offset in the resultset whose default
                value 0 .
            limit(int): limit query parameter. The number of Registries to limit in the resultset whose default
                value 10 .
            sort_by(basestring): sortBy query parameter. SortBy field name .
            order(basestring): order query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-events
        """
        check_type(headers, dict)
        check_type(event_id, basestring)
        check_type(tags, basestring,
                   may_be_none=False)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventId':
                event_id,
            'tags':
                tags,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/events')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bf36f1819e61575189c0709efab6e48a_v2_3_5_3', json_data)

    def count_of_events(self,
                        tags,
                        event_id=None,
                        headers=None,
                        **request_parameters):
        """Get the count of registered events with provided eventIds or tags as mandatory .

        Args:
            event_id(basestring): eventId query parameter. The registered EventId should be provided .
            tags(basestring): tags query parameter. The registered Tags should be provided .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!count-of-events
        """
        check_type(headers, dict)
        check_type(event_id, basestring)
        check_type(tags, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventId':
                event_id,
            'tags':
                tags,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/events/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b21d2947d715c198f5e62ba3149839a_v2_3_5_3', json_data)

    def get_eventartifacts(self,
                           event_ids=None,
                           limit=None,
                           offset=None,
                           order=None,
                           search=None,
                           sort_by=None,
                           tags=None,
                           headers=None,
                           **request_parameters):
        """Gets the list of artifacts based on provided offset and limit .

        Args:
            event_ids(basestring): eventIds query parameter. List of eventIds .
            tags(basestring): tags query parameter. Tags defined .
            offset(int): offset query parameter. Record start offset .
            limit(int): limit query parameter. # of records to return in result set .
            sort_by(basestring): sortBy query parameter. Sort by field .
            order(basestring): order query parameter. sorting order (asc/desc) .
            search(basestring): search query parameter. findd matches in name, description, eventId, type, category
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-event-artifacts
        """
        check_type(headers, dict)
        check_type(event_ids, basestring)
        check_type(tags, basestring)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(search, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'eventIds':
                event_ids,
            'tags':
                tags,
            'offset':
                offset,
            'limit':
                limit,
            'sortBy':
                sort_by,
            'order':
                order,
            'search':
                search,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/event/artifact')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c0e0d76b2561b8f2efd0220f02267_v2_3_5_3', json_data)

    def eventartifact_count(self,
                            headers=None,
                            **request_parameters):
        """Get the count of registered event artifacts with provided eventIds or tags as mandatory .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!event-artifact-count
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/event/artifact/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a137e0b583c85ffe80fbbd85b480bf15_v2_3_5_3', json_data)

    def get_connector_types(self,
                            headers=None,
                            **request_parameters):
        """Get the list of connector types .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.

        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-connector-types
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/system/api/v1/event/config/connector-types')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b94cfb5af084c1a65d8e51df71_v2_3_5_3', json_data)
