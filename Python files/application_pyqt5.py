from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont
import sys
from applicationUI import Ui_MainWindow
from Turkey_cities import sehirListesi, sehirilce
import socket
from db_Connection import dbConnection, dbCursor
import time
from unicode_tr.extras import slugify   ## pip install unicode_tr
from bs4 import BeautifulSoup
import requests


class Window(QtWidgets.QMainWindow):    
    
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.dbConnection = dbConnection
        self.dbCursor = dbCursor
        
        self.ui.btnLoad.clicked.connect(self.LoadItems)
        self.ui.btnGetItemSehir.clicked.connect(self.GetItemSehir)
        self.ui.btnClear.clicked.connect(self.Clear)
        self.ui.btnClear2.clicked.connect(self.Clear2)
        self.ui.btnClear2_2.clicked.connect(self.Clear3)
        self.ui.getAllLogs.clicked.connect(self.getAllLogs)
        self.ui.get10Logs.clicked.connect(self.getLast10Logs)
        self.ui.btnGetItemilce.clicked.connect(self.SearchLogs)
        self.ui.btnClear.setEnabled(False)
        self.ui.btnGetSelectedLogs.clicked.connect(self.ShowLogs2)
        self.ui.btnGetSelectedLogsSehir.clicked.connect(self.ShowLogs1)
        self.ui.btnEnglish.clicked.connect(self.English)
        self.ui.btnTurkish.clicked.connect(self.Turkish)
    def LoadItems(self):
        self.ui.btnLoad.setEnabled(False)
        self.ui.btnGetItemSehir.setEnabled(True)
        self.ui.btnGetSelectedLogsSehir.setEnabled(True)
        self.sehirListesi = sehirListesi
        self.ui.cbSehir.setEnabled(True)
        self.ui.cbSehir.addItems(self.sehirListesi)
        self.ui.btnClear.setEnabled(True)

    def GetItemSehir(self):
        self.ui.btnClear2_2.setEnabled(True)
        self.ui.btnGetSelectedLogsSehir.setEnabled(True)
        current_idx = self.ui.cbSehir.currentIndex() +1
        self.ui.cbilce.setEnabled(True)
        self.ui.btnGetItemSehir.setEnabled(False)
        self.ui.cbSehir.setEnabled(False)
        self.ui.btnGetSelectedLogs.setEnabled(True)
        self.ui.btnClear2.setEnabled(True)

        ilceler = []
        for i in range(0,len(sehirilce[f"{current_idx}"])):
                ilceler.append(sehirilce[f"{current_idx}"][i])

        self.ui.cbilce.addItems(ilceler)
        self.ui.btnGetItemilce.setEnabled(True)
                  
    def SearchLogs(self):
        try:
            try:
                current_ilce_text = slugify(self.ui.cbilce.currentText())
                current_sehir_text = slugify(self.ui.cbSehir.currentText())
                current_ilce_text_log = self.ui.cbilce.currentText()
                self.ui.btnGetItemilce.setEnabled(False)
                self.ui.cbilce.setEnabled(False)            
                self.ui.btnLoad.setEnabled(False)
                
                url = f"https://www.trnobetcieczane.com/ilce/{current_sehir_text}-{current_ilce_text}-nobetci-eczaneler/"    
                html = requests.get(url).content
                soup = BeautifulSoup(html , "html.parser")
                logs = soup.find("div", {"class":"citysingle"}).find_all("li")

                logsName = []
                for i in logs:
                    logsName.append(i.find("div",{"class":"eczanelistcontent"}).find("a").text)

                logsAdress = []
                for i in logs:
                    logsAdress.append((i.find("div",{"class":"eczanelistcontent"}).find("div").text).lstrip("Adres").upper().lstrip(" "))

                logsTel = []
                for i in logs:
                    logsTel.append((i.find("div",{"class":"eczanephone"}).find("a").text).lstrip("0 "))


                logsLocLinks = []
                for i in logs:
                    logsLocLinks.append(i.find("div",{"class":"eczanelistcontent"}).find("a",{"class":"maps-link"}).get("href"))

                logsLocLinks
                LogsLocHref = []
                for i in range(0,len(logsLocLinks)):
                    urlLoc = f"https://www.trnobetcieczane.com/{logsLocLinks[i]}"    
                    htmlLoc = requests.get(urlLoc).content
                    soupLoc = BeautifulSoup(htmlLoc , "html.parser")
                    LogsLocHref.append(soupLoc.find("a", {"class":"gbutton"}))

                logsLoc = []
                for i in range(0,len(LogsLocHref)):
                    logsLoc.append(str(LogsLocHref[i]["href"]).lstrip("https://www.google.com/maps?q="))
                    
                tm = time.localtime()
                timenow = f"{tm[2]}.{tm[1]}.{tm[0]}"
                if len(logs) >= 1:
                    self.ui.tableWidget.setRowCount(len(logs))                             
                    self.ui.tableWidget.setColumnCount(6)
                    if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                        self.ui.tableWidget.setHorizontalHeaderLabels(('Eczane Adı','Eczane İlçesi','Eczane Telefonu','Eczane Adresi','Eczane Konumu','Tarih')) 
                    else:
                        self.ui.tableWidget.setHorizontalHeaderLabels(('Pharmacy Name','District','Phone Number','Address','Location','Date')) 

                    for i in range(0,len(logs)):
                        self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(logsName[i]))
                        self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(current_ilce_text_log))
                        self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(logsTel[i]))
                        self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(logsAdress[i]))
                        self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(logsLoc[i]))
                        self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(timenow)))
                    

                    self.SaveLogs(logs = logs, timenow = timenow, logsName = logsName, logsAdress = logsAdress, logsTel = logsTel, logsLoc = logsLoc)
                
                else:        
                    print(self.ui.btnGetItemilce.text())
                    if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                        message4 = QMessageBox()
                        message4.setWindowTitle("Uyarı! Bu İlçe için Bugün için Girilmiş Bir Kayıt Yok")
                        message4.setIcon(QMessageBox.Information)
                        message4.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message4.setText("Maalesef Şu anda Bu Bölge İçin Nöbetçi Eczane Kayıtlarına Ulaşılamıyor, \nLütfen Daha Merkezii Bir Yer Seçiniz ya da Bir Süre sonra Tekrar Deneyiniz")    
                        message4.exec_()
                    else:
                        message4EN = QMessageBox()
                        message4EN.setWindowTitle("Attention! There aren't any Logs Today for this District")
                        message4EN.setIcon(QMessageBox.Information)
                        message4EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message4EN.setText("Unfortunately, Pharmacy On Duty Logs are not Available for This District at The Moment, \nPlease Choose More Central Location or Try Again Later")    
                        message4EN.exec_()

            except requests.exceptions.ConnectionError:
                if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                    messageInt1  = QMessageBox()
                    messageInt1.setWindowTitle("Uyarı! İnternete Erişiminiz Yok")
                    messageInt1.setIcon(QMessageBox.Information)
                    messageInt1.setWindowIcon(QtGui.QIcon("eczane.png"))
                    messageInt1.setText("Maalesef Şu anda İnternete Erişilemiyor. Lütfen Bağlantı Ayarlarınızı Kontrol Ediniz")    
                    messageInt1.exec_()            
                else:
                    messageInt1EN = QMessageBox()
                    messageInt1EN.setWindowTitle("Warning! Connection Error")
                    messageInt1EN.setIcon(QMessageBox.Information)
                    messageInt1EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                    messageInt1EN.setText("Internet Connection is Unavailable at the moment. Please Check Your Connection Settings")    
                    messageInt1EN.exec_()    

        except socket.gaierror:            
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                messageInt  = QMessageBox()
                messageInt.setWindowTitle("Uyarı! İnternete Erişiminiz Yok")
                messageInt.setIcon(QMessageBox.Information)
                messageInt.setWindowIcon(QtGui.QIcon("eczane.png"))
                messageInt.setText("Maalesef Şu anda İnternete Erişilemiyor. Lütfen Bağlantı Ayarlarınızı Kontrol Ediniz")    
                messageInt.exec_()            
            else:
                messageIntEN = QMessageBox()
                messageIntEN.setWindowTitle("Warning! Connection Error")
                messageIntEN.setIcon(QMessageBox.Information)
                messageIntEN.setWindowIcon(QtGui.QIcon("eczane.png"))
                messageIntEN.setText("Internet Connection is Unavailable at the moment. Please Check Your Connection Settings")    
                messageIntEN.exec_()    

    
    def SaveLogs(self, logs, timenow, logsName, logsAdress, logsTel, logsLoc):
        current_ilce_text = self.ui.cbilce.currentText()
        current_sehir_text = self.ui.cbSehir.currentText()
        current_ilce_id = self.ui.cbilce.currentIndex() + 1
        current_sehir_id = self.ui.cbSehir.currentIndex() + 1
        
        qm1 = QMessageBox()
        qm1.setIcon(QMessageBox.Question)
        qm1.setWindowIcon(QtGui.QIcon("eczane.png"))
        if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
            q = qm1.question(self,'Arama Başarılı',"Sonuçlar Veritabanına Kaydedilsin mi?", qm1.Yes | qm1.No) 
        else:
            q = qm1.question(self,'Search Succesful',"Save Results to Database?", qm1.Yes | qm1.No)
        
        if q == qm1.Yes:       
            self.dbConnection = dbConnection   
            self.dbCursor = dbCursor
            sql_kayit_kontrol = f"""
            SELECT kayit_tarihi, ilce_id, sehir_id from eczane where sehir_id = {current_sehir_id} AND ilce_id = {current_ilce_id} ORDER BY id DESC
            """
            self.dbCursor.execute(sql_kayit_kontrol)
            tarih = self.dbCursor.fetchone()
            
            try:
                if str(tarih[0]) == str(timenow):
                    if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                        message5 = QMessageBox() 
                        message5.setWindowTitle("Uyarı! Bu Kayıt Zaten Mevcut")
                        message5.setText(f"{timenow} Tarihi için {current_ilce_text} ilçesine ait kayıtlar Zaten Mevcut!")    
                        message5.exec_()  
                    else:
                        message5EN = QMessageBox() 
                        message5EN.setWindowTitle("Attention! This Log is Already Exist")
                        message5EN.setText(f"For the {timenow} date, there is a log already created for {current_ilce_text} district!")    
                        message5EN.exec_()  
                else:
                    sql = """
                    INSERT INTO eczane(sehir_id, ilce_id, eczane_ismi, eczane_adresi, eczane_telefonu, eczane_konumu, kayit_tarihi) VALUES (?,?,?,?,?,?,?);
                    """
                    sql2 = """
                    INSERT INTO ilce(sehir_id, ilce_id, ilce_ismi) VALUES (?,?,?);
                    """
                    sql3 = """
                    INSERT INTO sehir(sehir_id, sehir_ismi) VALUES (?,?);
                    """

                    for i in range(0,len(logs)):
                        values2 = [(current_sehir_id, current_ilce_id, sehirilce[str(current_sehir_id)][current_ilce_id-1])]
                        values3 = [(current_sehir_id, current_sehir_text)]

                        values1 = [(current_sehir_id, current_ilce_id, logsName[i], logsAdress[i], logsTel[i] ,logsLoc[i],str(timenow))] 

                        self.dbCursor.executemany(sql, values1)
                        self.dbConnection.commit()

                        self.dbCursor.execute(f"SELECT ilce_id,sehir_id FROM ilce WHERE ilce_id = {current_ilce_id} and sehir_id = {current_sehir_id}")
                        result1 = dbCursor.fetchone() 
                        self.dbCursor.execute("select count(ilce_id) from ilce")
                        a = dbCursor.fetchone()
                        if a[0] == 0:
                            self.dbCursor.executemany(sql2, values2)
                            self.dbConnection.commit()
                        elif result1 == None:
                            self.dbCursor.executemany(sql2, values2)
                            self.dbConnection.commit()
                        elif int(result1[0]) == current_ilce_id:
                            continue
                        else:
                            self.dbCursor.executemany(sql2, values2)
                            self.dbConnection.commit()
                        
                        self.dbCursor.execute(f"SELECT sehir_id FROM sehir WHERE sehir_id = {int(current_sehir_id)}")
                        result2 = dbCursor.fetchone()
                        self.dbCursor.execute("select count(sehir_id) from sehir")
                        b = dbCursor.fetchone()
                        if b[0] == 0:
                            self.dbCursor.executemany(sql3, values3)
                            self.dbConnection.commit()
                        elif result2 == None:
                            self.dbCursor.executemany(sql3, values3)
                            self.dbConnection.commit()
                        elif int(result2[0]) == current_sehir_id:
                            continue
                        else:
                            self.dbCursor.executemany(sql3, values3)
                            self.dbConnection.commit()
                    
                    if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                        message6 = QMessageBox()
                        message6.setWindowTitle("Kayıt Başarılı")
                        message6.setText("Sonuçlar Veritabanına Başarıyla Kaydedildi!")
                        message6.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message6.setIcon(QMessageBox.Information)
                        message6.exec_()
                    else:
                        message6EN = QMessageBox()
                        message6EN.setWindowTitle("Registration Successful")
                        message6EN.setText("Results are saved to Database Successfully!")
                        message6EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message6EN.setIcon(QMessageBox.Information)
                        message6EN.exec_()

            except TypeError:  
                sql = """
                INSERT INTO eczane(sehir_id, ilce_id, eczane_ismi, eczane_adresi, eczane_telefonu, eczane_konumu, kayit_tarihi) VALUES (?,?,?,?,?,?,?);
                """
                sql2 = """
                INSERT INTO ilce(sehir_id, ilce_id, ilce_ismi) VALUES (?,?,?);
                """
                sql3 = """
                INSERT INTO sehir(sehir_id, sehir_ismi) VALUES (?,?);
                """
                for i in range(0,len(logs)):
                    values2 = [(current_sehir_id, current_ilce_id, sehirilce[str(current_sehir_id)][current_ilce_id-1])]
                    values3 = [(current_sehir_id, current_sehir_text)]

                    values1 = [(current_sehir_id, current_ilce_id, logsName[i], logsAdress[i], logsTel[i] ,logsLoc[i],str(timenow))] 

                    self.dbCursor.executemany(sql, values1)
                    self.dbConnection.commit()

                    self.dbCursor.execute(f"SELECT ilce_id,sehir_id FROM ilce WHERE ilce_id = {current_ilce_id} and sehir_id = {current_sehir_id}")
                    result1 = dbCursor.fetchone() 
                    self.dbCursor.execute("select count(ilce_id) from ilce")
                    a = dbCursor.fetchone()
                    if a[0] == 0:
                        self.dbCursor.executemany(sql2, values2)
                        self.dbConnection.commit()
                    elif result1 == None:
                        self.dbCursor.executemany(sql2, values2)
                        self.dbConnection.commit()
                    elif int(result1[0]) == current_ilce_id:
                        continue
                    else:
                        self.dbCursor.executemany(sql2, values2)
                        self.dbConnection.commit()
                    
                    self.dbCursor.execute(f"SELECT sehir_id FROM sehir WHERE sehir_id = {int(current_sehir_id)}")
                    result2 = dbCursor.fetchone()
                    self.dbCursor.execute("select count(sehir_id) from sehir")
                    b = dbCursor.fetchone()
                    if b[0] == 0:
                        self.dbCursor.executemany(sql3, values3)
                        self.dbConnection.commit()
                    elif result2 == None:
                        self.dbCursor.executemany(sql3, values3)
                        self.dbConnection.commit()
                    elif int(result2[0]) == current_sehir_id:
                        continue
                    else:
                        self.dbCursor.executemany(sql3, values3)
                        self.dbConnection.commit()

                if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                        message7 = QMessageBox()
                        message7.setWindowTitle("Kayıt Başarılı")
                        message7.setText("Sonuçlar Veritabanına Başarıyla Kaydedildi!")
                        message7.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message7.setIcon(QMessageBox.Information)
                        message7.exec_()
                else:
                        message7EN = QMessageBox()
                        message7EN.setWindowTitle("Registration Successful")
                        message7EN.setText("Results are saved to Database Successfully!")
                        message7EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                        message7EN.setIcon(QMessageBox.Information)
                        message7EN.exec_()
        
        elif q == qm1.No:
            pass

    def getAllLogs(self):
        sql4 = """select sehir.sehir_ismi,ilce.ilce_ismi, eczane.eczane_ismi, eczane.eczane_adresi, eczane.eczane_telefonu, eczane.eczane_konumu, eczane.kayit_tarihi 
        from eczane
        INNER JOIN sehir ON eczane.sehir_id = sehir.sehir_id
        INNER JOIN ilce ON eczane.ilce_id = ilce.ilce_id
        WHERE sehir.sehir_id = ilce.sehir_id
        ORDER BY eczane.id DESC;
        """
        self.dbConnection
        self.dbCursor

        self.dbCursor.execute(sql4)
        tablo = self.dbCursor.fetchall()
        
        if len(tablo) <= 0:        
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                message1 = QMessageBox()
                message1.setWindowTitle("Bilgilendirme!")
                message1.setIcon(QMessageBox.Information)
                message1.setWindowIcon(QtGui.QIcon("eczane.png"))
                message1.setText("Henüz Herhangi Bir Veritabanı Kaydı Oluşturmadınız!")    
                message1.exec_()
            else:
                message1EN = QMessageBox()
                message1EN.setWindowTitle("Info!")
                message1EN.setIcon(QMessageBox.Information)
                message1EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                message1EN.setText("You Haven't Created Any Database Logs Yet!")    
                message1EN.exec_()

        self.ui.tableWidget.setRowCount(len(tablo))                             
        self.ui.tableWidget.setColumnCount(7)
        if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
            self.ui.tableWidget.setHorizontalHeaderLabels(('Şehir','Eczane İlçesi','Eczane Adı','Eczane Adresi','Eczane Telefonu','Eczane Konumu','Tarih')) 
        else:
            self.ui.tableWidget.setHorizontalHeaderLabels(('City','District','Pharmacy Name','Address','Phone Number','Location','Date')) 


        for i in range(0, len(tablo)):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(tablo[i][0])))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(tablo[i][1])))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(tablo[i][2])))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(tablo[i][3])))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(tablo[i][4])))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(tablo[i][5])))
            self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(tablo[i][6])))


    def getLast10Logs(self):
        sql7 = """select sehir.sehir_ismi,ilce.ilce_ismi, eczane.eczane_ismi, eczane.eczane_adresi, eczane.eczane_telefonu, eczane.eczane_konumu, eczane.kayit_tarihi 
                from eczane
                INNER JOIN sehir ON eczane.sehir_id = sehir.sehir_id
                INNER JOIN ilce ON eczane.ilce_id = ilce.ilce_id
                WHERE sehir.sehir_id = ilce.sehir_id
                ORDER BY eczane.id DESC LIMIT 10;
                """
        self.dbConnection
        self.dbCursor

        self.dbCursor.execute(sql7)
        tablo1 = self.dbCursor.fetchall()

        if len(tablo1) <= 0: 
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                message = QMessageBox()
                message.setWindowTitle("Bilgilendirme!")
                message.setIcon(QMessageBox.Information)
                message.setWindowIcon(QtGui.QIcon("eczane.png"))
                message.setText("Henüz Herhangi Bir Veritabanı Kaydı Oluşturmadınız!")    
                message.exec_()
            else:
                messageEN = QMessageBox()
                messageEN.setWindowTitle("Info!")
                messageEN.setIcon(QMessageBox.Information)
                messageEN.setWindowIcon(QtGui.QIcon("eczane.png"))
                messageEN.setText("You Haven't Created Any Database Logs Yet!")    
                messageEN.exec_()
        else:
            self.ui.tableWidget.setRowCount(len(tablo1))                             
            self.ui.tableWidget.setColumnCount(7)
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                self.ui.tableWidget.setHorizontalHeaderLabels(('Şehir','Eczane İlçesi','Eczane Adı','Eczane Adresi','Eczane Telefonu','Eczane Konumu','Tarih')) 
            else:
                self.ui.tableWidget.setHorizontalHeaderLabels(('City','District','Pharmacy Name','Address','Phone Number','Location','Date')) 

            for i in range(0, len(tablo1)):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(tablo1[i][0])))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(tablo1[i][1])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(tablo1[i][2])))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(tablo1[i][3])))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(tablo1[i][4])))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(tablo1[i][5])))
                self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(tablo1[i][6])))


    def ShowLogs1(self):
        current_sehir_text = self.ui.cbSehir.currentText()

        sql9 = f"""Select sehir.sehir_ismi,ilce.ilce_ismi, eczane.eczane_ismi, eczane.eczane_adresi, eczane.eczane_telefonu, eczane.eczane_konumu, eczane.kayit_tarihi
        from eczane
        INNER JOIN sehir ON eczane.sehir_id = sehir.sehir_id
        INNER JOIN ilce ON eczane.ilce_id = ilce.ilce_id        
        WHERE sehir.sehir_ismi = "{current_sehir_text}" and sehir.sehir_id = ilce.sehir_id
        ORDER BY eczane.id DESC;
        """

        self.dbConnection
        self.dbCursor

        self.dbCursor.execute(sql9)
        tablo2 = self.dbCursor.fetchall()
        
        if len(tablo2) <= 0:
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                message2 = QMessageBox()
                message2.setWindowTitle("Bilgilendirme!")
                message2.setIcon(QMessageBox.Information)
                message2.setWindowIcon(QtGui.QIcon("eczane.png"))
                message2.setText("Bu Şehir için Henüz Bir Veritabanı Kaydı Oluşturmadınız!")    
                message2.exec_()
            else:
                message2EN = QMessageBox()
                message2EN.setWindowTitle("Info!")
                message2EN.setIcon(QMessageBox.Information)
                message2EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                message2EN.setText("For the Selected City, You Haven't Created Any Database Logs Yet!")    
                message2EN.exec_()
        
        else:
            self.ui.tableWidget.setRowCount(len(tablo2))                             
            self.ui.tableWidget.setColumnCount(7)
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                self.ui.tableWidget.setHorizontalHeaderLabels(('Şehir','Eczane İlçesi','Eczane Adı','Eczane Adresi','Eczane Telefonu','Eczane Konumu','Tarih')) 
            else:
                self.ui.tableWidget.setHorizontalHeaderLabels(('City','District','Pharmacy Name','Address','Phone Number','Location','Date')) 

            for i in range(0, len(tablo2)):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(tablo2[i][0])))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(tablo2[i][1])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(tablo2[i][2])))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(tablo2[i][3])))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(tablo2[i][4])))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(tablo2[i][5])))
                self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(tablo2[i][6])))

    def ShowLogs2(self):
        current_ilce_text = self.ui.cbilce.currentText()
        current_sehir_id = self.ui.cbSehir.currentIndex() + 1
        sql10 = f"""Select sehir.sehir_ismi,ilce.ilce_ismi, eczane.eczane_ismi, eczane.eczane_adresi, eczane.eczane_telefonu, eczane.eczane_konumu, eczane.kayit_tarihi
        from eczane
        INNER JOIN sehir ON eczane.sehir_id = sehir.sehir_id
        INNER JOIN ilce ON eczane.ilce_id = ilce.ilce_id        
        WHERE sehir.sehir_id = ilce.sehir_id AND ilce.ilce_ismi = "{current_ilce_text}" AND sehir.sehir_id = {current_sehir_id}
        ORDER BY eczane.id DESC;
        """

        self.dbConnection
        self.dbCursor

        self.dbCursor.execute(sql10)
        tablo3 = self.dbCursor.fetchall()

        if len(tablo3) <= 0:
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                message3 = QMessageBox()
                message3.setWindowTitle("Bilgilendirme!")
                message3.setIcon(QMessageBox.Information)
                message3.setWindowIcon(QtGui.QIcon("eczane.png"))
                message3.setText("Bu İlçe için Henüz Bir Veritabanı Kaydı Oluşturmadınız!")    
                message3.exec_()
            else:
                message3EN = QMessageBox()
                message3EN.setWindowTitle("Info!")
                message3EN.setIcon(QMessageBox.Information)
                message3EN.setWindowIcon(QtGui.QIcon("eczane.png"))
                message3EN.setText("For the Selected District, You Haven't Created Any Database Logs Yet!")    
                message3EN.exec_()

        else:
            self.ui.tableWidget.setRowCount(len(tablo3))                             
            self.ui.tableWidget.setColumnCount(7)
            if self.ui.btnGetItemilce.text() == "Nöbetçi Eczane Ara":
                self.ui.tableWidget.setHorizontalHeaderLabels(('Şehir','Eczane İlçesi','Eczane Adı','Eczane Adresi','Eczane Telefonu','Eczane Konumu','Tarih')) 
            else:
                self.ui.tableWidget.setHorizontalHeaderLabels(('City','District','Pharmacy Name','Address','Phone Number','Location','Date')) 

            for i in range(0, len(tablo3)):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(tablo3[i][0])))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(tablo3[i][1])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(tablo3[i][2])))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(tablo3[i][3])))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(tablo3[i][4])))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(tablo3[i][5])))
                self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(tablo3[i][6])))

    def English(self):
        self.ui.btnEnglish.setEnabled(False)
        self.ui.btnTurkish.setEnabled(True)
        self.ui.btnClear.setText("Clear the Page")
        self.ui.btnClear2.setText("Choose Again")
        self.ui.btnClear2_2.setText("Choose Again")
        self.ui.btnGetItemilce.setText("Search Pharmacy on Duty")
        self.ui.btnGetItemSehir.setText("Confirm City Selection")
        self.ui.btnGetSelectedLogsSehir.setText("Get All Logs by Choosen City From Database")
        self.ui.btnGetSelectedLogs.setText("Get All Logs by Choosen District From Database")
        self.ui.lblIlce.setText("Please Choose any District:")
        self.ui.lblIlce.setGeometry(0,20,130,21)
        self.ui.lblIlce.setFont(QFont('MS Shell Dlg 2',8))
        self.ui.lblSehir.setText("Please Choose any City:")
        self.ui.lblSehir.setGeometry(5,30,120,21)
        self.ui.lblSehir.setFont(QFont('MS Shell Dlg 2',8))
        self.ui.get10Logs.setText("Get Last 10 Logs Added")
        self.ui.getAllLogs.setText("Get All Logs Added")
        self.ui.btnLoad.setText("--Load Cities--")    
    def Turkish(self):
        self.ui.btnEnglish.setEnabled(True)
        self.ui.btnTurkish.setEnabled(False)
        self.ui.btnClear.setText("Sayfayı Yenile")
        self.ui.btnClear2.setText("Yeniden Seç")
        self.ui.btnClear2_2.setText("Yeniden Seç")
        self.ui.btnGetItemilce.setText("Nöbetçi Eczane Ara")
        self.ui.btnGetItemSehir.setText("Seçimi Onayla")
        self.ui.btnGetSelectedLogsSehir.setText("Veritabanından Seçili Şehirdeki Nöbetçi Eczane Kayıtlarını Getir")
        self.ui.btnGetSelectedLogs.setText("Veritabanından Seçili İlçedeki Nöbetçi Eczane Kayıtlarını Getir")        
        self.ui.lblIlce.setText("İlçe Seçiniz:")
        self.ui.lblIlce.setGeometry(20,20,101,21)
        self.ui.lblIlce.setFont(QFont('MS Shell Dlg 2',12))
        self.ui.lblSehir.setText("Şehir Seçiniz:")
        self.ui.lblSehir.setGeometry(10,30,101,21)
        self.ui.lblSehir.setFont(QFont('MS Shell Dlg 2',12))
        self.ui.get10Logs.setText("Son 10 Kaydı Göster")
        self.ui.getAllLogs.setText("Tüm Veritabanı Kayıtlarını Göster ")
        self.ui.btnLoad.setText("--Şehirleri Yükle--")
    def Clear(self):
        self.ui.cbilce.clear()
        self.ui.cbilce.setEnabled(False)
        self.ui.tableWidget.clear()
        self.ui.btnLoad.setEnabled(False)
        self.ui.btnGetItemSehir.setEnabled(True)
        self.ui.cbSehir.setEnabled(True)
        self.ui.btnGetSelectedLogs.setEnabled(False)
        self.ui.btnGetItemilce.setEnabled(False)
        self.ui.get10Logs.setEnabled(True)
        self.ui.getAllLogs.setEnabled(True)
        self.ui.btnClear2.setEnabled(False)
        self.ui.btnClear2_2.setEnabled(False)
        self.ui.btnGetSelectedLogsSehir.setEnabled(True)

    def Clear2(self):
        self.ui.btnLoad.setEnabled(False)
        self.ui.btnGetItemSehir.setEnabled(False)
        self.ui.btnGetItemilce.setEnabled(True)
        self.ui.btnGetSelectedLogs.setEnabled(True)
        self.ui.cbilce.setEnabled(True)
    
    def Clear3(self):
        self.ui.btnLoad.setEnabled(False)
        self.ui.btnGetItemSehir.setEnabled(True)
        self.ui.btnGetItemilce.setEnabled(True)
        self.ui.btnGetSelectedLogsSehir.setEnabled(True)
        self.ui.cbSehir.setEnabled(True)
        self.ui.cbilce.setEnabled(False)
        self.ui.cbilce.clear()
        self.ui.btnClear2.setEnabled(False)
        self.ui.btnGetItemilce.setEnabled(False)
        self.ui.btnGetSelectedLogs.setEnabled(False)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()

  

    











