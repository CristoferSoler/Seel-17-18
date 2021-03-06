1 Beschreibung
--------------

### 1.1 Einleitung

Diese Umsetzungshinweise decken allgemeine Sicherheitsanforderungen für alle IT-Systeme ab, die Dienste anderen IT-Systemen bereitstellen, wie Clients oder anderen Servern. Diese Dienste können Basisdienste für das lokale oder externe Netz sein, aber auch den E-Mail-Austausch ermöglichen oder Datenbanken und Druckerdienste anbieten. Server haben eine zentrale Bedeutung für die Informationstechnik und damit für funktionierende Arbeitsabläufe einer Institution. Oft erfüllen Server Aufgaben, ohne dass eine direkte interaktive Nutzung durch einen Benutzer erfolgt. Ergänzend gibt es Serverdienste, die direkt mit den Anwendern interagieren und nicht auf den ersten Blick als Server-Dienst wahrgenommen werden, beispielsweise X-Server unter Unix.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Im Vorfeld der eigentlichen Planung ist die generelle Architektur des Netzes festzulegen bzw. zu analysieren, aus der sich im Allgemeinen auch Vorgaben für die einzusetzenden Betriebssysteme (Server und Client) ergeben. Insbesondere ist dabei festzulegen, welche Ziele mit dem aufzubauenden Server verfolgt werden. Dazu sind die voraussichtlichen Einsatzszenarien zu beschreiben und der Einsatzzweck zu definieren.

Falls ein neues Netz aufgebaut wird, ist zunächst die Struktur des Netzes insgesamt zu planen, wobei Fragen wie die Festlegung einer Netztopographie und die Entscheidung über den Grad der Serverzentrierung (Terminalserver, "klassische" Client-Server-Architektur oder Nutzung von Peer-to-Peer-Funktionalität) zu klären sind. Hier sind die Maßnahmen des Bausteins NET.1.1 Netz-Architektur und -Design heranzuziehen.

In einem weiteren Schritt folgt die Festlegung der auf der Ebene der Server und der Clients verwendeten Betriebssysteme und gegebenenfalls auch die Auswahl spezifischer Varianten (z. B. Windows Server 2016 gegenüber Windows Server 2012 oder Linux gegenüber einer herstellerspezifischen Variante von Unix).

Falls ein neues Netz aufgebaut wird, muss als genaue technische Grundlage für die weiteren Arbeiten der detaillierte Aufbau des Netzes geplant werden. Anzahl und Zusammenspiel der vorgesehenen Server sind festzulegen. Die Aufgaben der Server und die Art ihrer Nutzung durch die Clients sind zu bestimmen. Anhand der Anforderungen an die Verfügbarkeit muss festgelegt werden, bis zu welchem Grad redundante Strukturen im Netz vorzusehen sind. Hier sind auch die notwendigen Vorgaben für die Infrastruktur (vor allem Klimatisierung und Stromversorgung, siehe dazu SYS.1.1.M15 Lokale unterbrechungsfreie und stabile Stromversorgung) festzulegen. Parallel dazu ist eine allgemeine Sicherheitsrichtlinie zu erarbeiten (siehe SYS.1.1.M11Festlegung einer Sicherheitsrichtlinie für einen allgemeinen Server), die anschließend durch systemspezifische Sicherheitsrichtlinien und detaillierte Richtlinien für den Einsatz der Hard- und Software im Netz zu ergänzen ist (siehe dazu die Bausteine zu den einzelnen Server-Betriebssystemen).

**Beschaffung**

Im nächsten Schritt muss die Beschaffung der Hardware und eventuell zusätzlich benötigter Software erfolgen. Aufbauend auf Einsatzszenarien sind die Anforderungen an zu beschaffende Produkte zu formulieren und basierend darauf die Auswahl der geeigneten Produkte zu treffen. Mit der Beschaffung dieser Produkte ist dann die Grundlage für die Arbeiten des nächsten Schrittes gelegt. Vertiefende Informationen zur Beschaffung sind im Baustein OPS.1.2.6 Beschaffung, Ausschreibung und Einkauf zu finden.

**Umsetzung**

Die Benutzer bzw. die Administratoren haben einen wesentlichen Einfluss auf die Sicherheit eines Servers. Vor der tatsächlichen Inbetriebnahme müssen die Benutzer und Administratoren daher für den Umgang bzw. die Nutzung des aufzubauenden Servers geschult werden. Insbesondere für Administratoren empfiehlt sich aufgrund der Komplexität in der Planung und in der Verwaltung eine intensive Schulung. Die Administratoren sollen dabei detaillierte Systemkenntnisse erwerben, so dass eine konsistente und korrekte Systemverwaltung gewährleistet ist. Benutzern sollte insbesondere die Nutzung der verfügbaren Sicherheitsmechanismen vermittelt werden. Hier sind die Anforderungen des Bausteins ORP.3 Sensibilisierung und Schulung zur Informationssicherheit heranzuziehen.

Nachdem die organisatorischen und planerischen Vorarbeiten durchgeführt wurden, kann die Installation und Inbetriebnahme des Servers erfolgen. Dabei sind die folgenden Empfehlungen zu beachten:

* Schon die Installation und Grundkonfiguration eines Servers muss mit besonderer Sorgfalt durchgeführt werden, um schwer reparierbare Fehler von vornherein zu vermeiden. Allgemeine Hinweise hierzu finden sich in SYS.1.1.M16 Sichere Installation. Neben den allgemeinen Maßnahmen, die in diesen Umsetzungshinweisen beschrieben sind, sind jeweils auch die weitergehenden Maßnahmen, die in den betreffenden Bausteinen für das jeweilige Betriebssystem empfohlen werden, umzusetzen.
* Nach der Installation und Grundkonfiguration der Server müssen gegebenenfalls übergeordnete Verwaltungsstrukturen konfiguriert werden. Dabei kommt unter anderem auch zum Tragen, für welchen Einsatzzweck die einzelnen Server geplant sind, beispielsweise als Dateiserver, Druckserver oder, im Falle von Thin Clients, als Terminalserver. Hier ist insbesondere die Maßnahme SYS.1.1.M6 Deaktivierung nicht benötigter Dienste und Kennungen wichtig, um einen kontrollierbaren Betrieb des Servers gewährleisten zu können.
* Nachdem die Installation und Grundkonfiguration des Servers abgeschlossen ist, kann die eigentliche Serversoftware installiert und konfiguriert werden. Die dafür notwendigen Schritte unterscheiden sich je nach Art und Einsatzzweck der Software teilweise erheblich und werden teilweise in eigenen Bausteinen behandelt. Prinzipiell wird empfohlen, für die Installation und Konfiguration der Serversoftware analog wie für die Konfiguration des Betriebssystems selbst vorzugehen: 

 
	+ Erstellung eines Installationskonzepts
	+ Falls mehrere Server mit ähnlichen Einsatzgebieten und Konfiguration installiert werden sollen: Erstellen einer Referenzinstallation
	+ Installation, Grundkonfiguration, Aktualisierung und Härtung
	+ Test und optionaler Penetrationstest bei erhöhtem Schutzbedarf
	  

 
**Betrieb**

Nach der Erstinstallation und einer Testbetriebsphase wird der Regelbetrieb aufgenommen. Unter Sicherheitsgesichtspunkten sind dabei folgende Aspekte zu beachten:

* Client-Server-Netze ändern sich sehr häufig. Dabei muss bei jeder Änderung sichergestellt werden, dass die Sicherheit auch nach der Änderung nicht beeinträchtigt wird. Die dabei im Detail zu beachtenden Aspekte sind in den Bausteinen zu den jeweiligen Serverbetriebssystemen enthalten. Dabei ist zu berücksichtigen, dass auch der Entzug von Berechtigungen sowie das Löschen nicht mehr benötigter Datenbestände so geregelt wird, dass durch veraltete Strukturen keine Sicherheitslücken entstehen. Eine wesentliche Hilfe ist dabei eine effiziente, umfassende Systemverwaltung, die sich jederzeit auf aktuelle Informationen über den Zustand des Systems und seiner Rechtestrukturen abstützen kann (siehe dazu SYS.1.1.M3 Restriktive Rechtevergabe und SYS.1.1.M21 Betriebsdokumentation).
* Ein Mittel im Rahmen der Aufrechterhaltung der Sicherheit eines Servers ist die Überwachung des Systems bzw. seiner Einzelkomponenten. Die hier relevanten Empfehlungen finden sich in SYS.1.1.M10 Protokollierung und SYS.1.1.M23 Systemüberwachung. Dabei spielen auch insbesondere Datenschutzaspekte eine Rolle. Die häufigen Sicherheitslücken der meisten Client-Server-Systeme und die Vielzahl von Angriffen, die sich gegen diese Schwächen richten, fordern von den Administratoren, dass diese sich permanent über den Sicherheitsstatus der Systeme und über neue Bedrohungen informieren und rechtzeitig Gegenmaßnahmen einleiten (siehe dazu SYS.1.1.M7 Updates und Patches für Betriebssystem und Anwendungen).
**Aussonderung**

Ein Server darf nicht einfach ohne Ankündigung abgeschaltet werden. Wenn ein Server außer Betrieb genommen werden soll, dann müssen, wenn es direkte Auswirkungen für die Anwender hat, diese rechtzeitig informiert werden und es muss eine Reihe von Punkten beachtet werden, um Ausfallzeiten und Datenverluste zu verhindern. Diese Punkte sind in SYS.1.1.M25 Geregelte Außerbetriebnahme eines Servers beschrieben.

Bei der Aussonderung eines Servers ist außerdem darauf zu achten, dass keine schützenswerten Informationen mehr auf den Datenträgern vorhanden sind. Dazu genügt es nicht, die Datenträger einfach neu zu formatieren, sondern sie müssen mindestens einmal vollständig überschrieben werden. Es ist zu beachten, dass ein reines logisches Löschen und auch nicht das Neuformatieren der Datenträger mit den Mitteln des installierten Betriebssystems die Daten nicht von den Datenträgern entfernt, so dass sie mit geeigneter Software, oft sogar ohne großen Aufwand, wieder rekonstruiert werden können. Vertiefende Informationen sind in OPS.1.1.8 Löschen und Vernichten zu finden.

Die Aussonderung des Servers muss dokumentiert werden. Bestandsverzeichnisse und Netzpläne müssen aktualisiert werden und sofern sich durch die Aussonderung strukturelle Veränderungen des Informationsverbundes ergeben, sollte auch das Sicherheitskonzept entsprechend angepasst werden.

**Notfallvorsorge**

Nur eine regelmäßige und umfassende Datensicherung gewährleistet zuverlässig, dass alle gespeicherten Daten auch im Falle von Störungen, Ausfällen der Hardware oder (absichtlichen oder unabsichtlichen) Löschungen weiter verfügbar gemacht werden können. Die notwendigen Anforderungen sind im Baustein OPS.1.1.5 Datensicherung beschrieben.

Neben der Absicherung im laufenden Betrieb spielt jedoch auch die Notfallvorsorge eine wichtige Rolle, da nur so der Schaden im Notfall verringert werden kann. Hinweise zur Notfallvorsorge finden sich im Baustein DER.4 Notfallmanagement. Hierzu gehört auch die Planung des Umgangs mit Sicherheitsvorfällen, die sich auf die Anforderungen des Bausteins DER.2.1 Incident Management abstützen sollte. Einige Hinweise zu besonderen Aspekten, die bei der Notfallvorsorge für einen Server beachtet werden sollten, sind in SYS.1.1.M22 Einbindung in die Notfallvorsorge beschrieben.

Es wird vorausgesetzt, dass der Server in einem Serverraum (siehe Baustein INF.12 Serverraum), einem Serverschrank (siehe Baustein INF.6 Schutzschränke) oder in einem Rechenzentrum (siehe Baustein INF.2 Rechenzentrum) untergebracht ist. Die für die Serverbetriebssysteme umzusetzenden Anforderungen sind den jeweiligen betriebssystemspezifischen Bausteinen zu entnehmen. Dies gilt analog auch für die angeschlossenen Clients. Die Anforderungen des Bausteins OPS.1.1.2 Netz und System-Management bilden in jedem Fall den übergeordneten Rahmen für den Betrieb servergestützter Netze.

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Allgemeiner Server" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### SYS.1.1.M1 Geeignete Aufstellung [Haustechnik]

Ein Server muss grundsätzlich in einem abschließbaren Rechnerraum oder Serverschrank aufgestellt oder eingebaut werden. Dabei ist zu regeln, wer Zutritt zu dem Raum beziehungsweise Zugang auf den Server selbst erhält. Hierfür sind die Anforderungen der Bausteine INF.5 Technikraum, INF.6 Schutzschrank, beziehungsweise Rechenzentrum umzusetzen.

#### SYS.1.1.M2 Benutzerauthentisierung

Die Identifikations- und Authentikationsmechanismen von IT-Systemen bzw. IT-Anwendungen müssen so gestaltet sein, dass Benutzer eindeutig identifiziert und authentisiert werden. Die Identifikation und Authentisierung muss vor jeder anderen Interaktion zwischen IT-System und Benutzer erfolgen. Weitere Interaktionen dürfen nur möglich sein, nachdem die Benutzer sich erfolgreiche identifiziert und authentisiert haben. Die Authentisierungsinformationen müssen so gespeichert sein, dass nur autorisierte Benutzer darauf Zugriff haben (sie prüfen oder ändern können). Bei jeder Interaktion muss das IT-System die Identität des Benutzers feststellen können.

Es gibt verschiedene Techniken, über die die Authentizität eines Benutzers nachgewiesen werden kann. Die bekanntesten sind:

* PINs (Persönliche Identifikationsnummern)
* Passwörter
* Token wie z. B. Zugangskarten
* Biometrie
Für sicherheitskritische Anwendungsbereiche sollte starke Authentisierung verwendet werden, hierbei werden zwei oder mehr Authentisierungstechniken kombiniert, wie Passwort plus Transaktionsnummern (Einmalpasswörter) oder plus Chipkarte. Daher wird dies auch häufig als Zwei-Faktor-Authentisierung bzw. Mehr-Faktor-Authentisierung bezeichnet. Alle eingesetzten Authentisierungstechniken müssen sich auf dem Stand der Technik befinden.

**Passwörter**

Werden in einem Client Passwörter zur Authentisierung verwendet, so ist die Sicherheit der Zugangs- und Zugriffsrechteverwaltung des IT-Systems entscheidend davon abhängig, dass die Passwörter korrekt gebraucht werden. Dafür sollte eine Richtlinie zum Passwortgebrauch erstellt und veröffentlicht werden. Außerdem sollten die IT-Benutzer regelmäßig, z.B. bei Team-Meetings, darauf hingewiesen werden.

Wenn Passwörter zur Authentikation eingesetzt werden, sollte das IT-System Mechanismen bieten, die folgende Bedingungen erfüllen:

* Es wird gewährleistet, dass jeder Benutzer individuelle Passwörter benutzt (und diese auch selbst auswählen kann).
* Es wird überprüft, dass alle Passwörter den definierten Vorgaben genügen (z. B. Mindestlänge, keine Trivialpasswörter). Die Prüfung der Passwortgüte sollte individuell regelbar sein. Beispielsweise sollten vorgegeben werden können, dass die Passwörter mindestens ein Sonderzeichen enthalten müssen oder bestimmte Zeichenkombinationen verboten werden.
* Das IT-System generiert Passwörter, die den definierten Vorgaben genügen. Das IT-System muss die so erzeugten Passwörter dem Benutzer anbieten.
* Der Passwortwechsel sollte von den IT-Systemen regelmäßig initiiert werden. Die Lebensdauer eines Passwortes sollte einstellbar sein.
* Die Wiederholung alter Passwörter beim Passwortwechsel sollte vom IT-System verhindert werden (Passwort-Historie).
* Bei der Eingabe sollte das Passwort nicht auf dem Bildschirm angezeigt werden.
* Nach der Installation bzw. der Neueinrichtung von Benutzern sollte das Passwort-System einen Passwort-Wechsel nach der Erst-Anmeldung erzwingen.
Vertiefende Informationen zur Authentisierung sind in ORP.4 Identitäts- und Berechtigungsmanagement zu finden.

#### SYS.1.1.M3 Restriktive Rechtevergabe

Zugriffsrechte auf Dateien, die auf den Datenträgern des Servers gespeichert sind, müssen restriktiv vergeben werden. Benutzer dürfen nur auf die Dateien ein Zugriffsrecht erhalten, die sie für ihre Aufgabenerfüllung benötigen. Das Zugriffsrecht selbst wiederum wird auf die notwendige Zugangssart beschränkt (siehe dazu "Vergabe von Zugangsberechtigungen"). So ist es zum Beispiel in den seltensten Fällen notwendig, ein Schreibrecht auf Programmdateien zu vergeben.

Meist darf über die Vererbung von Rechten auf Dateien in Unterverzeichnissen zugegriffen werden, wenn ein Zugriffsrecht auf das übergeordnete Verzeichnis bestand. Daraus ergibt sich, dass Zugriffsrechte auf höchster Ebene (Volume-Ebene) nur sehr restriktiv erteilt werden sollten. Insbesondere ist bei der Installation neuer Softwareprodukte die Rechtevergabe einer strengen Kontrolle zu unterwerfen.

Sollte der Speicherplatz des Servers gering ausgelegt sein, kann eine Beschränkung der maximalen Speicherkapazität, die ein Benutzer auf dem Server belegen darf, eingestellt werden.

**Vergabe von Zugangsberechtigungen**

Zugangsberechtigungen erlauben der betroffenen Person oder einem autorisierten Vertreter, bestimmte IT-Systeme bzw. System-Komponenten und Netze zu nutzen. Zugangsberechtigungen sollten möglichst restriktiv vergeben werden. Diese sind für jede nutzungsberechtigte Person aufgrund ihrer Funktion, unter Beachtung der Funktionstrennung, im einzelnen festzulegen. Entsprechend der Funktion ist der Zugang zum Rechner zu definieren, z. B. Zugang zum Betriebssystem (Systemverwalter) oder Zugang zu einer IT-Anwendung (Anwender). Ergänzend hierzu muss sichergestellt sein, dass personelle und aufgabenbezogene Änderungen unverzüglich berücksichtigt werden.

Der Zugang zu IT-Systemen oder IT-Anwendungen sollte erst nach einer Identifikation (z. B. durch Name, Benutzer-Kennung oder Chipkarte) und Authentisierung (z. B. durch ein Passwort oder über ein Authentisierungstoken) des Nutzungsberechtigten möglich sein und protokolliert werden.

Die Ausgabe bzw. der Entzug von Zugangsmitteln wie Benutzer-Kennungen oder Chipkarten ist zu dokumentieren. Regelungen über die Handhabung von Zugangs- und Authentisierungsmitteln (z. B. Umgang mit Chipkarten, Passworthandhabung) müssen ebenfalls getroffen werden. Alle Zugangsberechtigten müssen auf den korrekten Umgang mit den Zugangsmitteln hingewiesen werden.

Zugangsberechtigungen sollten bei längeren Abwesenheiten von berechtigten Personen vorübergehend gesperrt werden, um Missbrauch zu verhindern, z. B. bei Krankheit oder Urlaub. Dies sollte zumindest bei Personen mit weitreichenden Berechtigungen wie Administratoren erfolgen.

Es ist notwendig, die vorgenannten Festlegungen auf ihre korrekte Einhaltung sporadisch zu kontrollieren.

**Administratoren-Kennungen**

In vielen komplexen IT-Systemen, z. B. unter Unix oder in einem Netz, gibt es eine Administratorrolle, die keinerlei Beschränkungen unterliegt. Unter Unix ist das der Super-User root, in einem Novell-Netz der SUPERVISOR bzw. admin. Durch fehlende Beschränkungen ist die Gefahr von Fehlern oder Missbrauch besonders hoch.

Um Fehler zu vermeiden, soll unter dem Super-User-Login nur gearbeitet werden, wenn es notwendig ist; andere Arbeiten sollten auch Administratoren nicht unter einer Administrator-Kennung erledigen, sondern über eine personenbezogene Kennung. Insbesondere dürfen keine Programme anderer Benutzer mit Administrator-Rechten aufgerufen werden. Sollten für bestimmte Tätigkeiten dennoch administrative Rechte erforderlich sein, wird empfohlen, ein rollenbasiertes Administrationskonzept zu erstellen und umzusetzen (siehe SYS.1.1.M14 Erstellung eines Benutzer- und Administrationskonzepts). Ferner sollte die routinemäßige Systemverwaltung (zum Beispiel Backup, Einrichten eines neuen Benutzers) nur menügesteuert durchgeführt werden können.

Durch Aufgabenteilung, Regelungen und Absprache ist sicherzustellen, dass Administratoren keine inkonsistenten oder unvollständigen Eingriffe vornehmen. Zum Beispiel darf eine Datei nicht gleichzeitig von mehreren Administratoren editiert und verändert werden, da dann nur die zuletzt gespeicherte Version erhalten bleibt.

Für alle Administratoren sind zusätzliche Benutzer-Kennungen einzurichten, die nur über die eingeschränkten Rechte verfügen, die die Administratoren zur Aufgabenerfüllung außerhalb der Administration benötigen. Für Arbeiten, die nicht der Administration dienen, dürfen die Administratoren ausschließlich diese zusätzlichen Benutzer-Kennungen verwenden.

#### SYS.1.1.M4 Rollentrennung

Grundsätzlich kann zwischen Kennungen für Benutzer- und Administratoren unterschieden werden. Nur Administratoren verwalten die IT-Systeme, während normale Benutzerkennungen nur die Rechte besitzen, um ihre arbeitsplatzspezifischen Aufgaben erfüllen zu können. Normale Benutzerkennungen dürfen keine Administrationsrechte besitzen, damit das Betriebssystem und die Konfiguration der Clients vor versehentlicher, fahrlässiger oder vorsätzlicher Modifikation durch die Benutzer geschützt werden. 

Falls Benutzer nur bestimmte administrative Aufgaben wahrnehmen müssen, ist es oftmals nicht erforderlich, ihnen alle mit einem eigenen Login verbundenen Rechte oder sogar Systemadministrator-Rechte zu geben. Beispiele sind bestimmte Tätigkeiten der routinemäßigen Systemverwaltung, wie die Erstellung von Backups oder das Einrichten eines neuen Benutzers, die mit einem Programm menügesteuert durchgeführt werden, oder Tätigkeiten, für die ein Benutzer nur ein einzelnes Anwendungsprogramm benötigt. Insbesondere bei Aushilfskräften und externen Dienstleistern sollte darauf geachtet werden, dass diese nur die Dienste verwenden und nur auf die Daten zugreifen dürfen, die sie tatsächlich benötigen. Wenn ihre Tätigkeit beendet ist, sollten deren Accounts deaktiviert und alle Zugangsberechtigungen entfernt werden.

Für diese Benutzer sollte eine eingeschränkte Benutzerumgebung geschaffen werden. Sie kann zum Beispiel unter Unix durch eine Restricted Shell (rsh) und eine Beschränkung der Zugriffspfade mit dem Unix-Kommando chroot realisiert werden. Eine weitere Möglichkeit besteht darin, einzelne Anwendungsprogramme, wie Web-Browser, im sogenannten Kiosk-Modus auszuführen, so dass nur ein beschränkter Zugriff besteht.

Werden an Benutzerkennungen besonders weitgehende Rechte vergeben, so sollte dies möglichst restriktiv erfolgen. Hierbei sollte zum einem der Kreis der privilegierten Benutzer möglichst eingeschränkt werden und zum anderen nur die für die Durchführung der Arbeit benötigten Rechte vergeben werden. Für alle Aufgaben, die ohne erweiterte Rechte durchgeführt werden können, sollten auch privilegierte Benutzer unter Kennungen mit Standard-Rechten arbeiten. 

#### SYS.1.1.M5 Schutz der Administrationsschnittstellen

Es gibt unterschiedliche Zugangssmöglichkeiten, um Server zu administrieren. Abhängig von der genutzten Zugangsart müssen eine Reihe von Sicherheitsvorkehrungen getroffen werden. Bei größeren Netzen ist es empfehlenswert, auch die Server in ein zentrales Netzmanagement-System einzubinden, da sonst eine sichere und effiziente Administration kaum gewährleistet werden kann. Die zur Administration verwendeten Methoden müssen in der Sicherheitsrichtlinie festgelegt werden und die Administration darf nur entsprechend der Sicherheitsrichtlinie durchgeführt werden.

Allgemein ist es wichtig, einen Überblick darüber zu erhalten, welcher Teil der Administration eines Servers normalerweise

* lokal über die Konsole,
* remote über das Netz, aber unter Nutzung der Standardmechanismen des Betriebssystems, oder
* über ein zentrales netzbasiertes Administrationswerkzeug
durchgeführt werden soll. Es wird empfohlen, für die verschiedenen Nutzungsarten eine Übersicht zu erstellen, welche Administrationstätigkeiten auf welchem Weg durchgeführt werden können. Insbesondere ist es wichtig festzuhalten, ob bestimmte Tätigkeiten auf einem bestimmten Weg normalerweise nicht durchgeführt werden dürfen. 

* Lokale Administration  
 Ein Server sollte prinzipiell in einem Serverraum oder zumindest einem abschließbaren Serverschrank aufgestellt sein. Für den Teil der Administration, der trotzdem teilweise lokal über die Konsole erfolgen soll oder muss, müssen entsprechende Vorgaben dafür gemacht werden, wer Zugang zur Konsole erhält, welche Art der Authentisierung für den lokalen Zugang genutzt werden darf und welche anderen Vorgaben berücksichtigt werden müssen. 
* Remote-Administration  
 Meist wird ein Server nicht lokal an der Konsole sondern von einem Arbeitsplatzrechner aus über das Netz administriert. Um zu verhindern, dass dabei Authentisierungsinformationen der Administratoren und Konfigurationsdaten der Server abgehört oder gar von einem Angreifer manipuliert werden, sollte die Administration nur über sichere Protokolle (beispielsweise nicht über Telnet, sondern über SSH, nicht über HTTP, sondern über HTTPS) erfolgen. Alternativ kann ein eigenes Administrationsnetz eingerichtet werden, das vom dem restlichen Netz getrennt ist.Eine ungesicherte Remote-Administration über externe (unsichere) Netze hinweg darf in keinem Fall erfolgen. Dies muss bereits bei der Festlegung der Sicherheitsrichtlinie berücksichtigt werden. Auch im internen Netz sollten, soweit möglich, keine unsicheren Protokolle verwendet werden. 
* Administration über ein zentrales Managementsystem  
 Falls für die Administration des Servers ein zentrales Managementsystem genutzt werden soll, so sollten für diesen Zugangsweg analoge Vorüberlegungen angestellt werden, wie für die Remote-Administration. Zusätzlich ist es wichtig, dass das zentrale Managementsystem selbst entsprechend sicher konfiguriert und administriert wird. 
**Sichere Authentisierung**

IT-Systeme aller Art sollten grundsätzlich sicherstellen, dass sich alle Benutzer, die darauf zugreifen möchten, authentisieren müssen. Nur so kann verhindert werden, dass unautorisierte Personen Zugang auf die Dienste erlangen, die das System anbietet, oder auf die Daten, die auf dem System gespeichert sind. 

In der Regel werden Server über eine Netzverbindung administriert. Die Informationen, die für eine netzbasierte Authentisierung benötigt werden, müssen hierfür über ein LAN oder WAN übertragen werden. Daher ist es zwingend erforderlich, dass diese Informationen nicht mitgelesen oder verändert werden können.

Außerdem muss sichergestellt werden, dass ein Angreifer sich nicht anmelden kann, indem er aufgezeichnete Anmeldeinformationen wieder einspielt. Daher müssen die Anmeldeinformationen, die für die Authentisierung zwischen Server und Client ausgetauscht werden, verschlüsselt und zusätzlich, beispielsweise mit Challenge-Response-Verfahren, dynamisiert werden. 

Nachdem die Authentisierung erfolgreich abgelaufen ist, muss das System sicher stellen, dass die Benutzer nur auf solche Dienste und Daten Zugriff erhalten, für die sie entsprechende Berechtigungen besitzen.

Wenn die Gefahr des Abhörens von Leitungen zu Terminals besteht, sollten Administratoren nur an der Konsole arbeiten, damit keine Passwörter abgehört werden können. Bei der Administration von Unix-Systemen kann eine verschlüsselte Kommunikation beispielsweise mit dem Protokoll Secure Shell erfolgen. Hiermit ist eine gesicherte Administration von entfernten Arbeitsstationen aus möglich .

#### SYS.1.1.M6 Deaktivierung nicht benötigter Dienste und Kennungen

Die Standardinstallation eines Betriebssystems enthält oft eine Reihe von Programmen und Diensten, die normalerweise nicht benötigt werden und die gerade deswegen eine Quelle von Sicherheitslücken sein können. Dies gilt insbesondere für Netzdienste. Nach der Installation muss deswegen überprüft werden, welche Dienste auf dem System installiert und aktiviert sind. Nicht benötigte Dienste müssen deaktiviert oder ganz deinstalliert werden.

Die Überprüfung auf laufende Dienste kann einerseits lokal mit den Mitteln des installierten Betriebssystems und bei Netzdiensten andererseits von außen durch einen Portscan von einem anderen System aus erfolgen. Durch eine Kombination beider Methoden kann weitgehend ausgeschlossen werden, dass das System noch weitere ungewollte Netzdienste anbietet.

**Gesichertes Login**

Es sollte ein Login-Programm verwendet bzw. Optionen aktiviert werden, so dass die folgenden Maßnahmen durchgeführt werden können:

* Jeder Benutzer muss eine eigene Kennung und ein eigenes Passwort erhalten. Es darf kein Zugang ohne Kennung oder Passwort möglich sein. Als Passwort-Ersatz kann die Authentisierung des Benutzers auch über elektronische Signaturen, Pass-Tickets oder Ähnliches erfolgen.
* Die Anzahl erfolgloser Login-Versuche kann beschränkt werden. Nach jedem erfolglosen Login-Versuch vergrößert sich die Wartezeit bis zur nächsten Login-Aufforderung. Nach einer bestimmten Anzahl von Fehlversuchen wird die betroffene Benutzer-Kennung und / oder das Terminal gesperrt. Dabei ist zu bedenken, dass dadurch nicht die Administratoren ausgesperrt werden dürfen, es muss an der Konsole eine Zugangsmöglichkeit für die Administration offen bleiben.
* Der Zeitpunkt des letzten erfolgreichen Logins wird dem Benutzer beim Login gemeldet.
* Erfolglose Login-Versuche werden dem Benutzer beim Login gemeldet. Eventuell sollte diese Meldung bei mehreren darauf folgenden Anmeldungen wiederholt werden.
* Der Zeitpunkt des letzten Logouts wird dem Benutzer beim Login gemeldet. Hierbei wird zwischen Logouts zu einem interaktiven Login und solchen zu einem nicht-interaktiven Login (Logout von Hintergrundprozessen) unterschieden.
* Für das Login über Netze, in denen Passwörter unverschlüsselt übertragen werden, empfiehlt sich die zusätzliche Verwendung von Einmalpasswörtern.
**Sperren und Löschen nicht benötigter Accounts und Terminals**

Wenn keine gravierenden Gründe dagegen sprechen, sollten Accounts, die über einen längeren Zeitraum nicht benutzt werden, gesperrt und später gelöscht werden. Wenn beim Löschen von Accounts Dateien übrig bleiben, die keinem existierenden Benutzereintrag mehr zugeordnet sind, besteht die Gefahr, dass diese Dateien später eingerichteten Benutzern unberechtigt zugeordnet werden.

Bevor die Heimatverzeichnisse der Benutzer gelöscht werden, sollten diese vorher gesichert werden. Bei der Sperrung bzw. auf jeden Fall vor dem Löschen eines Accounts sollte der betroffene Benutzer informiert werden. Beim Löschen von Accounts ist darauf zu achten, dass auch die Dateien des Benutzers gefunden werden, die nicht in seinem Heimatverzeichnis liegen. Solche Dateien müssen gelöscht oder anderen Benutzern zugeordnet werden. Weiterhin ist darauf zu achten, dass laufende Prozesse und noch anstehende Aufträge gelöscht werden, z. B. unter Unix in der crontab.

Ebenso sollten Terminals, die über einen längeren Zeitraum nicht benutzt werden, gesperrt und später entfernt werden.

Wenn ein neu einzurichtender Benutzer seinen Account nur für einen begrenzten Zeitraum benötigt, sollte dieser nur befristet eingerichtet werden. Es kann vorteilhaft sein, Accounts grundsätzlich nur befristet einzurichten und in regelmäßigen Abständen (z. B. jährlich) bei Bedarf zu verlängern.

**Quotas**

Auch wenn bei der Beschaffung eines IT-Systems darauf geachtet wurde, dass dieses genügend Speicherplatz bietet, wird in vielen Fällen bei längerer Nutzung der Speicherplatz früher oder später knapp. Auf IT-Systemen, die von verschiedenen Benutzern genutzt werden, müssen die vorhandenen Ressourcen daher so aufgeteilt werden, dass alle Benutzer möglichst optimal arbeiten können.

Häufig lässt sich das Phänomen beobachten, dass die Benutzer mehr Speicherplatz haben möchten, als ihnen zur Verfügung steht. Neben dem ständig wachsenden Speicherplatzbedarf von Anwendungen ist ein anderer Grund hierfür, dass sich viele Benutzer nur ungern von alten und unbenötigten Dateien trennen. Werden keine Regelungen zur Speicherplatz-Begrenzung und zur Archivierung getroffen, besteht die Gefahr, dass Speicherplatz für große Mengen an Altdaten verschwendet wird oder die Benutzerverzeichnisse überlaufen.

Eine einfache Lösung wäre es, bei steigender Nachfrage grundsätzlich immer mehr Speicherplatz als benötigt bereitzustellen. Dies ist allerdings in der Praxis nicht immer machbar. Auch wenn die Anwender für eine sparsame Datenhaltung sensibilisiert werden, wird jede unbenötigte Datei dennoch oft als wichtig angesehen.

Für Benutzer oder Benutzergruppen, aber auch für Anwendungen kann durch Disk Quotas ein Speichervolumen festgelegt werden, das nicht überschritten werden darf. Auf Servern und allen IT-Systemen, die von mehreren Benutzern bzw. Anwendungen konkurrierend benutzt werden, sollte daher der Speicherplatz für die einzelnen Benutzer, aber auch für Anwendungen durch Disk Quotas beschränkt werden. Hierzu gehören Server (z. B. Datei-, Web- und Mailserver) und Clients mit mehreren Benutzerkennungen. Für Clients, auf denen die Daten- von der Systempartition getrennt ist und die nur von einem Benutzer genutzt werden, kann auf eine Disk Quota verzichtet werden.

Dabei ist die Wahl des Quota-Volumens wichtig. Sollen alle Benutzer das gleiche Quota-Volumen erhalten, kann das erforderliche Volumen errechnet werden, indem der zu nutzende Speicherplatz durch die Anzahl der Benutzer dividiert wird. Zusätzlich sollte aber eine Speicherplatz-Reserve eingeplant werden. Problematisch ist die Wahl einer zu kleinen Disk Quota. Steht den Benutzern zu wenig Speicherplatz zur Verfügung, könnten sie versuchen, die Informationen außerhalb der vorgesehenen Verzeichnisse abzulegen, um die Restriktionen zu umgehen. Hierfür werden dann häufig Speicherorte verwendet, die dafür nicht geeignet sind, z. B. temporäre Verzeichnisse oder andere für alle Benutzer beschreibbare Verzeichnisse. Wenn der Speicherplatz auf Dateiservern zu knapp bemessen ist, weichen Benutzer oft auf lokale Datenträger aus. Dies verstößt in vielen Fällen gegen die Regelungen und kann beispielsweise dazu führen, dass die Dateien nicht in die zentrale Datensicherung (Backup) einbezogen werden.

Es sollte einerseits festgelegt werden, welche Informationen wo abgespeichert werden sollen und auch, wie viele Versionen einer Datei wie lange auf dem Produktivsystem gespeichert werden sollen.

Datenbestände aus abgeschlossenen Projekten sollten geordnet archiviert und nicht "für alle Fälle" auf den Produktivsystemen vorrätig gehalten werden. Andererseits sollte festgelegt werden, wie viel Speicherplatz den verschiedenen Benutzergruppen und Anwendungen zur Verfügung gestellt wird. Zusätzlich sollte eine Reserve eingeplant werden. Es muss auch festgelegt werden, wie den Benutzern bei Bedarf ein höheres Speichervolumen zugeteilt werden kann. Die festgesetzten Werte müssen dokumentiert werden. Außerdem müssen sie regelmäßig überprüft und aktualisiert werden.

Wurde die Größe der Disk Quota bestimmt, sollte überlegt werden, ob und wie auf einen höheren Bedarf an Speicherplatz reagiert werden soll. Diese Entscheidung wird durch die Auswahl eines Quota-Typs beeinflusst. Bei Hard Quotas werden feste Obergrenzen gesetzt, so dass die Benutzer nicht die Möglichkeit haben, mehr als das ihnen zugewiesene Speicherkontingent zu nutzen. Eine Soft Quota hingegen ermöglicht es den Benutzern, für eine festgelegte Zeitspanne und bis zu einer festgelegten Grenze die Disk Quota zu überschreiten. Wird die Disk Quota überschritten, muss mindestens der Benutzer hierüber informiert werden, beispielsweise per E-Mail. Es sollte überlegt werden, ebenfalls den IT-Betrieb zu benachrichtigen, damit er auf eventuell eintretende Probleme reagieren kann. Zusätzlich muss festgelegt werden, ob und wie einzelnen Benutzern zusätzlicher Speicherplatz zugeteilt werden kann. Dies sollte ein geregeltes und nachvollziehbares Verfahren sein. Disk Quotas sollten nicht "auf Zuruf" erhöht werden.

Bei vielen gängigen Betriebssystemen werden Hilfsmittel mitgeliefert, um Disk Quotas einzurichten. Es sollte aber geprüft werden, ob zusätzliche Software zur Einrichtung und Verwaltung einer Disk Quota benötigt wird.

#### SYS.1.1.M7 Updates und Patches für Firmware, Betriebssystem und Anwendungen

Häufig werden Fehler in Produkten bekannt, die dazu führen können, dass die Informationssicherheit des Informationsverbundes, wo diese betrieben werden, beeinträchtigt wird. Entsprechende Fehler können Hardware, Firmware, Betriebssysteme und Anwendungen betreffen. Diese Schwachstellen müssen so schnell wie möglich behoben werden, damit sie nicht durch interne oder externe Angreifer ausgenutzt werden können. Dies ist ganz besonders wichtig, wenn die betreffenden Systeme mit dem Internet verbunden sind. Die Hersteller von Betriebssystem- oder Software-Komponenten veröffentlichen in der Regel Patches oder Updates, die auf dem jeweiligen IT-System installiert werden müssen, um den oder die Fehler zu beheben.

Die Systemadministratoren sollten sich daher regelmäßig über bekannt gewordene Schwachstellen informieren.

Wichtig ist, dass Patches und Updates, wie jede andere Software, nur aus vertrauenswürdigen Quellen bezogen werden dürfen. Für jedes eingesetzte System oder Softwareprodukt muss bekannt sein, wo Sicherheitsupdates und Patches erhältlich sind. Außerdem ist es wichtig, dass Integrität und Authentizität der bereits installierten Produkte oder der einzuspielenden Sicherheitsupdates und Patches überprüft werden (siehe Abschnitt "Sicherstellung der Integrität und Authentizität von Softwarepaketen"), bevor ein Update oder Patch installiert wird. Vor der Installation sollten sie außerdem mit Hilfe eines Computer-Virenschutzprogramms geprüft werden. Dies sollte auch bei solchen Paketen gemacht werden, deren Integrität und Authentizität verifiziert wurde.

Sicherheitsupdates oder Patches dürfen jedoch nicht voreilig eingespielt werden, sondern müssen vor dem Einspielen getestet werden. Für diese Tests sollten stets aktuelle, auf die Systemumgebung abgestimmte Testpläne oder automatisierte Tests genutzt werden, um ein einheitliches, aussagekräftiges Ergebnis zu erzielen. Falls sich ein Konflikt mit anderen kritischen Komponenten oder Programmen herausstellt, kann ein solches Update sonst zu einem Ausfall des Systems führen. Nötigenfalls muss ein betroffenes System so lange durch andere Maßnahmen geschützt werden, bis die Tests abgeschlossen sind. Es sollte gewährleistet werden, dass Updates, die durch automatische Update-Mechanismen eingespielt werden, ebenfalls getestet werden.

Vor der Installation eines Updates oder Patches sollte stets eine Datensicherung des Systems erstellt werden, die es ermöglicht, den Originalzustand wieder herzustellen, falls Probleme auftreten. Dies gilt insbesondere dann, wenn ausführliche Tests aus Zeitgründen oder mangels eines geeigneten Testsystems nicht durchgeführt werden können.

In jedem Fall muss dokumentiert werden, wann, von wem und aus welchem Anlass Patches und Updates eingespielt wurden. Aus der Dokumentation muss sich der aktuelle Patchlevel des Systems jederzeit schnell ermitteln lassen, um beim Bekanntwerden von Schwachstellen schnell Klarheit darüber zu erhalten, ob das System dadurch gefährdet ist.

Falls festgestellt wird, dass ein Sicherheitsupdate oder Patch mit einer anderen wichtigen Komponente oder einem Programm inkompatibel ist oder Probleme verursacht, so muss sorgfältig überlegt werden, wie weiter vorgegangen wird. Wird entschieden, dass auf Grund der aufgetretenen Probleme ein Patch nicht installiert wird, so ist diese Entscheidung auf jeden Fall zu dokumentieren. Außerdem muss in diesem Fall klar beschrieben sein, welche Maßnahmen ersatzweise ergriffen wurden, um ein Ausnutzen der Schwachstelle zu verhindern. Eine solche Entscheidung darf nicht von den Administratoren alleine getroffen werden, sondern sie muss mit den Vorgesetzten und dem ISB abgestimmt sein.

**Sicherstellung der Integrität und Authentizität von Softwarepaketen**

Durch unvorsichtiges Ausführen von Programmen, die aus "unsicheren" Quellen stammen, kann beträchtlicher Schaden entstehen. Schadsoftware (so genannte Malware) kann beispielsweise Programme zum Ausspähen von Passwörtern, Trojanische Pferde oder Backdoors auf einem Computer installieren, oder ganz einfach Daten beschädigen oder löschen.

Typische Quellen für solche Schadsoftware sind beispielsweise Programme, die sich als Bildschirmschoner, Virenscanner oder sonstige Hilfsprogramme ausgeben, und an E-Mails angehängt sind. Häufig werden diese unter gefälschten Absenderadressen an sehr viele Empfänger verschickt. Oft werden die Programme aus dem Internet heruntergeladen und ohne Überprüfung installiert.

Selbst wenn ansonsten keine Verschlüsselungs- oder Signaturtechniken eingesetzt werden, sollte die Nutzung in dem Umfang, wie er in dieser Maßnahme beschrieben wird, in Erwägung gezogen werden.

Software sollte grundsätzlich nur aus bekannten Quellen installiert werden, besonders dann, wenn sie nicht auf Datenträgern geliefert, sondern beispielsweise aus dem Internet heruntergeladen wurde. Dies gilt besonders für Updates oder Patches, die normalerweise nicht mehr auf Datenträgern ausgeliefert werden. Die meisten Hersteller und Distributoren bieten zu diesem Zweck Prüfsummen an, die zumindest eine Prüfung der Integrität eines Paketes erlauben. Die Prüfsummen werden dabei meist auf den Webseiten der Hersteller veröffentlicht oder auch per E-Mail verschickt. Um die Integrität eines heruntergeladenen Programms oder einer Archivdatei zu verifizieren, wird dann die veröffentlichte Prüfsumme mit einer von einem entsprechenden Programm lokal erzeugten Prüfsumme verglichen.

Falls zu einem Softwarepaket Prüfsummen angeboten werden, so sollten diese vor der Installation des Paketes überprüft werden.

Eine Überprüfung der Authentizität kann mit Prüfsummen jedoch nicht erfolgen. Daher werden in vielen Fällen für Programme oder Pakete digitale Signaturen angeboten. Die zur Überprüfung der Signatur benötigten öffentlichen Schlüssel sind wiederum meist auf den Webseiten des Herstellers oder von Public-Key-Servern verfügbar. Häufig werden die Prüfsummen mit einem der Programme PGP oder GnuPG erzeugt.

Ergibt die Prüfung, dass es sich um eine gültige Signatur des jeweiligen Herstellers handelt, so resultiert daraus ein deutlich höherer Grad an Vertrauenswürdigkeit für das Paket, als lediglich durch das Vorhandensein einer Prüfsumme.

Manchmal führen selbst die eingebauten Software-Updatemechanismen des jeweiligen Betriebssystems oder der Anwendungssoftware keine Prüfsummenvergleiche durch. Wenn möglich, sollte allerdings bei jedem Softwarepaket vor dem Einspielen ein Prüfsummencheck durchgeführt werden.

Ferner sind nicht alle Prüfsummenvergleiche ohne Mitwirkung der Anwender durchführbar, da die hierfür erforderlichen Checksummen, Signaturen oder Zertifikate von den Herstellern nicht auf eine einheitliche Weise bereitgestellt werden. Daher ist häufig eine manuelle Verifikation auf den Herstellerseiten oder die Anpassung der URLs in der Patch- und Änderungssoftware nötig.

Falls zu einem Softwarepaket digitale Signaturen verfügbar sind, sollten diese auf jeden Fall vor der Installation des Pakets überprüft werden.

Ein prinzipielles Problem bei der Verwendung digitaler Signaturen stellt die Verifikation der Authentizität des verwendeten Schlüssels selbst dar. Trägt der öffentliche Schlüssel keine Signatur einer bekannten vertrauenswürdigen Person oder Organisation (etwa eines Trustcenters), so bieten die mit dem entsprechenden privaten Schlüssel erzeugten Signaturen keine wirkliche Sicherheit, dass das Softwarepaket tatsächlich vom Entwickler, Hersteller oder Distributor stammt. Daher sollten die öffentlichen Schlüssel, sofern sie nicht zertifiziert sind, möglichst aus einer anderen Quelle als das Softwarepaket selbst bezogen werden, beispielsweise von einer CD-ROM des Herstellers, von einem anderen Spiegelserver, auf dem das Paket ebenfalls heruntergeladen werden kann, oder von einem Public Key Server.

Zur Überprüfung von Prüfsummen und digitalen Signaturen müssen die entsprechenden Programme lokal vorhanden sein. Die Administratoren sollten über die Bedeutung und Aussagekraft von Prüfsummen und digitalen Signaturen informiert sein. Außerdem müssen die Administratoren genügend Zeit haben, die entsprechenden Programme im Arbeitsalltag einzusetzen und sich mit der Bedienung vertraut zu machen.

Von einem Bezug von Patches und Änderungen per E-Mail ist aus verschiedenen Gründen abzuraten. Die Herkunft von E-Mails ist ohne Einsatz zusätzlicher Sicherheitsmechanismen schwer festzustellen und die Empfängeradressen in den Institutionen sind oft Verteilerlisten, deren Adresse leicht zu erraten ist. Patches und Änderungen können außerdem mittlerweile sehr umfangreich sein. Viele Unternehmen und Behörden haben die Größe von E-Mail-Anhängen beschränkt und verbieten unter Umständen zudem die Annahme ausführbarer Anhänge. Ferner werden durch die großen Datenmengen die E-Mail-Systeme unnötig belastet. Daher kann eine rechtzeitige Verfügbarkeit der Software-Änderungen, welche besonders bei Sicherheitspatches kritisch sein kann, via E-Mail nicht ausreichend gewährleistet werden.

Des Weiteren bieten einige Hersteller an, Änderungen und Patches dem Kunden direkt auf Datenträgern zuzusenden. Auch in diesem Fall sollten die Patches und Änderungen möglichst anhand von Prüfsummen oder digitalen Signaturen verifiziert werden, denn Absender-Angaben auf Postsendungen und Hersteller-Logos auf CDs und DVDs lassen sich leicht fälschen.

Ein weiterer Aspekt zur Prüfung der Echtheit der Aktualisierung können vom Hersteller veröffentlichte Nachrichten auf seiner Webseite, per Newsletter oder über ähnliche Kanäle sein. Einige Hersteller haben Zyklen und Zeitpunkte etabliert, zu denen in der Regel systematisch Informationen über Änderungen veröffentlicht werden.

#### SYS.1.1.M8 Regelmäßige Datensicherung

Nur eine regelmäßige und umfassende Datensicherung gewährleistet zuverlässig, dass alle gespeicherten Daten auch im Falle von Störungen, Auswirkungen von Schadsoftware, Ausfällen der Hardware oder (absichtlichen oder unabsichtlichen) Löschungen weiter verfügbar gemacht werden können. Die notwendigen Anforderungen sind im Baustein OPS 1.1.5 Datensicherung beschrieben.

#### SYS.1.1.M9 Einsatz von Viren-Schutzprogrammen

Zum Schutz vor Schadprogrammen können unterschiedliche Wirkprinzipien genutzt werden. Programme, die IT-Systeme nach sämtlichen bekannten Schadprogrammen durchsuchen, haben sich in der Vergangenheit als wirksames Mittel in der Schadprogramm-Prävention erwiesen. Entsprechend der in OPS1.1.4 Schutz vor Schadprogrammen beschriebenen Anforderungen sollten daher Viren-Schutzprogramme eingesetzt werden.

#### SYS.1.1.M10 Protokollierung

Die am Server mögliche Protokollierung ist in einem sinnvollen Umfang zu aktivieren. In regelmäßigen Abständen muss der IT-Betrieb die Protokolldateien der Server überprüfen. Es sollten alle sicherheitsrelevanten Ereignisse protokolliert werden. Dabei sind insbesondere folgende Vorkommnisse von Interesse:

* falsche Passworteingabe für eine Benutzer-Kennung bis hin zur Sperrung der Benutzer-Kennung bei Erreichen der Fehlversuchsgrenze,
* Versuche von unberechtigten Zugriffen,
* Stromausfall,
* Daten zur Netzauslastung und -überlastung.
Wie viele Ereignisse darüber hinaus protokolliert werden, hängt unter anderem vom Schutzbedarf der jeweiligen IT-Systeme ab. Je höher deren Schutzbedarf ist, desto mehr sollte protokolliert werden.

Da die Protokoll-Dateien mit der Zeit sehr umfangreich werden können, sollten die Auswertungsintervalle so kurz gewählt werden, dass eine sinnvolle Auswertung möglich ist. Um eine sinnvolle Auswertung zu ermöglichen, sollte jeder Protokoll-Eintrag Benutzer-Kennung bzw. Prozessnummer, Kennzeichnung des Endgeräts, Datum und Uhrzeit enthalten.

Es ist zu prüfen, welche gesetzlichen oder vertraglichen Aufbewahrungsfristen für Protokoll-Dateien beachtet werden müssen. Um die Nachvollziehbarkeit von Aktionen zu gewährleisten, kann eine Mindestspeicherdauer vorgeschrieben sein, aus Datenschutzgründen kann es auch eine Löschungspflicht geben.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Allgemeiner Server".

#### SYS.1.1.M11 Festlegung einer Sicherheitsrichtlinie für Server

Die Sicherheitsvorgaben für jeden Server ergeben sich aus der organisationsweiten Sicherheitsrichtlinie. Ausgehend von der allgemeinen Richtlinie müssen die Anforderungen für den gegebenen Kontext konkretisiert werden und in einer Sicherheitsrichtlinie für den Server oder eine Gruppe von Servern zusammengefasst werden. In diesem Zusammenhang ist zu prüfen, ob neben der organisationsweiten Sicherheitsleitlinie weitere übergeordnete Vorgaben wie IT-Richtlinien, Passwortrichtlinien oder Vorgaben zur Internetnutzung zu berücksichtigen sind.

Die Sicherheitsrichtlinie muss allen Personen und Gruppen, die an der Beschaffung und dem Betrieb der Server beteiligt sind, bekannt sein und Grundlage für deren Arbeit sein. Wie bei allen Richtlinien sind ihre Inhalte und ihre Umsetzung im Rahmen einer übergeordneten Revision regelmäßig zu prüfen.

Die Sicherheitsrichtlinie sollte das generell zu erreichende Sicherheitsniveau spezifizieren und grundlegende Festlegungen zum Betrieb des Servers treffen. Zur Verbesserung der Übersichtlichkeit kann es sinnvoll sein, für verschiedene Einsatzgebiete gesonderte Sicherheitsrichtlinien zu entwickeln.

Als erstes sollte die allgemeine Konfigurations- und Administrationsstrategie ("Liberal" oder "Restriktiv") festgelegt werden, da die weiteren Entscheidungen von dieser Festlegung wesentlich abhängen.

Für Server, die lediglich Daten mit normalem Schutzbedarf speichern und verarbeiten, kann eine relativ liberale Strategie gewählt werden, was in vielen Fällen die Konfiguration und Administration vereinfacht. Generell ist es aber auch in diesen Fällen empfehlenswert, die Strategie nur "so liberal wie nötig" auszulegen.

Bei einem Server, auf dem Daten mit hohem Schutzbedarf gespeichert oder verarbeitet werden, wird grundsätzlich eine restriktive Strategie empfohlen. Für Server mit besonderem Schutzbedarf bezüglich eines der drei Grundwerte sollte unbedingt eine restriktive Konfigurations- und Administrationsstrategie umgesetzt werden.

Nachfolgend sind einige Punkte aufgeführt, die berücksichtigt werden sollten:

* Regelungen zur physikalischen Zugangsskontrolle: Ein Server sollte grundsätzlich in einem abschließbaren Rechnerraum oder Serverschrank aufgestellt oder eingebaut werden. Dabei ist zu regeln, wer Zutritt zu dem Raum beziehungsweise Zugang auf den Server selbst erhält.
* Entscheidung, ob der Server virtualisiert werden soll (siehe SYS.1.5. Server-Virtualisierung).
* Regelungen für die Arbeit der Administratoren und Revisoren: 

 
	+ Nach welchem Schema werden Administrationsrechte vergeben? Welcher Administrator darf welche Rechte ausüben und wie erlangt er diese Rechte?
	+ Über welche Zugangswege dürfen Administratoren und Revisoren auf die Systeme zugreifen (beispielsweise nur lokal an der Konsole, über ein eigenes Administrationsnetz oder über verschlüsselte Verbindungen)?
	+ Welche Vorgänge müssen dokumentiert werden? In welcher Form wird die Dokumentation erstellt und gepflegt?
	+ Gilt für bestimmte Änderungen ein Vier-Augen-Prinzip?
	  

 
* Vorgaben für die Installation und Grundkonfiguration 

 
	+ Welche Installationsmedien werden zur Installation verwendet?
	+ Soll ein zentraler Authentisierungsdienst genutzt werden oder erfolgt die Benutzerverwaltung und -authentisierung nur lokal?
	+ Regelungen zur Benutzer- und Rollenverwaltung, Berechtigungsstrukturen (Ablauf und Methoden der Authentisierung und Autorisierung, Berechtigung zu Installation, Update, Konfigurationsänderungen etc.). Nach Möglichkeit sollte ein Rollenkonzept für die Administration erarbeitet werden.
	+ Vorgaben für die zu installierenden Softwarepakete.
	  

 
* Falls bei der Planung für den Server festgelegt wurde, dass Teile des Dateisystems verschlüsselt werden sollen, so ist es empfehlenswert, an dieser Stelle festzulegen, wie dies zu geschehen hat: 

 
	+ Welche Teile des Dateisystems sollen verschlüsselt werden?
	+ Welcher Mechanismus zur Einbindung des verschlüsselten Dateisystems soll verwendet werden?
	+ Welche Kryptoalgorithmen und Schlüssellängen sollen verwendet werden?
	+ Welche Daten sollen in den verschlüsselten Dateisystemen gespeichert werden?
	+ Wie werden die verschlüsselten Dateisysteme in das Backup einbezogen?
	  

 
* Regelungen zu Erstellung und Pflege von Dokumentation
* Vorgaben für den sicheren Betrieb 

 
	+ Welcher Benutzerkreis darf sich lokal auf dem System anmelden?
	+ Welche Benutzer erhalten Zugang über das Netz? Welche Protokolle dürfen verwendet werden?
	+ Auf welche Ressourcen dürfen die Benutzer zugreifen?
	  

 
* Vorgaben für die Passwortnutzung (Passwortregeln, Regeln und Situationen für Passwortänderungen, gegebenenfalls Hinterlegung von Passwörtern) 

 
	+ Wer darf das System herunterfahren?
	  

 
* Netzkommunikation und -dienste 

 
	+ Soll ein lokaler Paketfilter aufgesetzt werden?
	+ Welche Netzdienste werden von dem Server angeboten?
	+ Welche Authentisierungsverfahren sollen für die angebotenen Dienste gewählt werden?
	+ Auf welche externen Netzdienste soll von dem Rechner aus zugegriffen werden können?
	+ Soll ein verteiltes Dateisystem eingebunden werden?Verteilte Dateisysteme, bei denen die Nutzdaten unverschlüsselt übertragen werden, sollten nur im internen Netz verwendet werden. Soll ein verteiltes Dateisystem über ein unsicheres Netz hinweg genutzt werden, so muss es durch zusätzliche Maßnahmen (kryptographisch geschütztes VPN, Tunneling) gesichert werden.
	  

 
* Protokollierung 

 
	+ Welche Ereignisse werden protokolliert?
	+ Wo werden die Protokolldateien gespeichert? Werden sie lokal gespeichert oder soll ein zentraler Server eingesetzt werden, an dem die einzelnen Systeme im Netz ihre Protokollierungsinformationen schicken?
	+ Wie und in welchen Abständen werden die Protokolle ausgewertet?
	+ Wer hat Zugriff auf die Logdateien?
	+ Ist gewährleistet, dass personenbezogene Informationen nicht an unbefugte Personen gelangen?
	+ Wie lange sollen die Logdateien gespeichert werden?
	  

 
Anhand der oben genannten Punkte kann eine Checkliste erstellt werden, die bei Audits oder Revisionen hilfreich sein kann.

Die Verantwortung für die Sicherheitsrichtlinie liegt beim Sicherheitsmanagement, Änderungen und Abweichungen hiervon dürfen nur in Abstimmung mit dem Sicherheitsmanagement erfolgen.

Bei der Erstellung einer Sicherheitsrichtlinie ist es empfehlenswert, so vorzugehen, dass zunächst ein Maximum an Forderungen und Vorgaben für die Sicherheit der Systeme aufgestellt wird. Diese können anschließend den tatsächlichen Gegebenheiten angepasst werden. Idealerweise wird so erreicht, dass alle notwendigen Aspekte berücksichtigt werden. Für jede im zweiten Schritt verworfene oder abgeschwächte Vorgabe sollte der Grund für die Nicht-Berücksichtigung dokumentiert werden. 

#### SYS.1.1.M12 Planung des Server-Einsatzes

Eine grundlegende Voraussetzung dafür, dass ein Server sicher betrieben werden kann ist ein angemessenes Maß an Planung im Vorfeld.

Die Planung für den Einsatz eines Servers kann in mehreren Schritten nach dem Prinzip des Top-Down-Entwurfs erfolgen: Ausgehend von einem Grobkonzept für das Gesamtsystem werden konkrete Planungen für Teilkomponenten in spezifische Teilkonzepten festgelegt. Die Planung betrifft dabei nicht nur Aspekte, die klassischerweise mit dem Begriff Sicherheit verknüpft werden, sondern auch normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen.

Im Grobkonzept sollten beispielsweise folgende typische Fragestellungen behandelt werden:

* Welche Aufgaben soll das zu planende System erfüllen? Welche Dienste sollen von dem Server bereitgestellt werden? Gibt es besondere Anforderungen an die Verfügbarkeit des Systems oder an die Vertraulichkeit oder Integrität der gespeicherten oder verarbeiteten Daten?
* Diese Vorgaben kommen aus der übergreifenden Planung und werden von den allgemeinen Zielvorgaben bestimmt. Je genauer die Rahmenbedingungen bekannt und je präziser die Vorgaben formuliert sind, desto einfacher werden die folgenden Planungsschritte.
* Sollen in dem System bestimmte Hardwarekomponenten eingesetzt werden? Dies kann beispielsweise für die Auswahl des Betriebssystems wichtig sein.
* Welche Anforderungen an die Hardware (CPU, Arbeitsspeicher, Kapazität der Datenträger, Kapazität des Netzes etc.) ergeben sich aus den allgemeinen Anforderungen?
* Handelt es sich bei dem eingesetzten Netz um einen homogenen oder heterogenen Rechnerverbund?
* Ersetzt das System ein altes, vorhandenes? Sollen von dem alten System Datenbestände oder Hardwarekomponenten übernommen werden?
* Sollen die Daten lokal oder auf einem SAN-System abgelegt werden?
* Sollen die Server virtualisiert werden?
Die folgenden Teilkonzepte sollten bei der Planung des Servereinsatzes berücksichtigt werden:

* Authentisierung und Benutzerverwaltung:   
 Welche Arten der Benutzerverwaltung und Benutzerauthentisierung sollen auf dem System genutzt werden? Werden Benutzer nur lokal verwaltet oder soll ein zentrales Verwaltungssystem genutzt werden? Soll das System auf einen zentralen, netzbasierten Authentisierungsdienst zugreifen, oder wird nur eine lokale Authentisierung benötigt? 
* Benutzer- und Gruppenkonzept:   
 Ausgehend vom organisationsweiten Benutzer-, Rechte- und Rollenkonzept müssen entsprechende Regelungen für das System erstellt werden.
* Administration:   
 Wie soll das System administriert werden? Werden alle Einstellungen lokal vorgenommen oder der Server in ein zentrales Administrations- und Konfigurationsmanagement integriert?
* Partitions- und Dateisystem-Layout:   
 In der Planungsphase sollte eine erste Abschätzung des benötigten Plattenplatzes durchgeführt werden. Zur einfacheren Administration und Wartung ist es empfehlenswert, so weit wie möglich eine Trennung von Betriebssystem (Systemprogramme und -konfiguration), Anwendungsprogrammen und -daten (beispielsweise Datenbank-Server und Daten) und gegebenenfalls Benutzerdaten vorzunehmen. Verschiedene Betriebssysteme bieten hierfür unterschiedliche Mechanismen an (Aufteilung in Laufwerke unter Windows, Filesysteme unter Unix). Oft kann es sinnvoll sein, bestimmte Daten sogar auf einer eigenen Festplatte oder einem eigenen Plattensystem zu speichern. Dies erlaubt es beispielsweise, bei einer Neuinstallation oder einem Update des Systems die Daten auf den anderen Partitionen ohne Umkopieren zu übernehmen.  
 Falls auf dem Server Daten mit hohem Schutzbedarf bezüglich der Vertraulichkeit gespeichert werden, so wird der Einsatz verschlüsselter Dateisysteme dringend empfohlen. Dabei brauchen nicht notwendigerweise alle Dateisysteme verschlüsselt zu werden, sondern es wird oft ausreichend sein, für den Teil des Dateisystems eine Verschlüsselung vorzusehen, auf dem die Daten selbst gespeichert werden. Dies wird durch eine entsprechende Planung des Partitions- und Dateisystemlayouts erleichtert. Bei der Auswahl einer Verschlüsselung von einzelnen Dateien und Verzeichnissen sollte den Anwendern die Auswahl abgenommen werden, ob die Dateien verschlüsselt werden oder unverschlüsselt abgelegt werden.In der Planungsphase sollte die vorgesehene Aufteilung der Partitionen und deren Größe dokumentiert werden.
* Netzdienste und Netzanbindung:   
 In Abhängigkeit von den Anforderungen an die Vertraulichkeit, Integrität und Verfügbarkeit der Daten, die auf dem Server gespeichert oder verarbeitet werden sollen, muss die Netzanbindung des Servers geplant werden.  
 Generell wird empfohlen, einen Server nicht direkt im selben IP-Subnetz zu platzieren wie die Clients, die auf den Server zugreifen sollen. Wenn der Server zumindest durch einen Router von den Clients getrennt ist, dann bestehen wesentlich bessere Möglichkeiten zur Steuerung des Zugangs und zur Erkennung von Anomalien im Netzverkehr, die auf mögliche Probleme hindeuten.
* Ein Server, der Daten mit einem hohen Schutzbedarf bezüglich Vertraulichkeit oder Integrität speichert oder verarbeitet, sollte in einem eigenen IP-Subnetz angesiedelt werden und zumindest durch einen Paketfilter vom Rest des Netzes getrennt werden. Bei einem sehr hohen Schutzbedarf sollte ein Application Level Gateway eingesetzt werden.
* Bei normalem Schutzbedarf kann ein Server, der ausschließlich von Clients aus dem internen Netz genutzt wird, ausnahmsweise auch im selben Teilnetz angesiedelt werden. Es wird jedoch empfohlen, auch in diesem Fall den Server bei anstehenden Umstellungen in der Netzstruktur in ein eigenes Teilnetz zu verlegen.
* Abhängig vom festgelegten Einsatzzweck des Rechners wird außerdem eventuell der Zugang auf bestimmte Dienste im Netz (etwa Web-, File-, Datenbank-, Druck-, DNS oder Mailserver) benötigt. Dies muss bereits im Rahmen der Planung berücksichtigt werden, damit nicht zu einem späteren Zeitpunkt Schwierigkeiten beispielsweise durch zu geringe Übertragungskapazitäten oder Probleme mit zwischengeschalteten Sicherheitsgateways entstehen.
* Neben dem eigentlichen Dienst, für den ein Server aufgesetzt wird, werden oft noch andere Dienste benötigt, um den Server effizient nutzen und administrieren zu können. Beispielsweise wird für eine Administration über das Netz ein sicherer Zugang (beispielsweise SSH) benötigt, oder die Dateien für ein Webangebot können über das Netz auf den Webserver übertragen werden. Wenn die dadurch entstehende Netzkommunikation über unsichere Netze stattfindet, so müssen geeignete sichere Protokolle benutzt werden. Außerdem dürfen die Dienste nur autorisierten Benutzern und Rechnern zur Verfügung gestellt werden. Dies kann durch eine Passwortvergabe, durch den Einsatz eines Paketfilters oder anderer Mechanismen realisiert werden. Kein Dienst sollte in einem unsicheren Netz wie dem Internet bereitgestellt werden, wenn dies nicht ausdrücklich vorgesehen ist. 
* In der Planungsphase sollte eine Übersicht über die vorgesehenen und benötigten Netzdienste sowie über die in diesem Zusammenhang nötigen Netzverbindungen erstellt werden. Allgemein ist es wichtig, bereits in der Planungsphase zu überlegen, wie groß die Abhängigkeit eines Systems vom Funktionieren der Netzanbindung sein darf.
* Tunnel oder VPN:  
 Falls bereits in der Planungsphase absehbar ist, dass auf das System über unsichere Netze zugegriffen werden muss, sollten frühzeitig geeignete Lösungen untersucht werden. Beispielsweise kann der Zugang über ein VPN erfolgen.
* Monitoring:  
 Um die Verfügbarkeit und Auslastung des Systems und der angebotenen Dienste zu beobachten, kann ein Monitoring-System eingesetzt werden. In der Regel wird dafür auf einem weiteren Server ein Monitoring-Daemon installiert, dem ein lokal installierter Agent die zu überwachenden Daten sendet. Außerdem besteht die Möglichkeit, die Aktivitäten von Netzdiensten, die von externen Systemen angeboten werden, zu überwachen. Bei Problemen kann zum Beispiel automatisch der IT-Betrieb alarmiert werden.
* Protokollierung:  
 Die Protokollierung von Meldungen des Systems und der eingesetzten Dienste spielt eine wichtige Rolle, beispielsweise bei der Diagnose und Behebung von Störungen oder bei der Erkennung und Aufklärung von Angriffen. In der Planungsphase sollte entschieden werden, welche Informationen mindestens protokolliert werden sollen, und wie lange die Protokolldaten aufbewahrt werden sollen. Außerdem muss festgelegt werden, ob die Protokolldaten lokal auf dem System oder auf einem zentralen Logserver im Netz gespeichert werden sollen.Sinnvoller Weise sollte bereits in der Planungsphase festgelegt werden, wie und zu welchen Zeitpunkten Daten ausgewertet werden sollen.
* Hochverfügbarkeit:   
 Falls an die Verfügbarkeit des Systems und seiner Dienste besondere Anforderungen gestellt werden, so sollte bereits in der Planungsphase überlegt werden, wie diese Anforderungen erfüllt werden können. 
Alle Entscheidungen, die in der Planungsphase getroffen wurden, müssen so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Dabei ist zu beachten, dass meist andere Personen neben dem Autor diese Informationen auswerten müssen. Daher ist auf passende Strukturierung und Verständlichkeit zu achten.

#### SYS.1.1.M13 Beschaffung von Servern

Die Beschaffung eines Servers betrifft sowohl die Hard- als auch die Software, aus der der Server aufgebaut werden soll. Werden bei der Beschaffung eines Servers Fehler gemacht, so kann dies schwerwiegende Folgen auf den sicheren Betrieb eines Netzes haben, da mit ungeeigneter Hard- und Software das angestrebte Sicherheitsniveau unter Umständen nur schwer erreichbar ist.

Bevor ein Server beschafft wird, muss daher eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Aufgrund der Bewertung kann dann eine fundierte Kaufentscheidung erfolgen, die sicherstellt, dass der Server im praktischen Betrieb den Anforderungen genügt.

Auch rein funktionale Merkmale von Servern können Auswirkungen auf die Informationssicherheit haben. Meist ist dann der Grundwert Verfügbarkeit betroffen, beispielsweise wenn ein Server wegen unzureichender Speicherausstattung nicht die geforderten Antwortzeiten oder Durchsatzraten erreicht. Außerdem spielt die Unterstützung durch den Hersteller eine nicht zu vernachlässigende Rolle, wenn es beispielsweise darum geht, dass zeitnah Patches für Sicherheitslücken zur Verfügung gestellt werden.

Aus dem Blickwinkel der Informationssicherheit sind zentrale Anforderungen an Server, dass

* Hard- und Software so ausgelegt sind, dass die Anforderungen an die Verfügbarkeit des Servers und die Integrität der Daten erfüllt werden können,
* die Administration über sichere Protokolle möglich ist,
* die Benutzerverwaltung es erlaubt, das organisationsweite Rollenkonzept entsprechend umzusetzen, und
* dass es gegebenenfalls möglich ist, besonders sensitive Daten zu verschlüsseln.
Nachfolgend werden einige Anforderungen aufgelistet, die bei der Beschaffung von Servern berücksichtigt werden sollten:

* Grundlegende funktionale Anforderungen 

 
	+ Unterstützt das Gerät alle benötigten Hardwareschnittstellen?
	+ Unterstützt die Software alle benötigten Protokolle und Datenformate?
	+ Sicherheit
	+ Unterstützt das System sichere Protokolle zur Administration?
	+ Wenn Server nicht über ein eigenes Administrationsnetz administriert werden, muss die Administration mit Hilfe von sicheren Netzprotokollen möglich sein.
	  

 
* Wartbarkeit 

 
	+ Wird die Hard- und Software ausreichend lange vom Hersteller unterstützt und gepflegt?  
	 Der Hersteller sollte solange den Server unterstützen, wie er auch eingesetzt werden soll. Hierzu gehört es, dass Support angeboten wird und Updates bereitgestellt werden.
	+ Bietet der Hersteller regelmäßige Updates und schnell verfügbare Sicherheitspatches für die Software an?  
	 Es ist insbesondere wichtig, dass der Hersteller zeitnah auf bekannt gewordene Sicherheitsmängel reagiert.
	+ Wird für das Produkt die Möglichkeit des Abschlusses von Wartungsverträgen angeboten?  
	 Oft ist der Zugriff auf Updates und Unterstützungsleistungen vom Hersteller nur in Verbindung mit einem gültigen Wartungsvertrag möglich.
	+ Können im Rahmen der Wartungsverträge maximale Reaktionszeiten für die Problembehebung festgelegt werden?  
	 Ein Wartungsvertrag ist nur dann geeignet, wenn mit den garantierten Reaktions- und Wiederinbetriebnahmezeiten die festgelegten Ansprüche an die Verfügbarkeit der Geräte abgedeckt werden können.
	+ Bietet der Hersteller einen technischen Kundendienst (Hotline) an, der in der Lage ist, sofort bei Problemen zu helfen?  
	 Dieser Punkt sollte Bestandteil des abgeschlossenen Wartungsvertrags sein. Beim Abschluss des Vertrags ist auf die Sprache der zur Verfügung gestellten Hotline des Herstellers zu achten. 
	  

 
* Zuverlässigkeit/Ausfallsicherheit 

 
	+ Gibt es verlässliche Informationen zur Zuverlässigkeit und Ausfallsicherheit von Hard- und Software?
	+ Bietet der Hersteller gegebenenfalls Hochverfügbarkeitslösungen an?
	+ Wenn die Verfügbarkeitsanforderungen nicht über Wartungsverträge abgedeckt werden können, sollte das System Hochverfügbarkeitslösungen unterstützen. 
	  

 
* Benutzerfreundlichkeit 

 
	+ Lässt sich das Produkt einfach installieren, konfigurieren, administrieren und benutzen?
	+ Es sollten darüber hinaus Schulungen für das Produkt angeboten werden. 
	  

 
* Kosten 

 
	+ Wie hoch sind die Anschaffungskosten für Hard- und Software?
	+ Wie hoch sind die voraussichtlichen laufenden Kosten (Wartung, Betrieb, Support)?  
	 Diese Kosten müssen bereits in der Beschaffungsphase mit berücksichtigt werden. Der Inhalt der Wartungs- und Supportverträge sollte geprüft werden (Reaktionszeiten, Hotline, Qualifikation des Personals, etc.).
	+ Wie hoch sind die voraussichtlichen laufenden Kosten für das Personal?
	+ Müssen zusätzliche Soft- oder Hardware-Komponenten angeschafft werden?  
	 Diese Frage sollte bereits in der Planungsphase beantwortet werden. Wenn beispielsweise bereits ein Netz-Management-System im Einsatz ist, sollte die Kompatibilität mit den zu beschaffenden Geräten geprüft werden.  
	 Zudem sollte der Aufwand zur Integration in eine bestehende Infrastruktur beachtet werden.
	+ Wie hoch sind die Kosten für die Schulung von Administratoren?
	+ Mit welchen Kosten muss gerechnet werden, wenn wegen erhöhter Kapazitätsanforderungen ein Upgrade der Hardware notwendig ist?  
	 Die Kosten können in diesem Fall erheblich höher ausfallen, als die Kosten für die Hardware selbst, da in etlichen Lizenzmodellen von Softwareanbietern der Lizenzpreis von der Anzahl der Prozessoren oder dem Prozessortakt abhängt, so dass bei einem Hardwareupgrade auch gleichzeitig eine neue Programmlizenz erforderlich sein kann. 
	  

 
* Protokollierung 

 
	+ Welche Möglichkeiten der Protokollierung sind vorhanden?  
	 Die angebotenen Möglichkeiten zur Protokollierung müssen mindestens die in der Sicherheitsrichtlinie festgelegten Anforderungen erfüllen. Insbesondere sind die folgenden Punkte relevant:
	+ Ist der Detailgrad der Protokollierung konfigurierbar?
	+ Werden durch die Protokollierung alle relevanten Daten erfasst?
	+ Unterstützt das System zentrale Protokollierung (z. B. Syslog)?
	+ Kann die Protokollierung so erfolgen, dass die Bestimmungen des Datenschutzes erfüllt werden können?
	+ Werden Alarmierungsfunktionen unterstützt? 
	  

 
* Infrastruktur 

 
	+ Abmessungen und Kompatibilität mit Schutzschränken  
	 Auch der Platzbedarf eines Servers ist bei der Beschaffung zu berücksichtigen. Kann das Gerät in die vorgesehenen Schutzschränke eingebaut werden (Formfaktor, Gewicht, Befestigungselemente)?
	+ Stromversorgung und Abwärme  
	 Vom Hersteller sollten Angaben zum Stromverbrauch und zu den Anforderungen an die Umgebungstemperatur verfügbar sein. Reicht die vorhandene Kapazität der Stromversorgung und der USV aus? Reicht die vorhandene Kühlleistung zur Abfuhr der Abwärme des Geräts aus? 
	  

 
Die Anforderungen und die auf ihrer Basis getroffenen Auswahlentscheidungen sollten so dokumentiert werden, dass zu einem späteren Zeitpunkt nachvollziehbar ist, wie die Entscheidung zu Stande gekommen ist.

#### SYS.1.1.M14 Erstellung eines Benutzer- und Administrationskonzepts

Ablauf, Rahmenbedingungen und Anforderungen an administrative Aufgaben, sowie die Aufgabentrennungen zwischen den verschiedenen Rollen der Benutzer des IT-Systems sollten in einem Benutzer- und Administrationskonzept festgeschrieben werden. Hierzu sollten die am IT-System zugelassenen Benutzer, angelegten Benutzergruppen und Rechteprofile dokumentiert werden. Folgende Angaben zur Rechtevergabe an Benutzer und Benutzergruppen sollten festgelegt werden:

Zugelassene Benutzer: 

* zugeordnetes Rechteprofil (gegebenenfalls Abweichungen vom verwendeten Standard-Rechteprofil)
* Begründung für die Wahl des Rechteprofils (und gegebenenfalls der Abweichungen)
* Zuordnung des Benutzers zu einer Organisationseinheit, Raum- und Telefonnummer
* Zeitpunkt und Grund der Einrichtung
* Befristung der Einrichtung
Zugelassene Gruppen: 

* zugehörige Benutzer 
* Zeitpunkt und Grund der Einrichtung 
* Befristung der Einrichtung 
Vertiefende Informationen und konkrete Anforderungen hierzu sind im Baustein ORP.4 Identitäts- und Berechtigungsmanagement zu finden.

#### SYS.1.1.M15 Unterbrechungsfreie und stabile Stromversorgung [Haustechnik]

Eine lokale unterbrechungsfreien Stromversorgung (USV) hat die Aufgabe, ein einzelnes IT-System oder sehr wenige IT-Geräte gegen die Folgen kurzfristiger Unterbrechungen der Stromversorgung zu schützen. Diese Zielsetzung ist meist in kleineren IT-Strukturen gegeben, die zudem nicht über eine Netzersatzanlage verfügen.

Für größere IT-Strukturen oder gar die Versorgung ganzer Gebäude werden vornehmlich zentrale USV-Systeme eingesetzt.

Gleichgültig, ob eine lokale USV als Beistellgerät oder als 19-Zoll-Einschub eingesetzt wird, ist ihre Leistung und ihre Stützzeit durch die Geräteeigenschaften festgeschrieben und können in der Regel nicht verändert werden.

Bei den heute verfügbaren lokalen USV-Geräten und den üblicherweise durch sie bereitzustellenden geringen Leistungen (im Bereich bis circa 1 kVA) können diese Stromausfälle bis zu 120 Minuten problemlos überbrücken (Stützzeit). Welche Stützzeit tatsächlich im konkreten Szenario erforderlich ist, hängt davon ab, wie lange einerseits das Herunterfahren der angeschlossenen Geräte (Shutdown) dauert und wie lange andererseits darauf gewartet werden soll, dass die Stromversorgung wieder anspringt (Wartezeit). Da ein großer Teil aller Stromausfälle nur wenige Minuten dauert, dürfte eine Wartezeit von 15 Minuten meistens ausreichen, um eine Versorgungsunterbrechung zu überbrücken. Dauert die Versorgungsunterbrechung länger als die Wartezeit, und muss das versorgte IT-System heruntergefahren werden, um Datenverluste zu vermeiden, sollte die gesamte Stützzeit nach der Formel

Stützzeit = Wartezeit plus zweifache Shutdown-Zeit

dimensioniert werden. Durch den zweifachen Ansatz der Shutdown-Zeit ist eine Sicherheitsreserve gegeben, falls das Herunterfahren länger dauert als angenommen. Bei jedem Austausch oder Ergänzung von IT-Geräten, die durch eine USV versorgt werden, muss erneut geprüft werden, ob die vorhandene Stützzeit ausreicht.

Drei USV-Arten sind zu unterscheiden:

* VFD-USV  
 Bei der VFD-USV (VFD steht für Voltage and Frequency Dependent) werden die angeschlossenen Verbraucher im Normalbetrieb direkt aus dem Stromversorgungsnetz gespeist. Kleinere Störungen im Versorgungsnetz können also direkt bis zu den angeschlossenen Verbrauchern gelangen. Erst wenn dieses ausfällt, schaltet sich die VFD-USV selbsttätig zu und übernimmt die Versorgung. Dazu benötigt sie bis zu 10 ms (Umschaltlücke), was für manche IT-Geräte schon zu viel sein kann. Die VFD-USV wurde früher auch Offline-USV genannt.
* VI-USV (Voltage Independent)  
 Hierbei wird die Versorgungsspannung bei kleineren Schwankungen nachgeregelt (VI steht für Voltage Independent), ohne dass die USV als solche die Versorgung der angeschlossenen Verbraucher komplett übernimmt. Die Frequenz am Ausgang einer VI-USV ist aber wie bei einer VFD-USV direkt vom Versorgungsnetz abhängig. Auch bei der VI-USV kann es bei der Umschaltung auf Batteriebetrieb zu einer Umschaltlücke kommen.
* VFI-USV (Voltage and Frequency Independent)  
 Bei der VFI-USV (Voltage and Frequency Independent) gibt es im Normalfall keine direkte Verbindung zwischen USV-Eingang und -Ausgang. Die elektrische Energie wird eingangsseitig gleichgerichtet und in den Zwischenkreis gespeist. Von dort werden die Batterien im optimalen Ladezustand gehalten und der Wechselrichter versorgt. Dieser erzeugt die für die angeschlossenen Verbraucher erforderliche Wechselspannung.  
 Da die Ausgangsenergie unabhängig vom Eingang permanent über den Wechselrichter erzeugt wird, gibt es hier keine Umschaltlücke. Die VFI-USV wurde früher als Online-USV bezeichnet. 
Da die VFI-USV als einzige der drei Systeme wirklich unterbrechungsfrei arbeitet, sollt diesem immer der Vorzug geben werden. Unter Berücksichtigung weiterer, hier nicht behandelter Qualitätsmerkmale stellt eine USV, die nach DIN IEC 62040-3 gemäß VFI-SS-111 klassifiziert ist, das Optimum für die IT-Versorgung dar.

Entgegen einer immer wieder geäußerten Annahme stellt eine USV gleich welcher Bauart keinen Überspannungsschutz im eigentlichen Sinn dar. Eine USV ist zwar in der Lage, im Rahmen ihrer normalen Funktion zu hohe Spannungen von den angeschlossenen Verbrauchern fernzuhalten. Gegen Überspannungen, wie sie durch die technischen Einrichtungen des Überspannungsschutzes abgefangen werden, hilft aber eine USV keinesfalls. Im Gegenteil, eine USV muss wie alle anderen elektrischen Verbraucher durch geeignete Schutzmaßnahmen gegen Überspannungen geschützt werden (siehe Abschnitt "Überspannungsschutz").

Um mögliche Probleme mit Schutzleiterströmen zu vermeiden, sollten IT-Geräte, die über eine lokale USV versorgt werden, nicht über geschirmte Leitungen (z. B. Druckerkabel) mit anderen IT-Geräten verbunden werden, die über einen anderen Weg versorgt werden.

Da die Batterien einer lokalen USV in den seltensten Fällen in ihrem optimalen Temperaturbereich (typischerweise um 20°C) betrieben werden, ist die Batterie-Lebensdauer bei lokalen USV-Geräten recht gering, im günstigsten Fall bis zu 5 Jahre, meist weniger. Während dieser Betriebszeit verlieren die Batterien permanent an Leistung, so dass eine lokale USV nach vielleicht zwei oder drei Jahren allenfalls noch die Hälfte der Stützzeit im Neuzustand bereitstellen kann. Um sicher zu stellen, dass die USV die erforderliche Stützzeit bereitstellt, sollte etwa einmal pro Jahr die tatsächliche Stützzeit ermittelt werden. Manche USV-Systeme verfügen dazu über eingebaute Prüfmechanismen. Ist das nicht der Fall, kann der Wert durch einen Lasttest ermittelt werden.

Wie bei allen anderen elektrischen Geräten ist auch bei USV-Systemen darauf zu achten, dass sie in den vom Hersteller genannten Temperaturbereichen betrieben werden. Dies ist bei der Dimensionierung der Kühlung zu berücksichtigen.

Da die USV die letzte Bastion gegen den Stromausfall vor der IT-Hardware ist, kommt ihr große Bedeutung für die Sicherstellung der Verfügbarkeit zu. Sie hat also denselben Schutzbedarf wie die durch die USV versorgte IT. Wenn die USV-versorgten IT-Systeme redundant ausgelegt sind, sollten auch USV-Systeme redundant vorhanden sein.

Außerdem ist bei einer USV besonders auf den Schutz vor dem Zugang Unbefugter, Brand und Wasser zu achten. Ein sinnvoller Schutz gegen Brand macht es nahezu unverzichtbar, einander Redundanz bietenden USV-Einheiten in getrennten Brandabschnitten unterzubringen. Nur so kann verhindert werden, dass bei Brand einer Einheit nach kurzer Zeit auch alle anderen durch Brand ausfallen.

Um die Schutzwirkung einer USV aufrechtzuerhalten, muss sie regelmäßig gewartet werden. Dafür sind die vom Hersteller vorgesehenen Wartungsintervalle der USV einzuhalten.

**Überspannungsschutz**

In jedem elektrisch leitenden Netz, gleichgültig ob es der Energieversorgung oder der Datenübertragung dient, kann es zu jeder Zeit zu Überspannungen kommen. Überwiegend werden solche Überspannungen durch andere Stromverbraucher im gleichen Versorgungsnetz verursacht. Überspannungen durch Blitz sind dagegen zwar sehr viel seltener, haben aber ein ungleich höheres Schadenspotential.

Nicht nur über die im Haus verlegten Leitungen, sondern auch über alle elektrisch leitenden Außenanbindungen wie Telefon-, Wasser- oder Gasleitungen können Überspannungen in ein Gebäude und die dort betriebene IT gelangen. Darüber hinaus können Überspannungen auch auf interne Leitungen eingekoppelt werden.

Die erforderlichen Maßnahmen zum Schutz von IT-Geräten sind unabhängig von der Ursache der Überspannung im Wesentlichen die gleichen. Die Normenreihe zum Blitzschutz von baulichen Anlagen DIN EN 62305 "Blitzschutz" (entspricht der Normenreihe VDE 0185-305 und IEC 62305) beschreibt ein Gesamtkonzept zum Blitzschutz. Auf Basis dieser Normenreihe DIN EN 62305 ist ein Überspannungsschutzkonzept zu erstellen.

Die DIN EN 62305 beschreibt in ihrem Teil 2 "Risiko-Management" allgemeinverbindlich den Weg zu einem risikoorientierten Blitz- und Überspannungsschutz. Im Teil 3 wird der "Schutz von baulichen Anlagen und Personen" behandelt, in Teil 4 "Elektrische und elektronische Systeme in baulichen Anlagen".

Im Überspannungsschutzkonzept sind natürlich auch Netzersatzanlagen (NEA) und unterbrechungsfreie Stromversorgungen (USVen) zu berücksichtigen. Obwohl USVen einen gewissen Schutz der angeschlossenen Geräte bewirken, sind sie keinesfalls als Überspannungsschutzeinrichtung zu betrachten, sondern einzig und allein als zu schützendes elektronisches Gerät.

An die Stelle der bisherigen drei Stufen Grob-, Mittel- und Feinschutz ist das Konzept der energetischen Koordination getreten. Nach der Norm ist eine energetische Koordination zwar nur dann zwingend erforderlich, wenn es einen äußeren Blitzschutz gibt. Im Sinne der Informationssicherheit sollte die energetische Koordination auch in Fällen ohne äußeren Blitzschutz berücksichtigt werden. Vereinfacht dargestellt bedeutet das folgendes:

* Hinter jedem Schutzelement (SPD - Surge Protecting Device) darf maximal so viel durch Überspannung verursachte Energie wirken, wie alle dahinter befindlichen elektrischen Einrichtungen (inklusive der folgenden SPDs) verkraften. Ein reines Leitungsnetz ist natürlich wesentlich robuster und verträgt deutlich mehr Energie als z. B. die Schnittstelle einer Netzwerkkarte in einem Rechner .
* Alle eingesetzten SPDs müssen sich miteinander vertragen. Der Ausgang eines vorderen SPDs und der Eingang des folgenden müssen aufeinander angepasst sein. Der Nachweis der energetischen Koordination kann auf dreierlei Weise erbracht werden: 
Durch den Aufbau des Blitz- und Überspannungsschutzes werden wie Zwiebelschalen ineinander liegende Blitzschutzzonen (LPZ, Lightning Protection Zone) gebildet. Mit steigendem Schutz werden sie von außen nach innen mit LPZ 0, LPZ 1, LPZ 2 etc. bezeichnet. Dabei kann eine Zone nur dann gebildet werden, wenn es die nächst äußere gibt: So ist es nicht möglich, eine LPZ 2 zu realisieren, ohne auch die LPZ 1 zu haben.

Für einfache elektrische und elektromechanische Geräte ist die LPZ 1 meist ausreichend. Zum Schutz elektronischer Geräte (IT-Hardware, USV etc.) ist mindestens die LPZ 2 zu realisieren. Bei besonders empfindlichen Geräten, z. B. in der Medizin- oder Messtechnik kann durchaus die LPZ 3 erforderlich werden.

**Hinweis:**

Die LPZ (Blitzschutzzonen) sind nicht zu verwechseln mit den Schutzklassen des äußeren Blitzschutzsystems, das mit LPS (Lightning Protection System) bezeichnet wird.

Ob ein LPS erforderlich ist und mit welcher Schutzklasse, muss anhand der Risikobewertung (gemäß Teil 2 der DIN EN 62305) entschieden werden. Der früher ausreichende Blick in eine Gebäudeliste genügt nicht mehr!

In vielen Fällen ist der gebäudeweite Aufbau einer LPZ 2 oder LPZ 3 gar nicht erforderlich. Während der Übergang von der LPZ 0 (das ist alles außerhalb eines Gebäudes, wo der Blitz also tatsächlich direkt einschlagen kann) zur LPZ 1 tatsächlich möglichst nah an der Gebäudehülle zu erfolgen hat, kann der Aufbau höherer LPZ an beliebiger Stelle und in beliebigem Umfang erfolgen. Wichtig ist dabei aber darauf zu achten, dass keine Leitung, die nur den Schutz der LPZ 1 genießt (z. B. Heizungsrohre) durch höherwertige LPZ hindurch läuft.

Die früher notwendigen Mindestleitungslängen zwischen den SPDs, also den Schutzelementen, und der unterschiedlichen LPZ sind heute nicht mehr zwingend. Es gibt SPDs, die in einem Bauteil den Übergang von der LPZ 0 direkt in die LPZ 2 realisieren.

Die Schutzwirkung eines SPDs reicht nach beiden Seiten (auf die kommende und die gehende Leitung) nur über eine bestimmte Kabelstrecke, die im Einzelnen vom Hersteller zu benennen ist. Wird die Kabellänge abgehend überschritten, sind wiederholt SPDs einzubauen, um den Schutz aufrecht zu erhalten.

Nach DIN EN 62305 müssen Blitzschutzsysteme (LPS) abhängig von der Schutzklasse in Abständen von ein bis vier Jahren überprüft werden. Für die Überspannungsschutzeinrichtungen sieht die Norm keine ausdrücklichen Prüfintervalle vor. Im Sinne der Informationssicherheit sollten aber alle SPDs periodisch (mindestens einmal pro Jahr) und nach bekannten Ereignissen geprüft und gegebenenfalls ersetzt werden. Um diese Prüfung überhaupt durchführen zu können, sollten, sofern verfügbar, ausschließlich solche SPDs eingebaut werden, die eine integrierte Defektanzeige oder (noch besser) eine Lebensdaueranzeige besitzen.

Neben dem Überspannungsschutz auf allen elektrisch leitenden Systemen müssen in Serverräumen und den Kerneinheiten eines Rechenzentrums Maßnahmen gegen elektrostatische Aufladung getroffen werden. Der Durchgangswiderstand der Bodenbeläge in solchen Räumen muss zwischen 10 und 100 Megaohm liegen. Die Einstufung nach DIN-Vorschrift 4102-1 "Brandverhalten von Baustoffen und Bauteilen" muss mindestens "B1 schwer entflammbar" erreichen. Dies gilt auch für einen Doppelboden oder Installationsboden.

Unabhängig von Umfang und Ausbau des Überspannungsschutzes ist zu beachten, dass ein umfassender Potentialausgleich aller in den Überspannungsschutz einbezogenen elektrischen Betriebsmittel erforderlich ist! Die Mehrzahl der Schäden an IT-Geräten durch Überspannungen ist auf nicht konsequent umgesetzten Potentialausgleich zurückzuführen.

#### SYS.1.1.M16 Sichere Installation und Grundkonfiguration von Servern

Nachdem die Planung eines neuen Servers abgeschlossen und eine Sicherheitsrichtlinie erstellt wurde, kann mit der Installation des Servers begonnen werden.

Die Installation des Systems sollte nur von autorisierten Personen (Administratoren oder vertraglich gebundene Dienstleister) durchgeführt werden. Administratoren für IT-Systeme und deren Vertreter müssen sorgfältig ausgewählt werden. Sie müssen regelmäßig darüber belehrt werden, dass die Befugnisse nur für die erforderlichen Administrationsaufgaben verwendet werden dürfen. Da Administratoren hinsichtlich der Funktionsfähigkeit der eingesetzten Hard- und Software eine Schlüsselrolle innehaben, muss auch beim Ausfall von Administratoren die Weiterführung der Tätigkeiten gewährleistet sein. Hierzu müssen die benannten Vertreter über den aktuellen Stand der Systemkonfiguration verfügen sowie Zugriff auf die für die Administration benötigten Passwörter, Schlüssel und Sicherheitstoken haben. Vertiefende Informationen hierzu sind in ORP.4 Identitäts- und Berechtigungsmanagement zu finden.

Es ist empfehlenswert, zunächst ein kurzes Installationskonzept entsprechend den funktionalen Anforderungen aus der Planung und den Vorgaben der Sicherheitsrichtlinie zu erstellen. Prinzipiell ist es vorteilhaft, die Installation in zwei Phasen vorzunehmen: Zunächst wird ein Grundsystem installiert und konfiguriert, anschließend werden die weiteren benötigten Dienste und Anwendungen eingerichtet. Die Installationsprogramme der meisten Betriebssysteme unterstützen diese Vorgehensweise mehr oder weniger gut.

Die beschriebenen Schritte brauchen nicht notwendigerweise alle für jeden Server erneut durchgeführt zu werden. Dies könnte sogar insofern kontraproduktiv sein, als die ständige Wiederholung die Gefahr von Fehlern erhöht. Es wird daher empfohlen, die beschriebenen Schritte einmal besonders sorgfältig auf einem Referenz-System durchzuführen, die nötigen Konfigurationen genau zu dokumentieren und so ein angepasstes Installationskonzept für das betreffende Betriebssystem zu erhalten. Dabei muss beachtet werden, dass dieses Installationskonzept auch bei Änderungen am Betriebssystem, die kein komplett neues Release darstellen (Service-Packs, Update-Releases oder ähnliches) überprüft und gegebenenfalls angepasst werden muss.

Bei virtuellen Server wird in den seltensten Fällen für jede Instanz ein abgeändertes Betriebssystem installiert, hier wird in der Regel ein Grundsystem erstellt, dass in die Instanz kopiert und als eigenständiger Klon gestartet wird. In dieser Instanz werden im nächsten Schritt die benötigten Serverdienste oder Anwendungsprogramme installiert und zu jedem späteren Zeitpunkt kann ein neuer Klon generiert werden, um beispielsweise mehrere Instanzen mit identischen Serverdiensten oder Anwendungsprogrammen zu erhalten. Damit können sich aber auch Fehlentscheidungen und falsche Einstellungen, die bei der Erstellung des Grundsystems getroffen wurden, bei der Installation der Klone auf zahlreiche weitere Instanzen vererben. Für jeden einzelnen Klon sollten daher alle Empfehlungen dieser Maßnahme ebenfalls sorgfältig umgesetzt werden.

**Installation**

Diese Maßnahme beinhaltet nur Empfehlungen für die ersten Schritte einer Installation und nicht für die endgültige Konfiguration für den geplanten Einsatzzweck. Die weitergehenden Konfigurationsschritte sind sehr stark vom jeweiligen System und Einsatzgebiet abhängig und werden in eigenen Maßnahmen in den Betriebssystem-Bausteinen behandelt.

Während der Installation und der späteren Konfiguration sollten zumindest die wichtigen Schritte so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Beispielsweise kann eine Checkliste für die Installation erstellt werden, auf der durchgeführte Schritte abgehakt und vorgenommene Einstellungen vermerkt werden können. Eine entsprechende Dokumentation ist für eine Fehleranalyse oder spätere Neuinstallation hilfreich. Dabei sollte beachtet werden, dass neben dem Autor auch weitere, auf diesem Gebiet eventuell weniger spezialisierte, Administratoren auf die Dokumentation zurückgreifen müssen. Daher ist es wichtig, dass die Dokumentation gut strukturiert und verständlich ist.

Wird der Server von Datenträgern wie DVDs oder anderen Speichermedien installiert, wird empfohlen, die Installation und Grundkonfiguration offline oder zumindest in einem sicheren Netz (Installations- oder Administrationsnetz) durchzuführen. Generell sollte verhindert werden, dass andere IT-Systeme während der Installation auf das zu installierende IT-System zugreifen können. Dies ist wichtig, weil während der Installation meist noch keine Passwörter vergeben und keine Schutzmechanismen aktiv sind, aber eventuell schon Zugänge möglich sind. Falls die Installation mehrerer IT-Systeme teilweise über das Netz erfolgen soll (beispielsweise Nachladen von Paketen), so wird empfohlen, einen Installationsserver im Administrationsnetz zu nutzen.

Insbesondere beim Betriebssystem selbst ist es wichtig, dass die installierte Version aus einer vertrauenswürdigen Quelle stammt. Dies ist besonders wichtig, wenn beispielsweise CD -Images aus dem Internet heruntergeladen wurden. In diesem Fall sollte unbedingt geprüft werden, ob digitale Signaturen der Pakete verfügbar sind, die zur Verifikation von Integrität und Authentizität der Pakete verwendet werden können. Pakete und CD-Images, für die keine digitalen Signaturen oder wenigstens Prüfsummen existieren, sollten möglichst nicht eingesetzt werden.

Bei der Einrichtung der Festplattenpartitionen muss das in der Planungsphase erstellte Konzept umgesetzt werden. Wenn ein verschlüsseltes Dateisystem eingesetzt werden soll, so muss es meist initialisiert werden, bevor Daten hineinkopiert werden können, denn oft lässt sich ein Dateisystem nicht im Nachhinein verschlüsseln. Auch einige RAID-Systeme und -Level erfordern eine Konfiguration, die abgeschlossen sein muss, bevor die betreffenden Dateisysteme eingerichtet werden können.

Sofern dies nicht bereits automatisch geschehen ist, sollte spätestens beim Abschluss der Grundinstallation auch die Protokollierung der Systemereignisse aktiviert werden. Die Protokolldaten können bei Problemen bei der weiteren Installation und Konfiguration wertvolle Informationen liefern.

**Aktualisierung**

Wird das System von einer CD, DVD oder einem anderen "Offline-Medium" installiert, so sollte nach der Grundinstallation überprüft werden, ob zwischenzeitlich Aktualisierungen oder Sicherheitspatches vom Hersteller oder Distributor veröffentlicht wurden.

**Installation der jeweiligen Serverdienste und Anwendungsprogramme**

Nachdem das Betriebssystem installiert und Grundkonfiguration und Aktualisierung abgeschlossen wurde, können die jeweiligen Serverdienste installiert und konfiguriert werden. Sowohl auf Clients als auch Servern werden in der Regel Serverdienste zur Fernadministration benötigt. Bei Servern kommen die eigentlichen Serverdienste hinzu, bei Clients müssen in der Regel grafische Benutzeroberflächen und Anwendungsprogramme installiert und eingerichtet werden. Hierfür wird ein analoges Vorgehen wie für das Betriebssystem selbst empfohlen. Außerdem wird empfohlen, das Betriebssystem zu härten.

#### SYS.1.1.M17 Einsatzfreigabe

Bevor das Serversystems im produktiven Betrieb eingesetzt und bevor es an ein produktives Netz angeschlossen wird, sollte eine Einsatzfreigabe durchgeführt werden, diese ist zu dokumentieren. Die Einsatzfreigabe basiert auf einer Prüfung der Installations- und Konfigurationsdokumentation und der Funktionsfähigkeit des Systems in einem Test. Sie erfolgt durch eine in der Institution dafür autorisierte Stelle.

Vertiefende Informationen hierzu sind in OPS.1.1.7 Softwaretests- und Freigaben zu finden.

Bei erhöhtem Schutzbedarf sollte überlegt werden, einen internen Penetrationstest durchzuführen (siehe DER.3.3 Penetrationstest). 

Falls festgestellt wird, dass ein Sicherheitsupdate oder Patch mit einer anderen wichtigen Komponente oder einem Programm inkompatibel ist oder Probleme verursacht, so muss sorgfältig überlegt werden, wie weiter vorgegangen wird. Wird entschieden, dass auf Grund der aufgetretenen Probleme ein Patch nicht installiert wird, so ist diese Entscheidung auf jeden Fall zu dokumentieren. Außerdem muss in diesem Fall klar beschrieben sein, welche Maßnahmen ersatzweise ergriffen wurden, um ein Ausnutzen der Schwachstelle zu verhindern. Eine solche Entscheidung darf nicht von den Administratoren alleine getroffen werden, sondern sie muss mit den Vorgesetzten und dem ISB abgestimmt sein.

#### SYS.1.1.M18 Verschlüsselung der Kommunikationsverbindungen

Wenn möglich, sollte die Netzkommunikation von oder zu einem Server verschlüsselt werden. Die Verschlüsselung ist abhängig von dem Dienst, den der Server bereitstellt, vertiefende Informationen zu den jeweiligen Netzdiensten sind in APP.3 Netzbasierte Dienste zu finden. Eine der am verbreitetsten Möglichkeiten, Netzdienste zu verschlüsseln, ist der Einsatz von TLS.

Transport Layer Security (TLS) ist eine Weiterentwicklung von Secure Sockets Layer (SSL) und wird dazu verwendet, Informationen während der Übertragung in Netzen, in der Regel zwischen Serverdiensten und Clients oder zwischen Serverdiensten untereinander kryptographisch abzusichern. Clients können die Verschlüsselung über SSL/TLS nur dann nutzen, wenn diese von den Serverdiensten unterstützt wird. SSL/TLS kann dazu eingesetzt werden, Informationen aus der Anwendungsschicht ( z. B. HTTP, LDAP, POP3, IMAP und SMTP) verschlüsselt über TCP/IP zu übertragen. Überdies können mittels SSL/TLS auch sichere VPNs (Virtuelle Private Netze) aufgebaut werden. Mit OpenVPN, einer unter der GNU GPL (General Public License) frei verfügbaren Software, können VPNs mittels SSL/TLS verschlüsselte Verbindungen realisiert werden. Vertiefende Informationen zu VPNs sind in Baustein NET.3.3 Virtual Private Networks (VPN) zu finden.

In der Regel ist es bei vielen Serverdiensten nur ein geringer Mehraufwand, diese so zu konfigurieren, dass eine SSL/TLS-Verschlüsselung unterstützt wird, oder so, dass diese für einen Informationsaustausch ausschließlich genutzt wird. Daher ist für alle Serverdienste zu prüfen, ob mit vertretbarem Aufwand eine Verschlüsselung über SSL/TLS möglich und praktikabel ist. Ist dies mit vertretbarem Aufwand möglich, sollte die SSL/TLS-Verschlüsselung aktiviert werden. Generell sollte der interne und externe Nachrichtenstrom von und zu LDAP-, E-Mail- und Webservern mit SSL/TLS verschlüsselt werden.

**Auswahl einer vertrauenswürdigen Zertifizierungsstelle**

Zu Beginn eines neuen mit SSL/TLS abgesicherten Kommunikationsaufbaus findet ein sogenannter Handshake zwischen Client und Server statt. Hierbei verständigen sich Client und Server über die kryptographischen Algorithmen, die für Schlüsselaustausch, Verschlüsselung und Integritätssicherung eingesetzt werden. Außerdem einigen sich Client und Server über die SSL-Version, die verwendet wird. Zusätzlich dazu sendet der Server sein X.509-Zertifikat an den Client. Optional kann der Server auch so konfiguriert werden, dass auch der Client aufgefordert wird, dem Server sein X.509-Zertifikat zu übermitteln.

Die Identität der Kommunikationspartner wird hierbei über diese Zertifikate geprüft. X.509-Zertifikate enthalten die öffentlichen Schlüssel sowie eine Bestätigung einer weiteren Instanz, der Zertifizierungsstelle oder auch Trustcenter oder Certificate Authority (CA) genannt, über die korrekte Zuordnung des öffentlichen Schlüssels zu dessen "Besitzer". Der Wert eines Zertifikates hängt davon ab, welche Felder des X.509-Zertifikats von der Zertifizierungsstelle geprüft werden, bevor das Zertifikat ausgestellt wird, und wie vertrauenswürdig die Zertifizierungsstelle selbst ist. Daher spielt die Auswahl einer vertrauenswürdigen Zertifizierungsstelle eine wichtige Rolle.

Aufgrund der Vielzahl von Zertifizierungsstellen auf dem Markt sollte eine Institution die Zertifizierungsstelle sorgfältig auswählen. Es ist ratsam, die für den späteren Betrieb wesentlichen Auswahlkriterien im Vorfeld festzulegen. Zu diesen können beispielsweise gehören:

* ob das Root-Zertifikat schon in CA-Listen der Clients, wie dem Browser, enthalten ist,
* wo sich Sitz und Rechtsstand der Zertifizierungsstelle befinden, und auch wo der Sitz des technischen Betriebs sich befindet,
* was die geschäftliche Ausrichtung der Zertifizierungsstelle ist (Ist CA-Betrieb ein zentrales Geschäftsfeld?), was die angebotenen CA-Dienste umfassen (z. B. OSCP, CRL),
* welches Sicherheitsniveau die Zertifizierungsstelle nachweisen kann,
* wie gut Umfang und Qualität des technischen Supports sind sowie,
* wie hoch die Zertifikatskosten sind.
Grundsätzlich sollten die Kosten eines Zertifikats jedoch keinesfalls das allein ausschlaggebende Kriterium darstellen. Wird der angebotene Serverdienst von einem beschränkten Benutzerkreis verwendet, z. B. nur innerhalb eines LAN s, kann ein Zertifikat auch ohne die Beteiligung einer Zertifizierungsstelle selbst erstellt und signiert und auf alle Clients eingespielt werden, auf denen der Serverdienst genutzt werden soll.

**Extended Validation Zertifikate**

Um Angriffe mit gefälschten Webseiten zu erschweren und der Problematik entgegen zu wirken, dass diverse Zertifizierungsstellen SSL/TLS-Anträge nicht immer zuverlässig prüfen, wurden Extended Validation Zertifikate zum Umgang mit Zertifikaten mit höheren Sicherheitsanforderungen eingeführt. Diese sollen verhindern, dass, wenn ein Zertifikat ausgestellt wird, eine CA nur den Domainnamen prüft. Darüber hinaus soll die CA außerdem noch eindeutig nachvollziehen, von wem die betreffende Domain registriert wurde. Im Unterschied zu den normalen X.509 SSL/TLS-Zertifikaten wird bei diesen erweiterten Zertifikaten (Extended Validation SSL-Zertifikate, EV-SSL) die Identität des Antragstellers ausführlicher überprüft. Hierbei verpflichten sich die beteiligten Zertifizierungsstellen und Browser-Hersteller, die "Guidelines for the Issuance and Management of Extended Validation Certificates" des CA/Browser Forums einzuhalten. Danach sind unter anderem folgende Kriterien vom Antragsteller zu erfüllen:

* Identitätsnachweis und Adresse des Antragstellers,
* Nachweis, dass der Antragsteller alleiniger Eigentümer der Domain ist,
* Bestätigung, dass die antragstellende Person überhaupt berechtigt ist, den Antrag zu stellen und
* Nennung einer Hauptkontaktperson.
Zusätzlich darf der Antragsteller oder die antragstellende Person auf keiner Liste mit verbotenen Organisationen oder Personen stehen. Außerdem darf das Land, in dem sich der Sitz oder der Rechtsstand des Antragstellers befindet, weder Handelsembargos oder irgendwelchen anderen Sanktionen ausgesetzt sein, die durch dasjenige Land verhängt wurden, dessen Gesetzgebung die Zertifizierungsstelle unterliegt.

Für die Anwender sind EV-SSL-Zertifikate daran zu erkennen, dass in den unterstützten Browsern bestimmte Bereiche, wie die URL im Adressfeld oder das von vielen Browsern verwendete Vorhängeschlosssymbol, das eine verschlüsselte Seite kennzeichnet, grün hinterlegt ist. Je nach Konfiguration des Sicherheitsgateways (Firewall), hinter dem die Benutzer auf Webseiten mit EV-SSL-Zertifikaten zugreifen, kann es aber vorkommen, dass diese Markierungen in den Browsern der Clients nicht angezeigt werden. Wird beispielsweise der Nachrichtenfluss zwischen Client und Webserver von einem Proxy ent- und wieder neu verschlüsselt, wird im Browser lediglich das SSL/TLS-Zertifikat des Sicherheitsgateways angezeigt.

Neben den höheren finanziellen Kosten, die für die Ausstellung eines EV-SSL-Zertifikats entstehen können, dauert die Antragstellung in der Regel auch länger, da zusätzliche Informationen von der Zertifizierungsstelle überprüft werden. Wenn es möglich ist, wird empfohlen, diesen zusätzlichen Aufwand in Kauf zu nehmen. Insbesondere in Bereichen, in denen Informationen mit höherem Schutzbedarf bezüglich Vertraulichkeit und Integrität übertragen werden, sollten EV-SSL-Zertifikate bevorzugt eingesetzt werden.

**Common Name Eintrag**

Browser zeigen immer eine Sicherheitswarnung an, wenn der im Zertifikat einer Webseite eingetragene Common Name (Allgemeiner Name) nicht mit dem vollständigen DNS-Name (Fully Qualified Domain Name) übereinstimmt, über den der Server im Web erreichbar ist. Daher sollte sichergestellt sein, dass der Common Name zu der URL passt, die tatsächlich verwendet wird, um mit dem Server zu kommunizieren. Wenn es möglich ist, sollten Wildcard-Zertifikate (z. B. *.example.de) vermieden werden. Diese werden häufig eingesetzt, um mit einem einzelnen Zertifikat mehrere Subdomains abzusichern.

**Vollständige Zertifikatskette**

Da für die Prüfung der hierarchischen Zertifikatskette durch den Browser auch alle Zwischen-Zertifikate benötigt werden, reicht das SSL-Zertifikat des Servers alleine nicht aus. Deshalb sollte der Server so konfiguriert werden, dass beim Verbindungsaufbau alle erforderlichen Zertifikate an den Client gesendet werden. Dazu sollte die Zertifikatskette im Webserver entsprechend hinterlegt werden.

Zu beachten ist außerdem, dass neben Zertifikate, die fehlen, auch abgelaufene oder gesperrte Zertifikate die Prüfung der Zertifikatskette fehlschlagen lassen. Nur wenn alle Zertifikate gültig sind und beim Verbindungsaufbau übertragen wurden, kann die Zertifikatskette erfolgreich geprüft werden.

**Auswahl einer SSL/TLS Protokollversion**

Derzeit existieren fünf SSL/TLS-Protokollversionen: SSL v2, SSL v3, TLS v1.0, TLS v1.1 und TLS v1.2. SSL v1 wurde nicht veröffentlicht. Um eine sichere Verbindung zwischen Client und Server zu gewährleisten, sollte TLS 1.2 verwendet werden. TLS 1.1 bietet ausreichende Sicherheit, aber im Vergleich zu TLS 1.2 weist es jedoch einige Schwächen auf, z. B. sind in TLS 1.1 noch Cipher-Suites vorhanden, die auf IDEA und DES basieren, in TLS 1.2 nicht mehr. TLS 1.0 kann in bestehenden Anwendungen übergangsweise weiter eingesetzt werden, falls eine sofortige Migration zu TLS 1.1 oder vorzugsweise TLS 1.2 nicht möglich ist und geeignete Maßnahmen gegen Chosen-Plaintext-Angriffe ( z. B. BEAST) auf die CBC-Implementierung getroffen werden. Generell sollte jedoch eine Migration zu TLS 1.2 schnellstmöglich erfolgen. SSL v2 und SSL v3 dürfen nicht mehr eingesetzt werden. Siehe hierzu auch den BSI-Migrationsleitfaden zum Mindeststandard TLS 1.2.

**Sichere Cipher-Suites**

SSL/TLS nutzt Cipher-Suites, die bestimmen, wie sicher eine HTTPS -Verbindung ist. Jede Suite besteht aus spezifischen Modulen. Wenn ein bestimmtes Modul als unsicher oder schwach eingestuft wird, kann durch die Veränderung der Cipher Suite zu einem sichereren Modul gewechselt werden.

Da die Verwendung schwacher Cipher Suites clientseitig erzwungen werden kann, ist es erforderlich, serverseitig nur solche anzubieten, die Authentisierung und Verschlüsselung mit einer ausreichenden Stärke einsetzen. Darüber hinaus sollten die verwendeten Cipher-Suites Perfect Forward Secrecy (PFS) unterstützen. Weitere Hinweise zu kryptographischen Algorithmen und Schlüssellängen sind in der Technischen Richtlinie des BSI "Kryptographische Verfahren: Empfehlungen und Schlüssellängen - Teil 2 Verwendung von TLS" (TR-02102-2) und in CON.1 Kryptokonzept enthalten.

**Session Renegotiation/TLS-Kompression**

Mittels der sogenannten Session Renegotiation (Session-Neuverhandlung) können sowohl Client als auch Server die Parameter einer bestehenden HTTPS-Sitzung neu aushandeln. Aufgrund eines Fehlers in der Spezifikation des TLS-Protokolls (RFC 5246) ist es einem Man-in-the-Middle-Angreifer möglich, die Session Renegotiation zu missbrauchen, um beliebige Inhalte in eine existierende HTTPS-Sitzung einzufügen. Mittlerweile wurde das TLS-Protokoll erweitert (RFC 5746) und dieser Designfehler behoben. Generell sollte überlegt werden, ob serverseitig die Session Renegotiation erforderlich ist. Ist dies der Fall, dann sollte diese sicher konfiguriert werden, also auf Basis des RFC 5746. Eine Renegotiation, die durch den Client initiiert wird, sollte vom Server abgelehnt werden.

Darüber hinaus sollte die TLS-Kompression deaktiviert werden.

**Webserverspezifische Aspekte**

Generell wird empfohlen, die auf Webservern zur Verfügung gestellten Inhalte bei der Übertragung vom Server zum Client und umgekehrt mittels SSL/TLS zu schützen.

Wenn möglich, sollte darauf verzichtet werden, Webseiten mit gemischten Inhalten anzubieten. Als Webseite mit gemischtem Inhalt wird eine Seite bezeichnet, die zwar Verschlüsselung nutzt, dabei aber auch unverschlüsselte Inhalte ( z. B. JavaScript-, CSS-Dateien oder Bilder) einbindet. Ein Man-in-the-Middle-Angreifer kann die Übertragung einer einzelnen unverschlüsselten Datei ausnutzen, um eine HTTPS-Session zu übernehmen. Da Webseiten mit gemischten Inhalten zudem üblicherweise Browser-Warnungen erzeugen, wird dadurch die Benutzerfreundlichkeit verschlechtert.

HTTP Strict Transport Security (HSTS) ist eine weitere Methode, die gegen bekannte Schwächen von SSL schützt. Damit wird erschwert, dass ein Besucher durch einen Angriff oder serverseitige Konfigurationsprobleme von einer gesicherten auf eine ungesicherte Seite umgeleitet wird. Befindet sich ein Angreifer beispielsweise in demselben WLAN wie das Opfer, könnte er so die Session Cookies mitlesen und die HTTPS-Session übernehmen. Um HSTS zu aktivieren, muss der HSTS-Header auf dem Server konfiguriert werden.

**Schutz des privaten Serverschlüssels**

Ein besonders wichtiger Sicherheitsaspekt beim Einsatz von SSL/TLS ist der Schutz des privaten Serverschlüssels. Daher ist es ratsam, den Server so zu konfigurieren, dass der private Serverschlüssel beim Start des Servers durch Passworteingabe freigegeben werden muss. Besteht der Verdacht, dass der private Schlüssel kompromittiert wurde, so muss das zugrunde liegende Zertifikat widerrufen werden. 

**Validierung**

Die Auswirkungen von Konfigurationsänderungen auf dem Server lassen sich nicht immer mit Bestimmtheit vorhersagen. Auch Software Updates können mitunter zu überraschenden Änderungen führen. Es wird daher empfohlen, die SSL/TLS Konfiguration vor der Freigabe zur Nutzung auf Fehler zu prüfen und den Status in periodischen Abständen (regelmäßig) zu validieren.

#### SYS.1.1.M19 Einrichtung lokaler Paketfilter

Das gesamte Netz einer Institution sollte durch ein entsprechendes Sicherheitsgateway geschützt sein. Server, die Dienste nach außen hin anbieten, sollten in einer Demilitarisierten Zone ( DMZ) aufgestellt werden. Trotzdem ist es empfehlenswert, auch auf jedem Rechner entsprechende Zugangsbeschränkungen auf Anwendungs- oder Netzebene einzurichten. Dies gilt auch für Server, die nur intern genutzt werden und nicht zuletzt auch für Clients.

Ein lokaler Paketfilter kann einen Rechner gegen Angriffe schützen, die aus dem selben Subnetz heraus gestartet werden. Außerdem kann ein solcher Paketfilter dazu benutzt werden, eine feiner abgestufte Zugangskontrolle für einzelne Dienste zu realisieren, als dies beispielsweise mit Paketfiltern nur an Netzübergängen möglich ist.

Darüber hinaus kann ein lokaler Paketfilter auch dazu benutzt werden, ausgehende Netzverbindungen zu beschränken und so die Folgen einer Kompromittierung des Systems zu begrenzen. Ein solcher Schutz kann zwar eventuell von einem Angreifer nach einer erfolgreichen Kompromittierung des Rechners deaktiviert werden, andererseits wird ein Angreifer auf diese Weise zumindest behindert. Auf diese Weise kann entscheidende Zeit bei der Entdeckung und für mögliche Reaktionen gewonnen werden.

Zuletzt kann die Protokollfunktion eines lokalen Paketfilters es ermöglichen, bestimmte Angriffe überhaupt zu entdecken.

Praktisch alle aktuellen Betriebssysteme bieten die Möglichkeit, Filter zu definieren, die alle empfangenen oder zu sendenden Pakete nach bestimmten Regeln untersuchen und behandeln. Die Filtermöglichkeiten unterscheiden sich dabei zwischen den einzelnen Betriebssystemen teilweise erheblich. Praktisch immer können jedoch Regeln basierend auf der Quell- und Zieladresse des Pakets sowie auf dem verwendeten Protokolltyp (TCP/IP, UDP/IP, ICMP etc.) sowie gegebenenfalls dem Quell- oder Zielport definiert werden. Mit Hilfe von Paketfilterregeln können so beispielsweise Pakete, die von bestimmten Rechnern oder aus bestimmten Subnetzen stammen, gezielt verworfen werden.

Manche Serveranwendungen besitzen eigene Mechanismen, um den Zugang auf den Dienst für einzelne IP-Adressen oder Adressbereiche zu erlauben oder zu verbieten. Gegenüber diesen Mechanismen hat ein lokaler Paketfilter auf Betriebssystemebene den Vorteil, dass er den Dienst selbst gegen mögliche Angriffe schützt, die zu einer Kompromittierung führen, bevor die eingebaute Zugangsbeschränkung überhaupt wirksam werden kann.

Prinzipiell sollten alle Server mit hohem Schutzbedarf mit einem lokalen Paketfilter geschützt werden.

Es gibt zwei allgemeine Strategien, mit der Paketfilter-Regeln implementiert werden können: Die Blacklist-Strategie erlaubt alle Arten von Verbindungen, die nicht bestimmte Ausschlusskriterien erfüllen (Freizügige Strategie: "Alles ist erlaubt, was nicht explizit verboten ist"). Der Vorteil liegt dabei in einem eventuell geringeren Aufwand bei der Administration und der Fehlersuche. Ein schwerwiegender Nachteil ist jedoch, dass vergessene Regeln, die den Zugang auf nicht geschützte Netzdienste ermöglichen, als Grundlage für einen Angriff dienen können.

Demgegenüber werden bei der Whitelist-Strategie alle Arten von Verbindungen blockiert, die nicht zu einer Liste erlaubter Dienste gehören (Restriktive Strategie: "Alles ist verboten, was nicht explizit erlaubt ist").

Die Whitelist-Strategie bietet die größere Sicherheit und sollte daher grundsätzlich verwendet werden, wenn nicht wichtige Gründe dagegen sprechen. Der Nachteil liegt in einem tendenziell höheren Administrationsaufwand, da bei jeder Änderung der Anforderungen neue Regeln definiert werden müssen. In Ausnahmefällen, beispielsweise wenn ein Protokoll nicht auf fest definierten Ports arbeitet, kann auf die Blacklist-Strategie zurückgegriffen werden.

Es ist empfehlenswert, auf allen Servern im Rahmen der Grundkonfiguration einen lokalen Paketfilter mit einem Basis-Regelwerk einzurichten, bei dem grundsätzlich alle Verbindungsanfragen von außen abgewiesen werden. Dieses Regelwerk sollte aktiv sein, wenn das System ans Netz angeschlossen wird. Je nachdem welche Dienste von dem System angeboten werden sollen, können nach deren Konfiguration die dafür benötigten Protokolle und Ports freigeschaltet werden. Auch für Clients sollte dieses Vorgehen zumindest dann in Betracht gezogen werden, wenn diese besondere Anforderungen an die Sicherheit stellen.

Paketfilter erlauben meist ein detailliertes Protokollieren des Netzverkehrs. Das Aufsetzen eines lokalen Paketfilters ist daher auch in sicheren Netzen, die mit einem Sicherheitsgateway von einem unsicheren Netz wie dem Internet getrennt sind, sinnvoll, denn gewonnene Informationen können für die Erkennung von Angriffen hilfreich sein. Allerdings muss dabei darauf geachtet werden, dass keine Datenschutzbestimmungen verletzt werden. Gegebenenfalls sollten die entsprechenden Stellen (Datenschutzbeauftragter, Personalvertretung oder andere) beteiligt werden.

**Problem ICMP**

Das Internet Control Message Protocol ICMP wird dazu verwendet, Nachrichten über Fehler bei der Übertragung von IP-Paketen zu übermitteln. Beispielsweise existieren Nachrichten, die dem Sender eines Pakets mitteilen, dass das Zielnetz nicht erreichbar ist oder dass das Paket zu groß war, um an das Zielsystem weitergeleitet zu werden. Die Funktion der Tools ping und traceroute beruhen ebenfalls auf ICMP.

Neben vielen nützlichen Eigenschaften gibt es jedoch einige ICMP-Nachrichtentypen, mit denen Angreifer sich wichtige Informationen über ein Netz verschaffen und diese direkt für Angriffe benutzen können. Leider ist der radikale Ansatz, ICMP grundsätzlich am Sicherheitsgateway zu blockieren, ebenfalls keine befriedigende Lösung, da bestimmte Funktionen dann nicht mehr verfügbar sind. Auf ping und traceroute kann zwar in der Regel auf normalen Arbeitsplatzrechnern und Servern verzichtet werden, eine globale Blockierung von ICMP kann aber zu Beeinträchtigungen führen, die schwer zu diagnostizieren sind. Daher sollte überlegt werden sowohl am Sicherheitsgateway, als auch beim lokalen Paketfilter eine selektive ICMP-Filterung vorzunehmen, sofern dieser die entsprechenden Möglichkeiten zur Verfügung stellt. Dies sollte stets unter der Berücksichtigung des Einsatzzweckes des Rechners (Server oder Arbeitsplatzrechner), dessen Schutzbedarfs und die am Sicherheitsgateway getroffenen Maßnahmen geschehen. Beispielsweise kann für das interne Netz eine größere Zahl von Nachrichtentypen zugelassen werden, als für das externe Netz.

**Umsetzung und Überprüfung**

Welche Möglichkeiten der Filterung und Protokollierung zur Verfügung stehen, unterscheidet sich je nach Betriebssystem. Vor dem Aufsetzen eines lokalen Paketfilters sollte die vorhandene Dokumentation zu Rate gezogen werden.

Bei der Einrichtung von Paketfilterregeln sollte mit großer Sorgfalt vorgegangen werden, da ein Fehler in einer Regel unter Umständen dazu führen kann, dass sich ein Administrator, der über das Netz auf dem Rechner arbeitet, auf diese Weise "aussperrt" und die Korrekturen von der Systemkonsole aus vornehmen muss.

Nach dem Aktivieren des lokalen Paketfilters sollte einerseits geprüft werden, ob die benötigten Dienste noch erreichbar sind, andererseits sollte mit einem Portscan überprüft werden, ob die restlichen Ports alle blockiert sind.

#### SYS.1.1.M20 Beschränkung des Zugangs über Netze

Der Einsatz eines Sicherheitsgateways und eine geeignete Netzsegmentierung verringern die Angriffsfläche eines Servers. Diese Empfehlungen können aber nicht direkt auf einen Server umgesetzt, sondern müssen schon während der Netzplanung berücksichtigt werden. Vertiefende Informationen sind im NET1.1 Netzarchitektur und -design zu finden. 

#### SYS.1.1.M21 Betriebsdokumentation

Um einen reibungslosen Betriebsablauf zu gewährleisten, müssen Administratoren einen Überblick über das System haben bzw. sich verschaffen können. Dieses muss auch für deren Vertreter möglich sein, falls ein Administrator unvorhergesehen ausfällt. Der Überblick ist auch Voraussetzung, um Prüfungen des Systems (z. B. auf problematische Einstellungen, Konsistenz bei Änderungen) durchführen zu können.

Daher sollten die Veränderungen, die Administratoren am System vornehmen, dokumentiert werden, nach Möglichkeit automatisiert. Dieses gilt insbesondere für Änderungen an Systemverzeichnissen und -dateien.

Bei Installation neuer Betriebssysteme oder bei Updates sind die vorgenommenen Änderungen besonders sorgfältig zu dokumentieren. Durch die Aktivierung neuer oder durch die Änderung bestehender Systemparameter kann das Verhalten eines IT-Systems (insbesondere auch Sicherheitsfunktionen) maßgeblich verändert werden.

#### SYS.1.1.M22 Einbindung in die Notfallplanung

Der teilweise oder komplette Ausfall eines Servers kann gravierende Auswirkungen haben, wenn der Server wesentlicher Bestandteil innerbetrieblicher Arbeitsabläufe ist oder ein öffentlich zugängliches Angebot unterstützt (etwa in E-Commerce- oder E-Government-Anwendungen).

Im Rahmen der Notfallvorsorge ist daher ein Konzept zu entwerfen, wie die Folgen eines Ausfalls minimiert werden können und welche Aktivitäten im Falle eines Ausfalls durchzuführen sind.

Folgende Aspekte müssen dabei berücksichtigt werden:

* Die Notfallplanung für den Server muss in den existierenden Notfallplan integriert werden (siehe auch Baustein DER.4 Notfallmanagement).
* Durch einen Systemausfall kann es auch zu Datenverlusten kommen. Daher ist im Rahmen des allgemeinen Datensicherungskonzepts (siehe auch OPS.1.1.5 Datensicherung) ein Datensicherungskonzept für den Server zu erstellen. Darin muss nicht nur der Server selbst berücksichtigt werden, sondern auch die Systeme, von denen der Betrieb des Servers abhängt bzw. für die der Betrieb des Servers notwendig ist.
* Im Rahmen von Wartungs- und Serviceverträgen oder durch eigene Lagerhaltung muss die Versorgung mit Ersatzteilen innerhalb einer Frist sichergestellt werden. Die Ausfallzeit ist daher auf ein tragbares Maß zu reduzieren. Bei besonderen Anforderungen an die Verfügbarkeit des Servers muss gegebenenfalls eine Hochverfügbarkeitslösung eingesetzt werden.
* Die Systemkonfiguration muss dokumentiert werden. Wichtige Aufgaben müssen so beschrieben sein, dass das Gesamtsystem im Notfall auch ohne vorherige Kenntnis dieser Systemkonfiguration wiederhergestellt werden kann. Die Dokumentation sollte keinesfalls ausschließlich elektronisch vorliegen, sondern Handlungsanweisungen sollten auch in Papierform existieren. Gegebenenfalls können Konfigurationsdateien auch auf externe Datenträger geeignet hinterlegt werden.
* Es muss ein Wiederanlaufplan erstellt werden, der das geregelte Hochfahren des Systems gewährleistet. Hierzu sollte im Vorfeld ein Bootmedium erstellt werden, siehe Anschnitt "Bootmedium".
* Alle notwendigen Vorgehensbeschreibungen müssen regelmäßig überprüft und geprobt werden. Eventuell müssen variierende Vorgehensweisen bei unterschiedlichen Betriebssystemen berücksichtigt werden.
**Bootmedium**

Bei der Einrichtung eines Rechners sollte ein Bootmedium erstellt werden, das bei Ausfall einer Festplatte zum Starten des Systems oder bei Auftreten eines Schadprogramms zum Erzeugen eines kontrollierten Systemzustands genutzt werden kann. Solche Medien können beispielsweise CDs sein, deren Erstellung das jeweilige Betriebssystem eventuell anbietet, es können aber auch eigens eingerichtete CDs oder portable Laufwerke (beispielsweise USB-Sticks oder externe Festplatten mit USB- oder Firewire-Schnittstelle) erstellt werden. Neben "physischen" Medien können auch Image-Dateien verwendet werden, die erst bei Bedarf auf das Bootmedium kopiert oder gebrannt werden. Art und Umfang des Notfall-Bootmediums richten sich nach dem Einsatzzweck des Rechners und den vorhandenen Schnittstellen.

Das Notfall-Bootmedium kann unter anderem bei folgenden Problemen eingesetzt werden:

* Datenverlust durch Fehlbedienung,
* Bedienungs- und Administrationsfehler, die die Benutzung und einen Neustart verhindern,
* Infektion des Systems mit Schadprogrammen (beispielsweise Computer-Viren),
* Kompromittierung des Systems durch einen Angreifer, oder auch
* Hardware-Probleme.
Idealerweise sollte das Notfall-Bootmedium alle Programme und Daten enthalten, die zu einer Untersuchung und - falls möglich - der Behebung der Probleme benötigt werden. Gegebenenfalls können unterschiedliche Medien für verschiedene Problemszenarien erstellt werden.

Als "Grundausstattung" für ein Notfall-Bootmedium werden folgende Programme empfohlen:

* Viren-Schutzprogramme mit aktuellen Signaturen, beziehungsweise die Möglichkeit, aktuelle Signaturen einzupflegen,
* Programme zur Bearbeitung von Konfigurationsdateien oder Datenbanken des Systems (Editoren für Dateien, Registry oder ähnliches),
* Programm zur Wiederherstellung des Bootsektors und des MBR (Master Boot Record) der Systemplatte,
* Backup- / Recovery-Programme,
* Diagnoseprogramme zur Analyse von Hardware-Defekten.
Darüber hinaus können Programme zur weitergehenden Analyse hinzugefügt werden, etwa zur forensischen Untersuchung eines kompromittierten Systems.

Dabei ist es wichtig, dass alle Programme und Bibliotheken ausschließlich vom Bootmedium geladen werden. Es dürfen keine Komponenten des installierten Systems verwendet werden. Bei der Erstellung des Bootmediums ist außerdem darauf zu achten, dass neben den notwendigen Programmen auch alle Treiber vorhanden sind, die für den Zugriff auf die eingebauten Platten des Rechners benötigt werden. Dazu zählen beispielsweise Treiber für Festplattencontroller (insbesondere RAID-Controller) und Treiber für eine Festplattenverschlüsselung oder Festplattenkomprimierung.

In der Regel können auch weitere Programme oder Dokumentation auf dem Medium gespeichert werden. Beispielsweise kann es die Effizienz der Fehlersuche erhöhen, wenn auf dem Bootmedium stets eine aktuelle Dokumentation der Systemkonfiguration enthalten ist.

Das Notfall-Bootmedium muss selbst frei von Viren und anderen Schadprogrammen sein. Es dürfen deshalb nur Programme eingesetzt werden, die aus vertrauenswürdigen Quellen (etwa direkt vom Hersteller) stammen oder deren digitale Signatur überprüft wurde. Zumindest einmal nach der Erstellung sowie bei jeder Änderung sollte das Bootmedium außerdem mit einem Viren-Schutzprogramm überprüft werden.

Es ist nicht unbedingt notwendig, für jedes System ein eigenes Bootmedium zu erstellen. Ein entsprechend flexibel angelegtes Bootmedium kann für eine große Anzahl verschiedener Systeme ausreichend sein. Auf dem Bootmedium braucht nicht einmal notwendigerweise das selbe Betriebssystem eingesetzt zu werden, wie auf dem Zielsystem selbst. Aus Gründen der Kompatibilität ist dies jedoch oft vorteilhaft. Es muss allerdings unbedingt durch entsprechende Tests sichergestellt werden, dass das Medium auch wirklich bei allen Rechnern funktioniert, für die es eingesetzt werden soll. Je nach Betriebssystem müssen außerdem noch systemspezifische Aspekte beachtet werden, die in den jeweiligen IT-Grundschutz-Bausteinen beschrieben werden.

Nach Veränderungen am Zielsystem, etwa einem Update des Betriebssystems oder Konfigurationsänderungen, muss gegebenenfalls das Notfall-Bootmedium und die darauf gespeicherte Dokumentation aktualisiert werden. Änderungen am Bootmedium müssen dokumentiert werden.

Das Notfall-Bootmedium muss für die Systembetreuer schnell greifbar sein, damit im Falle einer Störung nicht wertvolle Zeit verloren geht. Andererseits muss es auch so sicher aufbewahrt werden, dass Unbefugte keinen Zugang darauf haben.

Die Funktion des Notfall-Bootmediums sollte regelmäßig getestet und die Bedienung der darauf gespeicherten Programme geübt werden, damit sichergestellt ist, dass das Medium im Fall von Problemen funktioniert und die Administratoren mit der Bedienung vertraut sind. Es sollte überlegt werden, mit dem Medium eine kurze gedruckte Anleitung aufzubewahren, die für typische Einsatzszenarien die wichtigsten Schritte zusammenfasst. 

#### SYS.1.1.M23 Systemüberwachung

Um auf kritische Systemereignisse reagieren zu können, sollte für Server ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept erstellt werden. Dazu gehört, dass Systemzustand und Funktionsfähigkeit der Servers und der darauf betriebenen Dienste laufend überwacht werden. Wenn Fehler auftreten oder definierte Grenzwerte über- oder unterschritten werden, sollte dies automatisch an das Betriebspersonal gemeldet werden. 

Hierfür werden in der Regel Statusinformationen von einem zentralen IT-System abgerufen, auf dem die Ereignisse ausgewertet werden. Über die Schnittstelle, die benötigt wird, um die Systemereignisse vom IT-System abzurufen, können aber oft Systemeinstellungen des Betriebssystems verändert werden, z. B. über SNMP (Simple Network Management Protocol). Ist eine solche Modifikation nicht gewünscht, dann sollten diese Merkmale deaktiviert werden.

#### SYS.1.1.M24 Sicherheitsprüfungen

Es sollte regelmäßig, mindestens monatlich, ein Sicherheitscheck der Server durchgeführt werden. Für praktisch alle Betriebssysteme sind Programme verfügbar oder bereits im Lieferumfang des Betriebssystems oder der Betriebssystem-Distribution enthalten, die entsprechende Funktionen zur Verfügung stellen.

Bei einem solchen Sicherheitscheck sollten beispielsweise folgende Punkte überprüft werden:

* Gibt es Benutzer ohne Passwort?
* Gibt es Benutzer, die längere Zeit die Server nicht mehr benutzt haben?
* Gibt es Benutzer, deren Passwort nicht die erforderlichen Bedingungen einhält?
* Welche Benutzer besitzen die Administrator-Rechte?
* Sind Systemprogramme und Systemkonfiguration unverändert und konsistent?
* Entsprechen die Berechtigungen von 

 
	+ Systemprogrammen und Systemkonfiguration
	+ Anwendungsprogrammen und -daten
	+ Benutzerverzeichnissen und -daten
	+ den Vorgaben der Sicherheitsrichtlinie?
	  

 
* Welche Netzdienste laufen auf den einzelnen Systemen? Sind sie den Vorgaben der Sicherheitsrichtlinie entsprechend konfiguriert?
Bei einem regelmäßigen Sicherheitscheck können auch Penetrationstests im lokalen Subnetz integriert werden. Dabei kann der "Grad" der Penetrationstests variiert werden (beispielsweise: wöchentlich einfache automatisierte Überprüfungen, monatlich gründlicherer Test mit teilweise manueller Durchführung, einmal jährlich ein grundlegender Test des gesamten Netzes).

Bei der Durchführung des Sicherheitschecks sollten die Administratoren ihre Schritte so dokumentieren, dass sie (beispielsweise bei einem Verdacht auf ein kompromittiertes System) nachvollzogen werden können. Die Ergebnisse des Sicherheitschecks müssen dokumentiert werden, Abweichungen vom "Sollzustand" muss nachgegangen werden.

#### SYS.1.1.M25 Geregelte Außerbetriebnahme eines Servers

Soll ein Server außer Betrieb genommen werden, so darf dies nicht unvorbereitet und ohne Ankündigung für die Benutzer geschehen, sondern es muss eine Reihe von Maßnahmen ergriffen werden, um sicher zu stellen, dass

* keine wichtigen Daten verloren gehen,
* keine Dienste oder Systeme beeinträchtigt werden, die von dem Server abhängen, und dass
* keine sensitiven Daten auf den Datenträgern des Servers zurück bleiben.
Dazu ist es insbesondere wichtig, einen Überblick darüber zu haben, welche Daten wo auf dem System gespeichert sind und von wo aus darauf zugegriffen wird. Ausgehend von diesen Informationen sollte eine Planung für die Außerbetriebnahme des Servers erfolgen. Dabei sollten die folgenden Punkte berücksichtigt werden:

* Datensicherung  
 Vor der Außerbetriebnahme des Servers müssen Daten, die noch benötigt werden, entweder extern gesichert bzw. archiviert (beispielsweise auf Magnetbändern, CD - oder DVD-ROMs) oder auf ein Ersatzsystem übertragen werden. Nach der Sicherung sollte überprüft werden, dass wirklich alle Daten korrekt gesichert wurden. Weitere Informationen zu diesem Themenkomplex finden sich in den Bausteinen OPS.1.1.5 Datensicherung und OPS.1.2.2 Archivierung.
* Ersatzsystem  
 Wenn die von dem Server bereitgestellten Dienste weiter benötigt werden, so muss rechtzeitig ein angemessenes Ersatzsystem bereitgestellt werden. Für die entsprechende Planung, Beschaffung und Inbetriebnahme müssen entsprechende Ressourcen zur Verfügung stehen, siehe auch Abschnitt "Migration eines Servers".
* Information der Benutzer  
 Falls das System ersatzlos abgeschaltet wird, so müssen die Benutzer rechtzeitig über die bevorstehende Abschaltung informiert werden und gegebenenfalls die Gelegenheit erhalten, eigene Daten zu sichern.
* Entfernen von Verweisen auf das System  
 Im Zuge der Außerbetriebnahme eines Systems müssen auch Verweise auf das System gelöscht werden. Dazu gehört beispielsweise das Löschen des DNS-Eintrags und der Einträge in sonstigen Verzeichnisdiensten sowie in Abhängigkeit vom Einsatzzweck weitere Verweise. Wird beispielsweise ein Webserver außer Betrieb genommen, so sollten Verweise auf diesen Server, die noch in eigenen Webseiten enthalten sind, gelöscht werden.
* Löschen der Daten auf dem abzuschaltenden System  
 Es muss sichergestellt werden, dass keine schützenswerten Informationen mehr auf den Datenträgern vorhanden sind. Dazu genügt es nicht, die Platten einfach neu zu formatieren, sondern sie müssen mindestens einmal vollständig überschrieben werden. Es ist zu beachten, dass weder das logische Löschen mit den Löschfunktionen des Betriebssystems noch das Neuformatieren der Platten die Daten tatsächlich von den Datenträgern entfernt. Mit geeigneter Software können Daten in solchen Fällen, oft sogar ohne großen Aufwand, wieder rekonstruiert werden. 
* Löschen von Datensicherungsmedien  
 Nach der Außerbetriebnahme eines Systems müssen gegebenenfalls auch die entsprechenden Datensicherungsmedien gelöscht oder unbrauchbar gemacht werden, wenn die darauf gespeicherten Daten nicht mehr benötigt werden.
* Entfernen sonstiger Informationen  
 Oft enthalten Serversysteme weitere Daten (beispielsweise Konfigurationsdaten), die in einem nichtflüchtigen Speicher abgelegt sind, oder sind von außen beschriftet (beispielsweise mit dem Rechnernamen, der IP-Adresse und weiteren technischen Informationen). Diese Informationen sollten nach Möglichkeit vor der Weitergabe des Gerätes entfernt werden, da ein Angreifer auch aus solchen Informationen eventuell Hinweise für mögliche Angriffe ziehen kann.
Es wird empfohlen, anhand der oben gegebenen Empfehlungen eine Checkliste zu erstellen, die bei der Außerbetriebnahme eines Systems abgearbeitet werden kann. Auf diese Weise kann vermieden werden, dass einzelne Schritte vergessen werden. 

**Migration eines Servers**

Sollen die Dienste des Servers von einem anderen System übernommen werden, so muss der Übergang geplant werden. Insbesondere dann, wenn besondere Anforderungen an die Verfügbarkeit der Dienste bestehen, ist eine besonders sorgfältige Planung erforderlich.

In den meisten Fällen ist es empfehlenswert, den "Funktionsübergang" auf das Ersatzsystem außerhalb der normalen Betriebszeiten durchzuführen. Falls dies nicht möglich ist müssen Maßnahmen getroffen werden, die sicher stellen, dass weder Daten beim Funktionsübergang verloren gehen, noch untragbare Ausfallzeiten entstehen.

Für die Migration wichtiger Server muss deswegen vorab ein entsprechendes Migrationskonzept erstellt werden. Dabei sollten insbesondere folgende Punkte mit berücksichtigt werden:

* Migration der Daten und Konfiguration  
 Nach der Übertragung der Daten auf das neue System muss überprüft werden, ob die Daten vollständig und korrekt übertragen wurden.  
 Wenn auf dem neuen System eine neue Version der Serversoftware eingesetzt werden soll, so muss sichergestellt sein, dass die neue Version mit den vorhandenen Datenbeständen korrekt umgehen kann. Dies betrifft nicht nur die Aufgabe, Daten der alten Version korrekt einzulesen, sondern insbesondere auch, diese Daten zu modifizieren oder neue Datensätze hinzuzufügen. Gerade in solchen Fällen tauchen oft Probleme auf, so dass gründliche Tests empfohlen werden.Außerdem ist es wichtig, dass die Konfiguration des alten Dienstes auf dem neuen System korrekt übernommen oder zumindest "funktional äquivalent nachgebaut" werden kann.
* Kompatibilität des Dienstes  
 Es muss sichergestellt sein, dass der Dienst auf dem Ersatzsystem mit dem ursprünglichen Dienst kompatibel ist. Dies ist insbesondere dann von Bedeutung, wenn im Rahmen der Migration auf dem neuen System eine neue Version des Serverprogramms eingesetzt werden soll, auf die jedoch weiter mit Clients der alten Version zugegriffen wird. Selbst dann, wenn ein Hersteller Berichte von Referenzkunden über erfolgreiche Migrationen vorlegt oder "problemlose Abwärtskompatibilität", "vollständige Rückwärtskompatibilität mit früheren Versionen" oder ähnliches zusichert, wird dringend empfohlen, vorab entsprechende Tests durchzuführen.
* Kryptographische Schlüssel  
 Falls Teile der Daten oder der Dateisysteme eines Servers verschlüsselt sind, so kommt der Sicherung oder Übertragung der entsprechenden kryptographischen Schlüssel besondere Bedeutung zu: Oft sind diese an einer anderen Stelle auf dem System gespeichert als die Nutzdaten selbst. Beispielsweise dann, wenn die Daten mit Hilfe systemnaher Programme blockweise direkt kopiert werden oder die Festplatten aus dem alten in das neue System umgebaut werden, muss sichergestellt sein, dass auch die kryptographischen Schlüssel mit übertragen werden, da sonst kein Zugriff mehr auf die verschlüsselten Daten möglich ist.
* Umstellung von Namen und Adressen  
 Falls auf einen Server nur über seine IP-Adresse oder einen DNS-Namen zugegriffen wird, so ist eine Migration meist relativ unproblematisch, da in diesem Fall einfach das Ersatzsystem die IP-Adresse des alten Systems übernehmen kann. Problematischer wird es beispielsweise, wenn das neue System den selben DNS-Namen bekommen soll, aber nicht die IP-Adresse übernehmen kann. Denn es dauert eine gewisse Zeit, bis die Änderung der Adresse bei allen Clients "angekommen" ist. Solche Latenzzeiten müssen bei der Planung der Migration berücksichtigt werden.  
 Falls auf das System anders zugegriffen wird (beispielsweise wenn die Adresse von einem anderen Verzeichnisdienst aufgelöst wird), so muss berücksichtigt werden, dass auch die Änderung auf diesem Weg eventuell ebenfalls eine gewisse Latenzzeit hat, bevor sie wirksam wird.  
 Das größte Problem entsteht dann, wenn Clients auf den Servern über eine Anwendung zugreifen, bei der die IP-Adresse oder der Name des Servers in einer lokalen Konfigurationsdatei oder -datenbank gespeichert sind. Falls eine größere Anzahl Clients manuell umkonfiguriert werden müssen, so kann dies eine erhebliche Zeit in Anspruch nehmen und muss vorab geplant werden.
* Dauerhafte Verbindungen  
 Falls es Clients gibt, die länger bestehende oder gar dauerhafte Netzverbindungen zu dem Dienst aufbauen, der auf einen neuen Rechner migriert werden muss (dies ist beispielsweise bei manchen Datenbankanwendungen der Fall), so muss dies bei der Migration berücksichtigt werden. Gegebenenfalls müssen diese Verbindungen auf den betreffenden Clients manuell beendet werden. Auch hierfür ist eine entsprechende Planung erforderlich.
Für die Durchführung der Migration ist es empfehlenswert, im Rahmen der Erarbeitung des Migrationskonzeptes eine Checkliste zu erstellen, die bei der Umstellung Schritt für Schritt durchgegangen werden kann. Bei der Planung der Migration und der Erstellung der Checkliste muss darauf geachtet werden, dass jeder Schritt nur von den vorhergehenden Schritten abhängig ist.

Bei hohen Anforderungen an die Verfügbarkeit des Dienstes sollte der gesamte Übergang vorab in einer Testumgebung unter möglichst realistischen Bedingungen geprobt werden, um mögliche Probleme frühzeitig zu identifizieren und zu beseitigen.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.1.1.M26 Mehr-Faktor-Authentisierung(C)

Zur Authentisierung gibt es unterschiedliche Verfahren, die auf folgenden Faktoren basieren können: Wissen, Besitz und biometrische Merkmale. Bei einem höheren Schutzbedarf wird eine Mehr-Faktor-Authentisierung empfohlen, bei der zwei der drei Faktoren verwendet werden. 

Am gebräuchlichsten ist die Nutzung der Faktoren Wissen und Besitz. Der Authentisierungsschlüssel wird hierbei in einer Hardware, z. B. Chipkarte, gespeichert (Faktor Besitz), die nur nach Eingabe einer PIN oder eines Passwortes eingesetzt werden kann (Faktor Wissen). Je nach Sicherheitsanforderungen können Schlüssel auch auf Clients (z. B. Notebook) bzw. Servern im Netz der Institution gespeichert sein. 

Alternativ kann die Nutzung einer Public-Key-Infrastruktur (PKI) empfohlen werden, die auf digitale Signaturen und asymmetrischen Kryptografieverfahren basiert. Die Gültigkeit der Signaturen wird über eine anerkannte Zertifizierungsstelle (CA – Certificate Authority) überprüft. Die Länge des Schlüssels bzw. der Signatur korreliert mit der Sicherheit des verwendeten Kryptoverfahrens.

#### SYS.1.1.M27 Hostbasierte Angriffserkennung(IA)

Mit dem Einsatz von hostbasierten Angriffserkennungssystemen (Host-based Intrusion Detection Systems, IDS) sollte das Systemverhalten auf Anomalien und Missbrauch hin überwacht werden. Die eingesetzten IDS-Mechanismen sollten geeignet ausgewählt, konfiguriert und ausführlich getestet werden. Im Falle einer Angriffserkennung muss eine geeignete Alarmierung des Betriebspersonals sichergestellt sein (siehe Baustein NET.3.4 IDS/IPS).

**Regelmäßige Integritätsprüfung**

Eine regelmäßige Kontrolle des Dateisystems, der Dateiattribute und der Prozessinformationen sowie weiterer wichtiger Elemente der Systemkonfiguration (beispielsweise unter Windows die Registry) auf unerwartete Veränderungen helfen dabei, Inkonsistenzen zu erkennen. Die Erkennung solcher Inkonsistenzen kann zur Vorbeugung gegen Systeminstabilitäten eingesetzt werden. Es können dadurch aber auch Angriffe zeitnah entdeckt werden. Sollte tatsächlich ein Angriff vorliegen, ist es wichtig, das Vorgehen des Angreifers zu rekonstruieren. Dies dient einerseits dazu, Manipulationen an Daten aufzudecken, und andererseits dazu, verborgene Hintertüren zu erkennen, die ein Angreifer für einen späteren Zugang auf den Rechner installiert haben könnte.

**Berechnung kryptographischer Prüfsummen**

Zur Erkennung von Manipulationen können Programme genutzt werden, die kryptographische Prüfsummen über einen Großteil der Dateien des Systems oder über andere Ressourcen berechnen. Zu unterscheiden sind dabei Integritätsprüfungsprogramme, welche nur auf Dateiebene arbeiten, und solche, die auch Prozesse und spezielle Konfigurationsdaten, wie die Windows-Registry oder Datenstrukturen des Kernels, überprüfen können. Es wird empfohlen, darauf zu achten, dass diese Werkzeuge auch zentral administriert und überwacht werden können. Außerdem müssen die von den Programmen verwendeten kryptographischen Mechanismen dem Stand der Technik entsprechen.

Einige Programme stellen lediglich fest, ob Veränderungen am Dateisystem durchgeführt wurden. Hierzu prüfen sie, ob die Zugriffsrechte, das Datum der letzten Modifikation oder die Inhalte der jeweiligen Datei geändert wurden. Modifikationen werden erkannt, indem die vorher erstellte kryptographische Prüfsumme mit der aktuell berechneten Prüfsumme verglichen wird. Mit einer speziellen Einstellung kann in vielen Fällen auch ein nur lesender Zugriff auf die Datei bemerkt werden.

**Schutz der Prüfsummendatei**

Um zu verhindern, dass das Integritätsprüfungsprogramm selbst oder die Datei, welche die Prüfsummen des Systems enthält, von einem Angreifer oder durch Schadsoftware verfälscht werden können, sollten sich diese auf einem schreibgeschützten Datenträger befinden. Allerdings muss die Prüfsummendatei bei erlaubten Veränderungen am Dateisystem ebenfalls geändert werden, so dass sich CDs, DVDs oder Wechselplatten für diesen Zweck empfehlen. Alternativ kann die Prüfsummendatei auch über das Netz schreibgeschützt zur Verfügung gestellt werden. Bei einer Verwaltung des Integritätsprüfungsprogramms über das Netz sollte dieser Weg auch bevorzugt werden. Einige Schadprogramme tarnen sich, so dass sie mit Methoden des manipulierten Betriebssystems nicht erkannt werden können. Daher ist es im Verdachtsfall sinnvoll, das System mittels eines manipulationsfreien Betriebssystems zu untersuchen. Dazu kann beispielsweise über ein vertrauenswürdiges Referenzsystem ein externer Datenträger erstellt werden, von dem dann das manipulationsfreie Betriebssystem gestartet wird.

**Prüfintervall und Prüfumfang**

Eine Integritätsprüfung sollte regelmäßig, beispielsweise jede Nacht, durchgeführt werden. Die Wahl eines geeigneten Prüfintervalls hängt stark vom Einsatzzweck des jeweiligen IT-Systems beziehungsweise der Einsatzumgebung ab. Bei der Durchführung von Integritätsprüfungen ist außerdem der Verbrauch an Speicherplatz und Rechenzeit, der für die Überprüfung der Prüfsummen notwendig ist, zu berücksichtigen. Der Einsatz des Integritätsprüfungsprogramms darf den ordnungsgemäßen Betrieb nicht beeinträchtigen.

Im normalen Betrieb jedes größeren IT-Systems ergeben sich ständig kleinere und größere Änderungen an Systemdateien. Generell ist es daher empfehlenswert, das Integritätsprüfungsprogramm so zu konfigurieren, dass nur Veränderungen an relevanten Dateien erfasst werden. Anderenfalls besteht die Gefahr, dass sehr viele Änderungsmeldungen ausgelöst werden, die auf ganz normale betriebliche Abläufe und nicht auf Angriffsversuche zurückzuführen sind (false positives). Als Folge kann es passieren, dass die Protokolldateien nicht mehr zeitnah ausgewertet werden können.

**Prozessinformationen im Arbeitsspeicher**

Neben dateibasierten Integritätsprüfungen gibt es auch die Möglichkeit, Prozessinformationen aus dem Arbeitsspeicher gegen eine Liste erlaubter Prozesse (Whitelist) zu prüfen. Auf diese Weise lassen sich auch bestimmte Manipulationen erkennen, die keine Spuren im Dateisystem hinterlassen. Andererseits gibt es Manipulationen, die nicht die Prozesse selbst, sondern nur deren Konfiguration betreffen. Solche Manipulationen lassen sich unter Umständen leichter durch eine Integritätsprüfung der Konfigurationsdateien aufdecken. Integritätsprüfungen des Dateisystems und des Arbeitsspeichers haben somit teilweise unterschiedliche Schutzwirkungen. Ein Vorteil der Prüfung von Prozessinformationen im Arbeitsspeicher ist, dass dazu nur wenige oder keine Festplattenzugriffe nötig sind, die deutlich langsamer sind als Arbeitsspeicherzugriffe. Dadurch kann wesentlich häufiger geprüft werden als bei einer dateibasierten Methode, bei der viele Informationen von der Festplatte gelesen werden müssen. So können unerwünschte Programme meist schneller entdeckt werden als bei einer dateibasierten Integritätsprüfung.

**Benachrichtigung**

Eine Benachrichtigung über das Ergebnis sollte, auch wenn keine Veränderungen festgestellt wurden, automatisch per E-Mail oder einen ähnlichen Weg an den IT-Betrieb erfolgen. Vorab sollte festgelegt werden, welche Maßnahmen einzuleiten sind, wenn ein Integritätsverlust festgestellt wird. Wichtig ist beispielsweise, ob automatische oder manuelle Aktionen durchgeführt werden.

#### SYS.1.1.M28 Redundanz(A)

Die Verfügbarkeit von Geschäftsprozessen, Anwendungen und Diensten hängt oft von der Funktion eines zentralen Servers ab. Je mehr Anwendungen aber auf einem Server laufen, desto ausfallsicherer muss dieser sein. Ein Server enthält in der Regel verschiedene potentielle Fehlerquellen ("Single Points of Failure"), also Komponenten, deren Ausfall den Ausfall des Gesamtsystems auslösen kann: Festplatten, Stromversorgung, Lüfter, Backplane, etc. Die Wiederherstellung des Gesamtsystems kann in diesem Fall erhebliche Zeit in Anspruch nehmen. Neben der Vorhaltung von Ersatzteilen können zusätzlich folgende Möglichkeiten zur Steigerung der Verfügbarkeit eingesetzt werden:

* Cold-Standby
* Hot-Standby (manuelles Umschwenken)
* Cluster (automatisches Umschwenken)
* Load balanced Cluster
* Failover Cluster
Jede einzelne dieser Techniken bietet ein unterschiedliches Niveau an Verfügbarkeit und ist in der Regel mit unterschiedlichen Kosten verbunden. Unter Umständen kann eine höhere Verfügbarkeit erzielt werden, wenn die betroffenen Server virtualisiert werden (siehe SYS.1.5 Server-Virtualisierung).

**Cold-Standby**

Beim Cold-Standby wird neben dem eigentlichen Produktivsystem ein zweites baugleiches Ersatzsystem bereitgehalten, das aber nicht aktiv ist. Wenn das erste System ausfällt, kann das Ersatzsystem manuell hochgefahren und ins Netz integriert werden.

Nach der Vorhaltung von einzelnen Ersatzteilen ist dies die einfachste Redundanz-Lösung, die mit den entsprechenden Vorteilen und Nachteilen verbunden ist:

Vorteile einer Cold-Standby Lösung:

* Cold-Standby Lösungen bringen keine Komplexitätserhöhung für das Gesamtsystem mit sich.
* Die Kosten für ein Cold-Standby System belaufen sich lediglich auf die Kosten der zusätzlichen Hardware und sind somit am geringsten unter den vorgestellten Möglichkeiten.
* Neuaufsetzen oder Änderungen im System sind ohne Verfügbarkeitseinbußen möglich. Der Produktivbetrieb wird dafür während der Änderungen auf das Cold-Standby System umgelegt. 
Nachteile einer Cold-Standby Lösung

* Zum bestehenden System muss ein zweites System vorgehalten werden.
* Das Ersatzsystem muss ständig auf dem aktuellen Konfigurations- und Patch-Stand gehalten werden.
* Da das Ersatzsystem manuell aktiviert werden muss, müssen Administratoren das System kontinuierlich überwachen und im Notfall einschreiten.
* Wenn die Applikationsdaten nicht auf einem externen Speichersystem liegen, so dass der Zugang direkt aus dem Ersatzsystem möglich ist, dann müssen diese auf das Cold-Standby System migriert werden. 
Der Einsatz eignet sich gut für Server mit Anwendungen, bei denen kurze bzw. begrenzte Ausfallzeiten, bis ein Eingriff des IT-Betriebs möglich ist, unkritisch sind. Beispiele dafür sind:

* Server in kleineren Netzen (Intranet)
* Wenig frequentierte Server im Internet
**Hot-Standby (manuelles Umschwenken)**

Bei einem Hot-Standby steht ebenfalls ein Ersatzsystem bereit, das aber neben dem Produktivsystem parallel in Betrieb gehalten wird. Die Funktion des Produktivsystems wird überwacht, bei Ausfall wird das Ersatzsystem aktiv. Der Wechsel kann automatisch erfolgen oder auch manuell. Für den automatischen Wechsel sind zusätzliche Funktionalitäten im Gesamtsystem erforderlich z. B. die automatische Erkennung von Ausfällen. Dieser Fall wird im nächsten Abschnitt unter "Cluster" behandelt.

Um die Ausfallzeiten möglichst gering zu halten, muss der Zustand des Ersatzsystems kontinuierlich überprüft werden.

Vorteile einer Hot-Standby Lösung

* Die Ausfallzeiten sind im Vergleich zu Cold-Standby geringer.
* Wie beim Cold-Standby ist diese Lösung auch relativ kostengünstig, verglichen mit höherwertigen Hochverfügbarkeitslösungen, die im Folgenden beschrieben werden.
* Das Ersatzsystem ist in Betrieb und kann auch zu Datenreplikation benutzt werden.
* Neuaufsetzen oder Änderungen im System sind ohne Verfügbarkeitseinbuße möglich. Der Produktivbetrieb wird dafür während der Änderungen auf das Hot-Standby System umgelegt. 
Nachteile einer Hot-Standby Lösung

* Es wird auch hier immer nur die Hälfte der vorhandenen Hardware genutzt.
* Das Ersatzsystem muss ständig auf dem aktuellen Stand gehalten werden.
* Im Falle der manuellen Aktivierung des Hot-Standby Systems ist eine kontinuierliche Überwachung von einem Systemverantwortlichen erforderlich. 
Der Einsatz von Hot-Standby Systemen eignet sich für Anwendungen, bei denen kurze Ausfallzeiten unkritisch sind. Die Problematik der Systemüberwachung und der Aktivschaltung des Hot-Standby Servers muss dabei mitbedacht werden. Mögliche Einsatzbereiche sind z. B. für:

* Webserver mit oft variierendem Content
* Server in kleineren Netzen (Application-Server, Mailserver)
* Datenbank-Server und Fileserver (z. B. sekundärer Server repliziert primären Server ständig und wird im Fehlerfall als primärer Server geschaltet)
**Cluster (automatisches Umschwenken)**

Ein Cluster besteht aus einer Gruppe von zwei oder mehreren Rechnern, die zur Steigerung der Verfügbarkeit oder auch der Leistung einer Anwendung oder eines Dienstes parallel betrieben werden. Die Anwendung oder der Dienst kann dabei auf einem der Rechner aktiv durchgeführt werden oder auf mehreren verteilt (Performance-Steigerung).

Cluster werden je nach Funktionsart in

* Load balanced Cluster
* Failover Cluster und
unterschieden.

**Load balanced Cluster**

Beim Load balanced Cluster werden Instanzen einer Anwendung oder eines Dienstes in Abhängigkeit von der Auslastung unter den Servern verteilt. Wenn dies für eine Anwendung oder einen Dienst möglich ist, dann kann damit nicht nur eine Lastverteilung (Load balancing) und somit eine Performancesteigerung erreicht werden, sondern auch die Probleme bei Ausfällen werden verringert.

Eine der Voraussetzungen für den Einsatz von Load balancing ist, dass die jeweiligen Anwendungen oder Dienste keinen schreibenden Datenzugriff benötigen dürfen.

Eine Redundanz kann in diesem Fall geschaffen werden, indem Systeme mit ähnlicher Leistung mit Hilfe eines Load-Balancing Prozesses "nebeneinander" gestellt werden und dafür gesorgt wird, dass beim Ausfall eines Servers die anderen Server diesen Ausfall auffangen.

Vorteile eines Load balanced Clusters

* Es können damit sowohl Verfügbarkeitssteigerung als auch Leistungssteigerung erreicht werden.
* Alle verfügbare Ressourcen werden dauerhaft genutzt.
* Die Lösung ist hochgradig skalierbar.
* Die Komplexität des Gesamtsystems ist geringer als bei einem Failover Cluster. 
Nachteile eines Load balanced Clusters

* Der Einsatz ist nicht für alle Arten von Anwendungen möglich. Insbesondere Anwendungen, die keine reinen Lesezugriffe verwenden und zugleich den Zugriff aller Server auf die gleichen Speicherressourcen verlangen, sind für Load Balancing nicht geeignet. 
Wenn neben der Verfügbarkeit die Performance hohen Stellenwert hat und die Applikation einen verteilten Einsatz erlaubt, bietet ein Load balanced Cluster eine optimale Lösung. Das kann z. B. der Fall sein für:

* Web-Server
* Front-end Applikationen mit ausschließlichen Lesezugriffen (z. B. Web-Server-Farmen) 
**Failover Cluster**

Als Failover Cluster wird hier ein Cluster bezeichnet, wenn bei Ausfall eines der Cluster-Systeme automatisch der aktive Betrieb der Anwendung oder des Dienstes von einem anderen Teil des Clusters übernommen wird (Takeover). Die automatische Übernahme von Diensten beim Ausfall einer Systemkomponente durch eine funktional äquivalente Komponente wird Failover genannt. Für die Failover-Funktionalität ist eine dedizierte "heartbeat" (Herzschlag) Verbindung üblich, die die Kommunikation zwischen den Cluster-Servern gewährleistet. Die Cluster-Server müssen neben der Verbindung mit dem Client-Netz auch mit dem Administrationsnetz dediziert verbunden sein, um einen direkten Zugang im Notfall zu gewähren.

Ein automatisches Failover setzt voraus, dass alle Software- und Hardware-Komponenten geeignet überwacht werden. Daher ist es wichtig sicherzustellen, dass der Failover Mechanismus auf keinen falschen Annahmen basiert.

Folgende Punkte müssen beim Einsatz eines Failover-Clusters berücksichtigt werden:

* Zugriff auf gemeinsamen Speicher:  
 Neben den servereigenen Festplatten, die das Betriebssystem und die für den Betrieb notwendigen Daten enthalten, ist es in einem Cluster ratsam, die Anwendungsdaten auf gemeinsamen Speicher zu verwalten.  
 Der Zugriff auf diese Festplatten wird dem Teil des Clusters gewährt, der gerade aktiv ist. Es ist auch möglich, statt gemeinsamer Festplatten replizierte Festplatten zu verwenden. Dies ist dann sinnvoll, wenn das Failover von einem entfernten Standort aus stattfindet. Bei einem lokalen Failover sollte überlegt werden, ob die durch die Replikation erzeugte Komplexität und entstandene Abhängigkeiten nicht eine zusätzliche Bedrohung für die Verfügbarkeit darstellen.
* Portabilität der Anwendung:  
 Die Installation und Inbetriebnahme einer Anwendung auf zwei oder mehreren Servern parallel erfordert in den meisten Fällen den Einsatz zusätzlicher Lizenzen. Darüber hinaus muss überprüft werden, ob die Applikation eine Failover-Funktionalität erlaubt.
* NSPoF (No Single Points of Failure):  
 Wenn die Failover-Funktionalität des Clusters durch den Ausfall einer einzigen Komponente gestört werden kann, widerspricht dies dem eigentlichen Zweck der Cluster-Architektur. Um Single Points of Failure zu vermeiden, muss das Gesamtsystem analysiert werden und der Ausfall einzelner Komponenten (Netzteile, Systemspeicher, Hauptspeicher, Netzwerkkarten, Switche, Hubs etc.) in Betracht gezogen werden.
* Betriebssystem und Konfiguration der Cluster-Server:  
 Die Cluster-Server sollten mit gleichen Betriebssystemversionen, Patches, Libraries und Applikationsversionen ausgestattet sein. Eine möglichst identische Hardware- und Software-Konfiguration kann ein möglichst identisches Verhalten im Falle eines Failovers gewährleisten. Darüber hinaus reduziert sich im Falle von identischen Systemen die Komplexität des Gesamtsystems (Einsatz der gleichen Failover Software, Netz-Schnittstellen, Kompatibilität der gemeinsamen Speichersystems, Administration, Service).
* Dedizierte und redundante Verbindung zwischen den Servern:  
 Die Kommunikation zwischen den Cluster-Servern muss unabhängig von der Netzlast, möglichst verzögerungsfrei erfolgen, damit das Failover schnellstmöglichst stattfinden kann. Die Redundanz ist aufgrund der hohen Verfügbarkeitsanforderungen ebenfalls erforderlich.
* Einsatz von ausgereiften Software-Produkten für das Failover Management:  
 Die Entscheidung, ob ein Failover stattfinden muss oder nicht, ist eine sehr komplexe. Neue oder selbstentwickelte Tools können Fehler enthalten und dadurch letztendlich die Verfügbarkeit des Gesamtsystems reduzieren.
* Ausführliches Testen aller möglichen Failover-Aspekte:  
 Ein ausführliches Testen ist unter anderem auch dazu notwendig, um festzustellen, dass keine unerwarteten Fehlerquellen (Single Points of Failure) vorhanden sind. Insbesondere muss das Monitoring der Server und das Failover-Management auf alle möglichen Fehler getestet werden. 
Vorteile eines Failover Clusters

* Durch das automatische Takeover kann die Verfügbarkeit erheblich gesteigert werden.
* Es sind keine manuellen Eingriff nötig. 
Nachteile eines Failover Clusters

* Diese Lösung ist hoch komplex.
* Failover Cluster sind nicht gut skalierbar.
* Es wird immer nur ein Teil der Ressourcen genutzt.
* Es entstehen hohe Kosten aufgrund zusätzlicher Hardware und Software
Wie aus der Gegenüberstellung der Vorteile und Nachteile hervorgeht, ist der Einsatz eines Failover Clusters nur dann sinnvoll, wenn eine oder mehrere Applikationen sehr hohe Verfügbarkeitsanforderungen haben. Neben dem hohen Kostenaufwand sind sehr gute Kenntnisse des verantwortlichen Personals sowohl über die eingesetzten Betriebssysteme und Applikationen als auch über die Failover-Funktionalität erforderlich. Der Einsatz von Failover Lösungen für Server macht zudem nur dann Sinn, wenn auch alle Abhängigkeiten wie beispielsweise Netzanbindung oder Verfügbarkeit der Clients auch mit den entsprechenden Redundanzen ausgelegt sind.

Bereiche, für die typischerweise bei hohen Verfügbarkeitsanforderungen Failover Cluster eingesetzt werden, sind z. B.:

* Datenbank Anwendungen
* File Storage
* Anwendungen mit dynamischem Inhalt
* Mail Server
Wenn Geschäftsprozesse, Anwendungen oder Dienste hohe Anforderungen an die Verfügbarkeit haben, sollte auf jeden Fall überlegt werden, wodurch diese Anforderungen abgedeckt werden können. Die IT-Verantwortlichen und das Sicherheitsmanagement sollten für die entsprechenden Server ein Konzept erarbeiten und angemessene Architekturen auswählen. 

#### SYS.1.1.M29 Einrichtung einer Testumgebung(CIA)

Für Server mit hohen Sicherheitsanforderungen sollte eine Testumgebung eingerichtet werden, in der Konfigurationsänderungen, Updates und Patches vor dem Einspielen auf dem Produktionssystem vorab getestet werden können. Dies betrifft sowohl Sicherheitspatches und -updates als auch normale Updates, die vom Hersteller herausgegeben werden.

Die Testumgebung muss so beschaffen sein, dass sie eine "funktional äquivalente" Installation von Hard- und Software erlaubt. Dies bedeutet nicht notwendigerweise, dass zu einem teuren Serverrechner ein zweites, identisch konfiguriertes System beschafft werden muss. Zum Testen von Konfigurationsänderungen, Updates und Patches von Anwendungsprogrammen und Serversoftware genügt meist ein technisch deutlich sparsamer ausgestattetes System.

Es sollte jedoch auch die Möglichkeit bestehen, neue Gerätetreiber vor dem Einspielen zu testen. Daher kann es gegebenenfalls vorteilhaft sein, für verschiedene Arten von Tests unterschiedliche Testsysteme zu nutzen, etwa ein System für Tests systemnaher Programme oder von Betriebssystempatches und ein anderes für Tests im Zusammenhang mit der eigentlichen Serversoftware. In einem solchen Fall ist es jedoch wichtig sich bewusst zu sein, dass auf diese Weise gewisse Arten von Wechselwirkungen zwischen Betriebssystemumgebung und Serversoftware nicht abgedeckt werden können. Bei besonderen Anforderungen an die Sicherheit und Zuverlässigkeit eines Servers kann es deswegen erforderlich werden, tatsächlich ein zweites, identisch konfiguriertes System als Testumgebung zur Verfügung zu haben.

Für verschiedene typische und häufiger wiederkehrende Testfälle sollten Checklisten erstellt werden, die beim Testen abgearbeitet werden können und die neben der reinen Dokumentation des Tests oft auch zu einer Erhöhung der Effizienz und zur Vermeidung von Fehlern beitragen können.

Alle Tests sollten so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können.

####  Ein Dienst pro Server(CIA)

####  Application Whitelisting(CI)

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Zur Effizienz-Steigerung in Rechenzentren wird häufig Server-Virtualisierung eingesetzt. Da aktuelle Server-Hardware so leistungsfähig ist, dass klassische Server-Installationen die Hardware-Ressourcen oftmals nicht auslasten, können mehrere virtuelle Server auf einem Physischen betrieben werden. Dies spart Platz und Energie.

Durch das Zusammenfassen mehrerer Server auf einer Hardware muss diese unter Umständen jedoch auch besser abgesichert werden, als ein einzelner Server. Das Bundesamt für Sicherheit in der Informationstechnik (BSI) hat daher eine Empfehlung zum Thema veröffentlicht: CSE-113: Server-Virtualisierung. Sie richtet sich an Verantwortliche für die Planung und den Betrieb von IT-Infrastrukturen sowie an Betreiber von IT-Rechenzentren. Im Fokus stehen dabei produktunabhängige Empfehlungen zum sicheren Einsatz von Server-Virtualisierungsprodukten, die als Bare-metal-Hypervisoren eingesetzt werden. Bei derartigen Einsatzszenarien laufen neben dem Hypervisor, ein speziell für Virtualisierung optimiertes Betriebssystem, keine anderen Anwendungen auf der physischen Hardware.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeiner Server" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSITLS] Migrationsleitfaden zum Mindeststandard TLS 1.2

  

 Bundesamt für Sicherheit in der Informationstechni, 2015  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden\_Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_2.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden_Mindeststandard_BSI_TLS_1_2_Version_1_2.pdf)

 
* #### [CSE113] CSE-113: Server-Virtualisierung

  

 CSE-113:Server-Virtualisierung, BSI-Veröffentlichung zur Cyber-Sicherheit, 03.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_113.htm](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_113.htm)

 
* #### [IEC62305] IEC 62305 (VDE 0185-305 / DIN EN 62305) – Blitzschutz

  

 Normreihe zum Blitzschutz von baulichen Anlagen, (zuletzt abgerufen 05.10.2017)  
 <https://www.vde.com/resource/blob/936756/5b65d838e75e83f750bd8fa23bb620b1/merkblatt-blitzschutznormen-13-download-data.pdf>

 
* #### [ISi-Server] Absicherung eines Servers (ISi-Server), BSI, 09.2013

  

 Bundesamt für Sicherheit in der Informatiostechnik, 02.2017  
 <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
* #### [RFC5246] RFC 5246, The Transport Layer Security (TLS) Protocol

  

 Internet Engineering Task Force (IETF), (zuletzt aufgerufen 05.10.2017)  
 <https://tools.ietf.org/html/rfc5>

 
* #### [RFC5746] RFC 5746, Transport Layer Security (TLS) Renegotiation Indication Extension

  

 Internet Engineering Task Force (IETF), (zuletzt abgerufen 05.10.2017)  
 <https://tools.ietf.org/html/rfc5746>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
