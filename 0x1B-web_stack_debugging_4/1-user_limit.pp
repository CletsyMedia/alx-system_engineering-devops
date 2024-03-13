# Puppet manifest to change the OS configuration for the holberton user

# Define the maximum number of file descriptors
$desired_file_limit = 4096

# Change the OS configuration for the holberton user
exec { 'increase-hard-file-limits-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limits for holberton-user
exec { 'increase-soft-file-limits-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

