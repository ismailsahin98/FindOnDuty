sehirListesi = ['Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin', 'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakir', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir', 'Kars', 'Kastamonu', 'Kayseri', 
'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']


sehirilce = {
'1' : ('Aladağ', 'Ceyhan', 'Çukurova', 'Feke', 'İmamoğlu', 'Karaisalı', 'Karataş', 'Kozan', 'Merkez', 'Pozantı', 'Saimbeyli', 'Salbaş', 'Sarıçam', 'Seyhan', 'Tekir', 'Tufanbeyli', 'Yumurtalık', 'Yüreğir'),
'2' : ('Besni', 'Çelikhan', 'Gerger', 'Gölbaşı', 'Kahta', 'Merkez', 'Samsat', 'Sincik', 'Tut' ) ,
'3' : ('Başmakçı', 'Bayat', 'Bolvadin', 'Çay', 'Çobanlar', 'Dazkırı', 'Dinar', 'Emirdağ', 'Evciler','Hocalar', 'İhsaniye', 'İscehisar', 'Kızılören', 'Merkez', 'Sandıklı', 'Sinanpaşa', 'Şuhut', 'Sultandağı'),
'4' : ('Diyadin', 'Doğubayazıt', 'Eleşkirt', 'Hamur', 'Merkez', 'Patnos', 'Taşlıçay', 'Tutak'),
'5' : ('Göynücek', 'Gümüşhacıköy', 'Hamamözü', 'Merkez', 'Merzifon', 'Suluova', 'Taşova'),
'6' :('Akyurt', 'Altındağ', 'Ayaş', 'Bala', 'Beypazarı', 'Çamlıdere', 'Çankaya', 'Çubuk', 'Elmadağ', 'Etimesgut', 'Evren', 'Gölbaşı', 'Güdül', 'Haymana', 'Kahramankazan', 'Kalecik', 'Kazan', 'Keçiören', 'Kızılcahamam', 'Mamak', 'Merkez', 'Nallıhan', 'Polatlı', 'Pursaklar', 'Şereflikoçhisar', 'Sincan','Yahşihan','Yenimahalle'),
'7': ('Akseki', 'Aksu', 'Alanya', 'Demre', 'Döşemealtı', 'Elmalı', 'Finike', 'Gazipaşa', 'Gündoğmuş', 'İbradı', 'Kaş', 'Kemer', 'Kepez', 'Konyaaltı', 'Korkuteli', 'Kumluca', 'Manavgat', 'Merkez', 'Muratpaşa', 'Serik'), 
'8' : ('Ardanuç', 'Arhavi', 'Borçka', 'Hopa', 'Kemalpaşa', 'Merkez', 'Murgul', 'Şavşat', 'Yusufeli'), 
'9' : ('Acarlar', 'Akbük', 'Akçaova', 'Altınkum', 'Atça', 'Bağarası', 'Bozdoğan', 'Buharkent', 'Çine', 'Davutlar', 'Didim', 'Efeler', 'Germencik', 'Güzelçamlı', 'İncirliova', 'Karacasu', 'Karpuzlu', 'Koçarlı', 'Köşk', 'Kuşadası','Kuyucak', 'Merkez', 'Nazilli', 'Ortaklar', 'Pamukören', 'Söke', 'Sultanhisar', 'Umurlu', 'Yenipazar'), 
'10' : ('Akçay', 'Altıeylül', 'Altınoluk', 'Altınova', 'Ayvalık', 'Balya', 'Bandırma', 'Bigadiç', 'Burhaniye', 'Dursunbey', 'Edremit', 'Erdek', 'Gömeç', 'Gönen', 'Havran', 'İvrindi', 'Kadıköy', 'Karesi', 'Kepsut', 'Manyas', 'Marmara', 'Merkez', 'Sarımsaklı', 'Savaştepe', 'Sındırgı', 'Susurluk'),
'11' : ('Bozüyük', 'Gölpazarı', 'İnhisar', 'Merkez', 'Osmaneli', 'Pazaryeri', 'Söğüt', 'Yenipazar'), 
'12' : ('Adaklı', 'Genç', 'Karlıova', 'Kiğı', 'Merkez', 'Solhan', 'Yayladere', 'Yedisu'), 
'13': ('Adilcevaz', 'Ahlat', 'Güroymak','Hizan', 'Merkez', 'Mutki', 'Tatvan'),
'14' : ('Dörtdivan', 'Gerede', 'Göynük', 'Kıbrıscık', 'Mengen', 'Merkez', 'Mudurnu', 'Seben', 'Yeniçağa'),
'15': ('Ağlasun', 'Altınyayla', 'Bucak', 'Çavdır', 'Çeltikçi', 'Gölhisar', 'Karamanlı', 'Kemer', 'Merkez', 'Tefenni', 'Yeşilova'), 
'16': ('Büyükorhan', 'Gemlik', 'Gürsu', 'Harmancık', 'İnegöl', 'İznik', 'Karacabey', 'Keles', 'Kestel', 'Merkez', 'Mudanya', 'Mustafakemalpaşa', 'Nilüfer', 'Orhaneli', 'Orhangazi', 'Osmangazi', 'Yenişehir', 'Yıldırım'), 
'17': ('Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Çardak', 'Eceabat', 'Ezine', 'Gelibolu', 'Geyikli', 'Gökçeada', 'Küçükkuyu', 'Lapseki', 'Merkez', 'Yenice'), 
'18':('Atkaracalar', 'Bayramören', 'Çerkeş', 'Eldivan', 'Ilgaz', 'Kızılırmak', 'Korgun', 'Kurşunlu', 'Merkez', 'Orta', 'Şabanözü', 'Yapraklı'), 
'19': ('Alaca', 'Bayat', 'Boğazkale', 'Dodurga', 'İskilip', 'Kargı', 'Laçin', 'Mecitözü', 'Merkez', 'Oğuzlar', 'Ortaköy', 'Osmancık', 'Sungurlu', 'Uğurludağ'),
'20': ('Acıpayam', 'Akköy', 'Babadağ', 'Baklan', 'Bekilli', 'Beyağaç', 'Bozkurt', 'Buldan', 'Çal', 'Çameli', 'Çardak', 'Çivril', 'Güney', 'Honaz', 'Kale', 'Merkez', 'Merkezefendi', 'Pamukkale', 'Sarayköy', 'Serinhisar', 'Tavas'), 
'21' : ('Bağlar', 'Bismil', 'Çermik', 'Çınar', 'Çüngüş', 'Dicle', 'Eğil', 'Ergani', 'Hani', 'Hazro', 'Kayapınar', 'Kocaköy', 'Kulp', 'Lice', 'Merkez', 'Silvan', 'Sur', 'Yenişehir'), 
'22' :('Enez', 'Havsa', 'İpsala', 'Keşan', 'Lalapaşa', 'Meriç', 'Merkez', 'Süloğlu', 'Uzunköprü'), 
'23': ('Ağın', 'Alacakaya', 'Arıcak', 'Baskil', 'Karakoçan', 'Keban', 'Kovancılar', 'Maden', 'Merkez', 'Palu', 'Sivrice'), 
'24' : ('Çayırlı', 'İliç', 'Kemah', 'Kemaliye', 'Merkez', 'Otlukbeli', 'Refahiye', 'Tercan', 'Üzümlü'), 
'25' : ('Aşkale', 'Aziziye', 'Çat', 'Hınıs', 'Horasan', 'İspir', 'Karaçoban', 'Karayazı', 'Köprüköy', 'Merkez', 'Narman', 'Oltu', 'Olur', 'Palandöken', 'Pasinler', 'Pazaryolu', 'Şenkaya', 'Tekman', 'Tortum', 'Uzundere', 'Yakutiye'), 
'26' : ('Alpu', 'Beylikova', 'Çifteler', 'Günyüzü', 'Han', 'İnönü', 'Mahmudiye', 'Merkez', 'Mihalgazi', 'Mihalıcçık', 'Odunpazarı', 'Sarıcakaya', 'Seyitgazi', 'Sivrihisar', 'Tepebaşı'), 
'27' : ('Araban', 'İslahiye', 'Karkamış', 'Merkez', 'Nizip', 'Nurdağı', 'Oğuzeli', 'Şahinbey', 'Şehitkamil', 'Yavuzeli'), 
'28' : ('Alucra', 'Bulancak', 'Çamoluk', 'Çanakçı', 'Dereli', 'Doğankent', 'Espiye', 'Eynesil', 'Görele', 'Güce', 'Keşap', 'Merkez', 'Piraziz', 'Şebinkarahisar', 'Tirebolu', 'Yağlıdere'), 
'29' : ('Kelkit', 'Köse', 'Kürtün', 'Merkez', 'Şiran', 'Torul'), 
'30' : ('Çukurca', 'Merkez', 'Şemdinli', 'Yüksekova'), 
'31' : ('Altınözü', 'Antakya','Arsuz','Belen','Defne','Dörtyol','Erzin', 'Hassa','İskenderun','Kırıkhan', 'Kumlu', 'Merkez', 'Payas','Reyhanlı', 'Samandağ', 'Yayladağı'), 
'32' : ('Aksu', 'Atabey', 'Eğirdir', 'Gelendost', 'Gönen', 'Keçiborlu', 'Merkez', 'Şarkikaraağaç', 'Senirkent', 'Sütçüler', 'Uluborlu', 'Yalvaç', 'Yenişarbademli'), 
'33' : ('Akdeniz', 'Anamur', 'Aydıncık', 'Bozyazı', 'Çamlıyayla', 'Erdemli', 'Gülnar', 'Merkez', 'Mezitli', 'Mut', 'Silifke', 'Tarsus', 'Toroslar', 'Yenişehir'),
'34' : ('Adalar', 'Arnavutköy', 'Ataşehir', 'Avcılar', 'Bağcılar', 'Bahçelievler', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beşiktaş', 'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca', 'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüp', 'Fatih', 'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kağıthane', 'Kartal', 'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe', 'Sarıyer', 'Şile', 'Silivri', 'Şişli', 'Sultanbeyli', 'Sultangazi', 'Tuzla', 'Ümraniye', 'Üsküdar', 'Zeytinburnu'), 
'35' : ('Aliağa', 'Alsancak', 'Ayrancılar', 'Balçova', 'Bayındır', 'Bayraklı', 'Bergama', 'Beydağ', 'Bornova', 'Buca', 'Çeşme', 'Çiğli', 'Dikili', 'Foça', 'Gaziemir', 'Güzelbahçe', 'Karabağlar', 'Karaburun', 'Karşıyaka', 'Kemalpaşa', 'Kiraz', 'Kınık', 'Konak', 'Menderes', 'Menemen', 'Merkez', 'Narlıdere', 'Ödemiş', 'Seferihisar', 'Selçuk', 'Tire', 'Torbalı', 'Urla'), 
'36': ('Akyaka', 'Arpaçay', 'Digor', 'Kağızman', 'Merkez', 'Sarıkamış', 'Selim', 'Susuz'), 
'37' : ('Abana', 'Ağlı', 'Araç', 'Azdavay', 'Bozkurt', 'Çatalzeytin', 'Cide', 'Daday', 'Devrekani', 'Doğanyurt', 'Hanönü', 'İhsangazi', 'İnebolu', 'Küre', 'Merkez', 'Pınarbaşı', 'Şenpazar', 'Seydiler', 'Taşköprü', 'Tosya'), 
'38': ('Akkışla', 'Bünyan', 'Develi', 'Felahiye', 'Hacılar', 'İncesu', 'Kocasinan', 'Melikgazi', 'Merkez', 'Özvatan', 'Pınarbaşı', 'Sarıoğlan', 'Sarız', 'Talas', 'Tomarza', 'Yahyalı', 'Yeşilhisar'),
'39' : ('Alpullu', 'Babaeski', 'Büyükkarıştıran', 'Büyükmandıra', 'Demirköy', 'Kofçaz', 'Lüleburgaz', 'Merkez', 'Pehlivanköy', 'Pınarhisar', 'Vize'),
'40' : ('Akçakent', 'Akpınar', 'Boztepe', 'Çiçekdağı', 'Kaman', 'Merkez', 'Mucur'),
'41': ('Başiskele', 'Çayırova','Darıca', 'Derince', 'Dilovası', 'Gebze', 'Gölcük', 'İzmit', 'Kandıra', 'Karamürsel', 'Kartepe', 'Körfez', 'Merkez'),
'42' : ('Ahırlı', 'Akören', 'Akşehir', 'Altınekin', 'Beyşehir', 'Bozkır', 'Çeltik', 'Cihanbeyli', 'Çumra', 'Derbent', 'Derebucak', 'Doğanhisar', 'Emirgazi', 'Ereğli', 'Güneysınır', 'Hadim', 'Halkapınar', 'Hüyük', 'Ilgın', 'Kadınhanı', 'Karapınar', 'Karatay', 'Kulu', 'Meram', 'Merkez', 'Sarayönü', 'Selçuklu', 'Seydişehir', 'Taşkent', 'Tuzlukçu', 'Yalıhüyük', 'Yunak'),
'43' : ('Altıntaş', 'Aslanapa', 'Çavdarhisar', 'Domaniç', 'Dumlupınar', 'Emet', 'Gediz', 'Hisarcık', 'Merkez', 'Pazarlar', 'Şaphane', 'Simav', 'Tavşanlı'),
'44' : ('Akçadağ', 'Arapgir', 'Arguvan', 'Battalgazi', 'Darende', 'Doğanşehir', 'Doğanyol', 'Hekimhan', 'Kale', 'Kuluncak', 'Merkez', 'Pütürge', 'Yazıhan', 'Yeşilyurt'),
'45' : ('Ahmetli', 'Akhisar', 'Alaşehir', 'Demirci', 'Gölmarmara', 'Gördes', 'Kırkağaç', 'Köprübaşı', 'Kula', 'Merkez', 'Salihli', 'Sarıgöl', 'Saruhanlı', 'Şehzadeler', 'Selendi', 'Soma', 'Turgutlu', 'Yunusemre'),
'46' : ('Afşin', 'Andırın', 'Çağlayancerit', 'Dulkadiroğlu', 'Ekinözü', 'Elbistan', 'Göksun', 'Merkez', 'Nurhak', 'Onikişubat', 'Pazarcık', 'Türkoğlu'),
'47' : ('Artuklu', 'Dargeçit', 'Derik', 'Kızıltepe', 'Mazıdağı', 'Merkez', 'Midyat', 'Nusaybin', 'Ömerli', 'Savur', 'Yeşilli'),
'48' : ('Bodrum', 'Dalaman', 'Datça', 'Fethiye', 'Kavaklıdere', 'Köyceğiz', 'Marmaris', 'Menteşe', 'Merkez', 'Milas', 'Ortaca', 'Seydikemer', 'Ula', 'Yatağan'),
'49' : ('Bulanık', 'Hasköy', 'Korkut', 'Malazgirt', 'Merkez', 'Varto'),
'50' : ('Acıgöl', 'Avanos', 'Derinkuyu', 'Gülşehir', 'Hacıbektaş', 'Kozaklı', 'Merkez', 'Ürgüp'), 
'51': ('Altunhisar', 'Bor', 'Çamardı', 'Çiftlik', 'Merkez', 'Ulukışla'),
'52' : ('Akkuş', 'Altınordu', 'Aybastı', 'Çamaş', 'Çatalpınar', 'Çaybaşı', 'Fatsa', 'Gölköy', 'Gülyalı', 'Gürgentepe', 'İkizce', 'Kabadüz', 'Kabataş', 'Korgan', 'Kumru', 'Merkez', 'Mesudiye', 'Perşembe', 'Ulubey', 'Ünye'),
'53' : ('Ardeşen', 'Çamlıhemşin', 'Çayeli', 'Derepazarı', 'Fındıklı', 'Güneysu', 'Hemşin', 'İkizdere', 'İyidere', 'Kalkandere', 'Merkez', 'Pazar'),
'54' : ('Adapazarı', 'Akyazı', 'Arifiye', 'Erenler', 'Ferizli', 'Geyve', 'Hendek', 'Karapürçek', 'Karasu', 'Kaynarca', 'Kocaali', 'Merkez', 'Pamukova', 'Sapanca', 'Serdivan', 'Söğütlü', 'Taraklı'),
'55' : ('Alaçam', 'Asarcık', 'Atakum', 'Ayvacık', 'Bafra', 'Canik', 'Çarşamba', 'Havza', 'İlkadım', 'Kavak', 'Ladik', 'Merkez', 'Ondokuzmayıs', 'Salıpazarı', 'Tekkeköy', 'Terme', 'Vezirköprü', 'Yakakent'),
'56' :('Baykan', 'Eruh', 'Kurtalan', 'Merkez', 'Pervari', 'Şirvan', 'Tillo'),
'57': ('Ayancık', 'Boyabat', 'Dikmen', 'Durağan', 'Erfelek', 'Gerze', 'Merkez', 'Saraydüzü', 'Türkeli'),
'58': ('Akıncılar', 'Altınyayla', 'Divriği', 'Doğanşar', 'Gemerek', 'Gölova', 'Gürün', 'Hafik', 'İmranlı', 'Kangal', 'Koyulhisar', 'Merkez', 'Şarkışla', 'Suşehri', 'Ulaş', 'Yıldızeli', 'Zara'),
'59': ('Çerkezköy', 'Çorlu', 'Ergene', 'Hayrabolu', 'Kapaklı', 'Malkara', 'Marmaraereğlisi', 'Merkez', 'Muratlı', 'Saray', 'Şarköy', 'Süleymanpaşa'),
'60' : ('Almus', 'Artova', 'Başçiftlik', 'Erbaa', 'Merkez', 'Niksar', 'Pazar', 'Reşadiye', 'Sulusaray', 'Turhal', 'Yeşilyurt', 'Zile'),
'61' : ('Akçaabat', 'Araklı', 'Arsin', 'Beşikdüzü', 'Çarşıbaşı', 'Çaykara', 'Dernekpazarı', 'Düzköy', 'Hayrat', 'Köprübaşı', 'Maçka', 'Merkez', 'Of', 'Ortahisar', 'Şalpazarı', 'Sürmene', 'Tonya', 'Vakfıkebir', 'Yomra'),
'62': ('Çemişgezek', 'Hozat', 'Mazgirt', 'Merkez', 'Nazımiye', 'Ovacık', 'Pertek', 'Pülümür'),
'63':('Akçakale', 'Birecik', 'Bozova', 'Ceylanpınar', 'Eyyübiye', 'Halfeti', 'Haliliye', 'Harran', 'Hilvan', 'Karaköprü', 'Merkez', 'Siverek', 'Suruç', 'Viranşehir'),
'64' : ('Banaz', 'Eşme', 'Karahallı', 'Merkez', 'Sivaslı', 'Ulubey'),
'65' : ('Bahçesaray', 'Başkale', 'Çaldıran', 'Çatak', 'Edremit', 'Erciş', 'Gevaş', 'Gürpınar', 'İpekyolu', 'Merkez', 'Muradiye', 'Özalp', 'Saray', 'Tuşba'), 
'66': ('Akdağmadeni', 'Aydıncık', 'Boğazlıyan', 'Çandır', 'Çayıralan', 'Çekerek', 'Kadışehri', 'Merkez', 'Saraykent', 'Sarıkaya', 'Şefaatli', 'Sorgun', 'Yenifakılı', 'Yerköy'),
'67': ('Alaplı', 'Çaycuma', 'Devrek', 'Ereğli', 'Gökçebey', 'Kilimli', 'Kozlu', 'Merkez'),
'68' : ('Ağaçören', 'Eskil', 'Gülağaç', 'Güzelyurt', 'Merkez', 'Ortaköy', 'Sarıyahşi'),
'69' : ('Aydıntepe', 'Demirözü', 'Merkez'),
'70' : ('Ayrancı', 'Başyayla', 'Ermenek', 'Kazımkarabekir', 'Merkez', 'Sarıveliler'),
'71' : ('Bahşili', 'Balışeyh', 'Çelebi', 'Delice', 'Karakeçili', 'Keskin', 'Merkez', 'Sulakyurt', 'Yahşihan'),
'72' : ('Beşiri', 'Gercüş', 'Hasankeyf', 'Kozluk', 'Merkez', 'Sason'),
'73' : ('Beytüşşebap', 'Cizre', 'Güçlükonak', 'İdil', 'Merkez', 'Silopi', 'Uludere'),
'74' : ('Abdipaşa', 'Amasra', 'Kozcağız', 'Kurucaşile' ,'Merkez', 'Ulus'),
'75': ('Çıldır', 'Damal', 'Göle', 'Hanak', 'Merkez', 'Posof'),
'76' : ('Aralık', 'Karakoyunlu', 'Merkez', 'Tuzluca'), 
'77' : ('Altınova', 'Armutlu', 'Çiftlikköy', 'Çınarcık', 'Merkez', 'Termal'),
'78' : ('Eflani', 'Eskipazar', 'Merkez', 'Ovacık', 'Safranbolu', 'Yenice'), 
'79' : ('Elbeyli', 'Merkez', 'Musabeyli', 'Polateli'), 
'80' : ('Bahçe', 'Düziçi', 'Hasanbeyli', 'Kadirli', 'Merkez', 'Sumbas', 'Toprakkale'), 
'81' : ('Akçakoca', 'Çilimli', 'Cumayeri', 'Gölyaka', 'Gümüşova', 'Kaynaşlı', 'Merkez', 'Yığılca')
}

len(sehirilce["5"])
len(sehirilce["29"])




# sehirilce = ['ADANA', 'Aladağ', 'Ceyhan', 'Çukurova', 'Feke', 'İmamoğlu', 'Karaisalı', 'Karataş', 'Kozan', 'Merkez', 'Pozantı', 'Saimbeyli', 'Salbaş', 'Sarıçam', 'Seyhan', 'Tekir', 'Test', 'Tufanbeyli', 'Yumurtalık', 'Yüreğir',
# 'ADIYAMAN', 'Besni', 'Çelikhan', 'Gerger', 'Gölbaşı', 'Kahta', 'Merkez', 'Samsat', 'Sincik', 'Tut', 
# 'AFYONKARAHISAR', 'Başmakçı', 'Bayat', 'Bolvadin', 'Çay', 'Çobanlar', 'Dazkırı', 'Dinar', 'Emirdağ', 'Evciler', 
# 'Hocalar', 'İhsaniye', 'İscehisar', 'Kızılören', 'Merkez', 'Sandıklı', 'Sinanpaşa', 'Şuhut', 'Sultandağı', 
# 'AGRI', 'Diyadin', 'Doğubayazıt', 'Eleşkirt', 'Hamur', 'Merkez', 'Patnos', 'Taşlıçay', 'Tutak', 
# 'AMASYA', 'Göynücek', 'Gümüşhacıköy', 'Hamamözü', 'Merkez', 'Merzifon', 'Suluova', 'Taşova', 
# 'ANKARA', 'Akyurt', 'Altındağ', 'Ayaş', 'Bala', 'Beypazarı', 'Çamlıdere', 'Çankaya', 'Çubuk', 'Elmadağ', 'Etimesgut', 'Evren', 'Gölbaşı', 'Güdül', 'Haymana', 'Kahramankazan', 'Kalecik', 'Kazan', 'Keçiören', 'Kızılcahamam', 'Mamak', 'Merkez', 'Nallıhan', 'Polatlı', 'Pursaklar', 'Şereflikoçhisar', 'Sincan', 'Yenimahalle', 
# 'ANTALYA', 'Akseki', 'Aksu', 'Alanya', 'Demre', 'Döşemealtı', 'Elmalı', 'Finike', 'Gazipaşa', 'Gündoğmuş', 'İbradı', 'Kaş', 'Kemer', 'Kepez', 'Konyaaltı', 'Korkuteli', 'Kumluca', 'Manavgat', 'Merkez', 'Muratpaşa', 'Serik', 
# 'ARTVIN', 'Ardanuç', 'Arhavi', 'Borçka', 'Hopa', 'Kemalpaşa', 'Merkez', 'Murgul', 'Şavşat', 'Yusufeli', 
# 'AYDIN', 'Acarlar', 'Akbük', 'Akçaova', 'Altınkum', 'Atça', 'Bağarası', 'Bozdoğan', 'Buharkent', 'Çine', 'Davutlar', 'Didim', 'Efeler', 'Germencik', 'Güzelçamlı', 'İncirliova', 'Karacasu', 'Karpuzlu', 'Koçarlı', 'Köşk', 'Kuşadası','Kuyucak', 'Merkez', 'Nazilli', 'Ortaklar', 'Pamukören', 'Söke', 'Sultanhisar', 'Umurlu', 'Yenipazar', 
# 'BALIKESIR', 'Akçay', 'Altıeylül', 'Altınoluk', 'Altınova', 'Ayvalık', 'Balya', 'Bandırma', 'Bigadiç', 'Burhaniye', 'Dursunbey', 'Edremit', 'Erdek', 'Gömeç', 'Gönen', 'Havran', 'İvrindi', 'Kadıköy', 'Karesi', 'Kepsut', 'Manyas', 'Marmara', 'Merkez', 'Sarımsaklı', 'Savaştepe', 'Sındırgı', 'Susurluk',
# 'BILECIK', 'Bozüyük', 'Gölpazarı', 'İnhisar', 'Merkez', 'Osmaneli', 'Pazaryeri', 'Söğüt', 'Yenipazar', 
# 'BINGOL', 'Adaklı', 'Genç', 'Karlıova', 'Kiğı', 'Merkez', 'Solhan', 'Yayladere', 'Yedisu', 
# 'BITLIS', 'Adilcevaz', 'Ahlat', 'Güroymak','Hizan', 'Merkez', 'Mutki', 'Tatvan',
# 'BOLU', 'Dörtdivan', 'Gerede', 'Göynük', 'Kıbrıscık', 'Mengen', 'Merkez', 'Mudurnu', 'Seben', 'Yeniçağa', 'BURDUR', 'Ağlasun', 'Altınyayla', 'Bucak', 'Çavdır', 'Çeltikçi', 'Gölhisar', 'Karamanlı', 'Kemer', 'Merkez', 'Tefenni', 'Yeşilova', 
# 'BURSA', 'Büyükorhan', 'Gemlik', 'Gürsu', 'Harmancık', 'İnegöl', 'İznik', 'Karacabey', 'Keles', 'Kestel', 'Merkez', 'Mudanya', 'Mustafakemalpaşa', 'Nilüfer', 'Orhaneli', 'Orhangazi', 'Osmangazi', 'Yenişehir', 'Yıldırım', 
# 'CANAKKALE', 'Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Çardak', 'Eceabat', 'Ezine', 'Gelibolu', 'Geyikli', 'Gökçeada', 'Küçükkuyu', 'Lapseki', 'Merkez', 'Yenice', 
# 'CANKIRI', 'Atkaracalar', 'Bayramören', 'Çerkeş', 'Eldivan', 'Ilgaz', 'Kızılırmak', 'Korgun', 'Kurşunlu', 'Merkez', 'Orta', 'Şabanözü', 'Yapraklı', 
# 'CORUM', 'Alaca', 'Bayat', 'Boğazkale', 'Dodurga', 'İskilip', 'Kargı', 'Laçin', 'Mecitözü', 'Merkez', 'Oğuzlar', 'Ortaköy', 'Osmancık', 'Sungurlu', 'Uğurludağ',
# 'DENIZLI', 'Acıpayam', 'Akköy', 'Babadağ', 'Baklan', 'Bekilli', 'Beyağaç', 'Bozkurt', 'Buldan', 'Çal', 'Çameli', 'Çardak', 'Çivril', 'Güney', 'Honaz', 'Kale', 'Merkez', 'Merkezefendi', 'Pamukkale', 'Sarayköy', 'Serinhisar', 'Tavas', 
# 'DIYARBAKIR', 'Bağlar', 'Bismil', 'Çermik', 'Çınar', 'Çüngüş', 'Dicle', 'Eğil', 'Ergani', 'Hani', 'Hazro', 'Kayapınar', 'Kocaköy', 'Kulp', 'Lice', 'Merkez', 'Silvan', 'Sur', 'Yenişehir', 
# 'EDIRNE', 'Enez', 'Havsa', 'İpsala', 'Keşan', 'Lalapaşa', 'Meriç', 'Merkez', 'Süloğlu', 'Uzunköprü', 
# 'ELAZIG', 'Ağın', 'Alacakaya', 'Arıcak', 'Baskil', 'Karakoçan', 'Keban', 'Kovancılar', 'Maden', 'Merkez', 'Palu', 'Sivrice', 
# 'ERZINCAN', 'Çayırlı', 'İliç', 'Kemah', 'Kemaliye', 'Merkez', 'Otlukbeli', 'Refahiye', 'Tercan', 'Üzümlü', 
# 'ERZURUM', 'Aşkale', 'Aziziye', 'Çat', 'Hınıs', 'Horasan', 'İspir', 'Karaçoban', 'Karayazı', 'Köprüköy', 'Merkez', 'Narman', 'Oltu', 'Olur', 'Palandöken', 'Pasinler', 'Pazaryolu', 'Şenkaya', 'Tekman', 'Tortum', 'Uzundere', 'Yakutiye', 
# 'ESKISEHIR', 'Alpu', 'Beylikova', 'Çifteler', 'Günyüzü', 'Han', 'İnönü', 'Mahmudiye', 'Merkez', 'Mihalgazi', 'Mihalıcçık', 'Odunpazarı', 'Sarıcakaya', 'Seyitgazi', 'Sivrihisar', 'Tepebaşı', 
# 'GAZIANTEP', 'Araban', 'İslahiye', 'Karkamış', 'Merkez', 'Nizip', 'Nurdağı', 'Oğuzeli', 'Şahinbey', 'Şehitkamil', 'Yavuzeli', 
# 'GIRESUN', 'Alucra', 'Bulancak', 'Çamoluk', 'Çanakçı', 'Dereli', 'Doğankent', 'Espiye', 'Eynesil', 'Görele', 'Güce', 'Keşap', 'Merkez', 'Piraziz', 'Şebinkarahisar', 'Tirebolu', 'Yağlıdere', 
# 'GUMUSHANE', 'Kelkit', 'Köse', 'Kürtün', 'Merkez', 'Şiran', 'Torul', 
# 'HAKKARI', 'Çukurca', 'Merkez', 'Şemdinli', 'Yüksekova', 
# 'HATAY', 'Altınözü', 'Antakya','Arsuz','Belen','Defne','Dörtyol','Erzin', 'Hassa','İskenderun','Kırıkhan', 'Kumlu', 'Merkez', 'Payas','Reyhanlı', 'Samandağ', 'Yayladağı', 
# 'ISPARTA', 'Aksu', 'Atabey', 'Eğirdir', 'Gelendost', 'Gönen', 'Keçiborlu', 'Merkez', 'Şarkikaraağaç', 'Senirkent', 'Sütçüler', 'Uluborlu', 'Yalvaç', 'Yenişarbademli', 
# 'MERSIN', 'Akdeniz', 'Anamur', 'Aydıncık', 'Bozyazı', 'Çamlıyayla', 'Erdemli', 'Gülnar', 'Merkez', 'Mezitli', 'Mut', 'Silifke', 'Tarsus', 'Toroslar', 'Yenişehir',
# 'ISTANBUL', 'Adalar', 'Arnavutköy', 'Ataşehir', 'Avcılar', 'Bağcılar', 'Bahçelievler', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beşiktaş', 'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca', 'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüp', 'Fatih', 'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kağıthane', 'Kartal', 'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe', 'Sarıyer', 'Şile', 'Silivri', 'Şişli', 'Sultanbeyli', 'Sultangazi', 'Tuzla', 'Ümraniye', 'Üsküdar', 'Zeytinburnu', 
# 'IZMIR', 'Aliağa', 'Alsancak', 'Ayrancılar', 'Balçova', 'Bayındır', 'Bayraklı', 'Bergama', 'Beydağ', 'Bornova', 'Buca', 'Çeşme', 'Çiğli', 'Dikili', 'Foça', 'Gaziemir', 'Güzelbahçe', 'Karabağlar', 'Karaburun', 'Karşıyaka', 'Kemalpaşa', 'Kiraz', 'Kınık', 'Konak', 'Menderes', 'Menemen', 'Merkez', 'Narlıdere', 'Ödemiş', 'Seferihisar', 'Selçuk', 'Tire', 'Torbalı', 'Urla', 
# 'KARS', 'Akyaka', 'Arpaçay', 'Digor', 'Kağızman', 'Merkez', 'Sarıkamış', 'Selim', 'Susuz', 
# 'KASTAMONU', 'Abana', 'Ağlı', 'Araç', 'Azdavay', 'Bozkurt', 'Çatalzeytin', 'Cide', 'Daday', 'Devrekani', 'Doğanyurt', 'Hanönü', 'İhsangazi', 'İnebolu', 'Küre', 'Merkez', 'Pınarbaşı', 'Şenpazar', 'Seydiler', 'Taşköprü', 'Tosya', 
# 'KAYSERI', 'Akkışla', 'Bünyan', 'Develi', 'Felahiye', 'Hacılar', 'İncesu', 'Kocasinan', 'Melikgazi', 'Merkez', 'Özvatan', 'Pınarbaşı', 'Sarıoğlan', 'Sarız', 'Talas', 'Tomarza', 'Yahyalı', 'Yeşilhisar'
# 'KIRKLARELI', 'Alpullu', 'Babaeski', 'Büyükkarıştıran', 'Büyükmandıra', 'Demirköy', 'Kofçaz', 'Lüleburgaz', 'Merkez', 'Pehlivanköy', 'Pınarhisar', 'Vize'
# 'KIRSEHIR', 'Akçakent', 'Akpınar', 'Boztepe', 'Çiçekdağı', 'Kaman', 'Merkez', 'Mucur'
# 'KOCAELI', 'Başiskele', 'Çayırova','Darıca', 'Derince', 'Dilovası', 'Gebze', 'Gölcük', 'İzmit', 'Kandıra', 'Karamürsel', 'Kartepe', 'Körfez', 'Merkez',
# 'KONYA', 'Ahırlı', 'Akören', 'Akşehir', 'Altınekin', 'Beyşehir', 'Bozkır', 'Çeltik', 'Cihanbeyli', 'Çumra', 'Derbent', 'Derebucak', 'Doğanhisar', 'Emirgazi', 'Ereğli', 'Güneysınır', 'Hadim', 'Halkapınar', 'Hüyük', 'Ilgın', 'Kadınhanı', 'Karapınar', 'Karatay', 'Kulu', 'Meram', 'Merkez', 'Sarayönü', 'Selçuklu', 'Seydişehir', 'Taşkent', 'Tuzlukçu', 'Yalıhüyük', 'Yunak'
# 'KUTAHYA', 'Altıntaş', 'Aslanapa', 'Çavdarhisar', 'Domaniç', 'Dumlupınar', 'Emet', 'Gediz', 'Hisarcık', 'Merkez', 'Pazarlar', 'Şaphane', 'Simav', 'Tavşanlı'
# 'MALATYA', 'Akçadağ', 'Arapgir', 'Arguvan', 'Battalgazi', 'Darende', 'Doğanşehir', 'Doğanyol', 'Hekimhan', 'Kale', 'Kuluncak', 'Merkez', 'Pütürge', 'Yazıhan', 'Yeşilyurt'
# 'MANISA', 'Ahmetli', 'Akhisar', 'Alaşehir', 'Demirci', 'Gölmarmara', 'Gördes', 'Kırkağaç', 'Köprübaşı', 'Kula', 'Merkez', 'Salihli', 'Sarıgöl', 'Saruhanlı', 'Şehzadeler', 'Selendi', 'Soma', 'Turgutlu', 'Yunusemre'
# 'KAHRAMANMARAS', 'Afşin', 'Andırın', 'Çağlayancerit', 'Dulkadiroğlu', 'Ekinözü', 'Elbistan', 'Göksun', 'Merkez', 'Nurhak', 'Onikişubat', 'Pazarcık', 'Türkoğlu'
# 'MARDIN', 'Artuklu', 'Dargeçit', 'Derik', 'Kızıltepe', 'Mazıdağı', 'Merkez', 'Midyat', 'Nusaybin', 'Ömerli', 'Savur', 'Yeşilli'
# 'MUGLA', 'Bodrum', 'Dalaman', 'Datça', 'Fethiye', 'Kavaklıdere', 'Köyceğiz', 'Marmaris', 'Menteşe', 'Merkez', 'Milas', 'Ortaca', 'Seydikemer', 'Ula', 'Yatağan'
# 'MUS', 'Bulanık', 'Hasköy', 'Korkut', 'Malazgirt', 'Merkez', 'Varto'
# 'NEVSEHIR', 'Acıgöl', 'Avanos', 'Derinkuyu', 'Gülşehir', 'Hacıbektaş', 'Kozaklı', 'Merkez', 'Ürgüp', 'NIGDE', 'Altunhisar', 'Bor', 'Çamardı', 'Çiftlik', 'Merkez', 'Ulukışla'
# 'ORDU', 'Akkuş', 'Altınordu', 'Aybastı', 'Çamaş', 'Çatalpınar', 'Çaybaşı', 'Fatsa', 'Gölköy', 'Gülyalı', 'Gürgentepe', 'İkizce', 'Kabadüz', 'Kabataş', 'Korgan', 'Kumru', 'Merkez', 'Mesudiye', 'Perşembe', 'Ulubey', 'Ünye'
# 'RIZE', 'Ardeşen', 'Çamlıhemşin', 'Çayeli', 'Derepazarı', 'Fındıklı', 'Güneysu', 'Hemşin', 'İkizdere', 'İyidere', 'Kalkandere', 'Merkez', 'Pazar'
# 'SAKARYA', 'Adapazarı', 'Akyazı', 'Arifiye', 'Erenler', 'Ferizli', 'Geyve', 'Hendek', 'Karapürçek', 'Karasu', 'Kaynarca', 'Kocaali', 'Merkez', 'Pamukova', 'Sapanca', 'Serdivan', 'Söğütlü', 'Taraklı'
# 'SAMSUN', 'Alaçam', 'Asarcık', 'Atakum', 'Ayvacık', 'Bafra', 'Canik', 'Çarşamba', 'Havza', 'İlkadım', 'Kavak', 'Ladik', 'Merkez', 'Ondokuzmayıs', 'Salıpazarı', 'Tekkeköy', 'Terme', 'Vezirköprü', 'Yakakent'
# 'SIIRT', 'Baykan', 'Eruh', 'Kurtalan', 'Merkez', 'Pervari', 'Şirvan', 'Tillo', 'SINOP', 'Ayancık', 'Boyabat', 'Dikmen', 'Durağan', 'Erfelek', 'Gerze', 'Merkez', 'Saraydüzü', 'Türkeli'
# 'SIVAS', 'Akıncılar', 'Altınyayla', 'Divriği', 'Doğanşar', 'Gemerek', 'Gölova', 'Gürün', 'Hafik', 'İmranlı', 'Kangal', 'Koyulhisar', 'Merkez', 'Şarkışla', 'Suşehri', 'Ulaş', 'Yıldızeli', 'Zara'
# 'TEKIRDAG', 'Çerkezköy', 'Çorlu', 'Ergene', 'Hayrabolu', 'Kapaklı', 'Malkara', 'Marmaraereğlisi', 'Merkez', 'Muratlı', 'Saray', 'Şarköy', 'Süleymanpaşa'
# 'TOKAT', 'Almus', 'Artova', 'Başçiftlik', 'Erbaa', 'Merkez', 'Niksar', 'Pazar', 'Reşadiye', 'Sulusaray', 'Turhal', 'Yeşilyurt', 'Zile'
# 'TRABZON', 'Akçaabat', 'Araklı', 'Arsin', 'Beşikdüzü', 'Çarşıbaşı', 'Çaykara', 'Dernekpazarı', 'Düzköy', 'Hayrat', 'Köprübaşı', 'Maçka', 'Merkez', 'Of', 'Ortahisar', 'Şalpazarı', 'Sürmene', 'Tonya', 'Vakfıkebir', 'Yomra'
# 'TUNCELI', 'Çemişgezek', 'Hozat', 'Mazgirt', 'Merkez', 'Nazımiye', 'Ovacık', 'Pertek', 'Pülümür'
# 'SANLIURFA', 'Akçakale', 'Birecik', 'Bozova', 'Ceylanpınar', 'Eyyübiye', 'Halfeti', 'Haliliye', 'Harran', 'Hilvan', 'Karaköprü', 'Merkez', 'Siverek', 'Suruç', 'Viranşehir'
# 'USAK', 'Banaz', 'Eşme', 'Karahallı', 'Merkez', 'Sivaslı', 'Ulubey'
# 'VAN', 'Bahçesaray', 'Başkale', 'Çaldıran', 'Çatak', 'Edremit', 'Erciş', 'Gevaş', 'Gürpınar', 'İpekyolu', 'Merkez', 'Muradiye', 'Özalp', 'Saray', 'Tuşba', 
# 'YOZGAT', 'Akdağmadeni', 'Aydıncık', 'Boğazlıyan', 'Çandır', 'Çayıralan', 'Çekerek', 'Kadışehri', 'Merkez', 'Saraykent', 'Sarıkaya', 'Şefaatli', 'Sorgun', 'Yenifakılı', 'Yerköy'
# 'ZONGULDAK', 'Alaplı', 'Çaycuma', 'Devrek', 'Ereğli', 'Gökçebey', 'Kilimli', 'Kozlu', 'Merkez'
# 'AKSARAY', 'Ağaçören', 'Eskil', 'Gülağaç', 'Güzelyurt', 'Merkez', 'Ortaköy', 'Sarıyahşi'
# 'BAYBURT', 'Aydıntepe', 'Demirözü', 'Merkez',
# 'KARAMAN', 'Ayrancı', 'Başyayla', 'Ermenek', 'Kazımkarabekir', 'Merkez', 'Sarıveliler',
# 'KIRIKKALE', 'Bahşili', 'Balışeyh', 'Çelebi', 'Delice', 'Karakeçili', 'Keskin', 'Merkez', 'Sulakyurt', 'Yahşihan', 
# 'BATMAN', 'Beşiri', 'Gercüş', 'Hasankeyf', 'Kozluk', 'Merkez', 'Sason',
# 'SIRNAK', 'Beytüşşebap', 'Cizre', 'Güçlükonak', 'İdil', 'Merkez', 'Silopi', 'Uludere',
# 'BARTIN', 'Abdipaşa', 'Amasra', 'Kozcağız', 
# 'Kurucaşile', 'Merkez', 'Ulus', 
# 'ARDAHAN', 'Çıldır', 'Damal', 'Göle', 'Hanak', 'Merkez', 'Posof',
# 'IGDIR', 'Aralık', 'Karakoyunlu', 'Merkez', 'Tuzluca', 
# 'YALOVA', 'Altınova', 'Armutlu', 'Çiftlikköy', 'Çınarcık', 'Merkez', 'Termal',
# 'KARABUK', 'Eflani', 'Eskipazar', 'Merkez', 'Ovacık', 'Safranbolu', 'Yenice', 
# 'KILIS', 'Elbeyli', 'Merkez', 'Musabeyli', 'Polateli', 
# 'OSMANIYE', 'Bahçe', 'Düziçi', 'Hasanbeyli', 'Kadirli', 'Merkez', 'Sumbas', 'Toprakkale', 
# 'DUZCE', 'Akçakoca', 'Çilimli', 'Cumayeri', 'Gölyaka', 'Gümüşova', 'Kaynaşlı', 'Merkez', 'Yığılca']



# ililce["data"][0]["il_adi"]
# len(ililce["data"])

# for i in range(0,len(ililce["data"])):
#     for j in range(0 , len(ililce["data"][i]["ilceler"])):
#         print(ililce["data"][i]["ilceler"][j]["ilce_adi"])




# len(ililce["data"][0]["ilceler"])
# len(ililce["data"][1]["ilceler"])