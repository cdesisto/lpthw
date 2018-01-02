# let's start tellin this fable
print("Mary had a little lamb.")
# here we are showing off how to do a fancy way of using f-strings...but really we could just use a normal string
print("It's fleece was white as {}.".format('snow'))
# oops, in the original script I had a capital W on went, that's bad, I fixed it here.
print("And everywhere that Mary went.")
# well it's a really long eplipsis we are making here, but pretty cooooooooool way to do it
print("." * 10) # what'd that do?

# now I want to spell out a fatty food with one letter at a time by setting each letter as a variable!
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
# gettin crazy here, camel case!
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try remoiving it to see what happens
# when I take the comma out I get a syntax error, there's nothing to say after end6 - duh!
# to check myself I put a '+' instead of the comma and it threw a syntax error
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
