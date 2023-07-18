# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

def setup():
    import utils.setup
    utils.setup.setup()

def reset():
    from machine import reset
    reset()

def shell():
    import shell
    shell.shell()

# when user enters REPL and executes setup()
