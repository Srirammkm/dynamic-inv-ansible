# dynamic-inv-ansible
fetch the IPs of VMs in AWS using TAG. Tags can be changed dynamically this python script will fetch IPs without any manual editing of script.
export AWS_ACCESS_KEY_ID='AK123'
export AWS_SECRET_ACCESS_KEY='abc123'

change configuration in ansible.cfg file
* change private_key_path = /path/to/key
* change user remote_user = username

In playbook.yml (here nginx.yml)
define host and give default value. so that you can pass the host as arg variable 
ex: ansible-playbook -i fhost.py nginx.yml -e service=node
in this the task will execute only on host named NODE eventhough our script exract IPs of all the machines running on cloud(AWS)


