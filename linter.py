import os
from cuda_lint import Linter

_phpmd = os.path.join(os.path.dirname(__file__), 'phpmd.phar')
_rules = 'cleancode,codesize,controversial,design,naming,unusedcode' 


class Phpmd(Linter):
    syntax = ('PHP', 'PHP_')
    cmd = ('php', _phpmd, '@', 'text', _rules)
    regex = (
        r'(?P<filename>.+):(?P<line>\d+)'
        r'\s*(?P<message>.+)$'
    )
    default_type = 'warning'
    comment_re = r'\s*<!--'
    tempfile_suffix = 'php'
