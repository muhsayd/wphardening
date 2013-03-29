#!/usr/bin/env python

from optparse import OptionParser, OptionGroup
from lib.checkWordpress import checkWordpress
from lib.chmodWordPress import chmodWordPress
from lib.removeWordPress import removeWordPress
from lib.robotsWordPress import robotsWordPress
from lib.wizardWordPress import wizardWordPress
from lib.deleteVersionWordPress import deleteVersionWordPress
import os
import sys

def main():
	usage = "usage: %prog [options] arg"
	version = '\nWP Hardening v0.1 (beta)\n'
	parser = OptionParser(usage, version=version)
	parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="active verbose mode output results")
	
	group1 = OptionGroup(parser, "Target", "This option must be specified to modify the package WordPress.")
	group1.add_option("-d", "--dir", dest="path", help="**REQUIRED** - Working Directory.", metavar="DIRECTORY")
	parser.add_option_group(group1)
	
	group2 = OptionGroup(parser, "Hardening", "Different tools to hardening WordPress.")
	group2.add_option("-c", "--chmod", action="store_true", dest="chmod", help="Chmod 755 in directory and 644 in files.")
	group2.add_option("-r", "--remove", action="store_true", dest="remove", help="Remove files and directory.")
	group2.add_option("-b", "--robots", action="store_true", dest="robots", help="Create file robots.txt")
	group2.add_option("--delete-version", action="store_true", dest="delete_version", help="Deleted version WordPress.")
	parser.add_option_group(group2)
	
	group3 = OptionGroup(parser, "Miscellaneous")
	group3.add_option("--wizard", action="store_true", dest="wizard", help="Simple wizard interface for beginner users")
	parser.add_option_group(group3)

	(options, args) = parser.parse_args()

	if options.path == None:
		parser.print_help()
		sys.exit()
	
	options.path = os.path.abspath(options.path)
	if os.path.exists(options.path):
		print options.path
		wordpress = checkWordpress(options.path)
		if wordpress.isWordPress():
			print "This project is a WordPress."
			if options.delete_version <> None:
				asdf = deleteVersionWordPress(options.path)
				asdf.delete()
			if options.chmod <> None:
				asdf = chmodWordPress(options.path)
				asdf.changePermisions()
			if options.remove <> None:
				qwer = removeWordPress(options.path)
				qwer.deleteReadme()
				qwer.deleteLicense()
			if options.robots <> None:
				zxcv = robotsWordPress(options.path)
				zxcv.createRobots()
		else:
			print "This project is not a WordPress."
	else:
		print "Could not find the specified directory"

if __name__ == "__main__":
	main()
