# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\FAMILIA ROJAS YANES\Desktop\programas\ganado\tracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 884)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, 5, -1, 5)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.numero = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numero.setFont(font)
        self.numero.setMaximum(999999999)
        self.numero.setObjectName("numero")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numero)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fdn = QtWidgets.QDateEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fdn.setFont(font)
        self.fdn.setCalendarPopup(True)
        self.fdn.setTimeSpec(QtCore.Qt.TimeZone)
        self.fdn.setDate(QtCore.QDate(1800, 1, 1))
        self.fdn.setObjectName("fdn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fdn)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.marca = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.marca.setFont(font)
        self.marca.setObjectName("marca")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.marca)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.sexo = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sexo.setFont(font)
        self.sexo.setObjectName("sexo")
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sexo)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dueno = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dueno.setFont(font)
        self.dueno.setEditable(True)
        self.dueno.setObjectName("dueno")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dueno)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.mama = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mama.setFont(font)
        self.mama.setMaximum(999999999)
        self.mama.setSingleStep(1)
        self.mama.setObjectName("mama")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mama)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.descripcion = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descripcion.setFont(font)
        self.descripcion.setObjectName("descripcion")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.descripcion)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.criadero = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.criadero.setFont(font)
        self.criadero.setChecked(True)
        self.criadero.setObjectName("criadero")
        self.horizontalLayout.addWidget(self.criadero)
        self.comprado = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comprado.setFont(font)
        self.comprado.setObjectName("comprado")
        self.horizontalLayout.addWidget(self.comprado)
        self.otro_procedencia = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otro_procedencia.setFont(font)
        self.otro_procedencia.setObjectName("otro_procedencia")
        self.horizontalLayout.addWidget(self.otro_procedencia)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.procedencia_uis = QtWidgets.QStackedWidget(self.groupBox_2)
        self.procedencia_uis.setObjectName("procedencia_uis")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.procedencia_uis.addWidget(self.page_5)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comprado_precio = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comprado_precio.setFont(font)
        self.comprado_precio.setMaximum(1e+35)
        self.comprado_precio.setObjectName("comprado_precio")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comprado_precio)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comprado_vendedor = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comprado_vendedor.setFont(font)
        self.comprado_vendedor.setObjectName("comprado_vendedor")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comprado_vendedor)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.comprado_fecha = QtWidgets.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comprado_fecha.setFont(font)
        self.comprado_fecha.setCalendarPopup(True)
        self.comprado_fecha.setTimeSpec(QtCore.Qt.TimeZone)
        self.comprado_fecha.setDate(QtCore.QDate(1800, 1, 1))
        self.comprado_fecha.setObjectName("comprado_fecha")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comprado_fecha)
        self.verticalLayout.addWidget(self.frame)
        self.procedencia_uis.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.page_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.cual_otro_procedencia = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cual_otro_procedencia.setFont(font)
        self.cual_otro_procedencia.setObjectName("cual_otro_procedencia")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cual_otro_procedencia)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.notas_otro_procedencia = QtWidgets.QTextEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.notas_otro_procedencia.setFont(font)
        self.notas_otro_procedencia.setObjectName("notas_otro_procedencia")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.notas_otro_procedencia)
        self.procedencia_uis.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.procedencia_uis)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vendida = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vendida.setFont(font)
        self.vendida.setCheckable(True)
        self.vendida.setChecked(False)
        self.vendida.setObjectName("vendida")
        self.horizontalLayout_2.addWidget(self.vendida)
        self.muerta = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.muerta.setFont(font)
        self.muerta.setChecked(False)
        self.muerta.setObjectName("muerta")
        self.horizontalLayout_2.addWidget(self.muerta)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.final_uis = QtWidgets.QStackedWidget(self.groupBox_3)
        self.final_uis.setEnabled(False)
        self.final_uis.setObjectName("final_uis")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.page_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.muerta_causa = QtWidgets.QLineEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.muerta_causa.setFont(font)
        self.muerta_causa.setObjectName("muerta_causa")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.muerta_causa)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.muerta_fecha = QtWidgets.QDateEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.muerta_fecha.setFont(font)
        self.muerta_fecha.setCalendarPopup(True)
        self.muerta_fecha.setTimeSpec(QtCore.Qt.TimeZone)
        self.muerta_fecha.setDate(QtCore.QDate(1800, 1, 1))
        self.muerta_fecha.setObjectName("muerta_fecha")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.muerta_fecha)
        self.final_uis.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.page_4)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.vendida_comprador = QtWidgets.QLineEdit(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vendida_comprador.setFont(font)
        self.vendida_comprador.setObjectName("vendida_comprador")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vendida_comprador)
        self.label_20 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.vendida_precio = QtWidgets.QDoubleSpinBox(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vendida_precio.setFont(font)
        self.vendida_precio.setMaximum(1e+49)
        self.vendida_precio.setObjectName("vendida_precio")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vendida_precio)
        self.label_21 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.vendida_fecha = QtWidgets.QDateEdit(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vendida_fecha.setFont(font)
        self.vendida_fecha.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.vendida_fecha.setCalendarPopup(True)
        self.vendida_fecha.setTimeSpec(QtCore.Qt.TimeZone)
        self.vendida_fecha.setDate(QtCore.QDate(1800, 1, 1))
        self.vendida_fecha.setObjectName("vendida_fecha")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.vendida_fecha)
        self.final_uis.addWidget(self.page_4)
        self.verticalLayout_3.addWidget(self.final_uis)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.tabWidget_4 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_4.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_4.setMovable(True)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tabWidget_4Page1 = QtWidgets.QWidget()
        self.tabWidget_4Page1.setObjectName("tabWidget_4Page1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabWidget_4Page1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.tabWidget_4Page1)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.tabWidget_4Page1)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.marcar_vacunado_c_b_c1 = QtWidgets.QPushButton(self.frame_7)
        self.marcar_vacunado_c_b_c1.setObjectName("marcar_vacunado_c_b_c1")
        self.horizontalLayout_6.addWidget(self.marcar_vacunado_c_b_c1)
        self.marcar_vacunado_c_b_c2 = QtWidgets.QPushButton(self.frame_7)
        self.marcar_vacunado_c_b_c2.setObjectName("marcar_vacunado_c_b_c2")
        self.horizontalLayout_6.addWidget(self.marcar_vacunado_c_b_c2)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_12 = QtWidgets.QFrame(self.tabWidget_4Page1)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.desmarcar_vacunado_c_b_c1 = QtWidgets.QPushButton(self.frame_12)
        self.desmarcar_vacunado_c_b_c1.setObjectName("desmarcar_vacunado_c_b_c1")
        self.horizontalLayout_11.addWidget(self.desmarcar_vacunado_c_b_c1)
        self.desmarcar_vacunado_c_b_c2 = QtWidgets.QPushButton(self.frame_12)
        self.desmarcar_vacunado_c_b_c2.setObjectName("desmarcar_vacunado_c_b_c2")
        self.horizontalLayout_11.addWidget(self.desmarcar_vacunado_c_b_c2)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_5 = QtWidgets.QFrame(self.tabWidget_4Page1)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vacunas_ciclo1_c_b = QtWidgets.QListWidget(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vacunas_ciclo1_c_b.setFont(font)
        self.vacunas_ciclo1_c_b.setObjectName("vacunas_ciclo1_c_b")
        self.horizontalLayout_5.addWidget(self.vacunas_ciclo1_c_b)
        self.vacunas_ciclo2_c_b = QtWidgets.QListWidget(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vacunas_ciclo2_c_b.setFont(font)
        self.vacunas_ciclo2_c_b.setObjectName("vacunas_ciclo2_c_b")
        self.horizontalLayout_5.addWidget(self.vacunas_ciclo2_c_b)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.tabWidget_4.addTab(self.tabWidget_4Page1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.tab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.marcar_vacunado_aftosa_c1 = QtWidgets.QPushButton(self.frame_8)
        self.marcar_vacunado_aftosa_c1.setObjectName("marcar_vacunado_aftosa_c1")
        self.horizontalLayout_7.addWidget(self.marcar_vacunado_aftosa_c1)
        self.marcar_vacunado_aftosa_c2 = QtWidgets.QPushButton(self.frame_8)
        self.marcar_vacunado_aftosa_c2.setObjectName("marcar_vacunado_aftosa_c2")
        self.horizontalLayout_7.addWidget(self.marcar_vacunado_aftosa_c2)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.tab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.desmarcar_vacunado_aftosa_c1 = QtWidgets.QPushButton(self.frame_11)
        self.desmarcar_vacunado_aftosa_c1.setObjectName("desmarcar_vacunado_aftosa_c1")
        self.horizontalLayout_10.addWidget(self.desmarcar_vacunado_aftosa_c1)
        self.desmarcar_vacunado_aftosa_c2 = QtWidgets.QPushButton(self.frame_11)
        self.desmarcar_vacunado_aftosa_c2.setObjectName("desmarcar_vacunado_aftosa_c2")
        self.horizontalLayout_10.addWidget(self.desmarcar_vacunado_aftosa_c2)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_9 = QtWidgets.QFrame(self.tab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.vacunas_ciclo1_aftosa = QtWidgets.QListWidget(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vacunas_ciclo1_aftosa.setFont(font)
        self.vacunas_ciclo1_aftosa.setObjectName("vacunas_ciclo1_aftosa")
        self.horizontalLayout_8.addWidget(self.vacunas_ciclo1_aftosa)
        self.vacunas_ciclo2_aftosa = QtWidgets.QListWidget(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vacunas_ciclo2_aftosa.setFont(font)
        self.vacunas_ciclo2_aftosa.setObjectName("vacunas_ciclo2_aftosa")
        self.horizontalLayout_8.addWidget(self.vacunas_ciclo2_aftosa)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.tabWidget_4.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_4)
        self.buttons_dlg = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons_dlg.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_dlg.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_dlg.setObjectName("buttons_dlg")
        self.verticalLayout_4.addWidget(self.buttons_dlg)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)

        self.retranslateUi(Dialog)
        self.procedencia_uis.setCurrentIndex(0)
        self.final_uis.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.buttons_dlg.accepted.connect(Dialog.accept) # type: ignore
        self.buttons_dlg.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Formulario"))
        self.groupBox.setTitle(_translate("Dialog", "Información de la res"))
        self.label.setText(_translate("Dialog", "Número"))
        self.label_2.setText(_translate("Dialog", "Fecha Nacimiento"))
        self.fdn.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy"))
        self.label_3.setText(_translate("Dialog", "Marca"))
        self.label_5.setText(_translate("Dialog", "Sexo"))
        self.sexo.setItemText(0, _translate("Dialog", "Macho"))
        self.sexo.setItemText(1, _translate("Dialog", "Hembra"))
        self.label_6.setText(_translate("Dialog", "Dueño"))
        self.label_7.setText(_translate("Dialog", "Mama"))
        self.label_8.setText(_translate("Dialog", "Descripción"))
        self.groupBox_2.setTitle(_translate("Dialog", "Procedencia"))
        self.criadero.setText(_translate("Dialog", "Criadero"))
        self.comprado.setText(_translate("Dialog", "Comprado"))
        self.otro_procedencia.setText(_translate("Dialog", "Otro"))
        self.label_4.setText(_translate("Dialog", "Precio Compra"))
        self.comprado_precio.setPrefix(_translate("Dialog", "$"))
        self.label_9.setText(_translate("Dialog", "Vendedor"))
        self.label_14.setText(_translate("Dialog", "Fecha"))
        self.comprado_fecha.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy"))
        self.label_10.setText(_translate("Dialog", "Cual"))
        self.label_11.setText(_translate("Dialog", "Notas"))
        self.groupBox_3.setTitle(_translate("Dialog", "Final"))
        self.vendida.setText(_translate("Dialog", "Vendida"))
        self.muerta.setText(_translate("Dialog", "Muerta"))
        self.label_12.setText(_translate("Dialog", "Causa"))
        self.label_13.setText(_translate("Dialog", "Fecha"))
        self.muerta_fecha.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy"))
        self.label_19.setText(_translate("Dialog", "Comprador"))
        self.label_20.setText(_translate("Dialog", "Precio"))
        self.vendida_precio.setPrefix(_translate("Dialog", "$"))
        self.label_21.setText(_translate("Dialog", "Fecha"))
        self.vendida_fecha.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy"))
        self.label_15.setText(_translate("Dialog", "Ciclo 1:"))
        self.label_16.setText(_translate("Dialog", "Ciclo 2:"))
        self.marcar_vacunado_c_b_c1.setText(_translate("Dialog", "Marcar vacunado"))
        self.marcar_vacunado_c_b_c2.setText(_translate("Dialog", "Marcar Vacunado"))
        self.desmarcar_vacunado_c_b_c1.setText(_translate("Dialog", "Borrar"))
        self.desmarcar_vacunado_c_b_c2.setText(_translate("Dialog", "Borrar"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tabWidget_4Page1), _translate("Dialog", "Carbon y Botulismo"))
        self.label_17.setText(_translate("Dialog", "Ciclo 1:"))
        self.label_18.setText(_translate("Dialog", "Ciclo 2:"))
        self.marcar_vacunado_aftosa_c1.setText(_translate("Dialog", "Marcar vacunado"))
        self.marcar_vacunado_aftosa_c2.setText(_translate("Dialog", "Marcar Vacunado"))
        self.desmarcar_vacunado_aftosa_c1.setText(_translate("Dialog", "Borrar"))
        self.desmarcar_vacunado_aftosa_c2.setText(_translate("Dialog", "Borrar"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab), _translate("Dialog", "Aftosa"))
