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
        self.print_comment(
            """
            As a result, during this demo, I am going to show you some features of the upcoming CDK which are available
            upstream in projectatomic.io. Specifically, the "Nulecule Specification" and AtomicApp which can "run"
            applications that meet the spec. Yeah, yeah, lot's of things do this, but, what makes this different? Well,
            it will actually describe & run applications that are made up of multiple third-party applications. You can
            distribute your application through docker. And, finally, you can distribute your "component" so that other
            developers can consume them, through the specification, via docker.
        """)
        self.print_comment(
            """
            Let's get started...
        """)
        self.print_comment(
            """
            So, I am actually cheating a bit, and using Google's example Kubernetes app, GuestBook, but you will
            get the idea.
        """)

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
        self.print_and_exec_cmd("vagrant ssh")

        self.print_comment(
            """
            First and foremost, we need a tool which will generate a template for me to fill in. I don't know about you
            but remembering every single tool's syntax and vagaries is a bit much, especially when I use it only every
            few months. I like using DevAssistant (http://devassistant.org). Conveniently, there is a docker image for
            it.
        """)
        self.print_and_exec_cmd("docker pull langdon/da-container")

        self.print_comment(
            """
            Now we can use da to create us an empty template. We actually use this container as an executable so we
            don't have to install it locally and we don't have to muck about, too much, with mapping folders and
            the like
            """
        )
        self.print_and_exec_cmd("alias dev-assist='docker run -it --rm --privileged --name dev-assist -v `pwd`:/project langdon/devassistant'")
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
    demo.test_demo()
