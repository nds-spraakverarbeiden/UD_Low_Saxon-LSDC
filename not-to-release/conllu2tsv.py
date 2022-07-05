import sys,os,re

""" convert CoNLL-U file to a TSV file
	
	This is for doing annotation with spreadsheet software. With the preceding corpus added on top of the document, you can use autocompletion.
	Features and MISC are split along |, and only *known* attributes are processed, so make sure to add the list below if you introduce a new one.

	We spell out an additional header line. Use the line+row freeze feature to keep it visible during annotation.

	The TSV format is temporary only, and should be coded back into CoNLL-U after being finished

	synopsis: conll2tsv [-revert] FILE[1..n]
		-revert transform TSV to CoNLL-U; default: CoNLL-U to TSV
		FILE    file(s) to be converted, in default mode CoNLL-U, in revert mode TSV

	Output is written to stdout, capture with redirect into file:

		python3 my-conll-file.conll > my-tsv-file.tsv

"""

keys="""
	Foreign
	AdpType
	Definite
	Degree
	NumType

	Case
	Gender
	Number

	VerbForm
	PartType
	VerbType
	Person
	Mood
	Tense
	Aspect

	Polite
	Poss
	PronType
	Reflex

	Gender[psor]
	Number[psor]
	Person[psor]
"""
keys=[k for k in keys.split() if len(k)>0 ]

mkeys=["lemma[gml]","Case[regional]","Mood[regional]","Loan","SpaceAfter"]

# revert mode: TSV to CoNLL-U
# ideally, you should apply this only to portions you just created, so that they don't get conflated with the remaining corpus
if sys.argv[1]=="-revert":
	for file in sys.argv[2:]:
		with open(file,"rt",errors="ignore") as input:
			for line in input:
				line=line.strip()
				if line.startswith("#") or len(line)==0:
					print(line)
				else:
					# I'm doing annotation with Spreadsheet software, this skrews up data import
					line=re.sub("&quot;",'"', line)
					line=re.sub("&apos;","'",line)
					
					# split feature lists, so I can use autocompletion
					fields=line.split("\t")
					# print(fields)

					misc=dict(zip(mkeys,fields[7:7+len(mkeys)]))
					misc=[ k+"="+misc[k] for k in mkeys if k in misc and misc[k].strip()!="" ]
					misc="|".join(misc)
					if misc=="": misc="_"

					feats=dict(zip(keys,fields[7+len(mkeys):]))
					feats={ k:feats[k] if k in feats and feats[k].strip()!="" else "_" for k in keys }
					feats = [ k+"="+feats[k] for k in keys if k in feats and feats[k].strip()!="" and feats[k].strip()!="_"]
					feats="|".join(feats)
					if feats=="": feats="_"

					# print()
					# print(line)
					# print(fields[0:4])
					# print(mkeys,fields[7:7+len(mkeys)])
					# print(feats)
					# print(fields[4:7])
					# print(misc)
					print("\t".join(fields[0:4]+[feats]+fields[4:7]+[misc]))
	sys.exit()


# CoNLL-U to TSV
print("#"+"\t".join("ID FORM UPOS XPOS HEAD EDGE DEPS".split()+mkeys+keys))
print()
for file in sys.argv[1:]:
	with open(file,"rt",errors="ignore") as input:
		for line in input:
			line=line.strip()
			if line.startswith("#") or len(line)==0:
				print(line)
			else:
				# I'm doing annotation with Spreadsheet software, this skrews up data import
				line=re.sub('"',"&quot;",line)
				line=re.sub("'","&apos;",line)
				
				# split feature lists, so I can use autocompletion
				id,word,lemma,upos,xpos,feats,head,edge,deps,misc=line.split("\t")
				feats={ f.split("=")[0]:f.split("=")[1] for f in feats.split("|") if "=" in f }
				feats = [ feats[k] if k in feats else "" for k in keys ]
				misc={ m.split("=")[0]:m.split("=")[1] for m in misc.split("|") if "=" in m }
				misc=[ misc[k] if k in misc else "" for k in mkeys ]
				
				print("\t".join([id,lemma,upos,xpos,head,edge,deps]+misc+feats))
