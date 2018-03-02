1 Beschreibung
--------------

### 1.1 Einleitung

Als Fachanwendungen werden komplexe Anwendungen bezeichnet, die für individuelle und spezifische fachliche Aufgaben konzipiert sind sowie in der Regel nicht als Standardlösungen gekauft und eingesetzt werden. Stattdessen werden Basislösungen für den individuellen Einsatzzweck von Institutionen angepasst, oder die Anwendungen werden vollständig durch Dritte oder der Institution selbst entwickelt. Zu diesen Fachanwendungen gehören beispielsweise Personalverwaltungssoftware, Verfahren zur Verwaltung von Sozialdaten oder Meldedaten. Eine sorgfältige Planung von Sicherheitsmaßnahmen vor Auswahl und Inbetriebnahme einer Anwendung ist wesentlich für das erreichte Sicherheitsniveau, da Fehler in der Planung wie z. B. fehlende Sicherheitsfunktionen im laufenden Betrieb nicht oder nur mit hohen Zusatzaufwänden ausgeglichen werden können.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, aufzuzeigen, welche grundlegenden Sicherheitsanforderungen bei Planung, Beschaffung, Inbetriebnahme, regulärem Betrieb und Außerbetriebnahme einer Fachanwendung zu berücksichtigen sind. 

### 1.3 Abgrenzung

Der Fokus dieses Bausteins liegt auf organisatorischen und konzeptionellen Aspekten der Informationssicherheit von Fachanwendungen. Auswahl, Konfiguration und sicherer Betrieb von Sicherheitsfunktionen in Anwendungen sind in diesem Baustein nur allgemein und grundlegend beschrieben. Eine konkrete Beschreibung für breit genutzte Standardanwendungen findet sich in den weiteren Bausteinen der Schicht APP *Anwendungen* sowie im Baustein CON.4 *Auswahl und Einsatz von Standardsoftware*. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Fachanwendungen von besonderer Bedeutung:

### 2 1 Verlust der Vertraulichkeit oder Integrität in Fachanwendungen

Mit Fachanwendungen werden in der Regel vertrauliche Informationen verarbeitet, wie beispielsweise alle Arten von personenbezogenen Daten oder Geschäftsgeheimnisse. Werden diese Daten offengelegt oder ungewollt geändert, können hieraus Vertrags- oder Rechtsverstöße (einschließlich Datenschutzrechtsverstöße) resultieren. Insbesondere bei einem Verlust der Integrität können Rechtsverstöße durch Prozess- oder Verfahrensfehler entstehen. Wenn die Informationen nicht mehr verfügbar sind, können so Geschäfts- oder Fachaufgaben nicht mehr erfüllt werden. Der Verlust der Vertraulichkeit, Integrität und Verfügbarkeit kann so erhebliche Folgen haben, wie z. B. strafrechtlichen und finanziellen Konsequenzen, oder in Einzelfällen sogar Personenschäden. 

### 2 2 Ungeeignete Verwaltung von Zugangs- und Zugriffsrechten

Wenn die Vergabe von Zutritts- und Zugriffsrechten schlecht geregelt ist, führt das schnell zu gravierenden Sicherheitslücken, z. B. durch Wildwuchs in der Rechtevergabe. Dies führt schnell dazu, dass Benutzer Berechtigungen auf Zuruf erhalten oder umgekehrt nur über unnötig komplizierte Wege an diese kommen. Dadurch können einerseits fehlende Berechtigungen die tägliche Arbeit behindern, andererseits können so Berechtigungen ohne Erfordernis vergeben werden und so ein Sicherheitsrisiko darstellen.

### 2 3 Unzugängliche vertragliche Regelungen mit einem externen Dienstleister

Aufgrund von unzulänglichen vertraglichen Regelungen mit einem externen Dienstleister, insbesondere bei der Erstellung, Unterstützung der Einführung und Wartung der Anwendung, können vielfältige und auch schwerwiegende Sicherheitsprobleme auftreten. Wenn Aufgaben, Leistungsparameter oder Aufwände ungenügend oder missverständlich beschrieben wurden, kann die Folge sein, dass aus Unkenntnis, aufgrund fehlender Qualifizierung oder wegen fehlender Ressourcen Sicherheitsmaßnahmen nicht umgesetzt werden. Dies kann eine Vielzahl negativer Auswirkungen nach sich ziehen, wie die Nichterfüllung regulatorischer Anforderungen und Pflichten, die fehlende Einhaltung von Auskunftspflichten und Gesetzen bis hin zur fehlenden Übernahme von Verantwortung aufgrund des Verlusts von Kontroll- und Steuerungsmöglichkeiten.

### 2 4 Software-Konzeptionsfehler

Bei der Planung von Anwendungen, Programmen und Protokollen können sicherheitsrelevante Konzeptionsfehler entstehen. Diese ergeben sich häufig daraus, dass für einen bestimmten Zweck vorgesehene Anwendungsmodule und Protokolle in anderen Einsatzszenarien wiederverwendet werden. Wenn hier andere Sicherheitsvorgaben relevant sind, also beispielsweise für abgeschottete betriebliche Umgebungen vorgesehene Anwendungsmodule und Protokolle ans Internet angebunden werden, kann dies zu massiven Sicherheitslücken führen. 

### 2 5 Software-Schwachstellen

Bei Software-Schwachstellen handelt es sich um Fehler, die ein Sicherheitsrisiko für die mit der Anwendung verarbeiteten Daten darstellen. Diese Sicherheitsrisiken ergeben sich daraus, dass vorgesehene Sicherheitsmechanismen unwirksam sind oder es durch technischen Fortschritt werden, oder wenn dadurch Sicherheitsmechanismen gezielt umgangen werden können. Darüber hinaus können Softwarefehler auch zu mangelhafter Verarbeitungsleistung (Performance-Mängel) oder dem Ausfall der Anwendung führen. Mögliche Folgen eines Ausfalls sind Arbeitsausfall, Umsatzverluste oder Verstöße gegen vertragliche Vereinbarungen oder rechtliche Vorgaben.

### 2 6 Undokumentierte Funktionen

Viele Anwendungen enthalten häufig für Entwicklungs- oder Supportzwecke durch den Hersteller eingebaute undokumentierte Funktionen. Diese sind meistens den Benutzern nicht bekannt. Undokumentierte Funktionen sind dann problematisch, wenn sie das Umgehen wesentlicher Sicherheitsmechanismen, wie z. B. solcher zum Zugriffsschutz, erlauben. Dies kann die Vertraulichkeit und Integrität der verarbeiteten Daten erheblich beeinträchtigen.

### 2 7 Fehlende oder unzureichende Sicherheitsmaßnamen in Anwendungen

Sicherheitsmechanismen oder Sicherheitsfunktionen sollen in der Anwendung sicherstellen, dass bei der Verarbeitung von Informationen Vertraulichkeit, Integrität und Verfügbarkeit im benötigten Maße gewährleistet werden können. Häufig steht bei der Entwicklung einer Anwendung aber die fachliche Funktionalität oder der Zeit- und Kostenrahmen im Vordergrund, so dass wichtige Sicherheitsmechanismen zu schwach ausgeprägt sind, sodass sie einfach umgangen werden können, oder sogar ganz fehlen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen an Planung, Auswahl, Beschaffung, Inbetriebnahme, Betrieb und Aussonderung von Fachanwendungen aufgeführt. Grundsätzlich ist der die Anwendung einsetzende Fachbereich für die Erfüllung dieser Anforderungen zuständig. In der Praxis können diese Anforderungen nur erfüllt werden, wenn die IT-Betriebsverantwortlichen (z. B. IT-Leiter) und der Informationssicherheitsbeauftragten (ISB) hinzugezogen bzw. beteiligt werden. 

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### CON.5.A1 Festlegung benötigter Sicherheitsfunktionen der Fachanwendung [IT-Betrieb]

Für die Fachanwendung MÜSSEN die notwendigen Sicherheitsfunkionen bei der fachlichen Auswahl und der Integration in die IT-betrieblichen Infrastrukturen und Betriebsprozesse berücksichtigt werden. Die Auswahl und Umsetzung geeigneter Sicherheitsfunktionen in der Fachanwendung MUSS auf Grundlage der Daten, die in der Anwendung verarbeitet werden, und gegebenenfalls einer ergänzenden Risikoanalyse, erfolgen. Die Sicherheitsfunkionen MÜSSEN geeignet dokumentiert werden.

#### CON.5.A2 Test und Freigabe von Fachanwendungen [Leiter IT, Datenschutzbeauftragter]

Für einen geordneten Betriebsübergang einer Anwendung sowie bei wesentlichen Änderungen MUSS ein geeignetes Vorgehen bei Test und Freigabe entwickelt werden. Dabei MÜSSEN berücksichtigt werden:

* die fachliche Ebene (Vertreten durch die Fachverantwortlichen),
* die Ebene des IT-Betriebes (Vertreten durch den IT-Leiter),
* die Ebene der Informationssicherheit (Vertreten durch den Informationssicherheitsbeauftragten),
* die Ebene des Datenschutzes (Vertreten durch den Datenschutzbeauftragten) sowie
* je nach Art und Komplexität einer Anwendung weitere Funktionsträger wie z.B. die Personalvertretung.
#### CON.5.A3 Sichere Installation einer Fachanwendung [IT-Betrieb]

Es MUSS eine Installationsanweisung erstellt werden, die alle benötigten Anwendungsmodule (Bibliotheken), die Installationsreihenfolge und die Konfiguration der Anwendungsmodule beinhaltet. Die Installationsanweisung SOLLTE die notwendigen Aspekte bezüglich der Installationsumgebung berücksichtigen. Die Fachanwendung MUSS gemäß der Installationsanweisung installiert werden.

Bei Änderungen in der Anwendung und funktionalen Updates MUSS die Installationsanweisung aktualisiert werden.

#### CON.5.A4 Heranführen von Nutzerinnen und Nutzern an die Anwendung

Benutzer und Administratoren MÜSSEN an die korrekte Nutzung und Administration der Anwendung einschließlich der Sicherheitsfunktionen herangeführt werden. Hierzu SOLLTEN Richtlinien und Arbeitsanweisungen zur Nutzung und Administration der Anwendung, Schulungen und Einweisungen, Handbücher und Online-Hilfen sowie eine Benutzerunterstützung durch Schlüsselanwender angeboten werden.

#### CON.5.A5 Sicherer Betrieb einer Fachanwendung [IT-Betrieb]

Berechtigungen zur Nutzung und Administration einer Fachanwendung MÜSSEN korrekt vergeben und regelmäßig auf Korrektheit hin überprüft werden. Nicht mehr benötigte Berechtigungen MÜSSEN wieder entzogen werden.

Es MUSS sichergestellt werden, dass Protokolldaten regelmäßig ausgewertet und gesetzlich vorgegebene Speicherfristen für Protokolldaten eingehalten werden.

Sicherheitskritische Patches und Updates MÜSSEN durch den Hersteller der Anwendung auf Grundlage geeigneter vertraglicher Vereinbarungen bereitgestellt und zeitnah eingespielt werden. Dabei MUSS sichergestellt werden, dass Patches und Updates zuvor geeignet getestet und freigegeben wurden.

Es MÜSSEN regelmäßig Datensicherungen und Rücksicherungsübungen durchgeführt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Entwicklung und Einsatz von Fachanwendungen. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### CON.5.A6 Umfassende Dokumentation der Anforderungen an die Anwendung

Die e relevanten Anforderungen an die Anwendung SOLLTEN dokumentiert werden. Diese Dokumentation SOLLTE bei Änderungen an der Anwendung sowie funktionalen Updates fortgeschrieben werden.

#### CON.5.A7 Erstellung eines Mandantenkonzeptes [Leiter IT]

Es SOLLTE mit einem Mandantenkonzept sichergestellt werden, dass Anwendungen und Daten verschiedener Kunden sauber getrennt betrieben werden. Dieses SOLLTE durch den Betreiber der mandantenfähigen Anwendung erstellt und den nutzenden Institutionen zur Verfügung gestellt werden. Die benötigten Mechanismen zur Mandantentrennung beim Dienstleister SOLLTEN ausreichend umgesetzt sein. 

#### CON.5.A8 Geeignete Steuerung der Anwendungsentwicklung [Leiter IT]

Bei einer Entwicklung einer individuellen Anwendung SOLLTE ein geeignetes Steuerungs- und Projektmanagementmodell verwendet werden. Dabei SOLLTEN insbesondere die benötigten Qualifikationen beim Personal, die Abdeckung aller relevanten Phasen während des Lebenszyklus der Software, ein geeignetes Entwicklungsmodell, Risikomanagement und Qualitätsziele berücksichtigt werden.

#### CON.5.A9 Außerbetriebnahme von Anwendungen [Leiter IT]

Die Außerbetriebnahme von Anwendungen SOLLTE geplant werden. Es SOLLTE für alle Daten geklärt sein, welche Daten migriert, archiviert oder gelöscht werden. Nicht mehr benötigte Daten SOLLTEN sicher gelöscht werden. Die Außerbetriebnahme von Anwendungen sowie der zugehörigen IT-Systeme und Datenträger SOLLTE nachvollziehbar dokumentiert werden.

#### CON.5.A10 Notfallvorsorge für Anwendungen [Leiter IT]

Die Fachanwendungen SOLLTEN in die Planung zur Notfallvorsorge aufgenommen werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.5.A11 Geeignete und rechtskonforme Beschaffung

Bei der Beschaffung einer Fachanwendung SOLLTEN die bestehenden rechtlichen und organisatorischen Vorgaben umgesetzt werden. Werden bei der Beschaffung, Entwicklung oder dem Betrieb einer Anwendung Dienstleister einbezogen, SOLLTEN in den Verträgen die relevanten Sicherheitsaspekte berücksichtigt werden.

In der Institution SOLLTEN definierte Prozesse und festgelegte Ansprechpartner existieren, die die Berücksichtigung der jeweiligen Rahmenbedingungen sicherstellen. Es SOLLTE geklärt werden, welche Rolle Zertifizierungen bei der Vergabeentscheidung spielen.

#### CON.5.A12 Treuhänderische Hinterlegung

Für geschäftskritische Anwendungen SOLLTE geprüft werden, ob es notwendig ist, diese gegen Ausfall des Herstellers der Anwendung abzusichern. Dabei SOLLTE die treuhänderische Hinterlegung von nicht zum Lieferumfang der Anwendung gehörenden Materialien bei einer Escrow-Agentur erwogen werden, wie z. B. dokumentiertem Code, Konstruktionspläne, Schlüssel, Passwörter. In diesem Falle SOLLTEN die Pflichten der Escrow-Agentur bei der Lagerung und Herausgabe (wann darf das Hinterlegungsgut an wen herausgegeben werden?) vertraglich geregelt werden.

#### CON.5.A13 Entwicklung eines Redundanzkonzeptes für Anwendungen [Leiter IT]

Besteht hinsichtlich der Verfügbarkeit einer Anwendung ein hoher oder sehr hoher Schutzbedarf, so SOLLTE ein Redundanzkonzept erstellt werden. Dieses SOLLTE folgende Aspekte beinhalten:

* Planung eines eingeschränkten IT-Betriebs sowie der Wiederherstellung im Notfall (Notfallvorsorgekonzeption)
* Redundanz auf Anwendungsebene mittels Loadbalancing oder Anwendungsclustern / Cloud-Services
* Möglichkeiten zum Schwenken der Anwendungen auf andere Systeme 
Ergänzend SOLLTE sichergestellt werden, dass das Redundanzkonzept auch die für den Anwendungsbetrieb benötigten Gebäude und Räume, Systeme und Kommunikationsverbindungen einbezieht. Das Redundanzkonzept SOLLTE mit dem Notfallkonzept abgestimmt sein. Die Maßnahmen aus dem Redundanzkonzept SOLLTEN regelmäßig getestet und geübt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Entwicklung und Einsatz von Fachanwendungen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [12207] ISO/IEC 12207

  

 Systems and software engineering - Software life cycle processes, ISO, 02.2008  
 <https://www.iso.org/standard/43447.html>

 
* #### [15408] Common Criteria for Information Technology Security Evaluation (ISO 15408)

  

 Insbesondere Teil 2 "Security functional requirements", Common Criteria, 09.2012  
 <https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R4.pdf>

 
* #### [27001A14] ISO/IEC 27001: 2013 - Annex A.14 System Acquisition

  

 Information technology - Security technigues - Information security management systems - Requirements, insbesonder Annex A, A.14 Sytem Acquisition, development and maintenance, ISO, 04.2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>  
 

 
* #### [ISFBA] The Standard of Good Practice - Area BA - Business Application Management

  

 insbesonder Area BA - Business Application Management, Information Security Forum (ISF), 06.2016

 
* #### [NIST80053F145] NIST Special Publication 800-53 - REVISION 4 - APPENDIX PAGE F-145

  

 Revision 4, Security and Privacy Controls for Federal Information Systems and Organizations, insbesondere APPENDIX F-PS PAGE F-145, FAMILY: SYSTEM AND SERVICES ACQUISITION, FAMILY: SYSTEM AND COMMUNICATIONS PROTECTION and FAMILY: SYSTEM AND INFORMATION INTEGRITY, NIST, 2015  
 <http://nvlpubs.nist.gov/GGTSPU-fw1.bsi.bund.de-8690-598708-um44WKCwoM5r2JP4-LOD/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Entwicklung und Einsatz von Fachanwendungen" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

