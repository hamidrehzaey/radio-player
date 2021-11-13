import sys, vlc
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

radioGooshkonPlayer = vlc.MediaPlayer('http://r.gooshkon.ir:8000/live.ogg')
radioPersianPlayer = vlc.MediaPlayer('http://r.pgbu.ir:8000/live')

class Radio(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 500)
		self.setWindowTitle("radio player")
		self.layout = QGridLayout()
		self.setLayout(self.layout)

		self.cb = QComboBox()
		self.cb.setAccessibleName("choose radio:")
		self.cb.addItems(['radio gooshkon', 'radio persian'])
		self.cb.activated.connect(self.Show)
		self.layout.addWidget(self.cb)

		self.play = QPushButton('play')
		self.play.setShortcut(QKeySequence('ctrl+p'))
		self.layout.addWidget(self.play)
		self.play.clicked.connect(self.Play)
		self.play.hide()

		self.volume = QSlider()
		self.volume.setAccessibleName('volume control')
		self.layout.addWidget(self.volume)
		self.volume.setSliderPosition(50)
		self.volume.valueChanged.connect(self.Volume)

	def Show(self):
		if self.cb.currentText() == 'radio gooshkon':
			self.play.show()
			self.play.setText('play')
			self.play.setShortcut(QKeySequence('ctrl+p'))
		else:
			if radioGooshkonPlayer.is_playing():
				msg = QMessageBox()
				msg.setWindowTitle('stop')
				msg.setText('do you really want to stop radio gooshkon?')
				msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
				execute = msg.exec()
				if execute == QMessageBox.StandardButton.Yes:
					radioGooshkonPlayer.stop()
				else:
					self.cb.setCurrentIndex(0)

		if self.cb.currentText() == 'radio persian':
			self.play.show()
			self.play.setText('play')
			self.play.setShortcut(QKeySequence('ctrl+p'))
		else:
			if radioPersianPlayer.is_playing():
				msg = QMessageBox()
				msg.setWindowTitle('stop')
				msg.setText('do you really want to stop radio persian?')
				msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
				execute = msg.exec()
				if execute == QMessageBox.StandardButton.Yes:
					radioPersianPlayer.stop()
				else:
					self.cb.setCurrentIndex(1)

	def Play(self):
		if self.cb.currentText() == 'radio gooshkon':
			if self.play.text() == 'play':
				radioGooshkonPlayer.play()
				vol = 50
				radioGooshkonPlayer.audio_set_volume(vol)
				self.play.setText('stop')
				self.play.setShortcut(QKeySequence('ctrl+s'))
				return False

			if self.play.text() == 'stop':
				radioGooshkonPlayer.stop()
				self.play.setText('play')
				self.play.setShortcut(QKeySequence('ctrl+p'))
				return False

		elif self.cb.currentText() == 'radio persian':
			if self.play.text() == 'play':
				radioPersianPlayer.play()
				vol = 50
				radioPersianPlayer.audio_set_volume(vol)
				self.play.setText('stop')
				self.play.setShortcut(QKeySequence('ctrl+s'))
				return False

			if self.play.text() == 'stop':
				radioPersianPlayer.stop()
				self.play.setText('play')
				self.play.setShortcut(QKeySequence('ctrl+p'))
				return False

	def Volume(self, value):
		if self.cb.currentText() == 'radio gooshkon':
			vol = radioGooshkonPlayer.audio_get_volume()

			if value < vol:
				voldown = radioGooshkonPlayer.audio_get_volume() - 1
				radioGooshkonPlayer.audio_set_volume(voldown)

			if value > vol:
				volUp = radioGooshkonPlayer.audio_get_volume() + 1
				radioGooshkonPlayer.audio_set_volume(volUp)

		if self.cb.currentText() == 'radio persian':
			vol = radioPersianPlayer.audio_get_volume()

			if value < vol:
				voldown = radioGooshkonPlayer.audio_get_volume() - 1
				radioPersianPlayer.audio_set_volume(voldown)

			if value > vol:
				volUp = radioGooshkonPlayer.audio_get_volume() + 1
				radioPersianPlayer.audio_set_volume(volUp)

app = QApplication(sys.argv)
window = Radio()
window.show()
sys.exit(app.exec())