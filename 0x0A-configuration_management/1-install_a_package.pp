# install_puppet_lint.pp

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
