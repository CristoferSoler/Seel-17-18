1 Beschreibung
--------------

### 1.1 Einleitung

Webanwendungen stellen Funktionen und dynamische Inhalte über das Internetprotokoll HTTP (Hypertext Transfer Protocol) bzw. HTTPS (HTTP über SSL bzw. TLS, d. h. geschützt durch eine verschlüsselte Verbindung) zur Verfügung. Dazu werden auf einem Server Dokumente und Benutzeroberflächen (z. B. Eingabemasken) erzeugt und an entsprechende Clientprogramme (Webbrowser) ausgeliefert. Webanwendungen werden gewöhnlich auf der Grundlage von Frameworks entwickelt. Diese stellen ein Rahmenwerk für häufig wiederkehrende Aufgaben zur Verfügung (z. B. für Sicherheitskomponenten). 

Um eine Webanwendung zu betreiben, sind in der Regel mehrere IT-Systemkomponenten notwendig. Hierzu gehören üblicherweise ein Webserver, um Daten auszuliefern, ein Applikationsserver, um die eigentliche Anwendung zu betreiben und zusätzliche Hintergrundsysteme, die als Datenquellen über unterschiedliche Schnittstellen angebunden sind (z. B. Datenbank oder Verzeichnisdienst). 

Webanwendungen werden sowohl in öffentlichen IT-Netzen als auch in Firmennetzen (Intranet) eingesetzt, um Daten und Anwendungen bereitzustellen. Abhängig von dem Zweck der Webanwendungen werden diese in der Regel von Anwendern genutzt, die sich im Vorfeld authentisieren müssen. Dabei müssen Webanwendungen Sicherheitsmechanismen umsetzen, die den Schutz der Daten gewährleisten und deren Missbrauch verhindern. Typische Sicherheitskomponenten bzw. -mechanismen sind: Authentisierung, Autorisierung, Ein- und Ausgabevalidierung, Session-Management, Fehlerbehandlung und Protokollierung. 

### 1.2 Zielsetzung

Ziel des Bausteins ist der sichere Betrieb von Webanwendungen sowie der Schutz von Informationen, die durch eine Webanwendung verarbeitet werden.

### 1.3 Abgrenzung

In diesem Baustein werden die für Webanwendungen spezifischen Gefährdungen und Anforderungen betrachtet. Während Webserver die Webseiten ausliefern (siehe auch APP.3.2 *Webserver*), stellen Webanwendungen Funktionen zur Verfügung und bereiten dynamische Inhalte vor, die durch den Webserver ausgeliefert werden. Der Baustein APP.3.2 *Webserver* beinhaltet auch die redaktionelle Planung des Webauftritts sowie das Notfallmanagement, diese Aspekte werden daher in diesem Baustein nicht nochmals behandelt. Auch die sicherheitsrelevanten Aspekte einer serviceorientierte Architektur (SOA) (siehe APP.3.7 *Serviceorientierte Architekturen*) werden im vorliegenden Baustein nicht betrachtet.

2 Gefährdungslage
-----------------

Die folgenden spezifischen Bedrohungen und Schwachstellen sind im Bereich Webanwendungen von besonderer Bedeutung:

### 2 1 Mängel bei der Entwicklung und der Erweiterung von Webanwendungen

Wird eine Webanwendung mit fehlenden oder unzureichenden Vorgaben und Standards entwickelt bzw. erweitert, so kann dies zu Fehlern, Qualitätseinbußen oder einer unvollständig umgesetzten Funktionalität führen. Fehler, die in frühen Entwicklungsphasen gemacht werden, werden häufig erst in einem fortgeschrittenen Entwicklungsstadium entdeckt. Um diese Fehler nachträglich zu beheben, muss oft der Quellcode der Webanwendung aufwendig geprüft und wieder korrigiert werden. Dadurch können die Entwicklungskosten deutlich zunehmen. Im Fall von grundlegenden, architektonischen Fehlern muss die Webanwendung eventuell sogar komplett neu entwickelt werden. Gibt es darüber hinaus keine Vorgaben, um Sicherheitsmechanismen umzusetzen, kann der erforderliche Schutzbedarf der zu verarbeitenden Daten möglicherweise verletzt werden.

### 2 2 Umgehung der Autorisierung bei Webanwendungen

Angreifer versuchen häufig, auf Funktionen oder Daten von Webanwendungen zuzugreifen, die nur für eine eingeschränkte Benutzergruppe verfügbar sind. Ist die Autorisierung fehlerhaft umgesetzt, kann ein Angreifer die Berechtigungen eines anderen Benutzers mit umfangreicheren Rechten erlangen und auf geschützte Bereiche und Daten zugreifen. Das geschieht üblicherweise, indem ein Angreifer seine Eingaben gezielt manipuliert, indem er (nicht vorgesehene) Befehle oder Anweisungen in die Textfelder eingibt.

### 2 3 Unzureichende Validierung von Ein- und Ausgabedaten

Verarbeitet eine Webanwendung Eingangsdaten, die von einem Angreifer manipuliert wurden, können Schutzmechanismen umgangen werden. Auch die Ausgabedaten der Webanwendung werden entweder direkt an den Browser des Benutzers, die aufrufende Anwendung oder an nachgelagerte Systeme übermittelt. Werden die Daten vor der Ausgabe nicht ausreichend validiert, könnten sie Schadcode enthalten, der auf den Zielsystemen interpretiert oder ausgeführt wird.

### 2 4 Fehlende oder mangelhafte Fehlerbehandlung durch Webanwendungen

Treten Fehler während des Betriebs einer Webanwendung auf, kann das z. B. die Verfügbarkeit der Webanwendung bis zur Unerreichbarkeit einschränken. So werden eventuell Aktionen unvollständig durchgeführt, zwischengespeicherte Zustände und Daten gehen verloren oder Sicherheitsmechanismen fallen aus. Werden Fehler nicht korrekt behandelt, kann sowohl der Betrieb als auch der Schutz der Funktionen und Daten nicht mehr gewährleistet werden. 

### 2 5 Unzureichende Protokollierung von sicherheitsrelevanten Ereignissen

Werden sicherheitsrelevante Ereignisse von der Webanwendung unzureichend protokolliert, können diese zu einem späteren Zeitpunkt nicht nachvollzogen und die Ursache nicht mehr ermittelt werden. Kritische Fehler und Angriffe, wie beispielsweise unbefugte Konfigurationsänderungen an der Webanwendung, bleiben unbemerkt und eine Schwachstelle kann dann nur noch schwer behoben werden. 

### 2 6 Offenlegung sicherheitsrelevanter Informationen bei Webanwendungen

Webseiten und Daten, die von einer Webanwendung generiert und ausgeliefert werden, können Informationen zu den Hintergrundsystemen enthalten, z. B. Angaben zu IT-Komponenten und Versionsständen von Frameworks. Diese Informationen können einem Angreifer Hinweise für einen gezielten Angriff auf die Webanwendung geben. 

### 2 7 Missbrauch einer Webanwendung durch automatisierte Nutzung

Wenn ein Angreifer Funktionen einer Webanwendung automatisiert nutzt, kann er zahlreiche Vorgänge in kurzer Zeit ausführen und so auf Wiederholung basierende Angriffe gegen die Webanwendung effizient durchführen. Mithilfe eines wiederholt durchgeführten Login-Prozesses können z. B. gültige Kombinationen aus Benutzernamen und Passwort systematisch ermittelt (Brute-Force) oder Listen mit gültigen Benutzernamen erzeugt werden (Enumeration). Darüber hinaus kann das wiederholte Aufrufen von ressourcenintensiven Funktionen (z. B. komplexe Datenbankabfragen) für Denial-of-Service-Angriffe auf Anwendungsebene missbraucht werden.

### 2 8 Unzureichendes Session-Management von Webanwendungen

Wenn eine unbefugte Person aufgrund eines unzureichenden Session-Managements die Session-ID eines Benutzers ermittelt, lässt sich damit die Webanwendung im Kontext dieser Sitzung verwenden. Hierdurch kann z. B. ein Angreifer mit der Webanwendung als legitimer authentisierter Benutzer interagieren, ohne die eigentlichen Zugangsdaten zu kennen. Bei einem Session-Fixation-Angriff lässt sich zum Beispiel ein Angreifer zunächst eine Session-ID von der Webanwendung zuweisen und übermittelt diese dem Opfer (zum Beispiel über einen Link in einer E-Mail). Folgt das Opfer diesem Link und authentisiert sich anschließend gegenüber der Webanwendung mit der vom Angreifer übermittelten Session-ID, so kann der Angreifer die Anwendung anschließend mit der ihm bekannten Session-ID verwenden. Auf diese Weise ist es ihm möglich, im Sicherheitskontext des angegriffenen Benutzers auf die Webanwendung zuzugreifen und so Funktionen zu nutzen. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Webanwendungen aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.3.1.A1 Authentisierung bei Webanwendungen [Entwickler]

Um auf geschützte Ressourcen einer Webanwendung zugreifen zu können, MÜSSEN sich Benutzer gegenüber der Anwendung authentisieren. Dafür MUSS eine geeignete Authentisierungsmethode ausgewählt und der Auswahlprozess dokumentiert werden. Wird die sogenannte Digest-Authentisierungsmethode verwendet, MÜSSEN die Passwortdateien auf dem Webserver ausreichend geschützt werden.

Es MUSS eine zentrale Authentisierungskomponente verwendet werden, die möglichst mit etablierten Standardkomponenten umgesetzt wurde. Die Komponente MUSS die Benutzer dazu zwingen, sichere Passwörter gemäß einer Passwort-Richtlinie zu benutzen. Speichert eine Webanwendung Authentisierungsdaten auf einem Client, MUSS der Benutzer explizit zustimmen ("Opt-In") und auf die Risiken der Funktion hingewiesen werden.

Um sicherzugehen, dass eine gültige Sitzung (Session-ID) nicht von einem Angreifer übernommen wurde, MÜSSEN sich bei kritischen Funktionen die Benutzer erneut authentisieren. Auch MÜSSEN in der Webanwendung Grenzwerte für fehlgeschlagene Anmeldeversuche definiert sein. Alle angebotenen Authentisierungsverfahren der Webanwendung MÜSSEN das gleiche Sicherheitsniveau aufweisen. Zudem MÜSSEN Benutzer sofort informiert werden, wenn das Passwort zurückgesetzt wurde. 

#### APP.3.1.A2 Zugriffskontrolle bei Webanwendungen [Entwickler]

Darf nur ein beschränkter Benutzerkreis die Webanwendung nutzen, MUSS mittels einer Autorisierungskomponente sichergestellt werden, dass Benutzer nur solche Aktionen durchführen können, für die sie auch berechtigt sind. Jeder Zugriff auf geschützte Inhalte und Funktionen MUSS kontrolliert werden, bevor er ausgeführt wird. 

Allen Benutzern MÜSSEN restriktive Zugriffsrechte ordnungsgemäß zugewiesen werden. Wenn Mitarbeiter für eine Webanwendung Zugriffsrechte erhalten oder sich diese verändern, MÜSSEN die Verantwortlichen dies prüfen, bestätigen und nachvollziehbar dokumentieren. Die Dokumentation der vergebenen Zugriffsrechte MUSS immer auf dem aktuellen Stand sein. Auch MUSS es ein geregeltes Verfahren geben, um Benutzern Zugriffsrechte wieder zu entziehen. Sollte es nicht möglich sein, Zugriffsrechte zuzuweisen, MUSS dafür ein zusätzliches Sicherheitsprodukt eingesetzt werden. 

Es MÜSSEN alle von der Webanwendung verwalteten Ressourcen von der Autorisierungskomponente berücksichtigt werden. Die Benutzer MÜSSEN serverseitig und zentral auf einem vertrauenswürdigen IT-System autorisiert werden. Ist die Zugriffskontrolle fehlerhaft, MÜSSEN Zugriffe abgelehnt werden. Auch MUSS es eine Zugriffskontrolle bei URL-Aufrufen und Objekt-Referenzen geben. Ebenso MUSS der Zugriff auf Dateien durch die Benutzer mit restriktiven Dateisystemberechtigungen beschränkt werden und es MUSS ein sicherer Umgang mit temporären Dateien vorgesehen werden.

#### APP.3.1.A3 Sicheres Session-Management [Entwickler]

Session-IDs MÜSSEN geeignet geschützt werden. Sie MÜSSEN zufällig erzeugt werden (mit ausreichender Entropie) . Wenn das der Webanwendung zugrunde liegende Framework Session-IDs generieren kann, MUSS die Funktion des Frameworks verwendet werden. Werden Session-IDs mithilfe eines Frameworks verwaltet und erzeugt, so MUSS das Framework sicher konfiguriert werden. Auch MUSS die Session-ID ausreichend geschützt werden, wenn sie übertragen und clientseitig gespeichert wird.

Eine Webanwendung MUSS den Benutzern die Möglichkeit geben, eine bestehende Sitzung explizit zu beenden. Nachdem der Benutzer sich angemeldet hat, MUSS eine bereits bestehende Session-ID durch eine neue ersetzt werden. Die Sitzungsdauer MUSS beschränkt werden, z. B. indem inaktive Sitzungen automatisch nach einer bestimmten Zeit ungültig werden und eine maximale Gültigkeitsdauer vergeben wird (Timeout). Nachdem die Sitzung ungültig ist, MÜSSEN alle Sitzungsdaten (sowohl server- als auch clientseitig) ungültig und gelöscht sein. 

#### APP.3.1.A4 Kontrolliertes Einbinden von Daten und Inhalten bei Webanwendungen [Entwickler]

Es MUSS sichergestellt werden, dass eine Webanwendung ausschließlich vorgesehene Daten und Inhalte einbindet und an den Benutzer ausliefert. Wenn eine Webanwendung eine Upload-Funktion für Dateien anbietet, MUSS diese Funktion eingeschränkt werden (z. B. auf notwendige Dateitypen). Auch Zugriffs- und Ausführungsrechte MÜSSEN in diesem Fall restriktiv gesetzt werden. Zudem MUSS sichergestellt werden, dass ein Benutzer Dateien nur im vorgegebenen Pfad speichern kann. 

Die Ziele der Weiterleitungsfunktion einer Webanwendung MÜSSEN ausreichend eingeschränkt werden, sodass Benutzer ausschließlich auf vertrauenswürdige Webseiten weitergeleitet werden. Verlässt ein Benutzer die Vertrauensdomäne, MUSS er informiert werden.

#### APP.3.1.A5 Protokollierung sicherheitsrelevanter Ereignisse von Webanwendungen [Entwickler]

Eine Webanwendung MUSS sicherheitsrelevante Ereignisse mit den erforderlichen Merkmalen nachvollziehbar protokollieren. Der Zugriff auf die Protokolldaten MUSS auf wenige befugte Personen eingeschränkt werden. Bei der Auswertung der Protokolldaten MUSS sichergestellt werden, dass Schadcode in Protokoll-Einträgen vom Auswertungsprogramm nicht interpretiert wird. Vertiefende Informationen sind in OPS.1.1.5 Protokollierung zu finden.

#### APP.3.1.A6 Zeitnahes Einspielen sicherheitsrelevanter Patches und Updates

Systemadministratoren MÜSSEN sich regelmäßig über aktuelle Schwachstellen informieren und sicherheitsrelevante Updates zeitnah einspielen. Software-Updates und Patches für Webanwendungen DÜRFEN nur aus vertrauenswürdigen Quellen bezogen werden. Sie MÜSSEN vor dem Roll-Out ausreichend getestet werden. Bevor Updates oder Patches installiert werden, MUSS stets sichergestellt sein, dass der ursprüngliche Zustand der Webanwendung wiederhergestellt werden kann. Der aktuelle Patchlevel MUSS dokumentiert werden.

#### APP.3.1.A7 Schutz vor unerlaubter automatisierter Nutzung von Webanwendungen [Entwickler]

Webanwendungen MÜSSEN durch geeignete Schutzmechanismen vor automatisierten Zugriffen geschützt werden, z. B. indem Grenzwerte für die Anzahl der Zugriffsversuche in einer bestimmten Zeitspanne definiert werden. Dabei MUSS jedoch berücksichtigt werden, wie sich die Grenzwerte auf die Webanwendung auswirken, z. B. könnte es zu Funktionseinschränkungen für berechtigte Benutzer kommen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Webanwendungen. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.3.1.A8 Systemarchitektur einer Webanwendung

Bereits in der Entwurfsphase einer Webanwendung SOLLTEN Sicherheitsaspekte beachtet werden. Auch SOLLTE darauf geachtet werden, dass die Architektur der Webanwendung die Geschäftslogik der Institution exakt erfasst und korrekt umsetzt.

In der Systemarchitektur SOLLTE vorgesehen werden, die Serverdienste durch jeweils separate IT-Systeme voneinander zu trennen. Auch SOLLTEN jeweils eigene Benutzerkonten für die unterschiedlichen Serverprozesse der Systemkomponenten verwendet werden,. Dabei SOLLTEN die Rechte dieser Dienstekonten auf Betriebssystemebene soweit eingeschränkt werden, dass nur auf die erforderlichen Ressourcen und Dateien des Betriebssystems zugegriffen werden kann.

Die Netzarchitektur SOLLTE einen mehrschichtigen Ansatz verfolgen (Multi-Tier-Architektur). Dabei SOLLTEN mindestens die Sicherheitszonen Webschicht, Anwendungsschicht und Datenschicht berücksichtigt werden. Aus diesen Zonen SOLLTE NICHT auf Systeme im Intranet zugegriffen werden können. 

Die Softwarearchitektur der Webanwendung SOLLTE mit allen Bestandteilen und Abhängigkeiten dokumentiert werden. Die Dokumentation SOLLTE bereits während des Projektverlaufs aktualisiert und angepasst werden, sodass sie schon in der Entwicklungsphase benutzt werden kann und Entscheidungsfindungen nachvollziehbar sind. Es SOLLTEN in der Dokumentation alle für den Betrieb notwendigen Komponenten, die nicht Bestandteil der Webanwendung sind, als solche gekennzeichnet werden. Ebenso SOLLTE daraus hervorgehen, welche Komponenten welche Sicherheitsmechanismen umsetzen, wie die Webanwendung in eine bestehende Infrastruktur integriert wird und welche kryptografischen Funktionen und Verfahren eingesetzt werden.

#### APP.3.1.A9 Beschaffung, Entwicklung und Erweiterung von Webanwendungen [Tester, Leiter Entwicklung, Beschaffer, Entwickler]

Wenn Produkte für Webanwendungen beschafft werden, SOLLTE ein Anforderungskatalog erstellt werden. Um verschiedene Produkte miteinander vergleichen zu können, SOLLTE eine Bewertungsskala entwickelt werden. 

Wird die eigentliche Webanwendung oder eine Erweiterung hierzu eigenentwickelt, SOLLTE nach einem geeigneten Vorgehensmodell vorgegangen werden. Dabei SOLLTEN vor der Inbetriebnahme alle Phasen des Modells durchlaufen werden. Für die Entwicklung SOLLTEN zudem Programmierrichtlinien vorgegeben werden, die dabei helfen, ein einheitliches Sicherheitsniveau zu etablieren. 

Wenn die Sicherheitsmechanismen einer Webanwendung entworfen und entwickelt werden, SOLLTEN diese möglichst zukünftige Standards und Angriffstechniken berücksichtigen. Bei der Anwendungsentwicklung SOLLTEN die Entwicklungs-, Test- und Produktivsysteme voneinander getrennt sein. 

Falls die Webanwendung von einem Dienstleister entwickelt wird, SOLLTE sichergestellt werden, dass dieser Dienstleister die nötigen Sicherheitsanforderungen bei der Entwicklung umsetzt und der Auftraggeber jederzeit auf den Quelltext zugreifen kann. 

#### APP.3.1.A10 Abnahme und Freigabe von Webanwendungen [Leiter IT]

Bevor Webanwendungen oder Erweiterungen, die entweder selbst oder im Auftrag entwickelt wurden, in den Echtbetrieb übernommen werden, SOLLTEN sie abgenommen werden. Dies gilt auch für Standardsoftware, die für den speziellen Einsatzzweck angepasst wird. Die Ergebnisse des Software-Abnahme-Verfahrens SOLLTEN dokumentiert werden. Nach der Abnahme SOLLTE die Webanwendung formal freigegeben werden. Falls im laufenden Betrieb Fehler festgestellt werden, SOLLTE es ein Verfahren zur Fehlerbehebung geben.

#### APP.3.1.A11 Sichere Anbindung von Hintergrundsystemen

Hintergrundsysteme von Webanwendungen, auf denen Funktionalitäten und Daten ausgelagert werden, SOLLTEN ausreichend geschützt werden. Der Zugriff auf Hintergrundsysteme SOLLTE ausschließlich über definierte Schnittstellen und von definierten Systemen aus möglich sein. Der Datenverkehr zwischen den Benutzern und der Webanwendung bzw. den Anwendungen und weiteren Diensten sowie den Hintergrundsystemen SOLLTE durch Sicherheitsgateways (Firewalls) reglementiert werden. Außerdem SOLLTE der Datenverkehr verschlüsselt werden. Zugriffe der Webanwendung auf Hintergrundsysteme SOLLTEN zudem mit minimalen Rechten erfolgen.

Beim Einsatz eines Enterprise Service Bus (ESB) muss sichergestellt werden, dass sich alle Dienste gegenüber dem ESB authentisieren, bevor ihnen ein Zugriff erlaubt wird. Es SOLLTE ein eigenes logisches Netzsegment für den ESB vorhanden sein. Der Zugriff auf den ESB SOLLTE ausschließlich durch die angeschlossenen Anwendungen und Dienste möglich sein. Alle Zugriffe auf den ESB SOLLTEN authentisiert und bei der Kommunikation über Standort- und Netzgrenzen hinweg verschlüsselt sein.

#### APP.3.1.A12 Sichere Konfiguration von Webanwendungen [Entwickler]

Eine Webanwendung SOLLTE so konfiguriert sein, dass auf ihre Ressourcen und Funktionen ausschließlich über die vorgesehenen, abgesicherten Kommunikationspfade zugegriffen werden kann. Der Zugriff auf nicht benötigte Ressourcen und Funktionen SOLLTE daher eingeschränkt werden. Folgendes SOLLTE bei der Konfiguration von Webanwendungen berücksichtigt werden:

* Deaktivierung nicht benötigter HTTP-Methoden
* Zeichenkodierungskonfiguration
* Festlegung von Grenzwerten
* Restriktive Dateisystemberechtigungen
* Administration einer Webanwendung
#### APP.3.1.A13 Restriktive Herausgabe sicherheitsrelevanter Informationen [Entwickler]

Webseiten und Rückantworten von Webanwendungen SOLLTEN keine Informationen beinhalten, die einem Angreifer Hinweise geben, mit denen er Sicherheitsmechanismen umgehen kann. Dazu SOLLTE mindestens gehören: 

* neutrale Fehlermeldungen
* keine sicherheitsrelevanten Kommentare oder Produkt- und Versionsangaben 
* eingeschränkter Zugriff auf sicherheitsrelevante Dokumentation
* regelmäßiges Löschen nicht benötigter Dateien
* sichere Erfassung durch externe Suchmaschinen sowie der Verzicht auf absolute Pfadangaben
Die Webanwendung SOLLTE NICHT aus unsicheren Netzen administriert werden. Administrationszugänge hierauf SOLLTEN auf vertrauenswürdige Netzsegmente und IT-Systeme, wie z. B. aus dem Administrationsnetz, beschränkt werden. Konfigurationsdateien der Webanwendung SOLLTEN außerhalb des Web-Root-Verzeichnisses gespeichert werden. 

#### APP.3.1.A14 Schutz vertraulicher Daten [Entwickler]

Vertrauliche Daten einer Webanwendung SOLLTEN durch sichere, kryptographische Algorithmen geschützt werden. Werden solche Daten übertragen, SOLLTE zum Beispiel eine SSL/TLS-Verschlüsselung eingesetzt werden. Zudem SOLLTE die HTTP-Post-Methode verwendet werden. Im Fall von Verbindungsfehlern SOLLTE bei einem verschlüsselten Kanal NICHT auf einen unverschlüsselten gewechselt werden. 

Auch SOLLTE die Webanwendung durch Direktiven gewährleisten, dass clientseitig keine schützenswerten Daten zwischengespeichert werden. Weiterhin SOLLTEN in Formularen keine vertraulichen Formulardaten im Klartext angezeigt und auch nicht vom Browser gespeichert werden. Zugangsdaten der Webanwendung SOLLTEN serverseitig mithilfe von kryptographischen Algorithmen vor unbefugtem Zugriff geschützt werden (Salted Hash). Ebenso SOLLTEN Dateien mit Quelltexten der Webanwendung nicht abgerufen werden können. Auch SOLLTEN Konfigurationsdateien von Webanwendungen ausschließlich außerhalb des Web-Root-Verzeichnisses gespeichert werden.

#### APP.3.1.A15 Verifikation essentieller Änderungen

Sollen wichtige Einträge geändert werden, wie beispielsweise Passwörter und Konfigurationen, SOLLTE die Eingabe durch ein Passwort erneut verifiziert werden. Die Benutzer SOLLTEN über Änderungen mittels Kommunikationswege außerhalb der Web-Anwendung informiert werden, beispielsweise per E-Mail.

#### APP.3.1.A16 Umfassende Ein- und Ausgabevalidierung [Entwickler]

Alle an eine Webanwendung übergebenen Daten SOLLTEN als potenziell gefährlich behandelt und entsprechend gefiltert werden. Dabei SOLLTEN alle Ein- und Ausgabedaten sowie Datenströme und Sekundärdaten (z. B. Session-IDs) validiert werden. Serverseitig SOLLTEN die Daten auf einem vertrauenswürdigen IT-System geprüft werden. Fehleingaben SOLLTEN möglichst nicht automatisch behandelt werden (engl. *Sanitizing*). Lässt es sich jedoch nicht vermeiden, SOLLTE *Sanitizing* sicher umgesetzt werden, damit ein Missbrauch ausgeschlossen ist.

#### APP.3.1.A17 Fehlerbehandlung [Entwickler]

Treten während des Betriebs einer Webanwendung Fehler auf, SOLLTEN diese so behandelt werden, dass die Webanwendung weiter in einem konsistenten Zustand verbleibt. Folgende Punkte SOLLTEN bei der Fehlerbehandlung berücksichtigt werden: 

* vertrauliche Informationen in Fehlermeldungen sind zu vermeiden, 
* Fehlermeldungen müssen protokolliert werden, 
* eine veranlasste Aktion muss im Fehlerfall abgebrochen und 
* in der Folge der Zugriff auf die angeforderte Ressource oder Funktion abgewiesen werden. 
Zuvor reservierte Ressourcen SOLLTEN im Rahmen der Fehlerbehandlung wieder freigegeben werden. Auch SOLLTE der Fehler möglichst von der Webanwendung selbst behandelt werden. 

#### APP.3.1.A18 Kontrolle der Protokolldateien

Es SOLLTE für jede Webanwendung ein Konzept erstellt werden, das festlegt, wie umfangreich die Protokollierung sein soll und wie die Daten auszuwerten sind. Zudem SOLLTE ein Verantwortlicher benannt werden, der die Protokolle auswertet. Die Ergebnisse SOLLTEN dem ISB oder einem anderen hierfür bestimmten Mitarbeiter vorgelegt werden. Weiterhin SOLLTEN bestehende gesetzliche Vorgaben in Bezug auf die Protokolldaten eingehalten werden, wie zum Beispiel datenschutzrechtliche Aspekte.

#### APP.3.1.A19 Schutz vor SQL-Injection

Webanwendungen SOLLTEN alle Eingaben und Parameter sorgfältig überprüfen und filtern, bevor diese an das Datenbanksystem weitergeleitet werden. Zudem SOLLTEN Stored Procedures bzw. Prepared SQL-Statements eingesetzt werden. Können Prepared SQL-Statements nicht eingesetzt werden, SOLLTEN die SQL-Queries separat abgesichert werden.Um potenziellen Angreifern keine Anhaltspunkte für Angriffe zu liefern, SOLLTEN Webanwendungen neutrale Fehlermeldungen nach außen ausgeben. 

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.1.A20 Einsatz von Web Application Firewalls(CIA)

Damit Daten auf höheren Protokollebenen gefiltert werden können, SOLLTEN Institutionen auf Web Application Firewalls (WAF) zurückgreifen. Wird eine WAF eingesetzt, SOLLTE die Konfiguration auf die zu schützende Webanwendung angepasst werden. Die Konfiguration der WAF SOLLTE nach jedem Update der Webanwendung geprüft werden. 

#### APP.3.1.A21 Verhinderung von Clickjacking [Entwickler](CI)

Um Clickjacking-Angriffe zu vermeiden, SOLLTE sichergestellt sein, dass die Inhalte auf allen Webseiten der Webanwendung ausschließlich auf der obersten Ebene des Browser-Fensters angezeigt werden. Zudem SOLLTE in den HTTP-Response-Headern der Webanwendung die Direktive *X-FRAME-OPTIONS* gesetzt werden.

#### APP.3.1.A22 Durchführung von Penetrationstests(CIA)

Webanwendungen SOLLTEN regelmäßig Penetrationstest unterzogen werden. Penetrationstests SOLLTEN dabei ausschließlich von zuverlässigen, vertrauenswürdigen und qualifizierten Personal oder Dienstleistern durchgeführt werden. Im Vorfeld SOLLTEN mit allen Auftragnehmern für Penetrationstests detaillierte Vereinbarungen zur Durchführung und Auswertung der Tests getroffen werden. Auch SOLLTE das Einverständnis aller zuständigen Stellen eingeholt werden. Für den Testzeitraum SOLLTEN die jeweiligen Ansprechpartner verbindlich feststehen und auch erreichbar sein. Nach dem Penetrationstest SOLLTEN die Ergebnisse ausreichend geschützt und vertraulich behandelt werden. Der Abschlussbericht SOLLTE dem ISB und den verantwortlichen Führungskräften vorgelegt werden. 

#### APP.3.1.A23 Verhinderung von Cross-Site Request Forgery [Entwickler](CI)

Um Cross-Site-Request-Forgery-(CSFR)-Angriffe zu erschweren, SOLLTE die Webanwendung Sicherheitsmechanismen unterstützen, die es ermöglichen, beabsichtigte Seitenaufrufe des Benutzers von unbeabsichtigt weitergeleiteten Befehlen Dritter zu unterscheiden. Mindestens SOLLTE dabei geprüft werden, ob neben der Session-ID ein geheimes Token für den Zugriff auf geschützte Ressourcen und Funktionen benötigt wird. Auch SOLLTE bei Webanwendungen das Referrer-Feld im HTTP-Request als zusätzliches Merkmal geprüft werden, um so einen beabsichtigten Aufruf durch einen Benutzer zu erkennen. 

#### APP.3.1.A24 Verhinderung der Blockade von Ressourcen [Entwickler](A)

Zum Schutz vor Denial-of-Service-(DoS)-Angriffen SOLLTEN ressourcenintensive Operationen vermieden und besonders abgesichert werden. Ebenso SOLLTE ein möglicher Überlauf von Protokolldaten bei Webanwendungen überwacht und verhindert werden. SOAP-Nachrichten SOLLTEN anhand eines entsprechenden XML-Schemas validiert werden. Bei kritischen Diensten und Anwendungen SOLLTE geprüft werden, mit Anti-DoS-Dienstleistern zusammenzuarbeiten.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Webanwendungen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [HILWEB] Hilfmittel zur Nutzung des Bausteins Webanwendung

  

 BSI, (zuletzt abgerufen am 29.09.2017)  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Vorabversionen/Baustein\_Webanwendungen\_Hilfsmittel.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Vorabversionen/Baustein_Webanwendungen_Hilfsmittel.pdf)

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (zuletzt abgerufen am 28.09.2017)  
 <https://www.owasp.org>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Webanwendungen" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

