1 Beschreibung
--------------

### 1.1 Einleitung

Unternehmen und Behörden speichern immer mehr Daten und sind gleichzeitig immer stärker auf sie angewiesen. Gehen Daten dann verloren, z. B. durch defekte Hardware oder Malware, können gravierende Schäden entstehen. Durch regelmäßige Datensicherungen lassen sich solche Auswirkungen jedoch minimieren: Eine Datensicherung soll gewährleisten, dass durch einen redundanten Datenbestand der IT-Betrieb kurzfristig wiederaufgenommen werden kann, wenn Teile des operativen Datenbestandes verloren gehen.

### 1.2 Zielsetzung

Dieser Baustein zeigt auf, wie Institutionen ein Datensicherungskonzept erstellen können und welche Anforderungen dabei zu beachten sind.

### 1.3 Abgrenzung

Der Baustein beschreibt die grundsätzlichen Anforderungen, die zu einem angemessenen Datensicherungskonzept beitragen. Nicht behandelt werden Anforderungen an die Aufbewahrung und Erhaltung von elektronischen Dokumenten für die Langzeitspeicherung. Diese finden sich im Baustein OPS.1.2.2 *Archivierung*. Dieser Baustein beinhaltet keine system- oder anwendungsspezifischen Anforderungen zur Protokollierung, diese sind in den jeweiligen Bausteinen des IT-Grundschutz-Kompendiums zu finden, wie beispielsweise SYS.1.1. Allgemeiner Server, APP.3.2 Webserver oder NET.3.2 Firewall.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Datensicherung von besonderer Bedeutung:

### 2 1 Fehlende Datensicherung

Institutionen sind stärker denn je auf ihre IT-Systeme und die darin gespeicherten Daten angewiesen. Wenn Daten verloren gehen, z. B. durch Malware, technische Fehlfunktionen, einen Brand oder wenn Mitarbeiter Daten absichtlich oder unabsichtlich löschen und es keine Datensicherung gibt, ist das mitunter ein existenzbedrohender Schaden für die Institution, z. B. wenn alle Kundendaten verloren sind.

### 2 2 Fehlende Wiederherstellungstests

Eine Institution sichert regelmäßig ihre wichtigen Daten, darunter vor allem ihre Kundendaten. Wenn jedoch nicht regelmäßig getestet wird, ob sich die Daten wieder einspielen lassen, können die gesicherten Daten im Falle einer notwendigen Wiederherstellung nicht nutzbar sind. Im Fall der Kundendaten könnte dies für die Institution erhebliche Schäden bedeuten bis hin zur Einstellung des Vertriebs. 

### 2 3 Ungeeignete Aufbewahrung der Backup-Datenträger

Auf Backup-Datenträgern befinden sich zahlreiche schützenswerte Informationen der Institution. Sind die Datenträger an einem unsicheren Ort aufbewahrt, kann ein Angreifer (z. B. ein Innentäter), eventuell darauf zugreifen und schützenswerte Informationen stehlen oder manipulieren. Ebenso können Backup-Datenträger durch ungünstige Lagerung oder klimatische Raumbedingungen unbrauchbar werden und dann, wenn sie benötigt werden, nicht mehr verfügbar sein.

### 2 4 Fehlende oder unzureichende Dokumentation

Werden Datensicherungsmaßnahmen nicht oder nur mangelhaft dokumentiert, kann die Wiederherstellung länger dauern als geplant. Dadurch können sich wichtige Prozesse verzögern, z. B. in der Produktion. Auch ist es möglich, dass sich eine Datensicherung gar nicht mehr einspielen lässt und die Daten damit verloren sind.

### 2 5 Missachtung gesetzlicher Vorschriften

Wenn bei der Datensicherung gesetzliche Vorgaben, z. B. Datenschutzgesetze, nicht beachtet werden, können gegen die Institution Bußgelder verhängt oder Schadenersatzansprüche geltend gemacht werden.

### 2 6 Unsichere Cloud-Anbieter

Lagern Institutionen ihre Datensicherung zu einem Cloud-Anbieter aus, könnte auch ein Angreifer auf die Backup-Daten zugreifen oder das Backup kann nicht schnell genug wieder eingespielt werden. In der Folge sind schützenswerte Daten abgeflossen oder Datensicherungen im Notfall nicht in der benötigen Zeit verfügbar.

### 2 7 Ungenügende Speicherkapazitäten

Die Menge an verarbeiteten und folglich auch gespeicherten Daten nimmt stetig zu. Verfügen die Backup-Medien nicht über genügend Speicher, werden aktuellere Daten eventuell nicht mehr gesichert oder die eingesetzte Backup-Software überschreibt automatisch alte und eventuell noch benötigte Datensicherungen. Werden die Verantwortlichen hierüber nicht informiert, da z. B. das Monitoring unzureichend ist, gehen Daten eventuell ganz verloren oder es sind im Notfall nur die falschen Versionen verfügbar.

### 2 8 Unzureichendes Datensicherungskonzept

Wird für Datensicherungsmaßnahmen kein angemessenes Datensicherungskonzepts erstellt und befolgt, können gesicherte Daten in Bedarfsfall nicht wiederhergestellt werden. Bei den gesicherten Daten handelt es sich meist um schützenswerte Informationen, so dass das Backup verschlüsselt wird. Ist bei einem Datenverlust auch der Schlüssel zum Entschlüsseln des Backups betroffen, weil nicht bedacht wurde, diesen getrennt vorzuhalten, kann eine Wiederherstellung nicht möglich sein.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Datensicherung aufgeführt. Grundsätzlich ist der Informationssicherheitsbeauftragte für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. 

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### CON.3.A1 Erhebung der Einflussfaktoren der Datensicherung [IT-Betrieb, Fachverantwortliche]

Für jedes IT-System und eventuell für einzelne besonders wichtige IT-Anwendungen MÜSSEN die relevanten Einflussfaktoren ermittelt werden, wie z. B. Änderungsvolumen, Änderungszeitpunkte, Verfügbarkeitsanforderungen, Integritätsbedarf. Dazu SOLLTEN die Administratoren und die Verantwortlichen der einzelnen IT-Anwendungen befragt werden. Die Ergebnisse MÜSSEN nachvollziehbar und geeignet festgehalten werden. Neue Anforderungen MÜSSEN zeitnah in einem aktualisierten Datensicherungskonzept berücksichtigt werden.

#### CON.3.A2 Festlegung der Verfahrensweise für die Datensicherung [IT-Betrieb, Fachverantwortliche]

Für jedes IT-System und für jede Datenart MUSS ein Verfahren festgelegt werden, wie die Daten zu sichern sind. Dazu MÜSSEN Art, Häufigkeit und Zeitpunkte der Datensicherungen bestimmt werden. Weiterhin MÜSSEN die Verantwortlichkeiten für die Datensicherungen festgelegt werden. Auch MUSS definiert sein, welche Speichermedien benutzt und wie die Transport- und Aufbewahrungsmodalitäten auszusehen haben.

#### CON.3.A3 Ermittlung von rechtlichen Einflussfaktoren auf die Datensicherung

Die rechtlichen Anforderungen an die Datensicherung MÜSSEN ermittelt und in das Minimal- bzw. in das Datensicherungskonzept einfließen.

#### CON.3.A4 Erstellung eines Minimaldatensicherungskonzeptes

Es MUSS ein Minimaldatensicherungskonzept erstellt werden, dass festgelegt, welche Anforderungen für die Datensicherung mindestens einzuhalten sind. Dazu zählen kurze Beschreibungen, wie die Datensicherung erstellt und wiederhergestellt werden kann, welche Parameter gewählt wurden und welche Hard- und Software eingesetzt wird.

#### CON.3.A5 Regelmäßige Datensicherung [IT-Betrieb]

Es MÜSSEN regelmäßige Datensicherungen durchgeführt werden. Dabei MÜSSEN mindestens die Daten regelmäßig gesichert werden, die nicht aus anderen Informationen ableitbar sind. Die erstellten Datensicherungen MÜSSEN geeignet vor dem Zugriff Dritter geschützt werden. Es MUSS regelmäßig getestet werden, ob die Datensicherung auch wie gewünscht funktioniert, vor allem, ob gesicherte Daten problemlos zurückgespielt werden können

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Datensicherungskonzept. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### CON.3.A6 Entwicklung eines Datensicherungskonzepts [Leiter IT, Fachverantwortliche]

Es SOLLTE ein Datensicherungskonzept erstellt werden. Dieses SOLLTE mit allen Verantwortlichen abgestimmt werden. Darin SOLLTEN sämtliche zu berücksichtigende IT-Systeme aufgeführt werden. Die Mitarbeiter SOLLTEN über den sie betreffenden Teil des Datensicherungskonzepts unterrichtet werden. Es SOLLTE regelmäßig kontrolliert werden, ob das Datensicherungskonzept korrekt umgesetzt wird. 

#### CON.3.A7 Beschaffung eines geeigneten Datensicherungssystems [Leiter IT, IT-Betrieb]

Bevor ein Datensicherungssystem beschafft wird, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Die angeschafften Datensicherungssysteme SOLLTEN die Anforderungen des Sicherheits- und des Datensicherungskonzepts erfüllen.

#### CON.3.A8 Funktionstests und Überprüfung der Wiederherstellbarkeit [IT-Betrieb]

Es SOLLTE regelmäßig getestet werden, ob die Datensicherung auch wie gewünscht funktioniert und vor allem, ob gesicherte Daten problemlos und in angemessener Zeit zurückgespielt werden können.

#### CON.3.A9 Voraussetzungen für die Online-Datensicherung [Leiter IT, IT-Betrieb]

Wenn für die Datensicherung ein Online-Speicher genutzt werden soll, SOLLTEN mindestens folgende Punkte geregelt werden: 

* Gestaltung des Vertrages,
* Ort der Datenspeicherung,
* Vereinbarungen zur Dienstgüte (SLA),
* geeignete Authentisierungsmethoden,
* Verschlüsselung der Daten und
* Verschlüsselung auf dem Transportweg.
#### CON.3.A10 Verpflichtung der Mitarbeiter zur Datensicherung

Alle Mitarbeiter SOLLTEN über die Regelungen zur Datensicherung informiert sein. Auch SOLLTEN sie darüber informiert werden, welche Aufgaben sie bei der Erstellung von Datensicherungen haben und zu ihrer Durchführung verpflichtet werden.

#### CON.3.A11 Sicherungskopie der eingesetzten Software [IT-Betrieb]

Von eingesetzten Softwareprogrammen SOLLTEN Sicherungskopien angefertigt werden, sofern das rechtlich erlaubt und technisch möglich ist. Dabei SOLLTEN alle notwendigen Pakete und Informationen vorhanden sein, um die Software im Notfall wieder installieren zu können. Auch SOLLTEN die originalen Installationsquellen sowie die Lizenznummern an einem geeigneten Ort sicher aufbewahrt werden. 

#### CON.3.A12 Geeignete Aufbewahrung der Backup-Datenträger [IT-Betrieb]

Die Backup-Datenträger SOLLTEN vor unbefugtem Zugriff geschützt werden. Sie SOLLTEN räumlich von den Quell-Systemen getrennt werden. Der Aufbewahrungsort SOLLTE so klimatisiert sein, dass die Datenträger längerfristig aufbewahrt werden können.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.3.A13 Einsatz kryptografischer Verfahren bei der Datensicherung [IT-Betrieb]

Um die Vertraulichkeit und Integrität der gesicherten Daten zu gewährleisten, SOLLTEN alle Daten verschlüsselt werden. Es SOLLTE sichergestellt werden, dass sich die verschlüsselten Daten auch nach längerer Zeit wieder einspielen lassen. Verwendete kryptografische Schlüssel SOLLTEN mit einer getrennten Datensicherung geschützt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

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

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Datensicherungskonzept" von Bedeutung.

* G 0.2 Ungünstige klimatische Bedingungen
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

