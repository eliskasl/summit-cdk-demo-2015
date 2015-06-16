#!/usr/bin/env python

#import sys,time,random, os
#from blessings import Terminal
#import subprocess

from demo_runner import Demo

class CDKDemo(Demo):
    def run_demo(self):
        self.print_comment("first we install Vagrant from the regular Fedora repositories.")
        self.print_comment("Vagrant is available in the main Fedora repos since Fedora 21.")
        self.print_comment("Vagrant is also available at vagrantup.com for other platforms.")
        self.print_and_exec_cmd("yum install -y vagrant vagrant-doc vagrant-libvirt vagrant-libvirt-doc")


    def blah(self):
        #start demo
        self.print_comment("first we install Vagrant from the regular Fedora repositories.")
        self.print_comment("Vagrant is available in the main Fedora repos since Fedora 21.")
        self.print_comment("Vagrant is also available at vagrantup.com for other platforms.")
        self.print_and_exec_cmd("yum install -y vagrant vagrant-doc vagrant-libvirt vagrant-libvirt-doc")

        self.print_comment("Now we want to make it so that we can operate libvirt as a normal user.")
        self.print_comment("This is a requirement of vagrant.")
        self.print_and_exec_cmd("cp -vf /usr/share/vagrant/gems/doc/vagrant-libvirt-0.0.24/polkit/10-vagrant-libvirt.rules /etc/polkit-1/rules.d/")

        self.print_comment("Now we want to install a few useful vagrant plugins to make our work a bit easier.")
        self.print_comment("However, before we do that, we need to install a few more libraries to allow")
        self.print_comment("for the compilation of native ruby gems.")
        self.print_and_exec_cmd("yum install -y @development-tools ruby-devel ruby-libvirt rubygem-ruby-libvirt libvirt-devel rubygem-unf_ext")

        self.print_comment("First we install the vagrant-atomic plugin which sets up atomic as a special guest ")
        self.print_comment("type in vagrant because of the uniqueness of its use.")
        self.print_and_exec_cmd("vagrant plugin install vagrant-atomic")

        self.print_comment("Next, we install the vagrant-registration plugin which automatically subscribes and ")
        self.print_comment("unsubscribes a Red Hat VM with subscription-manager.")
        self.print_and_exec_cmd("vagrant plugin install vagrant-registration --plugin-version 0.0.11")
          
        self.print_comment("Now we can add the VM(s) we want to use to vagrant. We can get the VMs from the Red ")
        self.print_comment("Hat Portal at http://access.redhat.com with an appropriate subscription.") 
        self.print_comment("We will skip the download and assume the two 'box' files are in our work directory.")
        self.print_and_exec_cmd("vagrant box add --name 'rhel-atomic-7' rhel-atomic-libvirt-7.1-1.x86_64.box")
        self.print_and_exec_cmd("vagrant box add --name 'rhel-server-7' rhel-server-libvirt-7.1-1.x86_64.box")

        self.print_comment("Now let's take a look at the vagrant files included with the CDK")
        self.print_and_exec_cmd("tree")

        self.print_comment("Let's create a working directory and make a docker server.")
        self.print_and_exec_cmd("mkdir docker-dev")
        self.print_and_exec_cmd("cp -rvf cdk/components/rhel-with-docker/* docker-dev/")
        self.print_and_exec_cmd("tree docker-dev")

        self.print_comment("Now our credentials our already set in environment variables like this:")
        self.print_comment("export SUB_USERNAME='username'")
        self.print_comment("export SUB_PASSWORD='password'")
        self.print_comment("The Vagrantfile picks up those creds.")
        self.print_and_exec_cmd("cat docker-dev/docker-host/Vagrantfile")

        self.print_comment("We are going to add an image to the 'dev' Vagrantfile")
        self.print_comment("While we are at it we are going to map a port to access the container")
        self.print_and_exec_cmd("sed -i -e 's|d.build_dir = \".\"|d.image = \"fedora/apache\"\\n      d.ports=[\"8080:80\"]|g' docker-dev/dev/Vagrantfile")
        self.print_and_exec_cmd("cat docker-dev/dev/Vagrantfile")

        self.print_comment("Now we can start the server up")
        self.print_and_exec_cmd("cd docker-dev/dev/")
        USER_PROMPT = "[root@example.com dev]# "
        os.chdir("/root/docker-dev/dev/")
        self.print_and_exec_cmd("vagrant up")

        self.print_comment("Finally, we can see that apache is now running in a docker container on our rhel host")
        self.print_and_exec_cmd("export HOST_IP=$(virsh net-dhcp-leases vagrant-libvirt | grep docker | awk '{print $6}' | sed -e 's|/24||g')")
        self.print_and_exec_cmd("curl -L http://$HOST_IP:8080/")

if __name__ == '__main__':
    demo = CDKDemo()
    print(dir(demo))
    demo.main()
