# -*- coding: utf-8 -*-

import requests
import json

class Req():

    GET = 'get'
    POST_BY_FORM = 'post_by_form'
    POST_BY_JSON = 'post_by_json'

    def __init__(self, url, method=GET):
        self.url = url
        self.method = method
        self.data = {}

    def add_param(self, key, value):
        self.data[key] = value

    def __get(self):
        return requests.get(self.url, params=self.data)

    def __post(self, post_type):
        if post_type == self.POST_BY_FORM:
            return requests.post(self.url, data=self.data)
        elif post_type == self.POST_BY_JSON:
            __json = json.dumps(self.data)
            return requests.post(self.url, json=__json)

    def send(self):
        __send = {
            'get' : self.__get(),
            'post_by_form' : self.__post(self.POST_BY_FORM),
            'post_by_json' : self.__post(self.POST_BY_JSON)
        }
        return Response(__send[self.method.lower()])


class Response():

    def __init__(self, resp):
        self.__resp = resp
        self.__analysis_resp()

    def __analysis_resp(self):
        self.__url = self.__resp.url
        self.__code =  self.__resp.status_code
        self.__headers = self.__resp.headers
        self.__content = self.__resp.content

    @property
    def RAW_RESPONSE(self):
        return self.__resp

    @property
    def URL(self):
        return self.__url

    @property
    def STATUS_CODE(self):
        return self.__code

    @property
    def HEADERS(self):
        return self.__headers

    @property
    def CONTENTS(self):
        return self.__content

    @property
    def JSON_CONTENTS(self):
        return json.loads(self.__content)