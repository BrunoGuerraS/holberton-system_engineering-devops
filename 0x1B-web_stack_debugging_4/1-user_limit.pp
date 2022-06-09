# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec {'broken-limit':
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 500/" /etc/security/limits.conf &&
            sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 400/" /etc/security/limits.conf'
  
  provider => shell,
}
