#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hmac
import json
import time
import hashlib
import inspect
import requests

__author__ = 'sylar1015@163.com'

class Coinspot(object):

    def __init__(self, api_key, api_secret):

        self._api_key = str(api_key) if api_key else ''
        self._api_secret = str(api_secret) if api_secret else ''

    def get_func_name(self):
        return inspect.stack()[1][3]

    def is_public_method(self, method):
        if method in ['latest']:
            return True
        else:
            return False

    def get_url(self,method):
        base_url = ''
        if self.is_public_method(method):
            base_url = 'https://www.coinspot.com.au/pubapi/'
        else:
            base_url = 'https://www.coinspot.com.au/api/'

        url = base_url + method.replace('_', '/')
        return url

    def api_call(self, **kwargs):
        method = kwargs.get('method', '')
        data = kwargs.get('data', {})
        headers = kwargs.get('headers', {})

        if self.is_public_method(method):
            return requests.get(self.get_url(method)).json()
        else:
            nonce = int(time.time())
            data['nonce'] = nonce
            headers['key'] = self._api_key
            e = json.dumps(data, separators=(',', ':')).encode()
            headers['sign'] = hmac.new(self._api_secret.encode(),
                            e, hashlib.sha512).hexdigest()
            headers['Content-Type'] = 'application/json'
            return requests.post(self.get_url(method), json = data, headers = headers).json()

    def quote_buy(self, cointype = 'BTC', amount = 1):
        data = {'cointype' : cointype, 'amount' : amount}
        return self.api_call(method=self.get_func_name(), data=data)

    def quote_sell(self, cointype = 'BTC', amount = 1):
        data = {'cointype' : cointype, 'amount' : amount}
        return self.api_call(method=self.get_func_name(), data=data)

    def latest(self):
        return self.api_call(method=self.get_func_name())

    def orders(self, cointype = 'BTC'):
        data = {'cointype' : cointype}
        return self.api_call(method=self.get_func_name(), data=data)

    def orders_history(self, cointype = 'BTC'):
        data = {'cointype' : cointype}
        return self.api_call(method=self.get_func_name(), data=data)

    def my_coin_deposit(self, cointype = 'BTC'):
        data = {'cointype' : cointype}
        return self.api_call(method=self.get_func_name(), data=data)

    def my_coin_send(self, cointype = 'BTC', address = '', amount = 1):
        data = {'cointype' : cointype, 'address': address, 'amount': amount}
        return self.api_call(method=self.get_func_name(), data=data)

    def my_balances(self):
        return self.api_call(method=self.get_func_name())

    def my_orders(self):
        return self.api_call(method=self.get_func_name())

    def my_buy(self, cointype = 'BTC', amount = 1, rate = 0.1):
        data = {'cointype':cointype, 'amount':amount, 'rate':rate}
        return self.api_call(method=self.get_func_name(), data = data)

    def my_sell(self, cointype = 'BTC', amount = 1, rate = 0.1):
        data = {'cointype':cointype, 'amount':amount, 'rate':rate}
        return self.api_call(method=self.get_func_name(), data = data)

    def my_buy_cancel(self, order_id = ''):
        data = {'id': order_id}
        return self.api_call(method=self.get_func_name(), data = data)

    def my_sell_cancel(self, order_id = ''):
        data = {'id': order_id}
        return self.api_call(method=self.get_func_name(), data = data)