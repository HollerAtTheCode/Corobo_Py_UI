import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.10.10.10', username='niryo', password='robotics')
stdin, stdout, stderr = ssh_client.exec_command('python ~/scripts/try.py A1')


for line in stdout.read().splitlines():
    print(line)

