# Define the settings that would be passed via command line here. 
# Simply omit key-value pairs for the to default
settings_dict = {'username'     : 'USERNAME',
                 'timeout'      : 10,
                 'numthreads'   : 1,
                 'connections'  : 1,
                 'authurl'      : 'https://auth.api.rackspacecloud.com/v1.0',
                 'file_level'   : 'DEBUG',
                 'key'          : 'API_KEY_GOES_HERE',
                 'servicenet'   : False,
                 'useragent'    : 'com.whmcr.cloudsync',
                 'log_file'     : './cloud-sync.log',
                 'console_level': 'DEBUG',
                 'md5'          : True,
                 'exclude_paths': [ '\.svn', '\.git', ],
                }

# Arguments can also be defined. 
# format: [ 'source', 'destination' ]
op_args = ['/some/file/path', 'swift://some_container']


