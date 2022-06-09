# Sky is the limit, let's bring that limit higher
exec { 'Change limit':
  command  => 'sed -i s/15/4096/ /etc/default/nginx && sudo service nginx restart',
  provider => shell
}
