# Using Puppet, create a manifest that kills a process named killmenow

exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/local/bin/:/bin/',
} 
