#!/bin/python3

import boto3
import json

def tag(ec2):
    services = []
    for instance in ec2.instances.filter(Filters=[]):
        for tags in ec2.Instance(instance.id).tags:
            if tags["Key"] == 'Ansible':
                name = tags["Value"]
                if name not in services:
                    services.append(name)
    return services
def hosts(ec2,service):
#ansible is the tag name in AWS
    node = {'Name':'tag:Ansible','Values':[service]}
    host = []
    for instance in ec2.instances.filter(Filters=[node]):
        host.append(instance.public_ip_address)
    return host
def aws():
#change region-name as per your need
    ec2 = boto3.resource("ec2",region_name='ap-southeast-1')
    services = tag(ec2)
    groups = {}
    for service in services:
        grp = hosts(ec2,service)
        groups[i] = {
                    'hosts':grp
                    }
    print(groups)
if __name__ == "__main__":
    aws()
    
