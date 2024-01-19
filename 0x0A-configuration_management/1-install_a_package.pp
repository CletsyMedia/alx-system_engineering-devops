#!/usr/bin/pup
# 1-install_a_package.pp
# Puppet manifest to install Flask from pip3 with a specific version.

package { 'Flask':
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options => ['--user'],
}

package { 'Werkzeug':
  ensure          => '2.1.1',
  provider        => 'pip3',
  install_options => ['--user'],
}
