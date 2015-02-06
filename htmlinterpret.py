import graphics
def interpret (trees):
	for tree in trees:
		nodetype = tree[0]
		if (nodetype == "word-element"):
			graphics.word(tree[1])
		elif (nodetype=="tag-element"):
			tagname = tree[1]
			tagargs = tree[2]
			subtrees = tree[3]
			closetagname = tree[4]
			if (tagname <> closetagname):
				graphics.warning("unbalanced tags")
			else:
				graphics.begintag(tagname,tagargs)
				interpret(subtrees)
				graphics.endtag()