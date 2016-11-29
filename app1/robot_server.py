import os
import psutil
import time
import socket
import requests

from subprocess import Popen, STDOUT
from .models import Daemon

from django.conf import settings

def check_url(url):
    try:
        r = requests.head(url)
        return True
    except :
        return False

def find_local_ip(host=None):
    # see here: http://stackoverflow.com/questions/166506/
    try:
        if host is None:
            host = socket.gethostname()

        if 'local' not in host:
            host += '.local'

        try:
            ips = [ip for ip in socket.gethostbyname_ex(host)[2]
                   if not ip.startswith('127.')]
            if len(ips):
                return ips[0]
        except socket.gaierror:
            logger.debug('socket gaierror with hostname {}'.format(host))
            pass

        # If the above method fails (depending on the system)
        # Tries to ping google DNS instead (need a internet connexion)
        try:
            with closing(socket.socket()) as s:
                s.settimeout(1)
                s.connect(('8.8.8.8', 53))
                return s.getsockname()[0]
        except socket.timeout:
            logger.debug('socket timeout')
            pass

    except IOError as e:
        # network unreachable
        # error no 10065 = WSAESERVERUNREACH Windows Network unreachable
        if e.errno == errno.ENETUNREACH or e.errno == 10065:
            logger.debug('network unreachable')
            pass
        else:
            raise
    return '127.0.0.1'

class Server(object):
    def __init__(self, type, robot, simulator='no'):
        self.robot = robot
        self.daemon = Daemon.objects.get(type=type, simulator=simulator )

    def get_command(self):
        if self.daemon.type == 'jupyter':
            cmd = [
            'jupyter',
            'notebook',
            '--no-browser',
            '--ip=0.0.0.0',
            '--notebook-dir={}'.format(settings.PYTHON_ROOT)
            ]
            return cmd
        cmd = [
            'poppy-services',
            (self.robot.brand+'-'+self.robot.creature).lower(),
            '--'+self.daemon.type,
            '--no-browser',
        ]

        if not self.robot.camera:
            cmd += ['--disable-camera']

        if not 'no' in self.daemon.simulator:
            cmd += ['--'+self.daemon.simulator]

        return cmd

    def start(self):
        if 'running' in self.state():
            self.daemon.log += (  '{} : pidfile {} already exist. '
                              'Daemon already running.<br>'.format(time.strftime(
                              "%y/%m/%d %H:%M", time.localtime()),self.daemon.pid))
            self.daemon.save()
            return False

        else :
            if self.daemon.logfile=='none':
                FNULL = open(os.devnull, 'w')
                p = Popen(self.get_command(), stdout=FNULL, stderr=STDOUT)
            else :
                with open(os.path.join(settings.LOG_ROOT, self.daemon.logfile+
                self.daemon.type+'_'+self.robot.creature+'.log'), 'w') as log:
                    p = Popen(self.get_command(), stdout=log, stderr=STDOUT)
            self.daemon.pid = p.pid
            self.daemon.log += (  '{} : Daemon is now running with pid {}<br>'.
            format(time.strftime("%y/%m/%d %H:%M", time.localtime()),self.daemon.pid))
            self.daemon.save()
            return True

    def stop(self):
        if 'running' in self.state():
            try:
                p = psutil.Process(self.daemon.pid)
            except psutil.NoSuchProcess:
                return
            p_children = p.children(recursive=True)
            for process in p_children:
                process.kill()
            try :
                p.kill()
            except psutil.NoSuchProcess:
                pass
            time.sleep(1)
            
            if 'stopped' in self.state() :
                self.daemon.pid = -1
                self.daemon.log = ''
                self.daemon.save()
                return True
            else : 
                self.daemon.log += (  '{} : kill unsuccesfull. '
                                'Daemon always running.<br>'.format(time.strftime(
                                "%y/%m/%d %H:%M", time.localtime())))
                self.daemon.save()
                return False
        else :
            self.daemon.pid = -1
            self.daemon.log = ''
            self.daemon.save()
            return False
        
    def state(self):
        if psutil.pid_exists(self.daemon.pid):
            p = psutil.Process(self.daemon.pid)
            return 'Robot daemon is {}.'.format('running' if not p.status()=='zombie' else'stopped')
        else :
            return 'Robot daemon is stopped.'