1 Beschreibung
--------------

### 1.1 Einleitung

Als "Allgemeiner Client" wird ein IT-System mit einem beliebigen Betriebssystem bezeichnet, das die Trennung von Benutzern zulässt. Es sollten mindestens eine Administrator- und eine Benutzer-Umgebung eingerichtet werden können. Typischerweise ist ein solches IT-System vernetzt und wird als Client in einem Client-Server-Netz genutzt. Das IT-System kann auf einer beliebigen Plattform betrieben werden. Dabei kann es sich beispielsweise um einen PC mit oder ohne Festplatte, um ein mobiles oder stationäres Gerät, aber auch um eine Linux-Workstation oder einen Apple Mac handeln. Das IT-System verfügt in der Regel über Laufwerke für auswechselbare Datenträger, weitere Schnittstellen für den Datenaustausch sowie andere Peripheriegeräte.

### 1.2 Zielsetzung

Zielsetzung dieses Bausteins ist der Schutz von Informationen, die auf Clients, unabhängig des auf ihnen betriebenen Betriebssystems, erstellt, gelesen, bearbeitet, gespeichert oder versendet werden. 

### 1.3 Abgrenzung

In der Regel werden Client-Systeme unter einem Betriebssystem betrieben, das jeweils eigene Sicherheitsmaßnahmen erfordert. Für verbreitete Client-Betriebssysteme sind eigene Bausteine vorhanden, die diesen Baustein ergänzen. Der Baustein "Allgemeiner Client" bildet die Grundlage für die konkreten Bausteine, auf der diese aufbauen. Sofern für ein betrachtetes IT-System ein konkreter Baustein existiert, ist dieser zusätzlich zum Baustein Allgemeiner Client anzuwenden. Falls für eingesetzte Client-Systeme kein spezifischer Baustein existiert, müssen die Anforderungen dieses Bausteins geeignet angepasst werden. Sicherheitsempfehlungen für nicht frei konfigurierbare mobile Endgeräte, wie Smartphones oder Tablets, sind generell in der Schicht SYS.3 Mobile Devices zu finden.

Falls der Client weitere Schnittstellen zum Datenaustausch hat, wie z. B. USB, Bluetooth, LAN oder WLAN, müssen diese entsprechend den Sicherheitsvorgaben der Institution abgesichert werden, wie dies in den entsprechenden Bausteinen beschrieben ist. Hierzu sind Informationen in SYS.3.4 Mobile Datenträger, NET.2.3 Nahfunk und NET.2.2 WLAN-Nutzung zu finden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Allgemeiner Client von besonderer Bedeutung:

### 2 1 Schadprogramme

Schadprogramme werden mit dem Ziel entwickelt, unerwünschte und schädliche Funktionen auf Rechnern auszuführen. Sie werden meist heimlich aktiv, ohne dass die Benutzer dies wissen oder hierzu einwilligen. Je nach Ausprägung bieten sie einem Angreifer umfangreiche Kommunikations- und Steuerungsmöglichkeiten mit vielen Funktionen. Unter anderem könnten sie gezielt Passwörter ausforschen, IT-Systeme fernsteuern, Schutzsoftware deaktivieren oder Daten ausspionieren.

Clients sind besonders anfällig für Schadsoftware: Sie werden direkt von den Benutzern bedient und sind somit oft das Einfallstor für Schadsoftware. Besuchen die Benutzer infizierte Webseiten, öffnen E-Mails mit kompromittierendem Inhalt von privaten E-Mail-Konten oder kopieren Schadsoftware über lokale Datenträger auf den Client, verbreitet sich so die Schadsoftware über die Clients in das Netz der Institution. Zentrale Schutzmechanismen, wie z.B. ein Virenschutz auf dem Datei- oder E-Mail-Server, können so oft umgangen werden.

### 2 2 Unstrukturierte lokale Datenhaltung

Trotz regelmäßiger gegensätzlicher Empfehlung speichern viele Anwender auch wichtige Daten ausschließlich lokal ab. Beispielsweise werden Daten häufig statt auf einem zentralen Dateiserver in lokalen Benutzerverzeichnissen abgelegt. Auch E-Mails werden häufig nur lokal archiviert. Dieses Vorgehen kann zu folgenden Problemen führen:

* Datenverlust bei Hardwaredefekten und
* kein Zugriff auf relevante Daten im Vertretungsfall.
Aber auch wenn grundsätzliche Vorgaben zur zentralen Speicherung eingehalten werden, werden häufig zusätzlich lokale Kopien der zentral gespeicherten Daten angelegt. Dies kann zu folgenden Problemen führen:

* Verschwendung von lokalen Speicherplatz,
* vorschnelle oder nicht erfolgte Löschung von Daten und
* inkonsistente Versionsstände 
### 2 3 Datenverlust

Auf Clients werden typischerweise verteilt über die gesamte Institution viele Daten gespeichert, deren Verlust erhebliche Auswirkungen auf Geschäftsprozesse und damit auf die gesamte Institution haben kann. Werden geschäftsrelevante Daten zerstört oder verfälscht, können dadurch Geschäftsprozesse und Fachaufgaben verzögert oder sogar deren Ausführung verhindert werden. Insgesamt kann der Verlust gespeicherter Daten, neben einem Arbeitsausfall und den Kosten für eine Wiederbeschaffung, auch zu langfristigen Konsequenzen, wie beispielsweise Vertrauenseinbußen bei Kunden und Partnern, sowie einem negativen Eindruck in der Öffentlichkeit führen. Von den durch Datenverluste verursachten direkten und indirekten Schäden können Institutionen im Extremfall in ihrer Existenz bedroht sein.

### 2 4 Hardware-Defekte durch Fehlbedienung

Anders als bei zentralen IT-Systemen wie Servern arbeiten Client-Benutzer direkt am Endgerät. Durch den physischen Zugriff können sie den Client gewollt oder ungewollt beschädigen. Beispielsweise können sie gegen auf dem Boden stehende IT-Systeme treten, Monitore umwerfen, über Kabel stolpern oder Getränke in Tastaturen gießen. Oft ist es nicht ausreichend, Hardware erst bei einem Defekt zu ersetzen. Bei einem Festplattendefekt zum Beispiel können gespeicherte Daten meist nicht wiederhergestellt werden. Außerdem kann das IT-System bis zum Abschluss der Reparatur nicht eingesetzt werden. Bei einem Ausfall eines mobilen Gerätes unterwegs kann die Arbeit erst nach der Rückkehr fortgesetzt werden.

### 2 5 Software-Schwachstellen oder -Fehler

Für jede Art von Software gilt: Je komplexer sie ist, desto häufiger können Programmier- oder Designfehler auftreten. Unter Software-Schwachstellen werden Programmfehler verstanden, die den Anwendern oft (noch) nicht bekannt sind und die ein Sicherheitsrisiko für das -System darstellen. Beinahe täglich werden neue Sicherheitslücken in lange genutzter, aber auch in neuer Software gefunden.

Auf Clients werden in der Regel eine Vielzahl verschiedener Applikationen installiert, hierdurch erhöht sich die Menge an Schwachstellen, von denen das System betroffen sein kann. Hinzu kommt, dass eine größere Anzahl von (mobilen) Clients viel schwerer mit reparierenden Patches aktualisiert werden kann, als beispielsweise wenige Server.

Werden Softwarefehler nicht erkannt oder nicht umgehend behoben, kann das zu schwerwiegenden Folgen führen. Eine Software-Schwachstelle in einer viel genutzten Standardsoftware kann schnell dazu führen, dass weltweit Sicherheitsprobleme für alle Arten von Institutionen entstehen.

### 2 6 Unberechtigte IT-Nutzung

Die Identifikation und Authentisierung von Benutzern soll verhindern, dass ein Client unberechtigt verwendet wird. Aber auch IT-Systeme, bei denen sich Benutzer über Benutzer-IDs und Passwörter identifizieren und authentisieren müssen, können unberechtigt genutzt werden, wenn es einem Angreifer gelingt, die Zugangsdaten auszuspähen oder zu erraten. Wird keine Bildschirmsperre aktiviert, kann der Client auch bei kurzzeitiger Abwesenheit unberechtigt genutzt werden.

### 2 7 Bereitstellung nicht benötigter Betriebssystemkomponenten und Applikationen

Bei der Installation eines Betriebssystems besteht in der Regel die Möglichkeit, optionale Software zu installieren. Auch im laufenden Betrieb wird regelmäßig Software installiert und getestet. Mit jeder weiteren Anwendung steigen nicht nur Rechen- und Speicherlast eines Clients stetig, sondern auch die Wahrscheinlichkeit, Schwachstellen darin zu finden. Nicht benötigte Software unterliegt außerdem häufig keinem regelmäßigen Patchmanagement, so dass auch bekannte Sicherheitslücken nicht zeitnah geschlossen werden. Dadurch können Angreifer schon lange bekannte Schwachstellen nutzen.

### 2 8 Abhören von Räumen mittels Mikrofon und Kamera

Viele Clients verfügen über ein Mikrofon und eine Kamera. Diese können von Jedem verwendet werden, der über entsprechende Zugriffsrechte verfügt, bei vernetzten Systemen auch von Externen. Werden diese Rechte nicht sorgfältig vergeben, können Unbefugte Mikrofon oder Kamera dazu missbrauchen, um über das Internet Räume abzuhören oder unbemerkt Besprechungen aufzuzeichnen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Clients aufgeführt. Grundsätzlich ist der *IT-Betrieb* für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt. 

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.2.1.A1 Benutzerauthentisierung

Um den Client zu nutzen, MÜSSEN sich die Benutzer gegenüber dem IT-System authentisieren. Sollen die Benutzer hierfür Passwörter verwenden, MÜSSEN sichere Passwörter benutzt werden. Die Passwörter MÜSSEN der Passwort-Richtlinie der Institution entsprechen, siehe ORP.4 Identitäts- und Berechtigungsmanagement.

#### SYS.2.1.A2 Rollentrennung

Der Client MUSS so eingerichtet werden, dass normale Tätigkeiten nicht mit Administrationsrechten erfolgen. Nur Administratoren DÜRFEN Administrationsrechte erhalten. Es DÜRFEN nur Administratoren die Systemkonfiguration ändern, Anwendungen installieren bzw. entfernen oder Systemdateien modifizieren bzw. löschen können. Benutzer DÜRFEN ausschließlich lesenden Zugriff auf Systemdateien haben. 

Ablauf, Rahmenbedingungen und Anforderungen an administrative Aufgaben sowie die Aufgabentrennungen zwischen den verschiedenen Rollen der Benutzer des IT-Systems SOLLTEN in einem Benutzer- und Administrationskonzept festgeschrieben werden.

#### SYS.2.1.A3 Aktivieren von Autoupdate-Mechanismen

Automatische Update-Mechanismen (Autoupdate) MÜSSEN aktiviert werden, sofern nicht andere Mechanismen, wie regelmäßige manuelle Wartung oder ein zentrales Softwareverteilungssystem für Updates eingesetzt werden. Wenn für Autoupdate-Mechanismen ein Zeitintervall vorgegeben werden kann, SOLLTE mindestens täglich automatisch nach Updates gesucht und diese installiert werden.

#### SYS.2.1.A4 Regelmäßige Datensicherung

Zur Vermeidung von Datenverlusten MÜSSEN regelmäßige Datensicherungen erstellt werden. In den meisten Rechnersystemen können diese weitgehend automatisiert erfolgen. Es MÜSSEN Regelungen getroffen werden, welche lokal abgespeicherten Daten von wem wann gesichert werden. Es MÜSSEN mindestens die Daten regelmäßig gesichert werden, die nicht aus anderen Informationen abgeleitet werden können. Auch Clients MÜSSEN in das Datensicherungskonzept der Institution einbezogen werden. Bei vertraulichen und ausgelagerten Backups SOLLTEN die gesicherten Daten verschlüsselt gespeichert werden. Für eingesetzte Software SOLLTE separat entschieden werden, ob sie von der regelmäßigen Datensicherung erfasst werden muss. Es MUSS regelmäßig getestet werden, ob die Datensicherung auch wie gewünscht funktioniert, vor allem, ob gesicherte Daten problemlos zurückgespielt werden können. Die Benutzer SOLLTEN über die Regelungen, von wem und wie Datensicherungen erstellt werden, informiert werden. 

#### SYS.2.1.A5 Bildschirmsperre [Benutzer]

Eine Bildschirmsperre MUSS verwendet werden, damit keine Unbefugten auf den aktivierten Clients zugreifen können. Sie SOLLTE sich sowohl manuell vom Benutzer aktivieren lassen, als auch nach einem vorgegebenen Inaktivitäts-Zeitraum automatisch gestartet werden. Es MUSS sichergestellt sein, dass die Bildschirmsperre erst nach einer erfolgreichen Benutzerauthentikation deaktiviert werden kann. 

#### SYS.2.1.A6 Einsatz von Viren-Schutzprogrammen

In Abhängigkeit des installierten Betriebssystems und anderer vorhandener Schutzmechanismen des Clients MUSS geprüft werden, ob Viren-Schutzprogramme eingesetzt werden sollen. Konkrete Aussagen, ob Viren-Schutz notwendig ist, sind in der Regel in den Betriebssystem-Bausteinen des IT-Grundschutzes zu finden. Die entsprechenden Signaturen eines Viren-Schutzprogrammes MÜSSEN regelmäßig aktualisiert werden. Neben Echtzeit- und On-Demand-Scans MUSS eine eingesetzte Lösung die Möglichkeit bieten, auch komprimierte und verschlüsselte Daten nach Schadprogrammen zu durchsuchen.

Viren-Schutzprogramme auf den Clients MÜSSEN so konfiguriert sein, dass die Benutzer weder sicherheitsrelevante Änderungen an den Einstellungen vornehmen können noch sie deaktivieren können.

#### SYS.2.1.A7 Protokollierung

Es MUSS entschieden werden, welche Informationen auf Clients mindestens protokolliert werden sollen, wie lange die Protokolldaten aufbewahrt werden und wer unter welchen Voraussetzungen die Protokolldaten einsehen darf. Generell MÜSSEN alle sicherheitsrelevanten Systemereignisse protokolliert werden. 

#### SYS.2.1.A8 Absicherung des Boot-Vorgangs

Der Startvorgang des IT-Systems ("Booten") MUSS gegen Manipulation abgesichert werden. Es MUSS festgelegt werden, von welchen Medien gebootet werden darf. Es SOLLTE entschieden werden, ob und wie der Bootvorgang kryptographisch geschützt werden soll. Es MUSS sichergestellt werden, dass nur Administratoren die Clients von einem anderen als dem voreingestellten Laufwerken oder externen Speichermedien booten können. Nur Administratoren DÜRFEN von eingebauten optischen oder externen Speichermedien booten können. Die Konfigurationseinstellungen des Boot-Vorgangs Firmware MÜSSEN nur durch Benutzer mit administrativen Rechten verändert werden können.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeiner Client. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.2.1.A9 Festlegung einer Sicherheitsrichtlinie für Clients

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTEN die Anforderungen an allgemeine Clients konkretisiert werden. Die Richtlinie SOLLTE allen Benutzern sowie allen Personen, die an der Beschaffung und dem Betrieb der Clients beteiligt sind, bekannt und Grundlage für deren Arbeit sein. Die Umsetzung der in der Richtlinie geforderten Inhalte SOLLTE regelmäßig überprüft und die Ergebnisse sinnvoll dokumentiert werden.

#### SYS.2.1.A10 Planung des Einsatzes von Clients

Zum sicheren Betrieb von Clients SOLLTE im Vorfeld geplant werden, wo und wie die Clients eingesetzt werden sollen. Die Planung SOLLTE dabei nicht nur Aspekte betreffen, die klassischerweise mit dem Begriff Sicherheit verknüpft werden, sondern auch normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen. Neben Client-Typ-spezifischen Anforderungsprofilen SOLLTEN Vorgaben zur Authentisierung und Benutzerverwaltung definiert werden. Alle Entscheidungen, die in der Planungsphase getroffen wurden, SOLLTEN so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. 

#### SYS.2.1.A11 Beschaffung von Clients

Bevor Clients beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Der jeweilige Hersteller SOLLTE für den gesamten geplanten Nutzungszeitraum Patches für Schwachstellen zeitnah zur Verfügung stellen können. Die zu beschaffenden Systeme SOLLTEN über eine Firmware-Konfigurationsoberfläche für UEFI SecureBoot und für das TPM (sofern vorhanden) verfügen, die eine Kontrolle durch den Eigentümer (Institution) gewährt und so den selbstverwalteten Betrieb von SecureBoot und des TPM ermöglicht.

#### SYS.2.1.A12 Kompatibilitätsprüfung von Software

Vor einer beabsichtigten Beschaffung von Software SOLLTE deren Kompatibilität zum eingesetzten Betriebssystem in der vorliegenden Konfiguration geprüft und die Kompatibilitätsprüfung in das Freigabeverfahren der Software aufgenommen werden. Ist vom Hersteller der Software oder aus anderen Fachkreisen keine verbindliche Information zur Kompatibilität vorhanden, so SOLLTE die Kompatibilität in einer Testumgebung geprüft werden. Vor einer beabsichtigten Hardwareänderung oder bei einer Betriebssystemmigration SOLLTE auch die Treibersoftware für alle betreffenden Komponenten auf Kompatibilität zum Betriebssystem gewährleistet werden.

#### SYS.2.1.A13 Zugriff auf Ausführungsumgebungen mit unbeobachtbarer Codeausführung

Der Zugriff auf Ausführungsumgebungen mit unbeobachtbarer Codeausführung (z.B. durch das Betriebssystem speziell abgesicherte Speicherbereiche, Firmwarebereiche, etc.) SOLLTE nur durch Benutzer mit administrativen Berechtigungen möglich sein.

#### SYS.2.1.A14 Updates und Patches für Firmware, Betriebssystem und Anwendungen

Administratoren SOLLTEN sich regelmäßig über bekannt gewordene Schwachstellen informieren. Die identifizierten Schwachstellen SOLLTEN so schnell wie möglich behoben werden. Generell SOLLTE darauf achtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden. Wenn notwendig, SOLLTEN die betreffenden Anwendungen beziehungsweise das Betriebssystem nach dem Update neu gestartet werden. 

Solange keine entsprechenden Patches zur Verfügung stehen, SOLLTEN abhängig von der Schwere der Schwachstellen andere geeignete Maßnahmen zum Schutz des IT-Systems getroffen werden.

#### SYS.2.1.A15 Sichere Installation und Konfiguration von Clients

Es SOLLTE festgelegt werden, welche Komponenten des Betriebssystems, Fachanwendungen und weitere Tools installiert werden sollen.** **Die Installation und Konfiguration der IT-Systeme SOLLTE nur von autorisierten Personen (Administratoren oder vertraglich gebundene Dienstleister) nach einem definierten Prozess durchgeführt werden. Alle Installations- und Konfigurationsschritte SOLLTEN so dokumentiert werden, dass die Installation und Konfiguration durch einen sachkundigen Dritten anhand der Dokumentation nachvollzogen und wiederholt werden kann (siehe auch SYS.2.1.A36 Betriebsdokumentation).

Die Grundeinstellungen von Clients SOLLTEN überprüft und nötigenfalls entsprechend den Vorgaben der Sicherheitsrichtlinie angepasst werden. Erst nachdem die Installation und die Konfiguration abgeschlossen ist, SOLLTE der Client mit dem Internet verbunden werden.

#### SYS.2.1.A16 Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen

Nach der Installation SOLLTE überprüft werden, welche Komponenten der Firmware, des Betriebssystems, Anwendungen und weitere Tools auf den Clients installiert und aktiviert sind. Nicht benötigte Module, Programme, Dienste, Benutzerkennungen und Schnittstellen SOLLTEN deaktiviert oder ganz deinstalliert werden. Außerdem SOLLTEN nicht benötigte Laufzeitumgebungen, Interpretersprachen und Compiler deinstalliert werden. Entsprechende, nicht benötigte, jedoch fest mit dem IT-System verbundene Komponenten SOLLTEN deaktiviert werden. Auch in der Firmware vorhandene, nicht benötigte Komponenten (z.B. Diebstahlschutz, Fernwartung) SOLLTEN abgeschaltet werden. Es SOLLTE verhindert werden, dass diese Komponenten wieder reaktiviert werden können. Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration und Softwareausstattung für die IT-Systeme gewählt wurden.

#### SYS.2.1.A17 Einsatzfreigabe

Bevor der Client im produktiven Betrieb eingesetzt und bevor es an ein produktives Netz angeschlossen wird, SOLLTE eine Einsatzfreigabe erfolgen. Diese SOLLTE dokumentiert werden. Für die Einsatzfreigabe SOLLTE die Installations- und Konfigurationsdokumentation und die Funktionsfähigkeit der IT-Systeme in einem Test geprüft werden. Sie SOLLTE durch eine in der Institution dafür autorisierte Stelle erfolgen.

#### SYS.2.1.A18 Nutzung von TLS [Benutzer]

Kommunikationsverbindungen SOLLTEN durch Verschlüsselung geschützt werden, soweit möglich. Benutzer SOLLTEN darauf achten, dass bei Web-Seiten SSL/TLS verwendet wird. 

Der IT-Betrieb SOLLTE dafür sorgen, dass die eingesetzten Client-Produkte eine sichere Version von TLS unterstützen. Die Clients SOLLTEN kryptographische Algorithmen und Schlüssellängen verwenden, die dem Stand der Technik und den Sicherheitsanforderungen der Institution entsprechen. 

Neue Zertifikate SOLLTEN erst nach Überprüfung des "Fingerprints" aktiviert werden. Die Validierung von Zertifikaten SOLLTE in Anwendungsprogrammen wie Browsern und E-Mail-Clients aktiviert werden. Session Renegotiation und TLS-Kompression SOLLTEN deaktiviert werden.

#### SYS.2.1.A19 Restriktive Rechtevergabe

Der verfügbare Funktionsumfang des IT-Systems SOLLTE für einzelne Benutzer oder Benutzergruppen eingeschränkt werden, so dass sie genau die Rechte besitzen und auf die Funktionen zugreifen können, die sie für ihre Aufgabenwahrnehmung benötigen. Zugriffsberechtigungen SOLLTEN hierfür möglichst restriktiv vergeben werden. Es SOLLTE regelmäßig überprüft werden, ob die Berechtigungen, insbesondere für Systemverzeichnisse und -dateien, den Vorgaben der Sicherheitsrichtlinie entsprechen. Auf Systemdateien SOLLTEN möglichst nur die Systemadministratoren Zugriff haben. Der Kreis der zugriffsberechtigten Administratoren SOLLTE möglichst klein gehalten werden. Auch System-Verzeichnisse SOLLTEN nur die notwendigen Privilegien für die Benutzer zur Verfügung stellen. 

#### SYS.2.1.A20 Schutz der Administrationsschnittstellen

Abhängig davon, ob Clients lokal, über das Netz oder über zentrale netzbasierte Tools administriert werden, SOLLTEN geeignete Sicherheitsvorkehrungen getroffen werden. Die zur Administration verwendeten Methoden SOLLTEN in der Sicherheitsrichtlinie festgelegt und die Administration SOLLTE entsprechend der Sicherheitsrichtlinie durchgeführt werden. Die Administration über das Netz SOLLTE über sichere Protokolle erfolgen.

#### SYS.2.1.A21 Verhinderung der unautorisierten Nutzung von Rechnermikrofonen und Kameras

Der Zugriff auf Mikrofon und Kamera eines Clients SOLLTE nur durch den Benutzer selber möglich sein, solange er lokal am IT-System arbeitet. Wenn ein vorhandenes Mikrofon oder eine Kamera nicht genutzt und deren Missbrauch verhindert werden soll, SOLLTEN diese, wenn möglich, ausgeschaltet, abgedeckt (nur Kamera), deaktiviert oder physikalisch vom Gerät getrennt werden. Es SOLLTE geregelt werden, wie Kameras und Mikrofone in Clients genutzt und wie die Rechte vergeben werden.

#### SYS.2.1.A22 Abmelden nach Aufgabenerfüllung [Benutzer]

Es SOLLTEN alle Benutzer verpflichtet werden, sich nach Aufgabenerfüllung vom IT-System bzw. von der IT-Anwendung abzumelden, vor allem bei Nutzung eines Systems durch mehrere Benutzer. Ist für einen Benutzer absehbar, dass nur eine kurze Unterbrechung der Arbeit erforderlich ist, SOLLTE er die Bildschirmsperre aktivieren statt sich abzumelden. Wenn technisch möglich, SOLLTE die Bildschirmsperre nach längerer Inaktivität automatisch aktiviert bzw. der Benutzer automatisch abgemeldet werden.

#### SYS.2.1.A23 Nutzung von Client-Server-Diensten

Wenn möglich, SOLLTEN zum Informationsaustausch dedizierte Serverdienste genutzt und direkte Verbindungen zwischen Clients vermieden werden. Falls dies nicht möglich ist, SOLLTE festgelegt werden, welche Client-zu-Client-Dienste (früher oft als "Peer-to-Peer" bezeichnet) genutzt und welche Informationen darüber ausgetauscht werden dürfen. Wenn erforderlich, SOLLTEN die Benutzer für die Nutzung solcher Dienste geschult werden. Direkte Verbindungen zwischen Clients SOLLTEN sich nur auf das LAN beschränken. Auto-Discovery-Protokolle SOLLTEN auf das notwendige Maß beschränkt werden.

#### SYS.2.1.A24 Umgang mit Wechseldatenträgern im laufenden System

Es SOLLTE verhindert werden, dass auf Clients von Laufwerken oder über Schnittstellen unkontrolliert Software installiert oder unberechtigt Daten kopiert werden können. Es SOLLTE generell verhindert werden, dass von den Clients auf Daten aus nicht vertrauenswürdigen Quellen zugegriffen wird. Vertiefende Informationen zu Wechseldatenträgern sind im Baustein SYS.3.4 Mobile Datenträger zu finden.

#### SYS.2.1.A25 Richtlinie zur sicheren IT-Nutzung [Benutzer]

Es SOLLTE eine Richtlinie erstellt werden, in der für alle Mitarbeiter transparent beschrieben wird, welche Rahmenbedingungen bei der IT-Nutzung eingehalten werden müssen und welche Sicherheitsmaßnahmen zu ergreifen sind. Die Richtlinie SOLLTE folgende Punkte abdecken:

* Sicherheitsziele der Institution
* Wichtige Begriffe
* Aufgaben und Rollen mit Bezug zur Informationssicherheit
* Ansprechpartner zu Fragen der Informationssicherheit
* Von den Mitarbeitern umzusetzende und einzuhaltende Sicherheitsmaßnahmen
Die Richtlinie SOLLTE allen Benutzern zur Kenntnis gegeben werden. Jeder neue Benutzer SOLLTE die Kenntnisnahme der Richtlinie bestätigen, bevor er die Informationstechnik nutzen darf. Nach größeren Änderungen an der Richtlinie oder nach spätestens zwei Jahren SOLLTE eine erneute Bestätigung erforderlich. 

#### SYS.2.1.A26 Schutz von Anwendungen

Um die Ausnutzung von Schwachstellen in Anwendungen zu erschweren, SOLLTE ASLR und DEP/NX im Kernel aktiviert und von den Anwendungen genutzt werden. Sicherheitsfunktionen des Kernels und der Standardbibliotheken wie z. B. Heap- und Stackschutz SOLLTEN NICHT deaktiviert werden.

#### SYS.2.1.A27 Geregelte Außerbetriebnahme eines Clients

Bei der Außerbetriebnahme eines Clients SOLLTE sichergestellt werden, dass keine wichtigen Daten, die eventuell auf den verbauten Datenträgern gespeichert sind, verloren gehen, und dass keine sensitiven Daten zurück bleiben. Es SOLLTE einen Überblick darüber geben, welche Daten wo auf den IT-Systemen gespeichert sind. Es SOLLTE eine Checkliste erstellt werden, die bei der Außerbetriebnahme eines IT-Systems abgearbeitet werden kann. Diese Checkliste SOLLTE mindestens Aspekte zur Datensicherung weiterhin benötigter Daten und dem anschließenden sicheren Löschen aller Daten umfassen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.2.1.A28 Verschlüsselung der Clients(C)

Wenn vertrauliche Informationen auf den Clients gespeichert werden, SOLLTEN die schutzbedürftigen Dateien, ausgewählte Dateisystembereiche oder besser die gesamte Festplatte verschlüsselt werden. Hierfür SOLLTE ein eigenes Konzept erstellt und die Details der Konfiguration besonders sorgfältig dokumentiert werden, da im Fall von Problemen die Daten auf den verschlüsselten Dateisystemen sonst vollständig verloren sein können. In diesem Zusammenhang SOLLTEN folgende Inhalte geregelt werden: Authentifizierung (z. B. Passwort, PIN, Token), Ablage der Wiederherstellungsinformationen, zu verschlüsselnde Laufwerke, Schreibrechte auf unverschlüsselte Datenträger und wie sichergestellt wird, dass die Wiederherstellungsinformationen nur berechtigten Personen zugänglich sind. Auch verschlüsselte Dateien, Partitionen oder Datenträger SOLLTEN regelmäßig gesichert werden. Das verwendete Schlüsselmaterial DARF NICHT im Klartext auf den Clients gespeichert sein.

Benutzer SOLLTEN darüber aufgeklärt werden, wie sie sich bei Verlust eines Authentisierungsmittels zu verhalten haben.

#### SYS.2.1.A29 Systemüberwachung(A)

Die Clients SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden, das den Systemzustand und die Funktionsfähigkeit der Clients laufend überwacht und Fehlerzustände sowie die Überschreitung definierter Grenzwerte an das Betriebspersonal meldet.

#### SYS.2.1.A30 Einrichten einer Referenzinstallation für Clients(CIA)

Für Clients SOLLTE eine Referenzinstallation erstellt werden, in der die Grundkonfiguration und alle Konfigurationsänderungen, Updates und Patches vor dem Einspielen auf den Clients bei den Anwendern vorab getestet werden können. Darüber hinaus SOLLTE eine solche Referenzinstallation auch dazu genutzt werden, die Clients vereinfacht zu installieren und wieder aufzusetzen, indem eine entsprechend vorkonfigurierte Installation auf geeignete Art und Weise auf die zu installierenden Clients überspielt wird ("klonen"). Für verschiedene typische und häufiger wiederkehrende Testfälle SOLLTEN Checklisten erstellt werden, die beim Testen abgearbeitet werden können. Zusätzlich SOLLTEN alle Tests so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können.

#### SYS.2.1.A31 Einrichtung lokaler Paketfilter(CIA)

Auf jedem Rechner SOLLTEN, zusätzlich zu den eingesetzten zentralen Sicherheitsgateways, lokale Paketfilter eingesetzt werden. Als Strategie zur Paketfilter-Implementierung SOLLTE eine Whitelist-Strategie gewählt werden.

#### SYS.2.1.A32 Einsatz zusätzlicher Maßnahmen zum Schutz vor Exploits(CIA)

Auf dem IT-System SOLLTEN zusätzliche Maßnahmen zum expliziten Schutz vor Exploits (Schutz: Erschweren der erfolgreichen Ausführung) getroffen werden. Wenn notwendige Schutzmaßnahmen nicht mit Bordmitteln erfüllt werden können, SOLLTEN zusätzliche geeignete Sicherheitsprodukte eingesetzt werden. Sollte es nicht möglich sein, entsprechende Maßnahmen mit Bordmitteln oder einem geeigneten Sicherheitsprodukt umzusetzen, SOLLTEN andere geeignete (in der Regel organisatorische) Sicherheitsmaßnahmen ergriffen werden.

#### SYS.2.1.A33 Application Whitelisting(CIA)

Es SOLLTE über Application Whitelisting sichergestellt werden, dass nur erlaubte Programme und Skripte ausgeführt werden. Die Regeln SOLLTEN so eng wie möglich gefasst werden. Falls Pfade und Hashes nicht explizit angegeben werden können, SOLLTEN alternativ auch Zertifikats-basierte oder Pfad-Regeln genutzt werden.

#### SYS.2.1.A34 Einsatz von Anwendungsisolation(CIA)

Anwendungen, mit denen externe Daten bearbeitet werden, SOLLTEN ausschließlich in einer vom Betriebssystem isolierten Ablaufumgebung betrieben werden. 

#### SYS.2.1.A35 Aktive Verwaltung der Wurzelzertifikate(CI)

Im Zuge der Beschaffung und Installation des Clients SOLLTE dokumentiert werden, welche Wurzelzertifikate für den Betrieb des Clients notwendig sind. Auf dem Client SOLLTEN lediglich die für den Betrieb notwendigen und vorab dokumentierten Wurzelzertifikate enthalten sein. Es SOLLTE regelmäßig überprüft werden, ob die vorhandenen Wurzelzertifikate noch den Vorgaben der Institution entsprechen. Es SOLLTEN alle auf dem IT-System vorhandenen Zertifikatsspeicher in die Prüfung einbezogen werden (z.B. UEFI-Zertifikatsspeicher, Zertifikatsspeicher von Web-Browsern, etc.).

#### SYS.2.1.A36 Selbstverwalteter Einsatz von SecureBoot und TPM

Auf UEFI-kompatiblen Systemen SOLLTEN Bootloader, Kernel sowie alle benötigten Firmware-Komponenten durch selbstkontrolliertes Schlüsselmaterial signiert und nicht benötigtes Schlüsselmaterial entfernt werden. Sofern das TPM nicht benötigt wird, SOLLTE es deaktiviert werden.

#### SYS.2.1.A37 Schutz vor unbefugten Anmeldungen (CIA)

Um einen Zugang zum System durch kompromittierte Anmeldeinformationen zu verhindern, SOLLTE eine Mehrfaktorauthentisierung verwendet werden.

#### SYS.2.1.A38 Einbindung in die Notfallplanung(A)

Die Clients SOLLTEN im Notfallmanagementprozess berücksichtigt werden. Die Clients sind anhand der Geschäftsprozesse, für die sie benötigt werden, für den Wiederanlauf zu priorisieren. Es SOLLTEN geeignete Notfallmaßnahmen vorgesehen werden, indem mindestens Wiederanlaufpläne erstellt, Bootmedien zur Systemwiederherstellung generiert sowie Passwörter und kryptographische Schlüssel sicher hinterlegt werden.

#### SYS.2.1.A39 Unterbrechungsfreie und stabile Stromversorgung [Haustechnik](A)

Bei erhöhten Anforderungen an die Verfügbarkeit von stationären Clients SOLLTEN diese an eine unterbrechungsfreie Stromversorgung (USV) angeschlossen werden. Die USV SOLLTE hinsichtlich Leistung und Stützzeit ausreichend dimensioniert sein. Wenn Änderungen an den Verbrauchern durchgeführt wurden, SOLLTE erneut geprüft werden, ob die Stützzeit ausreichend ist. Sowohl für die USV-Geräte als auch die Clients SOLLTE ein Überspannungsschutz vorhanden sein. 

Die tatsächliche Kapazität der Batterie und damit die Stützzeit der USV SOLLTE regelmäßig getestet werden. Die USV SOLLTE regelmäßig gewartet werden.

#### SYS.2.1.A40 Betriebsdokumentation

Die Durchführung betrieblicher Aufgaben an Clients SOLLTE nachvollziehbar dokumentiert werden (wer?, wann?, was?), vor allem wenn dies Gruppen von Clients betrifft. Aus der Dokumentation SOLLTEN insbesondere Konfigurationsänderungen nachvollziehbar sein, auch sicherheitsrelevanten Aufgaben (wer ist z. B. befugt, neue Festplatten einzubauen) SOLLTEN dokumentiert werden. Alles, was automatisch dokumentiert werden kann, SOLLTE auch automatisch dokumentiert werden. Die Dokumentation SOLLTE gegen unbefugten Zugriff und Verlust geschützt werden.

#### SYS.2.1.A41 Verhinderung der Überlastung der lokalen Festplatte

Es SOLLTE überlegt werden, Quotas einzurichten. Alternativ SOLLTEN Mechanismen des verwendeten Datei- oder Betriebssystemsystems genutzt werden, die die Benutzer bei einem bestimmten Füllstand der Festplatte warnen oder nur noch dem Systemadministrator Schreibrechte einräumen.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeiner Client" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISiClient] Absicherung eines PC-Clients (ISi-Client),

  

 (zuletzt abgerufen am 27.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeiner Client" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.36 Identitätsdiebstahl
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
* G 0.43 Einspielen von Nachrichten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

