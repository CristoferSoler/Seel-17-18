1 Beschreibung
--------------

### 1.1 Einleitung

Microsoft Exchange ist eine Groupware-Lösung für mittlere bis große Institutionen. Mit ihr können elektronisch Nachrichten übermittelt werden und sie verfügt über weitere Dienste, um Workflows zu unterstützen und um mobile Geräten mittels Microsoft Exchange ActiveSync zu verwalten. Nachrichten, wie E-Mails, können mit Microsoft Exchange zentral verwaltet, zugestellt, gefiltert und versendet werden. Ebenso können typische Groupware-Anwendungen, wie Newsgroups, Kalender und Aufgabenlisten sowie Unified Messaging von Microsoft Exchange angeboten und verwaltet werden. Um die Funktionen von Microsoft Exchange nutzen zu können, ist neben dem Server-Dienst eine zusätzliche Client-Software nötig. Die Kombination aus Microsoft Exchange-Servern und Outlook-Clients wird hier als Microsoft Exchange-System bezeichnet. 

Microsoft Outlook ist ein Client, der durch die Installation des Office-Pakets von Microsoft oder durch Integration in die Betriebssysteme von mobilen Geräten direkt zur Verfügung gestellt wird. Darüber hinaus ermöglicht es die Webanwendung "Outlook Web App" über den Browser z. B. auf E-Mails, Kontakte und den Kalender zuzugreifen. Diese Dienstleistung ist im Microsoft Exchange-Paket bereits enthalten.

### 1.2 Zielsetzung

Das Ziel dieses Bausteins über typische Gefährdungen für Microsoft Exchange und Outlook zu informieren sowie aufzuzeigen, wie Microsoft Exchange und Outlook sicher in Institutionen eingesetzt werden.

### 1.3 Abgrenzung

Der Baustein enthält spezifische Gefährdungen und Anforderungen für Microsoft Exchange-Systeme. Gefährdungen und Anforderungen für die spezifischen Bausteine von Serverplattform, Betriebssystem und Clients sind nicht Bestandteil des Bausteins. Diese sind in den Bausteinen SYS.1.1 Allgemeiner Server sowie SYS.1.2 Allgemeiner Client und in den jeweiligen betriebssystemspezifischen Bausteinen zu finden.

Die Anforderungen aus dem Baustein APP.5.1. Groupware sind in jedem Fall zu erfüllen. Der vorliegende Baustein präzisiert und ergänzt Anforderungen, die für Microsoft Exchange-Systeme spezifisch sind.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Microsoft Exchange und Outlook von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichende Regelungen für Microsoft Exchange und Outlook

Übergreifende Regelungen und Vorgaben für Microsoft Exchange und Outlook sind notwendig, damit die Sicherheit der Informationen, die mit Microsoft Exchange und Outlook verarbeitet werden, gewährleistet wird. Beispielsweise können Daten verloren gehen, ungewollt verändert oder gelöscht werden, wenn Microsoft Exchange fehlerhaft und ungeregelt in das Active Directory eingebunden wird. Ähnliches gilt, wenn Postfachdatenbanken ungeregelt depubliziert und Microsoft Exchange unzureichend in der Sicherheitsrichtlinie berücksichtigt wird. Gleiches gilt, wenn die Microsoft Outlook-Clients ungeregelt auf die Microsoft Exchange-Server zugreifen können.

### 2 2 Fehlerhafte Migration von Microsoft Exchange

Microsoft Exchange-Systeme werden in der Praxis häufiger migriert als neu installiert. Um auf eine neue Version des Microsoft Exchange-Servers zu migrieren, muss in einigen Fällen das Betriebssystem auf eine neuere Version aktualisiert werden. Neue Betriebssysteme stellen ihrerseits oft Anforderungen an das bestehende Domänenkonzept und die existierenden Verzeichnisdienste. 

Wenn die Migration nicht sorgfältig geplant und durchgeführt wird, kann die interne Kommunikation über Microsoft Exchange in der Institution massiv gestört werden, was einen Rückgang der Produktivität zur Folge haben könnte. Während der Migration können Probleme bei der Konfiguration auftreten, indem sich z. B. die Konfigurationseinstellungen für die unterschiedlichen Versionen geändert haben oder bei der Anbindung an Verzeichnisdienste. Des Weiteren können fehlerhafte Protokolleinstellungen zu Unregelmäßigkeiten bei der Informationsübermittlung, Authentisierung und Verschlüsselung führen.

### 2 3 Unzulässiger Browserzugriff auf Microsoft Exchange

Mit Microsoft Exchange können die Anwender über einen Browser auf das eigene E-Mail-Konto zugreifen. Hierzu werden die Internet Information Services (IIS) verwendet, die fester Bestandteil des Microsoft Exchange-Servers sind. Wenn diese Funktion unsachgemäß geplant und fehlerhaft konfiguriert wird, kann unter Umständen unkontrolliert von außen auf das interne Netz zugegriffen werden. 

Wenn über einer Browser, der aus dem Internet genutzt wird, auf die E-Mails zugegriffen werden soll, birgt dies ein großes Gefahrenpotenzial. Ohne direkten Zugriff auf das Netz der Institution könnten Angreifer auf die E-Mails zugreifen und so unter anderem E-Mail-Adressen und -Inhalte ausspähen, E-Mail-Funktionen missbrauchen, Spam-Mails verschicken sowie Zugang zu firmeninternen Informationen erhalten. 

### 2 4 Unerlaubte Anbindung anderer Systeme an Microsoft Exchange

Microsoft Exchange-Systeme sind eng mit dem Betriebssystem Microsoft Windows verzahnt und arbeiten durch sogenannte Konnektoren mit Fremdsystemen zusammen. Mithilfe der Konnektoren (auch Connectors genannt) ist es anderen Systemen möglich, über bestimmte Protokolle (z. B. POP3) E-Mails von Microsoft Exchange-Servern abzurufen. 

Wenn bei einer Migration von Microsoft Exchange die Konnektoren nicht mit berücksichtigt werden, können die vorhandenen Konnektoren inkompatibel zu der migrierten Microsoft Exchange-Version sein. Hierdurch können E-Mails verloren gehen oder ungewollt verändert werden.

Außerhalb des homogenen Microsoft-Umfelds sind Sicherheitsstellungen, die sich nicht auf das Microsoft Exchange-System beziehen, ungültig. Ebenso verhält es sich mit festgelegten Sicherheitsparametern in Microsoft Exchange, die sich auf den Windows Server beziehen. Wenn verschiedene Teilsysteme separat administriert werden, können stets Inkonsistenzen auftreten. Unsachgemäß angebundene Fremdsysteme können zudem zur Folge haben, dass Daten verloren gehen oder das System blockiert wird.

### 2 5 Fehlerhafte Administration von Zugangs- und Zugriffsrechten unter Microsoft Exchange und Outlook

Werden Zugangsrechte zu einem Microsoft Outlook-Client bzw. auf innerhalb von Microsoft Exchange und Outlook gespeicherte Daten fehlerhaft angelegt und administriert, können Sicherheitslücken entstehen. Dies ist beispielsweise der Fall, wenn über die notwendigen Rechte hinaus zusätzliche Rechte vergeben werden und dadurch unberechtigte Personen auf vertrauliche Informationen zugreifen können. 

### 2 6 Fehlerhafte Konfiguration von Microsoft Exchange

Eine häufige Ursache für erfolgreiche Angriffe auf Dienste wie Microsoft Exchange sind fehlerhaft konfigurierte Systeme. Da ein Microsoft Exchange-System sehr komplex ist, können durch diverse Konfigurationseinstellungen und durch die sich gegenseitig beeinflussenden Parameter zahlreiche Sicherheitsprobleme entstehen. Die möglichen Fehlkonfigurationen erstrecken sich von der Installation und dem Betrieb der Microsoft Exchange-Komponenten auf ungeeigneten Systemen über nicht getätigte Verschlüsselungen und unzureichende Zugriffsbeschränkungen auf Microsoft Exchange-Servern bis hin zur fehlerhaften Rechtevergabe bei der Erzeugung oder Initialisierung einer Microsoft Exchange-Datenbank.

### 2 7 Fehlerhafte Konfiguration von Outlook

Der E-Mail-Client Microsoft Outlook ist ein wichtiger Teil des Microsoft Exchange-Systems. Für die Gesamtsicherheit des Systems ist es wichtig, dass der Client korrekt konfiguriert ist. Schon das ausgewählte Kommunikationsprotokoll kann spezielle Sicherheitsprobleme nach sich ziehen. Ebenso könnten private Schlüssel kompromittiert werden, mit denen E-Mails verschlüsselt und signiert werden. Wird auf Netzebene verschlüsselt, zum Beispiel durch IPSec oder TLS, kann dieser Verschlüsselungsmechanismus bei einem fehlerhaft konfigurierten Client unwirksam werden. Durch Fehlkonfiguration können Sicherheitsprobleme entstehen, zum Beispiel der Verlust der Vertraulichkeit durch unbefugten Zugriff.

### 2 8 Fehlfunktionen und Missbrauch selbst entwickelter Makros sowie Programmierschnittstellen unter Microsoft Outlook

Viele Softwarehersteller sehen in ihren Tools und Anwendungen Programmierschnittstellen vor, zum Beispiel als Application Programming Interface (API). Diese erlauben es, bestimmte Funktionen auch aus anderen Programmen heraus zu nutzen oder den Funktionsumfang der Anwendung zu erweitern. Microsoft Outlook kann missbraucht werden, um Schadsoftware zu verbreiten. Zu den Schadsoftwarevarianten zählen zum Beispiel bösartige Tools und Makros, die direkt Microsoft Outlook und die damit verbundenen E-Mail-Funktionen ausnutzen, um Informationen abzugreifen, zu verändern oder zu löschen. Makros wiederum können dazu genutzt werden, Nachrichten, Termine oder Aufgaben weiterzuleiten oder zu verschieben. Dabei können Fehler in Makros ein erhöhtes Risiko darstellen. Indexfehler innerhalb von Makros können zu falschen Ergebnissen und zu möglicherweise unwirtschaftlichen Entscheidungen in der Institution führen. Spezifische Folgen können unnötige Kosten oder ein automatisierter Datenabfluss sein.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Microsoft Exchange und Outlook aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt. 

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.5.2.A1 Planung des Einsatzes von Microsoft Exchange und Outlook [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Bevor Microsoft Exchange und Outlook eingesetzt werden können, MUSS der Einsatz von Microsoft Exchange und Outlook sorgfältig geplant werden. Dabei MÜSSEN mindestens folgende Punkte beachtet werden: 

* Aufbau der E-Mail-Infrastruktur,
* anzubindende Clients beziehungsweise Server-Systeme,
* Nutzung von funktionalen Erweiterungen,
* Absicherung der Zugangsports der Server- /Client-Komponenten,
* Vertraulichkeit, Integrität und Verfügbarkeit,
* zu verwendende Protokolle und
* Integration der Server- und Client-Systeme in die hierfür vorgesehenen Netzsegmente.
#### APP.5.2.A2 Auswahl einer geeigneten Microsoft Exchange-Infrastruktur [Leiter IT]

Es MUSS entschieden werden, mit welchen Systemen und Anwendungskomponenten, sowie in welcher hierarchischen Abstufung die Microsoft Exchange-Infrastruktur realisiert werden sollte. Im Rahmen der Auswahl MUSS auch entschieden werden, ob die Systeme als Cloud- oder lokaler Dienst betrieben werden sollen.

#### APP.5.2.A3 Berechtigungsmanagement

Für die Systeme der Microsoft Exchange-Infrastruktur MUSS ein Berichtigungskonzept erstellt, geeignet dokumentiert und angewendet werden. Es MÜSSEN den privilegierten Anwendern, sowie den Administratoren nur so viele Berechtigungen eingeräumt, wie für die Aufgabenerfüllung notwendig ist (Minimalprinzip). Es MUSS regelmäßig überprüft werden, ob die zugeteilten Rechte noch angemessen sind.

#### APP.5.2.A4 Zugriffsrechte auf Microsoft Exchange-Objekte

Die Zugriffsberechtigungen auf Microsoft Exchange-Objekte MÜSSEN auf Grundlage der das Prinzip des geringsten Privilegs (least privilege) festgelegt werden. Es MÜSSEN serverseitige Benutzerprofile für einen rechnerunabhängigen Zugriff auf Microsoft Exchange-Daten verwendet werden. Die Standard-NTFS-Berechtigungen auf das Microsoft Exchange-Verzeichnis MÜSSEN angepasst werden, sodass nur autorisierte Administratoren und Systemkonten auf die Daten in diesem Verzeichnis zugreifen können.

#### APP.5.2.A5 Datensicherung von Microsoft Exchange [Notfallbeauftragter]

Das bestehende Microsoft Exchange-System MUSS vor Installationen und Konfigurationsänderungen sowie in zyklischen Abständen gesichert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Microsoft Exchange und Outlook. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.5.2.A6 Sichere Installation eines Microsoft Exchange-Systems

Die Installation SOLLTE auf Basis der Einsatzplanung von Microsoft Exchange und Outlook und der festgelegten Sicherheitsrichtlinie erfolgen (siehe APP.1.2.A1 Planung des Einsatzes von Microsoft Exchange und Outlook). Da sich Microsoft Exchange-Systeme sehr stark in die Windows Umgebung integrieren, speziell in das Active Directory, SOLLTEN die entsprechenden spezifischen Sicherheitsrichtlinien berücksichtigt werden. Die Systeme, auf denen Microsoft Exchange und Outlook installiert werden soll, SOLLTEN geeignet abgesichert sein.

#### APP.5.2.A7 Migration von Microsoft Exchange-Systemen

Alle Migrationsschritte SOLLTEN gründlich geplant und dokumentiert werden. Es SOLLTEN die Microsoft Windows-Systemadministratoren an der Planung beteiligt werden. Es SOLLTEN bei der Planung der Migration Postfächer, Objekte, Sicherheitsrichtlinien, Active-Directory-Konzepte, E-Mail-Systeme und Funktionsunterschiede bei Microsoft Exchange und Outlook in den verschiedenen Versionen berücksichtigt werden. Das neue System SOLLTE, bevor es installiert wird, in einem separaten Testnetz geprüft werden, um Softwarefehlern und Kompatibilätsproblemen entgegenzuwirken.

#### APP.5.2.A8 Sicherer Betrieb von Microsoft Exchange

Alle Systeme und Anwendungen der Infrastruktur SOLLTEN so konfiguriert sein, dass sie den Schutzbedarf angemessen erfüllen. Dafür SOLLTE eine passende Basiskonfiguration zusammengestellt und dokumentiert werden. Die Einstellungen der einzelnen Konnektoren SOLLTEN ebenfalls angepasst werden. 

Die Verantwortlichen SOLLTEN bekannt gewordene Schwachstellen zeitnah in Abhängigkeit vom Schutzbedarf und der Kritikalität beheben. Generell SOLLTE darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden.

#### APP.5.2.A9 Sichere Konfiguration von Microsoft Exchange-Servern

Microsoft Exchange-Server SOLLTEN aufbauend auf den Vorgaben aus dem Sicherheitskonzept konfiguriert werden. Es SOLLTE eine maximal zulässige Größe sowohl für eingehende als auch für ausgehende Nachrichten eingestellt werden. Vorhandene Konnektoren SOLLTEN geeignet konfiguriert werden. Die Protokollierung des Microsoft Exchange-Systems SOLLTE aktiviert werden. Für vorhandenes Customizing SOLLTE ein entsprechendes Konzept erstellt werden.

Bei der Verwendung von funktionalen Erweiterungen (zum Beispiel Microsoft Exchange Access Sync, Spiegelport, Spamfilter, Outlook Web-App oder Data Loss Prevention) SOLLTE sichergestellt sein, dass die definierten Anforderungen an die Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit weiterhin erfüllt sind.

#### APP.5.2.A10 Einstellungen von Outlook

Nur Administratoren SOLLTEN die Outlook-Umgebung ändern können. Dazu SOLLTE für jeden Anwender ein eigenes Outlook-Profil mit den benutzerspezifischen Einstellungen angelegt werden. Die Anwender SOLLTEN nur ausgewählte Einstellungen (z. B. Signatur einrichten, Abwesenheitsagent aktivieren) benutzerdefiniert verändern können. . Dateianhänge SOLLTEN prinzipiell nicht automatisch aus E-Mails heraus geöffnet werden können. Vorschaufenster und die Autovorschau SOLLTE deaktiviert werden. E-Mails SOLLTEN NICHT automatisiert weitergeleitet werden. 

#### APP.5.2.A11 Absicherung der Kommunikation von und zu Microsoft Exchange-Systemen

Es SOLLTE nachvollziehbar entschieden werden, mit welchen Schutzmechanismen die Kommunikation von und zu Microsoft Exchange-Systemen abgesichert wird. Es SOLLTE entschieden und nachvollziehbar dokumentiert werden, welches der verschiedenen möglichen Verfahren Internet Protocol Security (IPSec) oder Transport Layer Security (TLS) eingesetzt werden soll.

Es SOLLTEN die 

* Administrationsschnittstellen,
* Client-Server-Kommunikation, 
* vorhandene Web-based-Distributed-Authoring-and-Versioning-(WebDAV)-Schnittstellen, 
* die Server-Server-Kommunikation, die Nachrichten-Kommunikation und 
* die Public-Key-Infrastruktur, die auf der E-Mail-Verschlüsselung von Microsoft Outlook (S/MIME) basieren,
verschlüsselt werden.

#### APP.5.2.A12 Einsatz von Microsoft Exchange für Outlook Anywhere

Outlook Anywhere SOLLTE entsprechend der Sicherheitsanforderungen der Institution konfiguriert werden. Der Zugriff auf Microsoft Exchange über das Internet SOLLTE auf die notwendigen Anwender beschränkt werden. Die Kommunikation zu Outlook Anywhere SOLLTE verschlüsselt werden (siehe APP.1.2.A11 Absicherung der Kommunikation von und zu Microsoft Exchange-Systemen).

#### APP.5.2.A13 Schulung von Administratoren [Leiter IT]

Für den Betrieb der Komponenten der Microsoft Exchange-Infrastruktur SOLLTE nur geeignetes und geschultes Personal eingesetzt werden.

#### APP.5.2.A14 Schulung zu Sicherheitsmechanismen von Outlook für Anwender [Informationssicherheitsbeauftragter (ISB)]

Outlook-Anwender SOLLTEN regelmäßig über bestehende und neue Gefahren beim Arbeiten mit Microsoft Outlook sensibilisiert und geschult werden. Allen Anwendern SOLLTEN relevante Sicherheitsmechanismen und die entsprechenden Vorgehensweisen innerhalb von Outlook vermittelt werden. Hierbei SOLLTEN Regelungen z. B. für Zugriffsmechanismen, Authentisierungsformen und kryptografische Vorgaben für die E-Mail-Verschlüsselung berücksichtigt werden.

#### APP.5.2.A15 Anwendungsdokumentation für Microsoft Exchange

Die Inhalte des Betriebshandbuches für Microsoft Exchange SOLLTEN nachvollziehbar dokumentiert sein. Das Betriebshandbuch SOLLTE angelehnt an den Lebenszyklus die Phasen Inbetriebnahme, Betrieb, Aussonderung und Wiederanlauf aufgebaut sein. Die Dokumentation SOLLTE gegen unbefugten Zugriff geschützt werden. Änderungen SOLLTEN nachvollziehbar dokumentiert bzw. referenziert sein.

#### APP.5.2.A16 Erstellung eines Notfallplans für den Ausfall von Microsoft Exchange und Outlook [Notfallbeauftragter]

Im Rahmen der Notfallvorsorge SOLLTE ein Konzept entworfen werden, mit dem sich die Folgen eines Ausfalls der Microsoft Exchange und Outlook-Komponenten minimieren lassen. Im Notfallplan SOLLTE definiert werden, was bei einem Ausfall zu tun ist, um eine zeitnahe Wiederherstellung des Normalbetriebs zu gewährleisten.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.5.2.A17 Verschlüsselung von Microsoft Exchange-Systemdatenbanken(CIA)

Es SOLLTE ein Konzept für die Verschlüsselung von pst-Dateien und Informationsspeicher-Dateien erstellt werden. Die Anwender SOLLTEN über die Funktionsweise und die Schutzmechanismen bei der Verschlüsselung von pst-Dateien informiert werden. Weitere Aspekte für lokale pst-Dateien, die berücksichtigt werden SOLLTEN, wenn Microsoft Exchange-Systemdatenbanken verschlüsselt werden, sind: 

* eigene Verschlüsselungsfunktionen, 
* Verschlüsselungsgrade sowie 
* Mechanismen zur Absicherung der Daten in einer pst-Datei.
Mechanismen wie z. B. Encrypting File System oder Windows BitLocker Laufwerkverschlüsselung SOLLTEN zur Absicherung der Daten in einer pst-Datei genutzt werden.

#### APP.5.2.A18 Regelmäßige Sicherheitsprüfungen für Microsoft Exchange-Systeme(CIA)

Das Microsoft Exchange-System SOLLTE regelmäßig auf Fehlkonfigurationen und Schwachstellen geprüft wird. Dafür SOLLTE es regelmäßig einer Sicherheitsprüfung durch unterschiedliche Personen unterzogen werden. Es empfiehlt sich, dafür eine Prüfliste aufzubauen, um einen definierten Prüfumfang zu gewährleisten. Folgende Aspekte SOLLTEN bei einer Prüfung berücksichtigt werden: 

* regelmäßige Recherchen sicherheitsrelevanter Informationen, 
* Berechtigungen für Revisionsbenutzer, 
* regelmäßige Prüfung der Berechtigungen, 
* Prüfung der Aktualität der Updates und 
* Prüfung der Sicherheit der Kommunikationsschnittstellen. 
Die Microsoft Exchange-Berechtigungen SOLLTEN regelmäßig mindestens stichprobenartig geprüft werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Microsoft Exchange und Outlook" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [TecNet] Microsoft Technet

  

 Microsoft Technet, (zuletzt abgerufen am 29.09.2017)  
 <https://technet.microsoft.com/de-de>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Microsoft Exchange und Outlook" von Bedeutung.

* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.45 Datenverlust
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

