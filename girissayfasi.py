# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girissayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_girispenceresi(object):
    def setupUi(self, girispenceresi):
        girispenceresi.setObjectName("girispenceresi")
        girispenceresi.resize(500, 217)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Python-LibraryProject-main (8)/Python-LibraryProject-main/KutuphaneProjesi/Sulu-boya-kitap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        girispenceresi.setWindowIcon(icon)
        girispenceresi.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"Spacer\" name=\"horizontalSpacer_3\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>91</x>\n"
"     <y>1</y>\n"
"     <width>41</width>\n"
"     <height>42</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>MS Sans Serif</family>\n"
"     <pointsize>10</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Horizontal</enum>\n"
"   </property>\n"
"   <property name=\"sizeHint\" stdset=\"0\">\n"
"    <size>\n"
"     <width>40</width>\n"
"     <height>20</height>\n"
"    </size>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.centralwidget = QtWidgets.QWidget(girispenceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 161, 41))
        self.pushButton.setStyleSheet("/* author = Nathan Woodrow */\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #222;\n"
"    background-color: #333;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #aaa;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #507098;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #507098;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    /*\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"    */\n"
"    background: #444;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #000;\n"
"    background-color: #444;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* MENU                                                                                 */\n"
"/* ==================================================================================== */\n"
"\n"
"QMenu\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    padding-right: 0px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    background: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #507098;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    padding: 1px;\n"
"    border: 1px solid #111;\n"
"    background-color: #888;\n"
"    color: #111;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);*/\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);*/\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* COMBO BOX                                                                            */\n"
"/* ==================================================================================== */\n"
"\n"
"QComboBox {\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0     #565656,\n"
"        stop: 0.1   #525252,\n"
"        stop: 0.5   #4e4e4e,\n"
"        stop: 0.9   #4a4a4a,\n"
"        stop: 1     #464646);\n"
"}\n"
"\n"
"\n"
"QComboBox:on {\n"
"    padding-top: 1px;\n"
"    padding-left: 3px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0     #555,\n"
"        stop: 0.1   #4C4C4C,\n"
"        stop: 0.5   #464646,\n"
"        stop: 0.9   #414141,\n"
"        stop: 1     #444);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #222;\n"
"    selection-background-color: #507098;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     border: 0px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(icons/down_arrow.png);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* SCROLL BAR                                                                           */\n"
"/* ==================================================================================== */\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #333;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border: 1px solid #111;\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    width: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #333;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border: 1px solid #111;\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    height: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"  width: 1px;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QDockWidget\n"
"{\n"
"      titlebar-close-icon: url(icons/cross.svg);\n"
"}\n"
"\n"
"QDockWidget::separator\n"
"{\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: #323232;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 0px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar {\n"
"    background: #323232;\n"
"    border: 1px solid #323232;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    /*\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    */\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"  margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);*/\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);*/\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* RADIO BUTTON                                                                         */\n"
"/* ==================================================================================== */\n"
"\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:checked,\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:unchecked,\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"}\n"
"\n"
"QGroupBox::indicator:checked,\n"
"QCheckBox::indicator:checked,\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"}\n"
"\n"
"QGroupBox::indicator:hover,\n"
"QCheckBox::indicator:hover,\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* CHECKBOX                                                                             */\n"
"/* ==================================================================================== */\n"
"\n"
"QAbstractItemView\n"
"{\n"
"  background-color: #222;\n"
"    alternate-background-color: #323232;\n"
"    color: silver;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QAbstractItemView::selected {\n"
"    border: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* TREE VIEW                                                                            */\n"
"/* ==================================================================================== */\n"
"\n"
"QTreeView {\n"
"    border: 0.5px solid rgba(108,108,108,75);\n"
"}\n"
"\n"
"QTreeView::item, QTreeView::branch {\n"
"    background: transparent;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::item:hover, QTreeView::branch:hover {\n"
"    background-color: #507098;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::item:selected, QTreeView::branch:selected {\n"
"    background-color: #507098;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(icons/caret-right_ffffff_14.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"     border-image: none;\n"
"     image: url(icons/caret-down_ffffff_14.png);\n"
"}\n"
"\n"
"QgsLayerTreeView\n"
"{\n"
"}\n"
"\n"
"QgsLayerTreeView::item\n"
"{\n"
"    border-top: 0.5px solid rgba(108,108,108,50);\n"
"    border-bottom: 0.5px solid rgba(108,108,108,50);\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QgsLayerTreeView::indicator:unchecked{\n"
"    image: url(icons/eye-blocked.svg);\n"
"}\n"
"\n"
"QgsLayerTreeView::indicator:checked {\n"
"    image: url(icons/eye.svg);\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* TABLE VIEW                                                                           */\n"
"/* ==================================================================================== */\n"
"\n"
"QHeaderView {\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: transparent;\n"
"    background-color: #323232;\n"
"    color: #777;\n"
"    border-right: 0px solid #777;\n"
"    border-top: 0px solid #777;\n"
"    padding: 0 0 2px 3px\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 35, 111, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 51, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 30, 151, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 70, 161, 31))
        self.pushButton_2.setStyleSheet("/* author = Nathan Woodrow */\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #222;\n"
"    background-color: #333;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #aaa;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #507098;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #507098;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    /*\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"    */\n"
"    background: #444;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #000;\n"
"    background-color: #444;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* MENU                                                                                 */\n"
"/* ==================================================================================== */\n"
"\n"
"QMenu\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    padding-right: 0px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    background: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #507098;\n"
"    color: #aaa;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    padding: 1px;\n"
"    border: 1px solid #111;\n"
"    background-color: #888;\n"
"    color: #111;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);*/\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);*/\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* COMBO BOX                                                                            */\n"
"/* ==================================================================================== */\n"
"\n"
"QComboBox {\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0     #565656,\n"
"        stop: 0.1   #525252,\n"
"        stop: 0.5   #4e4e4e,\n"
"        stop: 0.9   #4a4a4a,\n"
"        stop: 1     #464646);\n"
"}\n"
"\n"
"\n"
"QComboBox:on {\n"
"    padding-top: 1px;\n"
"    padding-left: 3px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0     #555,\n"
"        stop: 0.1   #4C4C4C,\n"
"        stop: 0.5   #464646,\n"
"        stop: 0.9   #414141,\n"
"        stop: 1     #444);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #222;\n"
"    selection-background-color: #507098;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     border: 0px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(icons/down_arrow.png);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* SCROLL BAR                                                                           */\n"
"/* ==================================================================================== */\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #333;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border: 1px solid #111;\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    width: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #333;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border: 1px solid #111;\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    height: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"  width: 1px;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QDockWidget\n"
"{\n"
"      titlebar-close-icon: url(icons/cross.svg);\n"
"}\n"
"\n"
"QDockWidget::separator\n"
"{\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: #323232;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 0px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);*/\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar {\n"
"    background: #323232;\n"
"    border: 1px solid #323232;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    /*\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    */\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"  margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);*/\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);*/\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* RADIO BUTTON                                                                         */\n"
"/* ==================================================================================== */\n"
"\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:checked,\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:unchecked,\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"}\n"
"\n"
"QGroupBox::indicator:checked,\n"
"QCheckBox::indicator:checked,\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"}\n"
"\n"
"QGroupBox::indicator:hover,\n"
"QCheckBox::indicator:hover,\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* CHECKBOX                                                                             */\n"
"/* ==================================================================================== */\n"
"\n"
"QAbstractItemView\n"
"{\n"
"  background-color: #222;\n"
"    alternate-background-color: #323232;\n"
"    color: silver;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QAbstractItemView::selected {\n"
"    border: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* TREE VIEW                                                                            */\n"
"/* ==================================================================================== */\n"
"\n"
"QTreeView {\n"
"    border: 0.5px solid rgba(108,108,108,75);\n"
"}\n"
"\n"
"QTreeView::item, QTreeView::branch {\n"
"    background: transparent;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::item:hover, QTreeView::branch:hover {\n"
"    background-color: #507098;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::item:selected, QTreeView::branch:selected {\n"
"    background-color: #507098;\n"
"    color: #DDD;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(icons/caret-right_ffffff_14.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"     border-image: none;\n"
"     image: url(icons/caret-down_ffffff_14.png);\n"
"}\n"
"\n"
"QgsLayerTreeView\n"
"{\n"
"}\n"
"\n"
"QgsLayerTreeView::item\n"
"{\n"
"    border-top: 0.5px solid rgba(108,108,108,50);\n"
"    border-bottom: 0.5px solid rgba(108,108,108,50);\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QgsLayerTreeView::indicator:unchecked{\n"
"    image: url(icons/eye-blocked.svg);\n"
"}\n"
"\n"
"QgsLayerTreeView::indicator:checked {\n"
"    image: url(icons/eye.svg);\n"
"}\n"
"\n"
"/* ==================================================================================== */\n"
"/* TABLE VIEW                                                                           */\n"
"/* ==================================================================================== */\n"
"\n"
"QHeaderView {\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: transparent;\n"
"    background-color: #323232;\n"
"    color: #777;\n"
"    border-right: 0px solid #777;\n"
"    border-top: 0px solid #777;\n"
"    padding: 0 0 2px 3px\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        girispenceresi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(girispenceresi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        girispenceresi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(girispenceresi)
        self.statusbar.setObjectName("statusbar")
        girispenceresi.setStatusBar(self.statusbar)
        self.actionGiri = QtWidgets.QAction(girispenceresi)
        self.actionGiri.setObjectName("actionGiri")
        self.actionKay_t_Ol = QtWidgets.QAction(girispenceresi)
        self.actionKay_t_Ol.setObjectName("actionKay_t_Ol")
        self.actionHakk_nda = QtWidgets.QAction(girispenceresi)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.action_k = QtWidgets.QAction(girispenceresi)
        self.action_k.setObjectName("action_k")
        self.menuProgram.addAction(self.actionKay_t_Ol)
        self.menuProgram.addAction(self.actionHakk_nda)
        self.menuProgram.addAction(self.action_k)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(girispenceresi)
        QtCore.QMetaObject.connectSlotsByName(girispenceresi)

    def retranslateUi(self, girispenceresi):
        _translate = QtCore.QCoreApplication.translate
        girispenceresi.setWindowTitle(_translate("girispenceresi", "Kütüphane - Giriş"))
        self.pushButton.setText(_translate("girispenceresi", "Giriş"))
        self.label_3.setText(_translate("girispenceresi", "Kullanıcı Adı:"))
        self.label_4.setText(_translate("girispenceresi", "Şifre:"))
        self.pushButton_2.setText(_translate("girispenceresi", "Kayıt Ol"))
        self.pushButton_3.setText(_translate("girispenceresi", "Admin"))
        self.menuProgram.setTitle(_translate("girispenceresi", "Program"))
        self.actionGiri.setText(_translate("girispenceresi", "Giriş"))
        self.actionKay_t_Ol.setText(_translate("girispenceresi", "Kayıt Ol"))
        self.actionHakk_nda.setText(_translate("girispenceresi", "Hakkında"))
        self.action_k.setText(_translate("girispenceresi", "Çıkış"))
