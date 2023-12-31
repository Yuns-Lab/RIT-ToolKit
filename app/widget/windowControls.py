# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QImage, QBrush, QColor, QFont, QIcon

from qfluentwidgets import NavigationWidget, isDarkTheme
from qframelesswindow import TitleBar

from ..common.resource import grp

class AvatarWidget(NavigationWidget):
    ''' Avatar widget '''
    def __init__(self, parent = None):
        super().__init__(isSelectable = False, parent = parent)
        self.avatar = QImage(grp('resource/lingyun.jpg')).scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        #
        painter.setPen(Qt.NoPen)
        #
        if self.isPressed:
            painter.setOpacity(0.7)
        # draw background
        if self.isEnter:
            c = 255 if isDarkTheme() else 0
            painter.setBrush(QColor(c, c, c, 10))
            painter.drawRoundedRect(self.rect(), 5, 5)
        # draw avatar
        painter.setBrush(QBrush(self.avatar))
        painter.translate(8, 6)
        painter.drawEllipse(0, 0, 24, 24)
        painter.translate(-8, -6)
        #
        if not self.isCompacted:
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
            font = QFont('Segoe UI')
            font.setPixelSize(14)
            painter.setFont(font)
            painter.drawText(QRect(44, 0, 255, 36), Qt.AlignVCenter, self.tr('Author：LingyunAwA'))

class CustomTitleBar(TitleBar):
    ''' Title bar with icon and title '''
    def __init__(self, parent):
        super().__init__(parent)
        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 10)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.window().windowIconChanged.connect(self.setIcon)
        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)
        # layout overwriting
        self.hBoxLayout.setContentsMargins(8, 0, 0, 0)
        self.hBoxLayout.setSpacing(7)
    #
    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()
    #
    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))