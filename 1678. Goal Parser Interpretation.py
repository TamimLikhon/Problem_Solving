command = "G()(al)"
brac = "()"
alp = "o"
com_pars = command.replace(brac, alp)
com_pars = com_pars.replace("(", "").replace(")", "")

print(com_pars)


#com_pars = command.replace("()", "o").replace("(al)", "al")
