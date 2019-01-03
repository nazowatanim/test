
import psutil
import json
from flask import Flask, request, Response
import json #for dumping JSON format
import requests
import subprocess
import random

app = Flask(__name__)


@app.route("/", methods=['GET'])
def test():
    return 'server has been created'

@app.route("/cpuusage", methods=['GET'])
def cpu_usage():
    try:

        json_key = {}
        cpu_usage = psutil.cpu_percent(interval=2)
        json_key['cpu_usage'] = float(cpu_usage)
        y=json.dumps(json_key)
        print (y)
        return  (y)
    except requests.exceptions.HTTPError:
        pass

@app.route("/cpu", methods=['GET'])
def cpu():
    try:
        x= psutil.cpu_times()
        print(x)
        #return (x)
        return  '{'+'\n'+'"'+'CPU usage time'+'"'+':'+(str(x))+'\n'+'}'
    except requests.exceptions.HTTPError:
        pass

@app.route("/memory", methods=['GET'])
def memory():
    try:
        x=psutil.virtual_memory()
        y=psutil.swap_memory()
        z=psutil.disk_usage('/')
        return '{'+'\n'+'"'+'memory'+'"'+':'+(str(x)+'\n'+'"'+'swap memory'+'"'+':'+str(y)+'\n'+'"'+'disk usage'+'"'+':'+str(z))+'\n'+'}'
    except requests.exceptions.HTTPError:
        pass

@app.route("/network", methods=['GET'])
def network():
    try:
        json_key={}
        output = subprocess.Popen(["netengine-utils ifconfig"], shell=True, stdout=subprocess.PIPE).communicate()[0]
        print(output)
        return (output)
    except requests.exceptions.HTTPError:
        pass

@app.route("/net", methods=['GET'])
def network2():
    try:
        y = psutil.net_io_counters(pernic=True)
        print(y)
    except requests.exceptions.HTTPError:
        pass


@app.route("/sensor", methods=['GET'])
def sensor():
    try:
        x=psutil.sensors_battery()
        print (x)
        return '{'+'\n'+'"'+'memory'+'"'+'sensors battery: '+str(x)+'\n'+'}'
    except requests.exceptions.HTTPError:
        pass

@app.route("/process", methods=['GET'])
def Process_Management():
    try:
        x=psutil.pids()
        #z=psutil.sensors_battery()
        return('pids:  '+str(x))
    except requests.exceptions.HTTPError:
        pass

@app.route("/pid", methods=['POST'])
def PID_Info():
    try:
        #y = psutil.users()
        data = request.get_json()
        pid = int(data['pid'])
        p = psutil.Process(pid)
        a=p.name()
        b=p.status()
        c=p.cpu_percent(interval=1.0)
        d=p.memory_info()
        e=p.exe()
        #z=psutil.sensors_battery()
        return('name:'+str(a)+', status:'+str(b)+', cpu:'+str(c)+'%'+'\n'+'memory_info:'+str(d)+'\n'+'command:'+str(e))
        #return('name:'+str(a)+', status: '+str(b))#+', cpu_percent: '+str(c))#+', noof cpu: '+str(d)+', memory_info: '+str(e))
    except requests.exceptions.HTTPError:
        return ('so such PID is running')




if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
