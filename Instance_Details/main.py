import json,requests as rq,subprocess,platform

def is_vpn_connected():
        system = platform.system()
        
        if system == "Windows":
            try:
                # Method 1: Check for common VPN adapter keywords
                result = subprocess.run(
                    ['powershell', 'Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Select-Object Name, InterfaceDescription'],
                    capture_output=True,
                    text=True
                )
                output = result.stdout.lower()
                
                # Check for common VPN indicators
                vpn_keywords = ['vpn', 'tap', 'tun', 'cisco', 'anyconnect', 'wireguard', 
                                'openvpn', 'fortinet', 'palo alto', 'checkpoint', 'pulse',
                                'virtual adapter', 'sonicwall', 'globalprotect']
                
                for keyword in vpn_keywords:
                    if keyword in output:
                        return True
                
                # Method 2: Check VPN connections
                vpn_check = subprocess.run(
                    ['powershell', 'Get-VpnConnection | Where-Object {$_.ConnectionStatus -eq "Connected"}'],
                    capture_output=True,
                    text=True
                )
                if vpn_check.stdout.strip():
                    return True
                
                # Method 3: Check for MetricStream specific domain access
                try:
                    test_response = rq.get('http://instances.rnd.metricstream.com:3000/', timeout=2)
                    return True
                except:
                    pass
                return False
            except Exception as e:
                print(f"Error checking VPN: {e}")
                return False
        elif system == "Linux":
            try:
                result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
                return 'tun' in result.stdout or 'tap' in result.stdout
            except Exception as e:
                print(f"Error: {e}")
                return False
        return False

def get_instance_data(instance,url = 'http://instances.rnd.metricstream.com:3000/instances/'):
    if is_vpn_connected() == True:
        print("✓ VPN is connected")
        if instance == None:
            instance = input("Enter you instance name : ")
        input_choice = input("Available Choices \nDB, SSH, Both, Mongo \nEnter your choice : ")
        response = rq.get(url + instance)

        data = response.json()
        jd = data['rows'][0][4]['DB'].split(':')

        match input_choice.lower():
            case 'db':
                db_data =data['rows'][0][4]['DB'].split(':')
                print(f"DB Host: {db_data[0]} \nDB Port: {db_data[1]}")
            case 'ssh':
                ssh_data =data['rows'][0][4]['SSH'].split(':')
                print(f"SSH Host: {ssh_data[0]} \nSSH Port: {ssh_data[1]}")
            case 'both':
                db_data =data['rows'][0][4]['DB'].split(':')
                ssh_data =data['rows'][0][4]['SSH'].split(':')
                print(f"DB Host: {db_data[0]} \nDB Port: {db_data[1]}")
                print(f"SSH Host: {ssh_data[0]} \nSSH Port: {ssh_data[1]}")
            case 'mongo':
                mongo_data =data['rows'][0][4]['MongoDB'].split(':')
                print(f"mongo Host: {mongo_data[0]} \nmongo Port: {mongo_data[1]}")
            case _:
                print("Invalid choice")
        print('*='*50)
    else:
        print("✗ VPN is not connected")