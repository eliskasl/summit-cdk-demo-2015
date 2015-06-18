#!/usr/bin/env python

import sys, os
sys.path.append("../")

from demo_runner import Demo

class CDKDemo(Demo):
    def run_demo(self):
        self.print_comment(
            """first we install Vagrant from the regular Fedora repositories. Vagrant is available in
               the main Fedora repos since Fedora 21. Vagrant is also available at vagrantup.com for
               other platforms.""")
        self.print_and_exec_cmd("yum install -y vagrant vagrant-doc vagrant-libvirt vagrant-libvirt-doc")

        self.print_comment(
            """Now we want to make it so that we can operate libvirt as a normal user. This is a
               requirement of vagrant.""")
        self.print_and_exec_cmd("cp -vf /usr/share/vagrant/gems/doc/vagrant-libvirt-0.0.26/polkit/10-vagrant-libvirt.rules /etc/polkit-1/rules.d/")

        self.print_comment(
            """Now we want to install a few useful vagrant plugins to make our work a bit easier. However,
               before we do that, we need to install a few more libraries to allow for the compilation
               of native ruby gems.""")
        self.print_and_exec_cmd("yum install -y @development-tools ruby-devel ruby-libvirt rubygem-ruby-libvirt libvirt-devel rubygem-unf_ext")

        self.print_comment(
            """First we install the vagrant-atomic plugin which sets up atomic as a special guest type in vagrant
               because of the uniqueness of its use.""")
        self.print_and_exec_cmd("vagrant plugin install vagrant-atomic")

        self.print_comment(
            """Next, we install the vagrant-registration plugin which automatically subscribes and unsubscribes a Red
               Hat VM with subscription-manager.""")
        self.print_and_exec_cmd("vagrant plugin install vagrant-registration --plugin-version 0.0.11")
          
        self.print_comment(
            """Now we can add the VM(s) we want to use to vagrant. We can get the VMs from the Red Hat
               Portal at http://access.redhat.com with an appropriate subscription. We will skip the download and
               assume the two 'box' files are in our work directory.""")
        self.print_and_exec_cmd("vagrant box add --name 'rhel-atomic-7' rhel-atomic-libvirt-7.1-1.x86_64.box")
        self.print_and_exec_cmd("vagrant box add --name 'rhel-server-7' rhel-server-libvirt-7.1-1.x86_64.box")

        self.print_comment("Now let's take a look at the vagrant files included with the CDK")
        self.print_and_exec_cmd("tree")

        self.print_comment("Let's create a working directory and make a docker server.")
        self.print_and_exec_cmd("mkdir docker-dev")
        self.print_and_exec_cmd("cp -rvf cdk/components/rhel-with-docker/* docker-dev/")
        self.print_and_exec_cmd("tree docker-dev")

        self.print_comment("Now our credentials are already set in environment variables like this:")
        self.print_comment("export SUB_USERNAME='username'")
        self.print_comment("export SUB_PASSWORD='password'")
        self.print_comment("The Vagrantfile picks up those creds.")
        self.print_and_exec_cmd("cat docker-dev/docker-host/Vagrantfile")

if __name__ == '__main__':
    demo = CDKDemo()
    demo.test_demo()
