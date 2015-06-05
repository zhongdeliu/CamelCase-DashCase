import sublime
import sublime_plugin
import re
import string


class CamelCaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selections = self.view.sel()
        for sel in selections:
            if self.view.substr(sel).find('-') != -1:
                self.view.replace(edit, sel, dashesToCamelCase(self.view.substr(sel)))
            else:
                self.view.replace(edit, sel, camelCaseToDashes(self.view.substr(sel)))


def dashesToCamelCase(source):
    s = string.capwords(source, '-').replace('-', '')
    return s[0].lower() + s[1:]


def camelCaseToDashes(source):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', source)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s).lower()
