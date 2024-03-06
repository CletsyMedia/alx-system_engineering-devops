# Puppet manifest to fix the issue identified with strace

# Replace bad "phpp" extension to "php" in "wp-settings.php".
exec { 'fix_wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}

# Notify a service restart if necessary
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Exec['fix_wordpress'],
}

