#!/usr/bin/env python

import sys, os
sys.path.append("../")

from demo_runner import Demo

class CDKDemo(Demo):
    def run_demo(self):
        os.chdir("demo")

        self.print_comment("Let's take a look at the vagrant files included with the CDK")
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

        self.print_comment(
            """We are going to add an image to the 'dev' Vagrantfile. While we are at it we are going
               to map a port to access the container""")
        self.print_and_exec_cmd("sed -i -e 's|d.build_dir = \".\"|d.image = \"fedora/apache\"\\n      d.ports=[\"8080:80\"]|g' docker-dev/dev/Vagrantfile")
        self.print_and_exec_cmd("cat docker-dev/dev/Vagrantfile")

        self.print_comment("Now we can start the server up")
        self.print_and_exec_cmd("cd docker-dev/dev/")
        USER_PROMPT = "[root@example.com dev]# "
        os.chdir("docker-dev/dev/")
        self.print_and_exec_cmd("vagrant up")

        self.print_comment("Finally, we can see that apache is now running in a docker container on our rhel host")
        self.print_and_exec_cmd("export HOST_IP=$(virsh net-dhcp-leases vagrant-libvirt | grep docker | awk '{print $6}' | sed -e 's|/24||g')")
        self.print_and_exec_cmd("curl -L http://$HOST_IP:8080/")

if __name__ == '__main__':
    demo = CDKDemo()
    demo.demo()
