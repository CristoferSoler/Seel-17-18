1 Beschreibung
--------------

### 1.1 Einleitung

Schadprogramme sind Programme, die in der Regel ohne Wissen und Einwilligung des Benutzers oder Besitzers eines IT-Systems schädliche Funktionen auf diesem ausführen. Diese Funktionen können ein breites Feld abdecken, das von Spionagemöglichkeiten über Erpressung (sogenannte Ransomware) bis hin zur Sabotage und Zerstörung von Informationen oder gar Geräten reicht.

Schadprogramme können grundsätzlich auf allen Betriebssystemen und IT-Systemen auftreten. Dazu gehören neben klassischen IT-Systemen wie Clients und Servern auch mobile Geräte wie Smartphones. Netzkomponenten wie Router, Industriesteuerungsanlagen und sogar IoT-Geräte, wie vernetzte Kameras, sind heutzutage ebenfalls vielfach durch Schadprogramme gefährdet. 

Schadprogramme verbreiten sich auf klassischen IT-Systemen zumeist über E-Mail-Anhänge, manipulierte Webseiten (Drive-by-Downloads) oder Datenträger. Smartphones werden in der Regel über die Installation von schädlichen Apps infiziert, auch Drive-by-Downloads sind möglich. Darüber hinaus sind offene Netzschnittstellen, fehlerhafte Konfigurationen und Softwareschwachstellen häufige Einfallstore auf allen IT-Systemen.

In diesem Baustein wird der Begriff "Viren-Schutzprogramm" verwendet. "Viren" stehen dabei als Synonym für alle Arten von Schadprogrammen. Gemeint ist also ein Programm zum Schutz vor jeglicher Art von Schadprogrammen.

### 1.2 Zielsetzung

Dieser Baustein beschreibt die Vorgehensweise, einen Schutz gegen Schadprogramme zu erstellen und umzusetzen, um eine Institution effektiv gegen Schadprogramme zu schützen.

### 1.3 Abgrenzung

In diesem Baustein werden die allgemeinen Anforderungen für den Schutz gegen Schadprogramme beschrieben. Spezifische Anforderungen, um bestimmte IT-Systeme der Institution vor Schadprogrammen zu schützen, finden sich in den jeweiligen Bausteinen insbesondere der Schicht SYS, etwa in SYS.2.2.3 Client unter Windows 10. Führt ein identifiziertes Schadprogramm zu einem Sicherheitsvorfall, sollten die Anforderungen des Bausteins DER.2.1. Behandlung von Sicherheitsvorfällen berücksichtigt werden. Die Anforderungen des Bausteins DER.2.3 Bereinigung helfen dabei, identifizierte Schadprogramme zu entfernen und einen bereinigten Zustand wieder herzustellen.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Schutz vor Schadprogrammen von besonderer Bedeutung:

### 2 1 Softwareschwachstellen und Drive-by-Downloads

Sind IT-Systeme nicht ausreichend vor Schadprogrammen geschützt, was unter anderem auch voraussetzt, dass Patches zeitnah eingespielt und Schutzmechanismen von Anwendungsprogrammen wie Browsern richtig konfiguriert sind, können Softwareschwachstellen ausgenutzt werden, um Schadcode auszuführen. Bei den sogenannten Drive-by-Downloads reicht es beispielsweise aus, eine schädliche Website zu besuchen. Eine Schwachstelle im Browser oder in einem installierten Plug-in wie Java oder Adobe Flash kann dann ausgenutzt werden, um das IT-System zu infizieren und dem Angreifer umfangreiche Kontrolle sowie einen Zugang zum Netz einer Institution zu verschaffen. Besonders gefährdet sind hier IT-Systeme, die nicht regelmäßig aktualisiert werden, etwa viele Smartphones.

### 2 2 Erpressung durch Ransomware

Eine weit verbreitete Art von Schadprogrammen ist die sogenannte Ransomware. Diese verschlüsselt die Daten des infizierten IT-Systems sowie häufig auch weitere Daten, die etwa über Netzfreigaben erreichbar sind. In der Regel verwenden die Angreifer dabei Verschlüsselungsmethoden, die ohne Kenntnis des Schlüssels nicht umkehrbar sind, und erpressen damit ihre Opfer um hohe Geldsummen. Besteht kein wirksamer Schutz gegen Schadprogramme und sind keine ergänzenden Vorkehrungen wie Datensicherungen getroffen, kann es zu erheblichen Einschränkungen der Verfügbarkeit von Informationen sowie zu massiven finanziellen sowie Image-Schäden kommen.

### 2 3 Gezielte Angriffe und Social Engineering

Institutionen werden häufig mit maßgeschneiderten Schadprogrammen angegriffen. Dabei werden z. B. Führungskräfte über Methoden des Social Engineerings dazu verleitet, schädliche E-Mail-Anhänge zu öffnen. Maßgeschneiderte Schadprogramme können häufig zudem nicht unmittelbar von Viren-Schutzprogrammen erkannt werden. Auch die Personalabteilung einer Institution kann beispielsweise ein Ziel sein, indem etwa maliziöse Bewerbungsunterlagen auf elektronischem Wege zugesendet werden. Hat der Angreifer auf diese Weise ein IT-System infizieren können, so kann er sich innerhalb der Institution ausbreiten und beispielsweise Informationen entwenden, manipulieren oder zerstören. 

### 2 4 Infektionen durch mobile Datenträger

Sind die Benutzer nicht ausreichend sensibilisiert, können auch mobile Datenträger als Einfallstor für Schadprogramme dienen. Ein Angreifer kann z. B. bösartige USB-Sticks auf dem Gelände einer Institution platzieren, die dann von unbedarften Benutzern an IT-Systeme angeschlossen werden. Gibt es keinen ausreichenden Schutz vor Schadprogrammen, kann ein Angreifer auf diesem Wege ebenfalls Zugriff auf das Netz und die Daten der Institution erlangen.

### 2 5 Botnetze

Über Schadprogramme können IT-Systeme einer Institution Teil von sogenannten Botnetzen werden. Ein Angreifer, der in einem solchen Botnetz häufig tausende von Systemen kontrolliert, kann diese beispielsweise einsetzen, um Spam zu versenden oder verteilte Denial-of-Service-Angriffe (DDoS) auf Dritte zu starten. Auch wenn die eigene Institution möglicherweise nicht unmittelbar geschädigt wird, kann dies trotzdem negative Auswirkungen bezüglich der Verfügbarkeit und Integrität der eigenen Dienste und IT-Systeme haben und sogar rechtliche Probleme nach sich ziehen.

### 2 6 Infektion von Produktionssystemen und IoT-Geräten

Neben klassischen IT-Systemen werden vermehrt auch Geräte durch Schadprogramme angegriffen, die auf den ersten Blick nicht wie offensichtliche Ziele wirken. Ein Angreifer kann beispielsweise eine über das Internet erreichbare Überwachungskamera infizieren, um zu spionieren. Aber auch eine vernetzte Glühbirne oder eine Kaffeemaschine mit App-Steuerung kann als Eintrittspunkt in das Netz der Institution oder als Teil eines Botnetzes dienen, wenn diese Geräte nicht ausreichend vor Schadprogrammen geschützt werden. Vernetzte Produktionssysteme oder Industriesteuerungen können ebenfalls mit Schadprogrammen manipuliert oder sogar zerstört werden, was Ausfälle und viele weitere Gefährdungen für die Institution und ihre Mitarbeiter, etwa durch Brände, nach sich ziehen kann.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz vor Schadprogrammen aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der ISB ist bei allen strategischen Entscheidungen zumindest einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten IT-Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.1.4.A1 Erstellung eines Konzepts für den Schutz vor Schadprogrammen

Es MUSS ein Konzept erstellt werden, welche IT-Systeme vor Schadprogrammen geschützt werden müssen. Außerdem MUSS festgehalten werden, wie der Schutz zu erfolgen hat. Ist kein verlässlicher Schutz möglich, so SOLLTEN die identifizierten IT-Systeme NICHT betrieben werden. Das Konzept SOLLTE nachvollziehbar dokumentiert werden.

#### OPS.1.1.4.A2 Nutzung systemspezifischer Schutzmechanismen

Es MUSS geprüft werden, welche Schutzmechanismen die verwendeten IT-Systeme sowie die darauf genutzten Betriebssysteme und Anwendungen bieten, um einen Schutz vor Schadprogrammen zu ermöglichen bzw. zu unterstützen. Diese Mechanismen MÜSSEN genutzt werden, sofern es keinen mindestens gleichwertigen Ersatz gibt oder gute Gründe dagegen sprechen. Werden sie nicht genutzt, SOLLTE dies begründet und dokumentiert werden.

#### OPS.1.1.4.A3 Auswahl eines Viren-Schutzprogrammes für Endgeräte

In Abhängigkeit vom verwendeten Betriebssystem, anderen vorhandenen Schutzmechanismen sowie der Verfügbarkeit geeigneter Viren-Schutzprogramme MUSS für den konkreten Einsatzzweck ein solches Schutzprogramm ausgewählt und installiert werden. Es DÜRFEN NUR Produkte für den Enterprise-Bereich mit auf die Institution zugeschnittenen Service- und Supportleistungen eingesetzt werden. Produkte für reine Heimanwender oder Produkte ohne Herstellersupport DÜRFEN NICHT im professionellen Wirk-Betrieb eingesetzt werden. Es DÜRFEN NUR Cloud-Funktionen solcher Produkte verwendet werden, bei denen keine gravierenden, nachweisbaren Daten- oder Geheimschutzaspekte dagegen sprechen.

#### OPS.1.1.4.A4 Auswahl eines Viren-Schutzprogrammes für Gateways und IT-Systeme zum Datenaustausch [Fachverantwortliche]

Für Gateways und IT-Systeme, die dem Datenaustausch dienen, MUSS ein geeignetes Viren-Schutzprogramm ausgewählt und installiert werden. Es DÜRFEN NUR Produkte für den Enterprise-Bereich mit auf die Institution zugeschnittenen Service- und Supportleistungen eingesetzt werden. Produkte für reine Heimanwender oder Produkte ohne Herstellersupport DÜRFEN NICHT im professionellen Betrieb eingesetzt werden. Es DÜRFEN NUR Cloud-Funktionen solcher Produkte verwendet werden, bei denen keine gravierenden, nachweisbaren Daten- oder Geheimschutzaspekte dagegen sprechen.

#### OPS.1.1.4.A5 Betrieb von Viren-Schutzprogrammen

Das Viren-Schutzprogramm MUSS für seine Einsatzumgebung geeignet konfiguriert werden. Die Erkennungsleistung SOLLTE dabei im Vordergrund stehen, sofern nicht Datenschutz oder Leistungs-Gründe im jeweiligen Einzelfall schwerer wiegen. Wenn sicherheitsrelevante Funktionen des Viren-Schutzprogramms nicht genutzt werden, SOLLTE dies begründet und dokumentiert werden. Bei Schutzprogrammen, die speziell für Desktop-Virtualisierung optimiert sind, SOLLTE transparent sein, ob auf bestimmte Detektionsverfahren zu Gunsten der Leistung verzichtet wird.

#### OPS.1.1.4.A6 Aktualisierung der eingesetzten Viren-Schutzprogramme und Signaturen

Auf den damit ausgestatteten IT-Systemen MÜSSEN die Scan-Engine des Viren-Schutzprogramms sowie die Signaturen für die Schadprogramme regelmäßig aktualisiert werden. Die Häufigkeit von qualitätsgesicherten Signatur-Updates MUSS dabei den Empfehlungen des Herstellers entsprechen.

Ein Update auf neue Programmversionen SOLLTE zeitnah nach Veröffentlichung erfolgen. Bei jedem Programmupdate des Viren-Schutzprogramms SOLLTE die Änderungsdokumentation des Herstellers auf relevante Änderungen hin überprüft werden. Nachdem das Update installiert wurde, MÜSSEN die Konfigurationseinstellungen überprüft und mit den dokumentierten Vorgaben abgeglichen werden.

#### OPS.1.1.4.A7 Sensibilisierung und Verpflichtung der Benutzer [Benutzer]

Benutzer MÜSSEN regelmäßig über die Bedrohung durch Schadprogramme aufgeklärt werden. Sie MÜSSEN die grundlegenden Verhaltensregeln einhalten, um die Gefahr eines Befalls durch Schadprogramme zu reduzieren. Dateien aus nicht vertrauenswürdigen Quellen SOLLTEN NICHT geöffnet werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Schutz vor Schadprogrammen. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.1.4.A8 Nutzung von Cloud-Diensten

Cloud-Dienste zur Verbesserung der Detektionsleistung der Viren-Schutzprogrammen SOLLTEN genutzt werden. Dabei MÜSSEN die entsprechenden Vorgaben aus den Anforderungen OPS.1.1.4.A3 Auswahl eines Viren-Schutzprogrammes für Endgeräte sowie OPS.1.1.4.A4 Auswahl eines Viren-Schutzprogrammes für Gateways und IT-Systeme zum Datenaustausch beachtet werden.

#### OPS.1.1.4.A9 Meldung von Infektionen mit Schadprogrammen [Benutzer]

Eingesetzte Viren-Schutzprogramm SOLLTEN automatisch eine Infektion mit einem Schadprogramm blockieren und melden. Die automatische Meldung SOLLTE an einer zentralen Stelle angenommen werden. Dabei SOLLTEN die zuständigen Mitarbeiter je nach Sachlage über das weitere Vorgehen entscheiden. Unabhängig von einer automatischen Meldung SOLLTE sich jedoch auch der Benutzer an die ihm benannten Ansprechpartner wenden, wenn der Verdacht auf eine Infektion mit einem Schadprogramm besteht. Das Vorgehen bei Meldungen und Alarmen der Viren-Schutzprogramme SOLLTE geplant, dokumentiert und getestet werden. Es SOLLTE insbesondere geregelt sein, was im Falle einer bestätigten Infektion geschehen soll.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.1.4.A10 Nutzung spezieller Analyseumgebungen(CIA)

Automatisierte Analysen in einer speziellen Testumgebung (basierend auf Sandboxen bzw. separaten virtuellen oder physischen Systemen) SOLLTEN für eine Bewertung von verdächtigen Dateien ergänzend herangezogen werden.

#### OPS.1.1.4.A11 Einsatz mehrerer Scan-Engines(CIA)

Zur Verbesserung der Erkennungsleistung SOLLTEN für besonders schutzwürdige IT-Systeme, wie Gateways und IT-Systemen zum Datenaustausch, Viren-Schutzprogramme mit mehreren alternativen Scan-Engines eingesetzt werden.

#### OPS.1.1.4.A12 Einsatz von Datenträgerschleusen(CIA)

Bevor insbesondere Datenträger von Dritten mit den IT-Systemen der Institution verbunden werden, SOLLTEN diese durch eine Datenträgerschleuse geprüft werden.

#### OPS.1.1.4.A13 Umgang mit nicht vertrauenswürdigen Dateien(CIA)

Ist es notwendig, nicht vertrauenswürdige Dateien zu öffnen, SOLLTE dies nur auf einem isolierten IT-System geschehen. Die betroffenen Dateien SOLLTEN dort z. B. in ein ungefährliches Format umgewandelt oder ausgedruckt werden, wenn sich hierdurch das Risiko einer Infektion durch Schadsoftware verringert.

#### OPS.1.1.4.A14 Auswahl und Einsatz von Cyber-Sicherheitsprodukten gegen gezielte Angriffe(CIA)

Bei erhöhtem Schutzbedarf und entsprechender Bedrohungslage SOLLTE der Einsatz sowie der Mehrwert von Produkten und Services geprüft werden, die im Vergleich zu herkömmlichen Viren-Schutzprogrammen einen erweiterten Schutzumfang bieten, wie z. B. Ausführung von Dateien in speziellen Analyseumgebungen, Härtung von Clients oder Kapselung von Prozessen. Vor einer Kaufentscheidung SOLLTEN Schutzwirkung und Kompatibilität zur eigenen IT-Umgebung getestet werden. 

#### OPS.1.1.4.A15 Externe Beratung(CIA)

Bei der Erstellung eines Konzepts zum Schutz vor Schadprogrammen SOLLTE externe Unterstützung in Anspruch genommen werden, wenn das eigene Know-how oder die Marktkenntnis nicht ausreichen. Um insbesondere Leistungsproblemen innerhalb der IT-Systeme und Netze vorzubeugen und den Schutz vor Schadprogrammen sinnvoll in ein Gesamtkonzept einzufügen, SOLLTE in komplexen IT-Infrastrukturen die Implementierung von Schutzprodukten nur durch erfahrene Experten vorgenommen werden. Nach der Installation von Schutzprogrammen SOLLTE die Konfiguration einem externen Expertenreview unterzogen werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Schutz vor Schadprogrammen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISFTS1] The Standard of Good Practice - Area TS1 Security Solutions

  

 insbesondere Area TS1 Security Solutions, Information Security Forum (ISF), 06.2016

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Schutz vor Schadprogrammen" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.39 Schadprogramme
* G 0.42 Social Engineering
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

