import unittest
import os
import winsound
import math
#import everything needed (just copied from test)
from pydub import AudioSegment
from pydub.utils import db_to_float, ratio_to_db
from TTS_parser import *
from PyQt4 import QtCore, QtGui
data_dir = os.path.join(os.path.dirname(__file__), 'spaced barakhari')
mainfile = AudioSegment.from_wav(os.path.join(data_dir, 'final_normalised2.wav'))
final2=(mainfile[:1000]-mainfile.rms)[:0]
for ms in mainfile:
	ms=ms+(100-ms.rms)
	final2=final2+ms
final2.export(data_dir+"\\abc.wav","wav")