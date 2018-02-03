1 Beschreibung
--------------

### 1.1 Einleitung

Ein Webserver ist die Kernkomponente jedes Webangebotes: Er nimmt Anfragen der Clients (Browser) entgegen und liefert, sofern möglich, die entsprechenden Inhalte zurück. Der Transport der Daten erfolgt in der Regel über das Hypertext Transfer Protocol (HTTP) oder dessen mit Transport Layer Security (TLS) verschlüsselte Variante HTTP Secure (HTTPS). Da Webserver eine einfache Schnittstelle zwischen Serveranwendungen und Benutzern bieten, werden sie auch häufig für interne Informationen und Anwendungen in Institutionsnetzen (Intranet) eingesetzt. 

Webserver sind (meistens) direkt im Internet verfügbar und bieten somit eine exponierte Angriffsfläche. Deswegen müssen sie durch geeignete Schutzmaßnahmen abgesichert werden.

### 1.2 Zielsetzung

Ziel des Bausteins ist der Schutz des Webservers und der Informationen, die durch den Webserver bereitgestellt werden.

### 1.3 Abgrenzung

Die Bezeichnung Webserver wird sowohl für die Software verwendet, die die HTTP-Anfragen beantwortet, als auch für die IT-Systeme, auf denen diese Software ausgeführt wird. In diesem Baustein wird vorrangig die Webserver-Software betrachtet. Sicherheitsaspekte des IT-Systems, auf dem die Webserver-Software installiert ist, werden in den entsprechenden Bausteinen der Schicht IT-Systeme behandelt (siehe SYS.1.1 *Allgemeiner Server* sowie beispielsweise SYS.1.3 *Server unter Linux oder *SYS.1.2.2 *Windows Server 2012*).

Empfehlungen, wie Webserver in die Netzarchitektur zu integrieren und mit Firewalls abzusichern sind, finden sich in den Bausteinen NET.1.1 *Netz-Architektur und Design* bzw. NET.3.2 *Firewall*.

Dynamische Inhalte und über HTML hinausgehende Funktionen werden durch Webanwendungen bzw. Webservices bereitgestellt. Diese sind nicht Gegenstand des vorliegenden Bausteins, sondern werden in den Bausteinen APP.3.1 *Webanwendungen* und APP.3.5 *Webservices* behandelt.

Der Baustein CON.1 *Kryptokonzept *beschreibt, wie kryptografische Schlüssel sicher verwaltet werden können.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Webserver von besonderer Bedeutung:

### 2 1 Reputationsverlust

Schaffen es Angreifer, eine Webseite zu manipulieren bzw. umzugestalten (Defacement), so kann der Ruf der Institution geschädigt werden. Ebenso kann die Veröffentlichung falscher Informationen (etwa fehlerhafter Produktbeschreibungen) dazu führen, dass die Reputation der Institution in der Öffentlichkeit verloren geht oder dass die Institution abgemahnt wird. Ein Schaden kann auch entstehen, wenn die Webseite nicht verfügbar ist und potenzielle Kunden deshalb zu Mitbewerbern wechseln.

### 2 2 Manipulation des Webservers

Ein Angreifer kann sich Zugang zu einem Webserver verschaffen, um dort Dateien zu manipulieren. Er könnte beispielsweise die Konfiguration ändern, zusätzliche Dienste starten, Schadsoftware installieren oder Webinhalte modifizieren. Er könnte auch Dateien, die zum Download angeboten werden, durch Dateien mit Schadprogrammen ersetzen. Auch kann ein Angreifer den manipulierten Server beispielsweise nutzen, um DDoS-Angriffe (DDoS, Distributed Denial of Service) auszuführen. Wird der eigene Server dazu benutzt, Schadsoftware zu verteilen, kann es passieren, dass der Webserver auf Blacklists geführt wird und für Besucher nicht mehr erreichbar ist.

### 2 3 Distributed Denial of Service (DDoS)

Durch DDoS-Angriffe kann ein Webserver teilweise oder auch ganz ausfallen. Für Benutzer ist das Webangebot dann nur noch sehr langsam oder gar nicht mehr verfügbar. Für viele Institutionen ist ein solcher Ausfall schnell geschäftskritisch, z. B. für einen Online-Shop.

Neben DDoS lässt sich auch mit anderen Arten von Denial-of-Service-Angriffen die Verfügbarkeit eines Webangebotes gezielt für einzelne Nutzer beeinträchtigen, indem beispielsweise einzelne Accounts durch fehlerhafte Anmeldungen gesperrt werden. Ein Angreifer könnte z. B. durch ungültige Anmeldeversuche eine Benutzerkontensperre auslösen.

### 2 4 Verlust vertraulicher Daten

Viele Webserver verwenden noch veraltete kryptografische Verfahren, wie RC4 oder SSL. Eine unzureichende Authentisierung bzw. eine ungeeignete Verschlüsselung kann dazu führen, dass Angreifer die Kommunikation zwischen den Clients und den Servern oder zwischen den Servern mitlesen oder ändern können.

### 2 5 Verstoß gegen Gesetze oder Regelungen

Verstöße gegen gesetzliche Regelungen, insbesondere gegen Telemedien- und Datenschutzgesetze, können rechtliche Konsequenzen nach sich ziehen. Ferner können die Webserverinhalte gegen das Urheberrecht verstoßen, etwa wenn Bilder verwendet werden, für die keine Rechte erworben worden sind.

### 2 6 Software-Schwachstellen oder -Fehler

Werden Updates und Patches für Webserver oder benutzte Erweiterungen nicht oder zu spät eingespielt, kann der Webserver erfolgreich angegriffen werden. Dadurch können Angreifer Dateien oder Dienste manipulieren oder den Webserver für weitere Angriffe missbrauchen. 

### 2 7 Fehlende oder mangelhafte Fehlerbehebung

Treten Fehler während des Betriebs eines Webservers auf, kann sich das zum Beispiel auf die Verfügbarkeit des Webservers auswirken. Auch werden eventuell Inhalte unvollständig dargestellt oder Sicherheitsmechanismen fallen aus. Werden Fehler nicht korrekt behandelt, ist sowohl der Betrieb als auch der Schutz der Funktionen und Daten eines Webservers nicht mehr gewährleistet.

### 2 8 Unzureichende Protokollierung von sicherheitsrelevanten Ereignissen

Werden sicherheitsrelevante Ereignisse vom Webserver unzureichend protokolliert, können diese zu einem späteren Zeitpunkt nicht nachvollzogen und die Ursache nicht mehr ermittelt werden. Kritische Fehler und Angriffe, wie beispielsweise unbefugte Konfigurationsänderungen, bleiben so lange Zeit unbemerkt. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Webserver aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.3.2.A1 Sichere Konfiguration eines Webservers

Nachdem ein Webserver installiert wurde, MUSS eine sichere Grundkonfiguration vorgenommen werden. Dazu MUSS beispielsweise der Webserver-Prozess einem Benutzerkonto mit minimalen Rechten zugewiesen werden. Auch MUSS der Webserver in einer gekapselten Umgebung ausgeführt werden, sofern dies vom Betriebssystem unterstützt wird. Der Webserver-Dienst DARF NICHT über unnötige Schreibberechtigungen verfügen. Nicht benötigte Module und Funktionen des Webservers MÜSSEN deaktiviert werden.

#### APP.3.2.A2 Schutz der Webserver-Dateien

Alle Dateien auf dem Webserver, insbesondere Skripte und Konfigurationsdateien, MÜSSEN so geschützt werden, dass sie nicht unbefugt gelesen und geändert werden können.

Es MUSS sichergestellt sein, dass die Webserver-Anwendung nur auf Dateien zugreifen kann, die sich innerhalb eines definierten Verzeichnisbaums (WWW-Wurzelverzeichnis) befinden. Ressourcen außerhalb des WWW-Verzeichnisses DÜRFEN NICHT aus diesem heraus verlinkt oder verknüpft werden. 

Weiterhin MÜSSEN Funktionen, die Verzeichnisse auflisten, deaktiviert werden. Dateien, die nicht verändert werden sollen, MÜSSEN schreibgeschützt sein. Vertrauliche Daten MÜSSEN verschlüsselt übertragen und gespeichert werden.

#### APP.3.2.A3 Absicherung von Datei-Uploads und -Downloads

Alle mithilfe des Webservers veröffentlichten Dateien MÜSSEN vorher auf Schadprogramme geprüft werden. Zudem MÜSSEN Dokumente von Restinformationen bereinigt werden. Abrufbare Dateien MÜSSEN auf einer separaten Partition der Festplatte gespeichert sein. 

Es MUSS eine Maximalgröße für Datei-Uploads spezifiziert sein. Für Uploads MUSS genügend Speicherplatz reserviert werden. Der Ablageort der Uploads MUSS zufällig erzeugt werden und DARF NICHT durch den Benutzer beeinflussbar sein.

#### APP.3.2.A4 Protokollierung von Ereignissen

Der Webserver MUSS mindestens folgende Ereignisse protokollieren:

* erfolgreiche Zugriffe auf Ressourcen,
* fehlgeschlagene Zugriffe auf Ressourcen aufgrund von mangelnder Berechtigung, nicht vorhandenen Ressourcen und Server-Fehlern sowie
* allgemeine Fehlermeldungen.
Die Protokollierungsdaten SOLLTEN regelmäßig ausgewertet werden.

#### APP.3.2.A5 Authentisierung

Wenn sich Clients am Webserver authentisieren, MUSS hierfür eine verschlüsselte Verbindung genutzt werden (siehe APP.3.2.A11 *Verschlüsselung über TLS*). Die Passwortdateien auf dem Webserver MÜSSEN kryptografisch gesichert und vor unbefugtem Zugriff geschützt gespeichert werden.

#### APP.3.2.A6 Zeitnahes Einspielen sicherheitsrelevanter Patches und Updates

Die verantwortlichen Mitarbeiter MÜSSEN sich regelmäßig bei verschiedenen Quellen über aktuelle Schwachstellen in der eingesetzten Webserver-Software informieren und sicherheitsrelevante Updates zeitnah einspielen. Software-Updates und Patches für Webserver sowie benutzte zusätzliche Anwendungen und Erweiterungen MÜSSEN ausschließlich aus vertrauenswürdigen Quellen bezogen werden und ausreichend getestet werden, bevor sie eingespielt bzw. eingesetzt werden. Bevor Updates oder Patches installiert werden, MUSS stets sichergestellt sein, dass der ursprüngliche Zustand des Webservers wiederhergestellt werden kann.

#### APP.3.2.A7 Rechtliche Rahmenbedingungen für Webangebote [Informationssicherheitsbeauftragter (ISB)]

Werden über den Webserver für Dritte Inhalte publiziert oder Dienste angeboten, MÜSSEN dabei verschiedene rechtliche Rahmenbedingungen beachtet werden. So MÜSSEN die jeweiligen Telemedien- und Datenschutzgesetze sowie das Urheberrecht eingehalten werden. Auch SOLLTEN die Anforderungen an die Barrierefreiheit gemäß Behindertengleichstellungsgesetz beachtet werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Webserver. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.3.2.A8 Planung des Einsatzes eines Webservers

Um geeignete Sicherheitsmaßnahmen für den Webserver auszuwählen, SOLLTE geplant und dokumentiert werden, für welchen Zweck er eingesetzt und wie der Webserver in die vorhandene IT-Infrastruktur integriert werden soll. In der Dokumentation SOLLTEN auch die Informationen oder Dienstleistungen des Webangebots und die jeweiligen Zielgruppen beschrieben werden. Für den technischen Betrieb und die Webinhalte SOLLTEN Verantwortliche festgelegt werden. 

#### APP.3.2.A9 Festlegung einer Sicherheitsrichtlinie für den Webserver [Informationssicherheitsbeauftragter (ISB)]

Es SOLLTE eine Sicherheitsrichtlinie erstellt werden, in der die erforderlichen Maßnahmen und Verantwortlichkeiten benannt sind. Weiterhin SOLLTE geregelt werden, wie Informationen zu aktuellen Sicherheitslücken besorgt werden, wie Sicherheitsmaßnahmen umgesetzt werden und wie vorgegangen werden soll, wenn Sicherheitsvorfälle eintreten.

#### APP.3.2.A10 Auswahl eines geeigneten Webhosters [Informationssicherheitsbeauftragter (ISB), Leiter IT]

Wird der Webserver nicht von der Institutionen selbst betrieben, sondern werden Angebote externer Dienstleister genutzt (Webhosting), SOLLTE die Institution bei der Auswahl eines geeigneten Webhosters auf folgende Punkte achten:

* Es SOLLTE vertraglich geregelt werden, wie die Dienste zu erbringen sind. Dabei SOLLTEN Sicherheitsaspekte schriftlich im Vertrag in einem Service Level Agreement (SLA) festgehalten werden. 
* Bei allen angebotenen Produkten SOLLTE die Basisinstallation sicher gestaltet werden. Der Dienstleister SOLLTE seine Kunden über die Risiken von zusätzlichen Anwendungen und Erweiterungen (Plug-ins) informieren. Darüber hinaus SOLLTE er sich dazu verpflichten, regelmäßig auf vorhandene Updates der genutzten Programme hinzuweisen.
* Die für die Diensterbringung eingesetzten IT-Systeme SOLLTEN vom Dienstleister regelmäßig kontrolliert und gewartet werden. Er SOLLTE dazu verpflichtet werden, bei technischen Problemen oder einer Kompromittierung von Kundensystemen zeitnah zu reagieren.
* Der Dienstleister SOLLTE grundlegende technische und organisatorische Maßnahmen umsetzen, um seinen Informationsverbund zu schützen.
#### APP.3.2.A11 Verschlüsselung über TLS

Der Webserver SOLLTE für alle Verbindungen eine Verschlüsselung über TLS anbieten (HTTPS). Wenn eine HTTPS-Verbindung angeboten wird, dann SOLLTEN alle Inhalte über HTTPS verfügbar sein. Sogenannter Mixed Content SOLLTE NICHT verwendet werden. Kritische Aktionen, wie die Anmeldung an einer Webanwendung (Login), SOLLTEN über HTTPS erfolgen.

#### APP.3.2.A12 Geeigneter Umgang mit Fehlern und Fehlermeldungen

Aus den HTTP-Informationen und den angezeigten Fehlermeldungen SOLLTEN NICHT der Name und die Version der Webserver-Software ersichtlich sein. Auch SOLLTE sichergestellt werden, dass der Webserver ausschließlich anwendungsspezifische Fehlermeldungen ausgibt, die der Information des Benutzers dienen. Bei unerwarteten Fehlern SOLLTE der Webserver in einen sicheren Zustand übergehen.

#### APP.3.2.A13 Zugriffskontrolle für Webcrawler

Der Zugriff von Webcrawlern SOLLTE nach dem Robots-Exclusion-Standard geregelt werden. Inhalte SOLLTEN mit einem Zugriffsschutz versehen werden (siehe APP.3.2.A5 *Authentisierung*), um sie vor Webcrawlern zu schützen, die sich nicht an diesen Standard halten.

#### APP.3.2.A14 Integritätsprüfungen und Schutz vor Schadsoftware

Es SOLLTE regelmäßig geprüft werden, ob die Dateien und Webinhalte noch integer sind und nicht durch Angreifer verändert wurden. Auch SOLLTEN die Dateien regelmäßig auf Schadsoftware geprüft werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.2.A15 Redundanz(A)

Webserver SOLLTEN redundant ausgelegt werden. Auch die Internetanbindung des Webservers und weitere IT-Systeme, wie etwa der Webanwendungsserver, SOLLTEN redundant ausgelegt sein.

#### APP.3.2.A16 Penetetrationstest und Revision [Informationssicherheitsbeauftragter (ISB), Leiter IT](CIA)

Es SOLLTEN regelmäßig Penetrationstests durchgeführt werden. Die Tests SOLLTEN dabei ausschließlich von zuverlässigen, vertrauenswürdigen und qualifizierten Mitarbeitern oder Dienstleistern durchgeführt werden. Im Vorfeld SOLLTEN mit allen Auftragnehmern für Penetrationstests detaillierte Vereinbarungen zur Durchführung und Auswertung der Tests getroffen werden. Auch SOLLTE das Einverständnis aller zuständigen Stellen eingeholt werden. Für den Testzeitraum SOLLTEN die jeweiligen Ansprechpartner verbindlich feststehen und auch erreichbar sein. Nach dem Penetrationstest SOLLTEN die Ergebnisse ausreichend geschützt und vertraulich behandelt werden. Der Abschlussbericht SOLLTE dem ISB vorgelegt werden. 

#### APP.3.2.A17 Erweiterte Authentisierungsmethoden für Webserver(CI)

Es SOLLTEN erweiterte Authentisierungsmethoden eingesetzt werden, z. B. Client-Zertifikate oder Mehr-Faktor-Authentisierung.

#### APP.3.2.A18 Schutz vor Denial-of-Service-Angriffen(A)

Um Denial-of-Service-Angriffe frühzeitig erkennen zu können, SOLLTE der Webserver ständig überwacht werden. Des Weiteren SOLLTEN Maßnahmen definiert und umgesetzt werden, die solche Angriffe verhindern oder zumindest abschwächen.

#### APP.3.2.A19 Einrichtung eines Internet-Redaktionsteams [Fachverantwortliche, Leiter IT](CIA)

Um Webangebote zu pflegen, SOLLTE eine eigenständige Internetredaktion eingerichtet werden. Die Internetredaktion SOLLTE alle Rollen enthalten, die im Konzept für Webangebote als Verantwortliche genannt wurden. Bei umfangreichen Webangeboten SOLLTE zusätzlich ein Ansprechpartner für Webanwendungen bestimmt werden. Ebenso SOLLTEN Prozesse, Vorgehensweisen und Verantwortliche benannt werden für den Fall von Problemen oder Sicherheitsvorfällen.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Webserver" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [CS068] BSI-Veröffentlichung zur Cyber-Sicherheit und sicheres Webhosting

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 08.2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_068.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_068.pdf)

 
* #### [HVK] Hochverfügbarkeitskompendium

  

 BSI, (zuletzt abgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium_node.html)

 
* #### [ISIWEB] BSI-Standards zur Internetsicherheit, Sicheres Bereitstellen von Webangeboten

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), (zuletzt abgerufen am 29.08.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Web-Server/web\_server\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Web-Server/web_server_node.html)

 
* #### [MLFTLS] BSI-Handlungsleitfaden, Migration auf TLS 1.2

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), Version 1.2, 06.2016  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden\_Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_2.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden_Mindeststandard_BSI_TLS_1_2_Version_1_2.pdf)

 
* #### [NIST80044] NIST Special Publication (SP) 800-44

  

 Guideline on Securing Public Web Servers, NIST,09.2017  
 <https://csrc.nist.gov/publications/detail/sp/800-44/version-2/final>

 
* #### [TR21022] BSI Technische Richtlinie, Kryptografische Verfahren

  

 Verwendung von Transport Layer Security (TLS), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2017  
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Webserver" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

