1 Beschreibung
--------------

### 1.1 Einleitung

Dieser Baustein deckt allgemeine Sicherheitsanforderungen für alle IT-Systeme ab, die anderen IT-Systemen Dienste bereitstellen, wie Clients oder anderen Servern. Diese Dienste können Basisdienste für das lokale oder externe Netz sein, aber auch den E-Mail-Austausch ermöglichen oder Datenbanken und Druckerdienste anbieten. Server haben eine zentrale Bedeutung für die Informationstechnik und damit für funktionierende Arbeitsabläufe einer Institution. Oft erfüllen Server Aufgaben, ohne dass eine direkte interaktive Nutzung durch einen Benutzer erfolgt. Ergänzend gibt es Serverdienste, die direkt mit den Anwendern interagieren und nicht auf den ersten Blick als Server-Dienst wahrgenommen werden, beispielsweise X-Server unter Unix.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist der Schutz von Informationen, die auf Servern verarbeitet, angeboten oder darüber übertragen werden, sowie der damit zusammenhängenden Dienste.

### 1.3 Abgrenzung

In der Regel werden Serversysteme unter Betriebssystemen betrieben, bei denen jeweils spezifische Sicherheitsanforderungen zu berücksichtigen sind. Für verbreitete Server-Betriebssysteme sind im IT-Grundschutz-Kompendium eigene Bausteine vorhanden, die diesen Baustein präzisieren. Der Baustein "Allgemeiner Server" bildet die Grundlage für die konkreten Bausteine, auf der diese aufbauen. Sofern für ein betrachtetes System ein konkreter Baustein existiert, ist dieser zusätzlich zum Baustein Allgemeiner Server anzuwenden. Falls für eingesetzte Serversysteme kein spezifischer Baustein existiert, müssen die Anforderungen dieses Bausteins geeignet konkretisiert werden.

Die jeweils spezifischen Dienste, die vom Server angeboten werden, sind nicht Bestandteil dieses Bausteins. Für diese Server-Dienste müssen zusätzlich zu diesem Baustein noch weitere Bausteine umgesetzt werden, gemäß den Ergebnissen der Modellierung nach IT-Grundschutz. Soweit für ein Serversystem im Einzelfall auch eine interaktive Nutzung durch Benutzer vorgesehen ist (z. B. Terminalserver), sind die damit verbundenen Sicherheitsaspekte ebenfalls gesondert zu betrachten, beispielsweise indem die entsprechenden konkretisierten Bausteine angewendet werden.

2 Gefährdungslage
-----------------

Die folgenden spezifischen Bedrohungen und Schwachstellen sind für Allgemeine Server von besonderer Bedeutung.

### 2 1 Software-Schwachstellen oder -Fehler

Je komplexer Software ist, desto häufiger treten Programmier- oder Designfehler auf. Unter Software-Schwachstellen werden unbeabsichtigte Programmfehler verstanden, die dem Anwender nicht oder noch nicht bekannt sind und ein Sicherheitsrisiko für das IT-System darstellen. Es werden ständig neue Sicherheitslücken in vorhandener, auch in weitverbreiteter oder ganz neuer Software gefunden.

Werden Softwarefehler nicht erkannt und zeitnah behoben, können die bei der Anwendung entstehenden Fehler weitreichende Folgen haben. Bei weitverbreiteter Standardsoftware können Software-Schwachstellen schnell dazu führen, dass schwerwiegende Sicherheitsprobleme für alle Arten von Institutionen entstehen können.

Insbesondere Fehler in Serverdiensten können gravierende Auswirkungen haben. Bei einer Schwachstelle oder einem Fehler in einem Netzdienst sind keine lokalen Zugriffsrechte notwendig, um diese auszunutzen, oft reicht es, dass der Angreifer über das Netz zugreifen kann. Bietet der Server den Serverdienst mit der Schwachstelle oder dem Fehler im Internet an, könnte unter Umständen von jedem IT-System weltweit dieser Fehler oder diese Schwachstelle ausgenutzt werden.

### 2 2 Datenverlust

Der Verlust von Daten kann besonders bei Servern erhebliche Auswirkungen auf Geschäftsprozesse und damit auf die gesamte Institution haben. Sehr viele IT-Systeme, wie Clients oder andere Server, sind oft darauf angewiesen, dass die dort zentral gespeicherten Daten verfügbar sind.

Wenn geschäftsrelevante Informationen, egal welcher Art, zerstört oder verfälscht werden, können dadurch Geschäftsprozesse und Fachaufgaben verzögert oder sogar deren Ausführung verhindert werden. Insgesamt kann der Verlust gespeicherter Daten, neben dem Ausfall und den Kosten für die Wiederbeschaffung der Daten, vor allem zu langfristigen Konsequenzen, wie Vertrauenseinbußen bei Kunden und Partnern, juristischen Auswirkungen sowie einem negativen Eindruck in der Öffentlichkeit, führen. In vielen Institutionen existieren Regelungen, dass keine Daten auf den lokalen Clients gespeichert werden dürfen, sondern hierfür zentrale Ablagen auf den Servern genutzt werden müssen. Ein Datenverlust dieser Daten hat dann gravierende Auswirkungen, von den verursachten direkten und indirekten Schäden können Institutionen sogar in ihrer Existenz bedroht sein.

### 2 3 Verhinderung von Diensten

Eine Art eines Angriffs auf die Verfügbarkeit, der "Denial of Service" genannt wird, zielt darauf ab, die Benutzer daran zu hindern, Funktionen oder Geräte zu verwenden, die ihnen normalerweise zur Verfügung stehen. Dieser Angriff steht häufig im Zusammenhang mit verteilten Ressourcen, indem ein Angreifer diese Ressourcen so stark in Anspruch nimmt, dass andere Benutzer an der Arbeit gehindert werden und nicht mehr auf Ressourcen, von denen sie abhängig sind, zugreifen können. In der Regel sind IT-Systeme auch stark voneinander abhängig, von der Verknappung der Ressourcen eines Servers sind schnell weitere Server betroffen. Es können zum Beispiel CPU-Zeit, Speicherplatz oder Bandbreite künstlich verknappt werden, dies kann dazu führen, dass der Dienst oder eine Ressource überhaupt nicht mehr genutzt werden kann.

### 2 4 Bereitstellung unbenötigter Betriebssystemkomponenten und Applikationen

Schon bei der Installation des Server-Betriebssystems besteht die Möglichkeit, alle mitgelieferten Applikationen und Dienste zu installieren. Auch im Betrieb wird oft Software installiert, die kurz getestet, aber danach nicht mehr benötigt wird. Oft ist gar nicht bekannt, dass diese nicht genutzten Anwendungen und Dienste auf den Servern vorhanden sind. Auf diese Weise befinden sich zahlreiche Applikationen und Dienste auf dem Server, die nicht eingesetzt werden und so den Server unnötig belasten.

Solche nicht genutzten Anwendungen und Dienste können Schwachstellen enthalten. Wenn die Anwendungen dann nicht mehr aktualisiert werden, können sie ein Einfallstor für Angreifer sein. Sind die installierten Anwendungen und Dienste unbekannt, ist dem IT-Betrieb nicht bewusst, dass diese ebenfalls aktualisiert werden müssen.

### 2 5 Überlastung von Servern

Wenn Server nicht ausreichend dimensioniert sind, ist irgendwann der Punkt erreicht, an dem sie den Anforderungen der Benutzer nicht mehr gerecht werden. Je nach Art der betroffenen Systeme kann dies eine Vielzahl von negativen Auswirkungen haben, beispielsweise dass die Server oder Dienste vorübergehend nicht verfügbar sind oder dass Datenverluste auftreten. Die Überlastung eines einzelnen Servers kann bei komplexen IT-Landschaften dazu führen, das bei weiteren Servern Probleme oder Ausfälle auftreten können.

Auslöser für die Überlastung von Informationssystemen können sein, dass

* installierte Dienste oder Anwendungen falsch konfiguriert sind und so unnötig Speicher beanspruchen,
* vorhandene Speicherplatzkapazitäten überschritten werden,
* zahlreiche Anfragen zur gleichen Zeit ein System überbeanspruchen und dadurch die Prozessoren überlastet werden,
* zu viel Rechenleistung von den Diensten beansprucht wird oder
* eine große Anzahl Nachrichten zur gleichen Zeit versendet werden.
3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von allgemeinen Servern aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.1.1.A1 Geeignete Aufstellung [Haustechnik]

Server MÜSSEN an Orten betrieben werden, zu denen nur berechtigte Personen Zutritt haben. Server MÜSSEN daher in Rechenzentren, Rechnerräumen oder abschließbaren Serverschränken aufgestellt beziehungsweise eingebaut werden, siehe hierzu die entsprechenden Bausteine. Es MUSS geregelt werden, wer Zutritt zu den Räumen beziehungsweise physischen Zugang auf die Server selbst erhält. Server DÜRFEN NICHT als Arbeitsplatzrechner genutzt werden.

Es MUSS auf eine geeignete räumliche Trennung der Systeme, die gesichert werden sollen, von den sichernden Systemen, etwa Backup-Servern in unterschiedlichen Brandabschnitten, geachtet werden, um die Auswirkungen bei einem physischen Schaden zu begrenzen.

#### SYS.1.1.A2 Benutzerauthentisierung

Um den Server zu nutzen, MÜSSEN sich die Benutzer gegenüber dem IT-System authentisieren. Sollen hierfür die Benutzer und Administratoren Passwörter verwenden, MÜSSEN sichere Passwörter benutzt werden. Hierfür SOLLTE es eine Passwort-Richtlinie geben. Diese Passwörter MÜSSEN komplex genug sein, geheim gehalten und regelmäßig gewechselt werden.

#### SYS.1.1.A3 Restriktive Rechtevergabe

Zugriffsrechte auf Dateien, die auf Servern gespeichert sind, MÜSSEN restriktiv vergeben werden. Jeder Benutzer DARF nur auf die Dateien Zugriffsrechte erhalten, die er für seine Aufgabenerfüllung benötigt. Das Zugriffsrecht selbst wiederum MUSS auf die notwendige Zugriffsart beschränkt sein, so ist es zum Beispiel in den seltensten Fällen notwendig, ein Schreibrecht auf Programmdateien zu vergeben. 

Es SOLLTE regelmäßig überprüft werden, ob die Berechtigungen, insbesondere für Systemverzeichnisse und -dateien, den Vorgaben der Sicherheitsrichtlinie entsprechen. Auf Systemdateien SOLLTEN möglichst nur die Systemadministratoren Zugriff haben. Der Kreis der zugriffsberechtigten Administratoren SOLLTE möglichst klein gehalten werden. Auch System-Verzeichnisse SOLLTEN nur die notwendigen Privilegien für die Benutzer zur Verfügung stellen. 

#### SYS.1.1.A4 Rollentrennung

Es MUSS sichergestellt werden, dass Kennungen mit Administratorrechten nur für Administrationsaufgaben verwendet werden. Für alle Administratoren MÜSSEN zusätzliche Benutzer-Kennungen eingerichtet werden, die nur über die eingeschränkten Rechte verfügen, die die Administratoren zur Aufgabenerfüllung außerhalb der Administration benötigen. Für Arbeiten, die nicht der Administration dienen, MÜSSEN die Administratoren ausschließlich diese Benutzer-Kennungen verwenden. Über die notwendigen Benutzer-Kennungen hinaus SOLLTEN keine weiteren Benutzer auf dem Server angelegt werden.

#### SYS.1.1.A5 Schutz der Administrationsschnittstellen

Abhängig von der genutzten Zugangsart (lokal, remote oder zentrales Systemmanagement) MÜSSEN geeignete Sicherheitsvorkehrungen getroffen werden. Die zur Administration verwendeten Methoden MÜSSEN in der Sicherheitsrichtlinie festgelegt werden. Die Administration MUSS entsprechend der Sicherheitsrichtlinie durchgeführt werden.

Für die Anmeldung von Benutzern und Diensten am System MÜSSEN Authentisierungsverfahren eingesetzt werden, die dem Schutzbedarf der Server angemessen sind. Dies SOLLTE in besonderem Maße für administrative Zugänge berücksichtigt werden. Soweit möglich, SOLLTE dabei auf zentrale, netzbasierte Authentisierungsdienste zurückgegriffen werden.

Die Administration MUSS über sichere Protokolle erfolgen. Es SOLLTE überlegt werden, alternativ ein eigenes Administrationsnetz einzurichten.

#### SYS.1.1.A6 Deaktivierung nicht benötigter Dienste und Kennungen

Alle nicht benötigten Dienste MÜSSEN von Servern deaktiviert oder deinstalliert werden, vor allem Netzdienste. Nicht benötigte Benutzerkennungen MÜSSEN entweder gelöscht oder zumindest so deaktiviert werden, dass unter diesen Kennungen keine Anmeldungen am System möglich sind. Vorhandene Standard-Kennungen MÜSSEN soweit wie möglich geändert oder deaktiviert werden. Voreingestellte Passwörter von Standard-Kennungen MÜSSEN geändert werden. Auf Servern SOLLTE der Speicherplatz für die einzelnen Benutzer, aber auch für Anwendungen, geeignet beschränkt werden.

Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration und Softwareausstattung für die Server gewählt wurden.

#### SYS.1.1.A7 Updates und Patches für Firmware, Betriebssystem und Anwendungen

Administratoren MÜSSEN sich regelmäßig über bekannt gewordene Schwachstellen der Betriebssysteme, eingesetzter Anwendungen und Dienste informieren. Die identifizierten Schwachstellen MÜSSEN so schnell wie möglich behoben werden, damit sie nicht durch Angreifer ausgenutzt werden können. Generell MUSS darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden.

Solange keine entsprechenden Patches zur Verfügung stehen, MÜSSEN abhängig von der Schwere der Schwachstellen und Bedrohungen andere geeignete Maßnahmen zum Schutz des Systems getroffen werden.

#### SYS.1.1.A8 Regelmäßige Datensicherung

Datensicherungen MÜSSEN vor Installationen und umfangreichen Konfigurationsänderungen sowie außerdem in festgelegten Intervallen vorgenommen werden. Diese MÜSSEN es ermöglichen, die auf dem Server gespeicherten Daten wieder herzustellen. In virtuellen Umgebungen SOLLTE geprüft werden, ob die Systemsicherung unter Umständen durch Snapshot-Mechanismen der Virtualisierungsumgebung realisiert werden kann.

#### SYS.1.1.A9 Einsatz von Viren-Schutzprogrammen

In Abhängigkeit des installierten Betriebssystems, des bereitgestellten Dienstes und anderer vorhandener Schutzmechanismen des Servers MUSS geprüft werden, ob Viren-Schutzprogramme eingesetzt werden sollen und können. Konkrete Aussagen, ob Viren-Schutz notwendig ist, sind in der Regel in den betriebssystemspezifschen Bausteinen des IT-Grundschutzes zu finden. Die entsprechenden Signaturen eines Viren-Schutzprogramms MÜSSEN regelmäßig aktualisiert werden. Neben Echtzeit- und On-Demand-Scans MUSS eine eingesetzte Lösung die Möglichkeit bieten, auch komprimierte und verschlüsselte Daten nach Schadprogrammen zu durchsuchen.

#### SYS.1.1.A10 Protokollierung

Es MUSS entschieden werden, welche Informationen durch die Server mindestens protokolliert werden sollen, wie lange die Protokolldaten aufbewahrt werden und wer unter welchen Voraussetzungen die Protokolldaten einsehen darf. Es MÜSSEN datenschutzrechtliche Vorgaben berücksichtigt werden. Generell MÜSSEN alle sicherheitsrelevanten Systemereignisse protokolliert werden. Diese umfassen mindestens:

* Systemstarts und Reboots,
* erfolgreiche und erfolglose Anmeldungen am System (Betriebssystem und Anwendungssoftware),
* fehlgeschlagene Berechtigungsprüfungen,
* blockierte Datenströme (Verstöße gegen ACLs oder Firewallregeln),
* Einrichtung oder Änderungen von Benutzern, Gruppen und Berechtigungen,
* sicherheitsrelevante Fehlermeldungen (z. B. Hardwaredefekte, Überschreitung von Kapazitätsgrenzen),
* Warnmeldungen von Sicherheitssystemen (z. B. Virenschutz).
### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeiner Server. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.1.1.A11 Festlegung einer Sicherheitsrichtlinie für Server

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTEN die Anforderungen an Server konkretisiert werden. Die Richtlinie SOLLTE allen Administratoren und anderen Personen, die an der Beschaffung und dem Betrieb der Server beteiligt sind, bekannt sein und Grundlage für deren Arbeit sein. Die Umsetzung der in der Richtlinie geforderten Inhalte SOLLTE regelmäßig überprüft und die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.

#### SYS.1.1.A12 Planung des Server-Einsatzes

Jedes Serversystem SOLLTE geeignet geplant werden, dabei sind mindestens folgende Punkte zu berücksichtigen:

* Auswahl der Hardwareplattform, des Betriebssystems und der Anwendungssoftware
* Dimensionierung der Hardware (Leistung, Speicher, Bandbreite, …)
* Art und Anzahl der Kommunikationsschnittstellen
* Leistungsaufnahme und Wärmelast, Platzbedarf und Bauform
* Realisierung administrativer Zugänge (siehe SYS.1.1.A3 Schutz der Administrationsschnittstellen)
* Zugriffe von Benutzern
* Realisierung der Protokollierung (siehe SYS.1.1.A7 Protokollierung)
* Realisierung der Systemaktualisierung (siehe SYS.1.1.A5 Updates und Patches für Betriebssystem und Anwendungen)
* Einbindung ins System- und Netzmanagement, die Datensicherung und Schutzsysteme (Virenschutz, IDS u. a.)
Alle Entscheidungen, die in der Planungsphase getroffen wurden, SOLLTEN so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. 

#### SYS.1.1.A13 Beschaffung von Servern

Bevor ein oder mehrere Server beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. 

#### SYS.1.1.A14 Erstellung eines Benutzer- und Administrationskonzepts

Ablauf, Rahmenbedingungen und Anforderungen an administrative Aufgaben, sowie die Aufgabentrennungen zwischen den verschiedenen Rollen der Benutzer des IT-Systems SOLLTEN in einem Benutzer- und Administrationskonzept festgeschrieben werden.

#### SYS.1.1.A15 Unterbrechungsfreie und stabile Stromversorgung [Haustechnik]

Jeder Server SOLLTE an eine unterbrechungsfreie Stromversorgung (USV) angeschlossen werden. Die USV SOLLTE hinsichtlich Leistung und Stützzeit ausreichend dimensioniert sein. Wenn Änderungen an den Verbrauchern durchgeführt wurden, SOLLTE erneut geprüft werden, ob die Stützzeit ausreichend ist. Sowohl für die USV-Geräte als auch die Server SOLLTE ein Überspannungsschutz vorhanden sein. 

Die tatsächliche Kapazität der Batterie und damit die Stützzeit der USV SOLLTE regelmäßig getestet werden. Die USV SOLLTE regelmäßig gewartet werden. Die USV SOLLTE in ein vorhandenes System- und Netzmanagement eingebunden werden.

#### SYS.1.1.A16 Sichere Installation und Grundkonfiguration von Servern

Server SOLLTEN so aufgesetzt werden, dass bei der Installation ausschließlich die benötigten Dienste ausgewählt werden. Installationen auf einem Server SOLLTEN nur von autorisierten Personen (Administratoren oder vertraglich gebundene Dienstleister) nach einem definierten Installationsprozess durchgeführt werden. System- und Anwendungssoftware SOLLTE aus vertrauenswürdigen Installationsquellen bezogen werden. Für sich wiederholende Installationen SOLLTEN geeignete Installations-Templates erstellt und angewendet werden.

Alle Installationsschritte SOLLTEN so dokumentiert werden, dass die Installation durch einen sachkundigen Dritten anhand der Dokumentation nachvollzogen und wiederholt werden kann.

Die Grundeinstellungen von Servern SOLLTEN überprüft und nötigenfalls entsprechend den Vorgaben der Sicherheitsrichtlinie angepasst werden. Erst nachdem die Installation und die Konfiguration abgeschlossen ist, SOLLTE der Server mit dem Internet verbunden werden.

#### SYS.1.1.A17 Einsatzfreigabe

Bevor das Serversystem im produktiven Betrieb eingesetzt und bevor es an ein produktives Netz angeschlossen wird, SOLLTE eine Einsatzfreigabe erfolgen. Diese SOLLTE geeignet dokumentiert werden. Für die Einsatzfreigabe SOLLTEN die Installations- und Konfigurationsdokumentation und die Funktionsfähigkeit des Systems in einem Test geprüft werden. Sie SOLLTE durch eine in der Institution dafür autorisierte Stelle erfolgen.

#### SYS.1.1.A18 Verschlüsselung der Kommunikationsverbindungen

Für alle vom Server angebotenen und genutzten Netzdienste SOLLTE geprüft werden, ob mit vertretbarem Aufwand eine Verschlüsselung der Kommunikationsverbindungen möglich und praktikabel ist. Ist dies mit vertretbarem Aufwand möglich, SOLLTE die Verschlüsselung aktiviert werden. 

#### SYS.1.1.A19 Einrichtung lokaler Paketfilter

Vorhandene lokale Paketfilter SOLLTEN über ein Regelwerk so ausgestaltet werden, dass die eingehende und ausgehende Kommunikation auf die erforderlichen Kommunikationspartner, Kommunikationsprotokolle bzw. Ports und Schnittstellen beschränkt werden. 

#### SYS.1.1.A20 Beschränkung des Zugangs über Netze

Generell SOLLTE das gesamte Netz einer Institution durch ein entsprechendes Sicherheitsgateway gegen unbefugte Zugänge geschützt sein. Server, die Dienste nach außen hin anbieten, SOLLTEN in einer Demilitarisierten Zone (DMZ) aufgestellt werden.

Server SOLLTEN möglichst nicht im selben IP-Subnetz wie die Clients platziert werden. Server SOLLTEN zumindest durch einen Router von den Clients getrennt sein.

#### SYS.1.1.A21 Betriebsdokumentation

Betriebliche Aufgaben, die an einem Server durchgeführt werden, SOLLTEN nachvollziehbar dokumentiert werden (wer?, wann?, was?). Aus der Dokumentation SOLLTEN insbesondere Konfigurationsänderungen nachvollziehbar sein. Sicherheitsrelevante Aufgaben (wer ist z. B. befugt, neue Festplatten einzubauen) SOLLTEN dokumentiert werden. Alles, was automatisch dokumentiert werden kann, SOLLTE auch automatisch dokumentiert werden. Die Dokumentation SOLLTE gegen unbefugten Zugriff und Verlust geschützt werden.

#### SYS.1.1.A22 Einbindung in die Notfallplanung

Der Server SOLLTE im Notfallmanagementprozess berücksichtigt werden. Dazu SOLLTEN die Notfallanforderungen an das System ermittelt und geeignete Notfallmaßnahmen umgesetzt werden, z. B. indem Wiederanlaufpläne erstellt oder Passwörter und kryptographische Schlüssel sicher hinterlegt werden.

#### SYS.1.1.A23 Systemüberwachung

Das Serversystem SOLLTE in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden, das den Systemzustand und die Funktionsfähigkeit des Systems und der darauf betriebenen Dienste laufend überwacht und Fehlerzustände sowie die Überschreitung definierter Grenzwerte an das Betriebspersonal meldet.

#### SYS.1.1.A24 Sicherheitsprüfungen

Serversysteme SOLLTEN regelmäßigen Sicherheitstests unterzogen werden, die die Einhaltung der Sicherheitsvorgaben überprüfen und ggf. vorhandene Schwachstellen identifizieren. Dies SOLLTE in besonderem Maße für Systeme mit externen Schnittstellen gelten. Angesichts mittelbarer Angriffe über infizierte Systeme im eigenen Netz SOLLTEN jedoch auch interne Serversysteme in festgelegten Zyklen entsprechend überprüft werden. Es SOLLTE geprüft werden, ob die Sicherheitsprüfungen dabei auch automatisiert, z. B. mittels geeigneter Skripte, realisiert werden können.

#### SYS.1.1.A25 Geregelte Außerbetriebnahme eines Servers

Bei der Außerbetriebnahme eines Servers SOLLTE sichergestellt werden, dass keine wichtigen Daten, die eventuell auf den verbauten Datenträgern gespeichert sind, verloren gehen, und dass keine sensitiven Daten zurück bleiben. Es SOLLTE einen Überblick darüber geben, welche Daten wo auf dem Server gespeichert sind. Es SOLLTE außerdem sichergestellt sein, dass vom Server angebotene Dienste durch einen anderen Server übernommen wurden, wenn dies erforderlich ist.

Es SOLLTE eine Checkliste erstellt werden, die bei der Außerbetriebnahme eines Servers abgearbeitet werden kann. Diese Checkliste SOLLTE mindestens Aspekte zur Datensicherung, Migration von Diensten und dem anschließenden sicheren Löschen aller Daten umfassen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.1.1.A26 Mehr-Faktor-Authentisierung(C)

Bei höherem Schutzbedarf SOLLTE eine sichere Zwei- oder Mehr-Faktor-Authentisierung für den Zugang zum Server eingerichtet werden, z. B. mit kryptographischen Zertifikaten, Chipkarten oder Token. Vordringlich SOLLTEN alle administrativen Zugänge zum Server mit Mehr-Faktor-Authentisierung abgesichert werden. 

#### SYS.1.1.A27 Hostbasierte Angriffserkennung(IA)

Mit dem Einsatz von hostbasierten Angriffserkennungssystemen (Host-based Intrusion Detection Systems, IDS bzw. Intrusion Prevention Systems, IPS ) SOLLTE das Systemverhalten auf Anomalien und Missbrauch hin überwacht werden. Die eingesetzten IDS/IPS-Mechanismen SOLLTEN geeignet ausgewählt, konfiguriert und ausführlich getestet werden. Im Falle einer Angriffserkennung SOLLTE das Betriebspersonal geeignet alarmiert werden.

Über Betriebssystem-Mechanismen oder geeignete Zusatzprodukte SOLLTEN Veränderungen an Systemdateien und Konfigurationseinstellungen überprüft, eingeschränkt und gemeldet werden.

#### SYS.1.1.A28 Redundanz(A)

Serversysteme mit hohen Verfügbarkeitsanforderungen SOLLTEN gegen Ausfälle geeignet geschützt sein. Hierzu SOLLTEN mindestens geeignete Redundanzen verfügbar sein und/oder Wartungsverträge mit den Lieferanten abgeschlossen werden. Es SOLLTE geprüft werden, ob bei sehr hohen Anforderungen Hochverfügbarkeitsarchitekturen mit automatischem Failover, gegebenenfalls über verschiedene Standorte hinweg, erforderlich sind. 

#### SYS.1.1.A29 Einrichtung einer Testumgebung(CIA)

Um Veränderungen am System oder der Konfiguration testen zu können, ohne den Produktivbetrieb zu gefährden, SOLLTEN entsprechende Testsysteme vorgehalten oder bei Bedarf bereitgestellt werden (z. B. als virtuelle Images). Die Testsysteme SOLLTEN den Produktivsystemen weitestmöglich entsprechen (Softwareversionen, Konfiguration). Für Anwendungssysteme SOLLTEN geeignete Testdaten generiert werden, die keine vertraulichen oder personenbezogenen Inhalte der produktiven Daten umfassen.

#### SYS.1.1.A30 Ein Dienst pro Server(CIA)

Abhängig von der Bedrohungslage und dem Schutzbedarf der Dienste SOLLTE auf einem Server nur jeweils ein Dienst betrieben werden.

#### SYS.1.1.A31 Application Whitelisting(CI)

Es SOLLTE bei erhöhtem Schutzbedarf über Application Whitelisting sichergestellt werden, dass nur erlaubte Programme ausgeführt werden. Zum einen SOLLTEN vollständige Pfade bzw. Verzeichnisse festgelegt werden, aus denen dies möglich sein darf. Zum anderen SOLLTE alternativ einzelnen Anwendungen explizit die Ausführung gestattet werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeiner Server" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISi-Server] Absicherung eines Servers (ISi-Server), BSI, 09.2013

  

 Bundesamt für Sicherheit in der Informatiostechnik, 02.2017  
 <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeiner Server" von Bedeutung.

* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
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

