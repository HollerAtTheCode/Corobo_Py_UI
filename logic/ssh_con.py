import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.connect('10.10.10.10', username='niryo', password='robotics')

stdin, stdout, stderr = ssh_client.exec_command('python niryo_script_01 A2 A1')