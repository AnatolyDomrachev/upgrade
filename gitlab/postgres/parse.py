import yaml

with open("pg_hba.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        
    except yaml.YAMLError as exc:
        print(exc)

for db in data['local'] :
    for user in data['local'][db] :
       print( 'local    ' + db + '   ' + user   + '    peer')

for db in data['host'] :
    for user in data['host'][db] :
        for ip in data['host'][db][user] :
           print( 'host    ' + db + '   ' + user   + '    ' + ip + '    md5')
