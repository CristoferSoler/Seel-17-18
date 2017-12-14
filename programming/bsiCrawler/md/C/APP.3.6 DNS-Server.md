1 Beschreibung
--------------

### 1.1 Einleitung

In diesem Baustein werden die grundsätzlichen Sicherheitseigenschaften des Domain Name System (DNS) und der hierfür benötigten Server betrachtet. DNS ist ein Netzdienst, der dazu eingesetzt wird, Hostnamen von IT-Systemen in IP-Adressen umzuwandeln. Üblicherweise wird zu einem Hostnamen die entsprechende IP-Adresse gesucht (Vorwärtsauflösung). Ist hingegen die IP-Adresse bekannt und der Hostname wird gesucht, wird dies als Rückwärtsauflösung bezeichnet. DNS kann mit einem Telefonbuch verglichen werden, das Namen nicht in Telefonnummern, sondern in IP-Adressen auflöst. Welche Namen zu welchen IP-Adressen gehören, wird im Domain-Namensraum verwaltet. Dieser ist hierarchisch aufgebaut und wird von DNS-Servern zur Verfügung gestellt. DNS-Server verwalten den Domain-Namensraum im Internet, werden aber auch häufig im internen Netz der Institution eingesetzt. Auf den Rechnern der Benutzer sind standardmäßig sogenannte Resolver installiert, über die Anfragen an DNS-Server gestellt werden und die als Antwort Informationen über den Domain-Namensraum zurückliefern. Die Bezeichnung DNS-Server steht im eigentlichen Sinne für die verwendete Software, wird jedoch meist auch als Synonym für den Rechner benutzt, auf dem diese Software betrieben wird.

DNS-Server können nach ihren Aufgaben unterschieden werden, dabei gibt es grundsätzlich zwei verschiedenen Typen: Advertising DNS-Server und Resolving DNS-Server. Advertising DNS-Server sind üblicherweise dafür zuständig, Anfragen aus dem Internet zu verarbeiten. Resolving DNS-Server hingegen verarbeiten Anfragen aus dem internen Netz. 

Ein Ausfall eines DNS-Servers kann sich gravierend auf den Betrieb einer IT-Infrastruktur auswirken. Dabei ist nicht direkt das ausgefallene DNS-System problematisch, sondern die daraus resultierende Einschränkung DNS-basierter Dienste. Unter Umständen sind Webserver, E-Mail-Server nicht mehr erreichbar und die Fernwartung funktioniert nicht mehr. Da DNS von sehr vielen Netzanwendungen benötigt wird, müssen laut Spezifikation (RFC 1034) mindestens zwei autoritative DNS-Server (Advertising DNS-Server) für jede Zone betrieben werden.

### 1.2 Zielsetzung

In diesem Baustein werden die für einen DNS-Server spezifischen Gefährdungen und die sich daraus ergebenden Anforderungen für einen sicheren Betrieb beschrieben. 

### 1.3 Abgrenzung

Der vorliegende Baustein enthält grundsätzliche Anforderungen, die zu beachten und zu erfüllen sind, wenn eine Institution DNS-Server betreibt. Der Fokus liegt dabei auf der Verfügbarkeit von DNS-Servern, der Integrität der übertragenen Informationen sowie auf Problemen, die auftreten können, wenn DNS-Server betrieben werden. Allgemeine und betriebssystemspezifische Aspekte eines Servers sind jedoch nicht Gegenstand des vorliegenden Bausteins, sondern werden im Baustein SYS1.1. *Allgemeiner Server* und in den entsprechenden betriebssystemspezifischen Bausteinen der Schicht IT-Systeme behandelt, z. B. SYS.1.3 *Unix-Server* oder SYS.1.2.2 *Windows Server 2012*. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für DNS-Server von besonderer Bedeutung:

### 2 1 Ausfall des DNS-Servers

Fällt ein DNS-Server aus, kann der gesamte IT-Betrieb hiervon betroffen sein. Da Clients und andere Server der Institution dann nicht mehr in der Lage sind interne und externe Adressen aufzulösen, können keine Datenverbindungen mehr aufgebaut werden. Auch externe IT-Systeme, z. B. von mobilen Mitarbeitern, Kunden und Geschäftspartnern, können nicht auf die Server der Institution zugreifen, wodurch in der Regel essenzielle Geschäftsprozesse gestört sind.

### 2 2 Unzureichende Leitungskapazitäten

Reichen die Leitungskapazitäten für einen DNS-Server nicht aus, können sich die Zugriffszeiten auf interne und externe Dienste erhöhen. Dadurch sind diese eventuell nur eingeschränkt oder gar nicht mehr nutzbar. Auch können Angreifer den DNS-Server dann leichter durch einen Denial-of-Service-(DoS)-Angriff überlasten.

### 2 3 Fehlende oder unzureichende Planung des DNS-Einsatzes

Planungsfehler stellen sich oft als besonders schwerwiegend heraus, da leicht flächendeckende Sicherheitslücken geschaffen werden können. Wird der DNS-Einsatz nicht oder nur unzureichend geplant, kann dies zu Problemen und Sicherheitslücken im laufenden Betrieb führen. Sind beispielsweise die Firewall-Regeln, um DNS-Verkehr im Netz zu ermöglichen, zu freizügig definiert, kann dies unter Umständen einen Angriff ermöglichen. Sind die Regeln jedoch zu restriktiv formuliert, können legitime Clients keine Anfragen an die DNS-Server stellen und werden beeinträchtigt, wenn sie Dienste wie E-Mail, FTP oder Ähnlichem benutzen.

### 2 4 Fehlerhafte Domain-Informationen

Selbst wenn der DNS-Einsatz sorgfältig geplant und somit alle sicherheitsrelevanten Punkte berücksichtigt wurden, ist das nicht ausreichend, wenn semantisch und/oder syntaktisch fehlerhafte Domain-Informationen erstellt werden. Beispielsweise, wenn einem Hostnamen eine falsche IP-Adresse zugeordnet wird, Daten fehlen oder nicht erlaubte Zeichen verwendet werden oder die Vorwärts- und Rückwärtsauflösung inkonsistent ist. Enthalten Domain-Informationen Fehler, funktionieren Dienste, die diese Informationen benutzen, aufgrund der Falschinformationen nur eingeschränkt. 

### 2 5 Fehlerhafte Konfiguration eines DNS-Servers

Sicherheitskritische Standardeinstellungen, selbst konfigurierte sicherheitskritische Einstellungen oder fehlerhafte Konfigurationen können dazu führen, dass ein DNS-Server nicht ordnungsgemäß funktioniert. Ist beispielsweise ein Resolving DNS-Server so konfiguriert, dass er rekursive Anfragen uneingeschränkt, also sowohl aus dem internen LAN als auch aus dem Internet, entgegennimmt, kann aufgrund der erhöhten Last die Verfügbarkeit des Servers stark beeinträchtigt sein. Zusätzlich könnte er dadurch anfällig für DNS-Reflection-Angriffe werden. 

Ebenso besteht bei fehlerhaft konfigurierten DNS-Servern die Gefahr, dass die Zonentransfers nicht auf berechtigte DNS-Server beschränkt sind. Damit kann jeder Host, der die Möglichkeit hat, eine Anfrage an die DNS-Server zu stellen, die gesamten Domain-Informationen dieser Server auslesen. Die so gewonnenen Daten können spätere Angriffe erleichtern.

### 2 6 DNS-Manipulation

Mit einem DNS-Cache-Poisoning-Angriff wird das Ziel verfolgt, dass der angegriffene Rechner falsche Zuordnungen von IP-Adressen und Namen speichert. Dabei wird ausgenutzt, dass DNS-Server erhaltene Domain-Informationen für einen gewissen Zeitraum im Cache zwischenspeichern. Gefälschte Daten können sich so weit verbreiten. Werden entsprechende Anfragen an den manipulierten DNS-Server gestellt, liefert dieser als Antwort die gefälschten Daten. Der Empfänger der Antwort speichert diese zwischen und sein Cache ist somit ebenfalls "vergiftet". Die gespeicherten Daten haben eine definierte Haltbarkeit (Time-To-Live, TTL). Wird der Resolving DNS-Server nach einer manipulierten Adresse gefragt, so wird er erst dann wieder einen anderen DNS-Server anfragen, wenn die Haltbarkeit abgelaufen ist. So ist es möglich, dass sich manipulierte DNS-Informationen lange halten, obwohl sie auf dem ursprünglich angegriffenen DNS-Server bereits wieder korrigiert sind. Gelingt es einem Angreifer beispielsweise die Namensauflösung für eine Domain zu übernehmen, indem er die Einträge so manipuliert, dass seine DNS-Server befragt werden, sind alle Subdomains automatisch mitbetroffen. DNS-Cache-Poisoning-Angriffe werden oft mit dem Ziel geführt, Anfragen auf maliziöse Server umzuleiten.

### 2 7 DNS-Hijacking

DNS-Hijacking ist eine Angriffsmethode, die verwendet wird, um die Kommunikation zwischen Advertising DNS-Servern und Resolvern über das IT-System eines Angreifers zu leiten. Dem Angreifer ist es mit dieser Man-in-the-Middle-Attacke möglich, die Kommunikation zwischen den Servern abzuhören und aufzuzeichnen. Die weitaus größere Gefahr besteht jedoch darin, dass ein erfolgreicher Angreifer jeglichen Verkehr der beiden Kommunikationspartner beliebig verändern kann. Wird nach einem erfolgreichen DNS-Hijacking-Angriff vom Resolver eines Client-IT-Systems eine Anfrage an einen DNS-Server gesendet, kann der Angreifer beispielsweise die Zuordnung von Namen und IP-Adresse abändern. DNS-Hijacking lässt sich auch mit anderen Angriffen kombinieren, besonders Phishing bietet sich in diesem Fall an. 

### 2 8 DNS-DoS

Bei einem DoS-Angriff auf einen DNS-Server werden so viele Anfragen an diesen gesendet, dass die Netzverbindung zum DNS-Server bzw. der DNS-Server selbst überlastet wird. In der Regel werden die Anfragen über Botnetze versendet, um die notwendige Datenrate zu erreichen. Ein auf diese Weise überlasteter DNS-Server kann keine legitimen Anfragen mehr beantworten.

### 2 9 DNS-Reflection

Bei einem DNS-Reflection-Angriff handelt es sich um einen DoS-Angriff, bei dem nicht der DNS-Server, an den die Anfragen gestellt werden, das Ziel ist, sondern der Empfänger der Antworten. Es wird ausgenutzt, dass bestimmte Anfragen eine verhältnismäßig große Antwortdatenmenge erzeugen. Es ist dabei möglich, einen Verstärkungsfaktor von 100 und mehr zu erreichen. Das bedeutet, dass die Antwort, gemessen in Bytes, mindestens 100-mal größer ist als die Anfrage. Durch die Anzahl und Größe der Antworten wird die Netzbandbreite bzw. der Rechner selbst über die Leistungskapazität hinaus überlastet. Somit kann jede beliebige technische IT-Komponente das Angriffsziel sein (siehe 2.8 *DNS-DoS*). DNS-Reflection-Angriffe werden durch Open-Resolver begünstigt.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen an DNS-Server aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.3.6.A1 Planung des DNS-Einsatzes

Da eine funktionierende Namensauflösung eine Grundvoraussetzung für viele Anwendungen und damit für einen reibungslosen Betrieb ist, MÜSSEN DNS-Server sorgfältig geplant werden. Dabei MUSS zunächst festgelegt werden, wie der Netzdienst DNS aufgebaut werden soll und welche Domain-Informationen schützenswert sind. Es MUSS auch geplant werden, wie DNS-Server in das Netz des Informationsverbundes eingebunden werden sollen. Die getroffenen Entscheidungen MÜSSEN dokumentiert werden.

#### APP.3.6.A2 Einsatz redundanter DNS-Server

Advertising DNS-Server (externe Anfragen) MÜSSEN redundant ausgelegt werden. Deshalb MUSS es für jeden Advertising DNS-Server mindestens einen zusätzlichen Secondary DNS-Server geben. 

#### APP.3.6.A3 Verwendung von separaten DNS-Servern für interne und externe Anfragen

Advertising DNS-Server (externe Anfragen) und Resolving DNS-Server (interne Anfragen) MÜSSEN serverseitig getrennt sein. Die Resolver der internen IT-Systeme DÜRFEN NUR die internen Resolving DNS-Server verwenden, um Namen aufzulösen.

#### APP.3.6.A4 Sichere Grundkonfiguration eines DNS-Servers

Ein Resolving DNS-Server MUSS so konfiguriert werden, dass er ausschließlich Anfragen aus dem internen Netz akzeptiert. Wenn er Anfragen versendet, MUSS er zufällige Source Ports benutzen. Sind DNS-Server bekannt, die falsche Domain-Informationen liefern, MUSS der Resolving DNS-Server daran gehindert werden, Anfragen dorthin zu senden. Ein Advertising DNS-Server MUSS so konfiguriert werden, dass er Anfragen aus dem Internet immer iterativ behandelt.

Es MUSS sichergestellt werden, dass DNS-Zonentransfers zwischen Primary und Secondary DNS-Servern funktionieren. Zudem MÜSSEN Zonentransfers so konfiguriert werden, dass diese nur zwischen Primary und Secondary DNS-Servern möglich sind. Um Zonentransfers abzusichern, MÜSSEN diese auf bestimmte IP-Adressen beschränkt werden. Die Version des verwendeten DNS-Server-Produktes MUSS verborgen werden.

#### APP.3.6.A5 Zeitnahes Einspielen sicherheitsrelevanter Patches und Updates

Die verantwortlichen Mitarbeiter MÜSSEN sich regelmäßig bei verschiedenen Quellen über neu bekannt gewordene Schwachstellen im eingesetzten DNS-Server-Produkt informieren und sicherheitsrelevante Updates zeitnah einspielen. Vorab MUSS jedoch auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. Solange keine Patches bei bekannten Schwachstellen verfügbar sind, MÜSSEN andere geeignete Maßnahmen getroffen werden, um die DNS-Server zu schützen. Bevor ein Patch eingespielt wird, MÜSSEN die Zonen- und Konfigurationsdateien gesichert werden.

#### APP.3.6.A6 Absicherung von dynamischen DNS-Updates

Um dynamische Updates sicher nutzen zu können, DÜRFEN NUR legitimierte IT-Systeme Domain-Informationen ändern. Auch MUSS festgelegt werden, welche Domain-Informationen die IT-Systeme ändern dürfen.

#### APP.3.6.A7 Überwachung von DNS-Servern

Um DNS-Server reibungslos zu betreiben und eventuelle Störungen oder Anomalien festzustellen, MÜSSEN diese laufend überwacht werden. Auch MUSS überwacht werden, wie ausgelastet die DNS-Server sind, um rechtzeitig die Leistungskapazität der Hardware anpassen zu können. Darüber hinaus MÜSSEN alle sicherheitsrelevanten Ereignisse an DNS-Servern geeignet protokolliert werden.

#### APP.3.6.A8 Verwaltung von Domainnamen [Leiter IT]

Es MUSS sichergestellt sein, dass die Registrierungen für alle Domains, die von einer Institution benutzt werden, regelmäßig und rechtzeitig verlängert werden. Es MUSS ein Mitarbeiter bestimmt werden, der dafür verantwortlich ist, die Internet-Domainnamen zu verwalten. Sofern ein Internetdienstleister mit der Domainverwaltung beauftragt wird, MUSS darauf geachtet werden, dass die Institution die Kontrolle über die Domains behält. 

#### APP.3.6.A9 Erstellen eines Notfallplans für DNS-Server

Es MUSS ein Notfallplan für DNS-Server erstellt werden. Er MUSS in die bereits vorhandenen Notfallpläne der Institution integriert werden. Auch MUSS darin ein Datensicherungskonzept für die Zonen- und Konfigurationsdateien beschrieben sein, das in das existierende Datensicherungskonzept der Institution integriert werden MUSS. Der Notfallplan MUSS auch einen Wiederanlaufplan für DNS-Server enthalten.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich DNS-Server. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.3.6.A10 Auswahl eines geeigneten DNS-Server-Produktes

Wird ein DNS-Server-Produkt beschafft, SOLLTE darauf geachtet werden, dass sich damit alle Sicherheitsanforderungen der Institution geeignet umsetzen lassen. Das Produkt SOLLTE sich in der Praxis ausreichend bewährt haben und die aktuellen RFC-Standards unterstützen. Es SOLLTE den Verantwortlichen dabei unterstützen, syntaktisch korrekte Master Files zu erstellen. Außerdem SOLLTE für das ausgewählte DNS-Server-Produkt genügend geschultes Personal vorhanden sein.

#### APP.3.6.A11 Ausreichende Dimensionierung der DNS-Server

Da die Hardware eines DNS-Servers die Leistung des gesamten Systems beeinflusst, SOLLTE sie ausreichend dimensioniert sein. Auch SOLLTE die Hardware ausschließlich für den Betrieb eines DNS-Servers benutzt werden. Ebenso SOLLTE die Netzanbindung der DNS-Server ausreichend bemessen sein.

#### APP.3.6.A12 Schulung der Verantwortlichen [Vorgesetzte, Leiter IT]

Es SOLLTE durch Schulungen sichergestellt werden, dass die Verantwortlichen mit den einzelnen Konfigurationsmöglichkeiten und sicherheitsrelevanten Aspekten der DNS-Server vertraut sind. 

#### APP.3.6.A13 Einschränkung der Sichtbarkeit von Domain-Informationen

Der Namensraum eines Informationsverbundes SOLLTE in einen öffentlichen und einen institutionsinternen Bereich aufgeteilt werden. Im öffentlichen Teil SOLLTEN nur solche Domain-Informationen enthalten sein, die von Diensten benötigt werden, die von extern erreichbar sein sollen. IT-Systeme im internen Netz SOLLTEN selbst dann keinen von außen auflösbaren DNS-Namen erhalten, wenn sie eine öffentliche IP-Adresse besitzen.

#### APP.3.6.A14 Platzierung der Nameserver

Primary und Secondary Advertising DNS-Server SOLLTEN in verschiedenen Netzsegmenten platziert werden. 

#### APP.3.6.A15 Auswertung der Logdaten

Die Logdateien des DNS-Servers sowie des unterliegenden Betriebssystems SOLLTEN regelmäßig überprüft und ausgewertet werden.

#### APP.3.6.A16 Integration eines DNS-Servers in eine "P-A-P"-Struktur

Die DNS-Server SOLLTEN in eine "Paketfilter – Application-Level-Gateway – Paketfilter"-(P-A-P)-Struktur (siehe auch NET.3.2 *Firewall*) integriert werden: Der Advertising DNS-Server SOLLTE in diesem Fall in einer demilitarisierten Zone (DMZ) des äußeren Paketfilters angesiedelt sein. Der Resolving DNS-Server SOLLTE in einer DMZ des inneren Paketfilters aufgestellt sein.

#### APP.3.6.A17 Einsatz von DNSSEC

Die DNS-Protokollerweiterung DNSSEC SOLLTE sowohl auf Resolving DNS-Servern als auch auf Advertising DNS-Servern aktiviert werden. Die dabei verwendeten Schlüssel Key-Signing-Keys (KSK) und Zone-Signing-Key (ZSK) SOLLTEN regelmäßig gewechselt werden.

#### APP.3.6.A18 Erweiterte Absicherung von Zonentransfers

Um Zonentransfers stärker abzusichern, SOLLTEN zusätzlich Transaction Signatures (TSIG) eingesetzt werden. 

#### APP.3.6.A19 Aussonderung von DNS-Servern

Wird ein DNS-Server ausgesondert, SOLLTEN alle Speichermedien des Servers sicher gelöscht werden. Außerdem SOLLTE der DNS-Server sowohl aus dem Domain-Namensraum als auch aus dem Netzverbund gelöscht werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.6.A20 Prüfung des Notfallplans auf Durchführbarkeit(A)

Es SOLLTE regelmäßig überprüft werden, ob der Notfallplan durchführbar ist.

#### APP.3.6.A21 Hidden-Master(CIA)

Um Angriffe auf den primären Advertising DNS-Server zu erschweren, SOLLTE eine sogenannte Hidden-Master-Anordnung vorgenommen werden.

#### APP.3.6.A22 Anbindung der DNS-Server über unterschiedliche Provider [Leiter IT](IA)

Extern erreichbare DNS-Server SOLLTEN über unterschiedliche Provider angebunden werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "DNS-Server" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSICS055] Sichere Bereitstellung von DNS-Diensten:

  

 Handlungsempfehlungen für Internet-Service-Provider (ISP) und große Unternehmen, BSI, 2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_055.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_055.pdf)

 
* #### [BSIDNSSEC] Umsetzung von DNSSEC

  

 Handlungsempfehlungen zur Einrichtung und zum Betrieb der Domain Name Security Extensions, BSI, 2015  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Cyber-Sicherheit/Themen/Umsetzung\_von\_DNSSEC.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Cyber-Sicherheit/Themen/Umsetzung_von_DNSSEC.pdf)

 
* #### [ISILANA] BSI-Standard zur Internet-Sicherheit (Isi-Reihe):

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [NIST800-81-2] NIST Special Publication 800-81-2:

  

 Secure Domain Name System (DNS) – Deployment Guide, NIST, 09.2013  
 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "DNS-Server" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

