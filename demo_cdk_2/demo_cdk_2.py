__author__ = 'lwhite'
#!/usr/bin/env python

import sys, os
sys.path.append("../")

from demo_runner import Demo

class CDK2Demo(Demo):
    def run_demo(self):
        # script
        # Explain the objective
        # start with da


        self.print_comment(
            """
            I am currently working on an application. I have a number of classic problems. First, I need to orchestrate
            my components without having to go to a whole lot of work to set them up and manage them. I also want to
            pass those components off to other developers, either because I work in a team or because I want open
            source contributors.
        """)
        self.print_blank_lines(3)

        self.print_comment(
            """
            As a result, during this demo, I am going to show you some features of the upcoming CDK which are available
            upstream in projectatomic.io. Specifically, the "Nulecule Specification" and AtomicApp which can "run"
            applications that meet the spec. Yeah, yeah, lot's of things do this, but, what makes this different? Well,
            it will actually describe & run applications that are made up of multiple third-party applications. You can
            distribute your application through docker. And, finally, you can distribute your "component" so that other
            developers can consume them, through the specification, via docker.
        """)
        self.print_blank_lines(1)

        self.print_comment(
            """
            Let's get started...
        """)
        self.print_blank_lines(2)

        self.print_comment(
            """
            So, I am actually cheating a bit, and using Google's example Kubernetes app, GuestBook, but you will
            get the idea.
        """)
        self.print_blank_lines(3)

        self.print_comment(
            """
            Ok, let's use vagrant to get started. Conveniently, there is a vagrant box which has a lot of the tools
            we need installed already.
        """)
        output = """A `Vagrantfile` has been placed in this directory. You are now
            ready to `vagrant up` your first virtual environment! Please read
            the comments in the Vagrantfile as well as documentation on
            `vagrantup.com` for more information on using Vagrant.
        """
        self.print_and_fake_exec_cmd("vagrant init -m atomicapp/dev", output)

        self.print_comment(
            """
            Now, let's bring that box up and then ssh in to it.
        """)
        output = "vagrant up output...."
        self.print_and_fake_exec_cmd("vagrant up", output)
        output = """
        Last login: Thu Jun 18 12:26:29 2015 from 192.168.121.1
        """
        self.print_and_fake_exec_cmd("vagrant ssh", output)
        self.user_prompt = "[vagrant@cdk2-demo ~]# "

        self.print_comment(
            """
            First and foremost, we need a tool which will generate a template for me to fill in. I don't know about you
            but remembering every single tool's syntax and vagaries is a bit much, especially when I use it only every
            few months. I like using DevAssistant (http://devassistant.org). Conveniently, there is a docker image for
            it.
        """)
        self.print_and_exec_cmd("docker pull devassistant/nulecule")

        self.print_comment(
            """
            Now we can use da to create us an empty template. We actually use this container as an executable so we
            don't have to install it locally and we don't have to muck about, too much, with mapping folders and
            the like
            """
        )
        self.print_and_exec_cmd("alias dev-assist='docker run -it --rm --privileged --name dev-assist -v `pwd`:/project devassistant/nulecule'")
        self.print_and_exec_cmd("dev-assist create nulecule -n guestapp -a langdon -e langdon@redhat.com -v 0.0.1")

        self.print_comment(
            """
            OK, let's take a look at what it made.
            """
        )
        self.print_and_exec_cmd("tree guestapp")
        self.print_and_exec_cmd("cd guestapp")
        os.chdir("guestapp")


if __name__ == '__main__':
    demo = CDK2Demo()
    #demo.typing_speed = 250
    demo.demo()

vagrant_up_output="""
Bringing machine 'nulecule_demo' up with 'libvirt' provider...
==> nulecule_demo: Creating image (snapshot of base box volume).
==> nulecule_demo: Creating domain with the following settings...
==> nulecule_demo:  -- Name:              demo_cdk_2_nulecule_demo
==> nulecule_demo:  -- Domain type:       kvm
==> nulecule_demo:  -- Cpus:              1
==> nulecule_demo:  -- Memory:            512M
==> nulecule_demo:  -- Base box:          atomicapp/dev
==> nulecule_demo:  -- Storage pool:      mnt_vms
==> nulecule_demo:  -- Image:             /mnt/vms/demo_cdk_2_nulecule_demo.img
==> nulecule_demo:  -- Volume Cache:      default
==> nulecule_demo:  -- Kernel:            
==> nulecule_demo:  -- Initrd:            
==> nulecule_demo:  -- Graphics Type:     vnc
==> nulecule_demo:  -- Graphics Port:     5900
==> nulecule_demo:  -- Graphics IP:       127.0.0.1
==> nulecule_demo:  -- Graphics Password: Not defined
==> nulecule_demo:  -- Video Type:        cirrus
==> nulecule_demo:  -- Video VRAM:        9216
==> nulecule_demo:  -- Command line : 
==> nulecule_demo: Starting domain.
==> nulecule_demo: Waiting for domain to get an IP address...
==> nulecule_demo: Waiting for SSH to become available...
    nulecule_demo: 
    nulecule_demo: Vagrant insecure key detected. Vagrant will automatically replace
    nulecule_demo: this with a newly generated keypair for better security.
    nulecule_demo: 
    nulecule_demo: Inserting generated public key within guest...
    nulecule_demo: Removing insecure key from the guest if its present...
    nulecule_demo: Key inserted! Disconnecting and reconnecting using new SSH key...
==> nulecule_demo: Starting domain.
==> nulecule_demo: Waiting for domain to get an IP address...
==> nulecule_demo: Waiting for SSH to become available...
==> nulecule_demo: Creating shared folders metadata...
==> nulecule_demo: Setting hostname...
==> nulecule_demo: Rsyncing folder: /mnt/nbu/loc-projects/summit-2015/summit-cdk-demo-2015/demo_cdk_2/ => /home/vagrant/sync
==> nulecule_demo:   - Exclude: [".vagrant/", ".git/", ".#*", "*~"]
==> nulecule_demo: Rsyncing folder: /mnt/nbu/loc-projects/summit-2015/summit-cdk-demo-2015/ => /home/vagrant/demo
==> nulecule_demo:   - Exclude: [".vagrant/", ".git/", ".#*", "*~", "*qcow*"]
==> nulecule_demo: Mounting NFS shared folders...
==> nulecule_demo: Configuring and enabling network interfaces...
==> nulecule_demo: Running provisioner: shell...
    nulecule_demo: Running: inline script
==> nulecule_demo: Running provisioner: shell...
    nulecule_demo: Running: inline script
==> nulecule_demo: Loaded plugins: fastestmirror
==> nulecule_demo: Determining fastest mirrors
==> nulecule_demo:  * base: mirror.ash.fastserv.com
==> nulecule_demo:  * extras: mirror.linux.duke.edu
==> nulecule_demo:  * updates: mirror.cogentco.com
==> nulecule_demo: Resolving Dependencies
==> nulecule_demo: --> Running transaction check
==> nulecule_demo: ---> Package python-pip.noarch 0:1.5.6-5.el7 will be installed
==> nulecule_demo: ---> Package system-storage-manager.noarch 0:0.4-5.el7 will be installed
==> nulecule_demo: --> Finished Dependency Resolution
==> nulecule_demo: 
==> nulecule_demo: Dependencies Resolved
==> nulecule_demo: 
==> nulecule_demo: ================================================================================
==> nulecule_demo:  Package                      Arch         Version             Repository  Size
==> nulecule_demo: ================================================================================
==> nulecule_demo: Installing:
==> nulecule_demo:  python-pip                   noarch       1.5.6-5.el7         epel       1.3 M
==> nulecule_demo:  system-storage-manager       noarch       0.4-5.el7           base       106 k
==> nulecule_demo: 
==> nulecule_demo: Transaction Summary
==> nulecule_demo: ================================================================================
==> nulecule_demo: Install  2 Packages
==> nulecule_demo: 
==> nulecule_demo: Total download size: 1.4 M
==> nulecule_demo: Installed size: 6.3 M
==> nulecule_demo: Downloading packages:
==> nulecule_demo: Public key for system-storage-manager-0.4-5.el7.noarch.rpm is not installed
==> nulecule_demo: warning: /var/cache/yum/x86_64/7/base/packages/system-storage-manager-0.4-5.el7.noarch.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
==> nulecule_demo: --------------------------------------------------------------------------------
==> nulecule_demo: Total                                              441 kB/s | 1.4 MB  00:03     
==> nulecule_demo: Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
==> nulecule_demo: Importing GPG key 0xF4A80EB5:
==> nulecule_demo:  Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
==> nulecule_demo:  Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
==> nulecule_demo:  Package    : centos-release-7-1.1503.el7.centos.2.8.x86_64 (@anaconda)
==> nulecule_demo:  From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
==> nulecule_demo: Running transaction check
==> nulecule_demo: Running transaction test
==> nulecule_demo: Transaction test succeeded
==> nulecule_demo: Running transaction
==> nulecule_demo:   Installing : system-storage-manager-0.4-5.el7.noarch                      1/2
==> nulecule_demo:  
==> nulecule_demo:   Installing : python-pip-1.5.6-5.el7.noarch                                2/2
==> nulecule_demo:  
==> nulecule_demo:   Verifying  : python-pip-1.5.6-5.el7.noarch                                1/2
==> nulecule_demo:  
==> nulecule_demo:   Verifying  : system-storage-manager-0.4-5.el7.noarch                      2/2
==> nulecule_demo:  
==> nulecule_demo: 
==> nulecule_demo: Installed:
==> nulecule_demo:   python-pip.noarch 0:1.5.6-5.el7   system-storage-manager.noarch 0:0.4-5.el7  
==> nulecule_demo: 
==> nulecule_demo: Complete!
==> nulecule_demo: Running provisioner: shell...
    nulecule_demo: Running: inline script
==> nulecule_demo: Trying to pull repository docker.io/devassistant/nulecule ...
==> nulecule_demo: 
==> nulecule_demo: 5ab64d531ea2: Pulling image (latest) from docker.io/devassistant/nulecule
==> nulecule_demo: 5ab64d531ea2: Pulling image (latest) from docker.io/devassistant/nulecule, endpoint: https://registry-1.docker.io/v1/
==> nulecule_demo: 5ab64d531ea2: Pulling dependent layers
==> nulecule_demo: eb8e83ebb17d: Pulling metadata
==> nulecule_demo: eb8e83ebb17d: Pulling fs layer
==> nulecule_demo: eb8e83ebb17d: Download complete
==> nulecule_demo: f62b94603835: Pulling metadata
==> nulecule_demo: f62b94603835: Pulling fs layer
==> nulecule_demo: f62b94603835: Download complete
==> nulecule_demo: dfa2027ad557: Pulling metadata
==> nulecule_demo: dfa2027ad557: Pulling fs layer
==> nulecule_demo: dfa2027ad557: Download complete
==> nulecule_demo: 07de5afd3630: Pulling metadata
==> nulecule_demo: 07de5afd3630: Pulling fs layer
==> nulecule_demo: 07de5afd3630: Download complete
==> nulecule_demo: 6c75b7a64ee5: Pulling metadata
==> nulecule_demo: 6c75b7a64ee5: Pulling fs layer
==> nulecule_demo: 6c75b7a64ee5: Download complete
==> nulecule_demo: 64c3b83bf95f: Pulling metadata
==> nulecule_demo: 64c3b83bf95f: Pulling fs layer
==> nulecule_demo: 64c3b83bf95f: Download complete
==> nulecule_demo: 65f67771d011: Pulling metadata
==> nulecule_demo: 65f67771d011: Pulling fs layer
==> nulecule_demo: 65f67771d011: Download complete
==> nulecule_demo: 3bf7a72052a5: Pulling metadata
==> nulecule_demo: 3bf7a72052a5: Pulling fs layer
==> nulecule_demo: 3bf7a72052a5: Download complete
==> nulecule_demo: e1b3c476670b: Pulling metadata
==> nulecule_demo: e1b3c476670b: Pulling fs layer
==> nulecule_demo: e1b3c476670b: Download complete
==> nulecule_demo: 70dbbfa45167: Pulling metadata
==> nulecule_demo: 70dbbfa45167: Pulling fs layer
==> nulecule_demo: 70dbbfa45167: Download complete
==> nulecule_demo: f6bf40035209: Pulling metadata
==> nulecule_demo: f6bf40035209: Pulling fs layer
==> nulecule_demo: f6bf40035209: Download complete
==> nulecule_demo: 8aa58e23080f: Pulling metadata
==> nulecule_demo: 8aa58e23080f: Pulling fs layer
==> nulecule_demo: 8aa58e23080f: Download complete
==> nulecule_demo: 5ab64d531ea2: Pulling metadata
==> nulecule_demo: 5ab64d531ea2: Pulling fs layer
==> nulecule_demo: 5ab64d531ea2: Download complete
==> nulecule_demo: 5ab64d531ea2: Download complete
==> nulecule_demo: Status: Downloaded newer image for docker.io/devassistant/nulecule:latest
"""
