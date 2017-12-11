1 Beschreibung
--------------

### 1.1 Einleitung

Damit Informationen nicht in falsche Hände geraten, ist eine geregelte Vorgehensweise erforderlich, um Daten und Datenträger vollständig und zuverlässig zu löschen oder zu vernichten. Schutzbedürftige Informationen, die auf analogen und digitalen Datenträgern gespeichert sind, müssen hierbei betrachtet werden. 

Wenn nicht oder nur unzureichend gelöschte Datenträger weitergegeben, verkauft oder ausgesondert werden, können dadurch unbeabsichtigt schützenswerte Informationen weitergegeben werden und erhebliche Schäden entstehen. Daher muss jede Institution eine Vorgehensweise zum sicheren Löschen und Vernichten haben. 

### 1.2 Zielsetzung

In diesem Baustein wird beschrieben, wie Informationen in Institutionen sicher gelöscht und vernichtet und wie ein entsprechendes Konzept hierfür erstellt werden sollte. 

### 1.3 Abgrenzung

Der Baustein beinhaltet nur die allgemeinen prozessualen, technischen und organisatorischen Anforderungen an das Löschen und Vernichten. Einzelne Bausteine der Schichten CON (Konzepte und Vorgehensweisen), Sicherheitsmanagement (ISMS), ORP (Organisation und Personal), OPS (Betrieb), DER (Detektion und Reaktion), IND (Industrielle IT), APP (Anwendungen), SYS (IT-Systeme), NET (Netze und Kommunikation) und INF (Infrastruktur) können ergänzende und spezifischere Anforderungen an das Löschen und Vernichten definieren. Vor allem die Bausteine OPS.1.1.6 *Datensicherung*, OPS 1.2.2 *Archivierung,* OPS.1.2.3* Informations- und Datenträgeraustausch und* OPS.1.2.7 *Verkauf/Aussonderung von IT* sind zusätzlich zu berücksichtigen, da diese Themen direkt mit dem Löschen und Vernichten verbunden sind. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Löschen und Vernichten von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichend dokumentierte Regelungen beim Löschen und Vernichten

Wenn es keine dokumentierten Prozesse und Verfahrensweisen für das Löschen und Vernichten von Informationen und Datenträgern gibt oder werden diese nicht korrekt angewendet, können vertrauliche Informationen nicht wirklich sicher vernichtet werden und so in falsche Hände geraten. Diese Gefahr ist bei auszusondernden Datenträgern und IT-Systemen besonders hoch, da durch unzureichende Regelungen eventuell Informationen auf ihnen verbleiben. Diese Daten könnten durch unbefugte Dritte ausgelesen oder entwendet werden. Wenn darunter existenzielle Informationen sind, wäre so die gesamte Institution gefährdet. 

### 2 2 Vertraulichkeitsverlust durch Restinformationen auf Datenträgern

Bei elektronischer Datenübermittlung oder Datenträgerweitergabe passiert es immer wieder, dass auch Informationen weitergegeben werden, die die Institution nicht verlassen sollten. 

Bei den meisten Dateisystemen werden Dateien, die der Benutzer löscht, nicht wirklich vernichtet. Es werden lediglich die Verweise auf die Datei aus den Verwaltungsinformationen des Dateisystems gelöscht und die zu der Datei gehörenden Blöcke als frei markiert. Der tatsächliche Inhalt der Blöcke auf dem Datenträger bleibt jedoch erhalten und kann mit entsprechenden Werkzeugen rekonstruiert werden. Dadurch können sich Angreifer Zugriff auf die Datei verschaffen, z. B. wenn solche Datenträger an Dritte weitergegeben oder ungeeignet entsorgt werden. So könnten vertrauliche Informationen nach außen gelangen.

### 2 3 Unstrukturierte Datenhaltung

Durch unzureichende Vorgaben, sowie fehlende Schulung der Mitarbeiter, können Informationen unübersichtlich auf benutzten Datenträgern gespeichert werden. Das kann dazu führen, dass Informationen nicht vollständig gelöscht werden können, da kein Zuständiger mehr weiß, was in welchen Dateien gespeichert ist. Auch können Angreifer eventuell unbemerkt auf Informationen zugreifen, wenn viele Kopien einer Datei existieren und diese in verschiedenen Verzeichnissen mit unterschiedlichen Schutzfunktionen vorliegen. Kopien werden oft nicht nur in verschiedenen Verzeichnissen eines Datenträgers abgelegt. Viel kritischer ist es, wenn mehrere Kopien auf unterschiedlichen Datenträgern abgelegt werden und nicht mehr ersichtlich ist, wo was wann abgelegt wurde. Gesteigert wird dieses Problem, wenn die Datenträger dezentral beschafft und nicht kontrolliert werden. Eine unstrukturierte Datenhaltung gefährdet sowohl die Verfügbarkeit (das Arbeiten mit den Daten) als auch die Integrität und Vertraulichkeit.

### 2 4 Vertraulichkeitsverlust durch Auslagerungs- und temporäre Dateien

In Auslagerungsdateien oder Auslagerungspartitionen befinden sich mitunter vertrauliche Daten, z. B. Passwörter oder kryptografische Schlüssel. Die Auslagerungsdateien und damit auch die darin befindlichen Informationen sind jedoch nicht geschützt, da sie z. B. ausgelesen werden können, wenn die Festplatte ausgebaut und in einem anderen IT-System eingebaut wird. 

Auch fallen im laufenden Betrieb vieler Anwendungen Dateien an, die nicht für den produktiven Betrieb benötigt werden (z. B. Browser-Historie). Auch diese Dateien können sicherheitsrelevante Informationen enthalten. Werden Auslagerungs- oder temporäre Dateien nicht sicher gelöscht, können schützenswerte Informationen, Passwörter und Schlüssel von Unbefugten missbraucht werden, um sich einen Zugang zu weiteren IT-Systemen und Daten zu verschaffen, Wettbewerbsvorteile auf dem Markt zu erlangen oder gezielt Benutzerverhalten auszuspionieren.

### 2 5 Ungeeignete Entsorgung der Datenträger und Dokumente

Wenn Datenträger oder Dokumente nicht geeignet entsorgt werden, können hieraus eventuell Informationen extrahiert werden, die Dritten nicht in die Hände fallen sollten. So können Angreifer z. B. Datenträger aus unzureichend gesicherten Entsorgungseinrichtungen stehlen. Auch wenn beauftragte Entsorgungsdienstleister ungenügend kontrolliert werden, kann die Vertraulichkeit nicht ausreichend sichergestellt werden. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Löschen und Vernichten aufgeführt. Grundsätzlich ist der ISB für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### CON.6.A1 Regelung der Vorgehensweise für die Löschung und Vernichtung von Informationen [Leiter IT, Leiter Organisation]

Die Institution MUSS das Löschen und Vernichten von Informationen regeln. Dabei MUSS je nach Organisationseinheit geregelt werden, welche Informationen und Betriebsmittel unter welchen Voraussetzungen gelöscht und entsorgt werden dürfen. Ebenso MUSS festgelegt werden, in welchen räumlichen Bereichen Entsorgungs- und Vernichtungseinrichtungen aufgebaut werden sollen.

Außerdem MUSS schon in der Planungsphase festgelegt sein, wer für das Löschen und Vernichten von Informationen und Betriebsmitteln zuständig ist und welche Schnittstellen es zwischen den Organisationseinheiten gibt. Ebenso MUSS der Informationsfluss intern und zwischen den Zuständigen der Institution mit möglichen Outsourcing-Dienstleistern geregelt werden.

#### CON.6.A2 Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln und Informationen [Mitarbeiter, Leiter IT, Leiter Haustechnik]

Alle schutzbedürftigen Informationen und Betriebsmittel MÜSSEN sicher entsorgt werden. Zu diesem Zweck MÜSSEN abgesicherte und geeignete Entsorgungseinrichtungen auf dem Gelände der Institution verfügbar sein. Dabei MUSS auch berücksichtigt werden, dass Informationen und Betriebsmittel eventuell erst gesammelt und dann später entsorgt werden. Eine solche zentrale Sammelstelle MUSS vor unbefugten Zugriffen abgesichert werden.

Wenn externe Dienstleister beauftragt werden, MUSS der Entsorgungsvorgang ausreichend sicher und nachvollziehbar sein. Die mit der Entsorgung beauftragten Unternehmen SOLLTEN regelmäßig daraufhin überprüft werden, ob der Entsorgungsvorgang noch dem Sollzustand entspricht.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Löschen und Vernichten. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### CON.6.A3 Löschen der Datenträger vor und nach dem Austausch [Fachverantwortliche]

Bevor bereits benutzte Datenträger weitergegeben oder noch einmal eingesetzt werden, SOLLTEN alle darauf befindlichen Daten sicher gelöscht werden. Dazu SOLLTEN den Mitarbeitern geeignete Verfahren (siehe CON.6.A4* Auswahl geeigneter Verfahren zur Löschung oder Vernichtung von Datenträgern*) zur Verfügung stehen. 

#### CON.6.A4 Auswahl geeigneter Verfahren zur Löschung oder Vernichtung von Datenträgern [Leiter IT, Leiter Organisation]

Für das Löschen und Vernichten SOLLTEN geeignete Verfahren ausgewählt werden. So SOLLTE es für verschiedene Datenträgerarten immer geeignete Geräte und Werkzeuge geben, mit denen der verantwortliche Mitarbeiter die gespeicherten Informationen löschen oder vernichten kann. Es SOLLTE regelmäßig kontrolliert werden, ob die gewählten Verfahren noch dem Stand der Technik entsprechen und für die Institution noch ausreichend sicher sind. Die ausgewählten Verfahrensweisen SOLLTEN allen Mitarbeitern bekannt sein. 

#### CON.6.A5 Geregelte Außerbetriebnahme von IT-Systemen und Datenträgern [IT-Betrieb, Mitarbeiter, Fachverantwortliche, Leiter IT]

Es SOLLTE geregelt und dokumentiert werden, wie IT-Systeme und Datenträger außer Betrieb zu nehmen sind. Dabei SOLLTE sichergestellt sein, dass vor der Aussonderung alle auf einem IT-System oder Datenträger gespeicherten Informationen sicher gelöscht sind. Bei der Aussonderung SOLLTEN neben "klassischen" IT-Systemen auch alle IT-Systeme berücksichtigt werden, die dauerhafte Speicherelemente enthalten.

#### CON.6.A6 Einweisung aller Mitarbeiter in die Methoden zur Löschung oder Vernichtung von Informationen [Leiter IT]

Alle Mitarbeiter SOLLTEN in die Methoden und Verfahrensweisen zum Löschen und Vernichten von Informationen eingewiesen werden. Dabei SOLLTE nach den Anforderungen des Bausteins *ORP.3 Sensibilisierung und Schulung* vorgegangen werden. 

#### CON.6.A7 Beseitigung von Restinformationen [IT-Betrieb, Mitarbeiter]

Wenn Datenträger und Dateien weitergegeben werden, SOLLTE sichergestellt sein, dass sie keine sogenannten Restinformationen enthalten. Dazu SOLLTE ein Prozess in der Institution etabliert und dokumentiert werden. Damit die Mitarbeiter ihn auch ausreichend umsetzen, SOLLTEN sie über die Gefahren von Rest- und Zusatzinformationen in Dateien informiert werden. Es SOLLTE stichprobenartig überprüft werden, ob die in Dateien enthaltenen Restinformationen auch wirklich gelöscht werden.

#### CON.6.A8 Richtlinie für die Löschung und Vernichtung von Informationen [Mitarbeiter, Leiter IT, Datenschutzbeauftragter]

Die Regelungen der Institution zum* *Löschen und Vernichten SOLLTEN in einer Richtlinie dokumentiert werden. Die Richtlinie SOLLTE allen relevanten Verantwortlichen und Mitarbeitern der Institution bekannt sein und die Grundlage für deren Arbeit und Handeln bilden. Inhaltlich SOLLTE die Richtlinie alle eingesetzten Datenträger, Anwendungen, IT-Systeme und sonstigen Betriebsmittel und Informationen enthalten, die vom Löschen und Vernichten betroffen sind. Es SOLLTE regelmäßig und stichprobenartig überprüft werden, ob die Mitarbeiter sich an die Richtlinie halten. Die Richtlinie SOLLTE regelmäßig aktualisiert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.6.A9 Auswahl geeigneter Verfahren zur Löschung oder Vernichtung von Datenträgern bei erhöhtem Schutzbedarf [Leiter IT, Leiter Organisation](CIA)

Für das Löschen und Vernichten SOLLTEN Verfahren ausgewählt werden, die dem erhöhten Schutzbedarf der Informationen und Betriebsmittel gerecht werden. 

#### CON.6.A10 Beschaffung geeigneter Geräte zur Löschung oder Vernichtung von Daten [Leiter Organisation, Leiter IT, Beschaffungsstelle](CIA)

Bevor Geräte zur Löschung oder Vernichtung von Daten beschafft werden, SOLLTE eine Anforderungsdokumentation erstellt werden, anhand derer die auf dem Markt verfügbaren Werkzeuge miteinander verglichen werden können.

#### CON.6.A11 Vernichtung von Datenträgern durch externe Dienstleister [Leiter Organisation, Datenschutzbeauftragter](CIA)

Auf dem Gelände der Institution SOLLTEN alle zu vernichtenden Datenträger bis zur Abholung durch den externen Dienstleister sicher vor unbefugten Zugriffen aufbewahrt werden. Der Abtransport SOLLTE ebenfalls dem Schutzbedarf entsprechend abgesichert sein. Die Institution SOLLTE den Entsorgungsprozess regelmäßig durch eingewiesene Personen kontrollieren lassen. 

Zudem SOLLTEN die in OPS.2.1 *Outsourcing-Nutzung* beschriebenen generellen Anforderungen an Dienstleister und deren Mitarbeiter umgesetzt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Löschen und Vernichten" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001A8.3] ISO/IEC 27001:2013 - Annex A.8.3 Media handling

  

 ISO, Information technology- Security techniques- Information security management system- Requirements, insbesondere Annex A, A.8.3 Media handling, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [DIN663991] DIN 66399-1:2012-10 Büro- und Datentechnik Teil 1

  

 Teil 1: Grundlagen und Begriffe, 2012

 
* #### [DIN663992] DIN 66399-2:2012-10 Büro- und Datentechnik Teil 2

  

 Teil 2: Anforderungen an Maschinen zur Vernichtung von Datenträgern, 2012

 
* #### [DIN663993] DIN SPEC 66399-3:2013-02 - Büro- und Datenträgertechnik Teil 3

  

 Teil 3: Prozess der Datenträgervernichtung, 2013

 
* #### [SP80088] NIST Special Publication 800-88 Revision 1

  

 NIST, Guidelines for Media Sanitization, 12.2014  
 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Löschen und Vernichten" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.44 Unbefugtes Eindringen in Räumlichkeiten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

