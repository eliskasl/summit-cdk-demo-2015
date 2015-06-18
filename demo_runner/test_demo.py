from unittest import TestCase, main
from demo_runner import Demo
import os

__author__ = 'lwhite'


class StubTestDemo(Demo):
    def run_demo(self):
        print("ran demo")

class TestDemo(TestCase):
    def test_print_comment(self):
        demo = StubTestDemo()
        demo.typing_speed = 250
        str = """first we install Vagrant from the regular Fedora repositories.
                 Vagrant is available in the main Fedora repos since Fedora 21.
                 Vagrant is also available at vagrantup.com for other platforms.
              """
        demo.print_comment(str)

        str = "A single short comment"
        demo.print_comment(str)

    def test_can_we_use_an_editor(self):
        demo = StubTestDemo()
        demo.typing_speed = 250
        str = """can we open vi and use it?
              """
        demo.print_comment(str)
        demo.print_and_exec_cmd("echo -e \"here is some text \\nthat we can move around in\" > test.file")
        demo.print_and_exec_cmd("vi test.file")
        demo._print_output("jisome new text")

        os.remove("./test.file")

    def test__start(self):
        demo = StubTestDemo()
        demo._start("./test_prep_machine.sh", "./test_prep_demo.sh", 0)
        demo._start(None, "./test_prep_demo.sh", 0)
        demo._start("./test_prep_machine.sh", 0)
        demo._start(None, None, 0)

