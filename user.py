from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit,QSpacerItem,QSizePolicy,QTextEdit,QLabel,QVBoxLayout
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1177, 681)
        MainWindow.setStyleSheet("""
        /* Genel Widget Stili */
        QWidget {
            background-color: #1d1f21;
            color: white;
        }

        /* QLabel Stili */
        QLabel {
            color: #e9f0ec;
            font-size: 14px;
        }

        /* QLineEdit Stili */
        QLineEdit {
            background-color: #333;
            border: 1px solid #4CAF50;
            color: white;
            padding: 5px;
            font-size: 12px;
        }

        /* QPushButton Stili */
        QPushButton {
            background-color: #225523;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
            border: none;
        }
        QPushButton:hover {
            background-color: #0b350d;
        }

        /* QProgressBar Stili */
        QProgressBar {
            background-color: #333;
            border-radius: 5px;
        }
        QProgressBar::chunk {
            background-color: #4CAF50;
            border-radius: 5px;
        }

        /* QCheckBox Stili */
        QCheckBox {
            color: #a8e6cf;
            font-size: 12px;
        }

        /* QTextEdit Stili */
        QTextEdit {
            background-color: #333;
            color: white;
            border: 1px solid #050505;
        }

        /* QTableWidget Stili */
        QTableWidget {
            background-color: #2e2e2e;
            color: white;
            border: 1px solid #444;
            gridline-color: #444;
            font-size: 14px;
            selection-background-color: #2D89EF;
            selection-color: white;
            alternate-background-color: #252526;
            border-radius: 8px;
        }
        QTableWidget QHeaderView::section {
            background-color: #444;
            color: white;
            padding: 8px;
            border-right: 2px solid #666;            
            font-weight: bold;
        }
        QTableWidget::item {
            padding: 10px;
            border-radius: 5px;
            border-right: 1px solid #555;
        }
        QTableWidget::item:selected {
            background-color: #2D89EF;
            color: white;
        }

        /* QScrollBar Stili */
        QScrollBar:vertical {
            background: #222;
            width: 8px;
        }
        QScrollBar::handle:vertical {
            background: #555;
            min-height: 20px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical:hover {
            background: #777;
        }
    """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 1161, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 120, 461, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_cpu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_cpu.setObjectName("pushButton_cpu")

        self.pushButton_sunucu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_sunucu.setObjectName("pushButton_sunucu")
        self.verticalLayout.addWidget(self.pushButton_sunucu)
        self.pushButton_sunucu.setText("Sunucu Durumu")


        self.verticalLayout.addWidget(self.pushButton_cpu)
        self.pushButton_tablo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_tablo.setObjectName("pushButton_tablo")
        self.verticalLayout.addWidget(self.pushButton_tablo)

        self.pushButton_geometri = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_geometri.setObjectName("pushButton_geometri")
        self.verticalLayout.addWidget(self.pushButton_geometri)
        self.pushButton_geometri.setText("Geometrik Kontrol")

        self.pushButton_indeks = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_indeks.setObjectName("pushButton_indeks")
        self.verticalLayout.addWidget(self.pushButton_indeks)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(430, 50, 271, 20))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)

        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.page_6)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(290, 30, 541, 451))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")



        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_7.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_7.addWidget(self.lineEdit_4)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.pushButton_pg_baglan = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_pg_baglan.setObjectName("pushButton_pg_baglan")
        self.verticalLayout_7.addWidget(self.pushButton_pg_baglan)
        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1131, 581))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.progressBar_cpu = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_cpu.setProperty("value", 24)
        self.progressBar_cpu.setObjectName("progressBar_cpu")
        self.verticalLayout_5.addWidget(self.progressBar_cpu)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.progressBar_disk = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_disk.setProperty("value", 24)
        self.progressBar_disk.setObjectName("progressBar_disk")
        self.verticalLayout_5.addWidget(self.progressBar_disk)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.progressBar_ram = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_ram.setProperty("value", 24)
        self.progressBar_ram.setObjectName("progressBar_ram")
        self.verticalLayout_5.addWidget(self.progressBar_ram)
        
        self.textEdit_cpu = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_cpu.setObjectName("textEdit_cpu")
        font2 = QFont("Times New Roman", 14, QFont.Bold) 
        self.textEdit_cpu.setFont(font2)
        self.verticalLayout_5.addWidget(self.textEdit_cpu)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 1141, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_tabloveri = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_tabloveri.setObjectName("checkBox_tabloveri")
        self.horizontalLayout_5.addWidget(self.checkBox_tabloveri)
        self.checkBox_pk_tanimli_olmayan = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_pk_tanimli_olmayan.setObjectName("checkBox_pk_tanimli_olmayan")
        self.horizontalLayout_5.addWidget(self.checkBox_pk_tanimli_olmayan)
        self.checkBox_view_performans = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_view_performans.setObjectName("checkBox_view_performans")
        self.horizontalLayout_5.addWidget(self.checkBox_view_performans)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_enbuyuk_tablo = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_enbuyuk_tablo.setObjectName("checkBox_enbuyuk_tablo")
        self.horizontalLayout_4.addWidget(self.checkBox_enbuyuk_tablo)
        self.checkBox_pk_string = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_pk_string.setObjectName("checkBox_pk_string")
        self.horizontalLayout_4.addWidget(self.checkBox_pk_string)
        self.checkBox_join_view = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_join_view.setObjectName("checkBox_join_view")
        self.horizontalLayout_4.addWidget(self.checkBox_join_view)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_tablorapor = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_tablorapor.setObjectName("pushButton_tablorapor")
        self.horizontalLayout_3.addWidget(self.pushButton_tablorapor)
        self.pushButton_tablo_temizle = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_tablo_temizle.setObjectName("pushButton_tablo_temizle")
        self.horizontalLayout_3.addWidget(self.pushButton_tablo_temizle)
        self.pushButton_tablo_rapor_indir = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_tablo_rapor_indir.setObjectName("pushButton_tablo_rapor_indir")
        self.horizontalLayout_3.addWidget(self.pushButton_tablo_rapor_indir)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.textEdit_tablo = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_tablo.setObjectName("textEdit_tablo")
        font2 = QFont("Times New Roman", 14, QFont.Bold) 
        self.textEdit_tablo.setFont(font2)
        self.verticalLayout_4.addWidget(self.textEdit_tablo)
        self.stackedWidget.addWidget(self.page_4)

        
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)


#########################################

########################################

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.pushButton_carpi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_carpi.setGeometry(QtCore.QRect(1110, 10, 51, 21))
        self.pushButton_carpi.setObjectName("pushButton_carpi")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 671, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_conn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_conn.setObjectName("pushButton_conn")
        self.horizontalLayout_2.addWidget(self.pushButton_conn)
        spacer = QSpacerItem(5, 3, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_pg = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_pg.setText("")
        self.label_pg.setObjectName("label_pg")
        self.horizontalLayout_2.addWidget(self.label_pg)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_postgis = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_postgis.setText("")
        self.label_postgis.setObjectName("label_postgis")
        self.horizontalLayout_2.addWidget(self.label_postgis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Page 7 - Sunucu Durumu
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        
        # Layout
        self.verticalLayoutWidget_sunucu = QtWidgets.QWidget(self.page_7)
        self.verticalLayoutWidget_sunucu.setGeometry(QtCore.QRect(10, 10, 1151, 600))
        self.verticalLayoutWidget_sunucu.setObjectName("verticalLayoutWidget_sunucu")
        
        self.verticalLayout_sunucu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_sunucu)
        self.verticalLayout_sunucu.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_sunucu.setObjectName("verticalLayout_sunucu")
        
        # Checkboxes
        self.cb1 = QtWidgets.QCheckBox("Veritabanı Aktif Bağlantı Bilgileri", self.page_7)
        self.cb2 = QtWidgets.QCheckBox("Tune Ayarları", self.page_7)
        self.cb3 = QtWidgets.QCheckBox("Veritabanı Obje Bilgileri", self.page_7)
        self.cb4 = QtWidgets.QCheckBox("Disk Giriş/Çıkış Performansını Kontrol Et", self.page_7)
        
        # Checkbox Layout
        cb_layout1 = QtWidgets.QHBoxLayout()
        cb_layout1.addWidget(self.cb1)
        cb_layout1.addWidget(self.cb2)
        
        cb_layout2 = QtWidgets.QHBoxLayout()
        cb_layout2.addWidget(self.cb3)
        cb_layout2.addWidget(self.cb4)
        
        self.verticalLayout_sunucu.addLayout(cb_layout1)
        self.verticalLayout_sunucu.addLayout(cb_layout2)
        
        # Buttons
        self.runReportButton = QtWidgets.QPushButton("Raporu Çalıştır", self.page_7)
        self.genel_ayar_temizle = QtWidgets.QPushButton("Temizle", self.page_7)
        self.downloadReportButton = QtWidgets.QPushButton("Raporu İndir", self.page_7)
        
        # Button Layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.runReportButton)
        btn_layout.addWidget(self.genel_ayar_temizle)
        btn_layout.addWidget(self.downloadReportButton)
        
        self.verticalLayout_sunucu.addLayout(btn_layout)
        
        self.resultTextEdit = QtWidgets.QTextEdit(self.page_7)
        self.resultTextEdit.setObjectName("resultTextEdit")
        self.verticalLayout_sunucu.addWidget(self.resultTextEdit)
        self.stackedWidget.addWidget(self.page_7)
        self.resultTextEdit.setReadOnly(True)

        font2 = QFont("Times New Roman", 14, QFont.Bold) 
        self.resultTextEdit.setFont(font2)


##################################################

        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")

        # Layout
        self.verticalLayoutWidget_index = QtWidgets.QWidget(self.page_8)
        self.verticalLayoutWidget_index.setGeometry(QtCore.QRect(10, 10, 1151, 600))
        self.verticalLayoutWidget_index.setObjectName("verticalLayoutWidget_sunucu")

        self.verticalLayout_index = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_index)
        self.verticalLayout_index.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_index.setObjectName("verticalLayout_index")

        # Radio Buttons
        self.rb_kullanilmayan_index = QtWidgets.QRadioButton("Kullanılmayan İndeksler", self.page_8)
        self.rb_index_oran = QtWidgets.QRadioButton("İndeks Kullanım Oranları ve Boyutları", self.page_8)
        self.rb_btree = QtWidgets.QRadioButton("Bir kolona birden fazla B-tree İndeksi Tanımlanan Tablolar", self.page_8)
        self.rb_index_bloat = QtWidgets.QRadioButton("Şişmiş İndeksler", self.page_8)

        # Radio Button'ları grupla (yalnızca birinin seçilebilmesi için)
        self.radio_group = QtWidgets.QButtonGroup(self.page_8)
        self.radio_group.addButton(self.rb_kullanilmayan_index)
        self.radio_group.addButton(self.rb_index_oran)
        self.radio_group.addButton(self.rb_btree)
        self.radio_group.addButton(self.rb_index_bloat)

        # Radio Button Layout
        rb_layout1 = QtWidgets.QHBoxLayout()
        rb_layout1.addWidget(self.rb_kullanilmayan_index)
        rb_layout1.addWidget(self.rb_index_oran)

        rb_layout2 = QtWidgets.QHBoxLayout()
        rb_layout2.addWidget(self.rb_btree)
        rb_layout2.addWidget(self.rb_index_bloat)

        self.verticalLayout_index.addLayout(rb_layout1)
        self.verticalLayout_index.addLayout(rb_layout2)

        # Buttons
        self.run_report_index = QtWidgets.QPushButton("Raporu Çalıştır", self.page_8)
        self.index_clear = QtWidgets.QPushButton("Temizle", self.page_8)
        self.downloadReportButton_index = QtWidgets.QPushButton("Raporu İndir", self.page_8)

        # Button Layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.run_report_index)
        btn_layout.addWidget(self.index_clear)
        btn_layout.addWidget(self.downloadReportButton_index)

        self.verticalLayout_index.addLayout(btn_layout)

        # QTableWidget Tanımlama (QTextEdit yerine)
        self.index_result_table = QtWidgets.QTableWidget(self.page_8)
        self.index_result_table.setObjectName("index_result_table")

        # Kolon başlıkları
        headers = [
            "Tablo Adı", "İndeks Adı", "İndeks Kolonları", "İndeks Boyutu", 
            "İndeks Tarama Sayısı", "İndeks Kullanım Oranı (%)"
        ]

        self.index_result_table.setColumnCount(len(headers))
        self.index_result_table.setHorizontalHeaderLabels(headers)
        self.index_result_table.horizontalHeader().setStretchLastSection(True)
        self.index_result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Düzenlemeyi kapat
        self.index_result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Satır seçimi aktif et
        self.index_result_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)  # Otomatik boyutlandırma

        # QTableWidget'i Layout'a ekle
        self.verticalLayout_index.addWidget(self.index_result_table)

        self.stackedWidget.addWidget(self.page_8)
        self.index_result_table.setAlternatingRowColors(True)

        # Kolon başlıklarını tam genişlet
        header = self.index_result_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)



##################################################

        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")

        self.verticalLayoutWidget_geo = QtWidgets.QWidget(self.page_6)
        self.verticalLayoutWidget_geo.setGeometry(QtCore.QRect(10, 10, 1151, 600))
        self.verticalLayoutWidget_geo.setObjectName("verticalLayoutWidget_geo")

        self.verticalLayout_geo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_geo)
        self.verticalLayout_geo.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_geo.setObjectName("verticalLayout_geo")

        self.rb_geo_view = QtWidgets.QRadioButton("Geometrik fonksiyon içeren viewlar", self.page_6)
        self.rb_geo_table = QtWidgets.QRadioButton("Geometrik veri içeren tablolar", self.page_6)
        self.rb_srid = QtWidgets.QRadioButton("SRID Tanımlanmamış Kolonlar", self.page_6)
        self.rb_gist = QtWidgets.QRadioButton("GIST index olmayan geometrik kolonlar", self.page_6)

        rb_layout1 = QtWidgets.QHBoxLayout()
        rb_layout1.addWidget(self.rb_geo_view)
        rb_layout1.addWidget(self.rb_geo_table)

        rb_layout2 = QtWidgets.QHBoxLayout()
        rb_layout2.addWidget(self.rb_srid)
        rb_layout2.addWidget(self.rb_gist)

        self.verticalLayout_geo.addLayout(rb_layout1)
        self.verticalLayout_geo.addLayout(rb_layout2)

        # Buttons
        self.run_report_geo = QtWidgets.QPushButton("Raporu Çalıştır", self.page_6)
        self.geo_t_clear = QtWidgets.QPushButton("Temizle", self.page_6)
        self.downloadReportButton_geo = QtWidgets.QPushButton("Raporu İndir", self.page_6)

        # Button Layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.run_report_geo)
        btn_layout.addWidget(self.geo_t_clear)
        btn_layout.addWidget(self.downloadReportButton_geo)

        self.verticalLayout_geo.addLayout(btn_layout)

        self.result_geo = QtWidgets.QTableWidget(self.page_6)
        self.result_geo.setObjectName("result_geo")
        self.result_geo.horizontalHeader().setStretchLastSection(True)
        self.result_geo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  
        self.result_geo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) 
        self.result_geo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)  
        self.result_geo.setAlternatingRowColors(True)

        self.verticalLayout_geo.addWidget(self.result_geo)

        # Add page to stacked widget
        self.stackedWidget.addWidget(self.page_6)
        

        # Footer için bir widget ekliyoruz
        footer_label = QLabel("Bir hata ile karşılaşırsanız akayburkay23@gmail.com adresine ulaşabilirsiniz.")
        footer_label.setStyleSheet("color: gray; font-size: 10pt; padding-top: 10px;")
        footer_label.setAlignment(Qt.AlignCenter)  # Ortaya hizalama

        # Footer'ı en altta konumlandırıyoruz
        self.footerLayout = QVBoxLayout()
        self.footerLayout.addWidget(footer_label)
        
        # Footer'ı ana layout'a ekliyoruz
        self.verticalLayout_3.addLayout(self.footerLayout)
##################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBPulse"))
        self.setWindowIcon(QIcon("icon/db.ico"))  
        self.pushButton_cpu.setText(_translate("MainWindow", "Sistem Durumu"))
        self.pushButton_tablo.setText(_translate("MainWindow", "Tablo ve View Analizi"))
        self.pushButton_indeks.setText(_translate("MainWindow", "İndeks Analizi"))
        self.label.setMinimumWidth(500)

        self.label_7.setText(_translate("MainWindow", "Host:"))
        self.label_8.setText(_translate("MainWindow", "Port:"))
        self.label_9.setText(_translate("MainWindow", "Username:"))
        self.label_11.setText(_translate("MainWindow", "Password:"))
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.label_10.setText(_translate("MainWindow", "Database:"))
        self.pushButton_pg_baglan.setText(_translate("MainWindow", "Bağlan"))
        self.label_2.setText(_translate("MainWindow", "CPU Kullanımı:"))
        self.label_4.setText(_translate("MainWindow", "Disk Kullanımı:"))
        self.label_3.setText(_translate("MainWindow", "RAM Kullanımı:"))
        self.checkBox_tabloveri.setText(_translate("MainWindow", "En Çok Veri Sayısına Sahip Tablolar"))
        self.checkBox_pk_tanimli_olmayan.setText(_translate("MainWindow", "Primary Key Tanımı Olmayan Tablolar"))
        self.checkBox_view_performans.setText(_translate("MainWindow", "View Sorgu Süreleri"))
        self.checkBox_enbuyuk_tablo.setText(_translate("MainWindow", "En büyük 10 tablo"))
        self.checkBox_pk_string.setText(_translate("MainWindow", "Primary Key String Olan Tablolar"))
        self.checkBox_join_view.setText(_translate("MainWindow", "3 Veya Daha Fazla JOIN İçeren Viewlar"))
        self.pushButton_tablorapor.setText(_translate("MainWindow", "Raporu Çalıştır"))
        self.pushButton_tablo_temizle.setText(_translate("MainWindow", "Temizle"))
        self.pushButton_tablo_rapor_indir.setText(_translate("MainWindow", "Raporu İndir"))
        self.pushButton_carpi.setText(_translate("MainWindow", "X"))
        self.pushButton_carpi.setStyleSheet("QPushButton {background-color: red; color: white; border: none; font-size: 12px;}")
        self.pushButton_conn.setText(_translate("MainWindow", "Veritabanına Bağlan / Değiştir"))
        self.label_5.setText(_translate("MainWindow", "PostgreSQL Versiyon:"))
        self.label_6.setText(_translate("MainWindow", "POSTGIS Versiyon:"))

