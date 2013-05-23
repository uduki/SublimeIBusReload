import os
import sublime
import sublime_plugin

class IbusReloadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pkgDir = sublime.packages_path()
		target = "SublimeIBus/sublimeibusplugin.py"
		cmd = "touch"
		os.system(cmd + " " + pkgDir + "/" + target)
