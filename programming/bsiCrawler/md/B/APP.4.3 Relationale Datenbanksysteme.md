1 Beschreibung
--------------

### 1.1 Einleitung

Datenbanksysteme (DBS) sind ein weithin genutztes Hilfsmittel, um rechnergestützt große Datensammlungen zu organisieren, zu erzeugen, zu verändern und zu verwalten. Ein DBS besteht aus dem so genannten Datenbankmanagement-System (DBMS) und einer oder mehrerer Datenbanken. Eine Datenbank ist eine Zusammenstellung von Daten samt ihrer Beschreibung (Metadaten), die persistent im Datenbanksystem abgelegt werden. Da Datenbanksysteme einer zentralen Bedeutung in einer IT-Infrastruktur zukommt, ergeben sich wesentliche Sicherheitsanforderungen an sie. Meist sind Kernprozesse einer Institution von den Informationen aus den Datenbanken abhängig, wodurch sich entsprechende Verfügbarkeitsanforderungen ergeben. Zusätzlich bestehen oft hohe Anforderungen an Vertraulichkeit und Integrität der in den Datenbanken gespeicherten Informationen.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, relationale Datenbanksysteme sicher betreiben zu können sowie die Informationen, die in Datenbanken verarbeitet und gespeichert werden, angemessen zu schützen. Dazu werden Anforderungen beschrieben, mit denen sich Datenbanksysteme sicher planen, umsetzen und betreiben lassen und durch die spezifische Gefährdungen reduziert werden können.

### 1.3 Abgrenzung

In diesem Baustein werden Anforderungen an relationale Datenbanksysteme beschrieben. Sicherheitsanforderungen an nicht-relationale Datenbanksysteme sind nicht Gegenstand des vorliegenden Bausteins, sondern werden im Baustein APP.4.5 *Nicht-Relationale Datenbanksysteme* aufgeführt.

Um die Informationen in den Datenbanken durchgängig zu schützen, sollten bereits in der Anwendungsentwicklung Sicherheitsanforderungen an den Aufbau der Datenbanktabellen und den Zugriff auf die Datenbank beachtet werden. Anforderungen hierzu werden jedoch nicht in diesem Baustein aufgeführt, sondern finden sich z. B. in CON.3 *Softwareentwicklung*, APP.3.1 *Web-Anwendungen* sowie APP.3.5 *Webservices*.

Ebenso geht der Baustein nicht auf Gefährdungen und Anforderungen ein, die das dem Datenbanksystem zugrunde liegende Betriebssystem und die Hardware betreffen. Aspekte hierzu finden sich in den entsprechenden betriebssystemspezifischen Bausteinen der Schicht IT-Systeme, z. B. SYS.1.3 *Unix-Server* oder SYS.1.2.2 *Windows Server 2012*.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich relationale Datenbanksysteme von besonderer Bedeutung:

### 2 1 Unzureichende Dimensionierung der Systemressourcen

Verfügt die Hardware eines Datenbanksystems nicht über genügend Systemressourcen, besteht die Gefahr, dass die Datenbank ganz ausfällt oder fehlerhaft arbeitet. Dadurch können beispielsweise Daten nicht gespeichert werden. Auch können in Stoßzeiten die Ressourcen stark ausgelastet werden und sich dadurch die Performance verschlechtern. Dies wiederum kann dazu führen, dass Anwendungen nicht oder nicht fehlerfrei ausgeführt werden.

### 2 2 Aktivierte Standard-Benutzerkonten

Bei der Erstinstallation bzw. im Auslieferungszustand eines Datenbankmanagementsystems sind Benutzer- und Administrationskonten häufig nicht oder nur mit Passwörtern gesichert, die öffentlich bekannt sind. Dadurch besteht die Gefahr, dass diese Konten missbräuchlich genutzt werden. Beispielsweise kann sich ein Angreifer mit den öffentlich bekannten Anmeldedaten am Datenbankmanagementsystem als Benutzer oder sogar als Administrator anmelden. Danach kann er die Konfiguration oder die gespeicherten Daten auslesen, manipulieren oder löschen.

### 2 3 Unzureichende Vergabe von Berechtigungen

Werden Berechtigungen fehlerhaft vergeben oder verwaltet, können Verantwortliche oder Benutzer des Datenbankmanagementsystems Berechtigungen erhalten, die über das zwingend notwendige Maß hinausgehen. So ist es möglich, dass die zu umfassend berechtigten Verantwortlichen oder Benutzer unerlaubte Aktionen auf dem Datenbankmanagementsystem ausführen, die weitreichende Folgen nach sich ziehen, wie das folgende Beispiel zeigt:

Durch ein fehlerhaftes SQL-Statement (beispielsweise in einem Installationsskript) löscht ein Benutzer unbeabsichtigt sehr viele Datensätze in der Datenbank. Nachher wird festgestellt, dass der Benutzer für diese Datensätze eigentlich nur Leserechte benötigt hätte, aber unnötigerweise auch über Löschrechte verfügte.

### 2 4 Unverschlüsselte Datenbankanbindung

In der Standardkonfiguration verbinden sich viele Datenbankmanagementsysteme unverschlüsselt mit den Anwendungen. Wird zwischen Anwendungen und Datenbankmanagementsystem unverschlüsselt kommuniziert, können übertragene Daten und Zugangsinformationen mitgelesen oder auf dem Transportweg manipuliert werden.

### 2 5 Datenverlust in der Datenbank

Durch Hardware- oder Softwarefehler sowie durch menschliches Versagen können Daten in der Datenbank verloren gehen. Da in Datenbanken meist wichtige Informationen für Anwendungen gespeichert sind, können Dienste ausfallen oder ganze Produktionsprozesse still stehen.

### 2 6 Integritätsverlust der gespeicherten Daten

Durch falsch konfigurierte Datenbanken, Softwarefehler oder manipulierte Daten kann die Integrität der Informationen in der Datenbank verletzt werden. Wird dies nicht oder erst spät bemerkt, können Kernprozesse der Institution stark beeinträchtigt werden. Werden beispielsweise die Integritätsbeziehungen (referenzielle Integrität) zwischen den Tabellen nicht korrekt definiert, kann dies dazu führen, dass sich die Daten in der Datenbank in einem fehlerhaften Zustand befinden. Wird dieser Fehler erst im Produktivbetrieb oder gar nicht bemerkt, müssen nicht nur die inkonsistenten Daten aufwendig bereinigt und rekonstruiert werden. Es kann mit der Zeit auch ein weitreichendes Schadensausmaß eingetreten sein, beispielsweise wenn es sich um kritische Daten (steuerrelevante Daten, Rechnungsdaten oder gar um Steuerungsdaten für ganze Produktionssysteme) handelt.

### 2 7 SQL-Injections

Eine häufige Angriffsmethode auf Datenbanksysteme sind SQL-Injections. Greift eine Anwendung auf die Daten einer SQL-Datenbank zu, so werden Befehle in Form von SQL-Anweisungen an das DBMS übermittelt. Werden Eingabedaten innerhalb der Anwendung unzureichend validiert, kann ein Angreifer eigene SQL-Befehle in die Anwendung einschleusen, die dann mit der Berechtigung des Dienstkontos der Anwendung bearbeitet werden. Ein Angreifer kann so Daten lesen, manipulieren, löschen, neue Daten hinzufügen oder auch Systembefehle aufrufen. Obwohl SQL-Injections primär die Anwendungen im Frontend betreffen, wirken sie sich erheblich auf das Datenbanksystem selbst und die damit verbundene Infrastruktur aus.

### 2 8 Unzureichendes Patchmanagement

Durch den umfangreichen Funktionsumfang der Datenbankmanagementsysteme treten relativ häufig Fehler oder Schwachstellen auf, die über Patches und Aktualisierungen vom Hersteller behoben werden. Werden diese jedoch nicht oder zu spät eingespielt, können Schwachstellen ausgenutzt und das Datenbankmanagementsystem erfolgreich angegriffen werden. Dadurch ist es möglich, dass Angreifer die Systeme manipulieren und so geschäftskritische Daten abfließen, Dienste ausfallen oder ganze Produktionsprozesse still stehen.

### 2 9 Unsichere Konfiguration des Datenbankmanagementsystems

Häufig sind in der Standardkonfiguration des Datenbankmanagementsystems nicht benötigte Funktionen aktiviert, die es einem potenziellen Angreifer erleichtern, Informationen aus der Datenbank auszulesen oder zu manipulieren. Beispielsweise kann sich ein Angreifer aufgrund einer unveränderten Standardinstallation mit einer von der Institution nicht benutzten Programmierschnittstelle verbinden, um das DBMS zu administrieren, ohne sich dafür authentifizieren zu müssen. Dadurch kann er unerlaubt auf die Datenbanken der Institution zugreifen.

### 2 10 Malware und unsichere Datenbank-Skripte

Bei vielen Datenbankmanagementsystemen ist es möglich, bestimmte Aktionen über Skripte zu automatisieren, die im Kontext der Datenbank ausgeführt werden, z. B. mithilfe der Procedural Language/Structured Query Language (PL/SQL). Dazu gehören unter anderem auch sogenannte Datenbanktrigger. Werden diese jedoch von den Verantwortlichen ungeprüft benutzt, besteht die Gefahr, dass die Datenbank-Skripte nicht den Anforderungen an die Softwareentwicklung der Institution genügen.

Ebenfalls kann ein Angreifer Kernfunktionen (z. B. Data Dictionary Tables) einer Datenbank manipulieren, beispielsweise mithilfe von Schadprogrammen oder Datenbank-Skripten. Diese Art von Angriffen ist nur schwer zu entdecken. Qualitätsmängel in diesen Skripten und Malware können sowohl die Vertraulichkeit als auch die Integrität und die Verfügbarkeit der in den Datenbanken abgelegten Daten gefährden. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Datenbanksysteme aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.4.3.A1 Erstellung einer Sicherheitsrichtlinie für Datenbanksysteme [Informationssicherheitsbeauftragter (ISB)]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für Datenbanksysteme erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie Datenbanksysteme sicher betrieben werden können. Die Richtlinie MUSS allen im Bereich Datenbanksysteme verantwortlichen Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem ISB abgestimmt und dokumentiert werden. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.

#### APP.4.3.A2 Installation des Datenbankmanagementsystems

Es MUSS sichergestellt sein, dass die Installationspakete des Datenbankmanagementsystems aus sicheren Quellen stammen. Bereits veröffentlichte Patches MÜSSEN eingespielt werden, bevor das DBMS betrieben wird.

#### APP.4.3.A3 Basishärtung des Datenbankmanagementsystems

Das Datenbankmanagementsystem MUSS gehärtet werden. Hierfür MUSS eine Checkliste mit den durchzuführenden Schritten zusammengestellt und abgearbeitet werden. Auch MÜSSEN alle Passwörter entsprechend den internen Anforderungen der Institution geändert werden. Alle Passwörter MÜSSEN verschlüsselt gespeichert werden. Die Basishärtung MUSS regelmäßig überprüft und falls erforderlich angepasst werden.

#### APP.4.3.A4 Geregeltes Anlegen neuer Datenbanken

Neue Datenbanken MÜSSEN nach einem definierten Prozess angelegt werden. Wenn eine neue Datenbank angelegt wird, MÜSSEN Grundinformationen zur Datenbank nachvollziehbar dokumentiert werden. 

#### APP.4.3.A5 Benutzer- und Berechtigungskonzept

Das Benutzer- und Berechtigungskonzept (siehe ORP.4 *Identitäts- und Berechtigungsmanagement*) der Institution MUSS um die für Datenbankmanagementsysteme notwendigen Berechtigungen für Rollen, Profile und Benutzergruppen erweitert werden.

Es MUSS ein Prozess etabliert werden, der regelt, wie Datenbankbenutzer und deren Berechtigungen angelegt, genehmigt, eingerichtet, modifiziert und wieder entzogen bzw. gelöscht werden. Dabei DÜRFEN immer NUR so viele Zugriffsrechte vergeben werden, wie für die jeweiligen Aufgaben erforderlich sind (Need-to-know-Prinzip). Alle Änderungen SOLLTEN dokumentiert werden. Die eingerichteten Benutzer und die ihnen zugeordneten Berechtigungen MÜSSEN regelmäßig überprüft und falls erforderlich angepasst werden. 

#### APP.4.3.A6 Passwortänderung [Fachverantwortliche]

Alle Passwörter der Datenbankbenutzer MÜSSEN der Passwortrichtlinie der Institution entsprechen (siehe ORP.4 *Identitäts- und Berechtigungsmanagement*). Es MUSS gewährleistet sein, dass die Passwörter beim geringsten Verdacht eines Sicherheitsvorfalles geändert werden. Insbesondere bei privilegierten Datenbankaccounts und Dienstkonten SOLLTE ein Passwortwechsel sorgfältig geplant und gegebenenfalls mit den Anwendungsverantwortlichen abgestimmt werden.

#### APP.4.3.A7 Zeitnahes Einspielen von Sicherheitsupdates

Vorhandene Sicherheitsupdates für das Datenbankmanagementsystem und das Betriebssystem MÜSSEN zeitnah installiert werden. Vorab MUSS auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. Bevor ein Patch eingespielt wird, MUSS das Datenbanksystem gesichert werden (siehe APP.4.3.A9 *Datensicherung eines Datenbanksystems*).

Zusätzlich MUSS eine verantwortliche Rolle definiert werden, die dafür zuständig ist, sich regelmäßig über bekannte Sicherheitslücken des Datenbankmanagementsystems sowie über verfügbare Sicherheitsupdates zu informieren. Des Weiteren MUSS geprüft werden, ob die Update-Intervalle des Datenbankmanagementsystems auf die Update-Zyklen des Herstellers abgestimmt werden können. Das Ergebnis SOLLTE nachvollziehbar dokumentiert werden. 

#### APP.4.3.A8 Datenbank-Protokollierung

Sicherheitsrelevante Ereignisse des Datenbanksystems MÜSSEN mit einem eindeutigen Zeitstempel protokolliert werden. Dabei MÜSSEN sich Art und Umfang der Protokollierung am Schutzbedarf der zu verarbeiteten Informationen orientieren. Zusätzlich MUSS geprüft werden, ob die Protokollierung der Fachanwendungen zusammen mit der Protokollierung der Datenbank alle erforderlichen Informationen abdeckt, um betriebs- und sicherheitsrelevante Veränderungen an der Datenbank-Infrastruktur und den Anwendungen zu erkennen. Es SOLLTE so protokolliert werden, dass die Protokolldateien nicht nachträglich veränderbar sind. Vertiefende Informationen sind in OPS.1.1.57 *Protokollierung* zu finden.

#### APP.4.3.A9 Datensicherung eines Datenbanksystems

Es MÜSSEN regelmäßig Systemsicherungen des DBMS und der Daten durchgeführt werden. Auch bevor eine Datenbank neu erzeugt wird, MUSS das Datenbanksystem gesichert werden. Hierfür SOLLTEN die dafür zulässigen Dienstprogramme benutzt werden. 

Alle Transaktionen SOLLTEN so gesichert werden, dass sie jederzeit wiederherstellbar sind. Sofern die Datensicherung die verfügbaren Kapazitäten übersteigt, SOLLTE ein erweitertes Konzept (z. B. inkrementelle Sicherung) erstellt werden, um die Datenbank zu sichern. Abhängig vom Schutzbedarf der Daten SOLLTEN die Wiederherstellungsparameter vorgegeben werden (siehe OPS.1.1.5 *Datensicherung)*. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Relationale Datenbanksysteme. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.4.3.A10 Auswahl geeigneter Datenbankmanagementsysteme

Bevor Datenbankmanagementsysteme beschafft werden, SOLLTEN Anforderungen an die DBMS definiert und in einem Anforderungskatalog dokumentiert werden. Danach SOLLTEN alle infrage kommenden Datenbankmanagementsysteme anhand des Katalogs bewertet werden. Die Ergebnisse SOLLTEN dokumentiert werden.

#### APP.4.3.A11 Ausreichende Dimensionierung der Hardware [Leiter IT, Fachverantwortliche]

Datenbankmanagementsysteme SOLLTEN auf ausreichend dimensionierter Hardware installiert werden. Die Hardware SOLLTE über genügend Reserven verfügen, um auch eventuell steigenden Anforderungen gerecht zu werden. Zeichnen sich trotzdem während des Betriebs Ressourcenengpässe ab, SOLLTEN diese frühzeitig behoben werden. Wenn die Hardware dimensioniert wird, SOLLTE das erwartete Wachstum für den geplanten Einsatzzeitraum berücksichtigt werden.

#### APP.4.3.A12 Einheitlicher Konfigurationsstandard von Datenbankmanagementsystemen [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Für alle eingesetzten Datenbankmanagementsysteme SOLLTE ein einheitlicher Konfigurationsstandard definiert werden. Alle Datenbankmanagementsysteme SOLLTEN nach diesem Standard konfiguriert und einheitlich betrieben werden. Falls es bei einer Installation notwendig ist vom Konfigurationsstandard abzuweichen, SOLLTEN alle Schritte vom ISB freigegeben und nachvollziehbar dokumentiert werden. Der Konfigurationsstandard SOLLTE regelmäßig überprüft und falls erforderlich angepasst werden.

#### APP.4.3.A13 Restriktive Handhabung von Datenbank-Links

Es SOLLTE sichergestellt sein, dass nur Verantwortliche dazu berechtigt sind, Datenbank-Links (DB-Links) anzulegen. Werden solche Links angelegt, MÜSSEN sogenannte Private DB-Links vor Public DB-Links bevorzugt angelegt werden. Alle von den Verantwortlichen angelegten DB-Links SOLLTEN dokumentiert und regelmäßig überprüft werden. Zudem SOLLTEN DB-Links mitberücksichtigt werden, wenn das Datenbanksystem gesichert wird (siehe APP.4.3.A9 *Datensicherung eines Datenbanksystems*).

#### APP.4.3.A14 Überprüfung der Datensicherung eines Datenbanksystems

Die vorgenommenen Datensicherungen SOLLTEN regelmäßig daraufhin überprüft werden, ob die Integrität der Sicherungsdateien noch gewährleistet ist. Die verantwortlichen Mitarbeiter SOLLTEN zudem regelmäßig üben, wie sich Datenbanken im Notfall schnell wiederherstellen lassen.

#### APP.4.3.A15 Schulung der Datenbankadministratoren [Vorgesetzte, Leiter IT]

Es SOLLTE gewährleistet sein, dass nur ausreichend geschulte Mitarbeiter das Datenbankmanagementsystem administrieren. Es SOLLTE ein Schulungsplan erstellt werden, mit dem sichergestellt wird, dass Datenbankverantwortliche rechtzeitig zu Themen der Informationssicherheit (siehe ORP.3 *Sensibilisierung und Schulung zur Informationssicherheit*)und Performance sowie zu den Funktionen neuer Versionen des Datenbankmanagementsystems geschult werden.

#### APP.4.3.A16 Verschlüsselung der Datenbankanbindung

Das Datenbankmanagementsystem SOLLTE so konfiguriert werden, dass Datenbankverbindungen immer verschlüsselt werden. Die dazu eingesetzten kryptografischen Verfahren und Protokolle SOLLTEN den internen Vorgaben der Institution entsprechen (siehe CON.1 *Kryptokonzept*).

#### APP.4.3.A17 Datenübernahme oder Migration [Fachverantwortliche]

Falls initial oder regelmäßig Daten in eine Datenbank übernommen werden, SOLLTE vorab definiert werden, wie diese Datenübernahme erfolgen soll. Nachdem Daten übernommen wurden, SOLLTE geprüft werden, ob sie vollständig und unverändert sind.

#### APP.4.3.A18 Überwachung des Datenbankmanagementsystems

Es SOLLTEN Parameter, Ereignisse und Betriebszustände des Datenbankmanagementsystems definiert werden, die für den sicheren Betrieb kritisch sind. Diese SOLLTEN mithilfe eines Monitoring-Systems überwacht werden. Für alle kritischen Parameter und Ereignisse SOLLTEN Schwellwerte festgelegt werden. Wenn diese Werte überschritten werden, MUSS geeignet reagiert werden (z. B. müssen die zuständigen Mitarbeiter alarmiert werden). Anwendungsspezifische Parameter, Ereignisse und deren Schwellwerte SOLLTEN mit den Verantwortlichen für die Fachanwendungen abgestimmt werden (siehe auch APP.4.3.A11 *Ausreichende Dimensionierung der Hardware*).

#### APP.4.3.A19 Schutz vor schädlichen Datenbank-Skripten [Entwickler]

Werden Datenbank-Skripte entwickelt, SOLLTEN hierfür verpflichtende Qualitätskriterien definiert werden (siehe CON.3 *Softwareentwicklung*). Datenbank-Skripte SOLLTEN auf gesonderten Testsystemen ausführlichen Funktionstests unterzogen werden, bevor sie produktiv eingesetzt werden. Die Ergebnisse SOLLTEN dokumentiert werden.

#### APP.4.3.A20 Regelmäßige Audits

Bei allen Komponenten des Datenbanksystems SOLLTE regelmäßig überprüft werden, ob alle festgelegten Sicherheitsmaßnahmen umgesetzt und diese korrekt konfiguriert sind. Dabei SOLLTE geprüft werden, ob der dokumentierte Stand dem Ist-Zustand entspricht, ob die Konfiguration des Datenbankmanagementsystems der dokumentierten Standardkonfiguration entspricht, ob alle Datenbank-Skripte benötigt werden und ob sie dem Qualitätsstandard der Institution genügen. Zusätzlich SOLLTEN die Protokolldateien des Datenbanksystems und des Betriebssystems nach Auffälligkeiten untersucht werden (siehe DER.1 *Detektion von sicherheitsrelevanten Ereignissen*). Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.4.3.A21 Einsatz einer Datenbank-Firewall(CI)

Es SOLLTE eine Datenbank-Firewall eingesetzt werden, wenn auf Anwendungsseite nicht sichergestellt werden kann, dass die Datenbank ausreichend geschützt ist, z. B. vor SQL-Injections. Ebenso SOLLTE durch die Datenbank-Firewall unterbunden werden, dass unberechtigt auf eine Datenbank zugegriffen werden kann. Bevor eine Datenbank-Firewall eingesetzt wird, SOLLTEN mögliche Nebeneffekte evaluiert werden. Wenn Datenbank-Anwendungen aktualisiert werden, SOLLTE darauf geachtet werden, dass auch die Firewall angepasst wird.

#### APP.4.3.A22 Notfallvorsorge(CIA)

Für das Datenbankmanagementsystem SOLLTE ein Notfallplan erstellt werden, der festlegt, wie ein Notbetrieb realisiert werden kann und welche Ressourcen dafür nötig sind (siehe DER.4 *Notfallmanagement*). Zusätzlich SOLLTE der Notfallplan definieren, wie aus dem Notbetrieb der Regelbetrieb wiederhergestellt werden kann. Der Notfallplan SOLLTE die nötigen Meldewege, Reaktionswege, Ressourcen und Reaktionszeiten der Fachverantwortlichen festlegen, durch sich ein möglicher Notfall schnell eskalieren lässt. Auf Basis eines Wiederanlaufkoordinationsplanes SOLLTEN alle von der Datenbank abhängigen IT-Systeme vorab ermittelt und berücksichtigt werden.

#### APP.4.3.A23 Archivierung(CIA)

Ist es erforderlich, Daten eines Datenbanksystems zu archivieren, SOLLTE ein entsprechendes Archivierungskonzept erstellt werden. Es SOLLTE sichergestellt sein, dass die Datenbestände zu einem späteren Zeitpunkt wieder vollständig und konsistent verfügbar sind. 

Im Archivierungskonzept SOLLTEN sowohl die Intervalle der Archivierung als auch die Vorhaltefristen der archivierten Daten festgelegt werden. Zusätzlich SOLLTE dokumentiert werden, mit welcher Technik die Datenbanken archiviert wurden. Mit den archivierten Daten SOLLTEN regelmäßig Wiederherstellungstests durchgeführt werden. Die Ergebnisse SOLLTEN dokumentiert werden.

#### APP.4.3.A24 Datenverschlüsselung in der Datenbank(C)

Die Daten in den Datenbanken SOLLTEN verschlüsselt werden. Dabei SOLLTEN vorher unter anderem folgende Faktoren betrachtet werden: 

* Einfluss auf die Performance,
* Schlüsselverwaltungsprozesse und -verfahren, einschließlich separater Schlüsselaufbewahrung und -sicherung, 
* Einfluss auf Backup-Recovery-Konzepte, 
* funktionale Auswirkungen auf die Datenbank, beispielsweise Sortiermöglichkeiten. 
#### APP.4.3.A25 Sicherheitsüberprüfungen von Datenbanksystemen(CIA)

Datenbanksysteme SOLLTEN regelmäßig mithilfe von Sicherheitsüberprüfungen überprüft werden. Bei den Sicherheitsüberprüfungen SOLLTEN die systemischen und herstellerspezifischen Aspekte der eingesetzten Datenbank-Infrastruktur (z. B. Verzeichnisdienste) sowie des eingesetzten Datenbankmanagementsystems betrachtet werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Relationale Datenbanksysteme" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
* #### [TELEKOM\_DB] Sicherheitsanforderungen Datenbanksysteme

  

 Privacy and Security Assessment Verfahren: Sicherheitsanforderungen Datenbanksysteme, Deutsche Telekom, 06.2014   
 <https://www.telekom.com/de/verantwortung/datenschutz-und-datensicherheit/sicherheit/sicherheit/privacy-and-security-assessment-verfahren-342724>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Relationale Datenbanksysteme" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
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
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

