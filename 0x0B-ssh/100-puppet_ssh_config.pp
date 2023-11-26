# 100-puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile /home/vagrant/.ssh/school',
  match  => '^#?IdentityFile',
}
