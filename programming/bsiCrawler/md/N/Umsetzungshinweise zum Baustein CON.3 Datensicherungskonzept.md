1 Beschreibung
--------------

### 1.1 Einleitung

Unternehmen und Behörden speichern immer mehr Daten und sind gleichzeitig immer stärker auf sie angewiesen. Gehen Daten dann verloren, z. B. durch defekte Hardware oder Malware, können gravierende Schäden entstehen. Durch regelmäßige Datensicherungen lassen sich solche Auswirkungen jedoch minimieren: Eine Datensicherung soll gewährleisten, dass durch einen redundanten Datenbestand der IT-Betrieb kurzfristig wiederaufgenommen werden kann, wenn Teile des operativen Datenbestandes verloren gehen.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Um eine effektive Datensicherung einzurichten, müssen zuerst mögliche Einflussfaktoren identifiziert (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) und danach eine geeignete Verfahrensweise festgelegt werden (siehe CON.3.M2 *Festlegung der Verfahrensweise für die Datensicherung*). Darauf aufbauend müssen die Verantwortlichen ein Minimaldatensicherungskonzept (siehe CON.3.M4 *Erstellung eines Minimaldatensicherungskonzeptes*) und ein Datensicherungskonzept (siehe CON.3.M6 *Entwicklung eines Datensicherungskonzepts*) entwickeln. 

**Beschaffung**

Datensicherungen werden meistens mithilfe von Backup-Programmen durchgeführt. Allerdings sind nicht alle Programme für jede Institution geeignet. Deswegen muss die Sicherungssoftware sorgfältig ausgesucht werden (siehe CON.3.M7 *Beschaffung eines geeigneten Datensicherungssystems*). 

**Umsetzung**

Alle Mitarbeiter müssen über die Datensicherungen informiert werden und sollten wissen, welche Aufgaben sie selbst dabei zu erfüllen haben (siehe CON.3.M10 *Verpflichtung der Mitarbeiter zur Datensicherung*). Ebenso sollte eine Sicherungskopie der eingesetzten Software erstellt werden (siehe CON.3.M11 *Sicherungskopie der eingesetzten Software*). 

Alle Datensicherungen sind geeignet zu dokumentieren (siehe CON.3.M6 *Entwicklung eines Datensicherungskonzepts*). 

**Betrieb**

Die im Datensicherungskonzept vorgegebenen Schritte und Verfahrensweise müssen regelmäßig durchgeführt werden (siehe CON.3.M5 *Regelmäßige Datensicherung*). 

Datensicherungen enthalten meistens sehr viele schützenswerte Information über die Institution. Deshalb muss dafür gesorgt werden, dass die Backup-Datenträger geschützt aufbewahrt sind (siehe CON.3.M12 *Geeignete Aufbewahrung der Backup-Datenträger*).

**Notfallvorsorge**

Datensicherungen müssen im Notfall auch funktionieren, d. h. die gesicherten Daten müssen sich problemlos und schnell wieder einspielen lassen. Um das sicherzustellen, müssen regelmäßige Tests durchgeführt werden (siehe CON.3.A8 *Funktionstests und Überprüfung der Wiederherstellbarkeit*).

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Datensicherungskonzept" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### CON.3.M1 Erhebung der Einflussfaktoren der Datensicherung [IT-Betrieb, Fachverantwortliche]

Für jedes IT-System, eventuell sogar für einzelne IT-Anwendungen mit besonderer Bedeutung, müssen die nachfolgenden Einflussfaktoren ermittelt werden. Dazu können die Systemadministratoren und die Verantwortlichen der einzelnen IT-Anwendungen befragt werden. Die Ergebnisse sind nachvollziehbar zu dokumentieren. Im einzelnen muss ermittelt werden:

* Spezifikation der zu sichernden Daten: Ermittelt werden sollte der Datenbestand des IT-Systems (der IT-Anwendung), der für die Fachaufgaben erforderlich ist. Dazu gehören die Anwendungs- und Betriebssoftware, die Systemdaten (z. B. Initialisierungsdateien, Makrodefinitionen, Konfigurationsdaten, Textbausteine, Passwortdateien, Zugriffsrechtedateien), die Anwendungsdaten selbst und Protokolldaten (z.B. Login-Protokollierung, Protokolle über Sicherheitsverletzungen, Datenübertragungsprotokolle).
* Verfügbarkeitsanforderungen der IT-Anwendungen an die Daten: Für die im ersten Schritt spezifizierten Daten müssen nun die Verfügbarkeitsanforderungen festgelegt werden. Ein erprobtes Maß dazu ist die Angabe der maximal tolerierbaren Ausfallzeit. Sie gibt an, über welchen Zeitraum die Fachaufgabe ohne diese Daten weitergeführt werden kann, ohne dass auf Datensicherungsbestände zurückgegriffen werden muss. 
* Rekonstruktionsaufwand der Daten ohne Datensicherung: Um ein unter wirtschaftlichen Gesichtspunkten angemessenes Datensicherungskonzept zu entwickeln (siehe CON.3.M6 Entwicklung eines Datensicherungskonzepts), ist es notwendig zu wissen, ob und mit welchem Aufwand zerstörte Datenbestände rekonstruiert werden können, wenn eine Datensicherung nicht verfügbar ist. Untersucht werden sollte, aus welchen Quellen die Daten rekonstruiert werden können und wie lange das dauern würde. Beispiele hierfür sind die Aktenlage, Ausdrucke, Befragungen und Erhebungen.
* Datenvolumen: Für die Auswahl des Speichermediums ist ein entscheidender Faktor das gespeicherte und zu sichernde Datenvolumen. 
* Änderungsvolumen: Um die Häufigkeit der Datensicherung und das adäquate Sicherungsverfahren bestimmen zu können, muss bekannt sein, wie viele Daten sich in einem bestimmten Zeitabschnitt ändern. Notwendig sind Angaben, ob bestehende Dateien inhaltlich geändert oder ob neue Dateien erzeugt werden.
* Änderungszeitpunkte der Daten: Es gibt IT-Anwendungen, bei denen sich Datenänderungen nur zu bestimmten Terminen ergeben, wie zum Beispiel der Abrechnungslauf zur Lohnbuchhaltung zum Monatsende. In solchen Fällen ist eine Datensicherung unverzüglich nach einem solchen Termin sinnvoll. Daher sollte für die zu sichernden Daten angegeben werden, ob sie sich täglich, wöchentlich oder zu bestimmten Terminen ändern.
* Fristen: Für die Daten ist zu klären, ob bestimmte Fristen einzuhalten sind. Hierbei kann es sich um Aufbewahrungsfristen oder auch um Löschfristen im Zusammenhang mit personenbezogenen Daten handeln. Diese Fristen sind bei der Datensicherung zu berücksichtigen.
* Vertraulichkeitsbedarf der Daten: Der Vertraulichkeitsbedarf einer Datei überträgt sich bei einer Datensicherung auf die Sicherungskopie.
* Integritätsbedarf der Daten: Für Datensicherungen muss sichergestellt sein, dass die Daten integer gespeichert wurden und während der Aufbewahrungszeit nicht verändert werden. Das ist um so wichtiger, je höher der Integritätsbedarf der Nutzdaten ist. Daher ist für die Datensicherungen anzugeben, wie hoch der Integritätsbedarf ist.
* Kenntnisse und Fähigkeiten der IT-Benutzer: Um entscheiden zu können, wer die Datensicherung durchführt, der IT-Benutzer selbst oder speziell beauftragte Mitarbeiter bzw. die Systemadministratoren, ist ausschlaggebend, über welche Kenntnisse und Fähigkeiten der IT-Benutzer verfügt und welche Werkzeuge ihm zur Verfügung gestellt werden können. Falls die zeitliche Belastung bei der Durchführung einer Datensicherung für IT-Benutzer zu hoch ist, sollte dies angegeben werden.
#### CON.3.M2 Festlegung der Verfahrensweise für die Datensicherung [IT-Betrieb, Fachverantwortliche]

Wie eine Datensicherung durchzuführen ist, wird hauptsächlich von den in CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung* erhobenen Einflussfaktoren bestimmt. Für jedes IT-System und für jede Datenart muss die Verfahrensweise der Datensicherung festgelegt werden. Bei Bedarf ist sogar noch eine Unterscheidung für einzelne IT-Anwendungen des jeweiligen IT-Systems vorzunehmen.

Folgende Punkte sind bei der Festlegung einer Verfahrensweise für die Datensicherung zu betrachten:

* Art der Datensicherung,
* Häufigkeit und Zeitpunkt der Datensicherung,
* Anzahl der Generationen,
* Vorgehensweise und Speichermedium,
* Verantwortlichkeit für die Datensicherung,
* Aufbewahrungsort,
* Anforderungen an das Datensicherungsarchiv,
* Transportmodalitäten und
* Aufbewahrungsmodalität.
In der nachfolgenden Tabelle werden die Abhängigkeiten zwischen den genannten Punkten und den Einflussfaktoren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) dargestellt und anschließend erläutert:

Tabelle: Datensicherung

**Art der Datensicherung**

Folgende Datensicherungsarten gibt es:

* Volldatensicherung: Bei der Volldatensicherung werden sämtliche zu sichernden Dateien zu einem bestimmten Zeitpunkt auf einen zusätzlichen Datenträger gespeichert. Es wird dabei nicht berücksichtigt, ob die Dateien sich seit der letzten Datensicherung geändert haben oder nicht. Daher benötigt eine Volldatensicherung viel Speicher. Der Vorteil ist, dass die Daten vollständig für den Sicherungszeitpunkt vorliegen und die Restaurierung von Dateien einfach und schnell möglich ist, da nur die betroffenen Dateien aus der letzten Volldatensicherung extrahiert werden müssen. Werden Volldatensicherungen selten durchgeführt, so kann sich durch umfangreiche nachträgliche Änderungen innerhalb einer Datei ein hoher Nacherfassungsaufwand ergeben.
* Inkrementelle Datensicherung: Bei der inkrementellen Datensicherung werden im Gegensatz zur Volldatensicherung nur die Dateien gesichert, die sich gegenüber der letzten Datensicherung (Volldatensicherung oder inkrementelle Sicherung) geändert haben. Das spart Speicherplatz und verkürzt die erforderliche Zeit für die Datensicherung. Die inkrementelle Datensicherung basiert immer auf einer Volldatensicherung. In periodischen Zeitabständen werden Volldatensicherungen erzeugt, in der Zeit dazwischen werden eine oder mehrere inkrementelle Datensicherungen vollzogen. Bei der Restaurierung wird die letzte Volldatensicherung als Grundlage genommen, die um die in der Zwischenzeit geänderten Dateien aus den inkrementellen Sicherungen ergänzt wird.
* Differenzielle Datensicherung: Bei der differenziellen Datensicherung werden jedes Mal die Dateien gesichert, die sich gegenüber der letzten Volldatensicherung geändert haben. Eine differenzielle Datensicherung benötigt mehr Speicherplatz als eine inkrementelle, Dateien lassen sich aber einfacher und schneller restaurieren. Für die Restaurierung der Daten reicht die letzte Volldatensicherung sowie die aktuellste differenzielle, nicht wie bei der inkrementellen, wo unter Umständen mehrere Datensicherungen nacheinander eingelesen werden müssen.
* Spiegelung: Bei einer Datenspiegelung wird permanent eine exakte Kopie der Daten in einem anderen Verzeichnis oder Medium erstellt. Dies geschieht in der Regel transparent für den Benutzer, beispielsweise durch ein RAID-System. Eine Spiegelung alleine ersetzt keine Datensicherung, da Inkonsistenzen, Dateifehler oder Löschungen von Dateien sich sofort auf die gespiegelte Version auswirkt. Werden beispielsweise die originalen Datenbestände durch Ransomware verschlüsselt, wirkt sich dies direkt auf die gespiegelte Kopie aus.
Eine spezielle Form der genannten Datensicherungsstrategien ist die Image-Datensicherung. Hier werden nicht die einzelnen Dateien eines Festplattenstapels gesichert, sondern die physikalischen Sektoren der Festplatte. Es handelt sich dabei um eine Vollsicherung, die sehr schnell auf eine gleichartige Festplatte restauriert werden kann.

Eine weitere Form ist das Hierarchische Speicher-Management (HSM). Hierbei geht es in erster Linie darum, vorhandenen Speicher möglichst wirtschaftlich zu nutzen. Dateien werden abhängig von der Häufigkeit, mit der auf sie zugegriffen wird, auf schnellen Online-Speichern (Festplatten) gehalten, auf Nearline-Speicher (automatische Datenträger-Wechselsysteme) ausgelagert oder auf Offline-Speichern (Magnetbänder) archiviert. Gleichzeitig bieten diese HSM-Systeme auch automatische Datensicherungsroutinen kombiniert aus inkrementeller Datensicherung und Volldatensicherung.

Eine redundante Datenspeicherung bieten RAID-Systeme an (Redundant Array of Inexpensive Disks). Das RAID-Konzept beschreibt die Verbindung von mehreren Festplatten unter dem Kommando eines sogenannten Array-Controllers. Es gibt verschiedene RAID-Level, wovon RAID-Level 1 die Datenspiegelung beschreibt. RAID-Systeme ersetzen jedoch keine Datensicherung! Sie helfen nicht bei Diebstahl oder Brand, daher müssen auch die auf RAID-Systemen gespeicherten Daten auf zusätzliche Medien gesichert werden und diese Medien auch in anderen Brandabschnitten untergebracht werden.

Für die Entscheidung, welche Datensicherungsstrategie angewendet werden soll, sind die folgenden Einflussfaktoren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) zu berücksichtigen, um eine für die Anforderungen geeignete und gleichzeitig wirtschaftliche Form zu finden:

* Verfügbarkeitsanforderungen: Sind die Verfügbarkeitsanforderungen sehr hoch, so ist eine Datenspiegelung in Erwägung zu ziehen. Sind die Verfügbarkeitsanforderungen hoch, so sollte einer Volldatensicherung statt einer inkrementellen Datensicherung durchgeführt werden.
* Datenvolumen und Änderungsvolumen: Entspricht das Änderungsvolumen annähernd dem Datenvolumen (z. B. bei der Nutzung einer Datenbank), so verringert sich die Speicherplatzersparnis der inkrementellen Datensicherung so stark, dass eine Vollsicherung erwogen werden kann. Ist jedoch das Änderungsvolumen erheblich kleiner als das Datenvolumen, so spart die inkrementelle Datensicherung Speicherplatz.
* Änderungszeitpunkte der Daten: Einen geringen Einfluss auf die Datensicherungsstrategie können die Änderungszeitpunkte der Daten haben. Gibt es Zeitpunkte, an denen anwendungsbezogen der Komplettdatenbestand gesichert werden muss (z. B. nach buchhalterischen Wochen-, Monats- oder Jahresabschlüsse), so kommt zu diesen Zeitpunkten nur eine Vollsicherung infrage. 
* Kenntnisse der IT-Benutzer: Eine Datenspiegelung setzt entsprechende Kenntnisse des Systemadministrators voraus, erfordert jedoch vom Benutzer keinerlei Kenntnisse. Eine Volldatensicherung lässt sich auch von einem IT-Benutzer mit geringen Systemkenntnissen durchführen. Demgegenüber erfordert eine inkrementelle Datensicherung schon mehr Systemkenntnisse und Erfahrungen im Umgang mit Datensicherungen.
**Häufigkeit und Zeitpunkte der Datensicherung**

Tritt ein Datenverlust ein, sind alle Daten bis zur letzten Sicherung verloren. Je aktueller die letzte Datensicherung ist, desto weniger Datenverlust muss die Institution verkraften. Gleichzeitig muss beachtet werden, dass der Zeitpunkt der Datensicherung nicht nur periodisch (z.B. täglich, wöchentlich, werktags) gewählt werden kann, sondern dass auch ereignisabhängige Datensicherungen (z. B. nach x Transaktionen, nach Ausführung eines bestimmten Programms, nach Systemänderungen) notwendig sein können.

Bei der Auswahl der Häufigkeit und der Zeitpunkte der Datensicherung sind folgende Einflussfaktoren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) zu beachten: 

* Verfügbarkeitsanforderungen, Wiederherstellungsaufwand ohne Datensicherung und Änderungsvolumen: Der zeitliche Abstand der Datensicherungen ist so zu wählen, dass die Restaurierungs- und Nacherfassungszeit (Rekonstruktionsaufwand der geänderten Daten, für die keine Datensicherung vorhanden ist) der in diesem Zeitraum geänderten Daten (Änderungsvolumen) kleiner als die maximal tolerierbare Ausfallzeit ist. 
* Änderungszeitpunkte der Daten: Gibt es Zeitpunkte, an denen sich die Daten in großem Umfang ändern (z. B. Programmlauf für Gehaltszahlung oder Versionswechsel der Software) oder an denen der Komplettdatenbestand vorliegen muss, so bietet es sich an, unmittelbar danach eine Volldatensicherung durchzuführen. Dazu sind neben den periodischen die ereignisabhängigen Datensicherungszeitpunkte festzulegen. 
**Anzahl der Generationen**

Einerseits werden Datensicherungen in kurzen Zeitabständen wiederholt, um eine Kopie eines möglichst aktuellen Datenbestandes verfügbar zu haben, andererseits muss die Datensicherung gewährleisten, dass gesicherte Daten möglichst lange aufbewahrt werden. Eine Volldatensicherung wird als Generation bezeichnet. Die Anzahl der aufzubewahrenden Generationen und der zeitliche Abstand, der zwischen den Generationen liegen muss, sollte festgelegt werden. Diese Anforderungen lassen sich an folgenden Beispielen erläutern:

* Wird eine Datei absichtlich oder unabsichtlich gelöscht, so ist diese Datei in allen späteren Datensicherungen nicht mehr verfügbar. Stellt sich heraus, dass diese gelöschte Datei dennoch benötigt wird, so muss zur Wiederherstellung auf eine ältere Datensicherung zurückgegriffen werden, die zeitlich vor dem Löschen erstellt wurde. Ist eine solche Generation nicht mehr vorhanden, so muss die Datei neu erfasst werden.
* Tritt ein Integritätsverlust in einer Datei auf, z. B. durch Malware, ist es wahrscheinlich, dass dies nicht direkt, sondern erst zeitlich versetzt bemerkt wird. Um die Integrität der Datei wiederherstellen zu können, muss dann auf eine Generation zurückgegriffen werden, die vor dem Integritätsverlust erstellt wurde.
* Es kann nicht ausgeschlossen werden, dass eine Datensicherung fehlerhaft oder unvollständig erstellt wurde. Deswegen ist es oft hilfreich, wenn auf eine weitere Generation zurückgegriffen werden kann.
Um diese Vorteile des Generationenprinzips aufrechterhalten zu können, muss jedoch eine Randbedingung eingehalten werden: der zeitliche Abstand der Generationen darf ein Mindestmaß nicht unterschreiten. Beispiel: In einem automatisierten Datensicherungsverfahren kommt es zu wiederholten Abbrüchen des Datensicherungslaufs. Hierdurch würden nacheinander sämtliche Generationen überschrieben werden. Verhindert werden kann dies, indem vor Überschreiben einer Generation das Mindestalter überprüft und nur dann überschrieben wird, wenn dieses Alter überschritten ist.

Charakterisieren lässt sich ein Generationsprinzip durch zwei Größen: das Mindestalter der ältesten Generation und die Anzahl der verfügbaren Generationen. Dabei gilt:

* je höher das Mindestalter der ältesten Generation ist, je größer ist die Wahrscheinlichkeit, dass zu einer Datei mit Integritätsverlust (eine gelöschte Datei, die im Nachhinein als notwendig erkannt wird, ist ebenfalls darunter zu fassen) noch eine Vorläuferversion vorhanden ist,
* je größer die Anzahl der verfügbaren Generationen ist, umso aktueller ist die angeforderte Vorläuferversion.
Die Anzahl der Generationen hängt jedoch direkt mit den Kosten der Datensicherung zusammen, weil Datenträger in ausreichender Zahl vorhanden sein müssen. Da für jede Generation ein eigener Datenträger benutzt werden sollte, muss die Anzahl der Generationen auf ein wirtschaftlich sinnvolles Maß beschränkt werden.

Für die Wahl der Parameter des Generationsprinzips ergeben sich folgende Einflüsse (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*):

* Verfügbarkeitsanforderungen und Integritätsbedarf der Daten: Je höher die Verfügbarkeitsanforderungen oder der Integritätsbedarf der Daten ist, umso mehr Generationen müssen vorhanden sein, um im Fall des Integritätsverlustes die Wiederherstellungszeit zu minimieren.
* Wenn der Verlust einer Datei oder eine Integritätsverletzung möglicherweise erst sehr spät bemerkt werden kann, sind zusätzliche Quartals- oder Jahressicherungsdatenbestände empfehlenswert.
* Wiederherstellungsaufwand ohne Datensicherung: Sind die Daten zwar umfangreich, aber auch ohne Datensicherung rekonstruierbar, so kann das als eine weitere Pseudo-Generation ins Kalkül gezogen werden. 
* Datenvolumen: Je höher das Datenvolumen ist, desto mehr Speicherplatz wird gebraucht und desto höher sind auch die Kosten einer Generation. Ein hohes Datenvolumen kann deshalb die Anzahl der Generationen aus wirtschaftlichen Gründen beschränken.
* Änderungsvolumen: Je höher das Änderungsvolumen ist, umso kürzer sollten die Zeitabstände zwischen den Generationen sein, um eine möglichst zeitnahe Version der betreffenden Datei zu haben und den Wiederherstellungsaufwand gering zu halten.
**Vorgehensweise und Speichermedium**

Nachdem die Art der Datensicherung, die Häufigkeit und das Generationenprinzip festgelegt wurden, ist nun die Vorgehensweise und das angemessene Speichermedium auszuwählen. 

Um das Datenvolumen auf dem Speichermedium zu minimieren, können Datenkompressionsalgorithmen angewandt werden. Teilweise kann das Datenvolumen damit sehr stark reduziert werden. Es ist dabei jedoch sicherzustellen, dass die gewählten Parameter und Algorithmen dokumentiert und für die Wiederherstellung der Daten (Dekompression) vorgehalten werden.

Für die **Vorgehensweise** gibt es zwei Parameter, die festgelegt werden müssen: den Automatisierungsgrad und die Zentralisierung (Speicherort).

Beim Automatisierungsgrad ist zwischen manuell und automatisch zu unterscheiden:

* Manuelle Datensicherung bedeutet, dass die Datensicherung händisch angestoßen wird. Vorteilhaft kann sein, dass der Ausführende individuell den Termin der Datensicherung dem Arbeitsablauf anpassen kann. Nachteil ist, dass die Datensicherung von der Motivation und Disziplin des Mitarbeiters abhängt. Durch Krankheit oder sonstige Abwesenheitsgründe können so eventuell Datensicherungen ausfallen.
* Automatische Datensicherungen werden programmgesteuert zu bestimmten Terminen angestoßen. Vorteilhaft ist, dass die Datensicherung zuverlässig durchgeführt wird, sofern der Terminplan vollständig und aktuell ist. Nachteilig kann sein, dass der Terminplan aktuellen Änderungen angepasst werden muss oder wichtige Änderungen nicht unmittelbar gesichert werden.
Bezüglich der Zentralisierung sind zentral und dezentral durchgeführte Datensicherungen zu unterscheiden:

* Zentrale Datensicherungen zeichnen sich dadurch aus, dass der Speicherort und die Datensicherung am zentralen IT-System durchgeführt werden. Diese Verfahrensweise hat den Vorteil, dass nur ein Mitarbeiter intensiv geschult werden muss und die Benutzer von dieser Arbeit entlastet werden. Vorteilhaft ist weiterhin, dass durch das höhere zentrale Datenaufkommen kostengünstigere Speichermedien verwendet werden können. Nachteilig ist, dass eventuell vertrauliche Daten übertragen und von nicht Befugten eingesehen werden könnten.
* Dezentrale Datensicherungen werden von den Benutzern selbst durchgeführt, ohne dass die Daten auf ein zentrales IT-System übertragen werden müssen. Vorteilhaft ist, dass der Benutzer die Kontrolle über die Daten und die Backup-Datenträger behält, insbesondere wenn es sich um vertrauliche Daten handelt. Nachteilig ist, dass die konsequente Datensicherung damit von der Zuverlässigkeit der Benutzer abhängt und dass dezentrale Lösungen den Benutzern Zeitaufwand abfordern.
Nach der Entscheidung, ob die Datensicherung manuell oder automatisch, zentral oder dezentral durchgeführt wird, muss nun der geeignete Datenträger bzw. das geeignete Speichermedium für die Datensicherung gefunden werden. Dazu können folgende Parameter betrachtet werden:

* Datenträger-Anforderungszeit: Wie lang darf es dauern, bis ein Backup-Datenträger für eine Wiederherstellung bereitstehen muss? Roboter-Systeme können das innerhalb von Minuten, ausgelagerte Bänder müssen unter Umständen erst aufwendig transportiert und aufgelegt werden.
* Zugriffszeit, Transferrate: Wie lang eine Datensicherung dauert und wie schnell sich Daten wiederherstellen lassen, hängt von der mittleren Zugriffszeit des Datenträgers und von der Transferrate ab. Festplatten erlauben einen Zugriff auf bestimmte Dateien im Millisekunden-Bereich, ein Magnetband muss erst zur entsprechenden Stelle gespult werden und bei einem Cloud-Speicher hängt die Transferrate direkt von der Internet-Anbindung ab. 
* Speicherkapazität: Das Speichermedium muss über ausreichende Speicherkapazitäten verfügen. Dabei müssen auch zukünftige Datenmengen mit eingeplant werden. 
* Kosten: Die Kosten für die Datensicherung müssen in einem angemessenen Verhältnis zum Sicherungszweck stehen. Hierbei ist auch die Lebensdauer der Datenträger zu berücksichtigen.
Die folgenden Einflussgrößen (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) müssen dabei beachtet werden:

* Verfügbarkeitsanforderungen: Je höher die Verfügbarkeitsanforderungen sind, desto schneller muss auf die Datenträger als Speichermedium der Datensicherung zugegriffen werden können und desto schneller müssen die benötigten Daten vom Datenträger wieder einspielbar sein.
* Es muss sichergestellt sein, dass die Speichermedien auch bei Ausfall eines Lesegerätes zur Wiederherstellung genutzt werden können. Die Kompatibilität und Funktion eines Ersatzgerätes sind zu gewährleisten. 
* Daten- und Änderungsvolumen: Mit zunehmenden Datenvolumen werden oft preisgünstige Speichermedien benutzt. 
* Fristen: Müssen Löschfristen eingehalten werden (z. B. bei personenbezogenen Daten), muss das ausgewählte Speichermedium die Löschung ermöglichen. Speichermedien, die nicht oder nur mit großem Aufwand löschbar sind (z. B. WORM), sollten in diesem Fall vermieden werden.
* Vertraulichkeitsbedarf und Integritätsbedarf der Daten: Ist der Vertraulichkeits- oder Integritätsbedarf der zu sichernden Daten hoch, so überträgt sich dieser Schutzbedarf auch auf die zur Datensicherung eingesetzten Datenträger. Ist eine Verschlüsselung der Datensicherung nicht möglich, kann über die Auswahl von Datenträgern nachgedacht werden, die aufgrund ihrer kompakten Bauart in Datensicherungsschränken oder Tresoren untergebracht werden können.
* Kenntnisse der IT-Benutzer: Die Kenntnisse und datenverarbeitungsspezifischen Fähigkeiten der IT-Benutzer entscheiden darüber, ob eine Verfahrensweise gewählt werden kann, in der der Benutzer selbst manuell für die Datensicherung tätig wird, ob andere ausgebildete Personen die Datensicherung dezentral durchführen oder ob eine automatisierte Datensicherung praktikabler ist. 
**Verantwortlichkeit für die Datensicherung**

Für die Entscheidung, wer für die Datensicherung verantwortlich ist, kommen drei Personengruppen infrage: Zunächst kann es der Benutzer selbst sein (typischerweise bei dezentralen und nicht vernetzten IT-Systemen), der Systemverwalter oder ein für die Datensicherung speziell ausgebildeter Administrator. Wird die Datensicherung nicht vom Benutzer durchgeführt, sind die Verantwortlichen auf Verschwiegenheit bezüglich der Dateninhalte zu verpflichten. Eventuell sollten die Daten auch verschlüsselt werden.

Darüber hinaus sind die Entscheidungsträger zu benennen, die eine Wiederherstellung veranlassen können. Zu klären ist weiterhin, wer berechtigt ist, auf Datensicherungsträger zuzugreifen, insbesondere wenn sie in Datensicherungsarchiven ausgelagert sind. Es muss sichergestellt sein, dass nur Berechtigte Zutritt erhalten. Abschließend ist zu definieren, wer berechtigt ist, eine Wiederherstellung des Gesamtdatenbestandes oder ausgewählter, einzelner Dateien operativ durchzuführen.

Bei der Festlegung der Verantwortlichkeit ist insbesondere der Vertraulichkeits-, Integritätsbedarf der Daten und die Vertrauenswürdigkeit der zuständigen Mitarbeiter zu betrachten. Es muss sichergestellt werden, dass der Verantwortliche erreichbar ist und ein Vertreter benannt und eingearbeitet wird.

Als Einflussfaktor (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) ist zu beachten:

* Kenntnisse der IT-Benutzer: Die Kenntnisse und datenverarbeitungsspezifischen Fähigkeiten der IT-Benutzer entscheiden darüber, ob die Datensicherung eigenverantwortlich je IT-Benutzer durchgeführt werden sollte. Sind die Kenntnisse der IT-Benutzer nicht ausreichend, ist die Verantwortung dem Systemadministrator oder einer speziell ausgebildeten Person zu übertragen.
**Aufbewahrungsort**

Grundsätzlich sollten Datensicherungsmedien und Originaldatenträger in unterschiedlichen Brandabschnitten aufbewahrt werden (siehe CON.3.M12 *Geeignete Aufbewahrung der Backup-Datenträger*). Je weiter entfernt jedoch die Datenträger lagern, desto länger können die Transportwege und damit die Transportzeiten sein, und desto länger dauert die Wiederherstellung. Als Einflussfaktoren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) sind daher zu betrachten:

* Verfügbarkeitsanforderungen: Je höher die Verfügbarkeitsanforderungen sind, umso schneller müssen die Datenträger der Datensicherung verfügbar sein. Werden die Datenträger extern ausgelagert, so ist bei sehr hohen Verfügbarkeitsanforderungen zu erwägen, Kopien der Datensicherung zusätzlich in unmittelbarer Nähe vorzuhalten.
* Vertraulichkeits- und Integritätsbedarf der Daten: Je höher dieser Bedarf ist, umso besser muss verhindert werden, dass an den Datenträgern manipuliert werden kann. Die notwendige Zutrittskontrolle lässt sich durch entsprechende infrastrukturelle und organisatorische Maßnahmen erreichen.
* Datenvolumen: Mit steigendem Datenvolumen ist die Sicherheit des Aufbewahrungsortes zunehmend wichtig.
**Anforderungen an das Datensicherungsarchiv**

Datensicherungen besitzen einen mindestens ebenso hohen Schutzbedarf bezüglich Vertraulichkeit und Integrität wie die gesicherten Daten selbst. Bei der Aufbewahrung in einem zentralen Datensicherungsarchiv sind daher entsprechend wirksame Sicherheitsmaßnahmen notwendig, z. B. eine Zutrittskontrolle.

Zusätzlich muss durch organisatorische und personelle Maßnahmen (Datenträgerverwaltung) sichergestellt werden, dass der schnelle und gezielte Zugriff auf benötigte Datenträger möglich ist. Hierzu ist der Baustein OPS.1.2.2 *Archivierung *zu beachten.

Folgende Einflussfaktoren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*) müssen beachtet werden:

* Verfügbarkeitsanforderungen: Je höher die Verfügbarkeitsanforderungen sind, umso schneller muss der gezielte Zugriff auf benötigte Datenträger möglich sein. Wenn eine manuelle Bestandsführung den Verfügbarkeitsanforderungen nicht genügt, können automatisierte Zugriffsverfahren eingesetzt werden.
* Datenvolumen: Das Datenvolumen bestimmt letztendlich die Art und die Anzahl der aufzubewahrenden Datenträger bzw. die Größe des Online-Speichers. Für entsprechend große Datenvolumen ist eine ausreichende Aufbewahrungskapazität im Datenträgerarchiv vorzusehen.
* Fristen: Sind Löschungsfristen einzuhalten, muss die Organisation des Datensicherungsarchivs sicherstellen, dass die Daten zu den vorgegebenen Zeitpunkten gelöscht werden. Der Vorgang ist zu dokumentieren. 
* Vertraulichkeits- und Integritätsbedarf der Daten: Je höher dieser Bedarf ist, umso sorgfältiger muss verhindert werden, dass an den Datenträgern manipuliert werden kann. Die notwendige Zutrittskontrolle lässt sich durch entsprechende infrastrukturelle und organisatorische Maßnahmen erreichen.
**Transportmodalitäten**

Während einer Datensicherung werden Daten transportiert. Sei es, dass sie über ein Netz oder eine Leitung übertragen werden, sei es, dass Datenträger zum Datenträgerarchiv transportiert werden. Dabei gilt es folgendes zu beachten:

* Verfügbarkeitsanforderungen: Je höher die Verfügbarkeitsanforderungen sind, desto schneller müssen die Daten zur Wiederherstellung verfügbar sein. Das ist bei der Auswahl des Datenübertragungsmediums bzw. bei Auswahl des Datenträger-Transportweges zu berücksichtigen.
* Datenvolumen: Wenn zur Wiederherstellung die Daten über ein Netz übertragen werden, muss die Übertragungskapazität des Netzes beachtet werden. Es muss gewährleistet sein, dass das Datenvolumen innerhalb der erforderlichen Zeit (Verfügbarkeitsanforderung) übertragen werden kann.
* Änderungszeitpunkte der Daten: Werden Datensicherungen über ein Netz durchgeführt (insbesondere zu ausgewählten Terminen), kann aufgrund des zu übertragenden Datenvolumens ein Kapazitätsengpass entstehen. Daher ist zum Zeitpunkt der Datensicherung eine ausreichende Datenübertragungskapazität sicherzustellen.
* Vertraulichkeits- und Integritätsbedarf der Daten: Je höher dieser Bedarf ist, umso sorgfältiger muss verhindert werden, dass die Daten auf dem Transport abgehört, unbefugt kopiert oder manipuliert werden. Bei Datenübertragungen ist schließlich eine Verschlüsselung oder ein kryptografischer Manipulationsschutz zu bedenken. Beim physischen Transport sind sichere Behältnisse und Wege zu benutzen und eventuell auch Nutzen und Aufwand einer Verschlüsselung abzuwägen.
**Aufbewahrungsmodalität**

Im Rahmen des Datensicherungskonzeptes (siehe CON.3.M6 *Entwicklung eines Datensicherungskonzepts*) sollte mit betrachtet werden, ob für bestimmte Daten Aufbewahrungs- oder Löschfristen einzuhalten sind.

* Fristen: Falls Aufbewahrungsfristen einzuhalten sind, sollten die Daten archiviert werden (siehe OPS.1.2.2 Archivierung). Falls Löschfristen einzuhalten sind, müssen der organisatorische Ablauf festgelegt und die technischen Voraussetzungen geschaffen werden, damit die Daten zu den vorgegebenen Zeitpunkten gelöscht werden können.
#### CON.3.M3 Ermittlung von rechtlichen Einflussfaktoren auf die Datensicherung

Für die Datensicherung müssen eine Reihe von rechtlichen Einflussfaktoren beachtet werden, z. B. Datenschutzgesetze. So bestehen für die Aufbewahrung bestimmter Informationen verschiedene rechtliche Vorgaben. Werden diese nicht eingehalten, kann das zivil- oder strafrechtliche Konsequenzen haben. Daher sollten sich die Verantwortlichen informieren, welche rechtlichen Vorgaben zu beachten sind.

Hieraus ergeben sich Anforderungen, die im Datensicherungskonzept berücksichtigt werden müssen. 

#### CON.3.M4 Erstellung eines Minimaldatensicherungskonzeptes

Für eine Institution ist festzulegen, welche Minimalforderungen zur Datensicherung eingehalten werden müssen. Sie dient als Grundlage für ein Datensicherungskonzept und gilt generell für alle IT-Systeme und besonders auch für neue IT-Systeme, für die noch kein Datensicherungskonzept erarbeitet wurde.

Ein Minimaldatensicherungskonzept kann wie folgt aussehen: 

* Software: Es ist sämtliche erworbene oder selbst erstellte Software einmalig mittels einer Vollsicherung zu sichern.
* Systemdaten: Alle Systemdaten sind mindestens einmal monatlich mit einer Generation zu sichern.
* Anwendungsdaten: Alle Anwendungsdaten sind mindestens wöchentlich mittels einer Vollsicherung im Drei-Generationen-Prinzip zu sichern.
* Protokolldaten: Sämtliche Protokolldaten sind mindestens einmal monatlich mittels einer Vollsicherung im Drei-Generationen-Prinzip zu sichern.
* Durchführung: Eingesetzt Hard- und Software, verwendete Parameter, Vorgehensweise der Datensicherung bzw. Wiederherstellung.
#### CON.3.M5 Regelmäßige Datensicherung [IT-Betrieb]

Nach den Vorarbeiten und der Grundkonzeption müssen mit der gewählten Vorgehensweise regelmäßige Datensicherungen durchgeführt werden. 

Es müssen mindestens die Daten regelmäßig gesichert werden, die nicht aus anderen Informationen abgeleitet werden können. Dokumentationen, Programm- und Programmablaufbeschreibungen sind vorzuhalten.

Empfehlenswert ist die Erstellung eines Datensicherungskonzepts (siehe CON.3.M6 *Entwicklung eines Datensicherungskonzepts*).

Abhängig von der Menge und Wichtigkeit der laufend neu gespeicherten Daten und vom möglichen Schaden bei Verlust dieser Daten ist folgendes festzulegen: 

* ZeitintervallBeispiele: täglich, wöchentlich, monatlich
* ZeitpunktBeispiele: nachts, freitags abends
* Anzahl der aufzubewahrenden GenerationenBeispiel: Bei täglicher Komplettsicherung werden die letzten sieben Sicherungen aufbewahrt, außerdem die Freitag-Abend-Sicherungen der letzten zwei Monate.
* Umfang der zu sichernden DatenAm einfachsten ist es, Partitionen bzw. Verzeichnisse festzulegen, die bei der regelmäßigen Datensicherung berücksichtigt werden. Eine geeignete Differenzierung kann die Übersichtlichkeit vergrößern sowie Aufwand und Kosten sparen helfen.Beispiel: selbst erstellte Dateien und individuelle Konfigurationsdateien
* Speichermedien (abhängig von der Datenmenge)Beispiele: DVDs, USB-Speicher oder Festplatten
* Vorherige Löschung der Datenträger vor Wiederverwendung (z. B. bei Festplatten)
* Zuständigkeit für die Durchführung (Administrator, Benutzer)
* Zuständigkeit für die Überwachung der Sicherung, insbesondere bei automatischer Durchführung (Fehlermeldungen, verbleibender Platz auf den Speichermedien)
* Dokumentation der erstellten Sicherungen (Datum, Art der Durchführung der Sicherung sowie gewählte Parameter, Beschriftung der Datenträger)
Wegen des großen Aufwands können Komplettsicherungen in der Regel höchstens einmal täglich durchgeführt werden. Die seit der letzten Sicherung erstellten Daten können nicht wieder eingespielt werden. Daher und zur Senkung der Kosten sollten zwischen den Komplettsicherungen regelmäßig differenzielle oder inkrementelle Sicherungen durchgeführt werden. Hinweise zu den verschiedenen Arten von Datensicherungen finden sich in CON.3.M2 *Festlegung der Verfahrensweise für die Datensicherung*. 

Eine differenzielle oder inkrementelle Sicherung kann häufiger erfolgen, zum Beispiel sofort nach Erstellung wichtiger Dateien oder mehrmals täglich. Die Vereinbarkeit mit dem laufenden Betrieb ist sicherzustellen. 

Für eingesetzte Software ist separat zu entscheiden, ob sie von der regelmäßigen Datensicherung erfasst werden muss. Dies hängt beispielsweise davon ab, wie aufwändig eine Neuinstallation und das Einspielen von Patches und Updates ist. Unter Umständen ist es ausreichend, Sicherungskopien von den Originaldatenträgern anzufertigen (siehe CON.3.M11 *Sicherungskopie der eingesetzten Software*).

Alle Benutzer sollten über die Regelungen zur Datensicherung informiert sein (siehe CON.3.M10 *Verpflichtung der Mitarbeiter zur Datensicherung*).

Falls bei vernetzten Rechnern nur die Server-Platten gesichert werden, ist sicherzustellen, dass die zu sichernden Daten regelmäßig von den Benutzern oder automatisch dorthin überspielt werden. Bei größeren Änderungen an IT-Systemen oder im Informationsverbund muss der Datensicherungsprozess entsprechend angepasst werden.

Vertrauliche Daten sollten vor der Sicherung möglichst verschlüsselt werden, wobei darauf zu achten ist, dass eine Entschlüsselung auch nach einem längeren Zeitraum möglich sein muss (siehe CON.3.M13 *Einsatz kryptografischer Verfahren bei der Datensicherung*). 

Der Ausdruck von Daten auf Papier ist keine angemessene Art der Datensicherung.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Datensicherungskonzept".

#### CON.3.M6 Entwicklung eines Datensicherungskonzepts [Leiter IT, Fachverantwortliche]

Die Verfahrensweise der Datensicherung wird von einer großen Zahl von Einflussfaktoren bestimmt: Das IT-System, das Datenvolumen, die Änderungsfrequenz der Daten und die Verfügbarkeitsanforderungen sind einige dieser Faktoren. Im Datensicherungskonzept gilt es, eine Lösung zu finden, die diese Faktoren berücksichtigt und gleichzeitig unter Kostengesichtspunkten wirtschaftlich vertretbar ist.

Die technischen Möglichkeiten, Datensicherungen durchzuführen, sind vielfältig. Jedoch wird die Auswahl immer von den genannten Faktoren bestimmt. Daher gilt es zunächst, die Einflussgrößen der IT-Systeme und der damit realisierten IT-Anwendungen zu bestimmen und nachvollziehbar zu dokumentieren (siehe CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung)*. Anschließend muss die geeignete Verfahrensweise entwickelt und dokumentiert werden (siehe CON.3.M2 *Festlegung der Verfahrensweise für die Datensicherung*). Zum Abschluss muss durch die Institutionsleitung die Durchführung angeordnet werden. Auch muss das Datensicherungskonzept regelmäßige Funktionstest für Datensicherung vorsehen (siehe CON.3.M9 *Funktionstests und Überprüfung der Wiederherstellbarkeit*)

Die Ergebnisse sollten aktualisierbar und erweiterbar in einem Datensicherungskonzept niedergelegt werden. Ein möglicher Aufbau eines Datensicherungskonzepts ist im nachfolgenden Inhaltsverzeichnis beispielhaft aufgezeigt:

**Inhaltsverzeichnis Datensicherungskonzept**

**1. Definitionen**

* Anwendungsdaten, Systemdaten, Software, Protokolldaten
* Vollsicherung, inkrementelle Datensicherung
**2. Gefährdungslage **(**zur Motivation**)

* Abhängigkeit der Institution vom Datenbestand
* Typische Gefährdungen wie ungeschulte Benutzer, gemeinsam genutzte Datenbestände, Computer-Viren, Hacker, Stromausfall, Festplattenfehler
* Institutionsrelevante Schadensursachen
* Schadensfälle im eigenen Haus
**3. Einflussfaktoren je IT-System**

* Spezifikation der zu sichernden Daten
* Verfügbarkeitsanforderungen der IT-Anwendungen an die Daten
* Rekonstruktionsaufwand der Daten ohne Datensicherung
* Datenvolumen
* Änderungsvolumen
* Änderungszeitpunkte der Daten
* Fristen
* Vertraulichkeitsbedarf der Daten
* Integritätsbedarf der Daten
* Kenntnisse und datenverarbeitungsspezifische Fähigkeiten der IT-Benutzer
**4. Datensicherungsplan je IT-System**

**4.1 Festlegungen je Datenart **und **4.2 Festlegung der Vorgehensweise bei der Daten**wiederherstellung

* Art der Datensicherung
* Häufigkeit und Zeitpunkt der Datensicherung
* Anzahl der Generationen
* Datensicherungsmedium
* Verantwortlichkeit für die Datensicherung
* Aufbewahrungsort der Backup-Datenträger
* Anforderungen an das Datensicherungsarchiv
* Transportmodalitäten
* Wiederherstellungszeiten bei vorhandener Datensicherung
* Randbedingungen für das Datensicherungsarchiv  
 

 
	+ Vertragsgestaltung (bei externen Archiven)
	+ Refresh-Zyklen der Datensicherung
	+ Bestandsverzeichnis
	+ Löschen von Datensicherungen
	+ Vernichtung von unbrauchbaren Datenträgern
	+ Vorhalten von arbeitsfähigen Lesegeräten
	  

 
5. Minimaldatensicherungskonzept

6. Verpflichtung der Mitarbeiter zur Datensicherung

7. Sporadische Restaurierungsübungen

Einzelne Punkte dieses Datensicherungskonzepts werden in den Maßnahmen CON.3.M1 *Erhebung der Einflussfaktoren der Datensicherung*, CON.3.M2 *Festlegung der Verfahrensweise für die Datensicherung*, CON.3.M8 *Funktionstests und Überprüfung der Wiederherstellbarkeit* und CON.3.M10 *Verpflichtung der Mitarbeiter zur Datensicherung* näher ausgeführt.

#### CON.3.M7 Beschaffung eines geeigneten Datensicherungssystems [Leiter IT, IT-Betrieb]

Bei der Beschaffung eines Datensicherungssystems sollte nicht allein auf seine Leistungsfähigkeit geachtet werden, sondern auch auf die Bedienbarkeit und insbesondere auf seine Toleranz gegenüber Benutzerfehlern.

Die Sicherungssoftware sollte folgende Anforderungen erfüllen:

* Die Datensicherungssoftware sollte ein falsches oder ein beschädigtes Medium im Sicherungslaufwerk erkennen können.
* Sie sollte mit der vorhandenen Hardware problemlos zusammenarbeiten.
* Es sollte möglich sein, Sicherungen automatisch zu vorwählbaren Zeiten bzw. in einstellbaren Intervallen durchführen zu lassen, ohne dass hierzu manuelle Eingriffe (außer dem eventuell notwendigen Bereitstellen von Sicherungsdatenträgern) erforderlich wären.
* Es sollte möglich sein, einen oder mehrere ausgewählte Benutzer automatisch über das Sicherungsergebnis und eventuelle Fehlermeldungen per E-Mail oder ähnliche Mechanismen zu informieren. Die Durchführung von Datensicherungen inklusive des Sicherungsergebnisses und möglicher Fehlermeldungen sollten in einer Protokolldatei abgespeichert werden.
* Die Sicherungssoftware sollte die Sicherung des Backup-Mediums durch ein Passwort oder noch besser durch Verschlüsselung unterstützen. Weiterhin sollte sie in der Lage sein, die gesicherten Daten in komprimierter Form abzuspeichern.
* Durch Vorgabe geeigneter Include- und Exclude-Listen bei der Datei- und Verzeichnisauswahl sollte genau spezifiziert werden können, welche Daten zu sichern sind und welche nicht. Es sollte möglich sein, diese Listen zu Sicherungsprofilen zusammenzufassen, abzuspeichern und für spätere Sicherungsläufe wieder zu benutzen.
* Es sollte möglich sein, die zu sichernden Daten abhängig vom Erstellungsdatum bzw. ihrer letzten Modifikation auszuwählen.
* Die Sicherungssoftware sollte logische und physische Vollkopien sowie inkrementelle Kopien (Änderungssicherungen) erzeugen können. 
* Die zu sichernden Daten sollten auch auf Netzlaufwerken oder in Online-Datenspeichern abgespeichert werden können.
* Die Sicherungssoftware sollte in der Lage sein, nach der Sicherung einen automatischen Vergleich der gesicherten Daten mit dem Original durchzuführen und nach der Wiederherstellung von Daten einen entsprechenden Vergleich zwischen den rekonstruierten Daten und dem Inhalt des Sicherungsdatenträgers durchzuführen.
* Bei der Wiederherstellung von Dateien sollte es möglich sein auszuwählen, ob die Dateien am ursprünglichen Ort oder auf einer anderen Platte bzw. in einem anderen Verzeichnis wiederhergestellt werden. Ebenso sollte es möglich sein, das Verhalten der Software für den Fall zu steuern, dass am Zielort schon eine Datei gleichen Namens vorhanden ist. Dabei sollte man wählen können, ob diese Datei immer, nie oder nur in dem Fall, dass sie älter als die zu rekonstruierende Datei ist, überschrieben wird, oder dass in diesem Fall eine explizite Anfrage erfolgt.
Falls mit dem eingesetzten Programm die Datensicherung durch Passwort geschützt werden kann, sollte diese Option genutzt werden. Das Passwort ist dann gesichert zu hinterlegen.

Bei den meisten Betriebssystemen werden Programme für Datensicherungen mitgeliefert. Nicht alle erfüllen allerdings die Ansprüche an Produkte für professionelle und komfortable Datensicherungen. Sind jedoch keine anderen Produkte verfügbar, so sollten die systemzugehörigen Programme verwendet werden.

#### CON.3.M8 Funktionstests und Überprüfung der Wiederherstellbarkeit [IT-Betrieb]

Wenn ein Datenbestand nicht wieder hergestellt werden kann, kann dies viele Ursachen haben. Es können technische Defekte vorliegen, falsche Parameter oder schlicht überalterte Medien. Auch wenn Regeln nicht eingehalten oder die Datenträger nicht richtig verwaltet werden, kann dies zu irreparablen Fehlern führen.

Um dem vorzubeugen und Fehler frühzeitig zu entdecken, muss regelmäßig geprüft werden, ob sich die gesicherten Daten problemlos und in angemessener Zeit zurückspielen lassen. Sollten Defekte oder andere Probleme auftreten, müssen diese so schnell wie möglich repariert werden. 

Ebenso sollten die Verantwortlichen regelmäßig testen, ob die Datensicherung auch wie gewünscht funktioniert. Falls möglich, sollten die Programme so eingestellt werden, dass bei einem Fehler (z. B. volles Datensicherungsmedium) der zuständige Mitarbeiter automatisch informiert wird. 

Weiterhin muss nach einem Patch oder Update für das Datensicherungsprogramm überprüft werden, ob die Software noch korrekt funktioniert und z. B. keine Einstellungsparameter überschrieben wurden. 

#### CON.3.M9 Voraussetzungen für die Online-Datensicherung [Leiter IT, IT-Betrieb]

Die Erstellung einer Datensicherung mithilfe eines Online-Speicher-Dienstes wird in der Regel über eine entsprechende Anwendung auf dem Client eines Benutzers oder auf einem Server der Institution initiiert. Auch möglich ist z. B. ein hybrides Modell durch eine Appliance: Hier werden die Daten lokal auf der Appliance und zusätzlich in einem Online-Speicher-Dienst vorgehalten. In allen Fällen werden die zu sichernden Daten über das Internet von einem Rechner innerhalb der Institution auf einen Server des Online-Speicher-Anbieters übertragen. 

Je nach Anbieter kann der Umgang mit den übertragenen Daten dabei variieren. Ein Großteil der Anbieter unterstützt beispielsweise die Speicherung und Wiederherstellung unterschiedlicher Versionen einer zu übertragenden Datei. Bietet der Online-Speicher-Anbieter hingegen keine Versionierung von Dateien an, wird die ältere Datei ohne zusätzliche Rückfrage überschrieben und ist damit nicht mehr für eine Rücksicherung verfügbar. In diesem Fall erfüllt der Online-Speicher jedoch nicht die Anforderungen, die an eine Datensicherung im Unternehmens- oder Behördenumfeld gestellt werden. Institutionen sollten daher insbesondere auf die vorhandene Versionierung der Daten achten, um dem unerwünschten Löschen älterer Datenversionen vorzubeugen.

Grundsätzlich sollten immer die Fragen im Vordergrund stehen, welchen Schutzbedarf die gesicherten Daten haben, welchen gesetzlichen Verpflichtungen hinsichtlich der geschäftsrelevanten Daten eine Institution unterliegt und wie es sich auswirkt, wenn Daten verloren gehen oder durch Unbefugte verändert werden.

Viele Anbieter von Online-Speicher-Diensten sind sich durchaus bewusst, dass Institutionen großen Wert auf die Verfügbarkeit ihrer Daten legen und halten die Daten ihrer Kunden redundant vor. Institutionen sollten darauf achten, dass der Anbieter die Daten an unterschiedlichen Standorten bzw. in räumlich voneinander getrennten Rechenzentren speichert. Kommt es zu Problemen in einem Rechenzentrum, stehen die Daten in diesem Fall dennoch weiterhin in einem anderen Rechenzentrum zur Verfügung.

Unternehmen und Behörden sollten nicht nur Wert auf die sichere Speicherung ihrer Daten legen, sondern darüber hinaus auch die Umsetzung der Zugriffsmöglichkeiten auf die angelegten Benutzerkonten hinterfragen. Im Unternehmens- und Behördenumfeld sind gezielte Angriffe vorstellbar, deren Absicht darin liegt, eine Sperrung des Benutzerkontos herbeizuführen und auf diesem Weg den Zugriff auf das Backup der Daten zu verhindern. Eine solche Denial-of-Service-Attacke bedient sich dabei in der Regel unterschiedlicher Schwachstellen wie beispielsweise einer Kombination aus der automatischen Sperrung eines Benutzerkontos bei fehlgeschlagenen Anmeldeversuchen und einer nicht validierten E-Mail-Adresse. Als Schutzmaßnahme kann das Time-Out-Prinzip einem solchen gezielten Denial-of-Service-Angriff entgegenwirken. Dabei wird das Benutzerkonto nicht vollständig gesperrt, sondern lediglich ein erneuter Anmeldeversuch für einen vorgegebenen Zeitraum unterbunden.

Nicht nur Vollständigkeit und Verfügbarkeit ihrer gesicherten Daten interessieren Institutionen, vielmehr legen sie, unter anderem zur Vermeidung rechtlicher Konsequenzen oder eines Imageverlustes, auch großen Wert auf deren Vertraulichkeit und Integrität. Institutionen sollten daher Verschlüsselungsverfahren einsetzen, um das Sicherheitsniveau bei der Übermittlung und der Datenspeicherung bei externen Dienstleistern zu erhöhen.

Viele Anbieter von Online-Speicher-Lösungen werben mit der erhöhten Sicherheit durch Verschlüsselung. Hier muss jedoch genauer analysiert werden, wie die Verschlüsselung konkret umgesetzt ist. In der Regel erfolgt nämlich lediglich die eigentliche Übertragung der Daten verschlüsselt, etwa über den Aufbau einer https-Verbindung (Hyper Text Transfer Protocol Secure). Vor und nach dem Transport liegen die Daten jedoch unverschlüsselt im Klartext vor. Einige Anbieter stellen ihren Kunden, unabhängig vom Transportweg der Daten, zusätzliche Verschlüsselungsmethoden zur Verfügung. Allerdings kann die Institution dabei oft nicht ausschließen, dass sich ein Innentäter, also ein Mitarbeiter des Online-Speicher-Anbieters, die entsprechenden Schlüssel verschafft und damit auch auf die verschlüsselten Informationen zugreifen, diese verfälschen oder veröffentlichen kann. Erlangt ein Angreifer Zugriff auf die Daten, indem er die Authentisierung kompromittiert, dann ist die Verschlüsselung beim Anbieter ebenfalls wirkungslos.

Sehen Institutionen ihre Daten also als besonders schützenswert an, sollten sie diese bereits auf ihren eigenen Systemen und damit vor dem eigentlichen Datentransfer verschlüsseln.

Das Bedürfnis nach einer sicheren Methode zur Nutzung von Online-Speicher-Lösungen, gerade im Behörden- oder Unternehmensumfeld, wird vom Markt jedoch zunehmend aufgegriffen. So hat sich mittlerweile eine Reihe von Verschlüsselungslösungen etabliert, die größtenteils speziell auf die Zusammenarbeit mit Online-Speicher-Diensten abgestimmt sind. Die Programme überprüfen bereits bei der Installation, ob ein passender Ordner eines Online-Speichers existiert, und erzeugen anschließend einen entsprechenden Unterordner, in dem die verschlüsselten Dateien abgelegt werden. Institutionen, die zusätzliche Verschlüsselungssoftware einsetzen, sollten darauf achten, dass für die Anwendung ein ausreichend starkes Passwort oder anderer Zugriffsschutz gewählt wird. Zudem sollte eine Kopie der eingesetzten Softwarelösung und der zugehörigen kryptografischen Schlüssel an einem sicheren Ort hinterlegt werden, um im Falle eines vollständigen Datenverlustes innerhalb der Institution noch auf die verschlüsselten Datensicherungen des Online-Speichers zugreifen zu können. Zu diesem Zweck kann die Verschlüsselungssoftware unverschlüsselt beim Online-Speicher-Dienst gesichert werden, der Schlüssel muss selbstverständlich anders gesichert werden. Auf diesem Weg ist die Institution unabhängig davon, ob die Verschlüsselungssoftware auch nach einem längeren Zeitraum noch in einer kompatiblen Version zur Verfügung steht.

Institutionen sollten sich zudem davon überzeugen, dass die Wiederherstellung der gespeicherten Daten vom Online-Speicher fehlerfrei funktioniert, und sollten dies darüber hinaus regelmäßig testen (siehe CON.3.A8 *Funktionstests und Überprüfung der Wiederherstellbarkeit*).

#### CON.3.M10 Verpflichtung der Mitarbeiter zur Datensicherung

Alle Benutzer sollten über die Regelungen zur Datensicherung informiert sein, um gegebenenfalls auf Unzulänglichkeiten (zum Beispiel zu geringes Zeitintervall für ihren Bedarf) hinweisen oder individuelle Ergänzungen vornehmen zu können (zum Beispiel zwischenzeitliche Spiegelung wichtiger Daten auf der eigenen Platte). 

Auch die Information der Benutzer darüber, wie lange die Daten wieder einspielbar sind, ist wichtig. Werden zum Beispiel bei wöchentlicher Komplettsicherung nur zwei Generationen aufbewahrt, bleiben abhängig vom Zeitpunkt des Verlustes nur zwei bis drei Wochen Zeit, um die Daten wieder einzuspielen.

Mitarbeiter, die Aufgaben bei der Erstellung von Datensicherungen wahrnehmen sollen, sollten darüber informiert und darauf verpflichtet werden, dabei das Datensicherungskonzept bzw. das Minimaldatensicherungskonzept sorgfältig einzuhalten. Das ist vor allem dort wichtig, wo zentral durchgeführte Datensicherungen nicht greifen, also z. B. bei nicht-vernetzten oder mobilen Endgeräten. Die Mitarbeiter sollten regelmäßig an die Datensicherung erinnert und dazu motiviert werden. 

#### CON.3.M11 Sicherungskopie der eingesetzten Software [IT-Betrieb]

Bei Problemen mit IT-Systemen ist es oft nötig, die eingesetzten Betriebssysteme und Anwendungen zeitnah neu installieren zu können. Hierfür müssen alle Dateien, die zur Installation benötigt werden, vorliegen. Daher ist es erforderlich, Kopien anzufertigen und an geeigneter Stelle zu archivieren.

Wird die Software auf Datenträgern (z. B. DVDs oder USB-Sticks) ausgeliefert, sollte von den Originaldatenträgern bzw. von der Originalsoftware bei Eigenentwicklungen eine Sicherungskopie erstellt werden, von der die Software wieder eingespielt werden kann. Die Originaldatenträger und die Sicherungskopien sind getrennt voneinander aufzubewahren.

Insbesondere Anwendungen werden oft nicht auf Datenträgern ausgeliefert, sondern nur als separate Installationsdateien, als Bestandteil einer Paket- oder Softwareverwaltung oder als Quelltextpakete. Auch diese Installationsquellen sollten an einem geeigneten Ort hinterlegt werden.

Um kostenpflichtige Betriebssysteme oder Anwendungen zu installieren, müssen oft Lizenznummern während der Installation eingegeben werden. Deshalb ist es nötig, dass neben den Installationsquellen auch die Lizenznummern geeignet hinterlegt werden. Ein unerlaubter Zugriff auf die Installationsmedien und die Lizenznummern muss ausgeschlossen sein.

Wurde die Software aus Quelltexten übersetzt, so sollte die Dokumentation sämtliche beim Übersetzen verwendeten Optionen (insbesondere die Optionen, mit denen ein etwaiges Skript *configure* aufgerufen wurde) enthalten. Wurde die Software aus einem Binärpaket installiert, so sollten alle Schritte dokumentiert werden, mit denen die Installation später nachvollzogen werden kann.

Jede Änderung an einer Konfigurationsdatei sollte dokumentiert werden. Es empfiehlt sich, eine Versionsverwaltung einzusetzen. Zusätzlich müssen alle Konfigurationsdateien regelmäßig gesichert werden.

#### CON.3.M12 Geeignete Aufbewahrung der Backup-Datenträger [IT-Betrieb]

Backup-Datenträger unterliegen besonderen Anforderungen hinsichtlich ihrer Aufbewahrung:

* Der Zugriff auf diese Datenträger darf nur befugten Personen möglich sein.
* Ein ausreichend schneller Zugriff muss im Bedarfsfall gewährleistet sein.
* Der Aufbewahrungsort muss auch die klimatischen Bedingungen für eine längerfristige Aufbewahrung von Datenträgern gewährleisten.
* Für den Notfall müssen die Backup-Datenträger räumlich getrennt vom gesicherten IT-System aufbewahrt werden, wenn möglich in einem anderen Brandabschnitt.
### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.3.M13 Einsatz kryptografischer Verfahren bei der Datensicherung [IT-Betrieb]

Der Vertraulichkeitsbedarf einer Datei überträgt sich bei einer Datensicherung auf die Sicherungskopie. Daher sollte bei erhöhtem Schutzbedarf die Sicherung verschlüsselt werden.

Für die Datensicherungen müssen geeignete Verschlüsselungsverfahren ausgewählt werden. Das entscheidende Merkmal eines Verschlüsselungsverfahrens ist die Güte des Algorithmus sowie der Schlüsselauswahl. Da die Sicherheitseignung der Verschlüsselungsverfahren durch die technische Entwicklung von Hard- und Software sowie Fortschritte in der Kryptografie beschränkt wird, müssen sie regelmäßig nach dem Stand der Technik aktualisiert werden.

Auch muss sichergestellt sein, dass die Schlüssel geeignet verwaltet werden.

Weitere Hinweise zu kryptografischen Verfahren finden sich im Baustein CON.1 *Kryptokonzept*.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Datensicherungskonzept" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BKBU] Leitfaden Backup / Recovery / Disaster Recovery

  

 Bitkom, 2016  
 <https://www.bitkom.org/noindex/Publikationen/2017/Leitfaden/170125-LF-Backup-Recovery.pdf>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
