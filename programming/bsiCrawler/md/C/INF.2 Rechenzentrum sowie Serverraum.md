1 Beschreibung
--------------

### 1.1 Einleitung

Heute werden fast alle strategischen und operativen Funktionen und Aufgaben durch Informationstechnik (IT) maßgeblich unterstützt oder sind ohne IT nicht auszuführen. Dadurch steigen die Anforderungen an die Leistungsfähigkeit und Verfügbarkeit der IT-Systeme und deren Anbindung an die Netzumgebung stetig. Um diesem Leistungsbedarf gerecht zu werden, um entsprechende Reserven vorzuhalten und um die IT auch wirtschaftlich betreiben zu können, konzentrieren Behörden und Unternehmen jeglicher Größe ihre IT-Landschaft in Rechenzentren. 

Ein Rechenzentrum (RZ) ist wie folgt definiert: 

Weicht ein Rechenzentrum von dieser Definition ab, wird der betrachtete IT-Betriebsbereich als Serverraum bezeichnet. Diese Definition orientiert sich ausschließlich an der Bedeutung der IT-Struktur für die Aufgabenerfüllung der nutzenden Institution und steht damit im methodischen Einklang mit der DIN EN 50600.

Soll ein Serverraum abgesichert werden, können die Anforderungen dieses Bausteins entsprechend reduziert werden. Dies muss jedoch stichhaltig und nachvollziehbar begründet werden (entsprechend 6.) und es müssen mindestens die Basis-Anforderungen umgesetzt werden. 

### 1.2 Zielsetzung

Der Baustein richtet sich einerseits an Institutionen, die ein Rechenzentrum betreiben und im Rahmen einer Revision prüfen möchten, ob sie geeignete Sicherheitsmaßnahmen umgesetzt haben. Andererseits kann der Baustein auch dazu benutzt werden, die Sicherheitsmaßnahmen abzuschätzen, die umgesetzt werden müssen, wenn die IT in einem Rechenzentrum zentralisiert werden soll. Das oberste Ziel der in diesem Baustein beschriebenen Anforderungen ist es, den sicheren Betrieb des Rechenzentrums aufrechtzuerhalten. 

### 1.3 Abgrenzung

Gegenstand dieses Bausteins sind nur Rechenzentren mittlerer Art und Güte. Die hier beschriebenen Sicherheitsanforderungen reichen nicht aus, um Hochsicherheitsrechenzentren, wie sie beispielsweise im Bankenbereich eingesetzt werden, zu schützen. Ein Hochsicherheitsrechenzentrum unterscheidet sich vor allem in den Punkten Hochverfügbarkeit, Desastertoleranz, Redundanz der Komponenten, Widerstandsfähigkeit gegen Elementarschäden, Energie-Effizienz und Datensicherheit von den hier betrachteten mittleren Rechenzentren. 

Weiterhin eignet sich der vorliegende Baustein nicht für kleine Informationsverbünde mit z. B. nur einem oder sehr wenigen Servern oder IT-Systemen. Ein Beispiel hierfür ist kleines, mittelständisches Unternehmen (KMU) mit wenigen IT-Arbeitsplätzen und einem Server, der in einem separaten Raum steht. In solchen Fällen genügt es oft, den Baustein INF.6 *Schutzschrank/Technikraum* umzusetzen. 

Um den Baustein überschaubar zu halten, wurde bewusst auf technische Details und planerische Größen verzichtet. Nähere Informationen liefern einschlägige Normen, z. B. DIN EN 50600.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für Rechenzentren von besonderer Bedeutung: 

### 2 1 Fehlerhafte Planung

Wenn ein Rechenzentrum konzipiert und dabei nicht berücksichtigt wird, es gegen elementare Gefährdungen abzusichern, besteht ein sehr hohes Ausfallrisiko. So können z. B. Standortrisiken wie Luftverkehr, Erdbeben, Hochwasser oder politische Gesichtspunkte die Betriebssicherheit und Verfügbarkeit gefährden. Ebenso massiv kann es sich auf den Betrieb eines neuen Rechenzentrums auswirken, wenn durch eine fehlerhafte Konzeptionierung nicht genügend Bandbreite verfügbar ist oder die Energieversorgung am gewählten Standort nicht ausreicht. 

### 2 2 Unberechtigter Zutritt

Fehlen Zutrittskontrollen oder sind diese unzureichend, erhöht sich die Gefahr, dass unberechtigte Personen das Rechenzentrum betreten und dort fahrlässig, z. B. aufgrund mangelnder Fachkenntnisse, oder vorsätzlich Schaden anrichten. Angreifer können so z. B. schützenswerte Daten entwenden, Geräte stehlen oder Server manipulieren. Unzureichende Zutrittskontrollen wirken sich somit besonders auf die Verfügbarkeit, Vertraulichkeit und die Integrität von Daten beziehungsweise IT-Komponenten aus.

### 2 3 Unzureichende Überwachung

Wird die im Rechenzentrum betriebene IT und Infrastruktur unzureichend überwacht und betreut, können Komponenten unbemerkt ausfallen. Dadurch wird eventuell die Verfügbarkeit und fehlerfreie Funktion des Rechenzentrums stark beeinträchtigt. Ausfälle treten zudem oftmals schleichend ein. Ohne eine aktive Überwachung könnten diese zu spät bemerkt werden. Es ist dann oft nicht mehr möglich, rechtzeitig zu reagieren.

### 2 4 Unzureichende Klimatisierung im Rechenzentrum

IT-Komponenten benötigen eine bestimmte Betriebstemperatur, um korrekt zu funktionieren. Auch setzen sie ihre Energie in zusätzliche Wärme um. Wenn ein Rechenzentrum nicht oder nur unzureichend klimatisiert wird, können die klimatischen Bedingungen im Raum nicht stabil gehalten werden. Ist es dort zu kalt oder zu heiß, unter- oder überschreiten die Geräte eventuell ihre zulässige Betriebstemperatur. Die Folgen sind z. B. Fehlfunktionen und Ausfälle von technischen Komponenten oder auch beschädigte Speichermedien. 

### 2 5 Feuer

Verfügt ein Rechenzentrum über keinen oder nur über einen unzureichenden Brandschutz, besteht die Gefahr, dass ein Feuer entstehen und sich schnell ausbreiten kann. Durch Feuer und Rauch können große Schäden entstehen. Auch lassen sich Brandüberschläge eventuell nicht frühzeitig verhindern. 

### 2 6 Wasser

Durch Undichtigkeiten in der Infrastruktur des Rechenzentrums, Hochwasser, Rohrbruch, defekte Sprinkleranlagen, Kanalisationsschäden oder auch Klimaanlagendefekte kann Wasser in das Rechenzentrum eintreten. Das kann dazu führen, dass Geräte beschädigt werden oder nicht mehr funktionieren. Auch könnte so ein Kurzschluss ausgelöst werden, der zum Totalausfall führt oder sogar einen Brand verursacht.

### 2 7 Fehlender oder unzureichender Einbruchsschutz

Ein fehlender oder mangelhafter Einbruchsschutz macht es unbefugten Personen leicht, in ein Rechenzentrum einzudringen. Täter können so z. B. IT-Komponenten stehlen oder manipulieren und an vertrauliche Informationen gelangen. Auch könnten sie die Geräte zerstören oder das Rechenzentrum insgesamt beschädigen. 

### 2 8 Ausfall der Stromversorgung

Wenn der Strom ausfällt und es keine redundante Stromversorgung gibt, kann das zu erheblichen Störungen im Betriebsablauf eines Rechenzentrums und damit der Institution führen. So sind bei einem Stromausfall alle vom Rechenzentrum bereitgestellten IT-Services plötzlich nicht erreichbar. Auch können Daten verloren gehen. Weiterhin ist es möglich, dass durch einen plötzlichen Stromausfall IT-Systeme, aktive Netzkomponenten, TK-Systeme oder Überwachungstechnik beschädigt werden.

### 2 9 Verschmutzung

Staub und andere Verschmutzungen in einem Rechenzentrum können dazu führen, dass die Technik nicht mehr funktioniert. Durch Verschmutzungen fällt sie häufiger aus und verschleißt früher. 

### 2 10 Unzureichende Trassendimensionierung

Wenn Kabeltrassen nicht getrennt geführt und Mindestabstände nicht eingehalten werden, können Störungen der IT des Rechenzentrums auftreten. Auch Erweiterungen des Netzes können problematisch sein, sodass der Schutz vor Feuer- und Rauchentwicklungen eventuell nicht mehr gewährleistet ist. Auch ist zu beachten, dass Löcher für Kabeldurchführungen in Brandwänden nur mit 60 % des Querschnitts mit Kabeln belegt werden dürfen. 40 % müssen mit Brandschutzmörtel oder einem anderen für Brandschotte zugelassenen Material gefüllt werden. Wird diese Vorschrift nicht beachtet, kann ein Brand aus dem benachbarten Raum zu leicht auf das RZ übergreifen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Rechenzentren aufgeführt. Grundsätzlich ist der Leiter IT dafür zuständig, die Anforderungen zu erfüllen. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### INF.2.A1 Festlegung von Anforderungen [Planer, IT-Betrieb, Haustechnik, Informationssicherheitsbeauftragter (ISB)]

Für ein Rechenzentrum MÜSSEN angemessene technische und organisatorische Vorgaben definiert und umgesetzt werden. 

Wenn ein Rechenzentrum geplant wird oder geeignete Räumlichkeiten ausgewählt werden, MÜSSEN potenzielle Gefährdungen durch Umgebungseinflüsse sowie das Sicherheitsniveau der IT-Komponenten (insbesondere Verfügbarkeit) mitbetrachtet werden. Weiterhin MÜSSEN auch Schutzmaßnahmen vor potenziellen internen und externen Angriffen in die Gesamtbetrachtung einﬂießen.

Ein Rechenzentrum MUSS insgesamt als geschlossener Sicherheitsbereich konzipiert werden. Es MUSS zudem unterschiedliche Sicherheitszonen aufweisen. Hierfür MÜSSEN Verwaltungs-, Logistik-, Technik- und IT-Flächen klar voneinander getrennt werden. Im Falle eines Serverraums SOLLTE geprüft werden, ob unterschiedliche Sicherheitszonen umsetzbar sind. 

Auch MUSS darauf geachtet werden, dass Versorgungsleitungen (z. B. für Wasser oder Gas) möglichst nicht in unmittelbarer Nähe von schutzbedürftigen Technikkomponenten verlaufen. Vorhandene Versorgungsleitungen MÜSSEN zumindest an den kritischen Stellen regelmäßig überprüft werden, ob sie noch dicht sind.

#### INF.2.A2 Bildung von Brandabschnitten [Planer]

Es MÜSSEN geeignete Brandabschnitte für die Räumlichkeiten eines Rechenzentrums festgelegt werden. Schutzziel für die Brandwand bzw. den Brandabschnitt MUSS nicht nur der Personen- und Gebäudeschutz, sondern auch der Schutz des Inventars und dessen Verfügbarkeit sein. Somit MUSS nicht nur verhindert werden, dass sich ein Brand durch Flammen und heiße Rauchgase ausbreitet, sondern es MÜSSEN auch die Wärmestrahlung und die Ausbreitung von kaltem Rauch blockiert werden. Im Falle eines Serverraums SOLLTE geprüft werden, ob geeignete Brandabschnitte für die Räumlichkeiten umsetzbar sind. 

#### INF.2.A3 Einsatz einer unterbrechungsfreien Stromversorgung [Haustechnik]

Für alle betriebsrelevanten Komponenten des Rechenzentrums MUSS eine unterbrechungsfreie Stromversorgung (USV) installiert werden. Da der Leistungsbedarf von Klimatisierungsanlagen oft zu hoch für eine USV ist, MUSS aber mindestens die Steuerung der Anlagen an die unterbrechungsfreie Stromversorgung angeschlossen werden. Im Falle eines Serverraums SOLLTE je nach Verfügbarkeitsanforderungen der IT-Systeme geprüft werden, ob der Betrieb einer USV notwendig ist.

Die USV MUSS ausreichend dimensioniert sein, sodass alle Komponenten bei einem Ausfall der Versorgung so lange mit Strom versorgt werden, dass kein Datenverlust entsteht.

Bei relevanten Änderungen MUSS überprüft werden, ob die vorhandenen USV-Systeme noch ausreichend dimensioniert sind. Die Batterie der USV MUSS im erforderlichen Temperaturbereich gehalten werden und vorzugsweise in einem getrennten Bereich platziert sein. 

Die USV MUSS regelmäßig gewartet und auf Funktionsfähigkeit getestet werden. Dafür MÜSSEN die vom Hersteller vorgesehenen Wartungsintervalle eingehalten werden *(*siehe* INF.2.A10 Inspektion und Wartung der Infrastruktur)*. Um sicherzustellen, dass die USV die erforderliche Stützzeit bereitstellt, MUSS regelmäßig sowie zusätzlich, wenn sich bei den Verbrauchern etwas ändert, die tatsächliche Stützzeit ermittelt werden.

Wenn IT-Geräte über eine USV versorgt werden, DÜRFEN diese NICHT über geschirmte Leitungen mit weiteren IT-Geräten verbunden werden. 

#### INF.2.A4 Notabschaltung der Stromversorgung [Haustechnik]

Für den Notfall MUSS es geeignete Möglichkeiten geben, das Rechenzentrum spannungsfrei zu schalten. Dafür SOLLTE beispielsweise ein Not-Aus-Schalter installiert werden. Ein solcher Schalter MUSS nicht nur die externe Energieversorgung abtrennen, sondern auch die komplette USV-Anlage abschalten. Alle Not-Aus-Schalter MÜSSEN so geschützt sein, dass sie nicht unbeabsichtigt betätigt werden können.

#### INF.2.A5 Einhaltung der Lufttemperatur und -feuchtigkeit [Haustechnik]

Um IT-Systeme entsprechend den Hersteller-Empfehlungen zuverlässig betreiben zu können, MUSS sichergestellt werden, dass die Lufttemperatur und Luftfeuchtigkeit im IT-Betriebsbereich innerhalb der vorgeschriebenen Grenzen liegen. 

Die tatsächliche Wärmelast in den gekühlten Bereichen MUSS in regelmäßigen Abständen und nach größeren Umbauten durch Berechnung oder Messung überprüft werden. 

Auch MUSS eine eventuell vorhandene Klimatisierungseinrichtung regelmäßig gewartet werden. Wenn die beiden Parameter "Temperatur" und "Feuchtigkeit" vom Normwert abweichen, MÜSSEN sie über eine repräsentative Dauer hinweg in einem der Situation angepassten Zeitintervall aufgezeichnet werden.

#### INF.2.A6 Zutrittskontrolle [IT-Betrieb, Informationssicherheitsbeauftragter (ISB), Haustechnik]

Für den Schutz gegen unbefugten Zutritt zu einem Rechenzentrum MUSS es eine Zutrittskontrolle geben. 

Durch eine auf die jeweiligen Erfordernisse abgestimmte Zutrittsregelung MUSS für eigene Mitarbeiter und für nur zeitweilig Beschäftigte sichergestellt werden, dass sie keinen Zutritt zu IT-Systemen außerhalb ihres Tätigkeitsbereiches erhalten.

Außerdem MUSS sichergestellt werden, dass Besucher und Fremdpersonal während aller Arbeiten im Rechenzentrum von der Zutrittskontrolle individuell erfasst sowie beaufsichtigt werden.

Zudem MÜSSEN alle Zutrittsmöglichkeiten zu einem Rechenzentrum überwacht werden. Die Anforderungen der Institution an ein Zutrittskontrollsystem MÜSSEN in einem Konzept ausreichend detailliert dokumentiert werden. Im Falle eines Serverraums SOLLTE geprüft werden, ob eine Überwachung aller Zutrittsmöglichkeiten sinnvoll ist. 

Weiterhin MUSS geregelt werden, welche internen und externen Personen für welchen Zeitraum Zutritt erhalten. Dabei MUSS sichergestellt sein, dass keine unnötigen oder zu weitreichenden Zutrittsrechte vergeben werden. Es MUSS regelmäßig kontrolliert werden, ob die Regelungen zum Einsatz einer Zutrittskontrolle eingehalten werden.

#### INF.2.A7 Verschließen und Sichern [Mitarbeiter, Haustechnik]

Alle Türen des Rechenzentrums MÜSSEN stets verschlossen gehalten werden. Fenster sind möglichst schon bei der Planung zu vermeiden. Falls sie doch vorhanden sind, MÜSSEN sie ebenso wie die Türen stets verschlossen gehalten werden. Türen und Fenster MÜSSEN einen dem Sicherheitsniveau angemessenen Schutz gegen Angriffsversuche und Umgebungseinflüsse (z. B. Feuer und Rauch) bieten. Hierbei ist zu beachten, dass die bauliche Ausführung aller raumbildenden Elemente in Bezug auf die Sicherheit, vor allem hinsichtlich Sicherheitszonen, gleichwertig sein MUSS.

#### INF.2.A8 Einsatz einer Brandmeldeanlage [Planer]

In einem Rechenzentrum MUSS eine Brandmeldeanlage installiert werden. Diese MUSS alle Flächen überwachen. Alle Meldungen der Brandmeldeanlage MÜSSEN geeignet weitergeleitet werden (siehe dazu auch INF.2.A13 *Planung und Installation von Gefahrenmeldeanlagen*). Die Brandmeldeanlage MUSS regelmäßig gewartet. Es MUSS sichergestellt werden, dass in Räumen, die im Brandabschnitt des Rechenzentrums liegen, keine besonderen Brandlasten vorhanden sind.

#### INF.2.A9 Einsatz einer Lösch- oder Brandvermeidungsanlage [Planer]

In einem Rechenzentrum MUSS eine Lösch- oder Brandvermeidungsanlage nach aktuellem Stand der Technik installiert sein. 

In Serverräumen SOLLTEN hierfür Handfeuerlöscher in ausreichender Zahl und Größe benutzt werden. Die Feuerlöscher MÜSSEN so angebracht werden, dass sie im Brandfall leicht zu erreichen sind. Jeder Löscher MUSS regelmäßig inspiziert und gewartet werden, um die Funktionsfähigkeit im Ernstfall zu gewährleisten. Alle Mitarbeiter MÜSSEN in die Benutzung der Handfeuerlöscher eingewiesen werden.

#### INF.2.A10 Inspektion und Wartung der Infrastruktur [IT-Betrieb, Haustechnik, Wartungspersonal]

Für alle Komponenten der technischen Infrastruktur MÜSSEN mindestens die empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden. Um nachvollziehen zu können, wann welche Arbeiten durchgeführt wurden, MÜSSEN Inspektionen und Wartungsarbeiten protokolliert werden.

Kabel- und Rohrdurchführungen durch Brandwände MÜSSEN regelmäßig daraufhin geprüft werden, ob die Schotten normgerecht und unversehrt sind. Die Ergebnisse MÜSSEN dokumentiert werden.

#### INF.2.A11 Automatisierte Überwachung der Infrastruktur [IT-Betrieb, Haustechnik]

Alle Störungsmeldungen der Infrastruktur, z. B. Leckageüberwachung, Klima-, Strom- und USV-Anlagen, MÜSSEN automatisiert überwacht und schnellstmöglich geeignet weitergeleitet werden, z. B. über ein Monitoringsystem. 

Im Falle eines Serverraums SOLLTEN IT- und Supportgeräte, die nicht oder nur selten von einer Person bedient werden müssen, mit einer Fernanzeige für Störungen ausgestattet werden. Die verantwortlichen Mitarbeiter MÜSSEN zeitnah alarmiert werden. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Rechenzentrum sowie Serverraum. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### INF.2.A12 Entwurf und Umsetzung eines Perimeterschutzes für das Rechenzentrum [Planer, Haustechnik]

Die Sicherheitsmaßnahmen zum Perimeterschutz SOLLTEN gleichwertig mit denen des Sicherheitskonzeptes für das Gebäude und seines Umfelds sein. Je nach dem festgelegten Schutzbedarf für das Rechenzentrum und abhängig vom Gelände SOLLTE der Perimeterschutz aus folgenden Komponenten bestehen:

* äußere Umschließung oder Umfriedung,
* Sicherungsmaßnahmen gegen unbeabsichtigtes Überschreiten einer Grundstücksgrenze,
* Sicherungsmaßnahmen gegen beabsichtigtes gewaltloses Überwinden der Grundstücksgrenze,
* Sicherungsmaßnahmen gegen beabsichtigtes gewaltsames Überwinden der Grundstücksgrenze,
* Freiland-Sicherungsmaßnahmen sowie
* äußere Personen- und Fahrzeugidentifikation.
#### INF.2.A13 Planung und Installation von Gefahrenmeldeanlagen [Planer]

Es SOLLTE ein konsistentes Schutzkonzept für das betrachtete Gebäude erarbeitet werden. Erst danach SOLLTE geplant werden, welche Gefahrenmeldeanlagen für welche Gebäudebereiche des Rechenzentrums benötigt und installiert werden und wie mit Alarmmeldungen umzugehen ist. Das Konzept SOLLTE immer angepasst werden, wenn sich die Nutzung der Gebäudebereiche verändert. 

Es SOLLTE eine für das jeweilige Einsatzgebiet angemessene Gefahrenmeldeanlage (GMA) installiert werden. Die Meldungen der GMA SOLLTEN unter Beachtung der dafür geltenden Technischen Anschlussbedingungen (TAB) auf eine Alarmempfangsstelle aufgeschaltet werden. Die Alarmempfangsstelle SOLLTE jederzeit erreichbar und technisch sowie personell in der Lage sein, in geeigneter Weise auf die gemeldete Gefährdung zu reagieren. Der Übertragungsweg zwischen eingesetzter GMA und hilfeleistender Stelle SOLLTE redundant ausgelegt werden. Alle Übertragungswege SOLLTEN regelmäßig getestet werden. 

#### INF.2.A14 Einsatz einer Netzersatzanlage [Planer, Haustechnik]

Die Energieversorgung aus dem Netz eines Energieversorgungs-Unternehmens () SOLLTE um eine Netzersatzanlage (NEA) ergänzt werden. Der Betriebsmittelvorrat einer NEA SOLLTE regelmäßig kontrolliert werden. Um die Schutzwirkung einer NEA aufrechtzuerhalten, SOLLTE sie regelmäßig gewartet werden (siehe INF.2.A10 *Inspektion und Wartung der Infrastruktur*). Bei diesen Wartungen SOLLTEN auch Belastungs- und Funktionstests sowie Testläufe unter Last durchgeführt werden. 

#### INF.2.A15 Überspannungsschutzeinrichtung [Planer, Haustechnik]

Es SOLLTE auf Basis der aktuell gültigen Norm ein Blitz- und Überspannungsschutzkonzept nach dem Prinzip der energetischen Koordination (Anhang C der DIN EN 62305-4) erstellt und umgesetzt werden. Die energetische Koordination der Überspannungsschutzeinrichtungen SOLLTE in einem Konzept dokumentiert und abgenommen werden. 

Blitz- und Überspannungsschutzeinrichtungen SOLLTEN periodisch und nach bekannten Ereignissen geprüft und falls erforderlich ersetzt werden. Unabhängig von Umfang und Ausbau des Überspannungsschutzes SOLLTE beachtet werden, dass ein umfassender und durchgängiger Potenzialausgleich aller in den Überspannungsschutz einbezogenen elektrischen Betriebsmittel erforderlich ist. Bei Nachinstallationen SOLLTE darauf geachtet werden, dass der Potenzialausgleich mitgeführt wird.

#### INF.2.A16 Klimatisierung im Rechenzentrum [Haustechnik]

Es SOLLTE sichergestellt werden, das im Rechenzentrum geeignete klimatische Bedingungen für Lufttemperatur und Luftfeuchtigkeit (siehe INF.2.A5 *Einhaltung der Lufttemperatur und -feuchtigkeit*) sowie zusätzlich für die Bereiche Frischluftanteil und Schwebstoffbelastung geschaffen und aufrechterhalten werden. Die Klimatisierung SOLLTE für das Rechenzentrum ausreichend dimensioniert sein. Alle relevanten Werte SOLLTEN ständig überwacht werden. Weicht ein Wert von der Norm ab, SOLLTE eine automatische Alarmierung stattfinden. 

Die Klimatisierungsanlagen SOLLTEN in Rechnerraumbereichen möglichst ausfallsicher sein, z. B. durch redundant ausgelegte Komponenten. 

#### INF.2.A17 Brandfrüherkennung [Planer, Haustechnik]

Um Brände in Rechenzentren bereits in einem sehr frühen Stadium erkennen zu können, SOLLTE eine Anlage zur Brandfrüherkennung installiert werden.

Damit sich Entstehungsbrände nicht weiter ausbreiten können, SOLLTE durch die Brandfrüherkennung eine automatische Spannungsfreischaltung erfolgen. Dabei SOLLTEN die Überwachungsbereiche der Brandfrüherkennung sowie die Wirkungsbereiche der Spannungsfreischaltung hinreichend kleinteilig konzipiert werden, um ein ausgewogenes Verhältnis zwischen dem Brandschutz einerseits und der RZ-Verfügbarkeit andererseits zu erreichen.

Die Anlage zur Brandfrüherkennung SOLLTE dem aktuellen Stand der Technik entsprechen. Auch SOLLTE sie nach den Vorgaben des Herstellers betrieben und regelmäßig gewartet werden. 

#### INF.2.A18 Schutz vor Wasseraustritt [Haustechnik]

In Bereichen, in denen sich IT-Geräte mit zentralen Funktionen befinden, SOLLTEN wasserführende Leitungen vermieden werden. So SOLLTE es beispielsweise keine Heizkörper im Rechenzentrum geben. 

Sind wasserführende Leitungen (z. B. für die Kühlung direkt auf der RZ-Fläche) unvermeidbar, SOLLTE sichergestellt sein, dass Wasseraustritte möglichst frühzeitig erkannt und die Auswirkungen minimiert werden. Durch Sichtprüfungen SOLLTEN die vorhandenen Wasserleitungen regelmäßig daraufhin überprüft werden, ob sie noch dicht sind. Meldungen einer Detektionsanlage SOLLTEN an verantwortliche Mitarbeiter gemeldet werden, sodass diese anhand von Reaktionsplänen und einer aktuellen Dokumentation schnell eingreifen können (siehe *INF.2.A13 Planung und Installation von Gefahrenmeldeanlagen*). 

#### INF.2.A19 Durchführung von Funktionstests der technischen Infrastruktur [Haustechnik]

Die technische Infrastruktur eines Rechenzentrums SOLLTE regelmäßig (zumindest 1- bis 2-jährlich) sowie nach Systemumbauten und umfangreichen Reparaturen getestet werden. Die Ergebnisse SOLLTEN dokumentiert werden. Es SOLLTEN besonders ganze Reaktionsketten einem echten Funktionstest unterzogen werden.

#### INF.2.A20 Regelmäßige Aktualisierungen der Infrastruktur- und Baupläne [Planer]

Baupläne, Trassenpläne, Strangschemata, Fluchtwegpläne, Feuerwehrlaufkarten usw. SOLLTEN nach jeder Umbaumaßnahme oder wenn die Infrastruktur oder die Sicherheitstechnik erweitert wurde, umgehend aktualisiert werden. Außerdem SOLLTEN die Mitarbeiter entsprechend informiert werden. Es SOLLTE mindestens ein Mal innerhalb von drei Jahren überprüft werden, ob alle relevanten Pläne noch aktuell und korrekt sind.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### INF.2.A21 Ausweichrechenzentrum(A)

Es SOLLTE ein geografisch separiertes Ausweichrechenzentrum aufgebaut und eingesetzt werden. Das Ausweichrechenzentrum SOLLTE so dimensioniert sein, dass alle Prozesse der Institution aufrechterhalten werden können. Auch SOLLTE es ständig einsatzbereit sein. Alle Daten der Institution SOLLTEN regelmäßig ins Ausweichrechenzentrum gespiegelt werden.

#### INF.2.A22 Durchführung von Staubschutzmaßnahmen [Haustechnik](IA)

Wenn ein bestehendes Rechenzentrum erweitert wird, SOLLTEN geeignete Staubschutzmaßnahmen definiert, geplant und umgesetzt werden. Personen, die selbst nicht an den Baumaßnahmen beteiligt sind, SOLLTEN in ausreichend engen Zeitabständen kontrollieren, ob die Staubschutzmaßnahmen ordnungsgemäß funktionieren und die Regelungen zum Staubschutz eingehalten werden.

#### INF.2.A23 Sicher strukturierte Verkabelung im Rechenzentrum [Haustechnik](A)

Kabeltrassen SOLLTEN sorgfältig geplant und ausgeführt werden. Alle Kabel SOLLTEN vor ungewollten mechanischen Beanspruchungen, Manipulationen, Abhörversuchen oder Bränden geschützt sein. Für unterschiedliche Netzarten, z. B. Datennetz, Netz für Gefahrenmeldeanlagen und Stromnetz, SOLLTEN getrennte Kabel benutzt werden. Werden Kabel für verschiedene Netze gemeinsam geführt, SOLLTE sichergestellt sein, dass gegenseitige Störungen minimiert werden. Zudem SOLLTE eine redundante Trassenführung angestrebt werden.

#### INF.2.A24 Einsatz von Videoüberwachungsanlagen [Planer, Haustechnik, Datenschutzbeauftragter](IA)

Die Zutrittskontrolle und die Einbruchmeldung SOLLTEN durch Videoüberwachungsanlagen ergänzt werden. Dazu SOLLTEN die für Videoüberwachungsanlagen sinnvollen Flächen identifiziert werden. 

Eine geplante Videoüberwachung SOLLTE konsistent in das gesamte Sicherheitskonzept eingebettet werden. Auch SOLLTE bei der Planung, Konzeption und eventuellen Auswertung von Videoaufzeichnungen immer der Datenschutzbeauftragte mit einbezogen werden. 

Die für eine Videoüberwachung benötigten zentralen Technikkomponenten SOLLTEN in einer geeigneten Umgebung aufgestellt und geschützt werden. Es SOLLTE regelmäßig überprüft werden, ob die Videoüberwachungsanlage korrekt funktioniert.

#### INF.2.A25 Redundante Auslegung von unterbrechungsfreien Stromversorgungen [Planer]

Um die Verfügbarkeit eines Rechenzentrums sicherzustellen, SOLLTEN die USV-Anlagen redundant ausgelegt sein. Nach einem Stromausfall SOLLTEN alle für den ordnungsgemäßen Betrieb des Rechenzentrums erforderlichen Komponenten so lange mit Strom versorgt werden können, bis eine alternative Stromquelle angeschlossen werden kann. 

#### INF.2.A26 Redundante Auslegung von Netzersatzanlagen(A)

Bei erhöhtem Schutzbedarf SOLLTEN Netzersatzanlagen redundant ausgelegt werden. Es SOLLTE sichergestellt werden, dass auch diese Anlagen regelmäßig gewartet werden (siehe INF.2.A10 *Inspektion und Wartung der Infrastruktur*). 

#### INF.2.A27 Durchführung von Alarmierungs- und Brandschutzübungen(CA)

Mit den Angestellten der Institution SOLLTEN regelmäßige Alarmierungs- und Brandschutzübungen durchgeführt werden. Diese SOLLTEN auf einem Alarmierungsplan basieren, in dem die zu ergreifenden Maßnahmen dokumentiert sind. Es SOLLTE regelmäßig geprüft werden, ob die Maßnahmen noch korrekt, aktuell und praktikabel sind.

#### INF.2.A28 Einsatz von höherwertigen Gefahrenmeldeanlagen(IA)

Für Rechenzentrumsbereiche mit erhöhtem Schutzbedarf SOLLTEN ausschließlich Gefahrenmeldeanlagen der VDS-Klasse C benutzt werden. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Rechenzentrum sowie Serverraum" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BKRZ] Leitfaden Betriebssicheres Rechenzentrum

  

 Bundesverband Informationswirtschaft, Telekommunikation und neue Medien e.V. (BITKOM), 2013 (zuletzt abgerufen 04.10.2017)  
 <http://www.bitkom.org/Bitkom/Publikationen/Betriebssicheres-Rechenzentrum.html>

 
* #### [DIN50600-1] DIN EN 50600-1, Informationstechnik - Einrichtungen und Infrastrukturen von Rechenzentren

  

 Teil 1: Allgemeine Konzepte, DIN, 2012

 
* #### [DIN62305-4] IEC 62305-4 (VDE 0185-305 / DIN EN 62305) – Blitzschutz

  

 Teil 4: Elektrische und elektronische Systemene in baulichen Anlagen, DIN, 2011

 
* #### [VdSPeri] Sicherungsleitfaden Perimeter

  

 VdS Schadenverhütung GmbH, 2012 (zuletzt abgerufen 04.10.2017)  
 [http://vds.de/fileadmin/vds\_publikationen/vds\_3143\_web.pdf](http://vds.de/fileadmin/vds_publikationen/vds_3143_web.pdf)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Rechenzentrum sowie Serverraum" von Bedeutung.

* G 0.5 Naturkatastrophen
* G 0.6 Katastrophen im Umfeld
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.2 Ungünstige klimatische Bedingungen
* G 0.3 Wasser
* G 0.1 Feuer
* G 0.7 Großereignisse im Umfeld
* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.10 Ausfall oder Störung von Versorgungsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.34 Anschlag
* G 0.41 Sabotage
* G 0.44 Unbefugtes Eindringen in Räumlichkeiten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

