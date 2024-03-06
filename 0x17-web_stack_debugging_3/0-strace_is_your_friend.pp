exec {'fix-wordpress':
command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
notify  => Service['apache2'],
}

service {'apache2':
ensure => 'running',
