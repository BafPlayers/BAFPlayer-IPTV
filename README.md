# BAF IPTV Player - Yasal ve Ücretsiz Küresel İçerik Kütüphanesi

Bu dizin, **BAF IPTV Player** uygulamasında doğrudan kullanılabilecek, dünyanın her yerinden derlenmiş, tamamen yasal, telifsiz ve kamu malı (public domain / Creative Commons) içeriklerin devasa bir kütüphanesini içerir.

Tüm canlı yayınlar, radyo istasyonları, podcast ses akışları ve filmler otomatik doğrulama araçları ile kontrol edilmiş, bağlantıların aktif ve oynatılabilir olduğu doğrulanmıştır.

---

## 📂 Master Çalma Listesi ve Dosya Yapısı

Kullanıcıların içerik kütüphanesini kolayca yükleyebilmesi için tüm içerikler tek bir **Master Playlist** dosyasında birleştirilmiş ve aynı zamanda kategori bazlı ayrı M3U çalma listeleri halinde de sunulmuştur:

### 1. 📋 Master Oynatma Listesi
*   **[Library.m3u](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Library.m3u)**: Kütüphanedeki **tüm 1238 içeriği** (Canlı TV, Radyo, Film ve Dizi) tek bir dosyada toplayan ana oynatma listesi. Bu dosyayı IPTV oynatıcınıza yüklediğinizde içerikler otomatik olarak aşağıdaki kategorilere ayrılacaktır:
    *   `Canlı TV - [Ülke Adı]` (Live TV by Country)
    *   `Radyo` (Web Radio)
    *   `Film` (Movies & Scenic Loops)
    *   `Dizi` (Serialized Cartoons & Podcasts)

### 2. 📺 Canlı TV Kanalları (Ülkelere Göre Gruplanmış)
*   **[IPTV_Channels.m3u](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/IPTV_Channels.m3u)**: Dünya genelinden **1008 adet** yasal canlı TV kanalını barındıran çalma listesi. Oynatıcıda kolayca gizlenebilmesi veya filtrelenebilmesi için ülkelere göre gruplanmıştır (Örn: `group-title="Canlı TV - Türkiye"`, `group-title="Canlı TV - ABD"`, `group-title="Canlı TV - İngiltere"` vb.).
*   **[IPTV_Channels.txt](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/IPTV_Channels.txt)**: Tüm canlı kanalların adlarını, ülkelerini ve akış bağlantılarını listeleyen devasa metin belgesi.

### 3. 📻 İnternet Radyoları
*   **[Web_Radios.m3u](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Web_Radios.m3u)**: SomaFM, BBC, TRT ve diğer küresel yayıncılardan **40 adet** aktif radyo istasyonunu barındıran çalma listesi. (`group-title="Radyo"`)
*   **[Web_Radios.txt](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Web_Radios.txt)**: Radyo kanallarının tarzlarını, açıklamalarını ve ses akış linklerini listeleyen metin belgesi.

### 4. 🎬 Tek Bölümlük İçerikler (Filmler ve Doğa Döngüleri)
*   **[Movies.m3u](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Movies.m3u)**: Kamu malı sinema başyapıtları, bağımsız kısa filmler, uzay belgeselleri ve 4K doğa/stok video döngülerinden oluşan **34 adet** tekil video içeriği. (`group-title="Film"`)
*   **[Movies_And_Series.json](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Movies_And_Series.json)**: Filmlerin afiş görselleri, açıklamaları, çıkış yılları, türleri ve dosya boyutu gibi teknik meta verilerini barındıran JSON veritabanı.
*   **[Movies_And_Series.txt](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Movies_And_Series.txt)**: Filmleri kolay okunabilir formatta listeleyen metin belgesi.

### 5. 🎙️ Seri / Bölümlü İçerikler (Diziler ve Podcast'ler)
*   **[Series.m3u](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Series.m3u)**: Sürekli bölümleri ve serisi olan içeriklerin (klasik çizgi filmler ve en güncel podcast bölümleri) toplandığı **156 adet** bölümlük çalma listesi. (`group-title="Dizi"`)
*   **[Podcasts.json](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Podcasts.json)**: 15 popüler podcast serisinin en güncel 10'ar bölümünün (Toplam 147 aktif bölüm) başlıklarını, açıklamalarını, logolarını ve yayın tarihlerini tutan JSON veritabanı.
*   **[Podcasts.txt](file:///C:/Users/cagri/Source/Repos/BAFIPTVPlayer/IPTV Content/Podcasts.txt)**: Podcast bölümlerini gösteren metin belgesi.

---

## 📺 Kütüphane İçerik Ayrıntıları

### 1. Canlı TV Kanalları (Canlı TV - 1008 Kanal)
*   **Türkiye (100 Kanal)**: TRT Haber, TRT Spor, TRT Belgesel, TRT Müzik, TRT Çocuk, ulusal kanallar ve yerel/bölgesel canlı yayınlar.
*   **ABD & İngiltere (160+ Kanal)**: Haber, eğlence, klasik sinema, hava durumu ve teknoloji odaklı geniş İngilizce kanal seçeneği.
*   **Avrupa (Almanya, Fransa, İtalya, İspanya - 300+ Kanal)**: DW, France 24, TV5 Monde, Rai ve diğer büyük Avrupalı kamu ve özel yasal HLS yayıncıları.
*   **Uluslararası Seçki**: Azerbaycan, Brezilya, Japonya, Güney Kore, Çin, Hollanda, İsviçre vb. ülkelerden derlenmiş yasal yayın akışları.

### 2. Dünya Radyoları (Radyo - 40 İstasyon)
*   **TRT Radyoları**: TRT FM, TRT Radyo 1, TRT Radyo 3, TRT Türkü.
*   **BBC Radio Grubu**: BBC World Service, BBC Radio 1, BBC Radio 2, BBC Radio 3.
*   **SomaFM (ABD)**: 20+ bağımsız tematik chillout, ambient, lounge, dub, indie pop ve synthpop radyoları (Groove Salad, Lush, Space Station, Drone Zone, Dub Step Beyond, Covers, DEF CON vb.).
*   **Uluslararası Seçkinler**: WQXR Classical (New York), Jazz24 (Seattle), Swiss Jazz, Swiss Classic, Swiss Pop, Rai Radio 3 (İtalya), RFI Monde (Fransa), Antenne Bayern Chillout (Almanya).

### 3. Klasik Filmler & Doğa Döngüleri (Film - 34 İçerik)
*   **Sinema Başyapıtları**: *Night of the Living Dead* (1968), *His Girl Friday* (1940), *The General* (1926), *Nosferatu* (1922), *Carnival of Souls* (1962), *My Favorite Brunette* (1947), *Steamboat Bill, Jr.* (1928), *A Trip to the Moon* (1902), *Sherlock Holmes: Dressed to Kill* (1946).
*   **Avangart ve Kült Klasikler**: *Un Chien Andalou* (Fransa, 1929), *Man with a Movie Camera* (SSCB, 1929), *Battleship Potemkin* (SSCB, 1925), *The Cabinet of Dr. Caligari* (Almanya, 1920), *Rain (Regen)* (1929), *The Lost World* (1925), *Berlin: Symphony of a Great City* (1927), *Kids Auto Race At Venice* (Charlie Chaplin'in ilk Tramp rolü - 1914), *Plan 9 from Outer Space* (1957), *Secret Agent* (Hitchcock - 1936).
*   **Uzay Belgeselleri**: NASA ISS Laminar Flow Fluid Mechanics, Apollo 11 Onboard 16mm Film.
*   **Açık Kaynak Animasyonlar (Blender Open Movies)**: 
    *   *Sintel (2010)* - Ejderhasını arayan bir kızın fantastik hikayesi.
    *   *Tears of Steel (2012)* - Distopik Amsterdam'da geçen görsel efektli vfx kısa filmi.
    *   *Elephants Dream (2006)* - Sinema tarihinin ilk açık kaynaklı 3D animasyon kısa filmi.
    *   *Big Buck Bunny (2008)* - Orman canlılarından intikam alan dev tavşanın komik animasyonu.
    *   *Cosmos Laundromat: First Cycle (2015)* - Farklı dünyalara ışınlanan Franck adındaki koyunun bol ödüllü fantastik hikayesi.
    *   *Caminandes 1: Llama Drama (2013)* - Patagonia'da komik bir lamanın meyve arayışı.
    *   *Caminandes 2: Gran Dillama (2013)* - Elektrik teline takılan lamanın komik mücadelesi.
    *   *Caminandes 3: Llamigos (2016)* - Lamanın penguenle yemek paylaşma mücadelesi.
    *   *Sita Sings the Blues (ABD, 2008)* - Bol ödüllü bağımsız müzikal animasyon uzun metraj film.
*   **Ortam Döngüleri & Manzaralar**: Cozy Glen Lake Fireplace Loop, San Francisco in Cinemascope (1955), Park Conscious (1938 Scenic Loop).

### 4. Seri Çizgi Filmler & Podcast'ler (Dizi - 156 İçerik)
*   **Seri Çizgi Filmler (Classic Cartoons)**: Superman (1941 Fleischer Studios serisinden *The Mad Scientist*, *The Mechanical Monsters*, *Billion Dollar Limited* bölümleri), Bugs Bunny (*The Wabbit Who Came to Supper*, *A Corny Concerto*), Popeye (*Ali Baba*, *Sindbad*), Betty Boop (*Poor Cinderella*), Gulliver's Travels.
*   **Podcast Yayınları (15 Popüler Seri, En Güncel 10'ar Bölüm - 147 Bölüm)**:
    1.  *NASA's Curious Universe* (Uzay & Bilim)
    2.  *Science Vs (Gimlet)* (Bilim & Popüler Kültür)
    3.  *Astronomy Cast (Libsyn)* (Astronomik Bilimler)
    4.  *NPR Short Wave* (Hap Bilgilerle Bilim)
    5.  *The History of Rome* (Roma Tarihi Belgeseli)
    6.  *Philosophize This! (Stephen West)* (Derin Felsefe & Düşünürler)
    7.  *BBC In Our Time* (Felsefe, Bilim ve Tarih Tartışmaları)
    8.  *Lore (Aaron Mahnke)* (Tarihsel Efsaneler & Folklor)
    9.  *Dan Carlin's Hardcore History (Common Sense)* (Derin Siyasi & Tarihsel Bakış)
    10. *NPR Planet Money* (Eğlenceli Ekonomi Hikayeleri)
    11. *How I Built This with Guy Raz* (Girişimcilerin Başarı Öyküleri)
    12. *TED Radio Hour* (Zihin Açıcı Fikirler Belgeseli)
    13. *Lex Fridman Podcast* (AI, Bilim ve Kültür Röportajları)
    14. *The Tim Ferriss Show* (Performans & Başarı Taktikleri)
    15. *The Daily (New York Times)* (Günlük Küresel Analizler)

---

## 🛠️ Nasıl Test Edilir ve Kullanılır?

1.  **VLC veya Herhangi Bir IPTV Oynatıcı ile İzleme**:
    *   `Library.m3u` dosyasını VLC Media Player, Tivimate, IPTV Smarters Pro veya herhangi bir IPTV istemcisine sürükleyip bırakarak (veya URL olarak ekleyerek) anında izleyebilirsiniz.
2.  **BAF Player Entegrasyonu**:
    *   **Canlı TV ve Radyo Grupları**: `IPTV_Channels.m3u` ve `Web_Radios.m3u` oynatma listeleri doğrudan uygulamanın IPTV listelerine beslenebilir.
    *   **Dizi ve Film Oynatma**: `Series.m3u` ve `Movies.m3u` listeleriyle bölümlü dizileri ve tekli filmleri uygulamanın video oynatıcısında sırasıyla "Dizi" ve "Film" arayüz kategorilerinde gösterebilirsiniz.
    *   **Zengin Meta Veri Entegrasyonu**: Uygulamanın veritabanına zengin veri çekmek için `Movies_And_Series.json` ve `Podcasts.json` veritabanı dosyalarından doğrudan faydalanabilirsiniz.

*Not: Bu kütüphane resmi ve kamu malı kaynaklardan beslendiği için tamamen telifsiz, yasal ve güvenlidir. İnternet hızınıza bağlı olarak yayınların yüklenme süreleri değişiklik gösterebilir.*
