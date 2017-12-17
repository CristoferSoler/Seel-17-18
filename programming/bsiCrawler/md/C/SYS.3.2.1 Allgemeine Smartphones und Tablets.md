1 Beschreibung
--------------

### 1.1 Einleitung

Smartphones sind mobile Telefone, die mit einem großen, üblicherweise berührungsempfindlichen Display ausgestattet sind. Smartphones vereinen oft Mobiltelefone, Media-Player, Personal Information Manager und Digitalkamera in einem Gerät und bieten den Benutzern verschiedene Anwendungen und Funktionen, wie z. B. Web-Browser, E-Mail-Client oder GPS. Zudem sind sie mit Mobilfunk-, WLAN- und Bluetooth-Schnittstellen ausgestattet. Tablets sind, vereinfacht gesagt, Smartphones mit großem Formfaktor, mit denen oft nicht über das Mobilfunknetz telefoniert werden kann. Als Phablets werden Hybridgeräte aus Smartphone und Tablet bezeichnet, sie werden im Baustein nicht gesondert hervorgehoben.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, den Verantwortlichen des Sicherheitsmanagements und des IT-Betriebs Informationen zu den typischen Gefährdungen für Smartphones und Tablets zu geben. Außerdem sollen den Verantwortlichen Ansätze gezeigt werden, um schutzbedarfsgerechte Konfigurationsprofile zu erstellen. Diese Konfigurationsprofile können über eine zentrale Infrastruktur zum "Mobile Device Management" (MDM) verteilt und verwaltet werden. Es kann jedoch bei der Vielzahl von unterschiedlichen Betriebssystemen nicht grundsätzlich vorausgesetzt werden, dass die Geräte in ein solches MDM eingebunden sind. 

### 1.3 Abgrenzung

Dieser Baustein geht nicht darauf ein, wie spezifische Betriebssysteme von Smartphones und Tablets abgesichert werden, da dies detailliert in den Bausteinen für die jeweiligen Systeme beschrieben wird, z. B. SYS.3.2.3 iOS (for Enterprise) oder SYS.3.2.4 Android. Sicherheitsanforderungen für den Betrieb eines MDM werden in SYS.3.2.2 Mobile Device Management beschrieben. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Smartphone und Tablet von besonderer Bedeutung:

### 2 1 Verlust des mobilen Geräts

Da mobile Endgeräte oft klein sind und ständig transportiert werden, können sie leicht vergessen, verloren gehen oder gestohlen werden. Neben dem wirtschaftlichen Schaden wiegt der Verlust der Vertraulichkeit und Integrität der enthaltenen Daten besonders schwer. Über ein entwendetes mobiles Endgerät könnte ein Angreifer auf vertrauliche Informationen oder IT-Ressourcen der Institution zugreifen.

### 2 2 Fehlende Betriebssystems-Updates

Es erscheinen regelmäßig neue Versionen von mobilen Betriebssystemen sowie Updates. Die Updates und Versionen müssen bei Geräten, die herstellerspezifische Erweiterungen des Betriebssystems haben, erst von den Herstellern in ihre Version integriert und dann verteilt werden. Diese Updates werden in der Regel für die neueste Gerätegeneration und für eine Reihe von älteren Gerätegenerationen bereitgestellt. Allerdings werden nicht alle zurückliegenden Betriebssystem-Versionen im gleichen Umfang mit Updates und Sicherheitsupdates versorgt, teilweise werden Betriebssysteme auch aus wirtschaftlichen Gründen nicht weiterentwickelt. Nachträglich bekannt gewordene Schwachstellen im Betriebssystem einer bereits abgekündigten Gerätegeneration werden dann nicht mehr mit Updates versorgt und nicht mehr geschlossen.

### 2 3 Software-Schwachstellen in Anwendungen (Apps)

Anwendungen (Apps) können Schwachstellen enthalten, die für lokale Angriffe oder für Angriffe über Netzverbindungen ausgenutzt werden können. Außerdem werden viele Apps nach einiger Zeit von Dritt-Entwicklern nicht mehr weiter gepflegt. Erkannte Sicherheitsmängel können dann nicht durch entsprechende Updates behoben werden.

### 2 4 Manipulation

Ein Angreifer kann sich Zugang zu den Geräten verschaffen, um gezielt Dateien zu manipulieren. Er könnte beispielsweise die Konfiguration ändern, zusätzliche Dienste starten oder Schadsoftware installieren. Dadurch kann ein Angreifer auf dem manipulierten System beispielsweise die Kommunikationsverbindungen mitschneiden (ungewollter Datenabfluss) oder die Regeln nach seinen Bedürfnissen ändern (z. B. Zugriffe aus dem Internet auf das Intranet erlauben).

### 2 5 Malware

Wie jedes mit dem Internet verbundene Gerät sind auch mobile Endgräte von Schadsoftware bedroht. Das Infektionsrisiko ist verglichen mit PC-Betriebssystemen noch geringer, jedoch konzentrieren sich die Cyberkriminellen immer mehr auf diese Geräte. Wird ein Gerät infiziert, können Angreifer beispielsweise Daten auslesen, verändern oder löschen.

### 2 6 Webbasierte Angriffe auf mobile Browser

Auch Browser auf mobilen Endgeräten können vollständige Webseiten und Webinhalte anzeigen. Dadurch können die Geräte von Phishing-Angriffen, Drive-by-Exploits und anderen webbasierten Angriffsformen betroffen sein.

### 2 7 Missbrauch von Fitness- oder Ortungsdaten

Das Betriebssystem vieler Geräte enthält meist spezielle Funktionen, um Fitness- und Ortungsdaten zu verwalten. Diese oft personenbezogene Daten sind besonders sensibel und stellen ein attraktives Angriffsziel dar, insbesondere wenn sie über einen längeren Zeitraum gesammelt und gespeichert werden, insofern diese Funktionen durch den Benutzer aktiviert wurden.

In der Folge ist der Standort des Mitarbeiters durch einen Angriff auf das Gerät oder die Cloud-ID des Mitarbeiters erkennbar. Das kann neben den datenschutzrechtlichen Auswirkungen auch andere Angriffe auf den Mitarbeiter nach sich ziehen.

### 2 8 Missbrauch sensitiver Daten im Sperrbildschirm

Viele mobile Betriebssysteme verfügen über eine Funktion, um Mitteilungen von aktivierten Widgets und Push-Nachrichten auf dem Sperrbildschirm anzeigen zu lassen. Hierdurch können sensitive Informationen des Benutzers ungeschützt auf dem Sperrbildschirm unberechtigten Dritten preisgegeben und ausgenutzt werden.

### 2 9 Gefahren durch private Nutzung mobiler Geräte

Wenn Mitarbeitern firmeneigene Smartphones, Tablets und Phablets ausgehändigt werden, könnten sie die Geräte auch unerlaubt privat benutzen. Dadurch entstehen gleich mehrere Probleme für die Informationssicherheit der Institution. So könnte sich ein Benutzer selbstständig Apps installieren, die jedoch Schadfunktionen enthalten oder er besucht eine Webseite, die das Gerät mit Malware infiziert. Ebenso sind viele vom Benutzer privat installierte Apps ein Risiko für die auf dem Gerät gespeicherten Informationen der Institution, da sie z. B. Adressbücher zu unbekannten Servern übertragen oder direkt auf E-Mails oder Dokumente zugreifen. So können Daten abfließen oder umgekehrt unkontrolliert in die Institution gelangen. Bekannte Beispiele dafür sind Social-Media- und Chat-Apps.

### 2 10 Gefahren durch Bring Your Own Device (BYOD)

Werden private Endgeräte dienstlich genutzt, können beispielsweise bezüglich der Software-Lizenzen zu rechtlichen Problemen auftreten. Auch wenn im Notfall alle Daten durch das MDM auf dem Gerät gelöscht werden müssen, könnte der Benutzer damit nicht einverstanden sein. 

Oft können die IT-Verantwortlichen nicht mehr jedes einzelne vom Mitarbeiter mitgebrachte Gerät daraufhin prüfen, ob es sich auch dienstlich einsetzen lässt. Dadurch können ungeeignete Geräte verwendet und so gegen interne Datenschutz- und Sicherheitsanforderungen verstoßen werden. Zudem sind die Benutzer oft selbst dafür verantwortlich, ihre Geräte zu warten und reparieren zu lassen. Bei einer solchen Reparatur könnten beispielsweise Firmendaten unbefugt eingesehen werden. Falls nicht geregelt ist, was mit den Daten auf dem Gerät geschehen soll, wenn der Mitarbeiter aus dem Unternehmen ausscheidet, könnten diese missbraucht werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Smartphone und Tablet aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.3.2.1.A1 Festlegung einer Strategie für Smartphones und Tablets

Bevor eine Institution Smartphones oder Tablets bereitstellt, betreibt oder einsetzt, MUSS die generelle Strategie im Hinblick auf die Nutzung und Kontrolle der Geräte festgelegt werden. Hierbei MUSS unter anderem festgelegt werden, wer auf welche Informationen der Institution zugreifen darf.

#### SYS.3.2.1.A2 Festlegung einer Strategie für den Cloud-Einsatz

Die Institution MUSS für mobile Endgeräte eine generelle Strategie für die Cloud-Nutzung und Informationskontrolle sowie für den Schutz der Informationen festlegen. Der Zugriff und die Nutzung von Cloud-Diensten für Informationen der Institution MUSS geklärt und festgelegt werden. Die Benutzer MÜSSEN regelmäßig über den Einsatz von Cloud-Diensten geschult werden.

#### SYS.3.2.1.A3 Sichere Grundkonfiguration für mobile Geräte

Alle mobilen Endgeräte MÜSSEN so konfiguriert sein, dass sie den erforderlichen Schutzbedarf angemessen erfüllen. Dafür MUSS eine passende Grundkonfiguration zusammengestellt und dokumentiert werden. Wenn eine Institution ein MDM einsetzt, MUSS bei der Übergabe des mobilen Endgerätes bereits der MDM-Client installiert sein.

#### SYS.3.2.1.A4 Verwendung eines Zugriffschutzes [Benutzer]

Es MÜSSEN alle Smartphones und Tablets mit einem Gerätesperrcode geschützt werden. Die Nutzung der Bildschirmsperre MUSS vorgeschrieben werden. Die Anzeige von vertraulichen Informationen auf dem Sperrbildschirm MUSS deaktiviert sein. Alle mobilen Geräte MÜSSEN nach wenigen Minuten selbsttätig den Bildschirm sperren. Die Zeitdauer MUSS in Abhängigkeit zum Schutzbedarf stehen.

Nach mehreren fehlgeschlagenen Versuchen den Bildschirm zu entsperren, MUSS sich das mobile Gerät in den Werkszustand zurücksetzen. Es SOLLTEN sich dabei die Daten oder die Verschlüsselungsschlüssel sicher vernichten.

Es SOLLTE vermieden werden, dass die Benutzer bei einem Passwortwechsel vor kurzem verwendete Kennworte nutzen. Die Anzahl der Kennworte, nachdem sich ein Passwort wiederholen darf, SOLLTE festgelegt werden.

Es SOLLTE ein komplexes Gerätepasswort verwendet werden.

#### SYS.3.2.1.A5 Automatische Updates von Betriebssystem und Apps

Es MUSS ein Prozess für automatische Updates des Betriebssystems und der eingesetzten Apps etabliert sein. Die Aktualisierungen MÜSSEN getestet werden. Nach der Freigabe MÜSSEN die Aktualisierungen zeitnah ausgerollt werden. Bereits bei der Auswahl von zu beschaffenden mobilen Geräten MUSS die Institution darauf achten, dass der Hersteller über den geplanten Nutzungszeitraum Updates für die Geräte bereitstellt. Ältere Geräte, für die keine aktuellen Versionen mehr bereitgestellt werden, MÜSSEN ausgesondert und durch vom Hersteller unterstützte Geräte ersetzt werden.

#### SYS.3.2.1.A6 Datenschutzeinstellungen

Der Zugriff von Apps und Betriebssystem auf Daten und Schnittstellen MUSS angemessen eingeschränkt werden. Die Datenschutzeinstellungen MÜSSEN so restriktiv wie möglich konfiguriert werden. Insbesondere der Zugriff auf Kamera, Mikrofon und Geodaten MÜSSEN auf Konformität mit den organisationsinternen Datenschutz- und Sicherheitsvorgaben überprüft und restriktiv konfiguriert bzw. deaktiviert werden.

#### SYS.3.2.1.A7 Verhaltensregeln bei Sicherheitsvorfällen [Fachverantwortliche, Benutzer]

Generell MÜSSEN alle Sicherheitsvorfälle gemeldet und behandelt werden. Gehen Geräte verloren oder werden unberechtigt Änderungen an Gerät und Software festgestellt, MÜSSEN die Verantwortlichen sofort geeignete Gegenmaßnahmen einleiten.

Die möglichen Konsequenzen sicherheitskritischer Ereignisse MÜSSEN untersucht werden. Letztlich MÜSSEN alle erforderlichen Maßnahmen ergriffen werden, um auszuschließen, dass auf vertrauliche und geschäftskritische Informationen der Institution zugegriffen werden kann.

#### SYS.3.2.1.A8 Keine Installation von Apps aus unsicheren Quellen

Es MUSS unterbunden werden, dass sich Apps aus alternativen Märkten oder aus dem Dateisystem installieren lassen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeine Smartphones und Tablets. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.3.2.1.A9 Nutzung von funktionalen Erweiterungen

Funktionalen Erweiterungen SOLLTEN nur restriktiv genutzt werden. Wenn möglich, SOLLTE auf funktionalen Erweiterungen verzichtet werden. Die funktionalen Erweiterungen SOLLTEN keinen automatischen Zugriff auf schützenswerte Informationen haben. Sie SOLLTEN die festgelegte Grundkonfiguration nicht umgehen oder ändern können.

#### SYS.3.2.1.A10 Richtlinie für Mitarbeiter zur Benutzung von mobilen Geräten [Benutzer]

Es SOLLTE eine verbindliche Richtlinie für Mitarbeiter zur Benutzung von mobilen Geräten erstellt werden. Diese SOLLTE festlegen, wie mobile Geräte genutzt und gepflegt werden sollen. Darin SOLLTEN die Themen Aufbewahrung und Verlustmeldung behandelt werden. Außerdem SOLLTE klar verboten werden, Verwaltungssoftware zu deinstallieren oder das Gerät zu rooten.

#### SYS.3.2.1.A11 Verschlüsselung des Dateisystems

Der gesamte Speicher des mobilen Geräts SOLLTE verschlüsselt werden. Auch eventuell vorhandene SD-Karten SOLLTEN verschlüsselt werden.

#### SYS.3.2.1.A12 Verwendung nicht personalisierter Gerätenamen

Der Gerätename SOLLTE keine Hinweise auf die Institution oder den Benutzer enthalten.

#### SYS.3.2.1.A13 Regelungen zum Screensharing und Casting

Es SOLLTE entschieden werden, ob Screensharing oder Casting eingesetzt werden soll. Screensharing und Casting SOLLTEN organisatorisch oder technisch eingeschränkt werden. Hierzu SOLLTE eine entsprechende Vereinbarung mit den Benutzern getroffen werden.

#### SYS.3.2.1.A14 Schutz vor Phishing und Schadprogrammen im Browser

Alle mobilen Endgeräte SOLLTEN vor Schadprogrammen geschützt werden. Im verwendeten Browser SOLLTE "Safe Browsing" bzw. die Funktion zur Warnung vor schädlichen Inhalten aktiviert werden.

#### SYS.3.2.1.A15 Deaktivierung von Download-Boostern

Download-Booster, die Daten über die Server des Herstellers leiten, SOLLTEN deaktiviert werden.

#### SYS.3.2.1.A16 Deaktivierung nicht benutzter Kommunikationsschnittstellen [Benutzer]

Nicht benutzte Kommunikationsschnittstellen SOLLTEN deaktiviert werden. Notwendige Schnittstellen SOLLTEN nur in geeigneten Umgebungen aktiviert sein.

#### SYS.3.2.1.A17 Verwendung der SIM-Karten-PIN

Die Nutzung der SIM-Karte der Institution SOLLTE durch eine PIN geschützt werden. Die Super-PIN / PUK SOLLTE nur im Rahmen der definierten Prozesse von den Verantwortlichen benutzt werden.

#### SYS.3.2.1.A18 Verwendung eines Fingerabdrucksensors

Wenn ein biometrischer Fingerabdrucksensor genutzt werden soll, SOLLTE geprüft werden, ob ein ähnlicher oder höherer Schutz als mit einem Gerätepasswort erzielt werden kann. Im Zweifelsfall oder bei einem schlechteren Schutz SOLLTE ein biometrischer Fingerabdrucksensor NICHT genutzt werden. Die Benutzer SOLLTEN hinsichtlich der Fälschbarkeit von Fingerabdrücken sensibilisiert werden.

#### SYS.3.2.1.A19 Verwendung eines Sprachassistenten

Sprachassistenten SOLLTEN nur eingesetzt werden, wenn die Funktion notwendig ist. Ansonsten SOLLTEN sie deaktiviert werden. Generell SOLLTE ein Sprachassistent nicht genutzt werden können, wenn das Gerät gesperrt ist.

#### SYS.3.2.1.A20 Auswahl und Freigabe von Apps

Apps aus öffentlichen App-Stores SOLLTEN durch die Verantwortlichen geprüft und freigegeben werden. Dazu SOLLTE ein Freigabeprozess entwickelt werden, in dem auch geeignete Bewertungskriterien definiert sind. Alle freigegebenen Apps SOLLTEN intern in einem Standardkatalog veröffentlicht werden.

#### SYS.3.2.1.A21 Definition der erlaubten Informationen und Applikationen auf mobilen Geräten [Fachverantwortliche, Benutzer]

Die Institution SOLLTE festlegen, welche Informationen auf den mobilen Endgeräten verarbeitet werden dürfen. Grundlage für die Regelung SOLLTEN einerseits die Klassifikation der Institutionsdaten sein und andererseits die Bedingungen, unter denen die Daten auf den Geräten verarbeitet werden.

Die Benutzer der mobilen Endgeräte SOLLTEN nur freigegebene und geprüfte Apps aus als sicher klassifizierte Quellen installieren dürfen.

#### SYS.3.2.1.A22 Einbindung der Geräte in die interne Infrastruktur via VPN

Mobile Endgeräte SOLLTEN nur mittels eines VPNs in die Infrastruktur der Institution integriert werden. Hierzu SOLLTE ein geeignetes Verfahren ausgewählt und eingesetzt werden. Die Authentisierung SOLLTE bevorzugt durch Zertifikate statt durch den Einsatz klassischer Passworte implementiert und betrieben werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.2.1.A23 Zusätzliches Passwort für vertrauliche Anwendungen(CI)

Alle Anwendungen mit vertraulichen Daten SOLLTEN durch ein zusätzliches Passwort geschützt werden.

#### SYS.3.2.1.A24 Einsatz einer geschlossenen Benutzergruppe(CI)

Das Passwort für den Zugangspunkt (Access Point Name, APN) einer geschlossenen Benutzergruppe SOLLTE komplex sein. Die Authentisierung SOLLTE das CHAP-Protokoll nutzen.

#### SYS.3.2.1.A25 Nutzung von getrennten Arbeitsumgebungen(CI)

Es SOLLTEN Lösungen für getrennte Arbeitsumgebungen eingesetzt werden. Hierfür SOLLTEN nur zertifizierte Produkte beschafft werden. Die Arbeitsdaten SOLLTEN in der dienstlichen Umgebung verbleiben.

#### SYS.3.2.1.A26 Nutzung von PIM-Containern(CIA)

Information auf den mobilen Endgeräten SOLLTEN gekapselt werden, zum Beispiel in einem PIM-Container. Zusätzlich SOLLTEN die Daten durch ein Passwort und eine vom Betriebssystem unabhängige Verschlüsselung abgesichert werden.

#### SYS.3.2.1.A27 Einsatz abgesicherter Betriebssysteme(CIA)

Institution SOLLTEN ein Gerät einsetzen, das für die Verarbeitung von Informationen nach gesetzlichen Informationsschutz-Klassifizierungen zertifiziert ist.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeine Smartphones und Tablets" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_052.pdf)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015   
 [https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf ](https://nccoe.nist.gov/sites/default/files/nccoe/NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013  
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf ](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeine Smartphones und Tablets" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

