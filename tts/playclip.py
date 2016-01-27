import os,winsound

from pydub import AudioSegment
from mainarr_mod import mainarr

print len(mainarr)

data_dir = os.path.join(os.path.dirname(__file__), 'spaced barakhari') 
out_dir = os.path.join(os.path.dirname(__file__), 'test out')

mainaudio= AudioSegment.from_wav(os.path.join(data_dir, 'final.wav'))

def playclip(a,b,sil=1):	
	start= a
	end= b
	# print start,end
	clip=mainaudio[start:end]
	if (sil==1):	
		silence1=clip[:100]-clip.rms
		clip=silence1+clip+silence1
	clip.export(out_dir+"\\segment.wav", format="wav") #export to a file
	winsound.PlaySound(out_dir+"\\segment.wav", winsound.SND_FILENAME)

def playsound(a,b,sil=1):	
	start= mainarr[a][b][0]
	end= mainarr[a][b][1]
	#print start,end
	clip=mainaudio[start:end]
	if (sil==1):	
		silence1=clip[:100]-clip.rms
		clip=silence1+clip+silence1
	clip.export(out_dir+"\\segment.wav", format="wav") #export to a file
	winsound.PlaySound(out_dir+"\\segment.wav", winsound.SND_FILENAME)
	


