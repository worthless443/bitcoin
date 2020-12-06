#!/usr/bin/env python3
# Copyright (c) 2015-2019 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

'''
This checks if all command line args are documented.
Return value is 0 to indicate no error.

Author: @MarcoFalke
'''

from subprocess import check_output
import re, os

FOLDER_GREP = 'src'
FOLDER_TEST = 'src/test/'
REGEX_ARG = r'(?:ForceSet|SoftSet|Get|Is)(?:Bool)?Args?(?:Set)?\("(-[^"]+)"'
REGEX_DOC = r'AddArg\("(-[^"=]+?)(?:=|")'
CMD_ROOT_DIR = '$(git rev-parse --show-toplevel)/{}'.format(FOLDER_GREP)
CMD_GREP_ARGS = r"git grep --perl-regexp '{}' -- {} ':(exclude){}'".format(REGEX_ARG, CMD_ROOT_DIR, FOLDER_TEST)
CMD_GREP_WALLET_ARGS = r"git grep --function-context 'void WalletInit::AddWalletOptions' -- {} | grep AddArg".format(CMD_ROOT_DIR)
CMD_GREP_WALLET_HIDDEN_ARGS = r"git grep --function-context 'void DummyWalletInit::AddWalletOptions' -- {}".format(CMD_ROOT_DIR)
CMD_GREP_DOCS = r"git grep --perl-regexp '{}' {}".format(REGEX_DOC, CMD_ROOT_DIR)
# list unsupported, deprecated and duplicate args as they need no documentation
SET_DOC_OPTIONAL = set(['-h', '-help', '-dbcrashratio', '-forcecompactdb', '-zapwallettxes'])


class lints(object):
    
    def __init__(self):
        pass

    def lint_missing_argument_documentation(self):
        used = check_output(CMD_GREP_ARGS, shell=True).decode('utf8').strip()
        docd = check_output(CMD_GREP_DOCS, shell=True).decode('utf8').strip()
        regex = re.compile(REGEX_ARG)

        args_used = set(regex.findall(used))

        args_docd = set(regex.findall(docd)).union(SET_DOC_OPTIONAL)
        args_need_doc = args_used.difference(args_docd)
        args_unknown = args_docd.difference(args_used)
        self.args_need_doc, self.args_unknown = args_need_doc, args_unknown
# 
#         print("Args used        : {}".format(len(args_used)))
#         print("Args documented  : {}".format(len(args_docd)))
#         print("Args undocumented: {}".format(len(args_need_doc)))
#         print(args_need_doc)
#         print("Args unknown     : {}".format(len(args_unknown)))
#         print(args_unknown)
# 
        #assert 0 == len(args_need_doc), "Please document the following arguments: {}".format(args_need_doc)


    def lint_missing_hidden_wallet_args(self):
        wallet_args = check_output(CMD_GREP_WALLET_ARGS, shell=True).decode('utf8').strip()
        wallet_hidden_args = check_output(CMD_GREP_WALLET_HIDDEN_ARGS, shell=True).decode('utf8').strip()

        wallet_args = set(re.findall(re.compile(REGEX_DOC), wallet_args))
        wallet_hidden_args = set(re.findall(re.compile(r'    "([^"=]+)'), wallet_hidden_args))

        hidden_missing = wallet_args.difference(wallet_hidden_args)
        if hidden_missing:
            os.environ["checker"] = "0"
        else:
            os.environ["checker"] = "1"
            
            #assert 0, "Please add {} to the hidden args in DummyWalletInit::AddWalletOptions".format(hidden_missing)


class D_lints(lints):
    def __init__(self):
        super().__init__()
        self.lint_missing_argument_documentation()
        self.lint_missing_hidden_wallet_args() 
    @property   
    def echo(self):

        return self.args_need_doc


def main():
    l = D_lints()
    print(l.echo)
    if int(os.environ["checker"]):
        print(os.environ["checker"])
    

if __name__ == "__main__":
    main()
