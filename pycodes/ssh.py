import paramiko


def ssh(command):
    global client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('211.211.211.211', 1999,
                   username='username', password='password')
    stdin, stdout, stderr = client.exec_command(command)
    result = stdout.read().decode() if stdout else stderr.read().decode()
    return result


print(ssh('ls -alh').strip())
client.close()
