Livability actions
===================

These ansible playbooks are setup to start/stop the livability app on the configured dreamhost servers.

You will need to create a SSH key and grant it authorization to the app admin account.  Contact Dan for instructions.

### Starting Livability App
This assumes basic Ansible knowledge.  You can run this playbook at any time.  The script will check if
the app is running already - if so, it will do nothing - if not, it will start the app. 
```
[playbooks (master)]$ ansible-playbook -i inventory.yml start_livability.yml 

PLAY [Action livability database app] ***********************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************
ok: [ps458685.dreamhostps.com]

TASK [Get livability database status] ***********************************************************************************************************************************************************
fatal: [ps458685.dreamhostps.com]: FAILED! => {"changed": true, "cmd": "ps aux | grep /home/ssa_admin/SafeStatesLivability | grep -v grep", "delta": "0:00:00.010873", "end": "2018-10-31 07:03:29.852696", "msg": "non-zero return code", "rc": 1, "start": "2018-10-31 07:03:29.841823", "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
...ignoring

TASK [Start livability database] ****************************************************************************************************************************************************************
changed: [ps458685.dreamhostps.com]

PLAY RECAP **************************************************************************************************************************************************************************************
ps458685.dreamhostps.com   : ok=3    changed=2    unreachable=0    failed=0   

```

The livability app will be running at this point.

### Stopping the Livability App
There has not been a need to stop the app.  But just in case:
```
[playbooks (master)]$ ansible-playbook -i inventory.yml stop_livability.yml 

PLAY [Action livability database app] ***********************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************
ok: [ps458685.dreamhostps.com]

TASK [Get livability database status] ***********************************************************************************************************************************************************
ok: [ps458685.dreamhostps.com]

TASK [Stop livability database] *****************************************************************************************************************************************************************
changed: [ps458685.dreamhostps.com]

PLAY RECAP **************************************************************************************************************************************************************************************
ps458685.dreamhostps.com   : ok=3    changed=1    unreachable=0    failed=0   
```

The livability app will be stopped at this point.