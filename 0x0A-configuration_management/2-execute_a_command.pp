# 2-execute_a_command.pp
# Puppet manifest to kill a process named killmenow using pkill.

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'pgrep -f killmenow',
}
