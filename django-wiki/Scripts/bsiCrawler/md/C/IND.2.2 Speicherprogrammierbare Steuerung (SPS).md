1 Beschreibung
--------------

### 1.1 Einleitung

Eine speicherprogrammierbare Steuerung (SPS, engl. Programmable Logic Controller, PLC) ist eine ICS-Komponente. Sie übernimmt Steuerungs- und Regelaufgaben in der Betriebstechnik (engl. Operational Technology, OT). Die Grenzen zwischen verschiedenen Geräteklassen und Bauformen sind heute fließend: So kann zum Beispiel auch ein Fernwirkgerät (engl. Remote Terminal Unit, RTU) die Funktionen einer SPS übernehmen oder ein Programmable Automation Controller (PAC) kann versuchen, die Vorteile einer SPS und eines Industrie-PCs zu vereinen. Jedoch ist die SPS immer noch das klassische Automatisierungsgerät, sodass in diesem Baustein diese Begriffe synonym verwendet werden. 

Eine SPS verfügt über digitale Ein- und Ausgänge, ein Echtzeitbetriebssystem (Firmware) sowie weitere Schnittstellen für Ethernet oder Feldbusse. Die Verbindung zu Sensoren und Aktoren erfolgt über die analogen oder digitalen Ein- bzw. Ausgänge oder über einen Feldbus. Die Kommunikation mit Prozessleitsystemen findet meist über die Ethernet-Schnittstelle und IP-basierte Netze statt.

Die möglichen Realisierungen sind vielfältig: SPSen können als Baugruppe, Einzelgerät, PC-Einsteckkarte (Slot-SPS) oder als Software-Emulation (Soft-SPS) eingesetzt werden. Am häufigsten anzutreffen sind modulare SPSen, die aus verschiedenen funktionalen Steckmodulen zusammengesetzt werden. Zunehmend werden auch weitere Funktionen wie das Visualisieren, Alarmieren und Protokollieren durch die SPS realisiert.

Aufgrund der im OT-Umfeld typischen hohen Verfügbarkeitsanforderungen und der oft extremen Umgebungsbedingungen (Klima, Staub, Vibration, Korrosion) wurden ICS-Komponenten schon immer als robuste Geräte mit hoher Zuverlässigkeit und langer Lebensdauer konstruiert.

SPSen werden normalerweise über Spezialsoftware des jeweiligen Herstellers konfiguriert bzw. programmiert. Das wird entweder über sogenannte Programmiergeräte (z. B. als Anwendung unter Windows oder Linux) oder über eine Engineering-Station durchgeführt, die die Daten über ein Netz verteilt.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, alle Arten von speicherprogrammierbaren Steuerungen abzusichern, unabhängig von Hersteller, Bauart, Einsatzzweck und -ort. Er kann für eine einzelne SPS oder eine zusammenhängende, als SPS eingesetzte Baugruppe angewendet werden.

### 1.3 Abgrenzung

Der vorliegende Systembaustein ist anzuwenden, um alle Arten von speicherprogrammierbaren Steuerungen (d. h. SPSen und Geräte, die gleiche oder ähnliche Funktionen integrieren) abzusichern. Er ergänzt den Baustein IND.2.1 *Allgemeine ICS-Komponente*. Bei der Anwendung ist dieser daher auch zu berücksichtigen.

Der Baustein enthält keine organisatorischen Anforderungen zur Absicherung einer ICS-Komponente. Dafür müssen die Anforderungen des Bausteins IND.1 *Betriebs- und Steuerungstechnik* umgesetzt werden. Ebenso wird der Bereich funktionale Sicherheit (Safety) nicht behandelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich SPS von besonderer Bedeutung:

### 2 1 Unvollständige Dokumentation

Speicherprogrammierbare Steuerungen sind oft unvollständig dokumentiert, sodass nicht alle Produktfunktionen bekannt sind. Besonders lückenhaft sind häufig die Angaben über die verwendeten Dienste, Protokolle und Kommunikationsports sowie zur Berechtigungsverwaltung. Das erschwert jedoch die Gefährdungsanalyse, da Schnittstellen, Funktionen sowie sicherheitsrelevante Mechanismen übersehen werden. Dadurch können potenzielle Gefährdungen nicht berücksichtigt werden. Zudem kann nicht oder nur eingeschränkt auf neue Schwachstellen reagiert werden, wenn diese nicht erfasst ist. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich SPS aufgeführt. Grundsätzlich ist der ICS-Informationssicherheitsbeauftragte (ICS-ISB) für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Speicherprogrammierbare Steuerung SPS. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### IND.2.2.A1 Erweiterte Systemdokumentation für speicherprogrammierbare Steuerungen [ICS-Administrator]

Steuerungsprogramme und Konfigurationen SOLLTEN immer archiviert werden, wenn an ihnen etwas verändert wird. Änderungen an der Konfiguration oder der Tausch von Komponenten SOLLTEN vollständig dokumentiert werden.

#### IND.2.2.A2 Benutzerkontenkontrolle und restriktive Rechtevergabe [ICS-Administrator]

Zugriffsrechte auf Funktionen und Schnittstellen einer SPS SOLLTEN restriktiv vergeben werden. Bestehende Benutzerkonten SOLLTEN regelmäßig daraufhin überprüft werden, ob sie noch erforderlich sind, die zugewiesenen Berechtigungen noch stimmen. Wenn sich an den Zuständigkeiten der Mitarbeiter etwas ändert, SOLLTEN die Berechtigungen umgehend angepasst werden.

#### IND.2.2.A3 Zeitsynchronisation [ICS-Administrator]

Für die Systemzeit SOLLTE eine zentrale automatisierte Zeitsynchronisation eingerichtet werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Speicherprogrammierbare Steuerung (SPS)" finden sich unter anderem in folgenden Veröffentlichungen

5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Speicherprogrammierbare Steuerung (SPS)" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.41 Sabotage
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

