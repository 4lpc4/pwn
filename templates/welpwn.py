# paste these codes into your exp.py
# https://github.com/matrix1001/welpwn # reserve this link :)
import sys
sys.path.insert(0,'/Users/wanghao/4lpc4')
from PwnContext.core import *

try:
    from IPython import embed as ipy
except ImportError:
    print ('IPython not installed.')

if __name__ == '__main__':        
    # context.terminal = ['tmux', 'splitw', '-h'] # uncomment this if you use tmux
    context.log_level = 'debug'
    context.arch='amd64'
    # functions for quick script
    s       = lambda data               :ctx.send(str(data))        #in case that data is an int
    sa      = lambda delim,data         :ctx.sendafter(str(delim), str(data)) 
    st      = lambda delim,data         :ctx.sendthen(str(delim), str(data)) 
    sl      = lambda data               :ctx.sendline(str(data)) 
    sla     = lambda delim,data         :ctx.sendlineafter(str(delim), str(data)) 
    slt     = lambda delim,data         :ctx.sendlinethen(str(delim), str(data)) 
    r       = lambda numb=4096          :ctx.recv(numb)
    ru      = lambda delims, drop=True  :ctx.recvuntil(delims, drop)
    irt     = lambda                    :ctx.interactive()
    rs      = lambda *args, **kwargs    :ctx.start(*args, **kwargs)
    leak    = lambda address, count=0   :ctx.leak(address, count)
    dbg     = lambda gdbscript='', **kwargs    :ctx.debug(gdbscript=gdbscript, **kwargs)
    # misc functions
    uu32    = lambda data   :u32(data.ljust(4, ''))
    uu64    = lambda data   :u64(data.ljust(8, ''))

    ctx.binary = './pwn'
    ctx.remote_libc = './libc.so'
    ctx.remote = ('1.1.1.1', 1111)
    ctx.debug_remote_libc = False # True for debugging remote libc, false for local.

    rs()
    # rs('remote') # uncomment this for exploiting remote target

    libc = ctx.libc # ELF object of the corresponding libc.




