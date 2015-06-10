#!/usr/bin/env python

import sys,time,random
from blessings import Terminal
import subprocess

def hack_for_noop(str):
    return str

term = Terminal()
print_colors = { 'yellow': term.yellow,
                 'red': term.red,
                 'nc': hack_for_noop }


typing_speed = 250 #wpm
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
print_and_exec_cmd("vagrant plugin install vagrant-registration")
  


#py2output = subprocess.check_output(['python', 'py2.py', '-i', 'test.txt'])
#print('py2 said:', py2output)

# YELLOW='\033[1;33m'
# NC='\033[0m' # No Color

# NOTE_PROMPT=$USER_PROMPT
# NOTE_START=$YELLOW
# NOTE_END=$NC

# printf "I ${RED}love${NC} Stack Overflow\n"

# printf "${NOTE_START}"
# echo "$USER_PROMPT#
# echo "$USER_PROMPT#
# echo "$USER_PROMPT#
# printf "${NOTE_END}"

# #test printing to the shell

# echo "ls -l"
# ls -l
