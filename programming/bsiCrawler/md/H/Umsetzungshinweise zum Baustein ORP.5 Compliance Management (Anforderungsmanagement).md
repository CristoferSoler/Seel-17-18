1 Beschreibung
--------------

### 1.1 Einleitung

In jeder Institution gibt es aus den verschiedensten Richtungen gesetzliche, vertragliche, strukturelle und interne Richtlinien und Vorgaben, die beachtet werden müssen. Viele davon haben direkte oder indirekte Auswirkungen auf das Informationssicherheitsmanagement. Die Anforderungen sind je nach Branche, Land und anderen Rahmenbedingungen unterschiedlich. Weiterhin unterliegt beispielsweise eine Behörde anderen externen Regelungen als eine Aktiengesellschaft. Die Leitungsebene der Institution muss die Einhaltung der Anforderungen durch angemessene Überwachungsmaßnahmen (neudeutsch: Compliance) sicherstellen und ein Compliance Management System betreiben. 

Ziel des Compliance Managements ist es, jederzeit den Überblick über die verschiedenen Anforderungen an die einzelnen Bereiche der Institution zu haben und geeignete Maßnahmen zu identifizieren und umzusetzen, um Verstöße gegen diese Anforderungen zu vermeiden.

Diese Aufgabe wird typischerweise an einen Mitarbeiter übertragen. Die Rolle wird im Folgenden mit „Compliance Manager “ bezeichnet. In einigen Unternehmen wird z. B. auch die Bezeichnung „Anforderungsmanager “ benutzt. Sofern dies nicht durch andere Regelungen vorgeschrieben ist, müssen hierfür aber keine neuen Stellen geschaffen werden. Die Aufgabe kann beispielsweise vom Sicherheitsmanagement, der Revision, dem Controlling oder dem Justiziariat mit übernommen werden.

Je nach Größe einer Institution kann diese verschiedene Managementprozesse haben, die sich mit unterschiedlichen Aspekten des Risikomanagements beschäftigen, z. B. Sicherheitsmanagement, Datenschutzmanagement, Compliance Management, Controlling. Diese sollten vertrauensvoll zusammenarbeiten, um Synergieeffekte zu nutzen und Konflikte frühzeitig auszuräumen.

### 1.2 Lebenszyklus

Im Rahmen des Compliance Managements ist eine Reihe von Maßnahmen umzusetzen, beginnend mit der Konzeption über den Aufbau geeigneter Organisationsstrukturen bis hin zur regelmäßigen Revision. Die Schritte, die dabei zu durchlaufen sind, sowie die Maßnahmen, die in den jeweiligen Schritten beachtet werden sollten, sind im Folgenden aufgeführt. 

**Planung und Konzeption**

Es sollten Prozesse und Organisationsstrukturen etabliert sein, um den Überblick über die verschiedenen Anforderungen zu gewährleisten (siehe ORP.5.A4 Konzeption und Organisation des Compliance Managements). Neben den externen Regelungen, die die Institution betreffen, müssen auch die internen Richtlinien und Anforderungen definiert und transparent sein. Eine wichtige Grundlage, um alle geschäftsrelevanten Informationen, Geschäftsprozesse und Systeme angemessen abzusichern, ist die Einstufung von deren Schutzbedarf (siehe ORP.5.A10 Klassifizierung von Informationen). In der Folge leiten sich daraus konkrete Sicherheitsvorgaben für diese Objekte ab.

**Umsetzung**

Die identifizierten Anforderungen werden durch die Managementprozesse der Institution, insbesondere auch durch den Sicherheitsprozess, umgesetzt. Mitarbeiter, aber auch Besucher und externe Dienstleister müssen auf ihre Sorgfaltspflichten und die einzuhaltenden Maßnahmen im Umgang mit Informationen und IT-Systemen hingewiesen werden, bevor sie Zugang oder Zugriff darauf erhalten (siehe ORP.5.A3 Verpflichtung der Mitarbeiter auf Einhaltung einschlägiger Gesetze, Vorschriften und Regelungen).

**Betrieb**

Die Sicherheitsvorgaben, die die Institution zur Erfüllungen der Anforderungen erstellt hat, müssen dauerhaft eingehalten werden. Dies sollte regelmäßig überprüft werden (siehe ORP.5.A7 Aufrechterhaltung der Informationssicherheit). Sowohl die eigenen Regelungen als auch die rechtlichen Rahmenbedingungen, denen eine Institution unterliegt, können sich ändern. Dies muss im Rahmen des Compliance Managements berücksichtigt werden (siehe ORP.5.A2 Beachtung rechtlicher Rahmenbedingungen ).

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Compliance Management (Anforderungsmanagement)" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### ORP.5.M1 Identifikation der rechtlichen Rahmenbedingungen [Leiter Organisation, Institutionsleitung]

Ein Server muss grundsätzlich in einem abschließbaren Rechnerraum oder Serverschrank aufgestellt oder eingebaut werden. Dabei ist zu regeln, wer Zutritt zu dem Raum beziehungsweise Zugang auf den Server selbst erhält. Hierfür sind die Anforderungen der Bausteine INF.5 Technikraum, INF.6 Schutzschrank, beziehungsweise Rechenzentrum umzusetzen.

#### ORP.5.M2 Beachtung rechtlicher Rahmenbedingungen [Vorgesetzte, Leiter Organisation, Institutionsleitung]

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

#### ORP.5.M3 Verpflichtung der Mitarbeiter auf Einhaltung einschlägiger Gesetze, Vorschriften und Regelungen [Vorgesetzte, Personalabteilung]

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

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Compliance Management (Anforderungsmanagement)".

#### ORP.5.M4 Konzeption und Organisation des Compliance Managements [Institutionsleitung]

Grundsätzlich kann zwischen Kennungen für Benutzer- und Administratoren unterschieden werden. Nur Administratoren verwalten die IT-Systeme, während normale Benutzerkennungen nur die Rechte besitzen, um ihre arbeitsplatzspezifischen Aufgaben erfüllen zu können. Normale Benutzerkennungen dürfen keine Administrationsrechte besitzen, damit das Betriebssystem und die Konfiguration der Clients vor versehentlicher, fahrlässiger oder vorsätzlicher Modifikation durch die Benutzer geschützt werden. 

Falls Benutzer nur bestimmte administrative Aufgaben wahrnehmen müssen, ist es oftmals nicht erforderlich, ihnen alle mit einem eigenen Login verbundenen Rechte oder sogar Systemadministrator-Rechte zu geben. Beispiele sind bestimmte Tätigkeiten der routinemäßigen Systemverwaltung, wie die Erstellung von Backups oder das Einrichten eines neuen Benutzers, die mit einem Programm menügesteuert durchgeführt werden, oder Tätigkeiten, für die ein Benutzer nur ein einzelnes Anwendungsprogramm benötigt. Insbesondere bei Aushilfskräften und externen Dienstleistern sollte darauf geachtet werden, dass diese nur die Dienste verwenden und nur auf die Daten zugreifen dürfen, die sie tatsächlich benötigen. Wenn ihre Tätigkeit beendet ist, sollten deren Accounts deaktiviert und alle Zugangsberechtigungen entfernt werden.

Für diese Benutzer sollte eine eingeschränkte Benutzerumgebung geschaffen werden. Sie kann zum Beispiel unter Unix durch eine Restricted Shell (rsh) und eine Beschränkung der Zugriffspfade mit dem Unix-Kommando chroot realisiert werden. Eine weitere Möglichkeit besteht darin, einzelne Anwendungsprogramme, wie Web-Browser, im sogenannten Kiosk-Modus auszuführen, so dass nur ein beschränkter Zugriff besteht.

Werden an Benutzerkennungen besonders weitgehende Rechte vergeben, so sollte dies möglichst restriktiv erfolgen. Hierbei sollte zum einem der Kreis der privilegierten Benutzer möglichst eingeschränkt werden und zum anderen nur die für die Durchführung der Arbeit benötigten Rechte vergeben werden. Für alle Aufgaben, die ohne erweiterte Rechte durchgeführt werden können, sollten auch privilegierte Benutzer unter Kennungen mit Standard-Rechten arbeiten. 

#### ORP.5.M5 Ausnahmegenehmigungen [Vorgesetzte, Informationssicherheitsbeauftragter (ISB)]

Es gibt unterschiedliche Zugangssmöglichkeiten, um Server zu administrieren. Abhängig von der genutzten Zugangsart müssen eine Reihe von Sicherheitsvorkehrungen getroffen werden. Bei größeren Netzen ist es empfehlenswert, auch die Server in ein zentrales Netzmanagement-System einzubinden, da sonst eine sichere und effiziente Administration kaum gewährleistet werden kann. Die zur Administration verwendeten Methoden müssen in der Sicherheitsrichtlinie festgelegt werden und die Administration darf nur entsprechend der Sicherheitsrichtlinie durchgeführt werden.

Allgemein ist es wichtig, einen Überblick darüber zu erhalten, welcher Teil der Administration eines Servers normalerweise

* lokal über die Konsole,
* remote über das Netz, aber unter Nutzung der Standardmechanismen des Betriebssystems, oder
* über ein zentrales netzbasiertes Administrationswerkzeug
durchgeführt werden soll. Es wird empfohlen, für die verschiedenen Nutzungsarten eine Übersicht zu erstellen, welche Administrationstätigkeiten auf welchem Weg durchgeführt werden können. Insbesondere ist es wichtig festzuhalten, ob bestimmte Tätigkeiten auf einem bestimmten Weg normalerweise nicht durchgeführt werden dürfen. 

* Lokale AdministrationEin Server sollte prinzipiell in einem Serverraum oder zumindest einem abschließbaren Serverschrank aufgestellt sein. Für den Teil der Administration, der trotzdem teilweise lokal über die Konsole erfolgen soll oder muss, müssen entsprechende Vorgaben dafür gemacht werden, wer Zugang zur Konsole erhält, welche Art der Authentisierung für den lokalen Zugang genutzt werden darf und welche anderen Vorgaben berücksichtigt werden müssen. 
* Remote-AdministrationMeist wird ein Server nicht lokal an der Konsole sondern von einem Arbeitsplatzrechner aus über das Netz administriert. Um zu verhindern, dass dabei Authentisierungsinformationen der Administratoren und Konfigurationsdaten der Server abgehört oder gar von einem Angreifer manipuliert werden, sollte die Administration nur über sichere Protokolle (beispielsweise nicht über Telnet, sondern über SSH, nicht über HTTP, sondern über HTTPS) erfolgen. Alternativ kann ein eigenes Administrationsnetz eingerichtet werden, das vom dem restlichen Netz getrennt ist.Eine ungesicherte Remote-Administration über externe (unsichere) Netze hinweg darf in keinem Fall erfolgen. Dies muss bereits bei der Festlegung der Sicherheitsrichtlinie berücksichtigt werden. Auch im internen Netz sollten, soweit möglich, keine unsicheren Protokolle verwendet werden. 
* Administration über ein zentrales ManagementsystemFalls für die Administration des Servers ein zentrales Managementsystem genutzt werden soll, so sollten für diesen Zugangsweg analoge Vorüberlegungen angestellt werden, wie für die Remote-Administration. Zusätzlich ist es wichtig, dass das zentrale Managementsystem selbst entsprechend sicher konfiguriert und administriert wird. 
**Sichere Authentisierung**

IT-Systeme aller Art sollten grundsätzlich sicherstellen, dass sich alle Benutzer, die darauf zugreifen möchten, authentisieren müssen. Nur so kann verhindert werden, dass unautorisierte Personen Zugang auf die Dienste erlangen, die das System anbietet, oder auf die Daten, die auf dem System gespeichert sind. 

In der Regel werden Server über eine Netzverbindung administriert. Die Informationen, die für eine netzbasierte Authentisierung benötigt werden, müssen hierfür über ein LAN oder WAN übertragen werden. Daher ist es zwingend erforderlich, dass diese Informationen nicht mitgelesen oder verändert werden können.

Außerdem muss sichergestellt werden, dass ein Angreifer sich nicht anmelden kann, indem er aufgezeichnete Anmeldeinformationen wieder einspielt. Daher müssen die Anmeldeinformationen, die für die Authentisierung zwischen Server und Client ausgetauscht werden, verschlüsselt und zusätzlich, beispielsweise mit Challenge-Response-Verfahren, dynamisiert werden. 

Nachdem die Authentisierung erfolgreich abgelaufen ist, muss das System sicher stellen, dass die Benutzer nur auf solche Dienste und Daten Zugriff erhalten, für die sie entsprechende Berechtigungen besitzen.

Wenn die Gefahr des Abhörens von Leitungen zu Terminals besteht, sollten Administratoren nur an der Konsole arbeiten, damit keine Passwörter abgehört werden können. Bei der Administration von Unix-Systemen kann eine verschlüsselte Kommunikation beispielsweise mit dem Protokoll Secure Shell erfolgen. Hiermit ist eine gesicherte Administration von entfernten Arbeitsstationen aus möglich .

#### ORP.5.M6 Einweisung des Personals in den sicheren Umgang mit IT [Vorgesetzte, Personalabteilung]

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

#### ORP.5.M7 Aufrechterhaltung der Informationssicherheit [Informationssicherheitsbeauftragter (ISB)]

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

#### ORP.5.M8 Regelmäßige Überprüfungen des Compliance Managements

Nur eine regelmäßige und umfassende Datensicherung gewährleistet zuverlässig, dass alle gespeicherten Daten auch im Falle von Störungen, Auswirkungen von Schadsoftware, Ausfällen der Hardware oder (absichtlichen oder unabsichtlichen) Löschungen weiter verfügbar gemacht werden können. Die notwendigen Anforderungen sind im Baustein OPS 1.1.5 Datensicherung beschrieben.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### ORP.5.M9 Schutz gegen nachträgliche Veränderungen von Informationen [Informationssicherheitsbeauftragter (ISB), Benutzer](I)

Dateien, die an Dritte weitergegeben werden, können von diesen im Allgemeinen auch weiterbearbeitet werden. Dies ist nicht immer im Sinne des Erstellers. Daher sollten Daten gegen nachträgliche Veränderungen, auszugsweise Weitergabe oder Verarbeitung geschützt werden.

Häufig steht man vor dem Problem, dass Informationen über das Internet oder andere Netze Dritten zwar zur Verfügung gestellt, aber nicht hundertfach ausgedruckt oder nahtlos in andere Werke integriert werden sollen.

Hierzu gibt es verschiedene Lösungen, die teilweise auch miteinander kombiniert werden können. Beispiele hierfür sind:

* Die Verwendung von digitalen Signaturen, um unbemerkte Änderungen an Dateien zu verhindern (siehe auch CON.1 Kryptokonzept).
* Das Hinzufügen von Urheberrechts-Vermerken zu Informationen, wie Broschüren oder Dateien auf Webseiten. Diese können wie folgt lauten: "Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. Jede Verwertung außerhalb der Bestimmungen des Urheberrechtsgesetzes ohne Zustimmung des Autors ist unzulässig und strafbar." sowie "Copyright (©) 7/2016 by BSI".
* Die Verwendung von Dateiformaten, die nachträgliche Änderungen bzw. auszugsweise Weiterverarbeitung erschweren. Hierfür kann z. B. Postscript genutzt werden oder die Sicherheitseigenschaften von Anwendungsprogrammen, z. B. bei PDF-Dateien.
Viele Anwendungsprogramme bieten Sicherheitsmechanismen an, um den weiteren Umgang mit den erstellten Dateien einzuschränken. Im Folgenden werden einige solcher Sicherheitsmechanismen am Beispiel von PDF-Dateien vorgestellt. Da die Sicherheitsmechanismen der verschiedenen Anwendungsprogramme sehr unterschiedlich ausgeprägt sind und teilweise sogar von Version zu Version variieren, ist es wichtig, die Mitarbeiter darüber zu informieren, wie diese zu benutzen sind und welche Schritte vor der Weitergabe von elektronischen Dokumenten zu beachten sind. Es ist häufig sinnvoll, einen Mitarbeiter (plus Vertreter) gründlich hierzu auszubilden. Dieser sollte dann alle weiterzugebenden Dokumente entsprechend der Sicherheitsvorgaben bearbeiten oder als Ansprechpartner zur Verfügung stehen.

**Schutz von PDF-Dokumenten**

PDF-Dokumente können bei der Erstellung mit Zugriffsbeschränkungen versehen werden. So kann z. B. das Öffnen, Drucken oder Kopieren von PDF-Dateien eingeschränkt werden.

* Häufig sollen in einem Dokument vor dessen Veröffentlichung einzelne Passagen unkenntlich gemacht werden. Eine beliebte, aber extrem fehlerträchtige Methode ist es, Textpassagen elektronisch zu "schwärzen".Die so übermalten Informationen sind allerdings in vielen Fällen einfach auslesbar. Daher ist dies unbedingt zu unterlassen. 
* Durch die Verwendung von kryptographischen Verfahren können PDF-Dokumente signiert oder so verschlüsselt werden, dass nur bestimmte Anwender diese benutzen können. 
* Es können PDF-Sicherheitsrichtlinien erstellt werden. Diese kann jeder Benutzer für sich erstellen oder es können von der Institution vorgegebene Sicherheitsrichtlinien verwendet werden, hierfür ist ein Adobe Policy Server erforderlich. 
* DateischutzMit Adobe Acrobat, also der verbreitetsten Anwendung, mit der PDF-Dateien erstellt und nachbearbeitet werden können, ist die Vergabe von zwei Arten von Passwörtern möglich. Die einen werden zum Öffnen des Dokuments, die anderen zum Ändern der Sicherheitsattribute benötigt. Bei der Vergabe eines Passwortes wird zunächst danach gefragt, zu welchen Programmversionen die Schutzfunktion kompatibel sein soll. Bis zur Version "Adobe 5.0 und höher" ist dabei nur eine 40-Bit-Verschlüsselung mit RC4 möglich, ab "Adobe 5.0 und höher" ist eine 128-Bit-Verschlüsselung mit RC4 und ab "Adobe 7.0 und höher" ist eine 128-Bit-Verschlüsselung mit AES vorgesehen. Es sollte darauf geachtet werden, mindestens mit 128 Bit zu verschlüsseln, da der Dokumentenschutz sonst einfach ausgehebelt werden kann.Über die Sicherheitsattribute können unter anderem folgende Funktionen eingeschränkt werden: 

 
	+ Öffnen des Dokuments
	+ Drucken
	+ Ändern des Dokuments
	+ Kopieren von Texten, Bildern oder anderen Inhalte
	+ Zugriff auf Metadaten eines Dokuments
	+ Notizen und Formularfelder hinzufügen oder ändern
	  

 
Es sollte genau überlegt werden, welche Metadaten die Datei enthalten soll. Hier kann es beispielsweise erwünscht sein, einer Datei eine Vielzahl von Metadaten mitzugeben, damit dieses über Suchmaschinen gefunden werden kann. Es kann aber auch sinnvoll sein, keine Metadaten weiterzugeben, beispielsweise sollte der Name des Autors entfernt werden, wenn ein Dokument anonymisiert weitergegeben werden soll.

Leider bietet dies nur einen rudimentären Schutz, da PDF-Dateien (abhängig von der Programmversion, mit der sie erstellt wurden) auch mit Programmen geöffnet werden können, die diese Sicherheitsattribute ignorieren. Solange z. B. Drucken erlaubt wird, kann das Dokument sogar jederzeit wieder in eine PDF-Datei ohne jegliche Einschränkungen verwandelt werden.

Es muss also beachtet werden, dass je nach verwendetem Anwendungsprogramm, verwendeter Version und eingestellten Optionen mit den zur Verfügung gestellten Programmeigenschaften kein ausreichender Schutz erzielt werden kann. Je nach Schutzbedarf müssen Dateien daher mit kryptographischen Verfahren signiert werden (siehe auch CON.1 Kryptokonzept).

#### ORP.5.M10 Klassifizierung von Informationen(CIA)

Grundsätzlich sollten Mitarbeiter natürlich sorgfältig mit allen Informationen umgehen. Darüber hinaus gibt es aber in vielen Bereichen Daten, die einen höheren Schutzbedarf haben oder besonderen Restriktionen unterliegen, z. B. personenbezogene, finanzrelevante, vertrauliche oder Copyright-geschützte Daten. Für diese gelten je nach ihrer Kategorisierung unterschiedliche Beschränkungen im Umgang mit ihnen. Daher ist es wichtig, alle Mitarbeiter auf die für diese Daten geltenden Restriktionen hinzuweisen (siehe auch ORP.5.A3 Verpflichtung der Mitarbeiter auf Einhaltung einschlägiger Gesetze, Vorschriften und Regelungen ). Die Daten sollten möglichst entsprechend gekennzeichnet werden, z. B. indem die Kategorie bei Dokumenten in der Kopf- oder Fußzeile genannt wird.

Der Schutzbedarf von Daten wirkt sich natürlich unmittelbar auf alle Medien aus, auf denen diese gespeichert oder verarbeitet werden. Daten mit besonderem Schutzbedarf können in den unterschiedlichsten Bereichen anfallen, z. B. bei Fax oder E-Mail. Es sollte also in allen Bereichen Regelungen geben, in denen auch festgelegt ist, wer solche Daten lesen, bearbeiten bzw. weitergeben darf. Dazu gehört, falls erforderlich, auch die regelmäßige Überprüfung auf Korrektheit und Vollständigkeit der Daten.

Viele Informationen, aber auch Anwendungen, unterliegen Copyright-Vermerken oder Weitergaberestriktionen ("Nur für den internen Gebrauch"). Alle Mitarbeiter müssen darauf hingewiesen werden, dass weder Dokumente, noch Dateien oder Software ohne Berücksichtigung eventueller Copyright-Vermerke oder Lizenzbedingungen kopiert werden dürfen. 

Ein besonderes Augenmerk muss auch auf alle Informationen gelegt werden, die die Grundlage für die Aufgabenerfüllung bilden. Dazu gehören alle geschäftsrelevanten Daten, also z. B. diejenigen Daten, bei deren Verlust die Institution handlungsunfähig wird, die die wirtschaftlichen Beziehungen zusammenarbeitender Unternehmen beeinträchtigen können oder aus deren Kenntnis ein Dritter (z. B. Konkurrenzunternehmen) finanzielle Vorteile ziehen kann. Jede Behörde und jedes Unternehmen sollte eine Übersicht darüber haben, welche Daten als geschäftskritisch einzustufen sind. Neben den allgemeinen Sorgfaltspflichten können auch hier für diese Daten bei der Speicherung, Verarbeitung, Weitergabe und Vernichtung besondere Vorschriften und Regelungen gelten. Diese geschäftskritischen Informationen müssen vor Verlust, Manipulation und Verfälschung geschützt werden. Längerfristig gespeicherte oder archivierte Daten müssen regelmäßig auf ihre Lesbarkeit getestet werden. Nicht mehr benötigte Informationen müssen zuverlässig gelöscht werden (siehe auch CON.7 Löschen und Vernichten). 

#### ORP.5.M11 Erhebung der rechtlichen Rahmenbedingungen für kryptographische Verfahren und Produkte [IT-Betrieb, Verantwortliche der einzelnen Anwendungen](CI)

Bevor eine Entscheidung getroffen werden kann, welche kryptographischen Verfahren und Produkte eingesetzt werden sollen, müssen eine Reihe von Einflussfaktoren ermittelt werden. Dazu können die Systemadministratoren und die Verantwortlichen der einzelnen -Systeme bzw. IT-Anwendungen befragt werden. Die Ergebnisse müssen nachvollziehbar z. B. in einem Kryptokonzept dokumentiert werden (siehe auch CON.1 Kryptokonzept).

Für sämtliche festgelegten Speicherorte und Übertragungsstrecken sind folgende Einflussfaktoren zu ermitteln:

* Sicherheitsaspekte, z. B. zu erreichender Schutzbedarf und Angreiferpotential
* Technische Aspekte, z.B. IT-Systemumfeld, Datenvolumen, Performance
* Personelle und organisatorische Aspekte, z. B. Benutzerfreundlichkeit, Schulungsbedarf, zusätzlicher Personalbedarf
* Wirtschaftliche Aspekte, z. B. einmalige Investitionen, laufende Kosten, Personalkosten, Lizenzgebühren
* Einsatz von Key-Recovery-Mechanismen
* maximale Lebensdauer der kryptographischen Verfahren
* gesetzliche Rahmenbedingungen beim Einsatz kryptographischer Produkte
Beim Einsatz kryptographischer Produkte sind diverse gesetzliche Rahmenbedingungen zu beachten. In einigen Ländern dürfen beispielsweise kryptographische Verfahren nicht ohne Genehmigung eingesetzt werden. Daher muss untersucht werden,

* ob innerhalb der zum Einsatzgebiet gehörenden Länder Einschränkungen beim Einsatz kryptographischer Produkte zu beachten sind (innerhalb Deutschland gibt es keinerlei Einschränkungen) und
* ob für infrage kommende Produkte Exportbeschränkungen beachtet werden müssen.
Werden mobile IT-Systeme oder Komponenten auf Auslandsreisen eingesetzt, muss vor jedem Grenzübertritt geklärt werden, welche länderspezifischen Regelungen zu beachten sind (siehe auch CON.8 Sicherheit auf Auslandsreisen).

Es gibt allerdings nicht nur Maximalanforderungen, sondern auch Minimalanforderungen an die verwendeten kryptographischen Algorithmen oder Verfahren. So müssen z. B. bei der Übermittlung von personenbezogenen Daten Verschlüsselungsverfahren mit ausreichender Schlüssellänge eingesetzt werden.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Compliance Management (Anforderungsmanagement)" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [19600] ISO 19600:2014

  

 ISO, Compliance management systems, 2014 

 
* #### [27002K18] ISO/IEC 27002:2013 Kapitel 18 Compliance

  

 ISO, Information technology-security technique- Code of practice for information on security controls, insbesondere Kapitel 18 "Compliance", 2013

 
* #### [GSKHM] Hilfsmittel zur Nutzung der IT-Grundschutz-Kataloge

  

 BSI, (zuletzt abgerufen am 05.10.2017)  
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine_node.html)

 
* #### [ISFSM2.3] Standard of Good Practice for Inforation Security 2016 SM2.3 und SI2.3

  

 Information Security Forum Limited, insbesondere SM2.3 Legal and Regulatory Compliance und SI2.3 Information Security Compliance Monitoring, (zuletzt abgerufen 05.10.2017)  
 <www.securityforum.org>

 
