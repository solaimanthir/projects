import re
import paramiko

def connect_and_fetch_cmd_log(name, pwd, ipaddr, cmd):
    result = ""
    ssh_client = paramiko.SSHClient()

    # read keys from local "known hosts" file.
    ssh_client.load_system_host_keys()

    # set the policy to use when receiving a host key from a previously-unknown server
    #add the SSH host key in case if it is missing.
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    conn_try_limit = 10

    for i in range(conn_try_limit):
        try:
            print("connecting to device...Attempt#{}".format(i+1))

            #establish connection to device using username and password.
            ssh_client.connect(ipaddr, 
                        username=name, 
                        password=pwd,
                        look_for_keys=False )
            
            #connection is established. Run the command now.
            stdin, stdout, stderr = ssh_client.exec_command(cmd)

            #take the output of the executed command
            result = stdout.readlines()
            break

        except Exception as err:
            print("An error has occured...{}".format(err))
            print('\n')

    #close the client object and return result
    ssh_client.close()
    return result

#..........................................................

#use a valid login name in the device
login_name = "device_login"
#use a valid login password for the device
login_pwd = "device_pwd"
#a valid ipv4 address
login_ip = "172.16.12.8" 
cmd_str = "show running-configuration"

#main code
get_result = connect_and_fetch_cmd_log(login_name, login_pwd, login_ip, cmd_str)

#print result
# check if string is empty or contain spaces only
if not get_result or re.search("^\s*$", get_result):
    print('no output')
else:
    print(get_result)
