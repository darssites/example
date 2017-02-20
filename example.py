# The main module for the plugin.
# Note: In ALL plugins there must be a python file called [name-of-plugin].py in a folder called [name-of-plugin]!

def init(page, config):
	# This code runs when the generate command is called.
	print("Example plugin initialized!")

def site(page):
	# This code run whenever a new DarsSite is created.
	print("Site created.")
	# Doing something with the given site (printing the title)
	print("Site title: " + page.title)

def closesite(page):
	# This code runs just before the user stops editing the site.
	print("Site closed: " + page.title)
