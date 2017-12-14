1 Beschreibung
--------------

### 1.1 Einleitung

Die IT-Verkabelung umfasst alle Kommunikationskabel und passiven Komponenten (Rangier- bzw. Spleißverteiler, Patchfelder), die in eigener Hoheit der Institution betrieben werden. Sie ist also die physikalische Grundlage der internen Kommunikationsnetze einer Institution. Die IT-Verkabelung reicht von Übergabepunkten aus einem Fremdnetz (z. B. Anschluss eines TK-Anbieters, DSL-Anbindung eines Internet-Providers) bis zu den Anschlusspunkten der Netzteilnehmer. 

### 1.2 Zielsetzung

Ziel dieses Bausteins ist die IT-Verkabelung so zu schützen, dass die Kommunikation über diese Verbindungen weder mitgehört, noch manipuliert noch gestört werden kann.

### 1.3 Abgrenzung

Aktive Netzkomponenten (Router, Switches etc.) sind nicht Gegenstand dieses Bausteins. Ebenso ist auch das Thema Funknetze und WLAN ausgeklammert. Diese Themen werden in eigenen Bausteinen des IT-Grundschutz-Kompendiums behandelt. In diesem Baustein wird mit IT-Verkabelung die physische Grundlage eines hersteller- und anwendungsneutralen Kommunikationsnetzes, also eines Local Area Networks (LAN), bezeichnet. Eine Unterscheidung zwischen IT-Verkabelung zum Datentransport und TK-Verkabelung für Telekommunikationsdienste erfolgt nicht.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich IT-Verkabelung von besonderer Bedeutung:

### 2 1 Kabelbrand

Kabelbrände können erhebliche Schäden nach sich ziehen. Einige dieser Folgen sind zum Beispiel Kurzschlüsse, die Unterbrechung des Schutzleiters, die Entwicklung aggressiver Gase, Feuer oder die Entstehung von Schwelbränden. Kabelbrände bewirken in der Entstehungsphase häufig nur einen geringen Anstieg der Umgebungstemperatur. Damit besteht die zusätzliche Gefährdung, dass eine erhebliche Verrauchung durch "kalten" Brandrauch entsteht, bevor Rauchmelder ansprechen, die an der Raumdecke angebracht sind.

### 2 2 Unzureichende Netzdimensionierung

Wenn ein IT-Netz nicht ausreichend dimensioniert ist, leidet die Verfügbarkeit. Bei der Planung von Netzen, Trassen, Serverräumen oder Rechenzentren wird oft der Fehler begangen, die funktionale, kapazitive oder sicherheitstechnische Auslegung ausschließlich am aktuellen Bedarf auszurichten. Dabei wird übersehen, dass eine Erweiterung der Kapazität des Netzes durch neue Anforderungen eben so nötig werden kann wie z. B. durch die Änderung von technischen Standards. Eine Erweiterung von Netzen ist aber nur in dem Umfang möglich, wie es die vorhandenen, verlegten Kabel zulassen oder der zur Verfügung stehende Platz für zusätzliche Kabel erlaubt.

### 2 3 Unzureichende Dokumentation der Verkabelung

Ist aufgrund unzureichender Dokumentation die genaue Lage von Leitungen nicht bekannt, so kann es bei Bauarbeiten außerhalb oder innerhalb eines Gebäudes zu Beschädigungen von Leitungen kommen. Es kann nicht davon ausgegangen werden, dass alle Kabel und Leitungen in den Installationszonen gemäß gültiger Normen installiert sind. Eine unzureichende Dokumentation erschwert zudem die Prüfung, Wartung und Reparatur von Leitungen.

### 2 4 Unzulässige Kabelverbindungen

Wenn zwischen IT-Systemen oder anderen technischen Komponenten Kabelverbindungen hergestellt werden, die nicht vorgesehen sind, besteht die Gefahr, dass dadurch Sicherheitsprobleme oder Betriebsstörungen entstehen. Beispielsweise kann es aufgrund solcher unzulässiger Kabelverbindungen passieren, dass unerlaubt auf Netze, Systeme, Informationen oder Anwendungen zugegriffen werden kann. Durch unzulässige Kabelverbindungen können Informationen zusätzlich oder ausschließlich zu falschen Empfängern übertragen werden. Die normale Verbindung kann gestört werden.

### 2 5 Leitungsbeschädigungen

Je ungeschützter ein Kabel verlegt ist, desto größer ist die Gefahr einer Beschädigung. Eine Beschädigung führt nicht unbedingt sofort zu einem Ausfall von Verbindungen, sondern kann auch sporadische, schwer zu detektierende Übertragungsfehler nach sich ziehen. Auch die zufällige Entstehung unzulässiger Verbindungen ist möglich, wenn beispielsweise Kabelmäntel beziehungsweise Isolierungen nicht mehr vollständig intakt sind. Eine Beschädigung muss dabei nicht zwingend absichtlich erfolgen, sondern kann auch unbeabsichtigt entstehen.

### 2 6 Leitungsbeeinträchtigung

Die Übertragungseigenschaften von Kabeln mit elektrischer Signalübertragung können durch elektrische und magnetische Felder in ihrem Umfeld negativ beeinflusst werden. Übersprechen ist eine spezielle Form dieser Leitungsbeeinträchtigung. Dabei wird die Störung nicht allgemein im Umfeld, sondern durch Ströme und Spannungen von Signalen erzeugt, die auf eine benachbarte Leitung übertragen werden.

### 2 7 Abhören und Manipulation von Leitungen

Abhörangriffe auf Leitungen sind eine Gefahr für die Informationssicherheit, die nicht vernachlässigt werden sollte. Grundsätzlich gibt es keine abhörsicheren Kabel. Lediglich hinsichtlich des zum Abhören erforderlichen Aufwands unterscheiden sich die Kabel. Ob eine Leitung tatsächlich abgehört wird, ist nur mit hohem messtechnischem Aufwand feststellbar. Neben dem Abhören von Leitungen stellen weitere bewusste Manipulationen oder gar die Zerstörung von IT-Leitungen eine Gefahr für die Institution dar. Fehlfunktionen von Leitungen können bewusst und in manipulativer Absicht herbeigeführt werden. Solche Manipulationen verfolgen oftmals das Ziel, den IT-Betrieb zu stören oder finanzielle Schäden für die Institution zu verursachen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich IT-Verkabelung aufgeführt. Grundsätzlich ist der Leiter IT für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### INF.4.A1 Auswahl geeigneter Kabeltypen [Leiter Haustechnik]

Bei der Auswahl von Kabeln MÜSSEN die übertragungstechnischen Notwendigkeiten und die Umgebungsbedingungen bei der Verlegung sowie im Betrieb berücksichtigt werden. Die Auswahl der Kabel aus kommunikationstechnischer Sicht MUSS durch die erforderliche Übertragungsrate und die Entfernung zwischen den Übertragungseinrichtungen bestimmt werden. Im Bezug auf die Umgebungsbedingungen MÜSSEN Faktoren wie z. B. die Temperaturen, Kabelwege, Zugkräfte bei der Verlegung, die Verlegeart und etwaige Störquellen beachtet werden. Des Weiteren MÜSSEN die anzuwendenden Normen und Vorschriften bei der Auswahl der Kabel berücksichtigt werden.

#### INF.4.A2 Planung der Kabelführung [Leiter Haustechnik]

Kabel, Kabelwege und Kabeltrassen MÜSSEN vor ihrer Verlegung sowohl aus technischer wie auch aus physischer Sicht ausreichend dimensioniert werden. Dabei MÜSSEN zukünftige übertragungstechnische Notwendigkeiten ebenso mit einkalkuliert werden wie genügend Platz für mögliche technische Erweiterungen in Kabelkanälen und -trassen. Bei der gemeinsamen Führung von IT- und Stromverkabelung in einer Trasse MUSS außerdem darauf geachtet werden, das Übersprechen zwischen den einzelnen Kabeln zu vermeiden. Es MUSS darauf geachtet werden, erkennbare Gefahrenquellen zu umgehen.

#### INF.4.A3 Fachgerechte Installation [Leiter Haustechnik]

Installationsarbeiten an der IT-Verkabelung MÜSSEN sorgfältig und fachkundig erfolgen. Gleichzeitig MÜSSEN alle relevanten Normen beachtet werden. Die entscheidenden Kriterien für eine fachgerechte Ausführung der IT-Verkabelung MÜSSEN vom Auftraggeber in allen Phasen überprüft werden. Bei Anlieferung des Materials MUSS geprüft werden, ob die richtigen Kabel und Anschlusskomponenten geliefert wurden. Bei der Verlegung von IT-Kabeln MUSS besondere Sorgfalt darauf gelegt werden, dass die Montage keine Beschädigungen hervorruft und dass die Kabelwege so gewählt sind, dass Beschädigungen der verlegten Kabel durch die normale Nutzung des Gebäudes ausgeschlossen sind. Zudem MUSS generell darauf geachtet werden, dass IT-Kabel getrennt von der elektrotechnischen Verkabelung geführt werden. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich IT-Verkabelung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### INF.4.A4 Anforderungsanalyse für die IT-Verkabelung

Grundsätzlich SOLLTE eine Analyse der Anforderungen, die Einfluss auf eine zukunftssichere, bedarfsgerechte und wirtschaftliche Ausführung der IT-Verkabelung haben, durchgeführt werden. In ihr SOLLTE zunächst die kurzfristig geplante Nutzung durch die Anwender in der Institution und darauf aufbauend die längerfristige Entwicklung der IT-Nutzung abgeschätzt werden. Darüber hinaus MÜSSEN die Schutzziele der Verfügbarkeit, Integrität und Vertraulichkeit bei der Anforderungsanalyse für die IT-Verkabelung mit betrachtet werden.

#### INF.4.A5 Abnahme der IT-Verkabelung [Leiter Haustechnik]

Die IT-Verkabelung SOLLTE einem Abnahmeprozess unterzogen werden. Diese SOLLTE erst dann erfolgen, wenn alle durchzuführenden Aufgaben abgeschlossen sind, der Ausführende die Maßnahme zur Abnahme gemeldet hat und sich bei den Kontrollen durch den Auftraggeber keine inakzeptablen Mängel gezeigt haben. Der Abnahmetermin SOLLTE zeitlich so gewählt werden, dass die Kontrollen zur Abnahme in ausreichender Zeit vorbereitet werden können. Bei der Abnahme MÜSSEN die Aspekte der Informationssicherheit kontrolliert werden. Für das Abnahmeprotokoll SOLLTE eine Checkliste vorbereitet werden. Die Checkliste SOLLTE auch Punkte zu allgemeinen Anforderungen an die Betriebsräume enthalten. Das Abnahmeprotokoll MUSS von den Teilnehmern und Verantwortlichen unterzeichnet werden.

#### INF.4.A6 Laufende Fortschreibung und Revision der Netzdokumentation

Die Dokumentation der IT-Verkabelung SOLLTE als ein elementarer Bestandteil einer jeden Veränderung im Netz betrachtet und behandelt werden. Hierbei SOLLTEN alle von der Änderung betroffenen Dokumentationsbereiche leicht erfasst und angepasst werden können. Außerdem SOLLTE geprüft werden, ob der Einsatz eines Dokumentenmanagements für die Netzdokumentation zweckmäßig ist.

#### INF.4.A7 Entfernen und Deaktivieren nicht mehr benötigter IT-Verkabelung [Leiter Haustechnik]

Wenn IT-Verkabelung nicht mehr benötigt wird, SOLLTE sie fachgerecht und vollständig entfernt werden. IT-Verkabelung, die mit der vorhandenen Technik sinnvoll als Reserve weiter genutzt werden kann, SOLLTE in einem betriebsfähigen Zustand erhalten bleiben. Grundsätzlich SOLLTE eine Übersicht über nicht mehr benötigte Kabel aufgestellt und anhand dieser Dokumentation die Deaktivierung oder der Abbau/Ausbau der Kabel belegt werden. Anschließend MUSS die Dokumentation, in der der Bestand der IT-Verkabelung aufgeführt ist, aktualisiert werden.

#### INF.4.A8 Brandabschottung von Trassen [Leiter Haustechnik]

Zur Vermeidung von Kabelbränden SOLLTEN Trassen über eine ausreichende Be- und Entlüftung verfügen. Die brandschutztechnischen Auflagen MÜSSEN eingehalten werden. Darüber hinaus SOLLTEN nach Abschluss der Installationsarbeiten die Brandabschottung in regelmäßigen Abständen kontrolliert werden.

#### INF.4.A9 Dokumentation und Kennzeichnung der IT-Verkabelung

Eine Institution SOLLTE sicherstellen, dass sie für ihre IT-Verkabelung eine interne und eine externe Dokumentation besitzt. Die interne Dokumention MUSS alle Aufzeichnungen, die die Errichtung und den Betrieb der IT-Verkabelung betreffen, enthalten. Die interne Dokumentation SOLLTE so umfangreich angefertigt und gepflegt werden, dass der Betrieb und die zukünftige Weiterentwicklung der IT-Netze bestmöglich unterstützt werden. Die externe Dokumentation der Verkabelung SOLLTE so sparsam wie möglich ausfallen.

#### INF.4.A10 Neutrale Dokumentation in den Verteilern

In jedem Verteiler SOLLTE sich eine Dokumentation befinden, die den derzeitigen Stand von Rangierungen und Leitungsbelegungen wiedergibt. Diese Dokumentation SOLLTE möglichst neutral gehalten werden. Nur bestehende und genutzte Verbindungen SOLLTEN darin aufgeführt sein. Es SOLLTEN, soweit nicht ausdrücklich vorgeschrieben, keine Hinweise auf die Nutzungsart der Leitungen gegeben werden. Alle weitergehenden Informationen MÜSSEN in einer Revisionsdokumentation aufgeführt werden.

#### INF.4.A11 Kontrolle bestehender Verbindungen

Alle Verteiler und Zugdosen der Verkabelung SOLLTEN regelmäßig einer (zumindest stichprobenartigen) Sichtprüfung unterzogen werden. Neben der reinen Sichtkontrolle SOLLTE zusätzlich eine funktionale Kontrolle durchgeführt werden. Alle Unregelmäßigkeiten, die bei Sichtkontrollen oder funktionalen Kontrollen festgestellt werden, MÜSSEN unverzüglich dokumentiert und den zuständigen Organisationseinheiten gemeldet werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### INF.4.A12 Redundanzen für die Verkabelung(A)

Es SOLLTE geprüft werden, ob zumindest für wichtige Gebäude eine redundante, über unabhängige Trassen geführte primäre IT-Verkabelung geschaffen werden soll. Ebenso SOLLTE geprüft werden, ob die Anschlüsse an IT- oder TK-Provider redundant ausgelegt werden sollen. Bei hohen oder sehr hohen Verfügbarkeitsanforderungen SOLLTE überlegt werden, in den relevanten Gebäuden die Sekundär- und Tertiärverkabelung redundant auszulegen. Dabei SOLLTE die Sekundärverkabelung über mindestens zwei Steigeschächte geführt werden, die sich in verschiedenen Brandabschnitten des Gebäudes befinden sollten. Wird eine redundante Verkabelung verwendet SOLLTE deren Funktionsfähigkeit regelmäßig geprüft werden.

#### INF.4.A13 Materielle Sicherung der IT-Verkabelung(IA)

In Räumen mit Publikumsverkehr oder in unübersichtlichen Bereichen eines Gebäudes SOLLTEN Leitungen und Verteiler zusätzlich gegen unbefugte Zugriffe gesichert werden. In jedem Fall SOLLTE die Zahl der Stellen, an denen das verlegte Kabel zugänglich ist, auf ein Mindestmaß reduziert und die Länge der vor unberechtigten Zugriff zu schützenden Verbindungen möglichst klein gehalten werden.

#### INF.4.A14 Verhinderung von Ausgleichsströmen auf Schirmungen(A)

Die Stromversorgung der IT-Komponenten SOLLTE so gewählt sein, das Störungen durch Ausgleichsströme auf den Schirmungen von Datenleitungen verhindert werden. Je nach Netzform SOLLTEN außerdem Vorkehrungen gegen Einstrahlungen von außen, Abstrahlung durch die Leitung sowie zur Erkennung von Ausgleichsströmen getroffen werden.

#### INF.4.A15 Nutzung von Schranksystemen(IA)

Zur Verbesserung der Betriebssicherheit von aktiven und passiven Netzkomponenten SOLLTEN diese Geräte in Schranksystemen eingebaut oder aufgestellt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "IT-Verkabelung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [DIN4102] DIN 4102:2016-05

  

 Brandverhalten von Baustoffen und Bauteilen, Beuth Verlag 

 
* #### [DIN41494] DIN 41494

  

 Bauweisen für elektronische Einrichtungen, Beuth Verlag

 
* #### [DIN60297] DIN IEC 60297

  

 Bauweisen für elektronische Einrichtungen, Beuth Verlag 

 
* #### [EN50173] EN 50173:2007

  

 Informationstechnik - Anwendungsneutrale Kommunikationskabelanlagen, Beuth Verlag 

 
* #### [EN50174] EN 50174:2009

  

 Informationstechnik - Installation von Kommunikationsverkabelung, Beuth Verlag 

 
* #### [EN50310] EN 50310:2010

  

 Anwendung von Maßnahmen für Erdung und Potentialausgleich in Gebäuden mit Einrichtungen der Informationstechnik, VDE Verlag, 2010

 
* #### [EN50346] EN 50346:2010

  

  Prüfung installierter Verkabelung, Beuth Verlag, 2010 

 
* #### [IEC60364] IEC60364- Einrichten von Niederspannungsanlagen

  

 Beuth Verlag

 
* #### [IEEE8023] IEEE8023

  

 IEEE 802.3 – Standards in Lokalen Netzen, CSMA/CD, Ethernet Working Group, (zuletzt abgerufen am 28.09.2017)  
 [http://www.ieee802.org/3/ ](http://www.ieee802.org/3/)

 
* #### [ISO11801] ISO/IEC 11801:2010

  

 Informationstechnik - Anwendungsneutrale Standortverkabelung, ISO, 2010

 
* #### [VDE100] DIN VDE 0100- Bestimmung für das Errichten von Starkstromanlagen mit Notspannungen bis 1000V

  

 VDE Verlag 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "IT-Verkabelung" von Bedeutung.

* G 0.1 Feuer
* G 0.2 Ungünstige klimatische Bedingungen
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.12 Elektromagnetische Störstrahlung
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.37 Abstreiten von Handlungen
* G 0.41 Sabotage
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

