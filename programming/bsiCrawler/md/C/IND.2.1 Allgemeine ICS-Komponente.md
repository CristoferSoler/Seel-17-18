1 Beschreibung
--------------

### 1.1 Einleitung

Eine ICS-Komponente ist eine elektronische Komponente, die eine Maschine oder Anlage steuert oder regelt. Sie ist damit Bestandteil eines industriellen Steuerungssystems (engl. Industrial Control System, ICS) oder allgemeiner einer Betriebstechnik (engl. Operational Technology, OT). Solche Komponenten können Speicherprogrammierbare Steuerungen (SPS, engl. Programmable Logic Controller, PLC), Sensoren, Aktoren, eine Maschine oder andere Teile eines ICS sein.

Aufgrund der im OT-Umfeld typischen hohen Verfügbarkeitsanforderungen und der oft extremen Umgebungsbedingungen (Klima, Staub, Vibration, Korrosion) wurden ICS-Komponenten schon immer als robuste Geräte mit hoher Zuverlässigkeit und langer Lebensdauer konstruiert.

ICS-Komponenten werden normalerweise über Spezialsoftware des jeweiligen Herstellers konfiguriert bzw. programmiert. Das wird entweder über sogenannte Programmiergeräte (z. B. als Anwendung unter Windows oder Linux) oder über eine Engineering-Station durchgeführt, die die Anwendungsprogramme in die speicherprogrammierbaren Steuerungen lädt.

Die Rolle des Beauftragten für Informationssicherheit für den Bereich der industriellen Automatisierung wird je nach Art und Ausrichtung der Institution anders genannt. Eine weitere Bezeichnung neben ICS-Informationssicherheitsbeauftragter (ICS-ISB) ist auch Industrial Security Officer.

### 1.2 Zielsetzung

Ziel des Bausteins ist die Absicherung aller Arten von ICS-Komponenten, unabhängig von Hersteller, Bauart, Einsatzzweck und -ort. Er kann für ein einzelnes Gerät oder ein aus mehreren Komponenten aufgebautes modulares Gerät verwendet werden. 

### 1.3 Abgrenzung

Die Anforderungen sind für eine generische Komponente erarbeitet. Für spezifischere ICS-Komponenten sind unter IND.2 *ICS-Komponenten* zusätzliche Bausteine verfügbar, in denen Anforderungen beschrieben sind, die über die generischen Anforderungen dieses Bausteins hinausgehen und eventuell umgesetzt werden müssen. 

Der Baustein enthält keine organisatorischen Anforderungen zur Absicherung einer ICS-Komponente. Dafür müssen die Anforderungen des Bausteins IND.1 *Betriebs- und Steuerungstechnik* umgesetzt werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Allgemeine ICS-Komponente von besonderer Bedeutung: 

### 2 1 Beeinträchtigung durch schädliche Umgebungseinflüsse

ICS-Komponenten in industriellen Umgebungen sind häufig besonderen Bedingungen ausgesetzt, die den sicheren Betrieb beeinträchtigen können. Beispiele hierfür sind extreme Wärme, Kälte, Feuchtigkeit, Staub, Vibration oder auch ätzend oder korrodierend wirkende Atmosphären. Häufig treten auch mehrere Faktoren gleichzeitig auf. Durch solche schädlichen Umgebungseinflüsse können ICS-Komponenten schneller verschleißen und früher ausfallen. 

### 2 2 Unvollständige Dokumentation

ICS-Komponenten sind oft unvollständig dokumentiert, sodass nicht alle Produktfunktionen bekannt sind. Besonders lückenhaft sind häufig die Angaben über die verwendeten Dienste, Protokolle und Kommunikationsports sowie zur Berechtigungsverwaltung. Das erschwert die Gefährdungsanalyse, da Schnittstellen, Funktionen sowie sicherheitsrelevante Mechanismen übersehen werden. Dadurch können potenzielle Gefährdungen nicht berücksichtigt werden. Zudem kann nicht oder nur eingeschränkt auf neue Schwachstellen einer ICS-Komponente reagiert werden, wenn die verwendeten Dienste und Ports nicht vollständig erfasst sind. 

### 2 3 Unsichere Systemkonfiguration

Die Standardkonfiguration von ICS-Komponenten ist häufig darauf ausgelegt, dass die Komponenten korrekt funktionieren und sich leicht in Betrieb nehmen lassen. Sicherheitsmechanismen spielen dabei oft keine hinreichende Rolle. So sind in der Standardeinstellung häufig alle Dienste, Protokolle und Anschlüsse eingeschaltet und bleiben aktiv, auch wenn sie nicht benutzt werden. Ebenso bleiben voreingestellte Berechtigungen häufig unverändert.

Es ist für Angreifer leicht, solche Komponenten zu übernehmen und zu manipulieren. Ebenso ist es möglich, dass ein Angreifer die unsichere Systemkonfiguration ausnutzt, um die ICS-Komponente als Ausgangspunkt für weitere Angriffe zu nutzen. In der Folge können geschäftskritische Informationen abfließen oder auch der gesamte Betrieb der Institution beeinträchtigt werden. 

### 2 4 Unzureichendes Benutzer- und Berechtigungsmanagement

Einige ICS-Komponenten verfügen über ein eigenes Benutzer- und Berechtigungsmanagement. Ist dieses unzureichend konzipiert, kann es passieren, dass Mitarbeiter gemeinsam Benutzerkonten nutzen oder dass Berechtigungen von ausgeschiedenen Mitarbeitern oder Dienstleistern nicht gelöscht werden. Insgesamt können so unberechtigte Personen auf ICS- Komponenten zugreifen.

### 2 5 Unzureichende Protokollierung

Bei ICS-Komponenten beschränkt sich die Protokollierung häufig auf prozessrelevante Ereignisse. Für die Informationssicherheit relevante Daten werden oft nicht aufgezeichnet. Dadurch lassen sich Sicherheitsvorfälle nur schwer detektieren und auch hinterher nicht mehr rekonstruieren. 

### 2 6 Manipulation und Sabotage einer ICS-Komponente

Die vielfältigen Schnittstellen von ICS-Komponenten führen zu einem erhöhten Manipulationsrisiko für Systeme, Software und übertragene Informationen. Je nach Motivation und Kenntnissen des Täters kann sich das lokal aber auch standortübergreifend auswirken. Zudem können Status- und Alarmmeldungen oder sonstige Messwerte unterdrückt oder verändert werden.

Manipulierte Messwerte können Fehlentscheidungen von ICS-Komponenten bzw. des Bedienpersonals nach sich ziehen. Manipulierte Systeme können dazu genutzt werden, um andere Systeme oder Standorte anzugreifen oder um eine laufende Manipulation zu vertuschen.

### 2 7 Einsatz unsicherer Protokolle

Die im Umfeld industrieller Steuerungsanlagen eingesetzten Protokolle bieten teilweise keine oder nur eingeschränkte Sicherheitsmechanismen. Technische Informationen wie Mess- und Steuerwerte werden häufig im Klartext und ohne Integritätssicherung oder Authentifizierung übertragen. Ein Angreifer mit Zugang zum Übertragungsmedium kann dann die Inhalte der Kommunikation auslesen und verändern oder Steuerbefehle einschleusen und so Handlungen provozieren bzw. den Betrieb direkt beeinflussen. Ein Angriff auf Protokollebene ist auch dann möglich, wenn die ICS-Komponente ansonsten sicher konfiguriert ist und selbst keine Schwachstellen aufweist.

### 2 8 Denial-of-Service-(DoS)-Angriffe

Ein Angreifer kann den Betrieb von ICS-Komponenten durch DoS-Angriffe beeinträchtigen. Bei unter Echtzeitbedingungen ablaufenden Prozessen kann bereits eine kürzere Störung zu Informations- oder Kontrollverlust führen. 

### 2 9 Schadprogramme

Die von Schadprogrammen ausgehende Bedrohung verschärft sich auch in industriellen Steuerungsanlagen immer mehr. Infektionsmöglichkeiten ergeben sich durch Schnittstellen zur Außenwelt und zur Office-IT (vertikale Integration) aber auch durch mobile Endgeräte wie Service-Notebooks oder durch Wechseldatenträger bei der Programmierung und Wartung von ICS-Komponenten. Durch letztere können Schadprogramme auch in isolierte Umgebungen (Überwindung des "air gap") eingebracht werden.

### 2 10 Ausspionieren von Informationen

ICS-Komponenten enthalten häufig detaillierte Informationen über den geregelten oder überwachten Prozess bzw. Vorgang. Auch aus sonstigen übertragenen Werten, wie Mess- oder Steuerungsdaten, lassen sich diese Informationen teilweise rekonstruieren. Gleiches gilt für Steuerungsprogramme oder -parameter.

Angreifer könnten hier an Geschäftsgeheimnisse gelangen (Industriespionage), z. B. Rezepte, Verfahren oder anderes geistiges Eigentum. Auch können sie Informationen über die Funktionsweise einer ICS-Komponente und ihrer Sicherheitsmechanismen gewinnen, die sie für weitere Angriffe benutzen können.

### 2 11 Unzureichende Sicherheitsanforderungen bei der Beschaffung

Aus mangelndem Bewusstsein für die Risiken und aus Kostengründen wird bei der Beschaffung häufig die Informationssicherheit nicht berücksichtigt. Dadurch können in ICS-Komponenten mitunter schwerwiegende Schwachstellen enthalten sein, die sich später nur sehr aufwändig beheben lassen.

### 2 12 Manipulierte Firmware

Bei ICS-Komponenten lässt sich neben dem Anwendungsprogramm auch das Betriebssystem (Firmware) verändern. Hierdurch kann manipulierte Software in das System gelangen. Die internen Speicher könnten durch ein kompromittiertes Programmiergerät, über eine lokale Datenschnittstelle (z. B. USB) oder über eine andere bestehende Netzverbindung durch einen Angreifer verändert werden. Ebenso könnte ein Software-Update auf dem Weg vom Hersteller zum Betreiber manipuliert worden sein. Schließlich könnte eine Komponente mit bereits kompromittierter Firmware beim Betreiber eintreffen, etwa bei manipulierter Lieferkette (engl. supply chain) oder Einkauf aus unsicheren Quellen. Ein Angreifer erhält dadurch die Möglichkeit, Prozesse und Abläufe zu verändern bzw. zu verfälschen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Allgemeine ICS-Komponente aufgeführt. Grundsätzlich ist der ICS-Informationssicherheitsbeauftragte (ICS-ISB) für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### IND.2.1.A1 Einschränkung des Zugriffs für Konfigurations- und Wartungsschnittstellen [ICS-Administrator]

Es MUSS sichergestellt werden, dass nur berechtigte Mitarbeiter auf Konfigurations- und Wartungsschnittstellen von ICS-Komponenten zugreifen können. Die Konfiguration DARF NUR nach einer Freigabe an der ICS-Komponente oder einer Authentisierung geändert werden.

Standardmäßig eingerichtete bzw. herstellerseitig gesetzte Passwörter MÜSSEN gewechselt werden. Der Wechsel MUSS dokumentiert und das Passwort sicher hinterlegt werden. Standardmäßig eingerichtete bzw. herstellerseitig gesetzte Benutzerkonten SOLLTEN gewechselt werden.

#### IND.2.1.A2 Nutzung sicherer Protokolle für die Konfiguration und Wartung [ICS-Administrator, Wartungspersonal]

Für die Konfiguration und Wartung von ICS-Komponenten MÜSSEN sichere Protokolle benutzt werden. Die Daten DÜRFEN NICHT ungeschützt übertragen werden. 

#### IND.2.1.A3 Protokollierung [ICS-Administrator]

Es MUSS festgelegt werden:

* welche Daten/Ereignisse protokolliert werden sollen, 
* wie lange die Protokolldaten aufbewahrt werden und 
* wer diese einsehen darf. 
Generell MÜSSEN alle sicherheitsrelevanten Systemereignisse protokolliert und bei Bedarf ausgewertet werden. 

#### IND.2.1.A4 Deaktivierung nicht genutzter Dienste, Funktionen und Schnittstellen [ICS-Administrator, Wartungspersonal]

Alle nicht genutzten Dienste, Funktionen und Schnittstellen der ICS-Komponenten MÜSSEN deaktiviert oder deinstalliert werden.

#### IND.2.1.A5 Deaktivierung nicht benutzter Benutzerkonten [ICS-Administrator]

Nicht benutzte und unnötige Benutzerkonten MÜSSEN deaktiviert werden.

#### IND.2.1.A6 Netzsegmentierung [ICS-Administrator]

ICS-Komponenten MÜSSEN von der Office-IT getrennt werden. Sind ICS-Komponenten von anderen Diensten im Netz abhängig, SOLLTE das ausreichend dokumentiert werden. ICS-Komponenten SOLLTEN so wenig wie möglich mit anderen ICS-Komponenten kommunizieren.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeine ICS-Komponente. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### IND.2.1.A7 Backups [Leitstellen-Operator]

Von Programmen und Daten MÜSSEN regelmäßig und nach Systemänderungen Backups erstellt werden. 

#### IND.2.1.A8 Schutz vor Schadsoftware [ICS-Administrator]

ICS-Komponenten SOLLTEN durch geeignete Mechanismen vor Schadprogrammen geschützt werden. Wird dafür ein Virenschutzprogramm benutzt, SOLLTEN das Programm und die Virensignaturen immer auf dem aktuellen Stand sein. Wenn die Ressourcen auf der ICS-Komponente nicht ausreichend oder die Echtzeitanforderung durch den Einsatz von Virenschutzprogrammen gefährdet werden könnte, SOLLTEN alternative Maßnahmen, wie z. B. die Abschottung der Komponente oder des Produktionsnetzes, ergriffen werden.

#### IND.2.1.A9 Dokumentation der Kommunikationsbeziehungen [ICS-Administrator]

Es SOLLTE dokumentiert werden, mit welchen Systemen eine ICS-Komponente welche Daten austauscht. Außerdem SOLLTEN die Kommunikationsverbindungen neu integrierter ICS-Komponenten dokumentiert werden.

#### IND.2.1.A10 Systemdokumentation [Leitstellen-Operator, ICS-Administrator]

Es SOLLTE eine erweiterte Systemdokumentation erstellt werden. Darin SOLLTEN Besonderheiten im Betrieb (z. B. Sicherung, Regelwartungsmaßnahmen, Austausch und Wiederherstellung von Komponenten, Leistungen Dritter) und die Möglichkeiten zur Systemverwaltung (z. B. Fernzugriff) festgehalten werden. Außerdem SOLLTE dokumentiert werden, wenn ICS-Komponenten verändert wurden. Es SOLLTE sichergestellt sein, dass nur berechtigte Mitarbeiter auf die Systemdokumentation zugreifen können. Auch SOLLTE die Dokumentation im Störungsfall noch verfügbar sein.

#### IND.2.1.A11 Wartung der ICS-Komponenten [Wartungspersonal, Leitstellen-Operator, ICS-Administrator]

Bei der Wartung einer ICS-Komponente SOLLTEN immer die aktuellen und freigegebenen Sicherheitsupdates eingespielt werden. Updates für das Betriebssystem SOLLTEN erst nach Freigabe durch den Hersteller einer Komponente installiert werden oder die Aktualisierung SOLLTE in einer Testumgebung getestet werden, bevor diese in einer produktiven Komponente eingesetzt wird. Für kritische Sicherheitsupdates SOLLTE kurzfristig eine Wartung durchgeführt werden. 

#### IND.2.1.A12 Beschaffung von ICS-Komponenten [Leitstellen-Operator, ICS-Administrator]

Für ICS-Komponenten SOLLTEN einheitliche und dem Schutzbedarf angemessene Anforderungen an die Informationssicherheit definiert werden. Diese SOLLTEN berücksichtigt werden, wenn neue ICS-Komponenten beschafft werden.

#### IND.2.1.A13 Geeignete Inbetriebnahme der ICS-Komponenten [ICS-Administrator]

Bevor ICS-Komponenten in Betrieb genommen werden, SOLLTEN sie dem aktuellen intern freigegeben Firmware-, Software- und Patch-Stand entsprechen. 

Neue ICS-Komponenten SOLLTEN in die bestehenden Betriebs-, Überwachungs- und Informationssicherheitsmanagement-Prozesse eingebunden werden. Das SOLLTE insbesondere 

* die Änderungs- und Berechtigungsverwaltung, 
* das Schwachstellenmanagement, 
* den Schutz vor Schadsoftware, 
* die betriebliche Überwachung sowie Notfallplanung und 
* regelmäßige Sicherheitsüberprüfung der Systeme 
umfassen.

#### IND.2.1.A14 Aussonderung von ICS-Komponenten [ICS-Administrator]

Bei der Aussonderung von alten oder defekten ICS-Komponenten SOLLTEN alle schützenswerten Daten sicher gelöscht werden. Es SOLLTE insbesondere sichergestellt sein, dass alle Zugangsdaten nachhaltig entfernt wurden.

#### IND.2.1.A15 Zentrale Systemprotokollierung und -überwachung [ICS-Administrator]

Alle ICS-Komponenten SOLLTEN ihre Protokollierungsdaten an ein zentrales System übermitteln. Die protokollierten Daten SOLLTEN regelmäßig ausgewertet werden. Bei sicherheitskritischen Ereignissen SOLLTE eine automatische Alarmierung erfolgen. 

#### IND.2.1.A16 Schutz externer Schnittstellen [ICS-Administrator]

Von außen erreichbare Schnittstellen, z. B. Netzschnittstellen, USB-Ports oder serielle Anschlüsse, SOLLTEN vor Missbrauch geschützt werden.

#### IND.2.1.A17 Nutzung sicherer Protokolle für die Übertragung von Informationen [ICS-Administrator]

Mess- oder Steuerdaten SOLLTEN vor unberechtigten Zugriffen oder Veränderungen geschützt werden. Bei Anwendungen mit Echtzeitanforderungen SOLLTE geprüft werden, ob dies notwendig und umsetzbar ist. Werden Mess- oder Steuerdaten über öffentliche Netze übertragen, SOLLTEN sie angemessen geschützt werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### IND.2.1.A18 Kommunikation im Störfall [Leitstellen-Operator, ICS-Administrator](A)

Es SOLLTE alternative und unabhängige Kommunikationsmöglichkeiten geben, die bei einem Störfall benutzt werden können, um handlungsfähig zu bleiben. 

#### IND.2.1.A19 Security-Tests [ICS-Administrator](CIA)

Mithilfe von regelmäßigen Security-Tests SOLLTE geprüft werden, ob die technischen Sicherheitsmaßnahmen noch effektiv umgesetzt sind. Die Security Tests SOLLTEN nicht im laufenden Anlagenbetrieb erfolgen. Die Tests SOLLTEN auf die Wartungszeiten geplant werden. Die Ergebnisse SOLLTEN dokumentiert werden. Erkannte Risiken SOLLTEN bewertet und behandelt werden. 

#### IND.2.1.A20 Vertrauenswürdiger Code [ICS-Administrator](IA)

Firmware-Updates oder neue Steuerungsprogramme SOLLTEN nur eingespielt werden, wenn vorher ihre Integrität und Authentizität überprüft wurde. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeine ICS-Komponente" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [AHWAST] Ausführungshinweise zur Anwendung des Whitepaper - Anforderungen an sichere Steuerungs- und Telekommunikationssysteme (Version 1.1, 2014)

  

 BDEW Bundesverband der Energie- und Wasserwirtschaft e.V. und Oesterreichs E-Wirtschaft, Version 1.1, 2014  
 [https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
* #### [ICSSK] ICS-Security-Kompendium

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2016  
 [https://www.bsi.bund.de/DE/Themen/Industrie\_KRITIS/Empfehlungen/ICS/empfehlungen\_node.html](https://www.bsi.bund.de/DE/Themen/Industrie_KRITIS/Empfehlungen/ICS/empfehlungen_node.html)

 
* #### [ICSSKfH] ICS-Security-Kompendium für Hersteller und Integratoren

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014  
 <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.html>

 
* #### [NIST80082] NIST Special Publication 800-82, Revision 2

  

 Guide to Industrial Control Systems (ICS) Security, National Institute of Standards and Technology (NIST), 2015  
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2.pdf)

 
* #### [WAST] Whitepaper Anforderungen an sichere Steuerungs- und Telekommunikationssysteme

  

 BDEW Bundesverband der Energie- und Wasserwirtschaft e.V, Version 1.1, 01.2015  
 [https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeine ICS-Komponente" von Bedeutung.

* G 0.2 Ungünstige klimatische Bedingungen
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.10 Ausfall oder Störung von Versorgungsnetzen
* G 0.12 Elektromagnetische Störstrahlung
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.37 Abstreiten von Handlungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

