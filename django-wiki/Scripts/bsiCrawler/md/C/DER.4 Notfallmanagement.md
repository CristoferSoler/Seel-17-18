1 Beschreibung
--------------

### 1.1 Einleitung

In Notfallsituationen ist ein Zugriff auf Informationen zur Wiederherstellung eines Geschäftsprozesses, eines IT-Systems oder einer Fachaufgabe unentbehrlich. Hierzu sollten die entsprechenden Prozesse zur Aufrechterhaltung der Informationssicherheit in einem Notfall geplant, etabliert und überprüft werden.

Nur wenn geplant und organisiert vorgegangen wird, ist eine optimale Notfallvorsorge und Notfallbewältigung möglich. Ein professioneller Prozess zum Notfallmanagement reduziert deren Auswirkungen und sichert somit den Betrieb und Fortbestand der Institution. Es sind geeignete Maßnahmen zu identifizieren und umzusetzen, durch die Geschäftsprozesse und Fachaufgaben zum einen robuster und ausfallsicherer werden und die es zum anderen ermöglichen, den Notfall schnell und zielgerichtet zu bewältigen.

Die Aufrechterhaltung der Informationssicherheit ist deshalb in ein übergreifendes Notfallmanagement einzubinden. Das Notfallmanagement hat jedoch einen eigenen Prozessverantwortlichen (den Notfallbeauftragten), mit dem sich der Informationssicherheitsbeauftragte abstimmt.

### 1.2 Zielsetzung

Ziel des Bausteins Notfallmanagement ist es, Anforderungen zu beschreiben, durch die die Informationssicherheit selbst in kritischen Situationen gewährleistet wird. Dazu sind die entsprechenden Maßnahmen in ein ganzheitliches Kontinuitätsmanagement einzubetten und alle Aspekte zu betrachten, die erforderlich sind, um die Informationssicherheit auch bei Eintritt eines Schadensereignisses aufrechterhalten zu können. Dies reicht von der Planung bis zur Überprüfung aller Prozesse.

### 1.3 Abgrenzung

Bei Eintritt eines Schadensereignisses müssen die richtigen Informationen vollständig und korrekt zur Verfügung stehen. Im vorliegenden Baustein werden weder Kriterien noch Prozesse erläutert, anhand derer die Verantwortlichen entscheiden können, ob ein Notfall vorliegt oder nicht. Die Entscheidung darüber wird getroffen, während der Sicherheitsvorfall behandelt wird (siehe DER.2.1 *Behandlung von Sicherheitsvorfällen*).

Krisen werden im Rahmen eines eigenen Krisenmanagements betrachtet und in diesem Baustein nur als Schnittstelle, z. B. im Rahmen der weiteren Eskalation von Notfällen behandelt. Weiterführende Informationen zu den einzelnen Phasen des Notfallmanagements sowie der Abgrenzung des Notfallmanagements zum Krisenmanagement sind im BSI-Standard 100-4 enthalten.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Notfallmanagement von besonderer Bedeutung:

### 2 1 Personalausfall

Wenn Mitarbeiter ausfallen, z. B. durch Keime in der Kantine, Pandemie, Tod oder Streik, könnte die eigene Institution ihre Fachaufgaben und Geschäftsprozesse nicht mehr ausführen und zudem könnten relevante Informationen zum Wiederanlauf des Geschäftsprozesses oder der IT-Systeme nicht mehr zugänglich sein. Vielfach besitzen einzelne Personen spezifisches Fachwissen (Kopfmonopole), sodass ein Schaden auch dann eintreten kann, wenn der Personalausfall zahlenmäßig nur sehr gering ist.

### 2 2 Ausfall von IT-Systemen

Wenn Komponenten eines IT-Systems ausfallen, z. B. durch defekte Hardware oder Stromausfall, kann der gesamte IT-Betrieb gestört werden. Dadurch ist die Verfügbarkeit der jeweiligen Informationen und damit auch des jeweiligen Geschäftsprozesses gefährdet. Zudem können wichtige Informationen, die für Wiederanlaufmaßnahmen benötigt werden, nicht zur Verfügung stehen. 

### 2 3 Ausfall eines Weitverkehrsnetzes (WAN)

Die Ursachen für den Ausfall eines Weitverkehrsnetzes (Wide Area Network, WAN) können vielfältig sein. Daher ist es möglich, dass sich ein Netzausfall lediglich auf einzelne Benutzer, einen Anbieter oder eine bestimmte Region auswirkt. Häufig stören solche Ausfälle nur kurz und betreffen dann nur die Geschäftsprozesse und Fachaufgaben, die eine entsprechend hohe Verfügbarkeit des WAN benötigen. Es gibt aber auch immer wieder längere Ausfälle, die massive Probleme in der Kommunikation und Erreichbarkeit nach sich ziehen können.

### 2 4 Ausfall eines Gebäudes

Gebäude können unvorhergesehen unbenutzbar werden, z. B. weil sie durch Feuer, Sturm, Hochwasser, Erdbeben oder eine Explosion teilweise oder vollständig zerstört wurden. Ein Ausfall eines Gebäudes kann jedoch auch dadurch verursacht werden, dass wegen Sperrungen von Polizei oder Feuerwehr das Umfeld nicht mehr betreten werden kann oder das Gebäude verlassen werden muss, weil Strom, Wasser, Abwasser, Heizung oder Klimatisierung über einen gewissen Zeitraum nicht mehr funktionieren.

### 2 5 Ausfall eines Lieferanten oder Dienstleisters

Wenn Organisationseinheiten von Dienstleistern abhängig sind, kann sich der teilweise oder vollständige Ausfall eines Outsourcing-Dienstleisters oder eines Lieferanten erheblich auf die betriebliche Kontinuität auswirken, insbesondere bei kritischen Geschäftsprozessen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Notfallmanagement aufgeführt. Grundsätzlich ist der Notfallbeauftragte für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Notfallmanagement. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.4.A1 Erstellung eines Notfallhandbuchs [Informationssicherheitsbeauftragter (ISB)]

Es SOLLTE ein Notfallhandbuch erstellt werden, in dem die wichtigsten Informationen zu

* Rollen, 
* Sofortmaßnahmen, 
* Alarmierung und Eskalation, 
* Kommunikations-, grundsätzliche Geschäftsfortführungs-, Wiederanlauf und 
* Wiederherstellungspläne 
enthalten sind. Zuständigkeiten und Befugnisse SOLLTEN zugewiesen, kommuniziert und im Notfallhandbuch festgehalten werden. Es SOLLTE sichergestellt sein, dass im Notfall entsprechend geschultes Personal zur Verfügung steht. Es SOLLTE regelmäßig durch Tests und Übungen überprüft werden, ob die im Notfallhandbuch beschriebenen Maßnahmen auch wie Vorgesehen funktionieren.

Das Notfallhandbuch SOLLTE regelmäßig geprüft und, falls erforderlich, aktualisiert werden. Es SOLLTE auch im Notfall zugänglich sein. Ergänzt werden SOLLTE das Notfallhandbuch um Verhaltensregeln für Fälle (z. B. Brand), die allen Mitarbeitern bekannt gegeben werden sollten. 

#### DER.4.A2 Integration von Notfallmanagement in organisationsweite Abläufe und Prozesse [Institutionsleitung]

Die Prozesse im Sicherheitsmanagement SOLLTEN mit dem Notfallmanagement (siehe DER.2.1 *Behandlung von Sicherheitsvorfällen*) abgestimmt werden. 

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.4.A3 Festlegung des Geltungsbereichs und der Notfallmanagementstrategie [Institutionsleitung](CIA)

Der Geltungsbereich für das Notfallmanagement-System SOLLTE eindeutig festgelegt werden. Die Institutionsleitung SOLLTE eine Notfallmanagement-Strategie festlegen, die die angestrebten Ziele und das Risikoakzeptanzniveau darlegen.

#### DER.4.A4 Leitlinie zum Notfallmanagement und Übernahme der Gesamtverantwortung durch die Leitungsebene [Institutionsleitung](CIA)

Es SOLLTE eine Leitlinie zum Notfallmanagement von der Leitungsebene verabschiedet werden. Diese SOLLTE die wesentlichen Eckpunkte des Notfallmanagements enthalten. Die Leitlinie zum Notfallmanagement SOLLTE regelmäßig überprüft und gegebenenfalls überarbeitet werden. Die Leitlinie zum Notfallmanagement SOLLTE allen Mitarbeitern bekannt gegeben werden.

#### DER.4.A5 Aufbau einer geeigneten Organisationsstruktur für das Notfallmanagement [Institutionsleitung](CIA)

Es SOLLTEN die Rollen für das Notfallmanagement den Gegebenheiten der Institution angemessen festgelegt werden. Dies SOLLTE mit den Aufgaben, Pflichten und Kompetenzen der Rollen schriftlich dokumentiert werden. Es SOLLTEN für alle Rollen im Notfallmanagement qualifizierte Mitarbeiter benannt werden. Die Organisationsstruktur im Notfallmanagement SOLLTE regelmäßig darauf überprüft werden, ob sie praxistauglich, effektiv und effizient ist.

#### DER.4.A6 Bereitstellung angemessener Ressourcen für das Notfallmanagement [Institutionsleitung](CIA)

Die finanziellen, technischen und personellen Ressourcen für die angestrebten Ziele des Notfallmanagements SOLLTEN angemessen sein. Der Notfallbeauftragte bzw. das Notfallmanagement-Team SOLLTE über genügend Zeit für die Aufgaben im Notfallmanagement verfügen.

#### DER.4.A7 Erstellung eines Notfallkonzepts [Institutionsleitung](CIA)

Alle kritischen Geschäftsprozesse und Ressourcen SOLLTEN identifiziert werden (beispielsweise mit einer Business Impact Analyse (BIA)). Es SOLLTEN die wichtigsten, relevanten Risiken für die kritischen Geschäftsprozesse und Ressourcen identifiziert werden. Für jedes identifizierte Risiko SOLLTE entscheiden werden, welche Risikostrategien zur Risikobehandlung eingesetzt werden sollen. Es SOLLTEN Kontinuitätsstrategien entwickelt werden, die einen Wiederanlauf und eine Wiederherstellung der kritischen Geschäftsprozesse in der geforderten Zeit ermöglichen. Ein Notfallkonzept SOLLTE erstellt werden. Notfallpläne und Maßnahmen SOLLTEN entwickelt und implementiert werden, die eine effektive Notfallbewältigung und eine schnelle Wiederaufnahme der kritischen Geschäftsprozesse ermöglichen. Im Notfallkonzept SOLLTE die Informationssicherheit berücksichtigt und entsprechende Sicherheitskonzepte für die Notfalllösungen entwickelt werden.

#### DER.4.A8 Integration der Mitarbeiter in den Notfallmanagement-Prozess [Vorgesetzte, Leiter Personal](CIA)

Alle Mitarbeiter SOLLTEN regelmäßig für das Thema Notfallmanagement sensibilisiert werden. Zum Notfallmanagement SOLLTE es ein Schulungs- und Sensibilisierungskonzept geben. Die Mitarbeiter im Notfallmanagement-Team SOLLTEN regelmäßig entsprechend der benötigten Kompetenzen geschult werden.

#### DER.4.A9 Integration von Notfallmanagement in organisationsweite Abläufe und Prozesse [Institutionsleitung](CIA)

Es SOLLTE sichergestellt werden, dass Aspekte des Notfallmanagements in allen Geschäftsprozessen der Institution berücksichtigt werden. Die Prozesse, Vorgaben und Verantwortlichkeiten im Notfallmanagement SOLLTEN mit dem Risikomanagement und Krisenmanagement abgestimmt werden. 

#### DER.4.A10 Tests und Notfallübungen [Institutionsleitung](CIA)

Es SOLLTE eine Übungsplanung erstellt werden, sodass alle wesentlichen Pläne und Maßnahmen des Notfallmanagements regelmäßig und anlassbezogen getestet und geübt werden. Im Notfallmanagement SOLLTEN ausreichend Ressourcen für die Planung, Konzeption, Durchführung und Auswertung der Tests und Übungen bereitgestellt werden.

#### DER.4.A11 Überprüfung und Aufrechterhaltung der Maßnahmen zur Notfallvorsorge und -reaktion(CIA)

Es SOLLTEN die identifizierten Maßnahmen zur Notfallvorsorge und -reaktion regelmäßig und anlassbezogen überprüft werden. Die Überprüfungen SOLLTEN so geplant werden, dass kein relevanter Teil ausgelassen wird. Die Ergebnisse der Überprüfungen SOLLTEN ausgewertet und gegebenenfalls in Korrekturmaßnahmen umgesetzt werden. Die Korrekturmaßnahmen SOLLTEN geplant und die Umsetzung kontrolliert werden.

#### DER.4.A12 Dokumentation im Notfallmanagement-Prozess(CIA)

Der Ablauf des Notfallmanagement-Prozesses, die Arbeitsergebnisse der einzelnen Phasen und wichtige Entscheidungen SOLLTEN dokumentiert werden. Es SOLLTE ein Verfahren etabliert werden, das gewährleistet, dass regelmäßige Dokumente aktualisiert werden. Hierüber hinaus SOLLTE der Zugriff auf die Dokumentation nur auf autorisierte Personen eingeschränkt werden.

#### DER.4.A13 Überprüfung und Steuerung des Notfallmanagement-Systems [Institutionsleitung](CIA)

Die Leitungsebene SOLLTE ihre Aufgabe, das Notfallmanagement-System regelmäßig zu überprüfen, zu bewerten und gegebenenfalls zu korrigieren, wahrnehmen. Die Leitungsebene SOLLTE regelmäßig über den Stand des Notfallmanagements durch Management-Berichte informiert werden.

#### DER.4.A14 Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen [Institutionsleitung](IA)

Es SOLLTEN alle Notfallmaßnahmen regelmäßig oder bei größeren Änderungen daraufhin überprüft werden, ob sie noch eingehalten sowie korrekt umgesetzt werden und ob sie noch geeignet sind, die definierten Ziele zu erreichen.

Hierbei SOLLTE untersucht werden, ob technische Maßnahmen korrekt implementiert und konfiguriert wurden und ob organisatorische Maßnahmen effektiv und effizient umgesetzt sind. Bei Abweichungen SOLLTEN die Ursachen für Mängel ermittelt und Verbesserungsmaßnahmen veranlasst werden. Diese Ergebnisübersicht SOLLTE durch die Leitungsebene freigegeben werden. Es SOLLTE zudem ein Prozess initiiert werden, der steuert und überwacht, ob und wie die Verbesserungsmaßnahmen umgesetzt werden. Bei Verzug SOLLTE dies frühzeitig an die Leitungsebene eskaliert werden.

Es SOLLTE in der Institutionsleitung festgelegt sein, wie die Überprüfungstätigkeiten koordiniert werden. Insbesondere SOLLTEN die im Bereich der Revision, der IT, des Sicherheitsmanagements, des Informationssicherheitsmanagements und des Notfallmanagements durchgeführten Überprüfungen miteinander koordiniert werden. Dazu SOLLTE geregelt werden, welche Maßnahmen wann und von wem überprüft werden.

#### DER.4.A15 Bewertung der Leistungsfähigkeit des Notfallmanagement-Systems [Institutionsleitung](IA)

Es SOLLTE regelmäßig bewertet werden, wie leistungsfähig und effektiv das Notfallmanagement-System ist. Als Grundlage SOLLTEN Mess- und Bewertungskriterien, wie z. B. Leistungskennzahlen (engl.: Key Performance Indicators) definiert werden. Diese Messgrößen SOLLTEN regelmäßig ermittelt und mit den Vorjahreswerten verglichen werden. Weichen die Werte negativ ab, SOLLTEN die Ursachen ermittelt und Verbesserungsmaßnahmen definiert werden. Die Ergebnisse der Bewertung SOLLTEN an die Leitung berichtet werden.

Die Leitung SOLLTE entscheiden, mit welchen Maßnahmen das Notfallmanagement weiterentwickelt werden soll. Alle Entscheidungen der Leitungsebene SOLLTEN dokumentiert und die bisherigen Aufzeichnungen aktualisiert werden.

#### DER.4.A16 Notfallvorsorge- und Notfallreaktionsplanung für ausgelagerte Komponenten [Institutionsleitung](IA)

Bei der Notfallvorsorge- und Notfallreaktionsplanung für ausgelagerte Komponenten SOLLTE in den unterzeichneten Verträgen das Notfallmanagement des Lieferanten oder Dienstleisters geprüft werden. Diese Prüfung SOLLTE regelmäßig ein Verantwortlicher der Institutionsleitung durchführen. Auch SOLLTEN die Abläufe in Notfalltests und -übungen mit dem Lieferanten oder Outsourcing-Dienstleister abgestimmt und ggf. gemeinsam durchgeführt werden.

Die Ergebnisse und Auswertungen SOLLTEN regelmäßig zwischen der Institutionsleitung und dem Lieferanten oder Dienstleister ausgetauscht werden. Darin SOLLTEN auch eventuelle Verbesserungsmaßnahmen enthalten sein. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Notfallmanagement" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [22301] ISO 22301:2012

  

 Scietal security - Business continuity management systems - Requirements, ISO, 2012   
 <https://www.iso.org/standard/50038.html>

 
* #### [27001A17] ISO/IEC 27001:2013 - Annex A.17 Information security aspects of buisiness continuity management

  

 Information technology - Security techniques - Information security management systems - Requirements, insbesonder A.17 Information security aspects of business continuity management, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [27031] ISO/IEC 27031:2011

  

 Information technology - Security techniques - Guidelines for information and communications technology readiness for business continuity, 02.2011  
 <https://www.iso.org/standard/44374.html>

 
* #### [BSI3] Risikoanalyse auf der Basis IT-Grundschutz, BSI-Standard 200-3

  

 BSI, 2017  
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/IT-Grundschutz-Modernisierung/GS\_Standards/gs\_standards\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/IT-Grundschutz-Modernisierung/GS_Standards/gs_standards_node.html)

 
* #### [BSI4] Notfallmanagement, BSI-Standard 100-4

  

 BSI, (zuletzt aubgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard04/ITGStandard04\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard04/ITGStandard04_node.html)

 
* #### [BWV] Bericht des bundesbeauftragten für die Wirtschaftlichkeit in der Verwaltung

  

 Modell eines Risikomanagements für die Bundesverwaltung, Bundesrechnungshof, 04.2017  
 <https://www.bundesrechnungshof.de/de/veroeffentlichungen/gutachten-berichte-bwv/berichte/sammlung/2017-bwv-bericht-modell-eines-risikomanagements-fuer-die-bundesverwaltung>

 
* #### [ISFBC] The Standard of Good Practice- Area BC Business Continuity

  

 ISF, insbesonder Area BC Business Continuity, Juni 2016

 
* #### [LFKK] Krisenkommunikation - Leitfaden für Behörden und Unternehmen

  

 BMI, 2014   
 <https://www.bmi.bund.de/SharedDocs/Downloads/DE/Broschueren/2014/leitfaden-krisenkommunikation.pdf>

 
* #### [LFKRITIS] Schutz kritischer Infrastrukturen - Risiko- und Krisenmanagement (Leitfaden für Unternehmen und Behörden)

  

 BMI, 05.2011  
 [https://www.bmi.bund.de/SharedDocs/Downloads/DE/Broschueren/2011/leitfaden\_schutz-kritischer-infrastrukturn.pdf](https://www.bmi.bund.de/SharedDocs/Downloads/DE/Broschueren/2011/leitfaden_schutz-kritischer-infrastrukturn.pdf)

 
* #### [NIST80034] NIST Special Publication 800-34

  

 Contingency Planning Guide for Federal Information Systems, Revision 1, 05.2010  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf>

 
* #### [UMRA] Umsetzungsrahmenwerk zum Notfallmanagement nach BSI-Standard 100-4

  

 BSI, (zuletzt aufgerufen am 28.09.2017)  
 <https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Umsetzungsrahmenwerk/umra.html>

 
* #### [WKN] Webkurs Notfallmanagement nach BSI-Standard 100-4

  

 BSI, (zuletzt aufgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/Webkurs1004/0\_Startseite/nfm00\_Start.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/Webkurs1004/0_Startseite/nfm00_Start.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Notfallmanagement" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.27 Ressourcenmangel
* G 0.33 Personalausfall
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

