"""Dump the SQL data for download
"""
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option

import os
import re

SUBSTITUTION_PATTERN = re.compile("^(.+?')(.+?)(liblwgeom.+)$")

class Command(BaseCommand):
    option_list= BaseCommand.option_list + (
    make_option('-o', '--sql_output', type='string', action='store', dest='output',
        help='The output file where the SQL data will be dumped.',
        default="data/psql/dump.sql"),
    make_option('-r', '--reverse', type='string', action='store', dest='reverse',
        help='If specified, then the file at [output] will be processed to restore a prefix over $libdir (for Joes broken install) Note that a fresh database dump is NOT made.'),
    )
    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        #dump for deployment
        try:
            dumpfile = options['output']
            if options['reverse']:
                prefix = options['reverse']
                substitution(dumpfile,prefix)
                print "Rewrote %s using %s" % (dumpfile,prefix)
            else:    
                os.system('pg_dump -U %s -O -x %s > %s' % (settings.DATABASE_USER,settings.DATABASE_NAME,dumpfile))
                substitution(dumpfile,'$libdir/')
                print('sql dumped to: %s' % dumpfile)
        except KeyError:
            print "You must specify the SQL output file using -o or --sql_output."
            
def substitution(fname,prefix):
    """Find lines referring to the PostGIS extension libraries and adjust the path.  In most PostGIS installs,
       a symbolic path '$libdir' is used to identify the path to 'liblwgeom', but we have some installs that
       use a hard-coded path which doesn't always match when the SQL dump is moved to another server.
    """
    if not prefix.endswith("/"):
        prefix += "/"
    lines = []    
    for line in open(fname).readlines():
        lines.append(fix_line(line,prefix))
    out = open(fname,"w")
    for line in lines:
        out.write(line)
    out.close()    

def fix_line(line,prefix):
    """Return either the given line or a copy of the line with the given prefix in place of the original prefix."""
    parts = SUBSTITUTION_PATTERN.split(line)
    if len(parts) == 1:
        return parts[0]
    else:
        parts = parts[1:-1]    
        parts[1] = prefix
        return "".join(parts)
    
