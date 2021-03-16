#!/bin/python3

import boto3
import json

def hosts(ec2,i):
    n = {'Name':'tag:Ansible','Values':[i]}
    host=[]
    for i in ec2.instances.filter(Filters=[n]):
        host.append(i.public_ip_address)
    return host
def main():
    ec2 = boto3.resource("ec2",region_name='ap-southeast-1')
   # master_group = hosts(ec2,"master")
    service = ['node','master']
    groups = {}
    for i in service:
        grp = hosts(ec2,i)
        groups[i] = {
                    'hosts':grp
                    }
    print(groups)

if __name__ == "__main__":
    main()
    
