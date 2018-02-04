1 Beschreibung
--------------

### 1.1 Einleitung

Die Fernwartung beschreibt einen räumlich getrennten Zugriff auf IT-Systeme und die darauf laufenden Anwendungen zu Konfigurations-, Wartungs-, Reparatur- oder Kontrollzwecken. Die Fernwartung kann passiv durch einen ausschließlich betrachtenden Zugang auf das IT-System bzw. die Anwendungen erfolgen oder aktiv durch direkte administrative Eingriffe in das Betriebssystem oder laufende Anwendungen. Im Fall der passiven Fernwartung muss ein Benutzer vor Ort die eigentlichen Aktionen veranlassen. Bei der aktiven Fernwartung dagegen wird in ein Betriebssystem eingegriffen und dieses direkt durch einen Administrator bedient. Dabei werden unter anderem die Signale einer Maus und Tastaturbefehle, sowie Bildschirminhalte und Konsolenausgaben übertragen.

Selbst wenn wirkungsvolle Mechanismen zur Absicherung des Zugangs zur Fernwartung implementiert werden, bestehen direkte Zugriffsmöglichkeiten von außerhalb auf das interne Netz und alle darin verarbeiteten Daten. Durch diese Schnittstellen können Externe die Institution gefährden und somit wirtschaftliche und betriebstechnische Schäden anrichten. Daher ist es notwendig, bei der Fernwartung den gesamten Lebenszyklus der Informationssicherheit abzusichern.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Ist die Entscheidung für eine Fernwartung gefallen, muss der sichere Einsatz geplant und konzipiert werden. Die dabei zu berücksichtigenden Aspekte sind in* OPS.2.4.M1 Planung des Einsatzes der Fernwartung *und *OPS.2.4.M5 Erstellung einer Richtlinie für die Fernwartung* zusammengefasst. Die Sicherheit der Fernwartung kann bereits in der Planungs- und Konzeptionsphase entscheidend beeinflusst werden, indem sicherheitsrelevante Aspekte berücksichtigt werden. 

Wichtig ist außerdem *OPS.2.4.M6 Dokumentation bei der Fernwartung *für die durchgehende Dokumentation von Prozessen der Fernwartung und *OPS.2.4.M22 Planung des sicheren Einsatzes in einem abgesicherten Netzsegment* für die Sicherheit in Internet- und Intranet-Szenarien. 

Unabhängig von den nachfolgenden Maßnahmen sollten die Anforderungen des *Bausteins ORP.4 Identitäts- und Berechtigungsmanagement* beachtet, bewertet und umgesetzt werden.

**Beschaffung**

Im nächsten Schritt muss die Beschaffung geeigneter Werkzeuge für die Fernwartung und eventuell zusätzlich benötigter Hardware erfolgen. Aufbauend auf Einsatzszenarien sind die Anforderungen an zu beschaffende Produkte zu formulieren und basierend darauf die Auswahl der geeigneten Produkte zu treffen. Daher muss an dieser Stelle *OPS.2.4.M8 Auswahl geeigneter Fernwartungswerkzeuge *berücksichtigt werden.

**Umsetzung**

Nachdem die organisatorischen Vorarbeiten durchgeführt worden sind, kann die Umsetzung der Fernwartung erfolgen. Dabei sind vor allem die Maßnahmen *OPS.2.4.M9 Verwaltung der Fernwartungswerkzeuge*, *OPS.2.4.M10 Einsatz von kryptographischen Verfahren bei der Fernwartung* und *OPS.2.4.M11 Patch- und Änderungsmanagement bei der Fernwartung *zu beachten. 

Es sollten für die Fernwartung ausschließlich sichere Authentisierungsmechanismen eingesetzt werden (siehe hierzu *OPS.2.4.M16 Authentisierungsmechanismen bei der Fernwartung*).

Alle Benutzer und Administratoren sollten ausreichend über die Prozesse der Fernwartung geschult werden (siehe hierzu *OPS.2.4.M15 Schulung zur Fernwartung*).

Da die reine Umsetzung der Fernwartung viele Schnittstellen zum internen sowie externen Netz aufweist, sind geeignete Maßnahmen zum Schutz der Netze, IT-Systeme und Anwendungen zu treffen (siehe hierzu *OPS.2.4.M7 Sichere Protokolle bei der Fernwartung*, *OPS.2.4.M3 Regelungen zu Kommunikationsverbindungen*, *OPS.2.4.M17 Passwortsicherheit bei der Fernwartung *und *OPS.2.4.M14 Absicherung der Fernwartung*).

Sollten Dritte in die Umsetzung der Fernwartung eingebunden werden, sollten die Empfehlungen der Maßnahme *OPS.2.4.M18 Fernwartung durch Dritte* beachtet werden.

Um eine Hochverfügbarkeit der Fernwartung gewährleisten zu können, sollten die Maßnahmen aus *OPS.2.4.M21 Redundante Verwendung von Kommunikationsnetzen* berücksichtigt werden.

**Betrieb**

Nach der Umsetzung der Anforderungen für die Fernwartung wird der Regelbetrieb aufgenommen. Damit Sicherheitsverstöße bemerkt werden, muss eine entsprechende Angriffsabwehr und Überwachung aller IT-Systeme und Anwendungen, die durch die Fernwartung verwaltet werden, erfolgen.

Da die Fernwartung immer Veränderungen unterworfen ist, die sich meist aus veränderten Anforderungen oder Einsatzszenarien ableiten, muss sichergestellt werden, dass das gewünschte Sicherheitsniveau aufrechterhalten wird (siehe hierzu* OPS.2.4.M19 Betrieb der Fernwartung und OPS.2.4.M11 Patch- und Änderungsmanagement bei der Fernwartung*).

**Notfallvorsorge**

Empfehlungen zur Notfallvorsorge für die Fernwartung finden sich in den Maßnahmen *OPS.2.4.M12 Datensicherung bei der Fernwartung* und *OPS.2.4.M20 Erstellen eines Notfallplans für den Ausfall der Fernwartung.*

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Fernwartung" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### OPS.2.4.M1 Planung des Einsatzes der Fernwartung [IT-Betrieb]

Der Einsatz der Fernwartung muss an die Institution angepasst und bedarfsgerecht hinsichtlich technischer und organisatorischer Aspekte geplant werden. Es sollten mindestens die folgenden Aspekte im Rahmen der Einsatzplanung betrachtet werden:

* Soll die Fernwartung In-Band (also innerhalb des normalen IT-Netzes) oder Out-Band (also über ein dediziertes Administrationsnetz) stattfinden? Bei erhöhtem Schutzbedarf empfiehlt es sich, die Fernwartung aus einem dedizierten Administrationsnetz durchzuführen.
* Welche Schnittstellen und Protokolle sollen verwendet werden?
* Was für ein Schutzbedarf liegt vor? Welche Schutzziele müssen erfüllt werden?
* Welche Auditierungsanforderungen müssen beachtet werden?
* Welche gesetzlichen und internen Regelungen sind zu berücksichtigen?
* Erfolgt die Fernwartung durch Dienstleister? Dann ist OPS.2.4.M18 Fernwartung durch Dritte umzusetzen.
* Dürfen Online-Dienste zur Fernwartung genutzt werden?
* Welche Aufgabenverteilung innerhalb der Institution muss beim Einsatz der Fernwartung erfolgen?
* Welche Anforderungen aus der Netzseparierung sind zu beachten?
Je genauer die Rahmenbedingungen bekannt und je präziser die Vorgaben formuliert sind, desto einfacher werden die nächsten Konzeptionierungs- und Umsetzungsschritte der Fernwartung.

#### OPS.2.4.M2 Sicherer Verbindungsaufbau bei der Fernwartung [Benutzer]

Die Initiierung eines Fernwartungs-Zugriffs muss immer aus der Institution heraus erfolgen. Dies kann durch Anruf des zu wartenden IT-Systems bei der Fernwartungsstelle oder über einen automatischen Rückruf (Callback) realisiert werden. Das externe Wartungspersonal muss sich zu Beginn der Wartung authentisieren. Wird die Verbindung zur Fernwartungsstelle auf irgendeine Weise unterbrochen, so muss der Zugriff auf das System durch einen "Zwangslogout" beendet werden.

Der Benutzer des fernadministrierten IT-Systems muss dem Fernzugriff explizit zustimmen, z. B. über eine entsprechende Bestätigung am System.

#### OPS.2.4.M3 Absicherung der Kommunikationsverbindungen bei der Fernwartung [IT-Betrieb]

Die Kommunikationsschnittstellen und möglichen Zugänge für einen Verbindungsaufbau von außen sind auf das notwendige Maß, entsprechend der verwendeten Betriebssysteme und weiteren damit in Verbindung stehenden Hardware- und Software-Komponenten, zu beschränken. Ebenso müssen alle Kommunikationsverbindungen nach vollzogenem Fernzugriff getrennt werden (Deaktivierung). Für eine Fernwartung müssen notwendige Ports ständig bereitgestellt werden. Zum Beispiel können die zur Verfügung stehenden Ports mit Hilfe eines Firewall-Portals und hinterlegten Firewall-Regel nach erfolgreicher Authentisierung eines berechtigten Administrators geöffnet werden.

Es müssen unter Berücksichtigung des Schutzbedarfes des jeweiligen IT-Systems, der Anwendung bzw. der damit verbundenen Netzseparierung sichere Authentisierungsmechanismen eingesetzt werden. Wird für die Kommunikation kein eigenständiges Administrationsnetz verwendet, sollte eine Alternative mit identischen Sicherheitsmerkmalen verwendet werden. Der erlaubte Personenkreis für einen Verbindungsaufbau sollte nach dem Minimalprinzip eingeschränkt werden.

Wichtig ist, dass bei den Kommunikationsverbindungen und dem Verbindungsaufbau bei der Fernwartung folgende Punkte beachtet werden:

* Sicherstellung der Vertraulichkeit der übertragenen Daten: Die Sicherstellung der Vertraulichkeit der übertragenden Daten muss durch eine ausreichende sichere Verschlüsselung erreicht werden.
* Sicherstellung der Integrität der übertragenen Daten: Die eingesetzten Übertragungsprotokolle müssen eine zufällige Veränderung übertragener Daten erkennen und beheben.
* Sicherstellung der Verfügbarkeit der Fernwartung: Falls zeitliche Verzögerungen bei der Fernwartung nur schwer zu tolerieren sind, sollten redundante Übertragungswege zur Verfügung gestellt werden.
* Sicherstellung der Nachvollziehbarkeit der Datenübertragung: Um eine Kommunikation nachvollziehbar zu machen, können Protokollierungsfunktionen eingesetzt werden, die nachträglich feststellen lassen, welche Daten wann und an wen übertragen wurden.
* Sicherstellung des Datenempfangs: Ist es für die Fernwartung von Bedeutung, ob Daten korrekt empfangen wurden, können Quittungsmechanismen eingesetzt werden, aus denen hervorgeht, ob der Empfänger die Daten korrekt empfangen hat.
#### OPS.2.4.M4 Regelungen zu Kommunikationsverbindungen [IT-Betrieb]

Unter Beachtung des Bausteins *NET.3.2 Firewall *muss die Fernwartung in das Firewall-Regelwerk der Institution eingebunden werden. Hierbei muss darauf geachtet werden, dass bestehende Firewall-Infrastrukturen und deren Regelungen nicht umgangen werden.

Entsprechend dem Minimalprinzip (Whitelist-Strategie) sollten die für die Fernwartung benötigten Protokolle ergänzt werden.

Bei der Überprüfung der Netz-Konnektivität mittels ICMP müssen die Regelungen für die lokalen und entfernten Prüfungen beachtet werden. Lokal empfiehlt es sich, einen Ping of localhost in der lokalen Firewall zur Überprüfung der korrekten Funktionstüchtigkeit der Netzwerkkarte zu erlauben. Zur Überprüfung der grundsätzlichen Netzkonnektivität sollte eine entfernte Prüfung mittels Ping auf die benötigte Gegenstelle erlaubt sein.

Im Sinne der Firewall-Sicherheit muss überprüft werden, ob Remote Procedure Calls (RPCs) durch die etablierte Sicherheitsarchitektur analysiert und gefiltert werden können. Sollte eine Filterung nicht möglich sein, müssen entsprechende Schutzmaßnahmen gegen missbräuchliche RPC-Aufrufe getroffen werden.

Gemeinsam mit den Basismaßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich Fernwartung.

#### OPS.2.4.M5 Einsatz von Online-Diensten [IT-Betrieb, Benutzer]

Oftmals ist eine etablierte Software für die Fernwartung kostenpflichtig und muss auf jedem Client installiert werden. In Ausnahmesituationen kann es jedoch hilfreich sein, kurzfristig IT-Systeme über eine Fernwartung zu administrieren. Pragmatisch erscheint die Lösung, dass die Clients eine Verbindung zu einem Online-Dienst aufbauen und der Administrator über einen Webserver über den Online-Dienst auf die Clients zugreift.

Werden Online-Dienste genutzt, entstehen aber sicherheitstechnische Risiken. Dies sollte daher grundsätzlich verboten sein. Die Fernwartung über Online-Dienste sollte durch technische Maßnahmen verhindert werden. Wenn ein grundsätzliches Verbot im Einzelfall nicht möglich ist, sollte der Einsatz auf ein Minimum und nur für klar definierte Einsatzgebiete mit strikten Regelungen beschränkt werden.

Bei Online-Diensten zur Fernwartung verbindet sich die IT-Systeme des Fernwartenden und des Administrators jeweils mit einem Dienstanbieter im Internet. Dabei ist vom Fernwartenden nicht erkennbar, was mit diesen Informationen beim Diensteanbieter passiert bzw. welche Eingriffsmöglichkeiten dort bestehen. Es könnten Inhalte mitgeschnitten oder auch manipuliert werden. Dies gilt z. B. auch für Tastatureingaben (z. B. Passwörter).

Oft starten die Clients der Fernwartenden den Dienst automatisch und verbinden sich mit dem Online-Dienst. Ist dies der Fall, kann jeder, der die Zugangsdaten kennt (oft nur eine ID und PIN) unbeobachtet und unbemerkt auf die Clients zugreifen.Es sollte verboten werden, dass Clients automatisch eine Verbindung zu Online-Diensten aufbauen können, dies sollte auch technisch verhindert werden.

Der Vorteil von Online-Diensten besteht darin, dass z. B. in einem Notfall eine Fernwartung schnell initiiert werden kann, weil bei den Beteiligten keine besondere Infrastruktur notwendig ist. In diesem Fall müssen allerdings vorab genau geregelt werden, in welchen Fällen und unter welchen Bedingungen Online-Dienste zum Fernzugriff erlaubt sind. Diese sind zu dokumentieren und mit dem ISB und dem Datenschutzbeauftragten der Institution vorab abzustimmen.

Die Regelungen sollten z. B. folgende Punkte umfassen:

* Es sollte festgelegt werden, in welchen Fällen eine Fernwartung über Online-Dienste erlaubt ist. Beispielsweise kann es notwendig sein, bei definierten Notfällen oder um unmittelbare Gefahr für den Dienstbetrieb abzuwenden, auf die Fernwartung über Online-Dienste zurückzugreifen.
* Es muss geregelt werden, wie und von wem die Nutzung von Online-Diensten autorisiert wird. Dabei sollten für den Einzelfall die existierenden Meldewege eingehalten werden.
* Ein automatischer Verbindungsaufbau sollte untersagt werden. Die Verbindung muss im Einzelfall vom fernzuwartenden IT-System freigegeben werden.
* Für jede Verbindung sind neue Zugangsdaten zu generieren (z. B. neue PIN).
* Die Zugangsdaten dürfen nicht in Klartext übermittelt werden (z. B. nur mündlich, verschlüsselt).
* In einer Verbindung über einen Online-Dienst dürfen keine Passwörter oder andere vertrauliche Informationen dargestellt oder lokal eingegeben werden. Mit einer "Whitelist" kann beschrieben werden, welche Informationen übertragen werden dürfen.
### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Fernwartung".

#### OPS.2.4.M6 Erstellung einer Richtlinie für die Fernwartung [IT-Betrieb]

Es ist zu entscheiden, ob die Aspekte der Fernwartung in bestehenden Richtlinien ergänzt werden oder eine eigenständige Richtlinie zu erstellen ist. Sollte eine eigenständige Richtlinie erstellt werden, so ist in den bestehenden Richtlinien der Institution auf die Richtlinie für Fernwartung zu referenzieren. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution sollten die wesentlichen Kernaspekte für die Fernwartung konkretisiert werden. Die Richtlinie muss allen Verantwortlichen, die an der Konzeption, dem Aufbau und dem Betrieb sowie der Aussonderung beteiligt sind, bekannt sein und die Grundlage für deren Arbeit bilden können. Die Umsetzung der in der Richtlinie geforderten Inhalte sollte regelmäßig überprüft werden und die Ergebnisse sind anschließend sinnvoll zu dokumentieren. Die Vorgaben innerhalb der Richtlinie sollten stringent sein, um spätere Risikoeinschätzungen oder Risikoübernahmen durchführen zu können. Wird kryptographische Kommunikation für die Fernwartung benötigt, müssen die Anforderungen des Bausteins *CON.1 Kryptokonzept* berücksichtigt werden. 

#### OPS.2.4.M7 Dokumentation bei der Fernwartung [IT-Betrieb]

Es muss eine aktuelle Dokumentation der Fernwartung vorliegen. Vorhandene Stellvertreter müssen, mit Hilfe der Fernwartungsdokumentation, zu jeder Zeit die Aufgaben und Prozesse, übernehmen können. Aus diesem Grund empfiehlt es sich, bei größeren Infrastrukturen ein einheitliches Namenskonzept für die IT-Systeme der Institution zu verwenden, um die Transparenz zu erhöhen und Arbeitsprozesse durch gezielte Zugriffe zu optimieren.

Da die Dokumente, z. B. Arbeitsanweisungen für die Initiierung eines Fernzugriffs, meist vertrauliche Informationen und Daten beinhalten, müssen sie an geeigneten Orten gesichert abgelegt werden und auch im Rahmen des Notfallmanagements zur Verfügung stehen. Ebenso müssen sie vor unbefugtem Zugriff geschützt sein. Sämtliche Fernzugriffsmöglichkeiten müssen erfasst und dokumentiert sein, sofern es sich nicht um übliche Vorgehensweisen nach Betriebssystemstandard handelt. Im Asset-Management der Institution sollten die Systeme und deren Schnittstellen für die Fernadministration hinterlegt sein. Für das Notfallmanagement und für den Wiederanlaufplansollten die internen und externen Ansprechpartner der Systeme hinterlegt werden.

Die allgemeine Dokumentation der administrativen Prozesse für die verschiedenen IT-Komponenten sollte in Form von Betriebshandbüchern erfolgen. Im Betriebshandbuch für das jeweilige System, welches aus der Ferne administriert werden soll, muss ein Hinweis enthalten sein, von welchem System aus, mit welchen Rechten und durch welche Organisationseinheit hierauf zugegriffen werden darf.

Innerhalb der Fernwartungsprozesse wird auf die folgenden dokumentierten Angaben zugegriffen:

* Die aktuelle Dokumentation aller vorhandenen IT-Systeme und deren Konfiguration sowie gegebenenfalls dem Namenskonzept der IT-Systeme,
* Die Dokumentation der auf den jeweiligen IT-Systemen eingerichteten Benutzer und deren Rechteprofilen,
* Die neu hinzugekommenen Hard- und Softwarekomponenten in der Systemdokumentation,
* Die Dokumentation aller sicherheitsrelevanten Abläufe wie der Datensicherung oder der Vernichtung von Datenträgern,
* Die Beschreibungen aller gefundenen und behobenen Fehler.
#### OPS.2.4.M8 Sichere Protokolle bei der Fernwartung [IT-Betrieb]

Es sollten ausschließlich aktuelle und als sicher eingestufte Kommunikationsprotokolle zur Fernwartung eingesetzt werden. Die Kommunikation sollte verschlüsselt erfolgen. Die Empfehlungen des BSI aus der technischen Richtlinie (TR-02102) „Kryptographische Verfahren: Empfehlungen und Schlüssellängen“ sollten bei der Auswahl der Protokolle und Algorithmen beachtet werden. Damit die eingesetzten Protokolle geeignet verwaltet und die Sicherheitsanforderungen berücksichtigt werden, müssen Informationen zu Schwachstellen aus der Fachpresse bzw. aus einschlägigen Quellen beachtet und kontinuierlich aktualisiert werden. 

Die Administration mittels Tunnel kann durch einen SSH-Tunnel, SSL-Tunnel oder IPSec-Tunnel abgesichert erfolgen. Es sollte ausgehend vom Schutzbedarf der Institution eine angemessene Tunnelmethode ausgewählt werden. Diese muss natürlich von den eingesetzten IT-Systemen auch unterstützt werden.

Für die Verwendung der folgenden Protokolle empfiehlt sich die Verwendung der jeweiligen Versionen:

* Einsatz von SSH in der Version 2
* Gebrauch von TLS 1.2
* Verwendung von SNMP ab Version 3
* Nutzung von IPsec mit IKEv2 und idealerweise Zertifikaten
Bei erhöhtem Schutzbedarf sollte für SNMP Version 3 jeweils ein eigenständiges Benutzerkonto für den lesenden, schreibenden und sendenden Zugriff eingerichtet werden.

Alle anfallenden Syslog- und Event-Meldungen im Rahmen der Fernwartung müssen entsprechend der Protokollierungs- und Überwachungsvorgaben der Institution aufbereitet werden. 

#### OPS.2.4.M9 Auswahl geeigneter Fernwartungswerkzeuge [IT-Betrieb]

Die Auswahl geeigneter Fernwartungswerkzeuge orientiert sich an den betrieblichen, sicherheitstechnischen und datenschutzrechtlichen Anforderungen der Institution. Die Auswahl und Bewertung der in Frage kommenden Fernwartungswerkzeuge sollte mittels einer Anforderungsanalyse und anschließender Risikobewertung festgestellt werden. Alle Beschaffungsentscheidungen sollten mit den Verantwortlichen des Einkaufes, dem System- und Anwendungsverantwortlichen sowie dem Sicherheitsmanagement abgestimmt werden. Hierbei sollte auch die Personalvertretung beteiligt werden.

Die Fernwartungswerkzeuge sollten die Sicherheitsanforderungen der Institution unter Berücksichtigung des zu erfüllenden Schutzbedarfs erfüllen. Hieraus ergeben sich insbesondere Anforderungen an die kryptographischen Mechanismen. Ebenso sollten bei der Datenübermittlung die Verbindungsqualität und die Systemauslastung berücksichtigt werden. Für alle weiteren Funktionen sollten immer die Aspekte aus *OPS.2.4.M1 Planung des Einsatzes der Fernwartung* berücksichtigt werden. 

Nach der Betrachtung der Funktionen der Fernwartungswerkzeuge sollten abschließend die Hilfestellungs- und Support-Leistungen geprüft werden. Es sollte möglich sein, Fragen und Problemstellungen den Hersteller bzw. Herausgeber zu richten. Dieser sollte über einen Support mit mehrstufiger Eskalation und Priorisierung verfügen.

#### OPS.2.4.M10 Verwaltung der Fernwartungswerkzeuge [IT-Betrieb, Benutzer]

Da Fernwartungswerkzeuge eine Vielfalt unterschiedlicher Funktionen ermöglichen, müssen organisatorische Verwaltungsprozesse zum Umgang mit den ausgewählten Werkzeugen etabliert werden. Es muss eine Bedienungsanleitung für den geeigneten Umgang mit den Fernwartungswerkzeugen für den IT-Betrieb vorliegen. Musterabläufe für die passive und die aktive Fernwartung müssen für die Nutzung innerhalb der Institution erstellt und kommuniziert werden. Um mögliche Sicherheitslücken, resultierend aus Fehlkonfigurationen und Bedienungsproblemen, zu minimieren, muss der IT-Betrieb im Umgang mit den Fernwartungswerkzeugen sensibilisiert und geschult werden. Es muss ein Anwendungsverantwortlicher benannt werden, der als Ansprechpartner für alle fachlichen Fragen zu den Fernwartungswerkzeugen dient.

**Vorgaben für die Administration**

* Die Berechtigungen der Administratoren sollten nach dem Minimumprinzip vergeben werden. Wenn Administratoren ihre Zuständigkeit und Aufgabenbereiche verändern, müssen die Berechtigungen zeitnah angepasst werden.
* Die vorhandenen Prozesse der Berechtigungsvergabe und des Berechtigungsentzugs der Institution sind für die Fernwartung entsprechend anzupassen.
* In den Arbeitsanweisungen für die Fernwartung sollte aufgeführt werden, welche exakten Einsatzzwecke vorgesehen sind und welche verfügbaren Mittel verwendet werden sollten und dürfen.
Die benötigten Berechtigungen und Identitäten für die Fernwartung von Systemen und Anwendungen sollten in das etablierte Identitäts- und Berechtigungsmanagement eingebunden werden.

**Vorgaben für die Prozesse der Fernwartung**

* Für den Betrieb von Fernwartungswerkzeugen sind Vorgaben und Abläufe festzulegen. Zum Beispiel sollte festgelegt werden, wer auf die Werkzeuge zugreifen darf und wo Änderungen damit durchgeführt werden dürfen. Dies sollte in Form eines Prozessschaubildes dokumentiert werden.
* Die Fernwartungswerkzeuge müssen in den Prozess der Fernwartung selbst und in das Patch- und Änderungsmanagement eingegliedert werden, sofern diese nicht bereits Teil des Betriebssystems sind.
#### OPS.2.4.M11 Einsatz von kryptographischen Verfahren bei der Fernwartung [IT-Betrieb]

Bei der Fernwartung müssen kryptographische Verfahren (Signaturen und Verschlüsselungsverfahren) genutzt werden, um einerseits die Kommunikation abzusichern und andererseits eine sichere Authentisierung zu gewährleisten. Es müssen hinreichend starke kryptographische Verfahren zur Verschlüsselung bzw. Signatur innerhalb der Fernwartung verwendet werden. Die Stärke der verwendeten kryptographischen Verfahren und Schlüssel muss im Rahmen der Fernwartung regelmäßig überprüft und falls erforderlich angepasst werden. Die genutzten kryptographischen Verfahren sind, basierend auf den internen Vorgaben und den Empfehlungen des BSI, auf dem aktuellen Stand der Technik zu halten. Die allgemeinen Anforderungen und Maßnahmen werden durch die Empfehlungen des Bausteins *CON.1 Kryptokonzept *abgedeckt und gelten auch für den Einsatz der Verfahren bei der Fernwartung. 

#### OPS.2.4.M12 Patch- und Änderungsmanagement bei der Fernwartung [IT-Betrieb]

Alle Updates, Patches und sonstigen Änderungen an IT-Systemen und den darauf laufenden Anwendungen, die per Fernwartung getätigt werden, unterliegen den allgemeinen Vorgaben zum Patch- und Änderungsmanagement der Institution.

Darüber hinaus sollten die Anforderungen des Bausteins OPS.1.1.3 Patch- und Änderungsmanagement beachtet werden.

#### OPS.2.4.M13 Datensicherung bei der Fernwartung [IT-Betrieb]

Um Datenverluste innerhalb der Infrastruktur für die Fernwartung zu vermeiden, müssen für diese regelmäßige Datensicherungen (Backups) durchgeführt werden. Es müssen Vorgaben für die Datensicherung bei der Fernwartung* *anhand der Menge und Wichtigkeit der laufend neu gespeicherten Daten und des möglichen Schadens für die Institution bei Verlust dieser Daten getroffen werden. Die Anforderungen müssen dabei dem Patch- und Änderungsmanagement der Institution entsprechen.

Es muss ein Verantwortlicher für die Durchführung und Überwachung der Datensicherungen sowie für die Wiederherstellungsübungen benannt werden. Dieser muss Fehlermeldungen in Bezug auf die Datensicherungen behandeln und Speicherplatzressourcen verwalten.

Die Datensicherungsanforderungen der Fernwartung müssen mit den allgemeinen Vorgaben der Institution zur Datensicherung korrespondieren und sollten die folgenden Kriterien berücksichtigen: 

* Zeitintervalle (z. B. täglich, wöchentlich, monatlich),
* Zeitpunkte (z. B. nachts, freitags abends),
* die Anzahl der aufzubewahrenden Generationen,
* der Umfang der zu sichernden Daten,
* die Speichermedien (abhängig von der Datenmenge),
* die vorherige Löschung der Datenträger vor Wiederverwendung (z. B. bei Bändern oder Kassetten),
* die Zuständigkeit für die Durchführung der Datensicherung,
* die Zuständigkeit für die Überwachung der Sicherung, insbesondere bei automatischer Durchführung (z. B. Fehlermeldungen, verbleibender Platz auf den Speichermedien),
* die Dokumentation der erstellten Sicherungen (Datum, Art der Durchführung der Sicherung sowie gewählte Parameter, Beschriftung der Datenträger)
#### OPS.2.4.M14 Dedizierte Systeme bei der Fernwartung [IT-Betrieb]

Innerhalb der Fernwartung sollten Komponenten eingesetzt werden, die ausschließlich diesem Anwendungszweck dienen. Alle weiteren Funktionen und Dienste sollten deaktiviert werden. Durch die Umsetzung des Minimalprinzips wird automatisch auch die mögliche Angriffsfläche reduziert, die von Angreifern für Kompromittierungen genutzt werden könnten. Die dedizierten IT-Systeme stellen ihre Leistung und Ressourcen (z. B. RAM, CPU-Kapazität, Festplattenplatz) somit nur dem notwendigen Einsatzzweck zur Verfügung. Die Komponenten der Fernwartung sollten sicher konfiguriert sowie mit den aktuellsten Betriebssystem- und Anwendungssoftwareversionen betrieben werden.

#### OPS.2.4.M15 Absicherung der Fernwartung [IT-Betrieb]

Der direkte administrative Zugriff auf die IT-Systeme und Anwendungen über öffentliche Netze sollte im Grundsatz verboten und verhindert werden. Die Fernwartung sollte nur aus dem internen Netz (z. B. Institutionsstandort)über einen Kopplungs-Server erfolgen. Ein Kopplungs-Server (auch Jump Server) ist ein dediziertes gehärtetes IT-System, das verwendet wird, um Geräte in separaten Sicherheitszonen zu verwalten. Bei einem Zugriff über das öffentliche Netz sollte sich dieses System in einer sogenannten demilitarisierten Zone (DMZ) der Firewall befinden. Damit die übertragenen Informationen nicht abgehört oder gar manipuliert werden können, darf die Administration nur über sichere Protokolle (beispielsweise über SSH und HTTPS) erfolgen.

Bei Zugang über das öffentliche Netz erhält der Fernwartende nur die Möglichkeit, einen SSH- oder VPN-Tunnel (siehe NET.3.3 VPN ) zum dedizierten System aufzubauen. Erst nach erfolgreicher Authentisierung öffnet ein Administrator aus dem inneren Netz einen entsprechenden Tunnel zwischen Wartungsobjekt und Kopplungs-Server und etabliert damit erst eine durchgehende Verbindung zwischen Fernwartendem und Wartungsobjekt (Rendezvous Prinzip). Die hierbei verwendeten Protokolle und Algorithmen sollten den Empfehlungen des BSI und den internen kryptographischen Vorgaben der Institution entsprechen. 

Weitere Anforderungen beim Einsatz von VPN sind im Baustein* NET.3.3 VPN* beschrieben.

#### OPS.2.4.M16 Schulungen zur Fernwartung [IT-Betrieb]

Den Administratoren sollten ausreichende Kenntnisse im Umgang mit den Fernwartungskomponenten vermittelt werden. Diese Schulungsmaßnahmen sollten in die bereits etablierten Verfahren der Institution integriert werden.

Innerhalb der Sensibilisierungs- und Schulungsmaßnahmen sollten Grundlagen, Konzepte und Besonderheiten der Fernwartung sowie Kenntnisse über relevante Kommandos für die Einrichtung, Änderung und Löschung von Einstellungen innerhalb der Werkzeuge geschult werden. Die Schulungen sollten regelmäßig, z. B. einmal jährlich, oder bei Bedarf stattfinden. Alle Sensibilisierungs- und Schulungsmaßnahmen sollten dokumentiert werden. 

Wichtige Aspekte bei der Planung der Sensibilisierung und Schulung von Administratoren der Fernwartung sind:

* Analyse der Zielgruppen für Sensibilisierungs- und Schulungsprogramme
* die Planung von Schulungsinhalten (z. B. Anforderungen an die Fernwartung auf Basis dieses Umsetzungshinweises, Gesetze, interne Regularien)
* Messung und Auswertung des Lernerfolgs
* Bekanntgabe von Ansprechpartnern zu Sicherheitsfragen
Die Themenfelder der Schulung müssen entsprechend dem Einsatzzweck des Werkzeuges angepasst werden. Die folgenden oder einer Kombination mehrerer Themenfelder können Inhalt der Schulung sein:

* Einsatz im Rahmen vom Problem- und Incident-Management
* Einsatz im Rahmen des Notfallmanagements
* Einsatz bei Sicherheitsvorfallbehandlungen
* Sensibilisierung der Mitarbeiter: 

 
	+ im Umgang mit Passwörtern
	+ im Umgang mit dem Fernwartungswerkzeug
	+ in der Umsetzung der Anforderungen bzgl. der Nutzung kryptographischer Verfahren
	+ die Nutzung sicherer Protokolle
	+ das Rechte- und Rollenkonzept
	+ in der Vorgehensweise und dem Betrieb der Fernwartungsinfrastruktur und deren Werkzeuge
	+ hinsichtlich den abhängigen prozessualen Schnittstellen sowie Anwendungsschnittstellen
	+ der Durchführung von Datensicherungen
	  

 
Die Mitarbeiter müssen darauf hingewiesen werden, was sie bei der Fernwartung zu beachten haben. Wenn IT-Systeme von Mitarbeitern fernadministriert werden, müssen sie der Fernwartung explizit zustimmen, z. B. über eine entsprechende Bestätigung am System. Außerdem müssen sie alle Tätigkeiten während der Fernwartung beobachten.

#### OPS.2.4.M17 Authentisierungsmechanismen bei der Fernwartung [IT-Betrieb]

Zur Fernwartung werden dem Schutzbedarf angemessene Mechanismen zur Identifikation und Authentisierung benötigt. Es sollte Zwei-Faktor-Authentisierung verwendet werden.

Die Auswahl der Authentisierungsmethode und die Gründe, die zu der Auswahl geführt haben, sollten dokumentiert werden. Bestehende Authentisierungsmechanismen der Institution dürfen durch die Fernwartung nicht umgangen werden. Zur Erleichterung der Anmeldung bei der Fernwartung empfiehlt es sich, diese in ein Identitäts- und Berechtigungsmanagement und deren Infrastruktur zu integrieren.

#### OPS.2.4.M18 Passwortsicherheit bei der Fernwartung [IT-Betrieb]

Falls bei der Fernwartung passwortbasierte Authentisierungen verwendet werden, sollten Passwortregeln definiert, dokumentiert und den Administratoren bekannt gemacht werden, um ein Mindestniveau der Passwortqualität sicherzustellen. Für die Fernwartung sollten diese Passwortregeln technisch forciert werden. Da für die Fernwartung Zwei-Faktor-Verfahren zur Authentisierung eingesetzt werden sollten, bietet das passwortbasierte Authentisierungsverfahren alleine nur einen Basisschutz.

Für die Passwortsicherheit innerhalb der Fernwartungsprozesse sollte eine Softwarelösung eingesetzt werden, die den Umgang mit vielen unterschiedlichen Passwörtern sowie das Erstellen sicherer Passwörter erleichtert. Da es viele differenzierte Passwort-Manager-Anwendungen gibt, sollte die Auswahl der Anwendung an Hand folgender Kriterien stattfinden:

* Aktueller Stand der Technik
* Komplexität der generierten Passwörter
* Unterscheidung nach Bedarf zwischen On- und Offline-Passwort-Manager
* Passwort-Manager mit Zwei-Faktor-Authentisierung
* Security Optionen (z. B. automatischer Log-Off)
#### OPS.2.4.M19 Fernwartung durch Dritte [IT-Betrieb]

Es kann verschiedene Gründe geben, warum die Fernwartung durch Dritte durchgeführt werden soll. Beispielsweise kann die Fernwartung zu den vereinbarten Serviceleistungen von Geräte-Herstellern gehören. Es können auch intern die erforderlichen Ressourcen oder das Fachwissen fehlen.

Fernwartung durch Dritte ist besonders kritisch. Sollte sie im Einzelfall notwendig sein sind folgende Punkte zu beachten:

* Im Grundsatz sollte eine Fernwartung durch Dritte nur passiv, also betrachtend sein.
* Alle durchgeführten Änderungen (z. B. der Konfigurationseinstellungen, innerhalb des Quellcodes) sollten dokumentiert werden. Diese Dokumentation muss der ferngewarteten Institution übergeben werden.
* Wenn dies technisch möglich ist, sollten alle Tätigkeiten während der Administration von Dritten durch eigene IT-Experten beobachtet werden. Beispielsweise können bei der Fernadministration eines Clients über eine graphische Benutzeroberfläche oft alle Ein- und Ausgaben am zu wartenden IT-System angezeigt und aufgezeichnet werden. Auch wenn Fernwartung durch Dritte genutzt wird, weil intern das Know-How oder die Kapazität nicht verfügbar ist, kann das externe Wartungspersonal nicht unbeaufsichtigt gelassen werden. Bei Unklarheiten über die Vorgänge sollte die Verbindung sofort unterbrochen bzw. auf betrachtenden Modus umgeschaltet werden. Danach können die Fragen geklärt werden.
* Es muss jederzeit die Möglichkeit geben, die Fernwartung lokal abzubrechen.
* Werden während der Wartung Daten oder Programme auf dem lokalen IT-System angelegt, so muss dies deutlich erkennbar und nachvollziehbar sein, also z. B. darf dies nur in besonders markierten Verzeichnissen oder unter bestimmten Benutzer-Kennungen erfolgen.
* Alle Fernwartungsvorgänge müssen aufgezeichnet werden. Dabei ist zumindest Anfang und Ende der Fernwartung sowie die Beteiligten festzuhalten. Wenn auf dem gewarteten IT-System niemand die Fernzugriffe beobachten kann, müssen alle Tätigkeiten bei der Durchführung der Fernwartung auf dem zu wartenden IT-System protokolliert werden.
* Für das externe Wartungspersonal müssen vertragliche Regelungen getroffen worden sein, vor allem über die Geheimhaltung von Daten (Vertraulichkeitsvereinbarungen). Insbesondere ist festzulegen, dass Daten, die im Rahmen der Wartung extern gespeichert wurden, nach Abschluss der Arbeiten sorgfältig gelöscht werden. Ebenso sind die Pflichten und Kompetenzen des externen Wartungspersonals sorgfältig festzulegen.
Bei höherem Schutzbedarf sollten außerdem die folgenden Maßnahmen ergriffen werden:

Vor Auswahl eines Fernwartungspartners sollten Informationen über dessen Zuverlässigkeit und weiterführende Informationen eingeholt werden. Im Rahmen der betrieblichen, sicherheitstechnischen, datenschutzrechtlichen Vereinbarungen sowie der Zusammenarbeit in Notfällen sollten beispielsweise die Anforderungen an die zu erfüllenden Service Level Agreements (SLAs, Dienstgütevereinbarungen) übergeben werden. Darüber hinaus sollten Abstimmungen hinsichtlich der zu erfüllenden Netzsegmentierungs- und Separierungsvorgaben sowie die erwarteten Schutzmechanismen für die Clients und den zugrundeliegenden Betriebssystemen getroffen werden. Die Institution sollte mit dem Dienstleister vertraglich entsprechende Kontrollmechanismen der vereinbarten Services festlegen.

In Bezug auf das Identitäts- und Berechtigungsmanagement gilt bei der Auswahl des Fernwartungsdienstleisters, das dieser nie mehr Rechte erhalten darf, als er für die Erfüllung seiner Aufgaben unbedingt benötigt und das sich jeder Mitarbeiter des Dienstleisters über eine eindeutige personalisierte Benutzerkennung authentisieren muss.

Da die Institution als Dienstleistungsnehmer keinen direkten Einfluss auf die Arbeitsweise des Dienstleisters und dessen Personal besitzt, können sich durch mögliche Nachlässigkeiten oder Unzuverlässigkeiten unkontrollierbare Risiken ergeben. Um diese Risiken zu minimieren, sollten vertragliche Vereinbarungen zu mindestens den folgenden Themenfeldern benannt werden:

* gemeinsames Risikomanagement durch die enge Verzahnung der Fernwartungssysteme des Dienstleisters mit den Systemen der Institution
* Sicherheitsvorfallerkennung und -behandlung
* gemeinsames Notfallmanagement inklusive der Benennung der Business Impact Analyse Werte (BIA-Werte)
* eine Vertraulichkeitsvereinbarung,
* Festlegung der Kompetenzen und Pflichten 
* Festlegungen bezüglich Backup und Archivierungsanforderungen
* eine genaue Beschreibung, wie die IT-Systeme des Dienstleisters geschützt werden,
* Festlegungen rund um die Möglichkeit der Auditierung
* Festlegungen zum Zwecke der Einbindung in die Überwachungs- und Protokollierungsinfrastruktur der Institutionsstandorte
* Übergabe bzw. bestätigte Vernichtung (Vernichtungserklärung) der Backup- und Archivierungsdaten im Rahmen der Fernwartung nach Vertragsbeendigung
Weitere Informationen für den Betrieb der Fernwartung durch Dritte sind in den Bausteinen OPS.2.1 Outsourcing-Nutzung und OPS.3.1 Outsourcing-Anbieter beschrieben.

#### OPS.2.4.M20 Betrieb der Fernwartung [IT-Betrieb]

Damit der Betrieb der IT-Systeme und Anwendungen durch die Fernwartung gewährleistet werden kann, sollten die Initiative zum Aufbau einer Support- oder Fernwartungssession immer von den Benutzern der betreuten IT-Komponenten ausgehen. Da diese direkt mit den IT-Systemen und Anwendungen arbeiten, sollte ein Meldeprozess für Support- und Fernwartungsanliegen etabliert werden (z. B. Ticketsystem). Alle Zugriffe durch die Fernwartung sollten erst nach erfolgreicher Authentisierung gestattet werden.

Die zur Etablierung der Fernwartungszugänge erforderlichen Freischaltungen an der Sicherheitsinfrastruktur sollte in die etablierten Prozesse für Firewall-Regeln integriert werden. Die Integration der Fernwartung in die Sicherheitsinfrastruktur sollte alle Angaben des Bausteins* NET.3.2 Firewall* berücksichtigen. 

Ein Fernwartungsdienstleister sollte keinen Zugriff auf IT-Systeme und Anwendungen außerhalb des für die jeweilige Fernwartung notwendigen erhalten. Um sicherzustellen, dass nur berechtigte Zugriffe durch Administratoren möglich sind, sollte die Kommunikation zwischen Fernwartungserver und -client mittels einer Stateful-Firewall, besser einer Firewall-NG, verifiziert werden.

Darüber hinaus sollte überlegt werden, am zu wartenden IT-System noch weitere Funktionalitäten zu implementieren:

* Wenn eine Fernwartung durch Dritte nicht überwacht wird: Sperren der Fernwartung im Normalbetrieb und explizite Freigabe für eine genau definierte Zeitspanne,
* Einschränkung der Rechte der Administratoren: Die Administratoren sollten nicht die vollen Administrator-Rechte besitzen. Es sollte eine abgestufte Rechteverwaltung realisiert werden. Die Administratoren sollte nur auf die Daten und Verzeichnisse Zugriff haben, die aktuell von der Fernwartung betroffen sind.
* Sollte die Session ohne die Einwirkung der Administratoren unterbrochen werden, sollte der Wiederaufnahme der Verbindung eine erneute Authentisierung vorangehen.
Darüber hinaus sollten die nachfolgenden Hinweise beachtet werden.

Alle Fernwartungsvorgänge müssen aufgezeichnet werden. Dabei ist zumindest Anfang und Ende der Fernwartung sowie die Beteiligten festzuhalten. Wenn auf dem gewarteten IT-System niemand die Fernzugriffe beobachten kann, müssen alle Tätigkeiten bei der Durchführung der Fernwartung auf dem zu wartenden IT-System protokolliert werden. Die anfallenden Protokolldaten sollten regelmäßig ausgewertet werden.

Wenn ein Security Information and Event Management (SIEM) vorhanden ist, sollten die Protokolldaten zur Überprüfung auf Sicherheitsvorfälle an dieses übermittelt werden. 

Nach einer definierten Anzahl von Fehlversuchen sollte eine temporäre Sperre des Zuganges zur Fernwartung aktiviert werden. Anders als in der konventionellen IT sind mit Blick auf die besonderen Anforderungen der Fernwartung hinsichtlich Verfügbarkeit solche Sperren aber beispielsweise nicht erst nach zwanzig, sondern bereits nach drei Fehlversuchen vorzunehmen. 

Ein erfolgreicher DoS- oder DDoS-Angriff kommt einer Einladung zu weiteren Angriffen auf die IT-Systeme der Institution und beteiligten Dienstleistern gleich. Aus diesem Grund sollten Mechanismen zur Erkennung und Abwehr von hochvolumigen Angriffen, TCP-State-Exhaustion Angriffen und Angriffen auf Applikationsebene implementiert sein. Mögliche Maßnahmen gegen diese Art der Angriffe sind nicht Bestandteil dieser Umsetzungshinweise, werden jedoch in den Umsetzungshinweisen der Bausteine* NET.3.1 Router/Switche* und *NET.3.2Firewall *beschrieben.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.2.4.M21 Erstellen eines Notfallplans für den Ausfall der Fernwartung(A)

Im Rahmen der Notfallvorsorge sollte ein Konzept entwickelt werden, wie die Folgen eines Ausfalls von Fernwartungskomponenten minimiert werden können und welche Aktivitäten im Falle eines Ausfalls durchzuführen sind. Durch den Notfallplan sollte sichergestellt sein, dass Störungen, Schäden und Folgeschäden minimiert werden sowie eine zeitnahe Wiederherstellung des Normalbetriebs erfolgt. Bei Hochverfügbarkeit sollte die Infrastruktur der Fernwartung mittels einer Business Impact Analyse auf Kritikalität geprüft werden.

Weitere Aspekte der Notfallplanung werden im Baustein im Baustein *DER.4 Notfallmanagement *behandelt. 

#### OPS.2.4.M22 Redundante Verwendung von mobilen Kommunikationsnetzen(A)

Für den Schutz der Kommunikationsnetze der Fernwartung bei Hochverfügbarkeitsanforderungen sollten redundante Verbindungs- bzw. Kommunikationsnetze eingerichtet werden. Es sollten geregelt werden, ob hierfür externe Telekommunikationsnetze genutzt werden sollen, z. B. über Mobilfunk.

Die internen IT-Systeme der Institution sollten neben den etablierten produktiven Wegen zusätzlich über ein nicht produktiv genutztes Fallback-Zugangsnetz erreichbar sein. Der Fallback-Zugang könnte zum Beispiel über eine DSL- oder LTE-Verbindung realisiert sein beziehungsweise durch eine Festnetzverbindung.

#### OPS.2.4.M23 Planung des sicheren Einsatzes in einem abgesicherten Netzsegment [IT-Betrieb]

Für die Fernwartung sollte ein abgesichertes Netzsegment eingesetzt werden, dieses sollte in der Art wie eine *Demilitarized Zone* (*DMZ) realisiert und betrieben werden.*

Im Bereich der Fernwartung sollten sich alle Fernwartungskomponenten möglichst im abgesicherten Netzsegment befinden und nicht direkt im internen Netz lokalisiert sein. Dadurch kann die Ausbreitung aus einem nicht vertraulichen Netz in das Netz mit dem Fernwartungssystem geschützt werden, wenn dazwischen entsprechende Analysewerkzeuge und Tools integriert sind.

Die Fernwartungszugänge sollten nicht dazu führen, dass vorhandene Sicherheitsinfrastrukturen umgangen werden und so ein Zusammenschluss von vertrauenswürdigen und nicht vertrauenswürdigen Netzen erfolgt.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

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

 
