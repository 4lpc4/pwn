from pwn import *
import sys
from pwnlib.util.proc import wait_for_debugger
context.log_level = 'debug'
context.arch='amd64'

libc = ELF('./libc.so.6')
elf = ELF('./pwn')


# shellcode = asm(shellcraft.amd64.linux.sh())
# shellcode = asm(shellcraft.i386.linux.sh())

# example

# python newpwn.py ubuntu 10001
if len(sys.argv) > 2:
    p = remote(sys.argv[1],sys.argv[2])
else:
    p = process(sys.argv[1])

