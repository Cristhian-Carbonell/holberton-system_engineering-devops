# Client configuration file (w/ Puppet)
include stalib
file_line { 'Use_private_key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'Refuse_password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
