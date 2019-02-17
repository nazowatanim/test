'''extracts the bytes receive write parameter from the psutil network information in JSON format and subtract the loopback'''
import psutil
import json
import threading
from config import byte
net = psutil.net_io_counters(pernic=True)#to get the netowrk parameters
interface='lo' #get RX TX for loopback interface
a=obj=net.get(interface)
p=obj.bytes_recv
q=obj.bytes_sent
t=p+q#add total of RX TX for loopback
print (t)
#print (p)
#print (net)
'''get the RX TX for all the interfaces and extracts it in JSon format.
this function will be called every 1 second to check the parameters'''
def test():
    l = []
    j = []
    p= []
    #extracts only bytes recv/sent parameter
    for k, v in net.items():
    	x1={"bytes_recv":v.bytes_recv,"bytes_sent":v.bytes_sent}
    	x2={"bytes_recv_config":v.bytes_recv/byte,"bytes_sent_config":v.bytes_sent/byte}
    	x3=(v.bytes_recv/byte+v.bytes_sent/byte)
    	y1=json.dumps(x1)
    	y2=json.dumps(x2)
    	l.append(y1)
    	j.append(y2)
    	p.append(x3)
       
    threading.Timer(1.0, test).start()

    print (l)#testing
    print (j)#testing
    sum=0
    for i in p:
    	sum+=i
    total=sum-t #subtract loopback
    print ("consumption",abs(total))



