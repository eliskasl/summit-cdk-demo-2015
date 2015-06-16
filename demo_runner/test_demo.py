from unittest import TestCase, main
from demo_runner import Demo

__author__ = 'lwhite'

class TestDemo(TestCase):
    def test_print_comment(self):
        demo = Demo()
        demo.typing_speed = 250
        str = """first we install Vagrant from the regular Fedora repositories.
                 Vagrant is available in the main Fedora repos since Fedora 21.
                 Vagrant is also available at vagrantup.com for other platforms.
              """
        demo.print_comment(str)

if __name__ == '__main__':
    main()