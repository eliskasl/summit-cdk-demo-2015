#!/usr/bin/env python

import sys, time, random, os
from blessings import Terminal
import subprocess
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import random

def _hack_for_noop(str):
    return str

class Demo:
    def __init__(self):
        self._term = Terminal()
        self._print_colors = { 'yellow': self._term.yellow,
                     'red': self._term.red,
                     'nc': _hack_for_noop }
        self.typing_speed = 70 #wpm
        self.user_prompt = "[root@example.com cdk-demo]# "
        self.comment_color = 'yellow'
        self.max_words_per_line = 14
        self.min_words_per_line = 10
        self.test_mode = False
        self.reading_speed = 5 #lines per second
        self.line_length = 150 #length of one line

    def _slow_type(self, t, color):
        for l in t:
            sys.stdout.write(self._print_colors[color](l))
            sys.stdout.flush()
            time.sleep(random.random()*10.0/self.typing_speed)

    def _normal_print(self, t, color):
        sys.stdout.write(self._print_colors[color](t))
        sys.stdout.flush()

    def print_comment(self, str):
        comments = str.split()
        all_word_count = len(comments)
        current = 0
        while current < all_word_count - 1:
            line = ""
            words_in_line = random.randrange(self.min_words_per_line, self.max_words_per_line)
            if (current + words_in_line) >= all_word_count:
                line = " ".join(comments[current:all_word_count])
                current = all_word_count
            else:
                for counter in range(0, words_in_line):
                    line += comments[current] + " "
                    current += 1

            self._normal_print(self.user_prompt, 'nc')
            self._slow_type(line, self.comment_color)
            print ''

    def _print_command(self, str):
        self._normal_print(self.user_prompt, 'nc')
        self._slow_type(str, 'nc')
        print ''

    def _print_output(self, str):
        self._normal_print(str, 'nc')
        print ''

    def _calc_reading_delay(self, num_chars):
        reading_delay = int((num_chars / self.line_length) / self.reading_speed)
        return reading_delay

    def pause_demo(self, delay=5):
        """pauses the demo so that you have a marker to launch something else and cut it in
        :param delay: in seconds
        """
        time.sleep(delay)

    def print_cmd(self, cmd):
        self._print_command(cmd)

    def _print_cmd_output(self, output, fake_size=0):
        """
        prints the output of a command, does some chunking and a reading delay
        :param output: the command output to print
        :param fake_size: for testing, use this fake size for calc'ing reading delay
        """
        #delay a bit for the reader
        if fake_size == 0:
            reading_delay = self._calc_reading_delay(len(output))
        else:
            reading_delay = self._calc_reading_delay(fake_size)

        #this would be cool but it is going to have problems printing special chars
        #output_chunks = [output[i:i+reading_delay] for i in range(0, len(output), reading_delay)]
        #for chunk in output_chunks:
        #    self._print_output(chunk)
        #    time.sleep(1)

        self._print_output(output)
        time.sleep(reading_delay)

    def print_and_fake_exec_cmd(self, cmd, output):
        """ For those long running commands, capture the output, haven't quite figured out how this works if you need
        the executed result.
        :param cmd: the command you wish to print
        :param output: the output that should be shown as if the command was executed
        """
        self._print_command(cmd)
        self._print_cmd_output(output)

    def print_and_exec_cmd(self, cmd):
        self._print_command(cmd)
        if not self.test_mode:
            output = subprocess.check_output(cmd, shell=True)
            self._print_cmd_output(output)
        else:
            output = "fake output, we didn't really run it"
            random_output_size = random.randrange(150, 5000)
            reading_delay = self._calc_reading_delay(random_output_size)
            print("random_output_size= ", random_output_size, "reading_delay=", reading_delay)
            #don't really sleep in test
            self._print_cmd_output(output, reading_delay)


    #this needs a bunch more work if we support non-root users
#    def print_and_exec_cmd_root(self, cmd):
#        cmd = "sudo " + cmd
#        self.print_and_exec_cmd(cmd)

    def _start(self, prep_machine, prep_demo, delaystart):
        if prep_machine:
            print("Will run %s to prepare the machine..." % prep_machine)
            out = subprocess.check_output(prep_machine, shell=True)
            print("prep_machine_output")
            self._print_output(out)
        if prep_demo:
            print("Will run %s to prep for the demo..." % prep_demo)
            out = subprocess.check_output(prep_demo, shell=True)
            print("prep_demo_output")
            self._print_output(out)

        print("Starting demo...")
        time.sleep(delaystart)
        self.run_demo()

    def run_demo(self):
        raise NotImplementedError("Please Implement this method")

    def demo(self):
        parser = ArgumentParser(description='Run a demo.', formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("--prepmachine", help="A script to run before anything else.")
        parser.add_argument("--prepdemo", help="A script to run before running the demo.")
        parser.add_argument("--delaystart", type=int, default=0, help="Number of seconds to wait after doing prep(s) and starting the dmeo, so you can find the 'record button'")

        args = parser.parse_args()
        self._start(args.prepmachine, args.prepdemo, args.delaystart)

        sys.exit(0)

    def test_demo(self):
        self.typing_speed = 250
        self.test_mode = True
        self.demo()

