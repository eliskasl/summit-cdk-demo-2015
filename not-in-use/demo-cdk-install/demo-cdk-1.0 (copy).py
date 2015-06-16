#!/usr/bin/env python

import sys,time,random, os
from blessings import Terminal
import subprocess

def hack_for_noop(str):
    return str

term = Terminal()
print_colors = { 'yellow': term.yellow,
                 'red': term.red,
                 'nc': hack_for_noop }


typing_speed = 70 #wpm
def slow_type(t, color):
    for l in t:
        sys.stdout.write(print_colors[color](l))
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def normal_print(t, color):
    sys.stdout.write(print_colors[color](t))
    sys.stdout.flush()

    
USER_PROMPT = "[root@example.com cdk-demo]# "
NOTE_COLOR = 'yellow'

def print_comment(str):
    normal_print(USER_PROMPT, 'nc')
    comments = str.split(" ")
    
    str = "# " + str
    slow_type(str, NOTE_COLOR)
    print ''

def print_command(str):
    normal_print(USER_PROMPT, 'nc')
    slow_type(str, 'nc')
    print ''

def print_output(str):
    normal_print(str, 'nc')
    print ''

def print_and_exec_cmd(cmd):
    print_command(cmd)
    output = subprocess.check_output(cmd, shell=True)
    print_output(output)

#prep vm
#subprocess.check_output("yum install -y tree", shell=True)
#subprocess.check_output("vagrant box remove rhel-server-7", shell=True)
#subprocess.check_output("vagrant box remove rhel-atomic-7", shell=True)
#subprocess.check_output("rm -rf ~/docker-dev", shell=True)

subprocess.check_output("clear", shell=True)
#start demo
print_comment("first we install Vagrant from the regular Fedora repositories.")
print_comment("Vagrant is available in the main Fedora repos since Fedora 21.")
print_comment("Vagrant is also available at vagrantup.com for other platforms.")
print_and_exec_cmd("yum install -y vagrant vagrant-doc vagrant-libvirt vagrant-libvirt-doc")

print_comment("Now we want to make it so that we can operate libvirt as a normal user.")
print_comment("This is a requirement of vagrant.")
print_and_exec_cmd("cp -vf /usr/share/vagrant/gems/doc/vagrant-libvirt-0.0.24/polkit/10-vagrant-libvirt.rules /etc/polkit-1/rules.d/")

print_comment("Now we want to install a few useful vagrant plugins to make our work a bit easier.")
print_comment("However, before we do that, we need to install a few more libraries to allow")
print_comment("for the compilation of native ruby gems.")
print_and_exec_cmd("yum install -y @development-tools ruby-devel ruby-libvirt rubygem-ruby-libvirt libvirt-devel rubygem-unf_ext")

print_comment("First we install the vagrant-atomic plugin which sets up atomic as a special guest ")
print_comment("type in vagrant because of the uniqueness of its use.")
print_and_exec_cmd("vagrant plugin install vagrant-atomic")

print_comment("Next, we install the vagrant-registration plugin which automatically subscribes and ")
print_comment("unsubscribes a Red Hat VM with subscription-manager.")
print_and_exec_cmd("vagrant plugin install vagrant-registration --plugin-version 0.0.11")
  
print_comment("Now we can add the VM(s) we want to use to vagrant. We can get the VMs from the Red ")
print_comment("Hat Portal at http://access.redhat.com with an appropriate subscription.") 
print_comment("We will skip the download and assume the two 'box' files are in our work directory.")
print_and_exec_cmd("vagrant box add --name 'rhel-atomic-7' rhel-atomic-libvirt-7.1-1.x86_64.box")
print_and_exec_cmd("vagrant box add --name 'rhel-server-7' rhel-server-libvirt-7.1-1.x86_64.box")

print_comment("Now let's take a look at the vagrant files included with the CDK")
print_and_exec_cmd("tree")

print_comment("Let's create a working directory and make a docker server.")
print_and_exec_cmd("mkdir docker-dev")
print_and_exec_cmd("cp -rvf cdk/components/rhel-with-docker/* docker-dev/")
print_and_exec_cmd("tree docker-dev")

print_comment("Now our credentials our already set in environment variables like this:")
print_comment("export SUB_USERNAME='username'")
print_comment("export SUB_PASSWORD='password'")
print_comment("The Vagrantfile picks up those creds.")
print_and_exec_cmd("cat docker-dev/docker-host/Vagrantfile")

print_comment("We are going to add an image to the 'dev' Vagrantfile")
print_comment("While we are at it we are going to map a port to access the container")
print_and_exec_cmd("sed -i -e 's|d.build_dir = \".\"|d.image = \"fedora/apache\"\\n      d.ports=[\"8080:80\"]|g' docker-dev/dev/Vagrantfile")
print_and_exec_cmd("cat docker-dev/dev/Vagrantfile")

print_comment("Now we can start the server up")
print_and_exec_cmd("cd docker-dev/dev/")
USER_PROMPT = "[root@example.com dev]# "
os.chdir("/root/docker-dev/dev/")
print_and_exec_cmd("vagrant up")

print_comment("Finally, we can see that apache is now running in a docker container on our rhel host")
print_and_exec_cmd("export HOST_IP=$(virsh net-dhcp-leases vagrant-libvirt | grep docker | awk '{print $6}' | sed -e 's|/24||g')")
print_and_exec_cmd("curl -L http://$HOST_IP:8080/")
