"""Creating new strings: replacing old domain names with new domain names in an email:"""

message = "A kong string with a silly typo."
new_message = message[0:2] + "l" + message[3:]
print(new_message)

print("\n******Practice Example******\n")

# word = 'Zoz'
# word.index("o") >>>> 1


def replace_domain(email, old_domain, new_domain):
	if "@" + old_domain in email:
		index = email.index("@" + old_domain)
		new_email = email[:index] + "@" + new_domain
		return new_email
	return email

	# [:index] === all infront upto 1<index
