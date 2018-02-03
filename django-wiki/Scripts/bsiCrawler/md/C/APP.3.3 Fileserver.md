1 Beschreibung
--------------

### 1.1 Einleitung

Ein Fileserver (oder auch Dateiserver) ist ein Server in einem Netz, der Dateien für alle zugriffsberechtigten Benutzer bzw. Clients zentral bereitstellt. Die Datenbestände können von zugriffsberechtigten Benutzern gleichzeitig genutzt werden, ohne diese z. B. auf Wechseldatenträger zu transportieren oder per E-Mail zu verteilen. Dadurch, dass die Daten zentral vorgehalten werden, können die Daten strukturiert und in verschiedenen Dateiversionen bereitgestellt werden. Bei Fileservern können Rechte zentral vergeben werden und die Datensicherung kann an zentraler Stelle erfolgen.

Ein Fileserver verwaltet meistens Massenspeicher, die mit ihm über Schnittstellen wie SCSI (Small Computer System Interface) oder SAS (Serial Attached SCSI) verbunden sind. Die Speicher befinden sich entweder direkt im Gehäuse des Fileservers oder sind extern angeschlossen. Letzteres wird oft als Directly Attached Storage (DAS) bezeichnet. Ein Fileserver kann auf herkömmlicher Server-Hardware oder einer dedizierten Appliance, z. B. einem Network Attached Storage (NAS), betrieben werden. Oft können bei großen Datenmengen auch zentrale SAN-Speicher (Storage Area Network) über HBA (Host-Bus-Addapter) im Server und SAN Switche angebunden werden. 

### 1.2 Zielsetzung

In diesem Baustein werden die für einen Fileserver spezifischen Gefährdungen und die sich daraus ergebenden Anforderungen für einen sicheren Betrieb beschrieben.

### 1.3 Abgrenzung

Der vorliegende Baustein enthält grundsätzliche Anforderungen, die beim Betrieb von Fileservern zu beachten und zu erfüllen sind. Allgemeine und betriebssystemspezifische Aspekte eines Servers sind nicht Gegenstand des vorliegenden Bausteins, sondern werden im Baustein SYS1.1 Allgemeiner Server und in den entsprechenden betriebssystemspezifischen Bausteinen der Schicht IT-Systeme behandelt, z. B. SYS.1.3 Unix Server oder SYS.1.2.2 Windows Server 2012. Des Weiteren werden keine Anforderungen an Speichersysteme bzw. Speichernetze beschrieben, diese sind im Baustein SYS.1.8 Speichersysteme zu finden. Auch wird nicht auf dedizierte Dienste eingegangen, mit denen ein Fileserver betrieben werden kann, z. B. Samba.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind bei Fileservern von besonderer Bedeutung:

### 2 1 Ausfall eines Fileservers

Fällt ein Fileserver aus, kann der gesamte Informationsverbund davon betroffen sein und damit auch wichtige Geschäftsprozesse der Institution. Neben den Benutzern können auch Anwendungen auf Daten vom Fileserver angewiesen sein, um ordnungsgemäß zu funktionieren. Ist die Verfügbarkeit von Daten und Diensten nicht gegeben, können z. B. Fristen nicht eingehalten werden oder essenzielle Geschäftsprozesse fallen aus. Ist zudem kein Notfallmanagementkonzept umgesetzt, können sich Wiederanlaufzeiten weiter erhöhen. In vielen Fällen führt dies zu finanziellen Einbußen der Institution oder es wirkt sich auf andere Institutionen aus.

### 2 2 Unzureichende Dimensionierung des Fileservers

Wird die Leitungsanbindung oder Speicherkapazität des Fileservers unzureichend dimensioniert, können sich die Zugriffszeiten erhöhen oder es kommt zu Speicherengpässen. Dadurch besteht beispielsweise die Gefahr, dass Mitarbeiter aufgrund der längeren Wartezeiten frustriert sind und damit beginnen, Daten lokal zu speichern. So kann nicht mehr nachvollzogen werden, wo Daten gespeichert sind und wer in Besitz der Daten ist.

### 2 3 Unzureichende Überprüfung von abgelegten Dateien

Ist ein Fileserver unzureichend in das Konzept zum Schutz vor Schadprogrammen der Institution einbezogen, besteht die Gefahr, dass Angreifer unbemerkt Schadsoftware auf dem Fileserver platzieren. Dadurch können die Daten auf dem Fileserver unberechtigt eingesehen oder manipuliert werden. Es bestehen aber auch Sicherheitsrisiken für alle Geräte und Anwendungen, die auf die Daten des Fileservers zugreifen. So kann sich zum Beispiel Schadsoftware sehr schnell in der gesamten Institution ausbreiten. 

### 2 4 Fehlendes oder unzureichendes Zugriffsberechtigungskonzept

Werden Zugriffsberechtigungen und Freigaben nicht ordnungsgemäß konzipiert und vergeben, können eventuell Dritte unbefugt auf Daten zugreifen. Dadurch können Angreifer Daten verändern, löschen oder kopieren.

### 2 5 Unstrukturierte Datenhaltung

Wird die Speicherstruktur nicht vorgegeben bzw. halten sich die Mitarbeiter nicht daran, können Daten unübersichtlich und unkoordiniert auf dem Fileserver gespeichert werden. Das führt zu verschiedenen Problemen, wie zum Beispiel Speicherplatzverschwendung durch Redundanz, unbefugte Zugriffe, wenn sich z. B. Dateien in Verzeichnissen oder Dateisystemen befinden, die Dritten zugänglich gemacht werden oder nicht konsistente Versionsstände.

### 2 6 Ungeeignete Aufstellung des Fileserver

Werden Fileserver an leicht zugänglichen Orten aufgestellt, können Angreifer direkt auf deren Komponenten und damit auf die gespeicherten Daten zugreifen, z. B. indem sie Laufwerke abziehen oder ausbauen und mitnehmen. Kleinere NAS-Systeme können zudem leicht komplett gestohlen werden. Ebenso ist es möglich, dass ein Angreifer die Zugriffsbeschränkungen am Fileserver direkt aushebelt und so schützenswerte Daten einsehen kann. Hat er erst einmal Zugriff, kann er auch Schadprogramme einspielen und so die Sicherheit des gesamten Netzes gefährden. 

### 2 7 Fehlendes oder unzureichendes Datensicherungskonzept

Fällt ein Fileserver komplett aus, sind einzelne Komponenten defekt oder löscht ein Mitarbeiter Dateien unbeabsichtigt, können ohne ein funktionierendes Backup wichtige Daten verloren gehen. Sollte zudem kein RAID (Redundant Array of Independent Disks) eingesetzt werden, wirkt sich der Ausfall eines einzelnen Datenträgers direkt auf den laufenden Betrieb aus, da die Dateien nicht mehr verfügbar sind.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Fileserver aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.3.3.A1 Geeignete Aufstellung [Haustechnik]

Fileserver DÜRFEN NICHT in Büroräumen oder als Arbeitsplatzrechner betrieben werden. Sie MÜSSEN an Orten aufgestellt werden, zu denen nur berechtigte Personen Zutritt haben. Zudem MUSS auf eine schwingungsfreie bzw. erschütterungsfreie Umgebung des Fileservers geachtet werden. Auch Fileserver mit weiteren Funktionen, wie NAS-Systeme kombiniert mit einem WLAN-Access-Point oder mit Direktanschlüssen für Speicherkarten, MÜSSEN geeignet aufgestellt werden. Des Weiteren MUSS eine sichere Stromversorgung und entsprechend den Herstellervorgaben empfohlene Umgebungstemperatur und Luftfeuchte sichergestellt sein.

#### APP.3.3.A2 Einsatz von RAID-Systemen

Es MUSS geplant werden, ob im Fileserver ein RAID-System eingesetzt wird. Eine Entscheidung gegen ein solches System MUSS nachvollziehbar dokumentiert werden. Wenn ein RAID-System eingesetzt werden soll, MUSS entschieden werden: 

* welches RAID-Level benutzt werden soll, um die Datenträger logisch zusammenzufassen, 
* wie lang die Zeitspanne für einen RAID-Rebuild-Prozess sein darf und 
* ob ein Software- oder ein Hardware-RAID eingesetzt werden soll. 
Die RAID-Level MÜSSEN dem Stand der Technik entsprechen. Bei einem Hardware-RAID SOLLTE der RAID-Controller redundant ausgelegt sein. In einem RAID SOLLTEN Hotspare-Festplatten vorgehalten werden.

#### APP.3.3.A3 Einsatz von Antiviren-Programmen

Je nach Betriebssystem und anderen vorhandenen Schutzmechanismen MUSS der Fileserver in das Konzept zum Schutz vor Schadprogrammen der Institution einbezogen werden. Das eingesetzte Antiviren-Programm MUSS die über den Fileserver freigegebenen Dateien regelmäßig überprüfen. Neben Echtzeit- und On-Demand-Scans MUSS die eingesetzte Lösung auch komprimierte Dateien nach Schadprogrammen durchsuchen können. Darüber hinaus SOLLTE sie auch verschlüsselte Dateien prüfen können.

Alle Daten MÜSSEN durch die Antiviren-Lösung auf Schadsoftware untersucht werden, bevor sie auf dem Speichermedium abgelegt werden. Sowohl die Virensignaturen als auch die Antiviren-Software selbst MÜSSEN laufend aktualisiert werden. Es MUSS sichergestellt sein, dass Benutzer keine sicherheitsrelevanten Änderungen an den Einstellungen der Antiviren-Lösung vornehmen können.

#### APP.3.3.A4 Regelmäßige Datensicherung

Es MÜSSEN regelmäßig alle auf dem Fileserver befindlichen Daten gesichert werden. Dazu MUSS ein Datensicherungskonzept erstellt werden, das unter anderem definiert, in welchen Intervallen das Backup durchgeführt werden soll. Außerdem MUSS eine Datensicherung durchgeführt werden, wenn auf dem Fileserver etwas installiert oder neu konfiguriert wird. Alle gesicherten Daten MÜSSEN sich jederzeit wiederherstellen lassen. Dabei SOLLTE die maximale Wiederanlaufzeit erhoben und im Datensicherungskonzept berücksichtigt werden.

#### APP.3.3.A5 Restriktive Rechtevergabe

Zugriffsrechte auf die vom Fileserver verwalteten Dateien MÜSSEN restriktiv vergeben werden. Es MUSS sichergestellt sein, dass jeder Benutzer nur auf die Daten zugreifen kann, die er benötigt, um seine Aufgaben zu erfüllen. Systemverzeichnisse und -dateien DÜRFEN NICHT für unbefugte Benutzer freigegeben werden. 

Es MUSS regelmäßig überprüft werden, ob die Zugriffsberechtigungen noch aktuell sind und der Sicherheitsrichtlinie entsprechen. Zudem MUSS es einen definierten Prozess geben, um Berechtigungen neu einzurichten, zu ändern oder zu entziehen. Alle Zugriffsrechte MÜSSEN nachvollziehbar dokumentiert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Fileserver. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.3.3.A6 Beschaffung eines Fileservers

Bevor ein Fileserver beschafft wird, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Die Leistung, die Speicherkapazität, die Bandbreite sowie die Anzahl der Benutzer, die den Fileserver nutzen sollen, SOLLTE bei der Beschaffung des Fileservers berücksichtigt werden.

#### APP.3.3.A7 Auswahl eines Dateisystems

Es SOLLTE eine Anforderungsliste erstellt werden, anhand derer die Dateisysteme bewertet werden. Um Transaktionssicherheit zu gewährleisten, SOLLTE das Dateisystem eine Journaling-Funktion bieten. Auch SOLLTE es über einen Schutzmechanismus verfügen, der verhindert, dass zwei Benutzer oder Anwendungen zur gleichen Zeit schreibend auf eine Datei zugreifen. Es SOLLTE ein Dateisystem ausgewählt werden, das eine festgelegte Overhead-Grenze nicht überschreitet. Für Hochverfügbarkeitslösungen SOLLTEN verteilte Dateisysteme verwendet werden.

#### APP.3.3.A8 Strukturierte Datenhaltung [Benutzer]

Es SOLLTE eine Struktur festgelegt werden, nach der Daten abzulegen sind. Benutzer SOLLTEN regelmäßig über die geforderte strukturierte Datenhaltung informiert werden. Es SOLLTE schriftlich festgelegt werden, welche Daten lokal und welche auf dem Fileserver gespeichert werden dürfen. Programm- und Arbeitsdaten SOLLTEN getrennt gespeichert werden. Es SOLLTE regelmäßig überprüft werden, ob die Vorgaben zur strukturierten Datenhaltung eingehalten werden. 

#### APP.3.3.A9 Sicheres Speichermanagement

Es SOLLTEN alle Speicherressourcen des Fileservers katalogisiert werden, z. B. Festplatten, Flash-Speicher, Bandlaufwerke. Zudem SOLLTE regelmäßig überprüft werden, ob die Speicher noch wie vorgesehen funktionieren. Um bei Engpässen schnell reagieren zu können, SOLLTEN Ersatzspeicher vorgehalten werden. 

Wurde eine Speicherhierarchie (Primär-, Sekundär- bzw. Tertiärspeicher) aufgebaut, SOLLTE ein (teil-)automatisiertes Speichermanagement verwendet werden. Werden Daten automatisiert verteilt, SOLLTE regelmäßig manuell überprüft werden, ob das korrekt funktioniert.

Weiterhin SOLLTEN die eingesetzten Speicher in das Protokollierungskonzept des Informationsverbunds einbezogen werden. Folgende Ereignisse SOLLTEN mindestens protokolliert werden:

* Aktivitäten (Modifizieren, Hinzufügen bzw. Löschen von Daten),
* nicht autorisierte Zugriffe auf Daten und
* Änderungen von Zugriffsrechten.
#### APP.3.3.A10 Regelmäßige Tests des Datensicherungs- bzw. Wiederherstellungskonzepts

Es SOLLTE regelmäßig getestet werden, ob die Datensicherung und -wiederherstellung korrekt funktioniert. Dafür SOLLTE ein Zeitplan ausgearbeitet werden. Es SOLLTEN genügend Ressourcen bereitgestellt werden, um die Tests planen, konzipieren und durchführen zu können. 

Die Ergebnisse SOLLTEN ausreichend dokumentiert werden. Aufgedeckte Mängel SOLLTEN dazu führen, dass das Datensicherungskonzept überarbeitet wird.

#### APP.3.3.A11 Einsatz von Quotas

Es SOLLTE überlegt werden, Quotas einzurichten. Alternativ SOLLTEN Mechanismen des verwendeten Datei- oder Betriebssystemsystems genutzt werden, die die Benutzer bei einem bestimmten Füllstand der Festplatte warnen oder nur noch dem Systemadministrator Schreibrechte einräumen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.3.A12 Verschlüsselung des Datenbestandes(CI)

Alle Daten auf dem Fileserver SOLLTEN verschlüsselt werden. Dazu SOLLTEN die Datenträger vollständig verschlüsselt werden. Es SOLLTE sichergestellt werden, dass der Virenschutz die verschlüsselte Dateien auf Schadsoftware prüfen kann.Kryptografische Schüssel SOLLTEN sicher erzeugt und von den Daten getrennt aufbewahrt werden (siehe auch CON.1 Kryptokonzept).

#### APP.3.3.A13 Replizieren zwischen Standorten(A)

Für hochverfügbare Systeme SOLLTE eine angemessene Replikation der Daten auf mehreren Datenträgern stattfinden. Daten SOLLTEN zudem zwischen unabhängigen Geräten oder unabhängigen Standorten repliziert werden. Dafür SOLLTE ein geeigneter Replikationsmechanismus ausgewählt werden. Damit die Replikation wie vorgesehen funktionieren kann, SOLLTEN hinreichend genaue Zeitdienste genutzt und betrieben werden.

#### APP.3.3.A14 Einsatz von Error-Correction-Codes(I)

Es SOLLTEN grundsätzlich fehlererkennende bzw. fehlerkorrigierende Codes eingesetzt werden, um Daten zu speichern. Die notwendigen redundanten Bits SOLLTEN bei der Planung miteinbezogen werden. Es SOLLTE beachtet werden, dass je nach eingesetztem Verfahren Fehler nur mit einer gewissen Wahrscheinlichkeit erkannt und auch nur in begrenzter Größenordnung behoben werden können.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Fileserver" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [HVK] Hochverfügbarkeitskompendium

  

 BSI, (zuletzt abgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Fileserver" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.44 Unbefugtes Eindringen in Räumlichkeiten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

