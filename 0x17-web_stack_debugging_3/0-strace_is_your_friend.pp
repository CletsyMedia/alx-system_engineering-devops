# Puppet manifest to fix Apache 500 error

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running
service { 'apache2':
  ensure => running,
}

# Define a file resource to fix the issue in Apache configuration
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  content => template('apache2/apache2.conf.erb'),
  require => Package['apache2'],
  notify  => Service['apache2'],
}

# Define the Apache virtual host configuration
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => template('apache2/000-default.conf.erb'),
  require => Package['apache2'],
  notify  => Service['apache2'],
}

# Restart Apache service after configuration changes
exec { 'restart_apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => [File['/etc/apache2/apache2.conf'], File['/etc/apache2/sites-available/000-default.conf']],
}

