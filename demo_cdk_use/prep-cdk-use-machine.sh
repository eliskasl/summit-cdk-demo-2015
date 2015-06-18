#!/usr/bin/env bash

sudo yum install -y tree
sudo yum install -y vagrant vagrant-doc vagrant-libvirt vagrant-libvirt-doc
sudo cp -vf /usr/share/vagrant/gems/doc/vagrant-libvirt-0.0.26/polkit/10-vagrant-libvirt.rules /etc/polkit-1/rules.d/
sudo yum install -y @development-tools ruby-devel ruby-libvirt rubygem-ruby-libvirt libvirt-devel rubygem-unf_ext
vagrant plugin install vagrant-atomic
vagrant plugin install vagrant-registration --plugin-version 0.0.11
vagrant box add --force --name 'rhel-atomic-7' ~/rhel-atomic-libvirt-7.1-1.x86_64.box
vagrant box add --force --name 'rhel-server-7' ~/rhel-server-libvirt-7.1-1.x86_64.box
