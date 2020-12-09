# Client configuration file (w/ Puppet)
include stalib

file_line { 'private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
