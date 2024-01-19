# 0-create_a_file.pp
# Puppet manifest to create a file in /tmp with specific permissions and content.

# Create a file in /tmp
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
