1 Beschreibung
--------------

### 1.1 Einleitung

Mit Fernwartung wird ein räumlich getrennter Zugriff auf IT-Systeme und die darauf laufenden Anwendungen zu Konfigurations-, Wartungs-, Reparatur- oder Kontrollzwecken bezeichnet. Die Fernwartung kann passiv durch einen ausschließlich betrachtenden Zugang auf das IT-System bzw. die Anwendungen erfolgen oder aktiv durch direkte administrative Eingriffe in das Betriebssystem oder laufende Anwendungen. Im Fall der passiven Fernwartung muss ein Benutzer vor Ort unter Anleitung durch einen Administrator die eigentlichen Aktionen durchführen. Bei der aktiven Fernwartung dagegen wird in ein Betriebssystem eingegriffen und dieses direkt durch einen Administrator bedient. Dabei werden unter anderem die Signale einer Maus und Tastaturbefehle, sowie Bildschirminhalte und Konsolenausgaben übertragen. Selbst wenn wirkungsvolle Mechanismen zur Absicherung des Fernwartungs-Zugangs implementiert werden, bestehen direkte Zugriffsmöglichkeiten von außerhalb auf das interne Netz und darin verarbeiteten Daten. Durch diese Schnittstellen können Externe die Institution gefährden und somit wirtschaftliche und betriebstechnische Schäden anrichten. 

### 1.2 Zielsetzung

Ziel des Bausteins ist der Schutz der Informationen, die auf Basis der Fernwartung gespeichert, verarbeitet und übertragen werden. Zu diesem Zweck werden Anforderungen an die Fernwartung gestellt, die sich auf Funktionen der aktiven und passiven Fernwartung beziehen.

### 1.3 Abgrenzung

Dieser Baustein betrachtet Fernwartung aus der Sicht des IT-Betriebs und gibt Hinweise für Anwender, wie Fernwartung eingesetzt werden kann. Wichtig ist die ganzheitliche Gewährleistung der Informationssicherheit in allen Lebenszyklusphasen. Die Sicherheitsaspekte der eingesetzten Kommunikationsverbindungen, Authentisierungsmechanismen sowie die Absicherung der Fernwartungs-Zugänge sind dabei wichtige Bestandteile des Bausteins. Im Kontext des Bausteins Fernwratung werden nicht alle relevanten Aspekte der damit in Verbindung stehenden Geschäftsprozesse abgedeckt. Daher müssen vor allem Aspekte der Bausteine *OPS.1.1.3 Patch- und Änderungsmanagement*, *ORP.3 Sensibilisierung und Schulung, CON.1 Kryptokonzept *und CON.3* Datensicherungskonzept* gesondert gewährleistet werden. Ebenso sind die Vorgaben der Bausteinschichten NET (Netze und Kommunikation), DER (Detektion & Reaktion),die Bausteine der Schicht *OPS.2 IT-Betrieb von Dritten* und die Bausteine der Schicht *OPS.3 IT-Betrieb für Dritte *umgesetzt werden, die direkt mit der Fernadministration in Verbindung stehen. Bei cloudbasierten Produkten muss der Baustein *OPS.2.2 Cloud-Nutzung* beachtet werden. Ebenso sind die Remote Procedure Calls von Windows 2010 nicht Bestandteil dieses Bauteins.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Fernwartung von besonderer Bedeutung:

### 2 1 Unzureichende Kenntnisse über Regelungen der Fernwartung

Sollten die Beteiligten wichtige Regelungen nur unzureichend kennen und darum nicht anwenden, ist der Schutz der Informationen im Rahmen einer Ferwartung gefährdet. Daher bestehen Gefahren für den IT-Betrieb, wenn geltende Regelungen nicht allgemein bekannt gemacht werden. Insbesondere Administratoren, die Fernwartung einrichten und nutzen, sind auf Regelungen, z. B. zu Konfiguationen, angewiesen , da sonst mit der Fernwartung zusätzliche Betriebsrisiken, aber auch Sicherheitslücken zum internen Netz entstehen und Angriffe über die Fernwartung nicht erkannt oder abgewehrt werden können.

### 2 2 Fehlende oder unzureichende Planung und Regelung der Fernwartung

Wird die Fernwartung nicht sorgfältig geplant, aufgebaut und geregelt, kann nicht nur die Sicherheit eines IT-Systems, sondern aller IT-Systeme einer Institution beeinträchtigt werden, wenn Sicherheitslücken ausgenutzt werden. Sicherheitslücken können an vielen Stellen entstehen und Kommunikationsprotokolle, Patch-Prozesse, Verschlüsselungsalgorithmen und Authentisierungsmechanismen betreffen. Über unzureichend gesicherte Fernwartungsschnittstellen kann auch ein gekoppeltes Netz eines Dritten kompromittiert werden.

### 2 3 Unerlaubtes Ausüben von Rechten bei der Fernwartung

Auf die jeweiligen Aufgaben zugeschnittene Zutritts-, Zugangs- und Zugriffsberechtigungen werden eingesetzt, um Informationen, Geschäftsprozesse und IT-Systeme vor unbefugtem Zugriff zu schützen. Werden solche Berechtigungen bei der Fernwartung an unberechtigte Personen vergeben oder werden Rechte unautorisiert aus der Ferne ausgeübt, können sich eine Vielzahl von Gefahren für die Vertraulichkeit und Integrität von Daten und die Verfügbarkeit z. B. von Rechenleistungen ergeben. Mögliche Schadensszenarien sind beispielsweise das Einschleusen von Schadsoftware, die Manipulation von Daten und Informationen und die unbefugte Informationsgewinnung. Auswirkungen können z. B. finanzielle und Wissensverluste, physische Zerstörungen von Sachgütern und Kompromittierungen von IT-Systemen und Netzen sein.

### 2 4 Ungeeignete Nutzung von Authentisierung bei der Fernwartung

Bei der Fernwartung werden Authentisierungsmechanismen verwendet, die auf einer Benutzerverwaltung mit gespeicherten Authentisierungsdaten beruhen. Erlangen unberechtigte Dritte administrative Berechtigungen auf Fernwartungsrechner bzw. für Fernwartungswerkzeuge, können weitreichende Schäden für die Institution entstehen. Dazu zählen z. B. unbefugte Konfigurationen an IT-Systemen und Anwendungen, Kompromittierungen sowie Informations- und Datenverluste.

### 2 5 Unsicherer und unkontrollierter Aufbau von Kommunikationsverbindungen

Für eine Fernwartung ist grundsätzlich ein Zugriff auf Kommunikationsschnittstellen des administrierten Rechners erforderlich. Dies beinhaltet immer auch ein Gefährdungspotential.

Ebenso ist bei Kommunikationsschnittstellen von IT-Systemen für den Benutzer nicht immer offensichtlich, was neben Benutzer- und Protokollinformationen zusätzlich übertragen wird. Eine manipulierte oder auch nur aktivierte Kommunikationsschnittstelle kann unter Umständen ohne Initiierung durch einen Benutzer eine Verbindung zu einer Gegenstelle aufbauen oder über eine dem Benutzer nicht bekannte Funktion durch Dritte angesprochen werden.

### 2 6 Fehlerhafte Fernwartung

Für die Gewährleistung der Sicherheit und Funktionsfähigkeit von IT-Systemen und Anwendungen, auf die nur aus der Ferne zugegriffen werden kann, ist eine professionelle und kontinuierliche Fernwartung erforderlich. Werden diese IT-Systeme und Anwendungen nicht ordnungsgemäß per Fernwartung konfiguriert, gewartet, repariert und kontrolliert, können sie im schlimmsten Fall nicht mehr genutzt werden. Sollten innerhalb der Fernwartungsprozesse Fehler entstehen, können daraus direkt Fehlfunktionen einzelner Betriebssystemfunktionen resultieren. Außerdem können durch verspätete oder fehlerhafte IT-Systemwartungen Sicherheitslücken entstehen. 

### 2 7 Verwendung unsicherer Protokolle in der Fernwartung

Die Kommunikation über öffentliche und interne Netze mittels unsicherer Protokolle stellt eine potenzielle Gefahr dar. Werden z. B. veraltete Versionen von IPSec, SSH oder SSL/TLS eingesetzt, um einen Tunnel zwischen zwei Endpunkten bzw. Netzen herzustellen, kann die Sicherheit dieser Tunnel nicht ausreichend gewährleistet werden. Angreifer können Schwachstellen dieser Protokolle ausnutzen, um in geschützte Verbindungen eigene Inhalte einzuschleusen. Generell als unsicher gelten Protokolle, bei denen Informationen im Klartext übertragen werden.

### 2 8 Ungeeigneter Umgang mit Authentisierungsverfahren bei der Fernwartung

Die Sicherheit eines Authentisierungsverfahrens ist direkt abhängig vom sorgfältigen Umgang damit . Die Weitergabe von benutzergebundenen Authentisierungsdaten und die unsichere Aufbewahrung dieser Angaben stellen eine mögliche Gefahr dar. Es können Sicherheitslücken für den unbefugten Zugriff auf die Rechte- und Rollenprofile der Administratoren sowie auf IT-Systeme und Anwendungen entstehen.

### 2 9 Unsichere kryptographische Algorithmen bei der Fernwartung

Es kommt zu einem Sicherheitsverlust innerhalb der Fernwartung, wenn unsichere kryptographische Verfahren eingesetzt oder geheime Schlüssel nicht ausreichend geschützt werden. Nachlässigkeiten im Bereich der kryptographischen Algorithmen können zu Kompromittierungen kryptographischer Schlüssel führen. Zusätzlich können Angreifer leichter eindringen, wenn sie mit vertretbaren zeitlichen und technischen Ressourcen das eingesetzte kryptographische Verfahren analysieren oder brechen und anschließend dadurch in die Kommunikation eindringen können.

### 2 10 Unsichere und unkontrollierte Fremdnutzung der Fernwartungs-Zugänge

Wird Unbefugten bzw. Dritten ermöglicht, die Komponenten der Fernwartung ohne vertragliche Grundlage zu nutzen, indem z. B. Berechtigungskonzepte der Institution umgangen oder nicht sorgfältig umgesetzt werden, ist die Sicherheit der Fernwartung, der IT-Systeme und der Anwendungen nicht mehr gewährleistet.

### 2 11 Nutzung von Online-Diensten für die Fernwartung

Neben einer Fernwartung, bei der ein Administrator direkt eine Datenverbindung zu der zu administrierenden Institution aufbaut, können auch sogenannte Online-Dienste genutzt werden. Hierbei verbinden sich die zu administrierenden IT-Systeme mit den Servern eines Drittanbieters und die Administratoren können über einen Webbrowser oder Ähnlichem auf die zu administrierenden IT-Systeme zugreifen.

Da die Kommunikation nicht Ende-zu-Ende verschlüsselt wird und der Zugriff über einen Dritten stattfindet, könnte der Datenaustausch direkt mitgelesen werden. Zusätzlich könnten auch die IT-Systeme durch unberechtigte Personen administriert werden, indem die Datenverbindung verändert wird. Bauen die IT-Systeme automatisch beim Systemstart eine Datenverbindung zum Online-Dienst auf und sind die Zugangsdaten bekannt, könnte direkt auf das IT-System zugegriffen werden.

Um eine Verbindung zum Online-Dienst aufzubauen, werden oft keine administrativen Rechte auf den zu administrierenden IT-Systemen benötigt, der Administrator benötigt dann nur einen Browser. Benutzer ohne administrative Rechte können so unautorisiert einen Fernzugriff initiieren.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Fernwartung aufgeführt. Grundsätzlich ist der Leiter IT für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.2.4.A1 Planung des Einsatzes der Fernwartung [IT-Betrieb]

Der Einsatz der Fernwartung MUSS an die Institution angepasst und bedarfsgerecht hinsichtlich technischer und organisatorischer Aspekte geplant werden. Es MUSS geklärt werden, ob In-Band und/oder Out-Band Administration genutzt wird, welche IT-Systemschnittstellen und Protokolle verwendet werden. Es MUSS geklärt werden, wie die Fernwartung abgesichert wird und wie dies auditiert wird.

#### OPS.2.4.A2 Sicherer Verbindungsaufbau bei der Fernwartung [Benutzer]

Die Initiierung des Fernwartungs-Zugriffs MUSS aus der Institution heraus erfolgen. Der Benutzer des fernadministrierten IT-Systems MUSS dem Fernzugriff explizit zustimmen.

#### OPS.2.4.A3 Absicherung der Kommunikationsverbindungen bei der Fernwartung [IT-Betrieb]

Die möglichen Zugänge und Kommunikationsschnittstellen für einen Verbindungsaufbau von außen MÜSSEN auf das notwendige Maß beschränkt werden. Ebenso MÜSSEN alle Kommunikationsverbindungen nach vollzogenem Fernzugriff getrennt werden (Deaktivierung). Für eine Fernwartung MÜSSEN notwendige Ports ständig bereitgestellt werden. Es MÜSSEN unter Berücksichtigung des erforderlichen Schutzbedarfes des IT-Systems oder der Anwendung sichere Authentisierungsmechanismen für die Administratoren eingesetzt werden.

#### OPS.2.4.A4 Regelungen zu Kommunikationsverbindungen [IT-Betrieb]

Unter Beachtung der Firewall-Anforderungen der Institution MUSS die Fernwartung in das Firewall-Regelwerk eingebunden werden. Hierbei MUSS darauf geachtet werden, dass bestehende Firewall-Infrastrukturen und deren Regelungen nicht umgangen werden. 

Bei der Überprüfung der Netz-Konnektivität mittels ICMP MÜSSEN die Regelungen für die lokalen und entfernten Prüfungen beachtet werden.

#### OPS.2.4.A5 Einsatz von Online-Diensten [IT-Betrieb, Benutzer]

Es MUSS entschieden werden, ob eine Fernwartung über Online-Dienste erlaubt ist. Der Einsatz von Online-Diensten für die Fernwartung SOLLTE verboten werden. Es SOLLTEN technische und organisatorische Maßnahmen ergriffen werden, um das Verbot durchzusetzen.

Sofern der Einsatz nicht zu vermeiden ist, SOLLTE er auf möglichst wenige Fälle beschränkt werden. Die Bedingungen, unter denen eine Fernwartung über Online-Dienste erlaubt ist, SOLLTEN festgelegt werden. Die Clients SOLLTEN automatisiert keine Verbindungen zum zum Online-Dienst aufbauen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Fernwartung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.2.4.A6 Erstellung einer Richtlinie für die Fernwartung [IT-Betrieb]

Die Regelungen zur Fernwartung SOLLTEN in einer Richtlinie dokumentiert werden. Sollte eine eigenständige Richtlinie erstellt werden, SOLLTE in den bestehenden Richtlinien der Institution auf die Richtlinie für Fernwartung referenziert werden. Die Richtlinie SOLLTE allen Verantwortlichen, die an der Konzeption, dem Aufbau und dem Betrieb sowie der Aussonderung beteiligt sind, bekannt sein und die Grundlage für deren Arbeit bilden können.

#### OPS.2.4.A7 Dokumentation bei der Fernwartung [IT-Betrieb]

Es MUSS eine aktuelle Dokumentation der Fernwartung vorliegen. Vorhandene Stellvertreter SOLLTEN zu jeder Zeit die Aufgaben und Prozesse übernehmen können. Da die Dokumente meist vertrauliche Informationen und Daten beinhalten, SOLLTEN sie an geeigneten Orten gesichert abgelegt werden und auch im Rahmen des Notfallmanagements zur Verfügung stehen . Ebenso SOLLTE der Schutz vor unbefugtem Zugriff auf die Dokumentation sichergestellt sein. Sämtliche Fernzugriffsmöglichkeiten SOLLTEN erfasst und dokumentiert sein.

#### OPS.2.4.A8 Sichere Protokolle bei der Fernwartung [IT-Betrieb]

Es SOLLTEN aktuelle und als sicher eingestufte Kommunikationsprotokolle eingesetzt werden. Die Kommunikation SOLLTE verschlüsselt erfolgen. Dafür SOLLTEN ausgehend vom Schutzbedarf der Institution geeignete kryptographische Verfahren zur Realisierung eines Tunnels eingesetzt werden. Damit die eingesetzten Protokolle geeignet verwaltet werden können und die Sicherheitsanforderungen berücksichtigt werden, SOLLTEN Informationen zu Schwachstellen aus der Fachpresse bzw. aus einschlägigen Quellen beachtet und kontinuierlich aktualisiert werden.

#### OPS.2.4.A9 Auswahl geeigneter Fernwartungswerkzeuge [IT-Betrieb]

Die Auswahl geeigneter Fernwartungswerkzeuge SOLLTE sich aus den betrieblichen, sicherheitstechnischen und datenschutzrechtlichen Anforderungen der Institution ergeben. Alle Beschaffungsentscheidungen SOLLTEN mit den Verantwortlichen des Einkaufes, dem System- und Anwendungsverantwortlichen sowie dem Sicherheitsmanagement abgestimmt werden.

#### OPS.2.4.A10 Verwaltung der Fernwartungswerkzeuge [IT-Betrieb, Benutzer]

Es SOLLTEN organisatorische Verwaltungsprozesse zum Umgang mit den ausgewählten Werkzeugen etabliert werden. Es SOLLTE eine Bedienungsanleitung für den Umgang mit dem Fernwartungswerkzeug vorliegen. Musterabläufe für die passive und die aktive Fernwartung SOLLTEN erstellt und kommuniziert werden. Der IT-Betrieb SOLLTE im Umgang mit den Fernwartungswerkzeugen sensibilisiert und geschult werden. Es SOLLTE ein Ansprechpartner für alle fachlichen Fragen zu den Fernwartungswerkzeugen benannt werden.

#### OPS.2.4.A11 Einsatz von kryptographischen Verfahren bei der Fernwartung [IT-Betrieb]

Bei der Fernwartung SOLLTEN ausreichend starke kryptographische Verfahren genutzt werden, um die Kommunikation abzusichern und die Administrierenden zu authentisieren. Die Stärke der verwendeten kryptographischen Verfahren und Schlüssel SOLLTE im Rahmen der Fernwartung regelmäßig überprüft und falls erforderlich angepasst werden. 

#### OPS.2.4.A12 Patch- und Änderungsmanagement bei der Fernwartung [IT-Betrieb]

Es SOLLTEN die allgemeinen Vorgaben zum Patch- und Änderungsmanagement der Institution für die Fernwartung umgesetzt werden. Die IT-Systeme und Administrationswerkzeuge SOLLTEN alle im Patch- und Änderungsmanagement berücksichtigt werden. 

Die Fernwartungszugänge SOLLTEN geeignet aktiviert und deaktiviert werden. Alle Aktivierungen und Deaktivierungen der Fernwartungs-Zugänge SOLLTEN zusätzlich dokumentiert sein. Aus Sicherheitsgründen SOLLTEN alle durch die Fernwartung betreuten IT-Systeme und Anwendungen zeitnah gepatcht werden. Bevor Patches und Änderungen durch die Fernwartung in ein Produktivsystem eingespielt werden, SOLLTEN sie vorab in einer geeigneten eingerichteten Testumgebung geprüft werden.

#### OPS.2.4.A13 Datensicherung bei der Fernwartung [IT-Betrieb]

Zur Vermeidung von Datenverlusten innerhalb der Infrastruktur für die Fernwartung SOLLTEN regelmäßige Datensicherungen erfolgen. Es SOLLTEN Vorgaben der Datensicherung bei der Fernwartung anhand der Menge und Wichtigkeit der laufend neu gespeicherten Daten und des möglichen Schadens für die Institution bei Verlust dieser Daten getroffen werden. 

Alle Datensicherungsanforderungen der Fernwartung SOLLTEN mit den allgemeinen Vorgaben der Institution zur Datensicherung korrespondieren.

#### OPS.2.4.A14 Dedizierte Systeme bei der Fernwartung [IT-Betrieb]

Innerhalb der Fernwartung SOLLTEN Komponenten eingesetzt werden, die ausschließlich diesem Anwendungszweck dienen. Alle weiteren Funktionen/Dienste SOLLTEN deaktiviert werden. Die Komponenten der Fernwartung SOLLTEN sicher konfiguriert und eingestellt werden. 

#### OPS.2.4.A15 Absicherung der Fernwartung [IT-Betrieb]

Fernwartung SOLLTE nur aus dem internen Netz erfolgen. 

Falls es dennoch nötig ist, von einem öffentlichen Datennetz auf interne IT-Systeme zuzugreifen, SOLLTE ein abgesichertes Virtuelles Privates Netz (VPN) genutzt werden. Für die Fernwartung per VPN SOLLTE eine geschützte Datenverbindung zu dem VPN-Endpunkt generiert werden. Neben diesen externen Fernwartungs-Zugängen SOLLTEN auch die internen Fernwartungs-Zugänge abgesichert werden. Die Benutzung von internen Fernwartungs-Zugängen SOLLTE so weit wie möglich eingeschränkt werden. Des Weiteren SOLLTEN alle Aktivitäten während einer Administrationssitzung protokolliert werden. 

#### OPS.2.4.A16 Schulungen zur Fernwartung [IT-Betrieb]

Den Administratoren SOLLTEN ausreichende Kenntnisse im Umgang mit den Fernwartungskomponenten vermittelt werden. Diese Schulungsmaßnahmen SOLLTEN in die bereits etablierten Verfahren der Institution integriert werden.

Ebenso SOLLTEN die Mitarbeiter darauf hingewiesen werden, was sie bei der Fernwartung zu beachten haben. 

#### OPS.2.4.A17 Authentisierungsmechanismen bei der Fernwartung [IT-Betrieb]

Für die Fernwartung SOLLTEN Zwei-Faktor-Verfahren zur Authentisierung eingesetzt werden.

Die Auswahl der Authentisierungsmethode und die Gründe, die zu der Auswahl geführt haben, SOLLTEN dokumentiert werden. Zur Erleichterung der Anmeldung bei der Fernwartung SOLLTE diese in einem Identitäts- und Berechtigungsmanagement und deren Infrastrukturen integriert werden.

#### OPS.2.4.A18 Passwortsicherheit bei der Fernwartung [IT-Betrieb]

Falls bei der Fernwartung passwortbasierte Authentisierungen verwendet werden, SOLLTEN Passwortregeln definiert, dokumentiert und den Administratoren bekannt gemacht werden. Für die Fernwartung SOLLTEN diese Passwortregeln technisch forciert werden. 

#### OPS.2.4.A19 Fernwartung durch Dritte [IT-Betrieb]

Wenn es nicht möglich ist, auf externe Fernwartung zu verzichten, SOLLTEN alle Aktivitäten in diesem Rahmen von Internen beobachtet werden. Alle Fernwartungsvorgänge durch Dritte SOLLTEN aufgezeichnet werden. Mit externem Wartungspersonal MÜSSEN vertragliche Regelungen getroffen werden, vor allem über die Sicherheit der betroffenen IT-Systeme und Informationen. Die Pflichten und Kompetenzen des externen Wartungspersonals SOLLTEN vertraglich festgehalten werden.

#### OPS.2.4.A20 Betrieb der Fernwartung [IT-Betrieb]

Es SOLLTE ein Meldeprozess für Support- und Fernwartungsanliegen etabliert werden (z. B. Ticketsystem). Alle Zugriffe durch die Fernwartung SOLLTEN erst nach erfolgreicher Authentisierung gestattet werden. 

Die zur Etablierung der Fernwartungszugänge erforderlichen Freischaltungen an der Sicherheitsinfrastruktur SOLLTEN in die etablierten Prozessefür Firewall-Regeln integriert werden. Es SOLLTEN Mechanismen zur Erkennung und Abwehr von hochvolumigen Angriffen, TCP-State-Exhaustion Angriffen und Angriffen auf Applikationsebene implementiert sein.

Alle Fernwartungsvorgänge SOLLTEN aufgezeichnet werden. Die anfallenden Protokolldaten SOLLTEN regelmäßig ausgewertet werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.2.4.A21 Erstellen eines Notfallplans für den Ausfall der Fernwartung(A)

Im Rahmen der Notfallvorsorge SOLLTE ein Konzept entwickelt werden, wie die Folgen eines Ausfalls von Fernwartungskomponenten minimiert werden können und welche Aktivitäten im Falle eines Ausfalls durchzuführen sind. Durch den Notfallplan SOLLTE sichergestellt sein, dass Störungen, Schäden und Folgeschäden minimiert werden sowie eine zeitnahe Wiederherstellung des Normalbetriebs erfolgt. 

#### OPS.2.4.A22 Redundante Verwendung von mobilen Kommunikationsnetzen(A)

Für den Schutz der Kommunikationsnetze der Fernwartung bei Hochverfügbarkeitsanforderungen SOLLTEN redundante Verbindungs- bzw. Kommunikationsnetze eingerichtet werden. 

#### OPS.2.4.A23 Planung des sicheren Einsatzes in einem abgesicherten Netzsegment [IT-Betrieb]

Für die Fernwartung SOLLTE ein abgesichertes Netzsegment eingesetzt werden. Dieses SOLLTE in der Art wie eine Demilitarized Zone (DMZ) realisiert und betrieben werden. Die Fernwartungszugänge SOLLTEN NICHT dazu führen, dass vorhandene Sicherheitsinfrastrukturen umgangen werden und so ein Zusammenschluss von vertrauenswürdigen und nicht vertrauenswürdigen Netzen erfolgt.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Fernwartung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [CSE108] Fernwartung im industriellen Umfeld

  

 BSI-Veröffentlichung zur Cyber-Sicherheit - Allianz für Cyber-Sicherheit, CSE 108, BSI, Version 1.0, 01.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_108.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_108.pdf)

 
* #### [CSE54] Grundregeln zur Absicherung von Fernwartungszugängen

  

 BSI-Veröffentlichung zur Cyber-Sicherheit- Allianze für Cyber-Sicherheit, BSI, 06.2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_054.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_054.pdf)

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Fernwartung" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

