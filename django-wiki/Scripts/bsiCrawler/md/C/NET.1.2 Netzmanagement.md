1 Beschreibung
--------------

### 1.1 Einleitung

Ein zuverlässiges Netzmanagement ist Grundvoraussetzung für den sicheren und effizienten Betrieb moderner Netze. Dazu ist es erforderlich, dass das Netzmanagement alle Netzkomponenten umfassend integriert und geeignete Maßnahmen umsetzt, um die Management-Kommunikation und -Infrastruktur zu schützen.

Das Netzmanagement umfasst viele wichtige Funktionen, wie z. B. die Netzüberwachung, die Konfiguration der Komponenten, die Ereignisbehandlung und die Protokollierung. Eine weitere wichtige Funktion ist das Reporting, das als gemeinsame Plattform für Netz und IT-Systeme angelegt werden kann. Alternativ kann es dediziert als einheitliche Plattform oder als Bestandteil der einzelnen Management-Komponenten realisiert werden.

Die Netzmanagement-Infrastruktur besteht aus zentralen Management-Systemen (z. B. SNMP-Server), Administrations-Endgeräten mit Software für Management-Zugriffe, dezentralen Management-Agenten, dedizierten Management-Werkzeugen (z. B. Probes bzw. spezifische Messgeräte), Management-Protokollen (z. B. SNMP oder SSH) sowie Management-Schnittstellen (z. B. dedizierte Ethernet-Ports oder Konsolen-Ports).

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, die Informationssicherheit als integralen Bestandteil des Netzmanagements zu etablieren.

### 1.3 Abgrenzung

Dieser Baustein betrachtet die notwendigen Komponenten und konzeptionellen Aufgaben zum Netzmanagement. Das Pendant im Systemmanagement für vernetzte Clients und Server wird im Baustein SYS.5 *Systemmanagement* beschrieben.

Der vorliegende Baustein konkretisiert die grundsätzlichen Vorgaben des Bausteins NET.1.1 *Netz-Architektur und -Design. *Er behandelt außerdem, wie das Netzmanagement aufgebaut und abgesichert sowie die zugehörige Kommunikation geschützt werden kann. Details bezüglich der Absicherung von Netzkomponenten, insbesondere deren Management-Schnittstellen, werden jedoch in den Bausteingruppen NET.2 und NET.3 behandelt.

Das Management der passiven Netzinfrastruktur wird in den Bausteinen der Infrastruktur (Bausteinschicht INF) bzw. der industriellen IT (Bausteinschicht IND) behandelt. Daher werden diese Themen im Rahmen dieses Bausteins nicht ausgeführt.

Die in diesem Baustein thematisierte Protokollierung sollte in ein übergreifendes Protokollierungs- und Archivierungskonzept eingebunden sein. (siehe OPS.1.1.5 *Protokollierung*).

Auf das Thema Outsourcing geht der vorliegende Baustein nicht im Detail ein. Weitergehende Anforderungen dazu beschreibt der Baustein OPS.2.1 *Outsourcing*.

Allgemeine Gesichtspunkte zum sicheren, effizienten und geordneten Betrieb des Netzmanagements werden in diesem Baustein nur beschrieben, wenn es über die allgemeinen Anforderungen des Bausteins OPS.1.1.1 *Allgemeiner IT-Betrieb *hinaus geht.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Netzmanagement von besonderer Bedeutung:

### 2 1 Unberechtigter Zugriff auf zentrale Netzmanagement-Komponenten

Gelingt es Angreifern, auf Netzmanagement-Lösungen zuzugreifen, z. B. durch ungepatchte Sicherheitslücken oder eine ungenügende Netztrennung, können sie alle dort angeschlossenen Netzkomponenten kontrollieren und neu konfigurieren. So können sie z. B. auf schützenswerte Informationen zugreifen, Netzverkehr umleiten oder auch das gesamte Netz nachhaltig stören. 

### 2 2 Unberechtigter Zugriff auf einzelne Netzkomponenten

Wenn es Angreifern gelingt, auf einzelne Netzkomponenten zuzugreifen, können sie die jeweilige Komponente kontrollieren und manipulieren. Jeder über die Netzkomponente geleitete Datenverkehr kann somit kompromittiert werden. Darüber hinaus können weiterführende Angriffe vorbereitet werden, um tiefer in das Netz der Institution einzudringen. 

### 2 3 Unberechtigte Eingriffe in die Netzmanagement-Kommunikation

Wird die Management-Kommunikation abgehört und manipuliert, können auf diesem Weg aktive Netzkomponenten fehlkonfiguriert bzw. kontrolliert werden. Hierdurch kann die Netzintegrität verletzt und die Verfügbarkeit der Netzinfrastruktur eingeschränkt werden. Außerdem können die übertragenen Daten mitgeschnitten und eingesehen.

### 2 4 Unzureichende Zeitsynchronisation der Netzmanagement-Komponenten

Wird die Systemzeit der Netzmanagement-Komponenten unzureichend synchronisiert, können die Protokollierungsdaten eventuell nicht miteinander korreliert werden bzw. kann die Korrelation zu eventuell fehlerhaften Aussagen führen, da die unterschiedlichen Zeitstempel von Ereignissen keine gemeinsame Basis aufweisen. Damit kann nicht geeignet auf eingetretene Ereignisse regiert werden und Probleme können nicht beseitigt werden. Dadurch können beispielsweise Sicherheitsvorfälle und Datenabflüsse unerkannt bleiben.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen an das Netzmanagement aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Darüber hinaus ist der Informationssicherheitsbeauftragte (ISB) bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist er dafür verantwortlich, dass alle Anforderungen gemäß den festgelegten Sicherheitsrichtlinien erfüllt und regelmäßig überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese Rollen sind in eckigen Klammern in der Überschrift der jeweiligen Anforderung aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.1.2.A1 Planung des Netzmanagements

Die Netzmanagement-Infrastruktur MUSS geeignet geplant werden. Hierbei SOLLTEN alle in der Sicherheitsrichtlinie und Anforderungsspezifikation adressierten Punkte sowie das Rollen- und Berechtigungskonzept berücksichtigt werden. Mindestens MÜSSEN folgende Themen berücksichtigt werden:

* zu trennende Management-Bereiche,
* Zugriffsmöglichkeiten auf die Management-Server,
* Kommunikation für den Management-Zugriff,
* benutzte Protokolle, z. B. IPv4 und IPv6,
* Anforderungen an Management-Werkzeuge,
* Schnittstellen, um erfasste Ereignis- oder Alarmmeldungen weiterzuleiten,
* Protokollierung, inklusive erforderlicher Schnittstellen zu einer zentralen Protokollierungslösung,
* Reporting und Schnittstellen zu übergreifenden Lösungen,
* korrespondierende Anforderungen an die einzubindenden Netzkomponenten.
#### NET.1.2.A2 Anforderungsspezifikation für das Netzmanagement [Leiter IT]

Ausgehend von NET.1.2A1 *Planung des Netzmanagements* MÜSSEN Anforderungen an die Netzmanagement-Infrastruktur und -Prozesse spezifiziert werden. Dabei MÜSSEN alle wesentlichen Elemente für das Netzmanagement berücksichtigt werden. Auch SOLLTE die Richtlinie für das Netzmanagement beachtet werden.

#### NET.1.2.A3 Rollen- und Berechtigungskonzept für das Netzmanagement

Es MUSS ein Rollen- und Berechtigungskonzept für das Netzmanagement erstellt, umgesetzt und gepflegt werden. Das Konzept MUSS die speziellen Tätigkeiten und den zugehörigen Zugriff auf Informationen im Netzmanagement abbilden.

#### NET.1.2.A4 Grundlegende Authentisierung für den Netzmanagement-Zugriff [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Für den Management-Zugriff auf Netzkomponenten und auf Managementinformationen MUSS eine geeignete Authentisierung verwendet werden. Dafür MÜSSEN die Vorgaben der Institution für die Authentisierungsgüte und den Umgang mit den Authentisierungsinformationen umgesetzt werden. Auch MÜSSEN alle Default-Passwörter auf den Netzkomponenten geändert werden. Die neuen Passwörter MÜSSEN ausreichend stark sein und regelmäßig geändert werden.

#### NET.1.2.A5 Einspielen von Updates und Patches

Die verantwortlichen Mitarbeiter MÜSSEN sich regelmäßig über bekannt gewordene Schwachstellen der eingesetzten Netzmanagement-Lösungen informieren und sicherheitsrelevante Updates und Patches so schnell wie möglich einspielen. Nicht sicherheitsrelevante Updates DÜRFEN NICHT die Sicherheit und Stabilität der Netzmanagement-Lösung beeinträchtigen. 

#### NET.1.2.A6 Regelmäßige Datensicherung

Alle eingesetzten Netzmanagement-Lösungen MÜSSEN ins Datensicherungskonzept der Institution eingebunden werden (siehe CON.3* Datensicherungskonzept*). Hierbei MÜSSEN alle spezifischen Daten für das Netzmanagement berücksichtigt werden. Es MÜSSEN mindestens die Systemdaten für die Einbindung der zu verwaltenden Komponenten bzw. Objekte, Ereignismeldungen, Statistikdaten sowie vorgehaltene Daten für das Konfigurationsmanagement gesichert werden.

#### NET.1.2.A7 Grundlegende Protokollierung von Ereignissen

Die Netzmanagement-Lösung MUSS in das Protokollierungskonzept der Institution eingebunden werden (siehe OPS.1.1.5 *Protokollierung*). Darüber hinaus MÜSSEN mindestens folgende Ereignisse protokolliert werden: unautorisierte Zugriffe bzw. Zugriffsversuche, Leistungs- oder Verfügbarkeitsschwankungen des Netzes, Fehler in automatischen Prozessen (z. B. bei der Konfigurationsverteilung) sowie eingeschränkte Erreichbarkeit von Netzkomponenten. 

#### NET.1.2.A8 Zeit-Synchronisation

Alle Komponenten des Netzmanagements, inklusive der eingebundenen Netzkomponenten, MÜSSEN eine synchrone Uhrzeit nutzen. Die Uhrzeit MUSS an jedem Standort innerhalb des lokalen Netzes mittels NTP-Service synchronisiert werden. Ist ein separates Management-Netz eingerichtet, MUSS eine NTP-Instanz in diesem Management-Netz positioniert werden.

#### NET.1.2.A9 Absicherung der Netzmanagement-Kommunikation

Erfolgt die Netzmanagement-Kommunikation über die produktive Infrastruktur, MÜSSEN hierfür nach dem Stand der Technik sichere Protokolle verwendet werden. Ist dies nicht möglich MUSS ein eigens dafür vorgesehenes Administrationsnetz (Out-of-Band-Management) verwendet werden (siehe NET.1.1 *Netzarchitektur und -design*)

#### NET.1.2.A10 Beschränkung der SNMP-Kommunikation

Im Netzmanagement DÜRFEN keine unsicheren Versionen des Simple Network Management Protocol (SNMP) eingesetzt werden. Ist dies jedoch nicht möglich, MUSS die SNMP-Kommunikation entweder über ein separates Management-Netz erfolgen oder es MUSS SNMPv3 mit Authentisierung und Verschlüsselung benutzt werden. Grundsätzlich SOLLTE über SNMP nur mit den minimal erforderlichen Zugriffsrechten zugegriffen werden. Die Zugangsberechtigung SOLLTEN auf dedizierte Management-Server eingeschränkt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Netzmanagement. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.1.2.A11 Festlegung einer Sicherheitsrichtlinie für das Netzmanagement [Informationssicherheitsbeauftragter (ISB)]

Für das Netzmanagement SOLLTE eine Sicherheitsrichtlinie erstellt und nachhaltig gepflegt werden. Die Richtlinie SOLLTE allen Personen, die am Netzmanagement beteiligt sind, bekannt und grundlegend für deren Arbeit sein. Es SOLLTE regelmäßig und nachvollziehbar überprüft werden, dass die in der Richtlinie geforderten Inhalte umgesetzt werden. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.

Die Sicherheitsrichtlinie SOLLTE festlegen, welche Bereiche des Netzmanagements über zentrale Management-Werkzeuge und -Dienste realisiert werden. Auch SOLLTE sie definieren, inwieweit Aufgaben im Netzmanagement der Institution automatisiert realisiert werden sollen. 

Darüber hinaus SOLLTEN Rahmenbedingungen und Vorgaben für die Netztrennung, Zugriffskontrolle, Protokollierung sowie den Schutz der Kommunikation, das eingesetzte Netzmanagement-Werkzeug und die operativen Grundregeln für das Netzmanagement spezifiziert werden.

#### NET.1.2.A12 Ist-Aufnahme und Dokumentation des Netzmanagements

Es SOLTE eine Dokumentation erstellt werden, die beschreibt, wie die Management-Infrastruktur des Netzes aufgebaut ist. Darin SOLLTEN die initiale Ist-Aufnahme sowie alle durchgeführten Änderungen im Netzmanagement enthalten sein. Insbesondere SOLLTE dokumentiert werden, welche Netzkomponenten mit welchen Management-Werkzeugen verwaltet werden. Außerdem SOLLTEN alle für das Netzmanagement benutzten IT-Arbeitsplätze und -Endgeräte sowie alle Informationsbestände, Management-Daten und Informationen über den Betrieb des Netzmanagements erfasst werden. Letztlich SOLLTEN sämtliche Schnittstellen zu Anwendungen und Diensten außerhalb des Netzmanagements dokumentiert werden. 

Der so dokumentierte Ist-Zustand der Management-Infrastruktur SOLLTE mit der Dokumentation der Netz-Infrastruktur abgeglichen werden (siehe Baustein NET.1.1 *Netz-Architektur- und Design).*

Die Dokumentation SOLLTE vollständig und immer aktuell sein.

#### NET.1.2.A13 Erstellung eines Netzmanagement-Konzepts [Leiter IT]

Ausgehend von der Sicherheitsrichtlinie (siehe NET.1.2.A11 *Festlegung einer Sicherheitsrichtlinie für das Netzmanagement*) SOLLTE ein Netzmanagement-Konzept erstellt und nachhaltig gepflegt werden. Dabei SOLLTEN mindestens folgende Aspekte bedarfsgerecht berücksichtigt werden:

* Methoden, Techniken und Werkzeuge für das Netzmanagement,
* Absicherung des Zugangs und der Kommunikation, 
* Netztrennung, insbesondere Zuordnung von Netzmanagement-Komponenten zu Sicherheitszonen,
* Umfang des Monitorings und der Alarmierung je Netzkomponente,
* Protokollierung,
* Automatisierung, insbesondere zentrale Verteilung von Konfigurationsdateien auf Switches,
* Meldeketten bei Störungen und Sicherheitsvorfällen,
* Bereitstellung von Netzmanagement-Informationen für andere Betriebsbereiche und
* Einbindung des Netzmanagements in die Notfallplanung.
#### NET.1.2.A14 Fein- und Umsetzungsplanung

Es SOLLTE eine Fein- und Umsetzungsplanung für die Netzmanagement-Infrastruktur erstellt werden. Hierbei SOLLTEN alle in der Sicherheitsrichtlinie und im Netzmanagement-Konzept adressierten Punkte berücksichtigt werden.

#### NET.1.2.A15 Konzept für den sicheren Betrieb der Netzmanagement-Infrastruktur

Ausgehend von den Sicherheitsrichtlinien und dem Netzmanagement-Konzept SOLLTE ein Konzept für den sicheren Betrieb der Netzmanagement-Infrastruktur erstellt werden. Darin SOLLTE der Anwendungs- und Systembetrieb für die Netzmanagement-Werkzeuge berücksichtigt werden. Auch SOLLTE geprüft werden, wie sich die Leistungen anderer operativer Einheiten einbinden und steuern lassen. 

#### NET.1.2.A16 Einrichtung und Konfiguration von Netzmanagement-Lösungen

Lösungen für das Netzmanagement SOLLTEN anhand der Sicherheitsrichtlinie (siehe NET.1.2.A11 *Festlegung einer Sicherheitsrichtlinie für das Netzmanagement*), der spezifizierten Anforderungen (siehe NET1.2.A2 *Anforderungsspezifikation für das Netzmanagement*) und der Fein- und Umsetzungsplanung aufgebaut, sicher konfiguriert und in Betrieb genommen werden. Danach SOLLTEN die spezifischen Prozesse für das Netzmanagement eingerichtet werden.

#### NET.1.2.A17 Regelmäßiger Soll-Ist-Vergleich

Es SOLLTE regelmäßig und nachvollziehbar geprüft werden, inwieweit die Netzmanagement-Lösung dem Sollzustand entspricht. Dabei SOLLTE geprüft werden, ob die bestehende Lösung noch die Sicherheitsrichtlinie und Anforderungsspezifikation erfüllt. Auch SOLLTE geprüft werden, inwieweit die umgesetzte Management-Struktur und die genutzten Prozesse dem aktuellen Stand entsprechen. Weiter SOLLTE verglichen werden, ob die Management-Infrastruktur auf dem aktuellen Stand der Technik ist.

#### NET.1.2.A18 Schulungen für Management-Lösungen [Leiter IT, Vorgesetzte]

Für die eingesetzten Netzmanagement-Lösungen SOLLTEN Schulungs- und Trainingsmaßnahmen konzipiert und durchgeführt werden. Die Maßnahmen SOLLTEN die individuellen Gegebenheiten im Configuration-, Availability- und Capacity-Management sowie typische Situationen im Fehlermanagement abdecken. Die Schulungen und Trainings SOLLTEN regelmäßig wiederholt werden, mindestens jedoch, wenn sich größere technische oder organisatorische Änderungen innerhalb der Netzmanagement-Lösung ergeben.

#### NET.1.2.A19 Starke Authentisierung des Management-Zugriffs

Für den administrativen Zugriff auf Netzkomponenten SOLLTE eine dem Stand der Technik entsprechende Authentisierungsmethode verwendet werden. Die administrativen Zugänge SOLLTEN über einen zentralen Authentisierungsserver mittels personalisierter Konten über entsprechend sichere Protokolle authentisiert werden.

#### NET.1.2.A20 Absicherung des Zugangs zu Netzmanagement-Lösungen

Der Zugriff auf zentrale Netzmanagement-Lösungen und Management-Informationen SOLLTE durch eine dem Stand der Technik entsprechende Authentisierungsmethode geschützt werden. Die Zugänge SOLLTEN über einen zentralen Authentisierungsserver mittels personalisierter Konten authentisiert werden.

Es MÜSSEN dem Stand der Technik entsprechende Authentisierungs- und Verschlüsselungsmethoden realisiert werden, falls auf Netzmanagement-Werkzeuge von einem Netz außerhalb der Management-Netze, insbesondere aus einem produktiven Netz oder einem unzureichend sicheren Netz, zugegriffen wird.

#### NET.1.2.A21 Entkopplung der Netzmanagement-Kommunikation

Direkte Management-Zugriffe eines Administrators von einem IT-System außerhalb der Management-Netze auf eine Netzkomponente SOLLTEN vermieden werden. Ist ein solcher Zugriff ohne zentrales Management-Werkzeug notwendig, SOLLTE die Kommunikation entkoppelt werden. Solche Sprungserver SOLLTEN im Management-Netz integriert und in einem getrennten Zugangssegment positioniert sein.

#### NET.1.2.A22 Beschränkung der Management-Funktionen

Es SOLLTEN nur die benötigten Management-Funktionen aktiviert werden.

#### NET.1.2.A23 Protokollierung der administrativen Zugriffe

Im Rahmen des Netzmanagements SOLLTEN die Sitzungsdaten aller administrativen Zugriffe protokolliert und gespeichert werden. Hierbei SOLLTEN die datenschutzrechtlichen Bestimmungen eingehalten werden.

Die Protokollierungsdaten SOLLTEN in der Datensicherung ausreichend und gesetzeskonform geschützt werden. Darüber hinaus SOLLTE festgelegt werden, ob und in welchem Umfang Sitzungsdaten für forensische Analysen zu archivieren sind. Wenn Daten archiviert werden, SOLLTE darauf geachtet werden, dass dies gesetzeskonform und revisionssicher durchgeführt wird.

#### NET.1.2.A24 Zentrale Konfigurationsverwaltung für Netzkomponenten

Software bzw. Firmware und Konfigurationsdaten für Netzkomponenten SOLLTEN automatisch über das Netz verteilt und ohne Betriebsunterbrechung installiert und aktiviert werden können. Die hierfür benötigten Informationen SOLLTEN an zentraler Stelle sicher verfügbar sein sowie in die Versionsverwaltung und die Datensicherung eingebunden werden. Die zentrale Konfigurationsverwaltung SOLLTE nachhaltig gepflegt und regelmäßig auditiert werden. 

#### NET.1.2.A25 Statusüberwachung der Netzkomponenten

Die grundlegenden Performance- und Verfügbarkeits-Parameter der zentralen Netzkomponenten SOLLTEN kontinuierlich überwacht werden. Hierfür SOLLTEN vorab die jeweiligen Schwellwerte ermittelt werden (Baselining).

#### NET.1.2.A26 Umfassende Protokollierung, Alarmierung und Logging von Ereignissen

Wichtige Ereignisse oder Fehlerzustände SOLLTEN automatisch an ein zentrales Management-System übermittelt und dort protokolliert werden. Dies gilt sowohl für Ereignisse auf Netzkomponenten als auch für Ereignisse auf den Netzmanagement-Werkzeugen. Das zuständige IT-Personal SOLLTE zusätzlich automatisch benachrichtigt werden. Das Alarming und Logging SOLLTE mindestens folgende Punkte beinhalten:

* Ausfall bzw. Nichterreichbarkeit von Netz- oder Managementkomponenten
* Hardware-Fehlfunktionen
* fehlerhafte Anmeldeversuche
* kritische Zustände oder Überlastung von IT-Systemen
Ereignis-Meldungen bzw. Logging-Daten SOLLTEN kontinuierlich oder kumuliert einem zentralen Management-System übermittelt werden. Alarm-Meldungen SOLLTEN direkt bei Auftreten übermittelt werden.

#### NET.1.2.A27 Einbindung des Netzmanagements in die Notfallplanung

Die Netzmanagement-Lösungen SOLLTEN in die Notfallplanung der Institution eingebunden werden. Dazu SOLLTEN die Netzmanagement-Werkzeuge und die Konfigurationen der Netzkomponenten gesichert und in die Wiederanlaufpläne integriert sein.

#### NET.1.2.A28 Platzierung der Management-Clients für das In-Band-Management

Für die Administration sowohl der internen als auch externen IT-Systeme SOLLTEN dedizierte Management-Clients eingesetzt werden. Dafür SOLLTE mindestens ein Management-Client am äußeren Netzbereich (für die Administration am Internet anliegender IT-Systeme) und ein weiterer im internen Bereich (für die Administration interner IT-Systeme) platziert werden. 

#### NET.1.2.A29 Einsatz von VLANs in der Management-Zone

Werden Management Netze durch VLANs getrennt, SOLLTE darauf geachtet werden, dass der äußere Paketfilter sowie die daran angeschlossenen Geräte in einem eigenen Teilnetz stehen. Zudem SOLLTE sichergestellt werden, dass das ALG dabei nicht umgangen wird.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.1.2.A30 Hochverfügbare Realisierung der Management-Lösung(A)

Zentrale Management-Lösungen SOLLTEN hochverfügbar betrieben werden. Hierzu SOLLTEN die Server bzw. Werkzeuge inklusive der Netzanbindungen redundant ausgelegt sein. Auch die einzelnen Komponenten SOLLTEN hochverfügbar bereitgestellt werden.

#### NET.1.2.A31 Grundsätzliche Nutzung von sicheren Protokollen(CIA)

Für das Netzmanagement SOLLTEN ausschließlich sichere Protokolle benutzt werden. Es SOLLTEN alle Sicherheitsfunktionen dieser Protokolle verwendet werden.

#### NET.1.2.A32 Physische Trennung des Management-Netzes(CIA)

Das Management-Netz SOLLTE physisch getrennt werden.

#### NET.1.2.A33 Physische Trennung von Management-Segmenten [Leiter Netze](CIA)

Das Management-Netz SOLLTE in physisch getrennte Sicherheitszonen unterteilt werden. Dabei SOLLTEN physisch getrennte Sicherheitszonen mindestens für das Management von LAN-Komponenten, Sicherheitskomponenten und Komponenten zur Außenanbindung eingerichtet werden.

#### NET.1.2.A34 Protokollierung von Inhalten administrativer Sitzungen(CI)

Ergänzend zur Protokollierung von Sitzungsdaten (siehe NET.1.2.A22 *Protokollierung der administrativen Zugriffe*) SOLLTEN auch die Inhalte von administrativen Zugriffen protokolliert werden. Alternativ nach dem Vier-Augen-Prinzip vorgegangen werden. Auch die protokollierten Inhalte der administrativen Sitzungen SOLLTEN in der Datensicherung ausreichend und gesetzeskonform geschützt werden.

#### NET.1.2.A35 Festlegungen zur Beweissicherung(CIA)

Es SOLLTEN Vorgehensweisen zur Beweissicherung und zu forensischen Untersuchungen im Rahmen des Netzmanagements festgelegt und dokumentiert werden. Die erhobenen Protokollierungsdaten SOLLTEN für forensische Analysen gesetzeskonform und revisionssicher archiviert werden.

#### NET.1.2.A36 Einbindung der Protokollierung des Netzmanagements in eine SIEM-Lösung(CIA)

Die Protokollierung des Netzmanagements SOLLTE in eine Security-Information-and-Event-Management-(SIEM)-Lösung eingebunden werden. Hierzu SOLLTEN die Anforderungskataloge (siehe NET.1.2.A2) zur Auswahl von Netzmanagement-Lösungen hinsichtlich der erforderlichen Unterstützung von Schnittstellen und Übergabeformaten angepasst werden.

#### NET.1.2.A37 Standort-übergreifende Zeitsynchronisation(CI)

Die Zeitsynchronisation SOLLTE über alle Standorte der Institution sichergestellt werden. Hierfür SOLLTE eine gemeinsame Referenzzeit benutzt werden, z. B. über einen übergeordneten NTP-Server. 

#### NET.1.2.A38 Festlegung von Notbetriebsformen für die Netzmanagement-Infrastruktur(A)

Für eine schnelle Wiederherstellung der Sollzustände von Software bzw. Firmware sowie der Konfiguration der Komponenten in der Netzmanagement-Infrastruktur SOLLTEN hinreichend gute Ersatzlösungen festgelegt werden, mit denen die administrativen Tätigkeiten im Notfall durchgeführt werden können.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Netzmanagement" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISI] BSI-Standards zur Internet Sicherheit (Isi-Reihe)

  

 BSI, (zuletzt abgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Reihe\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Reihe_node.html)

 
* #### [TR21022] BSI Technische Richtlinie, Kryptografische Verfahren

  

 Verwendung von Transport Layer Security (TLS), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2017  
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Netzmanagement" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

