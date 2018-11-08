import time

#I am executing "make target" here
ptimer = ProcessTimer(['make','target'])

try:
  ptimer.execute()
  #poll as often as possible; otherwise the subprocess might 
  # "sneak" in some extra memory usage while you aren't looking
  while ptimer.poll():

    time.sleep(.5)
finally:
  #make sure that we don't leave the process dangling?
  ptimer.close()

print 'return code:',ptimer.p.returncode
print 'time:',ptimer.t1 - ptimer.t0
print 'max_vms_memory:',ptimer.max_vms_memory
print 'max_rss_memory:',ptimer.max_rss_memory