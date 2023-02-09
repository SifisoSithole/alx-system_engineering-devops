# Increases the amount of traffic

exec { 'increase_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
