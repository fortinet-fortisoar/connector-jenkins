""""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""
import json
import requests
import urllib.parse
from connectors.core.connector import get_logger, ConnectorError
from requests.auth import HTTPBasicAuth

logger = get_logger('jenkins')


class Jenkins(object):
    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.username = config.get('username')
        self.api_token = config.get('api_token')
        self.verify_ssl = config.get('verify_ssl')
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.error_msg = {
            400: 'Bad/Invalid Request',
            401: 'Unauthorized: Invalid credentials or token provided failed to authorize',
            403: 'Forbidden, source data source is read-only',
            404: 'Not found, either source or target data source could not be found',
            500: 'Internal Server Error',
            503: 'Service Unavailable',
            'time_out': 'The request timed out while trying to connect to the remote server',
            'ssl_error': 'SSL certificate validation failed'
        }

    def make_api_call(self, endpoint, method='post', payload=None, params=None, return_headers=False):
        try:
            service_endpoint = f'{self.server_url}{endpoint}' if not self.server_url.endswith('/') else f'{self.server_url}/{endpoint}'
            logger.debug("service_endpoint : {}".format(service_endpoint))
            response = requests.request(method, service_endpoint, auth=HTTPBasicAuth(self.username, self.api_token),
                                        params=params,
                                        data=payload, headers=self.headers,
                                        verify=self.verify_ssl)
            logger.debug("Rest API Response Status code : {}".format(response.status_code))
            if response.ok:
                if return_headers:
                    return response.headers.get('Location')
                try:
                    return response.json()
                except ValueError:
                    return {'status': 'success', 'response': response.text}
            else:
                logger.error(f'{self.error_msg.get(response.status_code)}: {response.text}')
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response.text})
        except requests.exceptions.SSLError as err:
            logger.error(err)
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout as err:
            logger.error(err)
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout as err:
            logger.error(err)
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError as err:
            logger.error(err)
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def normalize_job_path(job_path):
    job_path = job_path.strip("/")
    if not job_path.startswith("job/"):
        job_path = "job/" + job_path
    return "/" + job_path


def trigger_job(config, params):
    api_client = Jenkins(config)
    job_path = normalize_job_path(params.get('job_path', ''))
    build_parameters = params.get('build_parameters')
    endpoint = f'{job_path}/buildWithParameters'
    resp = {'job_path': job_path}
    payload = '&'.join(f"{key}={value}" for key, value in build_parameters.items()) if build_parameters else None
    build_url = api_client.make_api_call(endpoint, method='POST', return_headers=True, payload=payload)
    if build_url:
        build_number = build_url.rstrip('/').split('/')[-1] if build_url and '/' in build_url else None
        resp.update({'build_number': build_number})
    return resp


def get_job_status(config, params):
    api_client = Jenkins(config)
    job_path = normalize_job_path(params.get('job_path', ''))
    build_number = params.get('build_number')
    endpoint = f'/{job_path}/{build_number}/api/json'
    return api_client.make_api_call(endpoint, method='GET')


def get_list_jobs(config, params):
    api_client = Jenkins(config)
    job_path = normalize_job_path(params.get('job_path', ''))
    endpoint = f'{job_path}/api/json' if job_path else '/api/json'
    return api_client.make_api_call(endpoint, method='GET')


def resume_jenkins_job_with_input(config, params):
    api_client = Jenkins(config)
    job_path = normalize_job_path(params.get('job_path', ''))
    build_number = params.get('build_number')
    input_id = params.get('input_id')
    input_parameters = params.get('input_parameters')
    if not isinstance(input_parameters, list):
        input_parameters = [input_parameters]
    # Build the Jenkins input submission endpoint
    endpoint = f'{job_path}/{build_number}/input/{input_id}/submit'
    payload = None
    if input_parameters:
        input_param = json.dumps({"parameter": input_parameters})
        encoded_json = urllib.parse.quote(input_param)
        payload = f'json={encoded_json}&proceed=Proceed'
    resp = api_client.make_api_call(endpoint, 'POST', payload=payload)
    return {"status": "success", "response": "Provided input submitted successfully"}


def generic_rest_api_call(config, params):
    api_client = Jenkins(config)
    method = params.get('method')
    endpoint = params.get('endpoint')
    payload = params.get('payload')
    query_params = params.get('query_params')
    return api_client.make_api_call(endpoint, method=method, payload=payload, params=query_params)


def _check_health(config):
    api_client = Jenkins(config)
    return api_client.make_api_call('/api/json', method='GET')


operations = {
    'get_list_jobs': get_list_jobs,
    'trigger_job': trigger_job,
    'get_job_status': get_job_status,
    'resume_jenkins_job_with_input': resume_jenkins_job_with_input,
    'generic_rest_api_call': generic_rest_api_call
}
