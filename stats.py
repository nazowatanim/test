
import psutil
import json
from flask import Flask, request, Response
import json #for dumping JSON format
import requests

app = Flask(__name__)


@app.route("/", methods=['GET'])
def test():
    return 'server has been created'

@app.route("/cpu", methods=['GET'])
def cpu():
    try:
        x=psutil.cpu_times()
        return(str(x))
    except requests.exceptions.HTTPError:
        pass

@app.route("/memory", methods=['GET'])
def memory():
    try:
        x=psutil.virtual_memory()
        y=psutil.swap_memory()
        z=psutil.disk_usage('/')
        return('virtual memory: '+str(x)+'\n'+'swap memory: '+str(y)+'\n'+'disk usage: '+str(z))
    except requests.exceptions.HTTPError:
        pass

@app.route("/network", methods=['GET'])
def network():
    try:
        x=psutil.net_io_counters(pernic=True)
        y=psutil.net_if_addrs()
        z=psutil.net_if_stats()
        #a=psutil.users()
        return('network info : '+str(x)+'\n'+'network address: '+str(y)+'\n'+'Interface stats: '+str(z))#+'\n'+'users: '+str(a))
    except requests.exceptions.HTTPError:
        pass

@app.route("/sensor", methods=['GET'])
def sensor():
    try:
        x=psutil.sensors_temperatures()
        y=psutil.sensors_fans()
        z=psutil.sensors_battery()
        return('sensor temperatures : '+str(x)+'\n'+'sensor fans: '+str(y)+'\n'+'sensors battery: '+str(z))
    except requests.exceptions.HTTPError:
        pass
@app.route("/process", methods=['GET'])
def Process_Management():
    try:
        x=psutil.pids()
        #z=psutil.sensors_battery()
        return('system pids: '+str(x))
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
