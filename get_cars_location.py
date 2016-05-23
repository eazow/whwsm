# -*- coding: utf-8 -*-

import urllib2
import time
import hashlib
import json
import config

ACCOUNT = config.ACCOUNT

def get_access_token():
    account = ACCOUNT
    password = config.PASSWORD
    seconds = str(int(time.time()))
    signature = hashlib.md5(password+seconds).hexdigest()
    url = "http://api.gpsoo.net/1/auth/access_token?account=%s&time=%s&signature=%s" %\
        (account, seconds, signature)
    response  = urllib2.urlopen(url).read()
    response_json = json.loads(response)
    ret = response_json.get('ret')
    access_token = ''
    if ret == 0:
        access_token = response_json.get('access_token')
    
    return access_token
    
    #    $response = file_get_contents($url);
        
#         $accessToken = null;
#         $response = '{"access_token":"","expires_in":7200,"ret":0,"msg":""}';
#         $responseObj = json_decode($response);
#         if($responseObj && $responseObj->ret=='0') {
#             $accessToken = $responseObj->access_token;
#         }
#         return $accessToken;

def get_cars_location(name):
    account = ACCOUNT
    seconds = str(int(time.time()))
    access_token = ACCESS_TOKEN
    url = "http://api.gpsoo.net/1/account/monitor?access_token=%s&"+\
        "map_type=BAIDU&target=%s&account=%s&time=%s" 
        % (access_token, name, account, seconds);
        
    print url
        
    #{"ret":0,"msg":"","data":[{"imei":"868120123229731","device_info":3,"device_info_new":3,
    #"gps_time":1447247752,"sys_time":1447247757,"heart_time":1447293011,"server_time":1461742811,
    #"lng":114.360913,"lat":30.592742,"course":104,"speed":0,"acc":"0","acc_seconds":2592000,
    #"seconds":14449800}]
    #$response = file_get_contents($url);
    response  = urllib2.urlopen(url).read()
    print response
    response_json = json.loads(response)
    ret = response_json.get('ret')
    cars_location = []
    if ret == 0:
        cars_location = response_json.get('data')
        return cars_location


ACCESS_TOKEN = get_access_token()
print ACCESS_TOKEN
get_cars_location('大象租车'.decode('utf8'))

