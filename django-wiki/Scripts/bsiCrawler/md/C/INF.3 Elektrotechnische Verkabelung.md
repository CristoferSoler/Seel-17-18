1 Beschreibung
--------------

### 1.1 Einleitung

Die elektrotechnische Verkabelung von IT-Systemen und anderen Geräten umfasst alle Kabel und Verteilungen im Gebäude vom Einspeisepunkt des Verteilungsnetzbetreibers bis zu den Elektro-Anschlüssen der Verbraucher. 

Die ordnungsgemäße und normgerechte Ausführung der elektrotechnischen Verkabelung ist Grundlage für den sicheren IT-Betrieb.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist der Schutz der gesamten elektrotechnischen Verkabelung gegen Ausfall und Störung der Stromversorgung.

### 1.3 Abgrenzung

Die IT-Verkabelung zur Kommunikation der IT-Systeme wird in einem separaten Baustein behandelt (siehe INF.4 IT-Verkabelung).

2 Gefährdungslage
-----------------

Folgende spezifischen Bedrohungen und Schwachstellen sind im Bereich elektrotechnische Verkabelung von besonderer Bedeutung:

### 2 1 Kabelbrand

Wenn ein Kabel in Brand gerät, sei es durch Selbstentzündung oder durch Beflammung, kann dies verschiedene Folgen haben. Einige dieser Folgen sind zum Beispiel Kurzschlüsse, die Unterbrechungen des Schutzleiters, die Entwicklung aggressiver Gase, Feuer oder die Entstehung von Schwelbränden. Kabelbrände bewirken in der Entstehungsphase häufig nur einen geringen Anstieg der Temperatur. Damit besteht die zusätzliche Gefährdung, dass eine erhebliche Verrauchung durch "kalten" Brandrauch entsteht, bevor Rauchmelder ansprechen, die an der Raumdecke angebracht sind.

### 2 2 Unzureichende Dimensionierung der elektrotechnischen Verkabelung

Bei der Planung von Arbeitsplätzen, Serverräumen oder Rechenzentren wird oft der Fehler begangen, diese ausschließlich am aktuellen Bedarf auszurichten. Dabei wird übersehen, dass durch neue Anforderungen wie die Nutzung weiterer Server die Kapazität des Stromnetzes erweitert werden muss. Eine Erweiterung der elektrotechnischen Verkabelung ist aber nur in dem Umfang möglich, wie es die vorhandenen, verlegten Kabel zulassen oder der zur Verfügung stehende Platz für zusätzliche Kabel und Verteilungen erlaubt.

### 2 3 Unzureichende Dokumentation der Verkabelung

Ist aufgrund unzureichender Dokumentation die genaue Lage von Leitungen nicht bekannt, so kann es bei Bauarbeiten außerhalb oder innerhalb eines Gebäudes zu Beschädigungen von Leitungen kommen. Es kann nicht davon ausgegangen werden, dass alle Kabel und Leitungen in den Installationszonen gemäß gültiger Normen installiert sind. Eine unzureichende Dokumentation erschwert zudem die Prüfung, Wartung und Reparatur von Leitungen.

### 2 4 Unzureichende geschützte Verteiler

Unterverteilungen des Stromversorgungsnetzes sind vielfach frei zugänglich und unverschlossen in Fluren oder Treppenhäusern untergebracht. Dadurch ist es jedermann möglich, diese Verteiler zu öffnen, Manipulationen vorzunehmen und gegebenenfalls einen Stromausfall herbeizuführen. Ferner kann von solchen Verteilern eine unmittelbare Gefahr ausgehen, da nach Entnahme von Schraubsicherungen und deren Sockeln ein direktes Berühren spannungsführender Teile möglich ist. Offenstehende Türen an den Verteilerkästen können zudem den Verkehrsweg behindern, auch Verletzungen durch Klemmen und Quetschen an den Scherkanten sind möglich.

### 2 5 Leitungsbeschädigungen

Je ungeschützter ein Kabel verlegt ist, desto größer ist die Gefahr einer Beschädigung. Eine Beschädigung führt nicht unbedingt sofort zu einem Ausfall von Verbindungen. Auch die zufällige Entstehung unzulässiger Verbindungen ist möglich, wenn beispielsweise Kabelmäntel beziehungsweise Isolierungen nicht mehr vollständig intakt sind. Eine Beschädigung muss dabei nicht zwingend absichtlich erfolgen, sondern kann auch unbeabsichtigt entstehen.

### 2 6 Spannungsschwankungen und Über- bzw. Unterspannung

Durch Schwankungen der Versorgungsspannung kann es zu Funktionsstörungen und Beschädigungen der IT kommen. Die Schwankungen reichen von extrem kurzen und kleinen Ereignissen, die sich kaum oder gar nicht auf die IT auswirken, bis zu Totalausfällen oder zerstörerischen Überspannungen. Die Ursache dafür kann in allen Bereichen des Stromversorgungsnetzes entstehen, vom Netz des Energieversorgungsunternehmens bis zum Stromkreis, an dem die jeweiligen Geräte angeschlossen sind. 

### 2 7 Verwendung unzureichender Steckdosenleisten

Oft reicht die Zahl fest installierter Steckdosen für die Menge der zu betreibenden Geräte nicht aus. Um diesen Mangel auszugleichen, werden dann typischerweise Steckdosenleisten verwendet. Solche Steckdosenleisten stellen, wenn sie von unzureichender Qualität sind, eine gefährliche Zündquelle und damit eine große Brandgefahr dar. Werden zusätzlich mehrere kleinere Steckdosenleisten hintereinander geschaltet, um ausreichende Steckplätze für alle Geräte bereitzustellen, steigt die Gefahr durch zu geringen Leitungsquerschnitt und Überlastung weiter an.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich elektrotechnischer Verkabelung aufgeführt. Grundsätzlich ist der Leiter Haustechnik für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### INF.3.A1 Auswahl geeigneter Kabeltypen

Bei der Auswahl von Kabeln MÜSSEN die übertragungstechnischen Notwendigkeiten und die Umgebungsbedingungen bei der Verlegung sowie im Betrieb zu berücksichtigt werden. Bei der Auswahl von Elektrokabeln MÜSSEN die einschlägigen Normen und Vorschriften beachtet werden. In Bezug auf die Umgebungsbedingungen MÜSSEN Faktoren wie z. B. die Temperaturen, Kabelwege, Zugkräfte bei der Verlegung, die Verlegeart und etwaige Störquellen beachtet werden. 

#### INF.3.A2 Planung der Kabelführung [Leiter IT]

Kabel, Kabelwege und Kabeltrassen MÜSSEN vor ihrer Verlegung sowohl aus funktionaler wie auch aus physikalische Sicht ausreichend dimensioniert werden. Dabei MÜSSEN zukünftige elektrotechnische Notwendigkeiten ebenso mit einkalkuliert werden wie genügend Platz für mögliche technische Erweiterungen in Kabelkanälen und -trassen. Bei der gemeinsamen Führung von IT- und Stromverkabelung in einer Trasse MUSS außerdem darauf geachtet werden, das Übersprechen zwischen den einzelnen Kabeln zu vermeiden. Es SOLLTE generell darauf geachtet werden, dass IT-Kabel getrennt von der elektrotechnischen Verkabelung geführt werden. Es MUSS darauf geachtet werden, erkennbare Gefahrenquellen zu umgehen.

#### INF.3.A3 Fachgerechte Installation

Die Installationsarbeiten der elektrotechnischen Verkabelung MÜSSEN sorgfältig und fachkundig erfolgen. Gleichzeitig MÜSSEN alle relevanten Normen beachtet werden. Die entscheidenden Kriterien für eine fachgerechte Ausführung der elektrotechnischen Verkabelung MÜSSEN daher vom Auftraggeber in allen Phasen überprüft werden. Bei Anlieferung des Materials MUSS geprüft werden, ob die richtigen Kabel und Anschlusskomponenten geliefert wurden. Bei der Verlegung von Stromkabeln MUSS besondere Sorgfalt darauf gelegt werden, dass die Montage keine Beschädigungen hervorruft und dass die Kabelwege so gewählt sind, dass Beschädigungen der verlegten Kabel durch die normale Nutzung des Gebäudes ausgeschlossen sind. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Elektrotechnische Verkabelung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### INF.3.A4 Anforderungsanalyse für die elektrotechnische Verkabelung

Grundsätzlich SOLLTE eine Analyse der Anforderungen, die Einfluss auf eine zukunftssichere, bedarfsgerechte und wirtschaftliche Ausführung der elektrotechnischen Verkabelung haben, durchgeführt werden. In ihr SOLLTE zunächst die kurzfristig geplante Nutzung durch die Anwender in der Institution und darauf aufbauend die längerfristige Entwicklung der Nutzung abgeschätzt werden. 

#### INF.3.A5 Abnahme der elektrotechnischen Verkabelung

Die elektrotechnische Verkabelung SOLLTE einem Abnahmeprozess unterzogen werden. Eine Abnahme SOLLTE erst dann erfolgen, wenn alle durchzuführenden Aufgaben abgeschlossen sind, der Ausführende die Maßnahme zur Abnahme gemeldet hat und sich bei den Kontrollen durch den Auftraggeber keine inakzeptablen Mängel gezeigt haben. Der Abnahmetermin SOLLTE zeitlich so gewählt werden, dass die Kontrollen zur Abnahme in ausreichender Zeit vorbereitet werden können. Neben der korrekten Abrechnung und dem tatsächlichen Umfang der Leistungen MÜSSEN bei der Abnahme die Einhaltung der unterschiedlichen Normen für elektrotechnische Verkabelungen kontrolliert werden. Für das Abnahmeprotokoll SOLLTE eine Checkliste vorbereitet werden. Die Checkliste SOLLTE auch Punkte zu allgemeinen Anforderungen an die Betriebsräume enthalten. Das Abnahmeprotokoll MUSS von den Teilnehmern und Verantwortlichen rechtsverbindlich unterzeichnet werden. Das Protokoll SOLLTE Bestandteil der internen Dokumentation der Verkabelung sein.

#### INF.3.A6 Überspannungsschutz

Jedes elektrisch leitende Netz SOLLTE gegen Überspannungen geschützt werden. Hierfür MUSS ein den gültigen Normen entsprechendes Überspannungsschutzkonzept erstellt werden. Netzersatzanlagen und unterbrechungsfreie Stromversorgungen SOLLTEN in das Konzept mit aufgenommen werden. 

#### INF.3.A7 Entfernen und Deaktivieren nicht mehr benötigter Leitungen

Wenn Stromkabel nicht mehr benötigt werden, SOLLTEN sie fachgerecht und vollständig entfernt werden. Anschließend MÜSSEN die Brandschottungen fachgerecht verschlossen werden. Verkabelung, die mit der vorhandenen Technik sinnvoll als Reserve weiter genutzt werden kann, SOLLTE in einem betriebsfähigen Zustand erhalten bleiben. Solche Kabel MÜSSEN mindestens an den Endpunkten entsprechend gekennzeichnet werden. Grundsätzlich SOLLTE eine Übersicht über nicht mehr benötigte Kabel aufgestellt und anhand dieser Dokumentation die Deaktivierung oder der Abbau/Ausbau der Kabel belegt werden. Anschließend MUSS die entsprechende Dokumentation aktualisiert werden.

#### INF.3.A8 Brandschutz in Trassen

Zur Vermeidung von Kabelbränden SOLLTEN Trassen ausreichend dimensioniert werden. Darüber hinaus SOLLTE nach Abschluss der Installationsarbeiten die Belegungsdichte der Trassen in vernünftigen Abständen überprüft werden.

#### INF.3.A9 Dokumentation und Kennzeichnung der elektrotechnischen Verkabelung

Eine Institution SOLLTE sicherstellen, dass sie für ihre elektrotechnische Verkabelung eine interne und eine externe Dokumentation besitzt. Die interne Dokumentation MUSS alle Aufzeichnungen, die die Installation und den Betrieb der Verkabelung betreffen, enthalten. Die interne Dokumentation SOLLTE so umfangreich angefertigt und gepflegt werden, dass der Betrieb und die zukünftige Weiterentwicklung bestmöglich unterstützt werden. Die externe Dokumentation der Verkabelung SOLLTE so möglichst neutral gehalten werden.

#### INF.3.A10 Neutrale Dokumentation in den Verteilern

In jedem Verteiler SOLLTE sich eine Dokumentation befinden, die den derzeitigen Stand von Rangierungen und Leitungsbelegungen wiedergibt. Diese Dokumentation SOLLTE möglichst neutral gehalten werden und MUSS ein sicheres Schalten ermöglichen Nur bestehende und genutzte Verbindungen, sowie auflaufende Reserveleitungen SOLLTEN darin aufgeführt sein. Es SOLLTEN, soweit nicht ausdrücklich vorgeschrieben, keine Hinweise auf die Nutzungsart der Leitungen gegeben werden. Alle weitergehenden Informationen SOLLTEN in einer Revisionsdokumentation aufgeführt werden.

#### INF.3.A11 Kontrolle elektrotechnischer Anlagen und Verbindungen

Alle elektrotechnischen Anlagen, Verteiler und Zugdosen der Verkabelung SOLLTEN regelmäßig einer (zumindest stichprobenartigen) Sichtprüfung unterzogen werden. Neben der reinen Sichtkontrolle SOLLTE zusätzlich eine funktionale Kontrolle durchgeführt werden, sofern im Rahmen der DGUV-V3-Prüfung eine solche Kontrolle nicht bereits erfolgt ist. Alle Unregelmäßigkeiten, die bei Sichtkontrollen oder funktionalen Kontrollen festgestellt werden, MÜSSEN unverzüglich dokumentiert und den zuständigen Organisationseinheiten gemeldet werden. Die zuständigen Organisationseinheiten MÜSSEN im Anschluss die festgestellten Unregelmäßigkeiten überprüfen und beheben.

#### INF.3.A12 Vermeidung elektrischer Zündquellen

Die Nutzung privater Elektrogeräte innerhalb einer Institution SOLLTE klar geregelt werden. Alle Elektrogeräte SOLLTEN vor ihrer Verwendung durch eine Elektrofachkraft geprüft und für sicher befunden werden. Die Verwendung von Steckdosenleisten SOLLTE soweit wie möglich vermieden werden. Fehlende Steckdosen SOLLTEN durch eine Elektrofachkraft in vorhandene Kanalsysteme nachgerüstet oder fachgerecht auf Putz montiert werden. 

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### INF.3.A13 Sekundär-Energieversorgung(A)

Die primäre Energieversorgung aus dem Netz eines Energieversorgungs-Unternehmens SOLLTE bei erhöhten Anforderungen an die Verfügbarkeit um Maßnahmen zur Notfall-Versorgung ergänzt werden. Dafür SOLLTE für die abzusichernden Bereiche eine ausreichend dimensionierte zentrale USV und eine Netzersatzanlage (NEA) eingerichtet werden. Es SOLLTE geprüft werden, ob die Anschlüsse an den Netzbetreiber redundant ausgelegt werden sollen. NEA und USV MÜSSEN regelmäßig gewartet werden. 

#### INF.3.A14 A-B-Versorgung(A)

Es SOLLTE geprüft werden, ob über die normale einzügige Stromversorgung wichtiger IT-Komponenten hinaus eine zweizügige, sogenannte A-B-Versorgung geschaffen werden soll. Dabei SOLLTE sichergestellt werden, dass deren Funktionsfähigkeit permanent durch geeignete technische Einrichtungen, z. B. durch die Gebäudeleittechnik (GLT), überwacht wird.

#### INF.3.A15 Materielle Sicherung der elektrotechnischen Verkabelung(A)

In Räumen mit Publikumsverkehr oder in unübersichtlichen Bereichen eines Gebäudes SOLLTE überlegt werden, Leitungen und Verteiler gegen unbefugte Zugriffe zu sichern. In jedem Fall SOLLTE die Zahl und der Umfang der Stellen, an denen Einrichtungen der Energieversorgung für Unbefugte zugänglich sind, auf ein Mindestmaß reduziert werden.

#### INF.3.A16 Nutzung von Schranksystemen(A)

Zur Verbesserung der Betriebssicherheit elektrotechnischen Anschlüssen und -verteilern SOLLTEN diese Geräte in Schranksystemen eingebaut oder aufgestellt werden.

Die IT-Hardware SOLLTE, soweit es möglich ist, in Schranksystemen untergebracht werden. Diese SOLLTEN in Tiefe und Breite dem zunehmenden Platzbedarf der Einbaugeräte genügen und mit entsprechenden Zusatzeinrichtungen ausgerüstet oder jederzeit nachrüstbar sein.

#### INF.3.A17 Brandschott-Kataster(A)

Es SOLLTE ein Brandschott-Kataster geführt werden. In diesem SOLLTEN alle Arten von Schotts individuell aufgenommen werden. Nach Arbeiten an Brandschotts SOLLTEN die Änderungen im Kataster spätestens nach 4 Wochen eingetragen werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Elektrotechnische Verkabelung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BGVA3] Berufsgenossenschaftliche Vorschrift für Sicherheit und Gesundheit bei der Arbeit

  

 – A3 Elektrische Anlagen und Betriebsmittel 

 
* #### [DIN4102] DIN 4102:2016-05

  

 Brandverhalten von Baustoffen und Bauteilen, Beuth Verlag 

 
* #### [IEC60364] IEC60364- Einrichten von Niederspannungsanlagen

  

 Beuth Verlag

 
* #### [IEC62305] IEC 62305 (VDE 0185-305 / DIN EN 62305) – Blitzschutz

  

 Normreihe zum Blitzschutz von baulichen Anlagen, (zuletzt abgerufen 05.10.2017)  
 <https://www.vde.com/resource/blob/936756/5b65d838e75e83f750bd8fa23bb620b1/merkblatt-blitzschutznormen-13-download-data.pdf>

 
* #### [VDE100] DIN VDE 0100- Bestimmung für das Errichten von Starkstromanlagen mit Notspannungen bis 1000V

  

 VDE Verlag 

 
* #### [VDE105] DIN VDE 0105-100 – Betrieb von elektrischen Anlagen

  

 VDE Verlag 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Elektrotechnische Verkabelung" von Bedeutung.

* G 0.1 Feuer
* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.12 Elektromagnetische Störstrahlung
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.41 Sabotage
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

