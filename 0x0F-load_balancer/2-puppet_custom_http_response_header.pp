# Puppet manifest to add a custom HTTP header with the server hostname

# Define a class for configuring Nginx with a custom HTTP header
class nginx_custom_header {

  # Install the facter gem to enable Facter to gather facts about the system
  package { 'facter':
    ensure => installed,
  }

  # Define a custom fact to get the server hostname
  file { '/etc/facter/facts.d/server_hostname.txt':
    ensure  => file,
    content => "server_hostname=$(hostname)",
  }

  # Install Nginx
  package { 'nginx':
    ensure => installed,
  }

  # Define the custom HTTP header in Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;

        location / {
          add_header X-Served-By $server_hostname;
          try_files \$uri \$uri/ =404;
        }

        error_page 404 /error_404.html;
        location = /error_404.html {
          internal;
        }
      }
    ",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Remove the default Nginx default site configuration
  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    notify => Service['nginx'],
  }

  # Restart Nginx to apply the changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Apply the nginx_custom_header class
include nginx_custom_header
