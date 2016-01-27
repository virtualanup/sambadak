from math import log10,ceil,fmod,floor
from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.textedit = QtGui.QTextEdit(Form)
        self.textedit.setGeometry(QtCore.QRect(0, 0, 213, 220))
        self.textedit.setObjectName(_fromUtf8("textedit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
editboxtext=''

def PrintText(text):
	global editboxtext
	editboxtext+=u"\r\n"+text
	ui.textedit.setText(editboxtext)#edit this
#this tree node is used in the parser
class TreeNode:
	def __init__(self):
		self.children=[]
		self.data=0
	
	def AddChild(self,child):
		self.children.append(child)
	
	def SetData(self,data):
		self.data=data
	
	def GetData(self):
		return self.data
	
	def Print(self,width=0):
		PrintText((u"   "*width)+self.data)
		for child in self.children:
			child.Print(width+1)

class Parser:
	kakha=[u'क',u'ख',u'ग',u'घ',u'ङ',u'च',u'छ',u'ज',u'झ',u'ञ',u'ट',u'ठ',u'ड',u'ढ',u'ण',u'त',u'थ',u'द',u'ध',u'न',u'प',u'फ',u'ब',u'भ',u'म',u'य',u'र',u'ल',u'व',u'श',u'ष',u'स',u'ह',u'诶',u'比',u'西'] #letters 
	firstones=[u'अ',u'आ',u'इ',u'ई',u'उ',u'ऊ',u'ए',u'ऐ',u'ओ',u'औ',u'अ',u'अ']
	numbers=[u'०',u'१',u'२',u'३',u'४',u'५',u'६',u'७',u'८',u'९']
	alphabets=numbers+firstones+kakha
	symbols=[u'ा',u'ि',u'ी',u'ु',u'ू',u'े',u'ै',u'ो',u'ौ',u'ं']
	khuttakateko=u'्'
	allsymbols=symbols+[khuttakateko]
	punctuations=[u'.',u',u',u';',u'?',u'।',u':',u'\\',u'/']
	#the symbols in order are . , ; ? | : \ /
	puncvalues=[10002,10003,10004,10005,10006,10007,10008,10009]
	spacevalue=10001 #value for space
	space=u' '
	seperators=punctuations+[space]
	def __init__(self):
		pass
	
	def setText(self,text):
		text=text.replace(u'क्ष',u'诶')
		text=text.replace(u'त्र',u'比')
		text.replace(u'ज्ञ',u'西')
		self.maintext=text
	
	def PeekNextChar(self):
		if(self.pointer >= len(self.text)):
			return 0 #return 0 incase of overflow
		return self.text[self.pointer]
	
	def GetNextChar(self):
		if(self.pointer >= len(self.text)):
			return 0 #return 0 incase of overflow
		p=self.text[self.pointer]
		self.pointer+=1
		return p
	
	def IgnoreSpace(self):
		if(self.pointer >= len(self.text)):
			return
		while(self.pointer < len(self.text) and self.GetNextChar() == ' '):
			pass
		self.pointer-=1
		return;
	#this even seperates the letters like न्द्र to न् + द्र
	def Level1(self,text):
		tree=TreeNode()
		tree.SetData(text) #the topmost brach consist of all the text
		nextnode=TreeNode() #the next node
		pointer=0
		while pointer < len(text):
			nc=text[pointer]
			pointer+=1
			#first of all check if the next character is a symbol like comma and full stop
			if nc in self.punctuations:
				nextnode.SetData(nc)
				tree.AddChild(nextnode)
				nextnode=TreeNode()
			elif nc in self.alphabets:
				nextnode.SetData(nc) if nextnode.GetData() == 0 else nextnode.SetData(nextnode.data+nc)
				khutta=False #aile samma khutta kateko chaina
				while( pointer < len(text) and text[pointer] in self.allsymbols):
					nextnode.SetData(nextnode.data+text[pointer])
					pointer+=1
				tree.AddChild(nextnode)
				nextnode=TreeNode()
		return tree
	#divides word into smaller tokens
	def Level2(self):
		tree=TreeNode()
		tree.SetData(self.text) #the topmost brach consist of all the text
		nextnode=TreeNode() #the next node
		while True:
			self.IgnoreSpace()
			nc=self.GetNextChar()
			#first of all check if the next character is a symbol like comma and full stop
			if nc in self.punctuations:
				nextnode.SetData(nc)
				tree.AddChild(nextnode)
				nextnode=TreeNode()
			elif nc in self.alphabets:
				nextnode.SetData(nc) if nextnode.GetData() == 0 else nextnode.SetData(nextnode.data+nc)
				khutta=False #aile samma khutta kateko chaina
				while(self.PeekNextChar() in self.symbols):
					nextnode.SetData(nextnode.data+self.GetNextChar())
				if(self.PeekNextChar() == self.khuttakateko):
					khutta=True
					nextnode.SetData(nextnode.data+self.GetNextChar())
				if not khutta:
					child=self.Level1(nextnode.GetData())
					if(len(child.children) > 1):
						for c in child.children:
							nextnode.AddChild(c)
					tree.AddChild(nextnode)
					nextnode=TreeNode()
			self.IgnoreSpace()
			if(self.PeekNextChar() == 0):
				break
		if(nextnode.data != 0):
			tree.AddChild(nextnode)
		if(len(tree.children) == 1): #if only one child, return it
			return tree.children[0]
		return tree
	
	def Level3(self):
		tree=TreeNode()
		tree.SetData(self.maintext) #the topmost brach consist of all the text
		word=''
		p=0
		while p < len(self.maintext):
			char=self.maintext[p]
			p+=1
			if char in self.seperators:
				if(len(word) > 0):
					self.text=word
					#if word[-1:] in self.kakha:
					#	self.text+=self.khuttakateko
					self.pointer=0
					tree.AddChild(self.Level2())
					#add another child to represent the punctuation
					node=TreeNode()
					node.SetData(char)
					tree.AddChild(node)
					word=''
			elif char in self.numbers:
				dstart=p
				number=char
				while p < len(self.maintext) and (self.maintext[p] in self.numbers or self.maintext[p]==u'.'):
					number+=self.maintext[p]
					p+=1
				numinword=self.convertnum(number)
				lettersigns=[u'$',u'€',u'₹']
				letterwords=[u' डलर  ',u' इउरो  ',u' रुपैया  ']
				
				lastletter=word[len(word)-1:]
				if lastletter in lettersigns:
					word=word[:-1]
					numinword+=letterwords[lettersigns.index(lastletter)]
				elif p < len(self.maintext) and self.maintext[p] in lettersigns:
					p+=1
					numinword+=letterwords[lettersigns.index(self.maintext[p-1])]
				elif word==u'रू' or word==u'रू.':
					word=''
					numinword+=u' रुपैया  '
				elif len(tree.children) > 2 and tree.children[len(tree.children)-2].data == u'रू':
					numinword+=u' रुपैया  '
					tree.children=tree.children[:-2]
				self.maintext=self.maintext[:dstart-1]+numinword+self.maintext[p:]
				p=dstart-1					
				#replace the digit by word
			else:
				word+=char
		if(len(word) > 0):
			self.text=word
			self.pointer=0
			tree.AddChild(self.Level2())
		if(len(tree.children) == 1): #if only one child, return it
			return tree.children[0]
		return tree
	def ConverttoList(self,treenode):
		if(len(treenode.children) > 0):
			#analyze the data in treenode.data to see if we can directly generate something
			#else
			output=[]
			for smallernodes in treenode.children:
				output+=self.ConverttoList(smallernodes)
			return output
		else:
			#this is one letter or symbol only.
			if treenode.data in self.seperators:
				if treenode.data == self.space:
					return [self.spacevalue]
				elif treenode.data in self.punctuations:
					index=self.punctuations.index(treenode.data)
					return [self.puncvalues[index]]
			else:
				#it is a character (word)
				word=treenode.data
				#the first character is always the letter
				letter=word[0]
				if letter in self.numbers:
					return [self.numbers.index(letter)+100000] #index of sunya(0) is 100000 and so on
				if letter in self.firstones:
					return [self.firstones.index(letter)]
				#it is not number nor अ','आ...it is ka kha,ga...etc. Symbols may be attached with them
				#the second character means the symbol (ki,ku....) till now
				if not letter in self.kakha:
					return [] #this is not supposed to happen :D
				letterindex=self.kakha.index(letter)
				letterindex+=1 #the first 12 rows are packed by अ','आ
				symbolindex=0
				
				symbol=''
				if(len(word) > 1):
					symbol=word[1]
					if symbol in self.symbols:
						symbolindex=self.symbols.index(symbol)+1
					elif symbol==self.khuttakateko:
						return [letterindex*12+0.5]
				return [letterindex*12+symbolindex]
				#it cannot handle more than 1 symbol currently
	def GetListOutput(self):
		return self.ConverttoList(self.tree) #output to give to manish....
	def Parse(self):
		self.tree=self.Level3()
		return self.tree
	def ConvertBelowHundred(self,num):
		num=int(num)
		text=[
		u'सुन्य',u'एक',u'दुई',u'तिन',u'चार',u'पाँच',u'छ',u'सात',u'आठ',u'नौ',
		u'दस्',u'एघार',u'बार',u'तेर',u'चौध',u'पन्ध्र',u'सोर्ह',u'सत्र',u'अठार',u'उन्नाइस',
		u'बिस',u'एक्काइस',u'बाइस',u'तेइस',u'चौबिस',u'पच्चिस',u'छब्बिस',u'सत्ताइस',u'अठ्ठाइस',u'उनन्तिस',
		u'तिस',u'एक्तिस',u'बत्तिस',u'तेत्तिस',u'चौतिस',u'पैतिस',u'छतिस',u'सड्तिस',u'अड्तिस',u'उन्चालिस',
		u'चालिस',u'एक्चालिस',u'बयालिस',u'तिर्चालिस',u'चवालिस',u'पैतालिस',u'छयालिस',u'सड्चालिस',u'अड्चालिस',u'उनन्पचास',
		u'पचास',u'एकाउन्न',u'बाउन्न',u'तृपन्न',u'चवन्न',u'पच्पन्न',u'छपन्न',u'सन्ताउन्न',u'अन्ठाउन्न',u'उनन्साठी',
		u'साठी',u'एक्सठ्ठी',u'बैसठ्ठी',u'तिर्सठ्ठी',u'चौसठ्ठी',u'पैइसठ्ठी',u'छैसठ्ठी',u'सड्सठी',u'अड्सठ्ठी',u'उन्नान्सत्तरी',
		u'सत्तरी',u'एकत्तर',u'बहत्तर',u'तिरत्तर',u'चौरत्तर',u'पचत्तर',u'चेहत्तर',u'सतहत्तर',u'अठ्हत्तर',u'',u'उनानसी',
		u'असि',u'एकासी',u'बयासी',u'तिरासी',u'चौरासी'u'पचासी',u'छयासी',u'सतासी',u'अठासी',u'उनानब्बे',
		u'नब्बे',u'एकानब्बे',u'बयानब्बे',u'तिरानब्बे',u'चौरानब्बे',u'पन्चानब्बे',u'छयानब्बे',u'सन्तानबे',u'अन्ठानब्बे',u'उन्नानसय'
		]
		if(num > 99 or num<0):
			return u''
		return text[num]
	def NepaliNumtoEnglish(self,num):
		enum=0
		for char in num:
			if char in self.numbers:
				enum=enum*10+self.numbers.index(char)
		return enum
	def convertnum(self,num):
		#get the decimal part and the integer part
		#print(num)
		pos=num.find(u'.')
		decimal=u''
		integer=u''
		if pos != -1:
			integer=num[:pos]
			decimal=num[pos+1:]
		else:
			integer=num
		text=''
		#convert the bigger parts
		digitcount=[11,9,7,5,3,2]
		words=[u'खर्ब',u'अर्ब',u'करोड',u'लाख',u'हजार',u'सय']
		for dc in digitcount:
			if len(integer) > dc :
				if self.NepaliNumtoEnglish(integer[:-dc]) > 0:
					text+=u' '+self.ConvertBelowHundred(self.NepaliNumtoEnglish(integer[:-dc]))+u' '+words[digitcount.index(dc)]+u' '
				integer=integer[len(integer)-dc:]
		if(len(integer) > 0):
			text+=u' '+self.ConvertBelowHundred(self.NepaliNumtoEnglish(integer))+u' '
		if(len(decimal) > 0):
			if(len(text) ==0):
				text+=self.ConvertBelowHundred(0)
			text+=u' दस्मलब  ';
			for char in decimal:
				if char in self.numbers:
					text+=u' '+self.ConvertBelowHundred(self.NepaliNumtoEnglish(char))+u' '
		return text

#parser=Parser();
#parser.setText(u'मेरो नाम अनुप पोख्रेल हो । ') 569054 78625 089289 88124 
#output=parser.Parse()
#print(parser.GetListOutput())
#output.Print()
#PrintText(u' - '+parser.convertnum(u'000'))
#वी
#print(parser.NepaliNumToEnglish(u'१२३.४५६.७८९०  '))
#nepnum=u'७३६७.६७३६७३६७३ '
#print(number)
#PrintText(parser.convertnum(nepnum))
#Form.show()
#sys.exit(app.exec_())