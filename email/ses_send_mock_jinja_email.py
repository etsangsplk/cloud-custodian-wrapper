#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jinja2
import boto3
import os
import sys
import yaml

from dateutil import parser
from dateutil.tz import gettz
from easyprocess import EasyProcess
from email.mime.text import MIMEText
from tidylib import tidy_document

reload(sys)
sys.setdefaultencoding('UTF8')


def date_time_format(utc_str, tz_str='US/Eastern', format='%Y %b %d %H:%M %Z'):
    return parser.parse(utc_str).astimezone(gettz(tz_str)).strftime(format)


def get_date_time_delta(delta):
    return str(datetime.datetime.now().replace(tzinfo=gettz('UTC')) + datetime.timedelta(delta))


jinja2.filters.FILTERS['date_time_format']    = date_time_format
jinja2.filters.FILTERS['get_date_time_delta'] = get_date_time_delta


email_metadata = {
    'account': 'aws_account_03',
    'region': 'us-east-2',
    'ec2': {
        'policy': {u'actions': [{u'to': [u'resource-owner', u'ldap_uid_tags'], u'type': u'notify', u'transport': {u'queue': u'https://sqs.us-east-1.amazonaws.com/172119256206/cloudcustodian-mailer', u'type': u'sqs'}, u'template': u'default.html', u'subject': u'URGENT: Your AWS EC2 Resources will be shutdown.'}, {u'type': u'mark-for-op', u'days': 1, u'op': u'stop'}], u'resource': u'ec2', u'name': u'ec2-tag-compliance-mark', u'filters': [{u'State.Name': u'running'}, {u'tag:auto:custodian:maid-status': u'absent'}, {u'tag:BusinessUnit': u'absent'}, {u'tag:Environment': u'absent'}, {u'tag:Project': u'absent'}, {u'tag:OwnerEmail': u'absent'}], u'description': u'Schedule a resource that does not meet tag compliance policies\nto be stopped in one day.\n'},
        'action': {u'to': [u'resource-owner', u'ldap_uid_tags'], u'type': u'notify', u'transport': {u'queue': u'https://sqs.us-east-1.amazonaws.com/172119256206/cloudcustodian-mailer', u'type': u'sqs'}, u'template': u'default.html', u'subject': u'URGENT: Your AWS EC2 Resources will be shutdown.'},
        'resources': [
            {
                'Monitoring': {
                    'State':'disabled'
                },
                'PublicDnsName':'ec2-52-15-151-43.us-east-2.compute.amazonaws.com',
                'State':{
                    'Code':16,
                    'Name':'running'
                },
                'EbsOptimized':False,
                'LaunchTime':'2017-06-01T21:01:39+00:00',
                'PublicIpAddress':'52.15.151.43',
                'PrivateIpAddress':'172.31.11.109',
                'ProductCodes':[

                ],
                'VpcId':'vpc-e66ce98f',
                'StateTransitionReason':'',
                'InstanceId':'i-06190438c9cfe79c7',
                'EnaSupport':True,
                'ImageId':'ami-618fab04',
                'PrivateDnsName':'ip-172-31-11-109.us-east-2.compute.internal',
                'KeyName':'richard_gooch',
                'SecurityGroups':[
                    {
                        'GroupName':'launch-wizard-3',
                        'GroupId':'sg-a2bc95cb'
                    }
                ],
                'ClientToken':'zbxuO1496350898699',
                'SubnetId':'subnet-9cff75f5',
                'InstanceType':'t2.nano',
                'NetworkInterfaces':[
                    {
                        'Status':'in-use',
                        'MacAddress':'02:d2:88:f4:2a:cb',
                        'SourceDestCheck':True,
                        'VpcId':'vpc-e66ce98f',
                        'Description':'',
                        'NetworkInterfaceId':'eni-074a166f',
                        'PrivateIpAddresses':[
                            {
                                'PrivateDnsName':' ip-172-31-11-109.us-east-2.compute.internal',
                                'PrivateIpAddress':'172.31.11.109',
                                'Primary':True,
                                'Association':{
                                    'PublicIp':'52.15.151.43',
                                    'PublicDnsName':'ec2-52-15-151-43.us-east-2.amazonaws.com',
                                    'IpOwnerId':'amazon'
                                }
                            }
                        ],
                        'PrivateDnsName':'ip-172-31-11-109.us-east-2.compute.internal',
                        'Attachment':{
                            'Status':'attached',
                            'DeviceIndex':0,
                            'DeleteOnTermination':True,
                            'AttachmentId':'eni-attach-6e498e87',
                            'AttachTime':'2017-06-01T21:01:39+00:00'
                        },
                        'Groups':[
                            {
                                'GroupName':'launch-wizard-3',
                                'GroupId':'sg-a2bc95cb'
                            }
                        ],
                        'Ipv6Addresses':[

                        ],
                        'OwnerId':'830317098777',
                        'PrivateIpAddress':'172.31.11.109',
                        'SubnetId':'subnet-9cff75f5',
                        'Association':{
                            'PublicIp':'52.15.151.43',
                            'PublicDnsName':'ec2-52-15-151-43.us-east-2.compute.amazonaws.com',
                            'IpOwnerId':'amazon'
                        }
                    }
                ],
                'SourceDestCheck':True,
                'Placement':{
                    'GroupName':'',
                    'Tenancy':'default',
                    'AvailabilityZone':'us-east-2a'
                },
                'Hypervisor':'xen',
                'BlockDeviceMa ppings':[
                    {
                        'DeviceName':'/dev/sda1',
                        'Ebs':{
                            'Status':'attached',
                            'DeleteOnTermination':True,
                            'VolumeId':'vol-038ed85488b0174b2',
                            'AttachTime':'2017-06-01T21:01:39+00:00'
                        }
                    }
                ],
                'Architecture':'x86_64',
                'MatchedFilters':[
                    'State.Name',
                    'tag:auto:custodian:maid-status',
                    'tag:BusinessUnit',
                    'tag:Environment',
                    'tag:Project',
                    'tag:OwnerEmail'
                ],
                'RootDeviceType':'ebs',
                'RootDeviceName':'/dev/sda1',
                'VirtualizationType':'hvm',
                'Tags':[
                    {
                        'Key':'CreatorName',
                        'Value':'john_theodore'
                    },
                    {
                        'Key':'CreatorId',
                        'Value':'AIDAIBV3GV5HG5HEIZOO'
                    }
                ],
                'AmiLaunchIndex':0
            }
        ]
    },
    'ebs': {
        'resources': [{
            u'Attachments': [],
            u'AvailabilityZone':
            u'us-east-2a',
            u'CreateTime':
            u'2017-03-09T22:48:46.487000+00:00',
            u'Encrypted':
            False,
            u'Iops':
            300,
            u'MatchedFilters': [u'Attachments', u'tag:auto:custodian:maid-status'],
            u'Size':
            100,
            u'SnapshotId':
            u'',
            u'State':
            u'available',
            u'Tags': [
                {
                    u'Key': u'OwnerEmail',
                    u'Value': u'alice@example.com'
                },
                {
                    u'Key': u'auto:custodian:maid-status',
                    u'Value': u'Resource does not meet policy: delete@2017/04/30'
                }
            ],
            u'VolumeId':
            u'vol-xxxx001',
            u'VolumeType':
            u'gp2'
        }, {
            u'Attachments': [],
            u'AvailabilityZone':
            u'us-east-2a',
            u'CreateTime':
            u'2017-03-14T22:02:34.066000+00:00',
            u'Encrypted':
            False,
            u'Iops':
            300,
            u'MatchedFilters': [u'Attachments', u'tag:auto:custodian:maid-status'],
            u'Size':
            100,
            u'SnapshotId':
            u'',
            u'State':
            u'available',
            u'Tags': [
                {
                    u'Key': u'OwnerEmail',
                    u'Value': u'alice@example.com'
                },
                {
                    u'Key': u'auto:custodian:maid-status',
                    u'Value': u'Resource does not meet policy: delete@2017/04/30'
                }
            ],
            u'VolumeId':
            u'vol-xxxx002',
            u'VolumeType':
            u'gp2'
        }],
        'policy': {
            u'actions': [{
                u'subject':
                u'URGENT: Your AWS Resources will be shutdown.',
                u'template':
                u'jinja_template.j2',
                u'to': [u'resource-owner', u'resource-group'],
                u'transport': {
                    u'queue':
                    u'https://sqs.us-east-1.amazonaws.com/xxxxxx/cloudcustodian-mailer',
                    u'type':
                    u'sqs'
                },
                u'type':
                u'notify'
            }, {
                u'days': 30,
                u'op': u'delete',
                u'type': u'mark-for-op'
            }],
            u'comments':
            u'Mark any unattached EBS volumes for deletion in 3 days.\nVolumes set to not delete on\
              instance termination do have\nvalid use cases as data drives, but 99% of the time\
              they\nappear to be just garbage creation.\n',
            u'filters': [{
                u'Attachments': []
            }, {
                u'tag:auto:custodian:maid-status': u'absent'
            }],
            u'name':
            u'ebs-mark-unattached-deletion',
            u'resource':
            u'ebs'
        },
        'action': {
            u'subject': u'URGENT: Your AWS Resources will be shutdown.',
            u'template': u'jinja_template.j2',
            u'to': [u'resource-owner', u'resource-group'],
            u'transport': {
                u'queue':
                u'https://sqs.us-east-1.amazonaws.com/172119256206/cloudcustodian-mailer',
                u'type':
                u'sqs'
            },
            u'type': u'notify'
        }
    }
}


def get_file_data(file):
    with open(file) as jinja_template_file:
        file_data = jinja_template_file.read()
        jinja_template_file.close()
    return file_data


def write_file(file_data, file_dest):
    f = open(file_dest, 'w')
    f.write(file_data)
    f.close()


def get_custodian_policy_email(email_template_data, resources, policy, action,
                               account, region):
    custodian_html_email_jinja_template = jinja2.Template(email_template_data)
    return custodian_html_email_jinja_template.render(
        resources=resources,
        policy=policy,
        action=action,
        account=account,
        region=region)


def get_ses_credentials():
    ses_credentials = {}
    secrets_file = open('/secrets/aws-secrets.yml', 'r')
    secrets = yaml.load(secrets_file)
    secrets_file.close()
    ses_credentials['AWS_ACCESS_KEY_ID'] = secrets['accounts'][secrets[
        'aws_custodian_account']]['AWS_ACCESS_KEY_ID']
    ses_credentials['AWS_SECRET_ACCESS_KEY'] = secrets['accounts'][secrets[
        'aws_custodian_account']]['AWS_SECRET_ACCESS_KEY']
    return ses_credentials


def ses_send_email(email_to, email_from, email_subject, email_body,
                   ses_credentials):
    # the 'html' option ensures the email gets rendered as html, and no plain
    # text
    message = MIMEText(email_body.encode('utf-8'), 'html')
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = email_subject
    message['X-Priority'] = '1'
    ses_credentials = get_ses_credentials()
    aws_access_key_id = ses_credentials['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = ses_credentials['AWS_SECRET_ACCESS_KEY']
    ses_connection = boto3.client(
        'ses',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-east-1')
    return ses_connection.send_raw_email(
        RawMessage={'Data': message.as_string()})


def get_gleemail_template():
    cmd = [
        '../node_modules/gleemail/bin/gleemail', 'render',
        'custodian-email-template', '-r', 'mustache'
    ]
    shell_fork = EasyProcess(
        cmd, cwd='/custodian/email/gleemail-custodian').call(timeout=10)
    exit_code = shell_fork.return_code
    if exit_code != 0:
        msg = 'Failed to render gleemail template using command: %s\n\n' % str(
            cmd)
        sys.exit(msg)
    ugly_jinja_html = shell_fork.stdout
    return ugly_jinja_html


def get_final_rendered_email_message(unrendered_email_message, resource_type):
    return get_custodian_policy_email(
        final_unrendered_email_template,
        resources=email_metadata[resource_type]['resources'],
        policy=email_metadata[resource_type]['policy'],
        action=email_metadata[resource_type]['action'],
        account=email_metadata['account'],
        region=email_metadata['region'])


def get_final_unrendered_email_message():
    rendered_gleemail = get_gleemail_template()
    rendered_gleemail = '%s%s' % (
        '<!DOCTYPE html>',
        rendered_gleemail)
    jinja_template = get_file_data(
        'email/gleemail-custodian/templates/'
        'custodian-email-template/resources_table.jinja'
        # '/custodian/email/jinja_template.j2'
    )
    final_unrendered_email_template = rendered_gleemail.replace(
        'custodianresourcetable', jinja_template)
    env_vars = ['COMPANY_NAME', 'COMPANY_LOGO_URL', 'COMPANY_TAGGING_POLICY_URL']
    for env_var in env_vars:
        env_var_value = os.environ.get(env_var, None)
        if not env_var_value:
            exit_msg = 'Missing ENV variable: %s' % env_var
            sys.exit(exit_msg)
        final_unrendered_email_template = final_unrendered_email_template.replace(
            env_var, env_var_value
        )
    return final_unrendered_email_template


def tidylib_validate_html(rendered_html_data):
    document, errors = tidy_document(rendered_html_data, options={'numeric-entities':1})
    if errors:
        print(rendered_html_data)
        print(errors)
        sys.exit(1)
    else:
        sys.exit(0)


custodian_mail_template_location = '/custodian/email/jinja_template.j2'
final_unrendered_email_template = get_final_unrendered_email_message()
resource_type = os.environ.get('RESOURCE_TYPE', None)
if not resource_type:
    print('Need to set env RESOURCE_TYPE=ec2 or some other resource')
    sys.exit(0)
final_rendered_email_template = get_final_rendered_email_message(
    final_unrendered_email_template,
    resource_type
)

validate = bool(os.environ.get('EMAIL_VALIDATE', False))
if validate:
    tidylib_validate_html(final_rendered_email_template)

email_to = os.environ.get('EMAIL_TO', False)
email_from = os.environ.get('EMAIL_FROM', False)
if not email_to or not email_from:
    sys.exit(
        'Need to set ENV variables EMAIL_TO and EMAIL_FROM, eg: EMAIL_TO=john@example.com'
        ' EMAIL_FROM=ses_allowed_email@example.com ./ses_send_mock_jinja_email.py'
    )

write_file(
    file_data=final_unrendered_email_template,
    file_dest=custodian_mail_template_location)

ses_send_email(
    email_to=email_to,
    email_from=email_from,
    email_subject='test subject',
    email_body=final_rendered_email_template,
    ses_credentials=get_ses_credentials())
