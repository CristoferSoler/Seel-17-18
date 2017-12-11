1 Beschreibung
--------------

### 1.1 Einleitung

Unter Standardsoftware wird Software verstanden, die auf dem Markt angeboten und meistens über den Fachhandel bezogen wird, zum Beispiel über Kataloge oder Onlineportale. Sie zeichnet sich dadurch aus, dass Institutionen sie selbst installieren und mit wenig Aufwand anpassen können.

In diesem Baustein wird dargestellt, wie Institutionen unter Sicherheitsgesichtspunkten mit Standardsoftware umgehen sollten. So müssen Institution einen Anforderungskatalog für Standardsoftware erstellen, ein geeignetes Produkt auswählen, es sicher installieren, die Lizenzen geeignet verwalten und das Produkt auch wieder sicher deinstallieren können.

### 1.2 Zielsetzung

Der Baustein zeigt systematisch auf, welche Schutzmaßnahmen zu ergreifen sind, damit Standardsoftware auf sichere Art geplant, beschafft, betrieben und ausgesondert werden kann. Übergeordnetes Ziel ist dabei, die mit der Standardsoftware verarbeiteten Informationen zu schützen. 

### 1.3 Abgrenzung

Dieser Baustein befasst sich ausschließlich mit standardisierten Programmen, die so konzipiert sind, dass sie vom Anwender selbstständig ohne Unterstützung durch den Hersteller oder externe Dienstleister eingesetzt und angepasst werden können. 

Der vorliegende Baustein geht nicht auf Software-Tests und -Freigaben ein. Anforderungen dazu sind in* *OPS.1.1.6* Software-Tests und -Freigaben* aufgeführt. Auch die Softwareentwicklung wird nicht thematisiert. Dazu sollten die Anforderungen des Bausteins CON.4* Softwareentwicklung *gesondert berücksichtigt werden*.* 

Angaben zur Aussonderung werden vertiefend im Baustein *OPS.1.2.7 Verkauf/Aussonderung von IT* betrachtet. Weiterführende Anforderungen an Cloud-Anwendungen sind in den Bausteinen OPS.2.2 *Cloud-Nutzung *und* *APP.5.3 *Cloud-Anwendungen aus Client-Sicht *geregelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich *Standardsoftware* von besonderer Bedeutung:

### 2 1 Fehlende Anpassung der Standardsoftware an den Bedarf der Institution

Wenn eingekaufte Standardsoftware nicht an die Anforderungen der Institution angepasst wird, kann der interne Betrieb erheblich gestört werden. Formate könnten z. B. nicht mit bereits eingesetzten Programmen kompatibel sein oder neue Produkt könnten einen zu geringen Funktionsumfang haben. Das kann zu Leistungsverlusten, Störungen oder Fehlern innerhalb der Geschäftsprozesse führen.

### 2 2 Offenlegung schützenswerter Informationen durch fehlerhafte Konfiguration

Ist eine Standardsoftware fehlerhaft konfiguriert, z. B. wenn nicht benötigte Funktionen noch aktiviert sind, können unbeabsichtigt schützenswerte Informationen offengelegt werden. Das kann zu finanziellen Einbußen oder Reputationsschäden führen. Zusätzlich könnte die Institution auch gegen geltendes Recht verstoßen, z. B. wenn personenbezogene Daten offengelegt werden. 

### 2 3 Bezug von Standardsoftware und Updates aus unzuverlässiger Quelle

Werden Standardsoftware oder zugehörige Updates aus unzuverlässigen Quellen bezogen, kann die Integrität und Funktionalität der Software nicht sichergestellt werden. Dies gilt auch für Erweiterungen (*Plug-ins* oder *Add-ons*). Die Installation kompromittierter Software kann dazu führen, dass Schadcode in der Institution verteilt wird und dass die Software nicht wie vorgesehen funktioniert. Darüber hinaus kann die Integrität und Verfügbarkeit von IT-Systemen beeinträchtigt werden.

### 2 4 Manipulation von Daten durch Benutzer

Die in Standardsoftware verwendeten Daten können auf vielfältige Weise durch Benutzer manipuliert werden, z. B. wenn sie Daten fehlerhaft oder vorsätzlich falsch erfassen, inhaltlich verändern oder einfach löschen. Dadurch sind alle Fachprozesse beeinträchtigt, in deren Rahmen die entsprechende Anwendung eingesetzt wird. Werden die manipulierten Daten nicht erkannt, führt das zur Verarbeitung verfälschter Informationen. Darüber hinaus können Sicherheitslücken entstehen, die Angreifer ausnutzen können.

### 2 5 Software-Schwachstellen in Standardsoftware

Trotz intensiver Tests werden meist nicht alle Schwachstellen und Fehler in Standardsoftware entdeckt, bevor sie an die Kunden ausgeliefert wird. Werden diese nicht rechtzeitig erkannt, können daraus resultierende Abstürze oder Fehler zu weitreichenden Folgen führen. Darüber hinaus können Vertraulichkeit und Integrität der gespeicherten Daten und die Verfügbarkeit betroffener IT-Systeme beeinträchtigt werden. Durch Software-Schwachstellen bzw. -Fehler kann es außerdem zu schwerwiegenden Sicherheitslücken in Standardsoftware kommen. Diese können unter Umständen von Angreifern ausgenutzt werden, um Schadcode einzuschleusen.

### 2 6 Einsatz nicht-lizenzierter Standardsoftware

Wird Standardsoftware ohne gültige Software-Lizenz eingesetzt, weil beispielsweise das Lizenzvolumen unbemerkt überschritten wurde, kann das Vertragsstrafen zur Folge haben. Umgekehrt werden möglicherweise zu hohe Lizenzkosten entrichtet, wenn Standardsoftware an Arbeitsplätzen installiert ist, an denen sie nicht benötigt wird.

### 2 7 Unerlaubtes Ausüben von Rechten in Standardsoftware

Zutritts-, Zugangs- und Zugriffsrecht werden als organisatorische Maßnahmen eingesetzt, um Informationen, Geschäftsprozesse und IT-Systeme vor unbefugtem Zugriff zu schützen. Können unautorisierte Personen Standardsoftware oder bestimmte Funktionen benutzen, kann das die Vertraulichkeit und Integrität der Informationen gefährden, indem diese verändert, gelöscht oder unsachgemäß erstellt werden. Solche Sicherheitslücken entstehen beispielsweise durch fehlerhafte Rechtevergaben. Betroffene Geschäftsprozesse können korrumpiert werden, unbeabsichtigt fehlerhafte Informationen verarbeiten oder schützenswerte Informationen offenlegen.

### 2 8 Datenverlust durch fehlerhafte Nutzung von Standardsoftware

Durch falsch benutze Standardsoftware können Mitarbeiter Daten versehentlich löschen oder so verändern, dass diese unbrauchbar gemacht werden. Dadurch können ganze Geschäftsprozesse blockiert werden. Auch eine fehlerhafte Benutzung von Funktionen zur Verschlüsselung kann dazu führen, dass die Daten zwar noch vorhanden sind, aber nicht mehr entschlüsselt werden können. In diesem Fall können die Daten nicht mehr oder nur noch mit erhöhtem Aufwand wieder hergestellt werden, was zu einer zusätzlichen finanziellen Belastung der Institution führen kann.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von *Standardsoftware* aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### CON.4.A1 Sicherstellen der Integrität von Standardsoftware

Bei der Installation von Standardsoftware MUSS sichergestellt werden, dass es sich dabei um ein originales unverändertes Softwareprogramm handelt. Dazu MUSS es entweder von Originaldatenträgern oder von geprüften identischen Kopien des originalen Installationsprogramms installiert werden. Der Zugriff auf die Installationsroutinen MUSS auf berechtigte Mitarbeiter eingeschränkt werden. Die Originaldatenträger oder das Installationsprogramm MÜSSEN auf Schadsoftware überprüft werden. Von den Installationsdateien SOLLTEN Sicherungskopien angelegt und geprüft werden. 

#### CON.4.A2 Entwicklung der Installationsanweisung für Standardsoftware

Für die ausgewählte Standardsoftware MUSS eine Installationsanweisung erstellt werden. Auch MÜSSEN geeignete Parameter für die Konfiguration sowie organisatorische Rahmenbedingungen für die Installation der Software vorgegeben werden.

#### CON.4.A3 Sichere Installation und Konfiguration von Standardsoftware

Freigegebene Standardsoftware MUSS so installiert und konfiguriert werden, dass dabei die entsprechenden Installationsanweisungen (siehe CON.4.A2 *Entwicklung der Installationsanweisungen für Standardsoftware*) eingehalten werden. Wird von diesen Anweisungen abgewichen, MUSS das durch den Vorgesetzten genehmigt werden. Alle Installationen MÜSSEN vom IT-Betrieb durchgeführt werden. Dabei MUSS sichergestellt sein, dass lediglich die benötigten Programmfunktionen installiert werden. 

Die Software MUSS so konfiguriert werden, dass sie die Sicherheitsrichtlinien der Institution erfüllt. Nicht benötigte Dienste und Funktionen MÜSSEN deinstalliert werden. Falls dies nicht möglich ist, MÜSSEN sie abgeschaltet werden. Bevor und nachdem Standardsoftware installiert wurde, SOLLTEN von allen beteiligten IT-Systemen Datensicherungen durchgeführt werden. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Auswahl und Einsatz von Standardsoftware. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### CON.4.A4 Festlegung der Verantwortlichkeiten im Bereich Standardsoftware [Fachabteilung]

Für die Einführung einer Standardsoftware SOLLTEN Verantwortliche benannt werden. Dabei SOLLTE mindestens festgelegt werden, wer einen Anforderungskatalog erstellt, das Produkt auswählt, es testet und freigibt und wer letztlich für die Installation verantwortlich ist. Zusätzlich SOLLTE ein Einführungs- und Freigabeprozess definiert werden. Für den Betrieb von Standardsoftware SOLLTEN technische und fachliche Produktverantwortliche benannt werden.

#### CON.4.A5 Erstellung eines Anforderungskatalogs für Standardsoftware [Fachabteilung]

Vor der Beschaffung einer Standardsoftware SOLLTE ein Anforderungskatalog erstellt werden, der neben funktionalen auch Sicherheitsanforderungen umfasst. Dazu SOLLTEN auch die Programmanforderungen der Fach- und IT-Abteilungen erhoben werden. Der fertige Anforderungskatalog SOLLTE mit allen betroffenen Fachabteilungen abgestimmt werden.

#### CON.4.A6 Auswahl einer geeigneten Standardsoftware [Fachabteilung, Beschaffungsstelle]

Anhand des Anforderungskatalogs (siehe CON4.1.A5 *Erstellung eines Anforderungskatalogs für Standardsoftware*) SOLLTEN die am Markt erhältlichen Produkte gesichtet und mithilfe einer Bewertungsskala miteinander verglichen werden. Danach SOLLTE untersucht werden, ob die Produkte aus der engeren Wahl die Anforderungen der Institution auch wirklich erfüllen. Gibt es mehrere Produktalternativen, SOLLTEN auch zusätzliche Aufwände berücksichtigt werden, z. B. für Schulungen oder für die Migration. Letztlich SOLLTE die Beschaffungsstelle gemeinsam mit dem Leiter der anfordernden Fachabteilung und des IT-Betriebs anhand der Bewertungen und Testergebnisse ein geeignetes Softwareprodukt auswählen.

#### CON.4.A7 Überprüfung der Lieferung von Standardsoftware [Fachabteilung]

Es SOLLTE überprüft werden, ob neue Softwareprodukte vollständig und korrekt geliefert wurden. Dabei SOLLTE mindestens kontrolliert werden, ob die Lieferung bestellt wurde, für wen sie bestimmt ist und ob alle notwendigen Komponenten vorhanden sind. Auch reine Download-Software inklusive zugehöriger Lizenzdateien oder -schlüsseln SOLLTE entsprechend geprüft werden. Die Ergebnisse der Überprüfung SOLLTEN dokumentiert werden. Danach SOLLTEN alle gelieferten Produkte und Lizenzinformationen mit eindeutigen Identifizierungsmerkmalen versehen und in ein Bestandsverzeichnis übernommen werden.

#### CON.4.A8 Lizenzverwaltung und Versionskontrolle von Standardsoftware

Lizenzpflichtige Standardsoftware-Produkte, die auf IT-Systemen der Institution eingesetzt werden, SOLLTEN lizenziert sein. Um das sicherzustellen, SOLLTEN die installierten Programmversionen und die Lizenzen regelmäßig kontrolliert werden. Dafür SOLLTEN entsprechende Listen, Datenbanken oder spezielle Lizenzverwaltungsprogramme verwendet werden. Die Bestandslisten für die Lizenzen SOLLTEN immer auf dem aktuellen Stand sein. Darüber hinaus SOLLTEN die verschiedenen Konfigurationen der installierten Standardsoftware dokumentiert werden.

#### CON.4.A9 Deinstallation von Standardsoftware

Bei der Deinstallation von Standardsoftware SOLLTEN alle Dateien entfernt werden, die für den Betrieb der Software auf dem IT-System angelegt worden sind. Auch SOLLTEN alle Einträge in Systemdateien, die für das Produkt vorgenommen wurden, gelöscht werden. Um Standardsoftware wieder vollständig deinstallieren zu können, SOLLTEN die während der Installation durchgeführten Systemänderungen entweder manuell oder mit entsprechenden Programmen dokumentiert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.4.A10 Implementierung zusätzlicher Sicherheitsfunktionen(CIA)

Es SOLLTE geprüft werden, ob sich die Sicherheitsfunktionen der betriebenen Standardsoftware für einen erhöhten Schutzbedarf eignen. Ist das nicht der Fall, SOLLTEN geeignete Funktionen implementiert werden, um den Betrieb abzusichern.

Grundsätzlich SOLLTE ein erhöhter Schutzbedarf jedoch bereits bedacht werden, wenn die Anforderungen definiert werden und das Produkt ausgewählt wird.

#### CON.4.A11 Nutzung zertifizierter Standardsoftware(CIA)

Bei der Beschaffung von Standardsoftware SOLLTE festgelegt werden, ob eine Zusicherung des Herstellers, Vertreibers oder Anbieters über implementierte Sicherheitsfunktionen als ausreichend vertrauenswürdig anerkannt werden kann. Ist dies nicht der Fall, SOLLTE eine Zertifizierung der Anwendung nach Common Criteria als Entscheidungskriterium in Betracht gezogen werden. Stehen mehrere Produkte zur Auswahl, SOLLTEN Sicherheitszertifikate insbesondere dann berücksichtigt werden, wenn der evaluierte Funktionsumfang die Mindestfunktionalität (weitestgehend) umfasst und die Mechanismenstärke dem Schutzbedarf entspricht. Gibt es auf dem Markt kein geeignetes und zertifiziertes Produkt, SOLLTE die Einsatzumgebung der Standardsoftware entsprechend einem hohen Schutzbedarf abgesichert sein.

#### CON.4.A12 Einsatz von Verschlüsselung, Checksummen oder digitalen Signaturen(CI)

Wenn Daten mit erhöhtem Schutzbedarf übertragen oder gespeichert werden, SOLLTEN sie vorher verschlüsselt werden. Gibt es in einer Standardsoftware eine integrierte Verschlüsselungsfunktion, SOLLTE geprüft werden, ob diese ausreichend sicher ist. Das SOLLTE besonders bei älteren Produktversionen überprüft werden. Benutzer SOLLTEN im Umgang mit den Verschlüsselungsfunktionen geschult und sensibilisiert werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Auswahl und Einsatz von Standardsoftware" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [CC] Common Criteria for Information Technology Security Evaluation (CC)

  

 erschienen in der Normenreihe ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (zuletzt abgerufen am 28.09.2017)  
 <www.commoncriteriaportal.org>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Auswahl und Einsatz von Standardsoftware" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.22 Manipulation von Informationen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

