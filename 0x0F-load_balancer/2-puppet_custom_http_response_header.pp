# Puppet manifest to add a custom HTTP header with the server hostname

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => File['/etc/nginx/sites-available/default'],
}

exec { 'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
