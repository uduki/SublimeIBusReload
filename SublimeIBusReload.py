import os
import sublime
import sublime_plugin

class SublimeIbusReloadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pkgDir = sublime.packages_path()
		target = "sublimeibusplugin.py"
		cmd = "touch"
		os.system(cmd + " " + pkgDir + "/" + target)
