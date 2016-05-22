# -*- coding: utf-8 -*-

import urllib2
import time
import hashlib
import json
from .. import config

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
    url = "http://api.gpsoo.net/1/account/monitor?access_token=%s&\
        map_type=BAIDU&target=%s&account=%s&time=%s" \
        % (access_token, name, account, seconds);
        
    #{"ret":0,"msg":"","data":[{"imei":"868120123229731","device_info":3,"device_info_new":3,"gps_time":1447247752,"sys_time":1447247757,"heart_time":1447293011,"server_time":1461742811,"lng":114.360913,"lat":30.592742,"course":104,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14449800},{"imei":"868120123242288","device_info":3,"device_info_new":3,"gps_time":1447243197,"sys_time":1447243273,"heart_time":1447539340,"server_time":1461742811,"lng":114.421423,"lat":30.507110,"course":260,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14203471},{"imei":"868120123264837","device_info":3,"device_info_new":3,"gps_time":1447241611,"sys_time":1447241503,"heart_time":1447241915,"server_time":1461742811,"lng":114.413545,"lat":30.473144,"course":87,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14500896},{"imei":"868120123266568","device_info":3,"device_info_new":3,"gps_time":1447270417,"sys_time":1447270417,"heart_time":1447316420,"server_time":1461742811,"lng":114.369936,"lat":30.616153,"course":51,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14426391},{"imei":"868120123266600","device_info":3,"device_info_new":3,"gps_time":1447282234,"sys_time":1447282318,"heart_time":1447285806,"server_time":1461742811,"lng":114.367677,"lat":30.583995,"course":288,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14457005},{"imei":"868120123266618","device_info":3,"device_info_new":3,"gps_time":1447252769,"sys_time":1447252131,"heart_time":1447524557,"server_time":1461742811,"lng":114.369447,"lat":30.614113,"course":230,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14218254},{"imei":"868120123266626","device_info":3,"device_info_new":3,"gps_time":1447419361,"sys_time":1447419363,"heart_time":1447628931,"server_time":1461742811,"lng":114.255610,"lat":30.537328,"course":201,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14113880},{"imei":"868120123266691","device_info":3,"device_info_new":3,"gps_time":1447492287,"sys_time":1447492294,"heart_time":1447518277,"server_time":1461742811,"lng":114.276515,"lat":30.469135,"course":36,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":14224534},{"imei":"868120123277458","device_info":3,"device_info_new":3,"gps_time":1449400008,"sys_time":1449398890,"heart_time":1449400016,"server_time":1461742811,"lng":114.364602,"lat":30.592022,"course":230,"speed":0,"acc":"0","acc_seconds":2592000,"seconds":12342795}]}
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
get_cars_location('大象租车')

