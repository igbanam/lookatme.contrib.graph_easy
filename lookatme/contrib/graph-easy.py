"""
Introduce ASCII graphs with the Dot notation
"""


import urwid
import subprocess
import tempfile


from lookatme.exceptions import IgnoredByContrib

def graph_easy_exists():
    result = subprocess.getstatusoutput(['which graph-easy'])
    return result[0] == 0

def user_warnings():
    """Needed for lookatme.

    This extension assumes you have the Graph::Easy Perl module installed. For
    details on how to install this, please visit the Graph::Easy website at
    https://metacpan.org/dist/Graph-Easy/view/INSTALL
    """

    warnings = []
    result = subprocess.getstatusoutput(['graph-easy'])
    if not graph_easy_exists():
        warnings.append("'graph-easy' is not installed.")
    return warnings

def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    parts = lang.split('-')

    if parts[0] != "graph_easy":
        raise IgnoredByContrib()

    if len(parts) == 1:
        render_format = "ascii"
    else:
        if parts[1] not in ['ascii', 'boxart']:
            raise IgnoredByContrib()
        else:
            render_format = parts[1]

    output = ''
    file_descriptor, file_name = tempfile.mkstemp()
    with open(file_descriptor, 'w') as fd:
        fd.write(token['text'])

    if graph_easy_exists():
        result = subprocess.run([
            'graph-easy',
            '--input={}'.format(file_name),
            '--as={}'.format(render_format)
        ], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
    else:
        output = token['text']

    return urwid.Text(output)
