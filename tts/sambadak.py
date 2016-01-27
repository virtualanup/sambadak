# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtfinal.ui'
#
# Created: Thu Jun 27 21:34:13 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!
import unittest
import os
import math
#import everything needed (just copied from test)
from pydub import AudioSegment
from pydub.utils import db_to_float, ratio_to_db
from TTS_parser import *
from PyQt4 import QtCore, QtGui
data_dir = os.path.join(os.path.dirname(__file__), 'spaced barakhari')
class MessageBox(QtGui.QWidget):

 
    def __init__ (self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
 
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')
 
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self,  'Message',  'Are you sure to quit?',  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
 
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
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

class Ui_MainWindow(object):
    def __init__(self):
		print "start"
		#self.foo()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(748, 611)
        MainWindow.setMaximumSize(QtCore.QSize(748, 672))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 500, 195))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/logo.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-30, -10, 851, 611))
        self.label_2.setMaximumSize(QtCore.QSize(851, 611))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/bg.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.savebtn = QtGui.QCommandLinkButton(self.centralwidget)
        self.savebtn.setGeometry(QtCore.QRect(40, 470, 231, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(20)
        font.setKerning(True)
        self.savebtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savebtn.setIcon(icon)
        self.savebtn.setIconSize(QtCore.QSize(75, 100))
        self.savebtn.setAutoRepeat(True)
        self.savebtn.setObjectName(_fromUtf8("savebtn"))
        self.speakbtn = QtGui.QCommandLinkButton(self.centralwidget)
        self.speakbtn.setGeometry(QtCore.QRect(500, 470, 191, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(18)
        self.speakbtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speakbtn.setIcon(icon1)
        self.speakbtn.setIconSize(QtCore.QSize(75, 70))
        self.speakbtn.setObjectName(_fromUtf8("speakbtn"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 240, 611, 191))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Caslon Pro"))
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 491, 161))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/logo.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.letterslider = QtGui.QSlider(self.centralwidget)
        self.letterslider.setGeometry(QtCore.QRect(60, 200, 470, 19))
        self.letterslider.setMaximum(200)
        self.letterslider.setOrientation(QtCore.Qt.Horizontal)
        self.letterslider.setObjectName(_fromUtf8("letterslider"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 440, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.wordSlider = QtGui.QSlider(self.centralwidget)
        self.wordSlider.setGeometry(QtCore.QRect(60, 460, 611, 19))
        self.wordSlider.setMinimum(50)
        self.wordSlider.setMaximum(1000)
        self.wordSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wordSlider.setObjectName(_fromUtf8("wordSlider"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuTTS = QtGui.QMenu(self.menubar)
        self.menuTTS.setObjectName(_fromUtf8("menuTTS"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp_F1 = QtGui.QAction(MainWindow)
        self.actionHelp_F1.setObjectName(_fromUtf8("actionHelp_F1"))
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTTS.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.savebtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveclickk)
        QtCore.QObject.connect(self.speakbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.playclickk)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def saveclickk(self):
		self.connector()
		QtGui.QMessageBox.question(None,u'सेभ भयो',u'सेभ भएको छ । कृपया ओके थिच्नुहोस्',QtGui.QMessageBox.Ok)
		
    def connector(self):
	
		#set the directory of the data

		

		#as we will have a single file from beg to end assuming mainfile is the file which is a wav
		mainfile = AudioSegment.from_wav(os.path.join(data_dir, 'final_normalised.wav'))
	

		#get the time stamp from 2d array of tuples 
			#format is	array sound=
			#[[ka, ka , ki ,ki ,ku , ku , ke ,kai , ko , kau, kam, ka],
			#kha..
			#gha...
			#.
			#.
			#.
			#]
			#eg for ka and ka
			#[[(0.5,0.6),(0.7,0.8),......],[],[],[]]	
		#sound_timestamp=[[(285300,285600),(230850,231070)],[(91800,92200)]]
		#sound_timestamp=[[(306000,306350),(29070,29350)],[(216700,217200)]]
		#sound_timestamp=[[(519, 812), (1645, 1888), (2736, 3098), (3889, 4304), (5055, 5423), (6007, 6502), (7618, 7971), (8922, 9244), (10007, 10360), (11097, 11410), (12054, 12429), (13002, 13283)],[(1194, 1429), (2298, 2625), (3466, 3740), (4603, 4896), (5680, 5955), (6792, 7042), (7913, 8222), (8944, 9252), (10054, 10384), (11168, 11518), (12298, 12611), (13400, 13622)],
		sound_timestamp=[ [(0, 298), (298, 546), (546, 913), (913, 1333), (1333, 1706), (1706, 2156), (2156, 2514), (2514, 2841), (2841, 3199), (3199, 3517), (3517, 3897), (3897, 4183)] ,
		[(4183, 4423), (4423, 4755), (4755, 5069), (5069, 5368), (5368, 5648), (5648, 5903), (5903, 6213), (6213, 6536), (6536, 6871), (6871, 7243), (7243, 7562), (7562, 7842)] ,
		[(7842, 8180), (8180, 8502), (8502, 8795), (8795, 9128), (9128, 9407), (9407, 9718), (9718, 9928), (9928, 10209), (10209, 10518), (10518, 10838), (10838, 11224), (11224, 11552)] ,
		[(11552, 11955), (11955, 12405), (12405, 12842), (12842, 13160), (13160, 13568), (13568, 13978), (13978, 14412), (14412, 14776), (14776, 15197), (15197, 15544), (15544, 15949), (15949, 16221)] ,
		[(16221, 16526), (16526, 16976), (16976, 17361), (17361, 17796), (17796, 18181), (18181, 18510), (18510, 18838), (18838, 19199), (19199, 19552), (19552, 19887), (19887, 20279), (20279, 20577)] ,
		[(20577, 21027), (21027, 21477), (21477, 21927), (21927, 22377), (22377, 22827), (22827, 23242), (23242, 23692), (23592, 24142), (24142, 24592), (24592, 24999), (24999, 25408), (25408, 25858)] ,
		[(25858, 26197), (26197, 26573), (26573, 26952), (26952, 27375), (27375, 27654), (27654, 27956), (27956, 28328), (28328, 28684), (28684, 29042), (29042, 29380), (29380, 29723), (29723, 29997)] ,
		[(29997, 30444), (30444, 30845), (30845, 31293), (31293, 31716), (31716, 32083), (32083, 32533), (32533, 32970), (32970, 33420), (33420, 33818), (33818, 34268), (34268, 34697), (34697, 35013)] ,
		[(35013, 35463), (35463, 35913), (35913, 36363), (36363, 36781), (36781, 37231), (37231, 37681), (37681, 38131), (38131, 38581), (38581, 39031), (39031, 39355), (39355, 39742), (39742, 40141)] ,
		[(40141, 40558), (40558, 40969), (40969, 41396), (41396, 41846), (41846, 42287), (42287, 42737), (42737, 43146), (43146, 43594), (43594, 44044), (44044, 44494), (44494, 44929), (44929, 45297)] ,
		[(45297, 45747), (45747, 46197), (46197, 46647), (46647, 47097), (47097, 47547), (47547, 47997), (47997, 48447), (48447, 48897), (48897, 49347), (49347, 49797), (49797, 50204), (50204, 50526)] ,
		[(50526, 50814), (50814, 51123), (51123, 51444), (51444, 51818), (51818, 52192), (52192, 52548), (52548, 52913), (52913, 53279), (53279, 53620), (53620, 53947), (53947, 54287), (54287, 54625)] ,
		[(54625, 55070), (55070, 55483), (55483, 55872), (55872, 56306), (56306, 56724), (56724, 57109), (57109, 57523), (57523, 57892), (57892, 58316), (58316, 58758), (58758, 59208), (59208, 59557)] ,
		[(59557, 59987), (59987, 60420), (60420, 60858), (60858, 61308), (61308, 61758), (61758, 62182), (62182, 62618), (62618, 63068), (63068, 63506), (63506, 63951), (63951, 64354), (64354, 64771)] ,
		[(64771, 65167), (65167, 65539), (65539, 65955), (65955, 66397), (66397, 66760), (66760, 67210), (67210, 67660), (67660, 68028), (68028, 68443), (68443, 68813), (68813, 69263), (69263, 69576)] ,
		[(69576, 70026), (70026, 70476), (70476, 70906), (70906, 71318), (71318, 71768), (71768, 72218), (72218, 72668), (72668, 73118), (73118, 73568), (73568, 74011), (74011, 74461), (74461, 74760)] ,
		[(74760, 75035), (75035, 75383), (75383, 75686), (75686, 75964), (75964, 76251), (76251, 76551), (76551, 76843), (76843, 77161), (77161, 77468), (77468, 77761), (77761, 78056), (78056, 78298)] ,
		[(78298, 78678), (78678, 79052), (79052, 79422), (79422, 79741), (79741, 80096), (80096, 80506), (80506, 80806), (80806, 81180), (81180, 81559), (81559, 81916), (81916, 82296), (82296, 82593)] ,
		[(82593, 83038), (83038, 83488), (83488, 83938), (83938, 84388), (84388, 84838), (84838, 85288), (85288, 85738), (85738, 86176), (86176, 86626), (86626, 87076), (87076, 87498), (87498, 87877)] ,
		[(87877, 88327), (88327, 88777), (88777, 89191), (89191, 89587), (89587, 90029), (90029, 90393), (90393, 90807), (90807, 91193), (91193, 91568), (91568, 91971), (91971, 92394), (92394, 92712)] ,
		[(92712, 93162), (93162, 93612), (93612, 94062), (94062, 94512), (94512, 94962), (94962, 95412), (95412, 95862), (95862, 96312), (96312, 96707), (96707, 97157), (97157, 97577), (97577, 97985)] ,
		[(97985, 98311), (98200, 98669), (98669, 99058), (99058, 99439), (99439, 99883), (99883, 100269), (100269, 100629), (100629, 100979), (100979, 101328), (101328, 101672), (101672, 102064), (102064, 102342)] ,
		[(102342, 102683), (102683, 103031), (103031, 103389), (103389, 103747), (103747, 104153), (104153, 104539), (104539, 104911), (104911, 105251), (105251, 105607), (105607, 106003), (106003, 106434), (106434, 106741)] ,
		[(106567, 107191), (107191, 107587), (107587, 107974), (107974, 108401), (108401, 108851), (108851, 109261), (109261, 109675), (109675, 110066), (110066, 110421), (110421, 110849), (110849, 111285), (111285, 111620)] ,
		[(111620, 112045), (112045, 112455), (112455, 112802), (112802, 113165), (113165, 113569), (113569, 113913), (113913, 114307), (114307, 114662), (114662, 115022), (115022, 115431), (115431, 115781), (115781, 116129)] ,
		[(116129, 116496), (116496, 116907), (116907, 117276), (117276, 117673), (117673, 118123), (118123, 118552), (118552, 118999), (118999, 119327), (119327, 119704), (119704, 120094), (120094, 120530), (120530, 120805)] ,
		[(120805, 121255), (121255, 121705), (121705, 122155), (122155, 122605), (122605, 123055), (123055, 123505), (123505, 123955), (123955, 124405), (124405, 124855), (124855, 125305), (125305, 125755), (125755, 126205)] ,
		[(126205, 126631), (126631, 127034), (127034, 127482), (127482, 127904), (127904, 128354), (128354, 128786), (128786, 129230), (129230, 129662), (129662, 130071), (130071, 130424), (130424, 130814), (130814, 131114)] ,
		[(131114, 131520), (131520, 131943), (131943, 132307), (132307, 132718), (132718, 133168), (133168, 133521), (133521, 133900), (133900, 134350), (134350, 134764), (134764, 135192), (135192, 135632), (135632, 135944)] ,
		[(135944, 136356), (136356, 136783), (136783, 137199), (137199, 137608), (137608, 138058), (138058, 138472), (138472, 138909), (138909, 139263), (139263, 139713), (139713, 140114), (140114, 140564), (140564, 140924)] ,
		[(140924, 141303), (141303, 141711), (141711, 142070), (142070, 142509), (142509, 142909), (142909, 143339), (143339, 143789), (143789, 144239), (144239, 144650), (144650, 145100), (145100, 145550), (145550, 145889)] ,
		[(145889, 146338), (146338, 146788), (146788, 147232), (147232, 147586), (147586, 148005), (148005, 148415), (148415, 148799), (148799, 149233), (149233, 149683), (149683, 150133), (150133, 150554), (150554, 150853)] ,
		[(150853, 151297), (151297, 151739), (151739, 152189), (152189, 152639), (152639, 153089), (153089, 153501), (153501, 153951), (153951, 154340), (154340, 154790), (154790, 155240), (155240, 155645), (155645, 156026)] ,
		[(156026, 156359), (156359, 156689), (156689, 156980), (156980, 157246), (157246, 157569), (157569, 157880), (157880, 158204), (158204, 158552), (158552, 158887), (158887, 159177), (159177, 159528), (159528, 159839)] ,
		[(159839, 160289), (160289, 160739), (160739, 161120), (161120, 161498), (161498, 161846), (161846, 162236), (162236, 162605), (162605, 162939), (162939, 163333), (163333, 163713), (163713, 164103), (164103, 164408)] ,
		[(164408, 164699), (164699, 164980), (164980, 165361), (165361, 165647), (165647, 165938), (165938, 166195), (166195, 166575), (166575, 166880), (166880, 167330), (167330, 167655), (167655, 167994), (167994, 168250)] ,
		[(168250, 168641), (168641, 168962), (168962, 169380), (169380, 169830), (169830, 170247), (170247, 170564), (170564, 170948), (170948, 171258), (171258, 171665), (171665, 172100), (172100, 172522), (172522, 172810)] ]
		#calculation routine
			#so now we obtain value from the leaves 

		#initializing the parser
		
		parser=Parser()
		text=self.textEdit.toPlainText()
		
		parser.setText(unicode(text))
		output=parser.Parse()
		leaves=parser.GetListOutput()
		print parser.GetListOutput()
		for i in sound_timestamp:
			print len(i)
			#so just do foreach value in the leaf from left ->assign a sound
			#starting from a,aa till gya ,gyaaa
			#so for mainfile[i][j][k] where i is root alphabet say ka,kha,j is ka kaa ki,and k is the specific starting=0 or ending =1
			
		start_index=0
		end_index=1
		one_sec_of_silence=mainfile[:1000]-mainfile.rms
			#initialize list as container for storing raw audio clips 	
		raw_audio=[]

			#leaves is the output from our parser
		count=1
		print sound_timestamp[23][1]
		for ind in range(0,len(leaves)):
			index=leaves[ind]
			if(ind!=len(leaves)-1):
				
				print leaves[ind+1]
				if(leaves[ind+1]==10001):
					if(index%12==0):
						if(count>1):
							index+=0.5
							count=0
							
						else:
							count=0
				else:
					count+=1
					
			if(isinstance(index,int)):
				
				if index==10001:#1 is space
					raw_audio.append(one_sec_of_silence[:self.wordSlider.value()])
				elif index==10006:#2 is purnaviram
					raw_audio.append(one_sec_of_silence[:600])
				elif index==10002:#2 is purnaviram
					raw_audio.append(one_sec_of_silence[:600])
				elif index==10003:#3 is alpaviram
					raw_audio.append(one_sec_of_silence[:250])
				elif index==10004:#4 is ardaviram
					raw_audio.append(one_sec_of_silence[:300])				
				else:
					i=index/12
					j=index%12
					duration=sound_timestamp[i][j][end_index]-sound_timestamp[i][j][start_index]
					#if(index>=0 and index<=11):
						#raw_audio.append(mainfile[sound_timestamp[i][j][start_index]+duration/6:sound_timestamp[i][j][end_index]-(duration/4)])
					#else:
					if(duration>350):
						raw_audio.append(mainfile[sound_timestamp[i][j][start_index]+0:sound_timestamp[i][j][end_index]-100])
					elif(duration<300):
						raw_audio.append(mainfile[sound_timestamp[i][j][start_index]:sound_timestamp[i][j][end_index]])
						raw_audio.append(one_sec_of_silence[:20])
					else:
						raw_audio.append(mainfile[sound_timestamp[i][j][start_index]:sound_timestamp[i][j][end_index]])	#raw_audio.append(mainfile[sound_timestamp[i][j][start_index]+10:sound_timestamp[i][j][end_index]-50])
			else:
				new_index=math.floor(index)
				i=int(index/12)
				j=int(index%12)
				#calculate duration of the audio
				duration=sound_timestamp[i][j][end_index]-sound_timestamp[i][j][start_index]
				if (duration<=0):
					print "error"
				
				else:
					#cut audio from front to half 
					raw_audio.append(mainfile[sound_timestamp[i][j][start_index]:sound_timestamp[i][j][end_index]-(duration/1.80)])
			
			
		#now its time for connecting the parts

		final=one_sec_of_silence

		for audio_part in raw_audio:
			#final=final.append(one_sec_of_silence[:1],crossfade=150)+audio_part.fade_in(150)
			final=final.append(audio_part)+one_sec_of_silence[:self.letterslider.value()]
			
#		
		#append one second silence at the end
		#final=final.append(one_sec_of_silence,crossfade=100)
				
		#write the output to output.wav
		final.export(os.path.join(data_dir, 'output.wav'),"wav")
    def playclickk(self):
		self.connector();
		winsound.PlaySound(data_dir+"\\output.wav", winsound.SND_FILENAME)		
		os.remove(data_dir+"\\output.wav")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "संवादक", None))
        self.savebtn.setText(_translate("MainWindow", "सेभ गर्नुहोस्", None))
        self.speakbtn.setText(_translate("MainWindow", "बोल्नुहोस्", None))
        self.pushButton.setText(_translate("MainWindow", "मेट्नुहोस्", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTTS.setTitle(_translate("MainWindow", "TTS", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionHelp_F1.setText(_translate("MainWindow", "Help F1", None))
	
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

