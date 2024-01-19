#!/usr/bin/env python3

import re # regex
import numpy as np # number operations
import yaml # pyyaml for yaml
import paramiko # ssh into servers
from flask import Flask, render_template
import matplotlib.pyplot as plt
import time

# afunction that performs an SSH operation to remote systems
def sshlogin(ip, un, passw):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=ip, username=un, password=passw)
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    sshresult = ssh_stdout.read().decode('utf-8').split()[0]
    with open('sshresult','w') as myfile:
        myfile.write(sshresult)
    # convert uptime from seconds to days
    days = (int(float(sshresult)) / 86400)
    sshsession.close()
    print(days)
    return days

app = Flask(__name__)

@app.route('/graphing')
def graphing():
    # credentials for the servers
    with open('/home/student/sshpass.yml') as sshpass:
        creds = yaml.load(sshpass)
    svruptime = []
    xtick = []
    for cred in creds:
        xtick.append(cred['ip'])
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        svruptime.append(resp)
    xtick = tuple(xtick)
    svruptime = tuple(svruptime)

    # graphing
    # N = total number of bars
    N = 2
    # the x locations for the groups
    ind = np.arange(N)
    width = 0.35
    p1 = plt.bar(ind, svruptime, width)

    plt.ylabel('Uptime in Days')
    plt.title('Uptime of Servers in Days')
    plt.xticks(ind, xtick)
    # probably want to turn this into a log scale
    plt.yticks(np.arange(0, 20, 1))
    t = time.time()
    # added a timestamp to differentiate
    plt.savefig(f'static/status{t}.png')
    return render_template('graph.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
