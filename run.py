#!/usr/bin/python
import subprocess, datetime, shutil, sys, os
from subprocess import Popen, PIPE

# usage: ./run,py <command_file> <num_trials> [<wait_list>]
# wait list specifies which commands in the pipeline should be waited on. defaults to all 1s

MKDIR_BEFORE = True
NUM_TRIALS = int(sys.argv[2])
delta_sum = datetime.timedelta(0)
DIRTY = ['ansible'] # you edit this
wait_list = map(lambda x: int(x), sys.argv[3:])
if len(wait_list) == 0: wait_list = [1 for c in commands]


# generic directory cleanup
def cleanup(file_dir_list=DIRTY):
    for item in file_dir_list:
        if os.path.isfile(item):
            os.remove(item)
        elif os.path.isdir(item):
            shutil.rmtree(item)
            if MKDIR_BEFORE:
                os.makedirs('ansible')
    return 'success'


with open(sys.argv[1], 'ro') as cmd_file:
    command_str = cmd_file.read().strip('\n').strip(' ')
    commands = command_str.split('|')
    print 'Starting execution of command:\n', command_str, '\n'

print 'cleaning up: ', cleanup()

for x in range(NUM_TRIALS):
    proc_list = []
    start = datetime.datetime.now()

    for i in range(len(commands)):
        cmd = filter(lambda str: str != '', commands[i].split(' '))
        print 'cmd: ', cmd, 'wait: ', wait_list
        if i == 0: p = Popen(cmd, stdout=PIPE);
        else: p = Popen(cmd, stdin=proc_list[i-1].stdout, stdout=PIPE);
        if wait_list[i] == 1: p.wait();
        proc_list.append(p)

    end = datetime.datetime.now()
    delta = end - start
    delta_sum += delta

    print 'cleaning up: ', cleanup()
    print 'Trial', (x + 1), ':', delta, '\n'

print 'Finished execution. Overall:', delta_sum/NUM_TRIALS
