# download Using Puppet

package { 'screen':
 ensure   => '2.5.0',
 provider => 'gem',
 source   => 'http://rubygems.org/',
}
