import os
import subprocess


def run_and_wait(view, cmd):
    term = view.settings().get('vintageex_osx_terminal')
    color_term = os.path.expandvars("$COLORTERM")
    norm_term = os.path.expandvars("$TERM")
    if color_term == "$COLORTERM": color_term = None
    if norm_term == "$TERM": norm_term = None
    
    term = term or color_term or norm_term
    if term is None: 
        raise RuntimeError("No xterm found!")

    subprocess.Popen([
            term, '-e',
            "bash -c \"%s; read -p 'Press RETURN to exit.'\"" % cmd]).wait()


def filter_region(view, text, command):
    shell = view.settings().get('vintageex_osx_shell')
    shell = shell or os.path.expandvars("$SHELL")
    p = subprocess.Popen([shell, '-c', 'echo "%s" | %s' % (text, command)],
                         stdout=subprocess.PIPE)
    return p.communicate()[0][:-1]
