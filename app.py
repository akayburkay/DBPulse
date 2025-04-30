import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QFileDialog,QTableWidgetItem
from user import Ui_MainWindow
from PyQt5.QtCore import QTimer
import psutil
from fpdf import FPDF
import pandas as pd
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
import datetime



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        self.pushButton_conn.clicked.connect(self.db_page)
        self.pushButton_carpi.clicked.connect(self.anasayfa)
        self.pushButton_tablo.clicked.connect(self.tablo_page)
        self.pushButton_cpu.clicked.connect(self.cpu_performance_page)
        self.pushButton_pg_baglan.clicked.connect(self.pgconnection)
        self.pushButton_tablorapor.clicked.connect(self.tabloraporu)
        self.pushButton_sunucu.clicked.connect(self.sunucu_sayfasi)
        self.pushButton_geometri.clicked.connect(self.geometri_sayfasi)
        self.pushButton_indeks.clicked.connect(self.indeks_sayfasi)
        self.runReportButton.clicked.connect(self.runreport_sunucu)
        self.pushButton_tablo_temizle.clicked.connect(self.clear_table)
        self.pushButton_tablo_rapor_indir.clicked.connect(self.save_pdf_table)
        self.downloadReportButton.clicked.connect(self.download_report_pdf_server)
        self.run_report_index.clicked.connect(self.index_rapor)
        self.index_clear.clicked.connect(self.clear_index_table)
        self.downloadReportButton_index.clicked.connect(self.save_table_to_excel)
        self.run_report_geo.clicked.connect(self.run_geo)
        self.genel_ayar_temizle.clicked.connect(self.ayar)
        self.downloadReportButton_geo.clicked.connect(self.save_table_to_excel_geo)

        self.cpu_progress = self.progressBar_cpu
        self.ram_progress = self.progressBar_ram
        self.disk_progress = self.progressBar_disk
        self.set_progress_bar_style(self.cpu_progress)
        self.set_progress_bar_style(self.ram_progress)
        self.set_progress_bar_style(self.disk_progress)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000) 

    def ayar(self):
        self.resultTextEdit.clear()
    def indeks_sayfasi(self):
        self.stackedWidget.setCurrentIndex(7)
    def geometri_sayfasi(self):
        self.stackedWidget.setCurrentIndex(8)

    def sunucu_sayfasi(self):
        self.stackedWidget.setCurrentIndex(6)  
    def db_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def anasayfa(self):
        self.stackedWidget.setCurrentIndex(0)

    def tablo_page(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def cpu_performance_page(self):
        self.stackedWidget.setCurrentIndex(2)  
    
    def clear_table(self):
        self.textEdit_tablo.clear()
    
    def clear_index_table(self):
        self.index_result_table.clear()


    def pgconnection(self):
        if hasattr(self, 'conn') and self.conn is not None:
            try:
                self.conn.cursor().execute("SELECT 1")
                return self.conn  
            except (psycopg2.InterfaceError, psycopg2.OperationalError):
                self.conn = None  

        host = self.lineEdit.text()
        port = self.lineEdit_2.text()
        user = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        dbname = self.lineEdit_5.text()

        try:
            self.conn = psycopg2.connect(
                host=host, 
                port=port,
                dbname=dbname, 
                user=user, 
                password=password
            )

            if not hasattr(self, 'baglanti_bildirimi_gosterildi'):
                QMessageBox.information(self, "Başarılı", "Veritabanı bağlantısı başarıyla gerçekleşti!")
                self.baglanti_bildirimi_gosterildi = True  

            cur = self.conn.cursor()
            cur.execute("SHOW server_version;")
            postgres_version = cur.fetchone()[0]

            cur.execute("SELECT PostGIS_Version();")
            postgis_version = cur.fetchone()[0]

            self.label_5.setText(f"PostgreSQL Versiyon: {postgres_version}")
            self.label_6.setText(f"PostGIS Versiyon: {postgis_version}")

            cur.close()
            return self.conn

        except Exception as e:
            QMessageBox.critical(self, "Bağlantı Hatası", f"Bağlantı kurulamadı!\n{str(e)}")
            return None

    def set_progress_bar_style(self, progress_bar):
        value = progress_bar.value()

        if value <= 30:
            color = "#33FF99"  
        elif value <= 70:
            color = "#FFCC00"  
        else:
            color = "#FF3300"  

        progress_bar.setStyleSheet(f"""
            QProgressBar {{
                background-color: #2C2C2C;  
                border-radius: 10px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                width: 50px;  
                border-radius: 5px;
            }}
        """)


    def update_progress(self):
        cpu_usage = psutil.cpu_percent()
        
        ram = psutil.virtual_memory()
        ram_usage = ram.percent
        ram_total = round(ram.total / (1024**3), 2)  
        ram_used = round(ram.used / (1024**3), 2)
        ram_free = round(ram.available / (1024**3), 2)

        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        disk_total = round(disk.total / (1024**3), 2)  
        disk_used = round(disk.used / (1024**3), 2)
        disk_free = round(disk.free / (1024**3), 2)

        self.cpu_progress.setValue(int(cpu_usage))
        self.ram_progress.setValue(int(ram_usage))
        self.disk_progress.setValue(int(disk_usage))

        self.set_progress_bar_style(self.cpu_progress)
        self.set_progress_bar_style(self.ram_progress)
        self.set_progress_bar_style(self.disk_progress)

        sistem_bilgi = (
            "🔹 *Sistem Kullanım Bilgileri* 🔹\n"
            "-----------------------------------------\n"
            f"🖥️ *CPU Kullanımı:* %{cpu_usage}\n"
            "-----------------------------------------\n"
            f"💾 *RAM Kullanımı:* %{ram_usage}\n"
            f"    - **Toplam:** {ram_total} GB\n"
            f"    - **Kullanılan:** {ram_used} GB\n"
            f"    - **Boş:** {ram_free} GB\n"
            "-----------------------------------------\n"
            f"📂 *Disk Kullanımı:* %{disk_usage}\n"
            f"    - **Toplam:** {disk_total} GB\n"
            f"    - **Kullanılan:** {disk_used} GB\n"
            f"    - **Boş:** {disk_free} GB\n"
            "-----------------------------------------\n"
        )
        self.textEdit_cpu.setText(sistem_bilgi)


    

    
    def tabloraporu(self):
        analizler = {
            "tablo_veri_sayisi":self.checkBox_tabloveri.isChecked(),
            "en_buyuk_tablo":self.checkBox_enbuyuk_tablo.isChecked(),
            "pk_tanimli_olmayan":self.checkBox_pk_tanimli_olmayan.isChecked(),
            "pk_string":self.checkBox_pk_string.isChecked(),
            "view_performans":self.checkBox_view_performans.isChecked(),
            "view_join":self.checkBox_join_view.isChecked()
           
        }

        rapor = ""

        if analizler["tablo_veri_sayisi"]:
            rapor += "1)Tablo Veri Sayısı Analizi:\n"
            rapor += self.tablo_sayi_analizi()
            rapor += "\n\n"

        if analizler["en_buyuk_tablo"]:
            rapor += "2)Tablo Boyutu Analizi:\n"
            rapor += self.tablo_boyut_analizi()
            rapor += "\n\n"

        if analizler["pk_tanimli_olmayan"]:
            rapor += "3)Primary Key Tanımlı Olmayan Tablolar:\n"
            rapor += self.pk_tanimli_olmayan()
            rapor += "\n\n"

        if analizler["pk_string"]:
            rapor += "4)Primary Key String Olan Tablolar:\n"
            rapor += self.pk_string()
            rapor += "\n\n"
        
        if analizler["view_performans"]:
            rapor += "5)View Sorgulama Süreleri:\n"
            rapor += self.view_performans()
            rapor += "\n\n"

        if analizler["view_join"]:
            rapor += "6)3 Veya Daha Fazla Join İçeren Viewlar:\n"
            rapor += self.view_join()
            rapor += "\n\n"
        
        self.textEdit_tablo.setText(rapor)

    def tablo_sayi_analizi(self):
        query = """
            SELECT 
                relname AS table_name, 
                n_live_tup AS row_count
            FROM 
                pg_stat_user_tables
            ORDER BY 
                row_count DESC
            LIMIT 10;
        """
        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "Tablo veri sayısı analizi için veri bulunamadı.\n"
        except Exception as e:
            return f"Tablo veri sayısı analizi sırasında hata oluştu: {str(e)}\n"
    
    def tablo_boyut_analizi(self):
        query = """
            SELECT 
                relname AS table_name,
                pg_size_pretty(pg_total_relation_size(relid)) AS size
            FROM 
                pg_stat_user_tables
            ORDER BY 
                pg_total_relation_size(relid) DESC
            LIMIT 10;
        """
        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "Tablo boyutu analizi için veri bulunamadı.\n"
        except Exception as e:
            return f"Tablo boyutu analizi sırasında hata oluştu: {str(e)}\n"
    
    def pk_tanimli_olmayan(self):
        query = """
            SELECT 
                t.relname AS table_name
            FROM 
                pg_class t
                LEFT JOIN pg_constraint c ON t.oid = c.conrelid AND c.contype = 'p'
                LEFT JOIN pg_namespace n ON n.oid = t.relnamespace
            WHERE 
                t.relkind = 'r'  
                AND n.nspname NOT IN ('pg_catalog', 'information_schema')  
                AND c.conname IS NULL;  
        """
        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "Primary Key tanımlı olmayan tablo bulunamadı.\n"
        except Exception as e:
            return f"Primary Key analizi sırasında hata oluştu: {str(e)}\n"
    
    def pk_string(self):
        query = """
            SELECT 
                t.table_name, 
                c.column_name, 
                c.data_type
            FROM information_schema.table_constraints t
            JOIN information_schema.key_column_usage k 
                ON t.table_name = k.table_name 
                AND t.constraint_name = k.constraint_name
            JOIN information_schema.columns c 
                ON k.table_name = c.table_name 
                AND k.column_name = c.column_name
            WHERE t.constraint_type = 'PRIMARY KEY'
            AND c.data_type IN ('character varying', 'text', 'character');
        """
        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "Primary Key'i string olan tablo bulunamadı.\n"
        except Exception as e:
            return f"Primary Key string analizi sırasında hata oluştu: {str(e)}\n"
        
    def view_performans(self):
        query = """SELECT 
                v.viewname AS view_name,
                CASE 
                    WHEN SUM(s.total_exec_time) < 1000 
                    THEN ROUND(SUM(s.total_exec_time)::numeric, 2) || ' ms'
                    ELSE ROUND(SUM(s.total_exec_time)::numeric / 1000, 2) || ' sn'
                END AS total_exec_time
            FROM pg_stat_statements s
            JOIN pg_views v ON s.query LIKE '%' || v.viewname || '%'
            WHERE v.schemaname NOT IN ('pg_catalog', 'information_schema')
            GROUP BY v.viewname
            ORDER BY SUM(s.total_exec_time) DESC;
        """

        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "View Bulunamadı.\n"
        except Exception as e:
            return f"View Sorgu Analizi Sırasında Hata Oluştu: {str(e)}\n"
        
    def view_join(self):
        query="""SELECT 
    v.viewname
FROM 
    pg_views v
WHERE 
    v.schemaname NOT IN ('pg_catalog', 'information_schema')  -- Sistem şemaları hariç
    AND (
        (LENGTH(LOWER(v.definition)) - LENGTH(REPLACE(LOWER(v.definition), 'join', ''))) / LENGTH('join') >= 3
    )
ORDER BY 
    v.viewname;
"""
        try:
            result = self.execute_query(query)
            if result:
                return result
            else:
                return "3 Join İçeren View Bulunamadı.\n"
        except Exception as e:
            return f"Join Sorgusu Sırasında Hata Oluştu: {str(e)}\n"

    def execute_query(self, query):
        try:
            conn = psycopg2.connect(
                host=self.lineEdit.text(),
                port=self.lineEdit_2.text(),
                dbname=self.lineEdit_5.text(),
                user=self.lineEdit_3.text(),
                password=self.lineEdit_4.text()
            )
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            formatted_result = ""
            for row in result:
                formatted_result += ", ".join(map(str, row)) + "\n"
            cur.close()
            conn.close()
            return formatted_result

        except Exception as e:
            return f"Sorgu çalıştırılırken hata oluştu: {str(e)}"

    def runreport_sunucu(self):
        analiz = {
            "vt_baglantilari": self.cb1.isChecked(),
            "tune_ayarlari": self.cb2.isChecked(),
            "obje_bilgileri": self.cb3.isChecked(),
            "disk_giris": self.cb4.isChecked(),
        }
        rapor = ""
        if analiz["vt_baglantilari"]:
            rapor += "1)Veritabanı Aktif Bağlantı Bilgileri:\n"
            rapor += self.vt_baglanti_sayisi()
            rapor += "\n\n"

        if analiz["tune_ayarlari"]:
            rapor += "2)Tune Ayarları:\n"
            rapor += self.tune_ayarlari()
            rapor += "\n\n"

        if analiz["obje_bilgileri"]:
            rapor += "3)Veritabanı Obje Bilgileri:\n"
            rapor += self.obje_bilgileri()
            rapor += "\n\n"

        if analiz["disk_giris"]:
            rapor += "4)Disk Giriş/Çıkış Performansını Kontrol Et:\n"
            rapor += self.disk_kontrol()
            rapor += "\n\n"

        self.resultTextEdit.setText(rapor)

    def vt_baglanti_sayisi(self):
        query_server = """
            SELECT 
                datname AS veritabani, 
                usename AS kullanici, 
                COUNT(*) AS baglanti_sayisi
            FROM pg_stat_activity
            WHERE state = 'active'
            GROUP BY datname, usename, client_addr
            ORDER BY baglanti_sayisi DESC;
        """
        try:
            result = self.execute_query(query_server)
            if result:
                formatted_result = ""
                for row in result.split("\n"):
                    formatted_result += row + "\n"
                return formatted_result
            else:
                return "Aktif veritabanı bağlantısı bulunamadı.\n"
        except Exception as e:
            return f"Veritabanı bağlantı sayısını alırken hata oluştu: {str(e)}\n"

    def tune_ayarlari(self):
        query_server = """
            SELECT 
                name, 
                CASE 
                    WHEN name IN ('checkpoint_completion_target', 'random_page_cost', 'huge_pages', 'default_statistics_target', 'effective_io_concurrency', 'max_connections', 'max_worker_processes', 'max_parallel_workers_per_gather', 'max_parallel_workers', 'max_parallel_maintenance_workers') 
                    THEN setting
                    WHEN unit IN ('kB', '8kB') THEN (setting::bigint * 1.0 / 1024)::numeric(10,2) || ' MB'
                    WHEN unit = 'MB' THEN setting || ' MB'
                    WHEN unit = 'GB' THEN setting || ' GB'
                    ELSE setting 
                END AS formatted_value
            FROM pg_settings
            WHERE name IN (
                'max_connections',
                'shared_buffers',
                'effective_cache_size',
                'maintenance_work_mem',
                'checkpoint_completion_target',
                'wal_buffers',
                'default_statistics_target',
                'random_page_cost',
                'effective_io_concurrency',
                'work_mem',
                'huge_pages',
                'min_wal_size',
                'max_wal_size',
                'max_worker_processes',
                'max_parallel_workers_per_gather',
                'max_parallel_workers',
                'max_parallel_maintenance_workers'
            );
        """
        try:
            result = self.execute_query(query_server)
            if result:
                formatted_result = ""
                for row in result.split("\n"):
                    formatted_result += row + "\n"
                return formatted_result
            else:
                return "Tune Ayarı Analizinde Hata Oluştu.\n"
        except Exception as e:
            return f"{str(e)}\n"

    def disk_kontrol(self):
        query_server = """
            SELECT
                buffers_alloc AS "Yeni Tahsis Edilen Buffer Sayısı",
                buffers_clean AS "Arka Plan Yazıcı Tarafından Temizlenen Buffer Sayısı",
                buffers_backend AS "Backend İşlemler Tarafından Diske Yazılan Buffer Sayısı"
            FROM pg_stat_bgwriter;
        """
        try:
            result = self.execute_query(query_server)
            if result:
                formatted_result = ""
                for row in result.split("\n"):
                    formatted_result += row + "\n"
                return formatted_result
            else:
                return "Disk performans bilgisi bulunamadı.\n"
        except Exception as e:
            return f"Disk performans bilgisi alınırken hata oluştu: {str(e)}\n"

    def obje_bilgileri(self):
        query_server = """
        SELECT 
            COUNT(*) AS toplam_tablo,
            (SELECT COUNT(*) FROM pg_indexes WHERE schemaname NOT IN ('pg_catalog', 'information_schema')) AS toplam_indeks,
            (SELECT COUNT(*) FROM pg_views WHERE schemaname NOT IN ('pg_catalog', 'information_schema')) AS toplam_gorunum,
            (SELECT COUNT(*) FROM pg_proc WHERE pronamespace NOT IN 
                (SELECT oid FROM pg_namespace WHERE nspname IN ('pg_catalog', 'information_schema'))) AS toplam_fonksiyon
        FROM pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema');
        """
        try:
            result = self.execute_query(query_server)
            if result:
                values = result.strip().split(", ")  # Metni listeye çevir
                column_names = ["Tablo Sayısı", "İndeks Sayısı", "View Sayısı", "Fonksiyon Sayısı"]

                formatted_result = ""
                for i in range(len(column_names)):
                    formatted_result += f"{column_names[i]}: {values[i]}\n"

                return formatted_result
            else:
                return "Obje bilgileri alınırken hata oluştu.\n"
        except Exception as e:
            return f"Hata: {str(e)}\n"

   

    def save_pdf_table(self):
        """
        Tablo ve View Analizi raporunu PDF olarak kaydetme (Tarihsiz versiyon)
        """
        file_dialog = QFileDialog(self)
        file_dialog.setDefaultSuffix(".pdf")
        file_path, _ = file_dialog.getSaveFileName(
            self,
            "PDF olarak kaydet",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:
            try:
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)
                printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)

                # HTML içeriği (başlık ve metin)
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {{ font-family: Arial; font-size: 12pt; }}
                        h1 {{ text-align: center; color: #0066cc; }}
                        pre {{ white-space: pre-wrap; font-family: Consolas; }}
                        .bold {{ font-weight: bold; }}
                    </style>
                </head>
                <body>
                    <h1>Tablo ve View Analizi</h1>
                    <pre>{self.textEdit_tablo.toPlainText()}</pre>
                </body>
                </html>
                """

                doc = QTextDocument()
                doc.setHtml(html_content)
                doc.print_(printer)

                self.show_message("Başarılı", "PDF başarıyla kaydedildi.")

            except Exception as e:
                self.show_message("Hata", f"PDF oluşturulamadı:\n{str(e)}")

    def download_report_pdf_server(self):
        """
        Sunucu Durumu Analizi raporunu PDF olarak kaydetme (Türkçe karakter garantili)
        """
        file_dialog = QFileDialog(self)
        file_dialog.setDefaultSuffix(".pdf")
        file_path, _ = file_dialog.getSaveFileName(
            self,
            "PDF olarak kaydet",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:
            try:
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)
                printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)  # Kenar boşlukları

                # CSS ile tutarlı stil tanımı
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {{ 
                            font-family: Arial; 
                            font-size: 12pt;
                            font-weight: bold;  /* TÜM METNİ KALIN YAPAR */
                        }}
                        h1 {{ 
                            text-align: center; 
                            color: #0066cc;
                            font-weight: bold;  /* BAŞLIK DAHA KALIN */
                        }}
                        pre {{ 
                            white-space: pre-wrap; 
                            font-family: Consolas;
                        }}
                    </style>
                </head>
                <body>
                    <h1>Sunucu Durumu Analizi</h1>
                    <pre>{self.resultTextEdit.toPlainText()}</pre>
                </body>
                </html>
                """

                doc = QTextDocument()
                doc.setHtml(html_content)
                doc.print_(printer)

                self.show_message("Başarılı", "PDF başarıyla kaydedildi.")

            except Exception as e:
                self.show_message("Hata", f"PDF oluşturulamadı:\n{str(e)}")
                

    def show_message(self, title, message):
        """
        Kullanıcıya başarı ya da hata mesajı göstermek için yardımcı fonksiyon.
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information if title == "Başarılı" else QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    
    def index_rapor(self):
        conn = self.pgconnection() 
        if conn is None:  
            return  

        try:
            cur = conn.cursor()
            sorgu = ""
            columns = ["Tablo Adı", "İndeks Adı", "İndeks Kolonları", "İndeks Boyutu", "İndeks Tarama Sayısı", "İndeks Kullanım Oranı"]

            if self.rb_kullanilmayan_index.isChecked():
                sorgu = """
                    SELECT 
                        relname AS "Tablo Adı",
                        indexrelname AS "İndeks Adı",
                        idx_scan AS "İndeks Tarama Sayısı",
                        pg_size_pretty(pg_relation_size(indexrelid)) AS "İndeks Boyutu"
                    FROM 
                        pg_stat_user_indexes
                    WHERE 
                        idx_scan = 0
                    ORDER BY 
                        pg_relation_size(indexrelid) DESC;
                """
                columns = ["Tablo Adı", "İndeks Adı", "İndeks Tarama Sayısı", "İndeks Boyutu"]

            elif self.rb_index_oran.isChecked():
                sorgu = """
                    SELECT 
                        pg_stat_user_tables.relname AS "Tablo Adı",
                        pg_stat_user_indexes.indexrelname AS "İndeks Adı",
                        pg_stat_user_indexes.idx_scan AS "İndeks Tarama Sayısı",
                        pg_size_pretty(pg_relation_size(pg_stat_user_indexes.indexrelid)) AS "İndeks Boyutu",
                        round((100.0 * pg_stat_user_indexes.idx_scan / NULLIF(pg_stat_user_indexes.idx_scan + pg_stat_user_tables.seq_scan, 0))::numeric, 2) AS "İndeks Kullanım Oranı (%)"
                    FROM 
                        pg_stat_user_indexes
                    JOIN 
                        pg_stat_user_tables 
                        ON pg_stat_user_indexes.relid = pg_stat_user_tables.relid
                    ORDER BY 
                        "İndeks Kullanım Oranı (%)" DESC;
                """
                columns = ["Tablo Adı", "İndeks Adı", "İndeks Tarama Sayısı", "İndeks Boyutu", "İndeks Kullanım Oranı (%)"]

            elif self.rb_btree.isChecked():
                sorgu = """
                    SELECT 
                        t.relname AS "Tablo Adı",
                        i.relname AS "İndeks Adı",
                        ARRAY_AGG(c.attname) AS "İndeks Kolonları",
                        COUNT(*) AS "Bir Kolona Tanımlanan İndeks Sayısı"
                    FROM 
                        pg_index ix
                    JOIN 
                        pg_class t ON t.oid = ix.indrelid
                    JOIN 
                        pg_class i ON i.oid = ix.indexrelid
                    JOIN 
                        pg_attribute c ON c.attrelid = t.oid AND c.attnum = ANY(ix.indkey)
                    JOIN 
                        pg_namespace n ON n.oid = t.relnamespace
                    WHERE 
                        i.relkind = 'i'
                        AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
                    GROUP BY 
                        t.relname, i.relname
                    HAVING 
                        COUNT(*) > 1
                    ORDER BY 
                        "Bir Kolona Tanımlanan İndeks Sayısı" DESC;
                """
                columns = ["Tablo Adı", "İndeks Adı", "İndeks Kolonları", "Bir Kolona Tanımlanan İndeks Sayısı"]
            
            if self.rb_index_bloat.isChecked():
                sorgu = """
                WITH index_bloat AS (
    SELECT
        c.oid AS table_oid,
        c.relname AS "Tablo Adı",
        i.relname AS "İndeks Adı",
        pg_size_pretty(pg_relation_size(i.oid)) AS "İndeks Boyutu",
        pg_size_pretty(
            GREATEST(
                pg_relation_size(i.oid) - (pg_relation_size(c.oid) * NULLIF(i.reltuples, 0) / NULLIF(c.reltuples, 1)),
                0
            )::bigint
        ) AS "Şişme Boyutu",
        ROUND(
            100 * GREATEST(
                pg_relation_size(i.oid) - (pg_relation_size(c.oid) * NULLIF(i.reltuples, 0) / NULLIF(c.reltuples, 1)),
                0
            )::numeric 
            / NULLIF(pg_relation_size(i.oid), 1), 
        2) AS "Şişme Oranı (%)"
    FROM
        pg_class c
    JOIN
        pg_index ix ON c.oid = ix.indrelid
    JOIN
        pg_class i ON i.oid = ix.indexrelid
    JOIN
        pg_namespace n ON n.oid = c.relnamespace  -- Namespace eklenerek sistem indeksleri filtrelendi
    WHERE
        i.relkind = 'i'
        AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast') -- Sistem tablolarını hariç tut
)
SELECT 
    "Tablo Adı",
    "İndeks Adı",
    "İndeks Boyutu",
    "Şişme Boyutu",
    "Şişme Oranı (%)"
FROM index_bloat
WHERE "Şişme Oranı (%)" > 45 
ORDER BY "Şişme Oranı (%)" DESC;

                """
                columns = ["Tablo Adı", "İndeks Adı", "İndeks Boyutu", "Şişme Boyutu", "Şişme Oranı (%)"]
                
            if sorgu:
                cur.execute(sorgu)
                data = cur.fetchall()

                if not data:  
                    QMessageBox.information(self, "Bilgi", "Sorgu sonucunda hiçbir veri bulunamadı.")
                    return

                self.index_result_table.setRowCount(len(data))
                self.index_result_table.setColumnCount(len(columns))
                self.index_result_table.setHorizontalHeaderLabels(columns)

                for row_idx, row_data in enumerate(data):
                    for col_idx, cell_data in enumerate(row_data):
                        self.index_result_table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))
            cur.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Sorgu çalıştırılırken hata oluştu: {str(e)}")
        finally:
            conn.close()  
        
    def save_table_to_excel(self):
        if self.index_result_table.rowCount() == 0:
            QMessageBox.warning(self, "Uyarı", "Tabloda kaydedilecek veri bulunamadı!")
            return     
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Excel Olarak Kaydet", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        
        if not file_path:
            return  
        
        row_count = self.index_result_table.rowCount()
        column_count = self.index_result_table.columnCount()
        
        data = []
        headers = [self.index_result_table.horizontalHeaderItem(col).text() if self.index_result_table.horizontalHeaderItem(col) else f"Column {col}" for col in range(column_count)]
        
        for row in range(row_count):
            row_data = [self.index_result_table.item(row, col).text() if self.index_result_table.item(row, col) else "" for col in range(column_count)]
            data.append(row_data)
        
        df = pd.DataFrame(data, columns=headers)
        
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
            worksheet = writer.sheets["Sheet1"]
            for col_num, col_name in enumerate(df.columns):
                worksheet.set_column(col_num, col_num, 20)  #        
        print("Veriler başarıyla kaydedildi.")

    def save_table_to_excel_geo(self):
        if self.result_geo.rowCount() == 0:
            QMessageBox.warning(self, "Uyarı", "Tabloda kaydedilecek veri bulunamadı!")
            return     
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Excel Olarak Kaydet", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        
        if not file_path:
            return  
    
        row_count = self.result_geo.rowCount()
        column_count = self.result_geo.columnCount()
        
        data = []
        headers = [self.result_geo.horizontalHeaderItem(col).text() if self.result_geo.horizontalHeaderItem(col) else f"Column {col}" for col in range(column_count)]
        
        for row in range(row_count):
            row_data = [self.result_geo.item(row, col).text() if self.result_geo.item(row, col) else "" for col in range(column_count)]
            data.append(row_data)
        
        df = pd.DataFrame(data, columns=headers)
        
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
            worksheet = writer.sheets["Sheet1"]
            for col_num, col_name in enumerate(df.columns):
                worksheet.set_column(col_num, col_num, 20)        

    def run_geo(self):
        conn = self.pgconnection() 
        if conn is None:  
            return  
        try:
            cur = conn.cursor()
            sorgu = ""

            if self.rb_geo_table.isChecked():
                sorgu = """
                SELECT 
                c.table_name as "Tablo Adı",
                c.column_name as "Kolon Adı",
                gc.type AS "Geometri Türü",
                gc.srid AS srid,           
                pg_size_pretty(pg_relation_size(cls.oid)) AS "Tablo Boyutu"
                FROM information_schema.columns c
                JOIN pg_class cls ON c.table_name = cls.relname  
                JOIN pg_namespace ns ON cls.relnamespace = ns.oid AND ns.nspname = c.table_schema
                LEFT JOIN geometry_columns gc 
                    ON c.table_schema = gc.f_table_schema 
                    AND c.table_name = gc.f_table_name 
                    AND c.column_name = gc.f_geometry_column
                WHERE c.udt_name IN ('geometry', 'geography')
                ORDER BY c.table_schema, c.table_name, c.column_name;
                """
                cur.execute(sorgu)
                results = cur.fetchall()

            elif self.rb_geo_view.isChecked():
                sorgu = """SELECT 
                v.viewname AS "View Adı",
                f.proname AS "Fonksiyon Adı",
                pg_catalog.pg_get_function_result(f.oid) AS "Fonksiyon Sonucu"
                FROM 
                pg_views v
                JOIN 
                pg_catalog.pg_proc f ON f.prosrc LIKE 'ST\_%'  -- 'ST_' ile başlayan fonksiyonlar
                JOIN 
                pg_catalog.pg_namespace n ON n.oid = f.pronamespace
                WHERE 
                v.schemaname = n.nspname
                AND f.prosrc IS NOT NULL
                AND v.viewname IN (
                    SELECT table_name 
                    FROM information_schema.columns
                    WHERE udt_name IN ('geometry', 'geography')  -- Geometrik veri içeren kolonlar
                )
                ORDER BY v.schemaname, v.viewname;
                """
                cur.execute(sorgu)
                results = cur.fetchall()           
            elif self.rb_gist.isChecked():
                sorgu = """SELECT 
                c.table_name AS "Tablo Adı",
                c.column_name AS "Kolon Adı",
                pg_size_pretty(pg_relation_size(cls.oid)) AS "Tablo Boyutu"
                FROM 
                information_schema.columns c
                JOIN 
                pg_class cls ON c.table_name = cls.relname  
                JOIN 
                pg_namespace ns ON cls.relnamespace = ns.oid AND ns.nspname = c.table_schema
                LEFT JOIN 
                pg_index i ON cls.oid = i.indrelid
                LEFT JOIN 
                pg_class index_cls ON i.indexrelid = index_cls.oid
                LEFT JOIN 
                pg_am am ON index_cls.relam = am.oid
                WHERE 
                c.udt_name IN ('geometry', 'geography')  -- Geometrik veri türleri
                AND (am.amname != 'gist' OR am.amname IS NULL)  -- GIST index olmayan kolonlar
                ORDER BY 
                c.table_schema, c.table_name, c.column_name;
                """
                cur.execute(sorgu)
                results = cur.fetchall()

            elif self.rb_srid.isChecked():
                sorgu = """SELECT 
            f_table_name AS tablo_adı,
            f_geometry_column AS kolon_adı,
            srid,
            type AS geometri_tipi,
            coord_dimension AS koordinat_boyutu
        FROM 
            geometry_columns
        WHERE srid = 0
            """
                cur.execute(sorgu)
                results = cur.fetchall()

            if results:
                column_names = [desc[0] for desc in cur.description]  
                self.result_geo.setColumnCount(len(column_names))
                self.result_geo.setRowCount(len(results))
                self.result_geo.setHorizontalHeaderLabels(column_names)
                
                for row_idx, row_data in enumerate(results):
                    for col_idx, col_value in enumerate(row_data):
                        self.result_geo.setItem(row_idx, col_idx, QTableWidgetItem(str(col_value)))

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hata oluştu: {str(e)}")

        finally:
            cur.close()
            conn.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
