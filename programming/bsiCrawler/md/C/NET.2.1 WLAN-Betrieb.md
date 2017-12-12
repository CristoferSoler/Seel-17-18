1 Beschreibung
--------------

### 1.1 Einleitung

Über Wireless LANs (WLANs) können drahtlose lokale Netze aufgebaut oder bestehende drahtgebundene Netze erweitert werden. Bis heute basieren fast alle am Markt verfügbaren WLAN-Komponenten auf dem Standard IEEE 802.11 und seinen Ergänzungen. Eine besondere Rolle nimmt dabei das Hersteller-Konsortium Wi-Fi Alliance ein, das basierend auf dem Standard IEEE 802.11 mit "Wi-Fi" einen Industriestandard geschaffen hat. Dabei bestätigt die Wi-Fi Alliance mit dem Wi-Fi-Gütesiegel, dass ein Gerät gewisse Interoperabilitäts- und Konformitätstests bestanden hat. 

Aufgrund der meist einfachen Installation werden WLANs auch dazu eingesetzt, um temporär Netze einzurichten, beispielsweise auf Messen oder kleineren Veranstaltungen. Darüber hinaus können an öffentlichen Plätzen, wie Flughäfen oder Bahnhöfen, Netzzugänge über so genannte Hotspots angeboten werden. Dadurch werden den mobilen Benutzern Verbindungen in das Internet oder ihr Firmennetz ermöglicht. Die Kommunikation findet dann generell zwischen einem zentralen Zugangspunkt, dem Access Point, und der WLAN-Komponente des Endgeräts (z. B. über einen WLAN-USB-Stick oder eine integrierte WLAN-Funktion) statt.

### 1.2 Zielsetzung

In diesem Baustein soll systematisch aufgezeigt werden, wie WLANs sicher in einer Institution aufgebaut und betrieben werden können.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die beachtet und erfüllt werden müssen, wenn WLANs aufgebaut und betrieben werden. Anforderungen für eine sichere Nutzung von WLANs sind nicht Gegenstand des vorliegenden Bausteins. Die sichere Nutzung von WLANs wird im Baustein NET.2.2 *WLAN-Nutzung* behandelt. Ebenso wird hier nicht auf den Betrieb von Hotspots (siehe NET.2.3 *Betrieb von Hotspots*) eingegangen.

WLANs können entsprechend den Bedürfnissen eines Betreibers und der Hardware-Ausstattung, die zur Verfügung steht, in zwei verschiedenen Modi betrieben werden. Im Ad-hoc-Modus kommunizieren zwei oder mehr mobile Endgeräte, die mit einer WLAN-Netzkarte ausgestattet sind, direkt miteinander. Da WLANs im Ad-hoc-Modus sich selbstständig, also ohne feste Infrastruktur, aufbauen und konfigurieren können und somit eine vollvermaschte parallele Netz-Infrastruktur etablieren können, ist der Ad-hoc-Modus in einer zu schützenden Umgebung ungeeignet. Dieser wird im Folgenden nicht weiter betrachtet. In den meisten Fällen werden WLANs im Infrastruktur-Modus betrieben, d. h. die Kommunikation der Clients und die Verbindung in kabelgebundene LAN-Segmente erfolgt über den Access Point.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich WLAN-Betrieb von besonderer Bedeutung:

### 2 1 Ausfall oder Störung eines Funknetzes

In Funknetzen werden Informationen mittels elektromagnetischer Funkwellen übertragen. Strahlen andere elektromagnetische Quellen im selben Frequenzspektrum Energie ab, können diese die drahtlose Kommunikation stören und im Extremfall den Betrieb des WLANs verhindern. Dies kann durch andere Funksysteme und Geräte, wie beispielsweise Bluetooth, Mikrowellenherde oder andere WLAN-Netze hervorgerufen werden. Darüber hinaus sind auch Denial-of-Service-Angriffe möglich. Werden beispielsweise bestimmte Steuer- und Managementsignale wiederholt gesendet, kann dies dazu führen, dass das Funknetz nicht mehr verfügbar ist.

### 2 2 Fehlende oder unzureichende Planung des WLAN-Einsatzes

Planungsfehler stellen sich oft als besonders schwerwiegend heraus, da leicht flächendeckende Sicherheitslücken geschaffen werden können. Wird der Einsatz von WLANs nicht oder nur unzureichend geplant, kann sich eine Vielzahl von Problemen ergeben, wie beispielsweise die Folgenden:

* Vertrauliche Daten könnten mitgelesen werden, beispielsweise wenn WLAN-Standards eingesetzt werden, die nicht mehr dem Stand der Technik entsprechen (z. B. WEP zur Verschlüsselung).
* Die Übertragungskapazität kann unzureichend sein. Dadurch können bandbreitenintensive Anwendungen nicht mit der erforderlichen Dienstgüte genutzt werden.
### 2 3 Fehlende oder unzureichende Regelungen zum WLAN-Einsatz

Bei einer WLAN-Infrastruktur, die nicht zentral administriert wird, sind die Access Points in der Standard-Einstellung meist ohne oder nur mit unzureichenden Sicherheitsmechanismen vorkonfiguriert. Schließt ein Mitarbeiter beispielsweise aufgrund fehlender Regelungen einen ungenehmigten bzw. ungesicherten Access Point an ein internes Netz der Institution an, untergräbt er praktisch sämtliche im LAN ergriffenen Sicherheitsmaßnahmen, wie z. B. das Sicherheitsgateway (Firewall) zum Schutz gegen unberechtigte externe Zugriffe.

### 2 4 Ungeeignete Auswahl von Authentisierungsverfahren

Wenn Authentikationsverfahren und -mechanismen fehlen oder zu unzureichend sind, können Sicherheitslücken entstehen. Beispielsweise wird im Standard IEEE 802.1X (Port Based Network Access Control) das EAP (Extensible Authentication Protocol) definiert. In einigen der beschriebenen EAP-Methoden sind Schwachstellen enthalten, z. B. ist EAP-MD5 anfällig gegenüber Man-in-the-Middle- bzw. Wörterbuchangriffen. Wird EAP-MD5 eingesetzt, können Passwörter erraten und die Kommunikation kann abgehört werden.

### 2 5 Fehlerhafte Konfiguration der WLAN-Infrastruktur

Access Points und andere WLAN-Komponenten (z. B. WLAN Controller) bieten eine Vielzahl von Konfigurationseinstellungen, die insbesondere auch Sicherheitsfunktionen betreffen. Werden hier falsche Einstellungen vorgenommen, ist entweder keine Kommunikation über einen Access Point möglich oder die Kommunikation erfolgt ungeschützt bzw. mit einem zu geringen Schutzniveau.

### 2 6 Unzureichende oder fehlende WLAN-Sicherheitsmechanismen

Im Auslieferungszustand sind WLAN-Komponenten häufig so konfiguriert, dass keine oder nur wenige Sicherheitsmechanismen aktiviert sind. Einige der Mechanismen sind darüber hinaus unzureichend und bieten keinen ausreichenden Schutz. Auch heute noch werden diverse WLAN-Komponenten eingesetzt, die lediglich unzureichende Sicherheitsmechanismen wie z. B. WEP unterstützen. Teilweise können diese Geräte nicht einmal auf stärkere Sicherheitsmechanismen aufgerüstet werden. Werden solche Geräte eingesetzt, kann ein Angreifer leicht die gesamte Kommunikation abhören und damit in den Besitz vertraulicher Informationen kommen. 

### 2 7 Abhören der WLAN-Kommunikation

Da es sich bei Funk um ein Medium handelt, das sich mehrere Benutzer teilen können ("Shared Medium"), können die über WLANs übertragenen Daten problemlos mitgehört und aufgezeichnet werden. Wenn die Daten nicht oder nur unzureichend verschlüsselt werden, können übertragene Nutzdaten leicht gewonnen werden. Zudem überschreiten Funknetze bzw. die ausgesendeten Funkwellen nicht selten die Grenzen der selbstgenutzten Räumlichkeiten, so dass Daten auch noch in Bereiche ausgestrahlt werden, die nicht von den Benutzern oder einer Institution kontrolliert und gesichert werden können.

### 2 8 Vortäuschung eines gültigen Access Points (Rogue Access Point)

Ein Angreifer kann sich als Teil der WLAN-Infrastruktur ausgeben, indem er einen eigenen Access Point mit einer geeignet gewählter SSID in der Nähe eines Clients installiert. Dieser vorgetäuschte Access Point wird als "Rogue Access Point" bezeichnet. Bietet dieser dem WLAN-Client eine stärkere Sendeleistung als der echte Access Point, wird der Client diesen als Basisstation nutzen, falls keine beidseitige Authentisierung erzwungen wird. Zusätzlich könnte auch der echte Access Point durch einen Denial-of-Service-Angriff ausgeschaltet werden. Die Benutzer melden sich an einem Netz an, das nur vorgibt, das Zielnetz zu sein. Dadurch ist es einem Angreifer möglich, die Kommunikation abzuhören. Auch durch Poisoning- oder Spoofing-Methoden kann ein Angreifer eine falsche Identität vortäuschen bzw. den Netzverkehr zu seinen Systemen umlenken. So kann er die Kommunikation belauschen und kontrollieren. Besonders in öffentlichen Funknetzen (sog. Hotspots) ist ein Rogue Access Point ein beliebtes Angriffsmittel. 

### 2 9 Ungeschützter LAN-Zugang am Access Point

Sind Access Points sichtbar und ohne physischen Schutz montiert, kann sich ein Angreifer zwischen die Access Points und die Switch-Infrastruktur schalten, um den gesamten Netzverkehr abzuhören. Selbst wenn die Kommunikation mit WPA2 verschlüsselt wird, stellt dies eine Gefährdung dar, da diese Methoden nur die Luftschnittstelle absichern, die Ethernet-Anbindung aber nicht weiter berücksichtigen.

### 2 10 Hardware-Schäden

Hardware-Schäden können dazu führen, dass der Funkverkehr gestört wird. Im schlimmsten Fall kann das WLAN sogar komplett ausfallen. Dies betrifft insbesondere WLAN-Geräte, die außerhalb von geschützten Räumen angebracht werden (z. B. um offene Plätze abzudecken). Sie sind zusätzlichen Gefährdungen ausgesetzt, wie beispielsweise vorsätzliche Beschädigungen durch Angreifer oder umweltbedingte Schäden durch Witterung oder Blitzeinschlag.

### 2 11 Diebstahl eines Access Points

Werden WLAN Access Points ungesichert in Durchgangswegen angebracht, z. B. direkt unter der Decke oder in Bereichen mit starkem Publikumsverkehr installiert, können sie gestohlen werden. Dadurch lässt sich beispielsweise ein Shared-Secret Key für die Authentisierung am RADIUS-Server oder der verwendete Schlüssel (beispielsweise für WPA2-Personal) auslesen. Mit diesen Informationen kann dann unberechtigt auf das WLAN zugegriffen werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich WLAN-Betrieb aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.2.1.A1 Festlegung einer Strategie für den Einsatz von WLANs [Leiter IT]

Bevor in einer Institution WLANs eingesetzt werden, MUSS festgelegt sein, welche generelle Strategie die Institution im Hinblick auf die WLAN-Nutzung einnimmt. Insbesondere MUSS geklärt und festgelegt werden, in welchen Organisationseinheiten, für welche Anwendungen und zu welchem Zweck WLANs eingesetzt und welche Informationen hierüber übertragen werden dürfen. Ebenso MUSS festgelegt werden, in welchen räumlichen Bereichen WLANs aufgebaut werden sollen.

Außerdem MUSS schon in der Planungsphase festgelegt sein, wer für die Administration der unterschiedlichen WLAN-Komponenten zuständig ist, welche Schnittstellen es zwischen den am Betrieb beteiligten Verantwortlichen gibt, und wann welche Informationen zwischen den Zuständigen ausgetauscht werden müssen.

#### NET.2.1.A2 Auswahl eines geeigneten WLAN-Standards [Planer]

Um eine Eigenstörung des WLANs zu vermeiden, MUSS im Rahmen der WLAN-Planung zuerst ermittelt werden, welche der von der Institution betriebenen Systeme (z. B. Mikrowellengeräte, Bluetooth) in das ISM-Band bei 2,4 GHz sowie in das 5 GHz-Band abstrahlen. 

Außerdem MÜSSEN die vorhandenen Sicherheitsmechanismen der einzelnen WLAN-Standards gegeneinander abgewogen werden. Generell MUSS es sichergestellt sein, dass nur als allgemein sicher anerkannte Verfahren zur Authentisierung und Verschlüsselung eingesetzt werden. Erst nachdem die einzelnen Standards ausführlich bewertet worden sind, kann ein bestimmter WLAN-Standard festgelegt werden. Die Entscheidungsgründe MÜSSEN dokumentiert werden.

Geräte, die von anerkannt sicheren Verfahren auf unsichere zurückgreifen müssen, DÜRFEN in der Planung NICHT mehr berücksichtigt werden.

#### NET.2.1.A3 Auswahl geeigneter Kryptoverfahren für WLAN [Planer]

Um ein WLAN sicher zu betreiben, MUSS die Kommunikation über die Luftschnittstelle komplett kryptographisch abgesichert werden. Kryptographische Verfahren unsicherer als WPA2 DÜRFEN NICHT mehr eingesetzt werden.

Wird WPA2 mit Pre-Shared Keys (WPA2-PSK) verwendet, dann MUSS ein komplexer Schlüssel mit einer Mindestlänge von 20 Zeichen verwendet werden. Außerdem MUSS dieser regelmäßig gewechselt werden.

#### NET.2.1.A4 Geeignete Aufstellung von Access Points [Haustechnik]

Access Points MÜSSEN zugriffssicher montiert werden. Darüber hinaus MUSS darauf geachtet werden, dass die Ausbreitung der Funkwellen in Bereichen, die nicht durch das WLAN versorgt werden sollen, möglichst stark reduziert ist. Außeninstallationen MÜSSEN vor Witterungseinflüssen und elektrischen Entladungen wie z. B. Blitzschlag geeignet geschützt werden.

#### NET.2.1.A5 Sichere Basis-Konfiguration der Access Points

Access Points DÜRFEN NICHT in der Konfiguration des Auslieferungszustandes verwendet werden. Voreingestellte SSIDs (Service Set Identifiers), Zugangskennwörter oder kryptographische Schlüssel MÜSSEN direkt nach Inbetriebnahme geändert werden. Außerdem MÜSSEN unsichere Administrationszugänge (z. B. Telnet oder HTTP) abgeschaltet werden. Access Points MÜSSEN verschlüsselt administriert werden.

#### NET.2.1.A6 Sichere Konfiguration der WLAN-Clients

Um eine interne WLAN-Infrastruktur sicher betreiben zu können, SOLLTEN auch alle damit gekoppelten WLAN-Clients sicher konfiguriert sein. Geeignete Anforderungen für eine sichere Konfiguration von Clients sind im Baustein SYS.2.1 *Allgemeiner Client* und NET.2.2 *WLAN-Nutzung* zu finden. Zusätzlich MÜSSEN folgende WLAN-spezifischen Anforderungen erfüllt werden:

* Wird die WLAN-Schnittstelle über einen längeren Zeitraum nicht genutzt, MUSS diese deaktiviert werden.
* Es MUSS sichergestellt sein, dass mittels der WLAN-Kommunikation keine Sicherheitszonen gekoppelt werden und hierdurch etablierte Schutzmaßnahmen umgangen werden.
#### NET.2.1.A7 Aufbau eines Distribution Systems [Planer]

Wird ein Distribution System aufgebaut, MUSS prinzipiell entschieden werden, ob physisch oder logisch durch VLANs auf den Access Switches des kabelbasierten LANs getrennt wird.

#### NET.2.1.A8 Verhaltensregeln bei WLAN-Sicherheitsvorfällen

Bei einem Sicherheitsvorfall MUSS der IT-Betrieb passende Gegenmaßnahmen einleiten (siehe auch DER.2.1 *Incident Management*):

* Am Übergabepunkt der WLAN-Kommunikation ins interne LAN SOLLTE bei einem Angriff auf das WLAN die Kommunikation selektiv pro SSID, Access Point oder sogar für die komplette WLAN-Infrastruktur gesperrt werden.
* Wurden Access Points gestohlen, MÜSSEN festgelegte Sicherheitsmaßnahmen umgesetzt werden, damit der Access Point nicht missbräuchlich verwendet wird.
* Sind WLAN-Clients entwendet worden und wird eine zertifikatsbasierte Authentisierung verwendet, MÜSSEN die Client-Zertifikate gesperrt werden.
Die möglichen Konsequenzen sicherheitskritischer Ereignisse MÜSSEN untersucht werden. Letztlich MUSS ausgeschlossen werden, dass entwendete Geräte unberechtigt verwendet werden, um auf das Netz der Institution zuzugreifen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich WLAN-Betrieb. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.2.1.A9 Sichere Anbindung von WLANs an ein LAN [Planer]

Werden WLANs an ein LAN angebunden, SOLLTE der Übergang zwischen WLANs und LAN abgesichert werden, beispielsweise durch einen Paketfilter. Der Access Point SOLLTE unter Berücksichtigung der Anforderung NET.2.1.A7 *Aufbau eines Distribution Systems* eingebunden sein.

#### NET.2.1.A10 Erstellung einer Sicherheitsrichtlinie für den Betrieb von WLANs

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTEN die wesentlichen Kernaspekte für einen sicheren Einsatz von WLANs konkretisiert werden. Die Richtlinie SOLLTE allen Verantwortlichen, die an Aufbau und Betrieb von WLANs beteiligt sind, bekannt sein und Grundlage für deren Arbeit sein. Die Umsetzung der in der Richtlinie geforderten Inhalte SOLLTE regelmäßig überprüft werden. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.

#### NET.2.1.A11 Geeignete Auswahl von WLAN-Komponenten

Ist beschlossen worden, eine WLAN-Infrastruktur aufzubauen, SOLLTE anhand der Ergebnisse der Planungsphase eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden können. Werden WLAN-Komponenten beschafft, SOLLTE neben Sicherheit auch auf Datenschutz und Kompatibilität der WLAN-Komponenten untereinander geachtet werden.

#### NET.2.1.A12 Einsatz einer geeigneten WLAN-Management-Lösung

Um aus Sicherheitssicht eine optimale Konfiguration der WLAN-Komponenten gewährleisten zu können, SOLLTE eine zentrale Managementlösung eingesetzt werden. Der Leistungsumfang der eingesetzten Lösung SOLLTE im Einklang mit den Anforderungen der WLAN-Strategie sein.

#### NET.2.1.A13 Regelmäßige Sicherheitschecks in WLANs

WLANs SOLLTEN regelmäßig überprüft werden, ob eventuell Sicherheitslücken existieren. Zusätzlich SOLLTE nach unbefugt installierten Access Points innerhalb der bereitgestellten WLANs gesucht werden. Weiterhin SOLLTE die Performance gemessen werden. Die Ergebnisse von Sicherheitschecks SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

#### NET.2.1.A14 Regelmäßige Audits der WLAN-Komponenten

Bei allen Komponenten der WLAN-Infrastruktur (Access Points, Distribution System, WLAN-Management-Lösung etc.) SOLLTE regelmäßig überprüft werden, ob alle festgelegten Sicherheitsmaßnahmen umgesetzt und diese korrekt konfiguriert sind. Öffentlich aufgestellte Access Points SOLLTEN regelmäßig stichprobenartig darauf geprüft werden, ob es gewaltsame Öffnungs- oder Manipulationsversuche gab. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.2.1.A15 Verwendung eines VPN zur Absicherung von WLANs(CI)

Bei erhöhtem Schutzbedarf SOLLTE ein VPN eingesetzt werden, um die Kommunikation über die WLAN-Infrastruktur zusätzlich abzusichern. Weitere Informationen hierzu sind im Baustein NET.3.3 *VPN* zu finden.

#### NET.2.1.A16 Zusätzliche Absicherung bei der Anbindung von WLANs an ein LAN(CIA)

Wird eine WLAN-Infrastruktur an ein LAN angebunden, SOLLTE der Übergang zwischen WLANs und LAN entsprechend des höheren Schutzbedarfs zusätzlich abgesichert werden.

#### NET.2.1.A17 Absicherung der Kommunikation zwischen Access Points(C)

Die Kommunikation zwischen den Access Points über die Funkschnittstelle und das LAN SOLLTE verschlüsselt erfolgen, um die Vertraulichkeit der übermittelten Daten, zum Beispiel Roaming-Informationen oder Zugangsdaten von Benutzern, zu gewährleisten.

#### NET.2.1.A18 Einsatz von Wireless Intrusion Detection / Wireless Intrusion Prevention Systemen(CIA)

Um Sicherheitsvorfälle und Schwachstellen zeitnah zu entdecken und entsprechende Gegenmaßnahmen direkt einleiten zu können, SOLLTEN Wireless Intrusion Detection Systeme bzw. Wireless Intrusion Prevention Systeme eingesetzt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "WLAN-Betrieb" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSIDKS] Drahtlose Kommunikationssysteme und ihre Sicherheitsaspekte

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [ISIWLAN] BSI-Standard zur Internet-Sicherheit (ISi-Reihe)

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02.2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [TR03103] Technische Richtlinie Sicheres Wireless LAN

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "WLAN-Betrieb" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.44 Unbefugtes Eindringen in Räumlichkeiten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

