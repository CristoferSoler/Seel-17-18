1 Beschreibung
--------------

### 1.1 Einleitung

Als Groupware (auch kollaborative Software genannt) werden Anwendungen und Systeme bezeichnet, mit denen mehrere Personen (Gruppen) über räumliche und/oder zeitliche Distanzen hinweg zusammenarbeiten können. Mithilfe von Groupware-Systemen können Gruppen untereinander und miteinander kooperieren und Termine abstimmen. Dokumente und Daten lassen sich durch Groupware von mehreren Benutzern gleichzeitig verwenden und bearbeiten, wodurch der Informationsfluss effizienter gestaltet wird. 

Unter dem Begriff Groupware-Systeme werden unter anderem der Groupware-Server, die zugehörigen Groupware-Clients und die erforderlichen Groupware-Dienste zusammengefasst. Neben den Basisfunktionen, wie z. B. Projektmanagement, E-Mail, Kalender oder Notizbuch, bieten neuere Applikationen sogenannte Social-Media-Erweiterungen an, durch die Mitarbeiter noch besser kommunizieren und kooperieren können.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, Informationen zu schützen, die in und mit Groupware abgelegt, verarbeitet oder übertragen werden. Dazu müssen die für Groupware eingesetzten IT-Komponenten und deren Schnittstellen angemessen abgesichert und geeignete Verfahrensweisen etabliert werden.

### 1.3 Abgrenzung

Der Baustein enthält lediglich spezifische Gefährdungen und Anforderungen für Groupware-Systeme. Gefährdungen und Anforderungen für die spezifischen Bausteine von Serverplattform, Betriebssystem und Clients sind nicht Bestandteil des Bausteins. Diese sind in den Bausteinen SYS.1.1 Allgemeiner Server sowie SYS.1.2 Allgemeiner Client und in den jeweiligen betriebssystemspezifischen Bausteinen zu finden.

Der Baustein APP.5.1 Groupware wird in einem Informationsverbund meist in Verbindung mit einem weiteren spezifischen Baustein der Schicht APP.1 E-Mail/Groupware/Kommunikation genutzt, diese müssen ebenfalls separat umgesetzt werden. Zu diesen Bausteinen zählen unter anderem APP.1.2 Microsoft Exchange/Outlook, APP.1.3 Kontact, APP.1.4 Lotus Notes/Domino und APP.1.5 Instant Messaging.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich* *Groupware von besonderer Bedeutung:

### 2 1 Unzureichende Planung der Groupware

Der Groupware-Prozess kann ohne entsprechend dokumentierte Regelungen und einem definierten Sicherheitsverfahren nicht geeignet in der Institution eingehalten werden. Potenzielle Sicherheitsrisiken können insbesondere dann auftreten, wenn die Groupware fehlerhaft in die Verzeichnisdienste eingebunden wird, Datenbanken dedupliziert werden und die spezifischen Aspekte von Groupware nicht in einer Sicherheitsrichtlinie dokumentiert sind. 

Falls in der Planung der Groupware-Systeme die prozessualen, organisatorischen und technischen Regelungen vernachlässigt werden, könnten die daraus entstehenden Freiheiten, fehlerhafte Einstellungen, Programmierungen und Angriffe (intern/extern) hervorrufen. Dies würde die Groupware-Systeme, den Groupware-Prozess und prozessübergreifende Schnittstellen in ihren Aufgabenerfüllungen behindern. 

### 2 2 Fehlerhafte Einstellung der Groupware

Da Groupware-Systeme komplex sind, können durch die vielen möglichen Einstellungen und durch die sich gegenseitig beeinflussenden Parameter zahlreiche Sicherheitsprobleme entstehen. So könnten beispielsweise Serverkomponenten auf ungeeigneten Systemen betrieben werden. Zusätzlich wäre es möglich, das essentielle Einstellungen (zum Beispiel Verschlüsselung einzelner Groupware-Dienste oder Beschränkungen der Rechte entsprechend dem Berechtigungsmanagement) ignoriert oder missachtet werden. Diese Sicherheitslücken können zu einem signifikanten Verlust der Verfügbarkeit, Authentizität und Vertraulichkeit von Informationen führen und somit die Funktionen der Groupware-Systeme behindern und verarbeitete Daten verfälschen. 

Werden Rechte bei einer Groupware-Datenbank fehlerhaft vergeben, kann dies im Berechtigungsmanagement der Institution schädigende Daten-Leak-Szenarien oder unberechtigte Manipulation verursachen. Die Manipulationen können dabei zum Beispiel in fehlerhaften Einstellungen resultieren, die das gesamte Groupware-System stören oder einzelne Dienste.

### 2 3 Missbrauch selbst entwickelter Makros und Programmierschnittstellen bei Groupware-Diensten

In vielen Tools und Anwendungen gibt es Programmierschnittstellen (z. B. als Application Programming Interface – API), die es erlauben, bestimmte Funktionen anderen Anwendungen bereitzustellen oder den Funktionsumfang der Anwendung zu erweitern. Groupware kann jedoch dazu missbraucht werden, um Schadsoftware zu verbreiten. Dazu zählen beispielsweise Schadprogramme, die direkt die Groupware-Systeme infizieren, um Informationen abzugreifen, zu verändern oder zu löschen. 

Auch können Makros dazu genutzt werden, Nachrichten, Termine oder Aufgaben weiterzuleiten bzw. zu verschieben. Sind Makros fehlerhaft oder werden in ihnen falsche Werte berechnet, können z. B. Indexfehler zu falschen Ergebnissen und möglicherweise unwirtschaftlichen Entscheidungen in der Institution führen. 

### 2 4 Fehlerhafte Vergabe von Zugangs- und Zugriffsrechten auf Groupware-Dienste

Wenn Zugangsrechte zu einem Groupware-Client oder Zugriffsrechte auf gespeicherte Daten in Groupware-Diensten nicht genügend beschränkt werden, können Sicherheitslücken entstehen. Werden diese Rechte fehlerhaft angelegt und administriert, kann zudem der Betrieb gestört werden, beispielsweise wenn ein Mitarbeiter nicht auf für ihn wichtige Informationen zugreifen kann. Ebenso ist es möglich, dass dadurch Angreifer auf vertrauliche Informationen zugreifen und so schützenswerte Daten einsehen können. 

### 2 5 Unzureichendes Wissen der Administratoren von Groupware-Systemen

Schon kleine Konfigurationsfehler können die Sicherheit eines Groupware-Systems beeinträchtigen. Personal, das zu wenig über Groupware-Anwendungen und -Dienste weiß, kann aufgrund der komplexen Systemarchitekturen und der spezifischen Schutzmechanismen der eingesetzten Groupware unabsichtlich Sicherheitslücken verursachen. Ein unzureichender geschulter Administrator kann auch in einem Notfall oft nicht effektiv reagieren (z. B. bei Funktionsfehlern und Kompromittierungen). Durch unzureichend geschulte und sensibilisierte Administratoren können unerwünschte Zustände innerhalb der Groupware-Dienste und -Prozesse entstehen. Hierzu kann gehören, dass zwischen den Endgeräten und den Groupware-Systemen nicht vollständig synchronisiert wird oder aber auch, dass im Kalender die Zeitzonen zu fehlerhaften Startzeiten beiden vorhandenen Terminen führt. 

### 2 6 Datenverlust bei Groupware-Anwendungen

Der Verlust gespeicherter Daten in Groupware-Anwendungen kann erhebliche Auswirkungen auf Geschäftsprozesse und damit auf die gesamte Institution haben. Werden Daten in Verbindung mit Groupware-Anwendungen verfälscht oder gehen verloren, können privatwirtschaftliche Institutionen in ihrer Existenz bedroht sein. In Behörden kann der Verlust oder die Verfälschung jener Daten die internen Verwaltungs- und Fachaufgaben verzögern oder sogar ausschließen. 

Insgesamt kann der Verlust gespeicherter Daten in Groupware-Anwendungen, neben einem Arbeitsausfall und den Kosten für eine Wiederbeschaffung, auch zu langfristigen Konsequenzen, wie beispielsweise Vertrauenseinbußen bei Kunden und Partnern, sowie einem negativen Eindruck in der Öffentlichkeit, führen. 

### 2 7 Angriffe auf Groupware-Systeme und -Anwendungen

Groupware-Systeme und einzelne Groupware-Anwendungen können durch Dritte kompromittiert werden. Bei Groupware-Systemen können z. B. die Benutzer, das interne Netz, genutzte Groupware-Server sowie der Nachrichtenempfänger vorsätzlich angegriffen werden. Eventuelle Sicherheitslücken können durch Angreifer benutzt werden, um Informationen in geschlossenen Groupware-Systemen auszulesen, zu verändern oder zu löschen. Auch bei einem nicht ausreichend geschützten Zugang zu den Groupware-Anwendungen könnten Angreifer beispielsweise auf vertrauliche Daten zugreifen. 

### 2 8 Unzuverlässigkeit von Groupware

Über Groupware-Dienste lassen sich schnell und komfortabel Daten austauschen. Das ist jedoch nicht immer zuverlässig: So können durch fehlerhafte IT-Systeme oder gestörte Übertragungswege Nachrichten verlorengehen. Ursachen dafür sind beispielsweise beschädigte Leitungen, ausgefallene Netzkopplungselemente oder falsch konfigurierte Kommunikationssoftware. E-Mails können auch abhandenkommen, weil die Empfängeradresse nicht korrekt angegeben wurde. Ebenso ist möglich, dass Nachrichten durch Dritte abgefangen werden oder dass diese gezielt Konversationen mitlesen. 

Groupware-Dienste sind in der Grundeinstellung meistens nicht kryptografisch abgesichert. Dadurch können über Kalenderdienste eventuell auch Unbefugte die Terminplanung von Gruppen oder einzelnen Personen einsehen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Groupware aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.5.1.A1 Sichere Installation von Groupware-Systemen [Leiter IT]

Alle für ein Groupware-System benötigten Komponenten (z. B. auch die Sicherheitsgateways) MÜSSEN entsprechend der geplanten Systemlandschaft sicher installiert und konfiguriert werden. Während das System installiert wird, MÜSSEN alle Passwörter sicher gewählt sein. Nicht genutzte Komponenten MÜSSEN deaktiviert werden. Auch MÜSSEN die Installationsquellen vor unbefugtem Zugriff geschützt werden. 

#### APP.5.1.A2 Sichere Konfiguration der Groupware-Clients [Leiter IT, Benutzer]

Die Groupware-Clients der Benutzer MÜSSEN durch den Administrator so vorkonfiguriert sein, dass sie, ohne das der Benutzer etwas tun muss, maximal sicher sind. Die Benutzer MÜSSEN darauf hingewiesen werden, dass die Konfiguration nicht selbstständig geändert werden darf. Es MUSS zudem verhindert und untersagt sein, dass Passwörter im Klartext gespeichert werden. Werden Nachrichten auf einem Mailserver gespeichert und wird z. B. über Internet Message Access Protocol (IMAP) darauf zugegriffen, MUSS eine Größenbeschränkung für das serverseitige Postfach eingerichtet werden. Bevor Dateianhänge ausgeführt werden, MÜSSEN sie mit einem Svchutzprogramm vor Schadsoftware überprüft werden. Es MÜSSEN sichere Einstellungen für E-Mails im HTML-Format, die Vorschaufunktionen und die E-Mail-Filterregeln sowie für die sichere automatische Weiterleitung von E-Mails gewählt werden. 

#### APP.5.1.A3 Sicherer Betrieb von Groupware-Systemen [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Es MÜSSEN alle sicherheitsrelevanten Servicepacks, Updates und Patches für das jeweilige Softwareprodukt eingespielt werden. Administratoren MÜSSEN sich daher regelmäßig über neu bekanntgewordene Schwachstellen, der eingesetzten Groupware-Systeme und der genutzten Betriebssysteme informieren und sie zeitnah schließen. Um Groupware-Systeme in der Institution abzusichern, MÜSSEN Schutzmechanismen gegen Denial-of-Service-(DoS)-Attacken ergriffen werden. Die lokale Kommunikation MUSS angemessen geschützt sein. Die Kommunikation über öffentliche Netze MUSS verschlüsselt sein. Außerdem MÜSSEN die Zugriffsrechte auf die lokal angeschlossenen Benutzer beschränkt werden. Es SOLLTE eine Richtlinie erstellt werden, die über die in der jeweiligen Groupware erlaubten Protokolle und Dienste informiert. Insbesondere der Mailserver MUSS so eingestellt werden, dass er nicht als Spam Relay missbraucht werden kann. 

#### APP.5.1.A4 Datensicherung Archivierung bei Groupware [Informationssicherheitsbeauftragter (ISB), Datenschutzbeauftragter, Benutzer]

Bei einem Groupware-System MÜSSEN die Daten regelmäßig gesichert werden. Dafür MUSS geregelt werden, wie die gesendeten und empfangenen E-Mails der E-Mail-Clients und auf E-Mail-Servern gesichert werden. Auch SOLLTE eine dokumentierte Vorgehensweise erstellt werden, wie E-Mails zu archivieren sind. Dabei SOLLTE grundsätzlich geregelt sein, wie, wann und wo gesendete und empfangene E-Mails archiviert werden, beispielsweise ob zentral oder dezentral ggf. von den Benutzern selbst. Bei der Archivierung von E-Mails SOLLTEN z. B. zeitliche und organisatorische Sicherheitsaspekte beachtet werden. Der erforderliche Zeitraum SOLLTE überprüft, die Archivierung geplant und zudem überlegt werden, wie sich die E-Mails wieder einspielen lassen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeine Groupware. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.5.1.A5 Festlegung der Kommunikationspartner [Leiter Organisation, Leiter IT, Informationssicherheitsbeauftragter (ISB), Datenschutzbeauftragter]

Es SOLLTE festgelegt werden, welche Kommunikationspartner welche Informationen erhalten dürfen. Sollen Informationen an einen Kommunikationspartner außerhalb der eigenen Institution übertragen werden, SOLLTE sichergestellt werden, dass der Empfänger berechtigt ist, diese Informationen weiterzuverarbeiten. Alle Informationen SOLLTEN entsprechend ihrer strategischen Bedeutung für die Institution klassifiziert werden. Die Kommunikationspartner SOLLTEN darauf hingewiesen werden, dass die übermittelten Daten nur zu dem Zweck benutzt werden dürfen, zu dem sie weitergegeben wurden. Auch aus Datenschutzgründen (Bundesdatenschutzgesetz (BDSG), Weitergabekontrolle) SOLLTE eine Übersicht erstellt werden, welche Empfänger berechtigt sind, Informationen, insbesondere personenbezogene Daten zu erhalten. Bei zu übermittelnden Daten SOLLTE ersichtlich sein, welche Kommunikationspartner Informationen erhalten haben bzw. erhalten werden. 

#### APP.5.1.A6 Vertretungsregelungen bei E-Mail-Nutzung [Vorgesetzte, Informationssicherheitsbeauftragter (ISB), Benutzer]

Für die E-Mail-Bearbeitung SOLLTE für jeden Mitarbeiter jederzeit ein geeigneter Vertreter benannt sein. Vertreter SOLLTEN auf das Postfach des Vertretenden zugreifen können. Alternativ SOLLTEN die E-Mails an den Vertreter weitergeleitet werden. Werden E-Mails weitergeleitet, SOLLTEN die vertretenden Benutzer mindestens darüber informiert werden. Um die Vertreterregelungsprozesse zu unterstützen, SOLLTEN für Autoreply-Funktionen in E-Mail-Programmen spezielle Regelungen etabliert werden, mit denen diese Funktionen sicher gesteuert werden können. Wenn Mitarbeiter die Autoreply-Funktionen benutzen, SOLLTEN KEINE interne Informationen weitergegeben werden. 

#### APP.5.1.A7 Planung des sicheren Einsatzes von Groupware-Systemen [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Bevor eine Institution ein Groupware-System einführt, SOLLTE entschieden werden, wofür es genutzt wird und welche Informationscluster zukünftig auf dem Groupware-System verarbeitet werden sollen. Es SOLLTE entschieden werden, ob ein eigener Groupware-Server in der Institution eingesetzt oder ein Provider genutzt werden soll. Auch SOLLTE ermittelt werden, wie die Groupware-Clients auf die Server zugreifen. Für jede benutzte Funktion einer Groupware SOLLTE eine eigene Planung durchgeführt werden, bei der auch deren Sicherheitsaspekte berücksichtigt werden. 

Bei der Planung SOLLTE auch festgelegt werden, welche Daten,. unter welchen Rahmenbedingungen über Groupware-Dienste übermittelt werden dürfen und wie sich dies auf den Schutzbedarf auswirkt. Es SOLLTE ebenso beschrieben werden, wie ein ordnungsgemäßer Dateitransfer gewährleistet werden kann, z. B. durch organisatorische Regelungen oder technische Maßnahmen. Darüber hinaus SOLLTE auch geregelt werden, ob und wie Groupware-Dienste privat benutzt werden dürfen. Auch SOLLTEN Institutionen regeln, wie Mitarbeiter mit Webmail umgehen sollen. 

#### APP.5.1.A8 Festlegung einer Sicherheitsrichtlinie für Groupware [Leiter IT, Informationssicherheitsbeauftragter (ISB), Benutzer]

Es SOLLTE eine Sicherheitsrichtlinie für Groupware-Systeme und -Anwendungen erstellt und regelmäßig aktualisiert werden. Alle Benutzer und Administratoren SOLLTEN über neue oder veränderte Sicherheitsvorgaben für Groupware-Systeme informiert werden. Die Groupware-Sicherheitsrichtlinie SOLLTE konform zu den geltenden übergeordneten Sicherheitsrichtlinien der Institution sein. Es SOLLTE geprüft werden, ob die Sicherheitsrichtlinien korrekt angewendet werden. 

Es SOLLTE eine Sicherheitsrichtlinie für Benutzer und eine für Administratoren erstellt werden. Für die Benutzer SOLLTE darin angegeben werden, wie sich die Kommunikation absichern lässt (z. B. für die Netz- oder E-Mail-Kommunikation), welche Benutzerzugriffsrechte es gibt (z. B. auf Groupware-Server oder -Datenbanken), wie Informationen an Kommunikationspartner weitergegeben werden sollen und wie sich übermittelte Informationen absichern lassen (z. B. Signaturen/Verschlüsselungen). Die zu regelnden Inhalte für Administratoren SOLLTEN darüber hinaus die Einstellungsoptionen der Groupware-Komponenten beinhalten, außerdem die Vorgaben für mögliche Zugriffe von anderen Servern auf einen Groupware-Server und Angaben zum berechtigten Zugriffspunkt, von dem aus auf einen Groupware-Server zugegriffen werden darf. 

#### APP.5.1.A9 Sichere Administration von Groupware-Systemen [Leiter IT]

Administrative Zugänge sowie die dazugehörigen Aufgaben SOLLTEN abhängig ihrer Zuständigkeit getrennt werden. Um ein Groupware-System reibungslos zu betreiben, SOLLTEN Administratoren ernannt und geschult werden. Alle Administrationsaufgaben im Bereich Groupware und die vergebenen Berechtigungen SOLLTEN ausreichend dokumentiert werden. An Administratoren SOLLTEN nur die für die jeweiligen Aufgaben notwendigen Berechtigungen vergeben werden. Nachdem alle Groupware-Komponenten installiert wurden, SOLLTEN sie sicher konfiguriert werden. Es SOLLTE darauf geachtet werden, dass die genutzten Groupware-Systeme ausreichend dimensioniert sind. Auch SOLLTEN vertrauenswürdige Groupware-Dokumentationen bei der Administration berücksichtigt werden. Es SOLLTE regelmäßig überprüft werden, ob die vorhandenen Dokumentationen aktuell sind. 

#### APP.5.1.A10 Schulung zur Systemarchitektur und Sicherheit von Groupware-Systemen für Administratoren [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Um ein Groupware-System korrekt und sicher administrieren zu können, SOLLTEN die verantwortlichen Administratoren geschult werden. Für die Schulungen SOLLTE überlegt werden, einen Schulungsplan festzulegen. Die Administratoren SOLLTEN in allen sicherheitsrelevanten Bereichen des Groupware-Systems ausgebildet werden. Weitere Schulungsschwerpunkte SOLLTEN sein: 

* Überblick über Lösungen für Kommunikationssicherheit (z. B. Verschlüsselung, VPN), 
* Protokollierung, 
* Sichern und Verwalten von Konfigurationsdaten, 
* Datensicherung, 
* Incident Handling sowie 
* Disaster-Recovery-Maßnahmen. 
#### APP.5.1.A11 Berechtigungsverwaltung für Groupware-Systeme [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Die vergebenen Berechtigungen, vor allem die privilegierten, SOLLTEN regelmäßig mit dem Berechtigungskonzept abgeglichen und zeitnah angepasst werden, wenn sich die Aufgaben der Benutzer und der Administratoren ändern. Es SOLLTE ein Berechtigungskonzept erstellt werden, das alle Groupware-Komponenten umfasst. Berechtigungen SOLLTEN möglichst restriktiv vergeben werden. Administrative Tätigkeiten auf Betriebssystemebene und Groupware-Anwendungsebene SOLLTEN soweit wie möglich voneinander getrennt werden. Auch innerhalb der Administration SOLLTEN Rollen und Verantwortlichkeiten getrennt werden. 

#### APP.5.1.A12 Schulung zu Sicherheitsmechanismen von Groupware-Clients für Beutzer [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Es SOLLTEN alle Benutzer für die Arbeit mit dem Groupware-Client geschult und eingewiesen werden. Dabei SOLLTE den Benutzern gezeigt werden, welche Sicherheitsmechanismen verfügbar sind und wie sie eingesetzt werden können. Wer Groupware nutzt, SOLLTE für Gefährdungen und einzuhaltende Sicherheitsmaßnahmen sensibilisiert werden. Die Benutzer SOLLTEN über potenzielles Fehlverhalten belehrt werden. Sie SOLLTEN auch davor gewarnt werden, an E-Mail-Kettenbriefen teilzunehmen und viele Mailinglisten zu abonnieren. 

#### APP.5.1.A13 Verifizierung der zu übertragenden Daten vor Weitergabe und Beseitigung von Restinformationen [Leiter IT, Benutzer]

Bevor eine Datei per E-Mail über einen Groupware-Dienst verschickt wird, SOLLTE überprüft werden, ob diese Restinformationen enthält, die nicht veröffentlicht werden dürfen. Alle Benutzer SOLLTEN über die Gefahren von Rest- und Zusatzinformationen in Dateien sensibilisiert werden. Um diese Gefahren zu minimieren, SOLLTEN Dateien stichprobenhaft auf enthaltene Restinformationen überprüft werden. Alle Zusatzinformationen (Dateieigenschaften) von Dateien in Standardsoftwareformaten SOLLTEN ermittelt, überprüft und falls erforderlich angepasst werden, bevor sie weitergegeben werden. Ebenso SOLLTE darauf geachtet werden, dass die Dateien keine sogenannten Slack Bytes enthalten. 

#### APP.5.1.A14 Vermeidung problematischer Dateiformate [Benutzer]

Es SOLLTE vorgegeben werden, wie mit E-Mails im HTML-Format, mit anderen Dateiformaten und Dateianhängen umzugehen ist. Für HTML-formatierten E-Mails SOLLTE eine Richtlinie erstellt werden, die auf entsprechende Inhalte von Benutzerschulungen, Weiterleitungseinstellungen, Umwandlungsoptionen (z. B. in Textformate), Benutzerhinweise sowie auf mögliche sichere und gesonderte Arbeitsplätze eingeht. 

#### APP.5.1.A15 Protokollierung von Groupware-Systemen [Leiter IT]

Es SOLLTEN alle sicherheitsrelevanten Ereignisse von Groupware-Systemen protokolliert werden. Dafür SOLLTE ein geeignetes Protokollierungskonzept erstellt werden. Der Zugriff auf die Protokolldaten SOLLTE eingeschränkt werden. Wichtige Systemereignisse, wie Änderungen, Fehler und Störungen an Hardware, Betriebssystem, Treibern, Diensten und sonstiger Software, SOLLTEN protokolliert und regelmäßig ausgewertet werden. 

#### APP.5.1.A16 Umgang mit SPAM [Leiter IT, Informationssicherheitsbeauftragter (ISB), Benutzer]

Grundsätzlich SOLLTEN alle Benutzer unerwünschte E-Mails ignorieren und löschen. Es SOLLTE auf unerwünschte E-Mails NICHT geantwortet, Links in der E-Mail gefolgt oder ein Anhang ausgeführt werden. Falls die Institution E-Mail-Filterprogramme einführen möchte, SOLLTE das mit dem Datenschutzbeauftragten, der Personalvertretung und den Benutzern abgesprochen werden. Für Newsgroups und Mailinglisten SOLLTEN Regelungen erstellt werden. 

#### APP.5.1.A17 Auswahl eines Groupware- oder Mail-Providers [Vorgesetzte, Datenschutzbeauftragter]

Soll kein eigener Groupware-Server betrieben werden, sondern ein Dienstleister für den Betrieb des Groupware-Server beauftragt werden, SOLLTEN die funktionalen Aspekte identifiziert und mit dem möglichen Provider abgestimmt werden. Auch SOLLTE sichergestellt werden, dass der Groupware- oder Mail-Provider alle erforderlichen Sicherheitsmechanismen umsetzt und dass seine Server sicher betrieben werden. Benötigte interne Anforderungen SOLLTEN unter der Betrachtung von juristischen Aspekten schriftlich fixiert werden. Es SOLLTEN alle Mitarbeiter darüber informiert werden, was dabei zu beachten ist, wenn sie externe Groupware-Dienste benutzen. 

#### APP.5.1.A18 Spam- und Virenschutz durch Einsatz eines E-Mail-Scanners auf dem Mailserver [Informationssicherheitsbeauftragter (ISB)]

Auf dem zentralen Mailserver SOLLTE ein E-Mail-Scanner mit integriertem speicher resistenten Virenschutzprogramm installiert werden, der eingehende und ausgehende E-Mails, insbesondere deren Anhänge, auf Spam-Merkmale und schädliche Inhalte überprüft. Da verschlüsselte E-Mails nicht automatisch überprüft werden können, SOLLTE auch festgelegt werden, wie mit solchen E-Mails zu verfahren ist. Wenn ein E-Mail-Scanner genutzt wird, SOLLTEN darüber alle Mitarbeiter, der Datenschutzbeauftragte und der Personalvertretung informiert werden. 

#### APP.5.1.A19 Verschlüsselung von Groupware [Leiter IT, Informationssicherheitsbeauftragter (ISB), Benutzer]

Daten, die durch Groupware-Systeme übermittelt werden, SOLLTEN mithilfe geeigneter Schutzmechanismen abgesichert werden. So SOLLTE mit Verschlüsselungsverfahren und digitalen Signaturen die Integrität und Vertraulichkeit elektronisch übermittelter Informationen sichergestellt werden, beispielsweise durch eine TLS-Verbindungsverschlüsselung.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.5.1.A20 Erstellen eines Notfallplans für den Ausfall von Groupware-Systemen [Notfallbeauftragter, Leiter IT, Informationssicherheitsbeauftragter (ISB)](A)

Es SOLLTE ein Konzept entworfen werden, wie die Folgen eines Ausfalls minimiert werden können und was bei einem Ausfall zu tun ist. Die Notfallplanung für das eingesetzte Groupware-System SOLLTE den existierenden Notfallplan der Institution berücksichtigen. Wichtige Aufgaben, um das Groupware-System aufrechtzuerhalten bzw. wieder in Betrieb nehmen zu können, SOLLTEN so beschrieben sein, dass sie von entsprechend geschultem Personal durchgeführt werden können. Es SOLLTE ein Wiederanlaufplan für das Groupware-System erstellt werden, der beschreibt, wie die Systeme nach einem Ausfall wieder geregelt hochzufahren sind. Notfallübungen zur Systemwiederherstellung SOLLTEN regelmäßig, auch alle Aspekte eines Systemausfalls bzw. einer Kompromittierung berücksichtigt, durchgeführt werden. 

#### APP.5.1.A21 Ende-zu-Ende Verschlüsselung(CI)

Um schutzbedürftige Informationen über alle Kommunikationspartner hinweg vertraulich zu halten, SOLLTE eine Ende-zu-Ende-Verschlüsselung eingesetzt werden. Es SOLLTEN nur Protokolle zur Verschlüsselung genutzt werden, die dem heutigen Stand der Technik entsprechen (siehe CON.1 Kryptokonzept).

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeine Groupware" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [KOLAB] Kolab Groupware

  

 Dokumentation, (zuletzt abgerufen am 29.09.2017)   
 <https://docs.kolab.org/>

 
* #### [TN170645] Exchange Server 2016

  

 Microsoft Technet, (zuletzt abgerufen 29.09.2017)  
 [https://technet.microsoft.com/de-de/library/mt170645.asp](https://technet.microsoft.com/de-de/library/mt170645(v=exchg.160).asp)

 
* #### [ZIMBRA] Zimbra Groupware

  

 Dokumentation, (zuletzt abgerufen am 29.09.2017)  
 <https://www.zimbra.com/documentation/>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeine Groupware" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.42 Social Engineering
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

