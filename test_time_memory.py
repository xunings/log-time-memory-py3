import time
from ProcessTimer import *

ptimer = ProcessTimer(['./bin','arg1', 'arg2'])

try:
  ptimer.execute()
  #poll as often as possible; otherwise the subprocess might 
  # "sneak" in some extra memory usage while you aren't looking
  while ptimer.poll():

    time.sleep(.1)
finally:
  #make sure that we don't leave the process dangling?
  ptimer.close()

print('return code: {}'.format(ptimer.p.returncode) )
print('time: {}'.format(ptimer.t1 - ptimer.t0) )
print('max_vms_memory: {}'.format(ptimer.max_vms_memory) )
print('max_rss_memory: {}'.format(ptimer.max_rss_memory) )