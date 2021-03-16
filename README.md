# dynamic-inv-ansible
fetch the IPs of VMs in AWS using TAG. Tags can be changed dynamically this python script will fetch IPs without any manual editing of script.
export AWS_ACCESS_KEY_ID='AK123'
export AWS_SECRET_ACCESS_KEY='abc123'

change configuration in ansible.cfg file
* change private_key_path = /path/to/key
* change user remote_user = username

