1 Beschreibung
--------------

### 1.1 Einleitung

In diesem Baustein werden Geräte mit Funktionalitäten aus dem Bereich Internet of Things (IoT) betrachtet. Dies sind im Gegensatz zu "klassischen" IT-Systemen "intelligente" Gegenstände, die zusätzliche "smarte" Funktionen enthalten. IoT-Geräte werden in der Regel an Datennetze angeschlossen, in vielen Fällen drahtlos, und können sogar oft auf das Internet zugreifen und darüber erreicht werden. Hierdurch können sie Auswirkungen auf die Informationssicherheit des gesamten Informationsverbunds haben. 

IoT-Geräte können in Institutionen vorhanden sein, weil sie durch Mitarbeiter oder Externe mitgebracht werden, z. B. Smartwatches oder Wearables. In vielen Institutionen werden aber auch IoT-Geräte beschafft und betrieben, z. B. Geräte wie Brand-, Gas- und andere Warnmelder, Kaffeemaschinen oder Elemente der Gebäudesteuerung wie Kameras und HVAC (Heating, Ventilation and Air Conditioning). 

Generell kann zwischen direkt adressierbaren IoT-Geräten und IoT-Geräten, die eine zentrale Steuereinheit voraussetzen, unterschieden werden. Direkt adressierbare Geräte werden in der Regel mit einer eigenen IP-Adresse an ein Datennetz angeschlossen und können autark agieren oder durch eine zentralen Steuereinheit verwaltet werden. Es gibt aber auch IoT-Geräte, die ausschließlich direkt mit Steuereinheiten kommunizieren, z. B. über Funknetze wie Bluetooth oder ZigBee, und somit nicht direkt an Datennetze angeschlossen werden. Die Reichweite dieser Funkverbindungen kann, wenn vorgesehen, über ein separates, vermaschtes Netz vergrößert werden, indem jedes Gerät mit jedem Gerät eine Funkverbindung aufbaut.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, IoT-Geräte so abzusichern, dass über diese weder die Sicherheit der Informationen und IT der eigenen Institution noch die von Außenstehenden beeinträchtigt wird. Daher sollte sowohl ein unautorisierter Datenabfluss als auch die Manipulation der Geräte verhindert werden, speziell mit Blick auf Angriffe auf Dritte.

### 1.3 Abgrenzung

Dieser Baustein beschäftigt sich allgemein mit IoT-Geräten und soll für ein großes Spektrum unterschiedlicher IoT-Geräte anwendbar sein. Auf dedizierte Sicherheitseigenschaften etwa von Bedien- und Anzeigesystemen oder spezifischen Hard- und Software-Architekturen wird nicht näher eingegangen.

Je nach Ausprägung der IoT-Geräte sind die Übergänge zu Industriellen Steuerungssystemen (ICS-Systemen) oder eingebetteten Systemen fließend. Anforderungen für Geräte, die im Bereich Produktion und Fertigung eingesetzt werden, sind in den Bausteinen der Schicht IND (Industrielle IT) zu finden. 

Eingebettete Systeme sind informationsverarbeitende Systeme, die in ein größeres System oder Produkt integriert sind, dort Steuerungs-, Regelungs- und Datenverarbeitungsaufgaben übernehmen und dabei oft nicht direkt vom Benutzer wahrgenommen werden. Für diese ist Baustein SYS.4.3 Eingebettete Systeme umzusetzen.

Anforderungen für die häufig im Kontext eingesetzten Funkstrecken befinden sich in den Bausteinen der Schicht NET.2 Funknetze.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich IoT-Geräte von besonderer Bedeutung:

### 2 1 Ausspähung über IoT-Geräte

Bei der Entwicklung von IoT-Geräten ist der Aspekt der Informationssicherheit typischerweise ein nicht oder nur nachrangig beachtetes Entwurfsziel. Daher konnten IoT-Geräte immer wieder missbraucht werden, um über diese Informationen über die Nutzer bzw. den Einsatzbereich zu sammeln. So ist es immer wieder zu Vorfällen mit vernetzten bzw. IP-basierten Überwachungskameras gekommen, z. B.:

* 2013 wurden mehrere Banken in verschiedenen Ländern im Zuge der Kampagne "Carbanak" über Überwachungskameras kompromittiert. Die Täter erbeuteten einen dreistelligen Millionenbetrag. Bei diesen Angriffen wurden über die Kameras Bildschirminhalte und Tastatureingaben in den Finanzinstituten ausgespäht.
* 2014 wurden über die Webseite Insecam die Videobilder bzw. -streams von 73.000 unzureichend geschützten Webcams offen zur Verfügung gestellt.
* 2015 infizierte die zu dem Zeitpunkt 8 Jahre alte Schadsoftware Conficker eine Vielzahl von Bodycams verschiedener Polizeien.
### 2 2 Verwendung von UPnP

In LANs integrierte IoT-Geräte bauen oftmals selbstständig eine Verbindung zum Internet auf, indem sie Router im Netz per UPnP (Universal Plug and Play) so konfigurieren, dass eine Portweiterleitung entsteht. Die Geräte können dann nicht nur ins lokale Netz kommunizieren, sondern sind auch von außerhalb des LANs nicht nur sichtbar, sondern auch erreichbar. Wenn dann eine Schwachstelle im IoT-Gerät durch einen Angreifer ausgenutzt wird, könnte dieses dadurch Teil eines Botnetzes werden, es könnte aber auch weitere Schadsoftware in den Informationsverbund eingeschleust werden. Diese Lücke kann theoretisch zu einem späteren Zeitpunkt auch für andere Aktivitäten genutzt werden. 

### 2 3 Schäden Dritter

Wenn IoT-Geräte nicht regelmäßig gepatcht werden, bleiben bekannte Schwachstellen offen und können für umfangreiche Angriffe ausgenutzt werden. Ein Ziel eines Angriffs könnte dabei sein, die IoT-Geräte in ein Botnetz zu integrieren. In diesem Fall könnten sie beispielsweise dazu genutzt werden, um DDoS-Angriffe (Distributed Denial of Service) auszuführen und die Verfügbarkeit von Diensten einzuschränken.

Beispiel: Ende Oktober 2016 wurde ein DDoS-Angriff auf einen Internetdienstleister durchgeführt, bei dem ein Botnetz benutzt wurde, das zu großen Teilen aus IoT-Geräten bestand. Das sogenannte Mirai-Botnetz hat dabei auf Grund der großen Anzahl der Geräte eine Bandbreite erreicht, die weit über die vorher bekannten Botnetze hinausging. Die Webcams, Kameras, DVR Player, Router und Drucker, die bereits zum Botnetz gehörten, scannten selbstständig das Internet nach weiteren Geräten, um sie mit Schadsoftware zu infizieren und dem Botnetz hinzuzufügen. 

### 2 4 Spionageangriffe mittels Hintertüren in IoT-Geräten

Ende September 2016 wurde bekannt, dass einige Modelle von Überwachungskameras und Raumsensoren mit Hintertüren ausgestattet sind, die Spionage ermöglichen. Dies betrifft insbesondere Überwachungskameras, die in Rechenzentren und Serverräumen eingesetzt werden. Die Hintertüren ermöglichten offenbar, auf die Bild- und Videodaten der Kameras zuzugreifen sowie diese Daten auf Server im Internet zu kopieren. So können z. B. Benutzer- und Administrations-Kennwörter kompromittiert werden oder Gerätekonfigurationen, Infrastrukturdetails und sonstige vertrauliche Informationen Dritten zugänglich werden. Dies erleichtert weitergehende Angriffe, indem die Gewohnheiten des Personals ausgenutzt werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich IoT aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.4.4.A1 Einsatzkriterien für IoT-Geräte

IoT-Geräte MÜSSEN ein Minimum an Sicherheitskriterien erfüllen, damit sie in Institutionen eingesetzt werden können. Die Geräte MÜSSEN Update-Funktionen besitzen und der Hersteller MUSS einen Update-Prozess anbieten. Die Geräte MÜSSEN eine Authentisierung ermöglichen. Es DÜRFEN KEINE fest codierten Zugangsdaten im Gerät existieren. 

#### SYS.4.4.A2 Authentisierung

Um ein IoT-Gerät in einer Institution zu nutzen, MUSS eine Authentisierung aktiviert sein. Werden hierfür Passwörter verwendet, MÜSSEN sichere Passwörter benutzt werden. Hierfür SOLLTE es eine Passwort-Richtlinie geben. Diese Passwörter MÜSSEN komplex genug sein, geheim gehalten und regelmäßig gewechselt werden. Voreingestellte Passwörter MÜSSEN geändert werden. Zusätzlich empfiehlt sich die Verwendung von alternativen Authentisierungsmechanismen, wie z. B. zertifikatsbasierte Authentisierung. 

#### SYS.4.4.A3 Regelmäßige Aktualisierung

Es MUSS regelmäßig überprüft werden, ob die IoT-Geräte und zugehörige Komponenten wie Sensoren oder Management-Systeme auf dem aktuellen Stand sind. Wenn Sicherheitslücken identifiziert werden, MÜSSEN diese so schnell wie möglich behoben werden. Vorhandene Patches und Updates MÜSSEN sofort eingespielt werden oder anderweitige Sicherheitsmaßnahmen ergriffen werden, wenn keine Patches zur Verfügung stehen. Generell MUSS darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden.

#### SYS.4.4.A4 Aktivieren von Autoupdate-Mechanismen

Automatische Update-Mechanismen (Autoupdate) MÜSSEN aktiviert werden, sofern nicht andere Mechanismen, wie regelmäßige manuelle Wartung oder ein zentrales Softwareverteilungssystem für Updates eingesetzt werden. Wenn für Autoupdate-Mechanismen ein Zeitintervall vorgegeben werden kann, SOLLTE mindestens täglich automatisch nach Updates gesucht und diese installiert werden.

#### SYS.4.4.A5 Einschränkung des Netzzugriffs

Der Netzzugriff von IoT-Geräten MUSS auf das erforderliche Minimum eingeschränkt und kontrolliert werden. Dazu gehören:

* Verkehrskontrolle an Netzübergängen, z. B. durch Regelwerke auf Firewalls und Access Control Lists (ACLs) auf Routern. Es dürfen nur zuvor definierte ein- und ausgehende Verbindungen erlaubt werden.
* Restriktive Konfiguration des Routings auf IoT-Geräten und Sensoren, insbesondere die Unterdrückung von Default-Routen.
* Signaturen auf Intrusion-Prevention-Systemen (IPS).
* Die IoT-Geräte und Sensoren SOLLTEN in einem eigenen Netzsegment betrieben werden, das ausschließlich mit dem Netzsegment für das Management kommunizieren darf.
* Konfiguration von Virtual Private Networks (VPNs) zwischen den Netzen mit IoT-Geräten und Sensor-Netzen und den Management-Netzen .
* UPnP-Funktion MUSS an allen Routern deaktiviert sein. 
### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeines IoT-Gerät. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.4.4.A6 Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution

In der allgemeinen Sicherheitsrichtlinie der Institution SOLLTEN die Anforderungen an IoT-Geräte konkretisiert werden. Die Richtlinie SOLLTE allen Personen, die an der Beschaffung und dem Betrieb von IoT-Geräten beteiligt sind, bekannt und Grundlage für deren Arbeit sein. Die Umsetzung der in der Richtlinie geforderten Inhalte SOLLTE regelmäßig überprüft und die Ergebnisse sinnvoll dokumentiert werden.

#### SYS.4.4.A7 Planung des Einsatzes von IoT-Geräten

Zum sicheren Betrieb von IoT-Geräten SOLLTE im Vorfeld geplant werden, wo und wie diese eingesetzt werden sollen. Die Planung SOLLTE dabei nicht nur Aspekte betreffen, die klassischerweise mit dem Begriff Informationssicherheit verknüpft werden, sondern auch normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen. Dabei SOLLTEN Vorgaben zur Authentisierung, Update-Mechanismen und Netzanbindung definiert werden. Alle Entscheidungen, die in der Planungsphase getroffen wurden, SOLLTEN so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. 

#### SYS.4.4.A8 Beschaffungskriterien für IoT-Geräte [Informationssicherheitsbeauftragter (ISB), Beschaffungsstelle]

Der ISB SOLLTE auch bei Beschaffungen von Geräten, die keine offensichtliche IT-Funktionalität haben, beteiligt werden. Bevor IoT-Geräte beschafft werden, SOLLTE festgelegt werden, welche Sicherheitsanforderungen diese erfüllen müssen. Bei der Beschaffung von IoT-Geräten SOLLTEN Aspekte der materiellen Sicherheit ebenso wie Anforderungen an die Sicherheitseigenschaften der Software ausreichend berücksichtigt werden. Es SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. IoT-Geräten mit einem Cloud-Konzept SOLLTEN nicht beschafft werden. 

#### SYS.4.4.A9 Regelung des Einsatzes von IoT-Geräten

Für jedes IoT-Gerät SOLLTE ein Verantwortlicher für den Betrieb benannt sein. Die Verantwortlichen SOLLTEN ausreichend informiert sein über den Umgang mit dem IoT-Gerät. Alle für die Geräte Verantwortlichen, Benutzer und Administratoren SOLLTEN über Verhaltensregeln und Meldewege bei Ausfällen, Fehlfunktionen oder bei Verdacht auf einen Sicherheitsvorfall informiert sein. 

#### SYS.4.4.A10 Sichere Installation und Konfiguration von IoT-Geräten

Es SOLLTE festgelegt werden, unter welchen Rahmenbedingungen IoT-Geräte installiert und konfiguriert werden.* *Die Installation und Konfiguration der IoT-Geräte SOLLTE nur von autorisierten Personen (Verantwortlich für IoT-Geräte, Administratoren oder vertraglich gebundene Dienstleister) nach einem definierten Prozess durchgeführt werden. Alle Installations- und Konfigurationsschritte SOLLTEN so dokumentiert werden, dass die Installation und Konfiguration durch einen sachkundigen Dritten anhand der Dokumentation nachvollzogen und wiederholt werden kann.

Die Grundeinstellungen von IoT-Geräten SOLLTEN überprüft und nötigenfalls entsprechend den Vorgaben der Sicherheitsrichtlinie angepasst werden. Falls möglich, SOLLTEN IoT-Geräte erst mit IT-Netzen verbunden werden, nachdem die Installation und die Konfiguration abgeschlossen ist, dies gilt vor allem für öffentliche Netze.

#### SYS.4.4.A11 Verwendung sicherer Protokolle

Daten SOLLTEN nur verschlüsselt übertragen werden. IoT-Geräte SOLLTEN ein auf Verschlüsselung basierendes Protokoll (z. B. SSL/TLS bzw. SSH) unterstützen. Bietet das Produkt selbst keine Verschlüsselung, SOLLTE dies bei der Inbetriebnahme, z. B. über ein Virtual Private Network (VPN), flankierend umgesetzt werden.

#### SYS.4.4.A12 Sichere Integration in übergeordnete Systeme [Informationssicherheitsbeauftragter (ISB)]

Wenn IoT-Geräte in Zusammenhang mit übergeordneten Management-Systemen eingesetzt werden, SOLLTEN sie ausschließlich mit diesen kommunizieren.

#### SYS.4.4.A13 Deaktivierung und Deinstallation nicht benötigter Komponenten

Nach der Installation SOLLTE überprüft werden, welche Protokolle, Anwendungen und weitere Tools auf den IoT-Geräten installiert und aktiviert sind. Nicht benötigte Protokolle, Dienste, Benutzerkennungen und Schnittstellen SOLLTEN deaktiviert oder ganz deinstalliert werden. Dies gilt insbesondere für unsichere Dienste, wie z. B. Telnet oder SNMPv1/v2. Die Verwendung von nicht benötigten Funkschnittstellen, z. B. für WLAN, ZigBee, Bluetooth, SOLLTE unterbunden werden. 

Wenn dies nicht am Gerät selber möglich ist, SOLLTEN nicht benötigte Dienste über das Sicherheitsgateway (Firewall) eingeschränkt werden. Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration für die IoT-Geräte gewählt wurden.

#### SYS.4.4.A14 Einsatzfreigabe

Bevor IoT-Geräte im produktiven Betrieb eingesetzt und bevor sie an ein produktives Netz angeschlossen werden, SOLLTE eine Einsatzfreigabe erfolgen. Diese SOLLTE dokumentiert werden. Für die Einsatzfreigabe SOLLTE die Installations- und Konfigurationsdokumentation und die Funktionsfähigkeit der IoT-Geräte in einem Test geprüft werden. Sie SOLLTE durch eine in der Institution dafür autorisierte Stelle erfolgen.

#### SYS.4.4.A15 Restriktive Rechtevergabe

Die Zugriffsberechtigungen auf IoT-Geräte SOLLTEN möglichst restriktiv vergeben werden. Wenn dies über die IoT-Geräte selber nicht möglich ist, SOLLTE überlegt werden, dies netzseitig zu regeln.

#### SYS.4.4.A16 Beseitigen von Schadprogrammen auf IoT-Geräten

Der IT-Betrieb SOLLTE sich regelmäßig informieren, ob sich die eingesetzten IoT-Geräte mit Schadprogrammen infizieren und wie diese beseitigt werden können. Schadprogramme SOLLTEN unverzüglich beseitigt werden. Kann die Ursache für die Infektion nicht behoben bzw. eine Neuinfektion wirksam verhindert werden, SOLLTEN die betroffenen IoT-Geräte nicht mehr verwendet werden.

#### SYS.4.4.A17 Überwachung des Netzverkehrs von IoT-Geräten

Es SOLLTE überwacht werden, ob Netzverkehr von den IoT-Geräten oder Sensor-Systemen zu Nicht-Managementsystemen erfolgt.

#### SYS.4.4.A18 Protokollierung sicherheitsrelevanter Ereignisse bei IoT-Geräten

Sicherheitsrelevante Ereignisse SOLLTEN automatisch protokolliert werden. Falls dies durch die IoT-Geräte selber nicht möglich ist, SOLLTEN hierfür Router oder andere Protokollmechanismen genutzt werden. Die Protokolle SOLLTEN in sinnvollem Umfang ausgewertet werden.

#### SYS.4.4.A19 Schutz der Administrationsschnittstellen

Abhängig davon, ob IoT-Geräte lokal, direkt über das Netz oder über zentrale netzbasierte Tools administriert werden, SOLLTEN geeignete Sicherheitsvorkehrungen getroffen werden. Die zur Administration verwendeten Methoden SOLLTEN in der Sicherheitsrichtlinie festgelegt werden. Die IoT-Geräte SOLLTEN entsprechend der Sicherheitsrichtlinie administriert werden. Die Administration über das Netz SOLLTE über sichere Protokolle erfolgen.

#### SYS.4.4.A20 Geregelte Außerbetriebnahme von IoT-Geräten

Bei der Außerbetriebnahme von IoT-Geräten SOLLTE sichergestellt werden, dass keine wichtigen Daten, die eventuell auf den verbauten Datenträgern gespeichert sind, verloren gehen, und dass keine sensitiven Daten zurück bleiben. Es SOLLTE einen Überblick darüber geben, welche Daten wo auf IoT-Geräten gespeichert sind. Es SOLLTE eine Checkliste erstellt werden, die bei der Außerbetriebnahme von IoT-Geräten abgearbeitet werden kann. Diese Checkliste SOLLTE mindestens Aspekte zur Datensicherung weiterhin benötigter Daten und dem anschließenden sicheren Löschen aller Daten umfassen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.4.4.A21 Einsatzumgebung und Stromversorgung [Informationssicherheitsbeauftragter (ISB), Haustechnik](I)

Es SOLLTE geklärt werden, ob IoT-Geräte in der angedachten Einsatzumgebung betrieben werden dürfen (Schutzbedarf anderer Systeme, Datenschutz). IoT-Geräte SOLLTEN in der Einsatzumgebung vor Diebstahl, Zerstörung und Manipulation geschützt werden.

Es SOLLTE geklärt sein, ob ein IoT-Gerät bestimmte Anforderungen an die physikalische Einsatzumgebung hat, wie z. B. Luftfeuchtigkeit, Temperatur oder Energieversorgung. Falls erforderlich, SOLLTEN dafür ergänzende Maßnahmen bei der Infrastruktur umgesetzt werden.

Wenn IoT-Geräte mit Batterien betrieben werden, SOLLTE der regelmäßige Funktionstest und Austausch der Batterien geregelt werden.

IoT-Geräte SOLLTEN entsprechend ihrer vorgesehenen Einsatzart und des vorgesehenen Einsatzorts vor Staub und Verschmutzungen geschützt werden.

#### SYS.4.4.A22 Systemüberwachung(A)

Die IoT-Geräte SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden, das den Systemzustand und die Funktionsfähigkeit der IoT-Geräte laufend überwacht und Fehlerzustände sowie die Überschreitung definierter Grenzwerte an das Betriebspersonal meldet. Ist eine hohe Verfügbarkeit der IoT-Geräte erforderlich, SOLLTE geprüft werden, ob die verwendeten Geräte diese Anforderung erfüllen oder ob weitere Maßnahmen wie das Einrichten eines Clusters oder die Beschaffung von Standby-Geräten erforderlich sind. 

#### SYS.4.4.A23 Auditierung von IoT-Geräten(CIA)

In sicherheitskritischen Bereichen SOLLTEN alle zum Einsatz kommenden IoT-Geräte durch Experten sicherheitstechnisch überprüft werden.

#### SYS.4.4.A24 Sichere Konfiguration und Nutzung eines eingebetteten Webservers(CIA)

In IoT-Geräten integrierte Webserver SOLLTEN möglichst restriktiv konfiguriert sein. Es SOLLTEN nur die benötigten Komponenten und Funktionen installiert bzw. aktiviert sei. Der Webserver SOLLTE NICHT unter einem privilegierten Konto betrieben werden, soweit möglich. Sicherheitsrelevante Ereignisse SOLLTEN protokolliert werden. Der Zugang DARF nur nach Authentisierung möglich sein. Die Übertragung SOLLTE verschlüsselt sein.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeines IoT-Gerät" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ACS1] Sicherheit von IP-basierten Überwachungskameras

  

 CSE 128, Version 1.0, Allianz für Cyber-Sicherheit, 11.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_128.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_128.html)

 
* #### [ACS2] Spionageangriffe mittels Hintertüren in Überwachungskameras und Raumsensoren

  

 So schützen Sie Ihr Unternehmen, Expertenkreis Cyber-Sicherheit, Allianz für Cyber-Sicherheit, 10.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161010\_expkr\_statement01.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/partner/161010_expkr_statement01.pdf)

 
* #### [DHS] Department of Homeland Security

  

 Securing the Internet of Things, 12.2016,   
 <https://www.dhs.gov/securingtheIoT>

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (zuletzt abgerufen am 28.09.2017)  
 <https://www.owasp.org>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeines IoT-Gerät" von Bedeutung.

* G 0.2 Ungünstige klimatische Bedingungen
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

