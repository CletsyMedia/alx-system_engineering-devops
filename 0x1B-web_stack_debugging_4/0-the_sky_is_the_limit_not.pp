# Increasing the amount of traffic an Nginx server should handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  # Modification of the ULIMIT value for Nginx server
  command => '/bin/sed -i "s/ulimit -n 15/ulimit -n 4096/" /etc/default/nginx',
  # Specificity for the path
  path    => '/usr/local/bin/:/bin/',
}

# Restarting Nginx server
exec { 'restart-nginx':
  # Restarting Nginx server
  command => '/etc/init.d/nginx restart',
  # Specificity for the path to initialize the script
  path    => '/etc/init.d/',
}
