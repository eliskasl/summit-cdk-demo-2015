#!/usr/bin/env python

import sys,time,random, os
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
        self.max_words_per_line = 10
        self.min_words_per_line = 7

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
                    current += 1
                    line += comments[current] + " "

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

    def print_and_exec_cmd(self, cmd):
        self._print_command(cmd)
        output = subprocess.check_output(cmd, shell=True)
        self._print_output(output)

    def _start(self, prep_machine, prep_demo, delaystart):
        if prep_machine:
            print("Will run %s to prepare the machine..." % prep_machine)
            subprocess.check_output(prep_machine, shell=True)
        if prep_demo:
            print("Will run %s to prep for the demo..." % prep_demo)
            subprocess.check_output(prep_machine, shell=True)

        print("Starting demo...")
        time.sleep(delaystart)

        self.run_demo()

    def run_demo(self):
        raise NotImplementedError("Please Implement this method")

    def main(self):
        parser = ArgumentParser(description='Run a demo.', formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("--prepmachine", help="A script to run before anything else.")
        parser.add_argument("--prepdemo", help="A script to run before running the demo.")
        parser.add_argument("--delaystart", type=int, default=0, help="Number of seconds to wait after doing prep(s) and starting the dmeo, so you can find the 'record button'")

        args = parser.parse_args()
        self._start(args.prepmachine, args.prepdemo, args.delaystart)

        sys.exit(0)

