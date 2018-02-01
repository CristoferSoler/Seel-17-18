1 Beschreibung
--------------

### 1.1 Einleitung

Für einen verlässlichen IT-Betrieb sollten IT-Systeme und Anwendungen alle oder ausgewählte betriebs- und sicherheitsrelevanten Ereignisse protokollieren, d. h. sie automatisch speichern und für die Auswertung bereitstellen. Eine Protokollierung wird in vielen Institutionen eingesetzt, um Hard- und Softwareprobleme sowie Ressourcenengpässe zeitnah entdecken zu können. Aber auch Sicherheitsprobleme und Angriffe auf die betriebenen Dienste können anhand von Protokollierungsdaten nachvollzogen werden. Ebenso können mit solchen Daten durch forensische Untersuchungen Beweise gesichert werden, nachdem ein Angriff auf IT-Systeme bekannt wurde. 

In jedem Informationsverbund werden lokal Protokollierungsdaten von einer Vielzahl von IT-Systemen und Anwendungen generiert. Um jedoch einen Gesamtüberblick über einen Informationsverbund zu erhalten, können die von verschiedenen IT-Systemen und Anwendungen generierten Protokollinformationen an eine dedizierte Protokollierungsinfrastruktur gesendet und dort zentral gespeichert werden. Nur so lassen sich die Protokollierungsdaten an einer Stelle auswählen, filtern und systematisch auswerten. 

### 1.2 Zielsetzung

Der Baustein enthält Anforderungen, mit denen die Protokollierung möglichst aller sicherheitsrelevanten Ereignisse umgesetzt werden kann. Ziel ist es, alle hierfür relevanten Daten sicher zu erheben, zu speichern und geeignet für die Auswertung bereitzustellen sowie deren ordnungsgemäße Entsorgung sicherzustellen.

### 1.3 Abgrenzung

Im vorliegenden Baustein werden nur übergreifende Aspekte betrachtet, die für eine angemessene Protokollierung erforderlich sind. Die Protokollierung spezifischer IT-Systeme oder Anwendungen wird hier nicht behandelt, sondern in den jeweiligen Bausteinen beschrieben.

In vielen Betriebssystemen oder Anwendungen sind Protokollierungsfunktionen bereits vorhanden oder können dort mittels Zusatzprodukten integriert werden. Um diese Funktionen und die gespeicherten Protokollierungsdaten abzusichern, muss das zugrundeliegende Betriebssystem geschützt sein. Das ist jedoch nicht Bestandteil dieses Bausteins. Dafür sind die betriebssystemspezifischen Bausteine umzusetzen, z. B. SYS.1.1 *Allgemeiner Server* und SYS.2.1 *Allgemeine Clients*. 

Auch ist der Baustein abzugrenzen von der Detektion (siehe DER.1 *Detektion von sicherheitsrelevanten Ereignissen*) sowie der Reaktion auf Sicherheitsvorfälle (DER.2 *Incident Management*): Beide Aspekte werden im Baustein Protokollierung nicht oder nur am Rande behandelt. 

Vorgaben, wie mit personenbezogenen Daten umzugehen ist, werden im Baustein CON.2 *Datenschutz* geregelt. Wie lang und umfangreich Protokollierungsdaten archiviert werden müssen, ist darüber hinaus im Baustein OPS.1.1.2 *Archivierung* erläutert.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich der Protokollierung von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichende Protokollierung

In einem Informationsverbund gibt es häufig IT-Systeme oder Anwendungen, bei denen die Protokollierung in der Grundeinstellung nicht aktiviert wurde. Auch können einzelne IT-Systeme und Anwendungen manchmal gar nicht protokollieren. In beiden Fällen können wichtige Informationen verloren gehen und Angriffe nicht rechtzeitig erkannt werden. Das ist jedoch auch dann möglich, wenn die Protokollierung bei einzelnen IT-Systemen genutzt wird, aber die Protokolle nicht an einer zentralen Stelle zusammengeführt werden. In Informationsverbünden ohne zentrale Protokollierung ist es schwierig sicherzustellen, dass die relevanten Protokollinformationen aller IT-Systeme erhalten und ausgewertet werden.

Weiterhin müssen Protokollierungsdaten aussagekräftige Informationen enthalten. Welche Ereignisse protokolliert werden, hängt unter anderem auch vom Schutzbedarf der jeweiligen IT-Systeme bzw. Anwendungen ab. Wird dieser missachtet, indem beispielsweise bei der Protokollierung nur auf Standard-Einstellungen der IT-Systeme bzw. Anwendungen zurückgegriffen wird, kann dies dazu führen, dass besonders relevante Sicherheitsereignisse nicht protokolliert werden. Somit werden Angriffe eventuell nicht erkannt.

### 2 2 Fehlerhafte Auswahl von relevanten Protokollierungsdaten

Protokollierungsdaten liefern oft wichtige Informationen, um IT-Sicherheitsvorfälle zu erkennen. Die relevanten Meldungen aus der großen Menge der verschiedenen Protokollereignisse auszuwählen ist eine besondere Herausforderung. Denn viele protokollierte Meldungen haben nur informativen Charakter und lenken von den wirklich wichtigen Meldungen ab. Werden zu viele Protokollmeldungen ausgewählt, lässt sich die Fülle von Informationen nur schwer und mit hohem Zeitaufwand auswerten. 

Des Weiteren können Protokollierungsdaten verworfen oder überschrieben werden, wenn der Arbeitsspeicher oder die Festplattenkapazität des IT-Systems bzw. der Protokollierungsinfrastruktur nicht ausreichen. Werden dadurch zu wenige oder nicht genug relevante Protokollmeldungen aufgezeichnet, könnten sicherheitskritische Vorfälle unerkannt bleiben. 

### 2 3 Fehlende Zeitsynchronisation bei der Protokollierung

Wenn in einem Informationsverbund die Zeit nicht auf allen IT-Systemen synchronisiert wird, können die Protokollierungsdaten eventuell nicht miteinander korreliert werden bzw. kann die Korrelation zu eventuell fehlerhaften Aussagen führen, da die unterschiedlichen Zeitstempel von Ereignissen keine gemeinsame Basis aufweisen. Eine fehlende Zeitsynchronisation erschwert es somit, erhobene Protokollierungsdaten auszuwerten, insbesondere wenn diese auf einem zentralen Logserver gespeichert werden. Weiterhin kann eine fehlerhafte oder fehlende Zeitsynchronisation dazu führen, dass die Protokollierung nicht zur Beweissicherung herangezogen werden kann. 

### 2 4 Fehlplanung bei der Protokollierung

Wird die Protokollierung nicht ausreichend geplant, kann dies dazu führen, dass IT-Systeme oder Anwendungen nicht überwacht und so sicherheitsrelevante Ereignisse nicht identifiziert und angemessen behandelt werden. Ebenso können Datenschutzverstöße nicht nachvollzogen werden.

### 2 5 Vertraulichkeits- und Integritätsverlust von Protokollierungsdaten

Einige IT-Systeme in einem Informationsverbund generieren Protokollierungsdaten wie Benutzernamen, IP-Adressen, E-Mail-Adressen und Rechnernamen, die konkreten Personen zugeordnet werden können. Solche Informationen lassen sich kopieren, abhören und manipulieren, wenn sie nicht verschlüsselt übertragen und gesichert gespeichert werden. Dies kann dazu führen, dass Angreifer auf vertrauliche Informationen zugreifen oder dass durch manipulierte Protokollierungsdaten Sicherheitsvorfälle bewusst verschleiert werden. Ebenso kann ein Angreifer, wenn er an eine größere Menge von Protokollierungsdaten gelangt, diese Informationen nutzen, um die interne Struktur des Informationsverbundes aufzudecken und dadurch seine Angriffe gezielter ausrichten.

### 2 6 Falsch konfigurierte Protokollierung

Wenn die Protokollierung in IT-Systemen falsch konfiguriert ist, werden wichtige Informationen gar nicht oder fehlerhaft aufgezeichnet. Auch kann es sein, dass zu viele oder falsche Informationen protokolliert werden. So können zum Beispiel personenbezogene Daten unberechtigt protokolliert und gespeichert werden und die Institution kann so gegen gesetzliche Anforderungen verstoßen. 

Ebenso ist es durch eine falsch konfigurierte Protokollierung möglich, dass die Protokollierungsdaten in inkonsistenten oder proprietären Formaten vorliegen. Dadurch lassen sich die Protokolle eventuell nur schwer auswerten und IT-Sicherheitsvorfälle bleiben unentdeckt. 

### 2 7 Ausfall von Datenquellen

Liefern IT-Systeme in einem Informationsverbund nicht mehr die notwendigen Protokollierungsdaten, lassen sich Sicherheitsvorfälle nicht mehr angemessen detektieren. Ursache für Ausfälle von Datenquellen können Fehler in der Hard- und Software oder auch fehlerhaft administrierte IT-Systeme sein. Besonders wenn nicht bemerkt wird, dass Datenquellen ausgefallen sind, kann das zu einem falschen Bild der Sicherheitslage in der Institution führen. Dadurch können Angreifer z. B. sehr lange unbemerkt bleiben und geschäftskritische Informationen abgreifen oder Produktionssysteme manipulieren. 

### 2 8 Ungenügend dimensionierte Protokollierungsinfrastruktur

Aufgrund der komplexen Informationsverbünde und vielfältigen Angriffsszenarien steigen die Anforderungen an die Protokollierung, da sehr viele Protokollierungsdaten gespeichert und verarbeitet werden müssen. Weiterhin ist es bei Sicherheitsvorfällen üblich, die Intensität der Protokollierung zu erhöhen. Ist die Protokollierungsinfrastruktur dafür jedoch nicht ausgelegt, besteht die Gefahr, dass Protokollierungsdaten unvollständig gespeichert werden. Somit lassen sich sicherheitsrelevante Ereignisse nicht mehr oder nur unzureichend auswerten und Sicherheitsvorfälle bleiben unentdeckt.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Protokollierung aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.1.5.A1 Erstellung einer Sicherheitsrichtlinie für die Protokollierung [Informationssicherheitsbeauftragter (ISB), Fachverantwortliche]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie die Protokollierung sicher geplant, aufgebaut und betrieben werden soll. In der Richtlinie MUSS geregelt werden, wie, wo und was protokolliert werden soll. Dabei SOLLTEN sich Art und Umfang der Protokollierung am Schutzbedarf der Informationen orientieren.

Die Richtlinie MUSS vom ISB gemeinsam mit den Fachverantwortlichen erstellt werden. Sie MUSS allen für die Protokollierung verantwortlichen Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem ISB abgestimmt und dokumentiert werden. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse MÜSSEN dokumentiert werden.

#### OPS.1.1.5.A2 Festlegung von Rollen und Verantwortlichkeiten [Leiter IT]

Für die in der Protokollierungsrichtlinie (siehe OPS.1.1.5.A1 *Erstellung einer Sicherheitsrichtlinie für die Protokollierung*) als relevant definierten IT-Systeme und Anwendungen MÜSSEN Verantwortliche benannt werden. Diese MÜSSEN sicherstellen, dass die Protokollierungsrichtlinie eingehalten wird. 

#### OPS.1.1.5.A3 Konfiguration der Protokollierung auf System- und Netzebene

Alle sicherheitsrelevanten Ereignisse von IT-Systemen und Anwendungen MÜSSEN protokolliert werden. Sofern die in der Protokollierungsrichtlinie als relevant definierten IT-Systeme und Anwendungen über eine Protokollierungsfunktion verfügen, MUSS diese benutzt werden. Wenn die Protokollierung eingerichtet wird, MÜSSEN dabei die Herstellervorgaben für die jeweiligen IT-Systeme oder Anwendungen beachtet werden. Es MUSS in angemessenen Intervallen stichpunktartig überprüft werden, ob die Protokollierung noch korrekt funktioniert. Die Intervalle MÜSSEN in der Protokollierungsrichtlinie definiert werden. Sofern betriebs- und sicherheitsrelevante Ereignisse nicht auf einem IT-System protokolliert werden können, MÜSSEN weitere IT-Systeme zur Protokollierung (z. B. von Ereignissen auf Netzebene) integriert werden. 

#### OPS.1.1.5.A4 Zeitsynchronisation der IT-Systeme

Die Systemzeit aller protokollierenden IT-Systeme und Anwendungen MUSS immer synchron sein. Es MUSS sichergestellt sein, dass das Datum und Zeitformat der Protokolldateien einheitlich ist. Weitere Hinweise hierzu finden sich im Baustein NET.1.2 *Netz-Management*.

#### OPS.1.1.5.A5 Einhaltung rechtlicher Rahmenbedingungen [Informationssicherheitsbeauftragter (ISB)]

Bei der Protokollierung MÜSSEN die gesetzlichen Bestimmungen aus den aktuellen Gesetzen zum Bundes-/Landesdatenschutz eingehalten werden (siehe CON.2 *Datenschutz*). Darüber hinaus MÜSSEN eventuelle Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeitervertretungen gewahrt werden. Ebenso MUSS sichergestellt sein, dass alle weiteren relevanten gesetzlichen Bestimmungen beachtet werden. Protokollierungsdaten MÜSSEN nach einem festgelegten Prozess gelöscht werden. Es MUSS technisch unterbunden werden, dass Protokollierungsdaten unkontrolliert gelöscht oder verändert werden. 

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Protokollierung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.1.5.A6 Aufbau einer zentralen Protokollierungsinfrastruktur

Vor allem in größeren Informationsverbünden SOLLTEN alle gesammelten sicherheitsrelevanten Protokollierungsdaten an einer zentralen Stelle gespeichert werden. Dafür SOLLTE eine zentrale Protokollierungsinfrastruktur im Sinne eines Logserver-Verbunds aufgebaut und in einem hierfür eingerichteten Netzsegment platziert werden. Der Logserver-Verbund SOLLTE die Protokollierungsdaten von IT-Systemen und Anwendungen ausschließlich nach dem Pull-Prinzip beziehen. Wird dies von IT-Systemen und Anwendungen nicht unterstützt, SOLLTEN die Protokollierungsdaten auf vorgelagerten IT-Systemen gesammelt und dort vom Logserver-Verbund abgeholt werden. Die hierfür erforderlichen Kommunikationsverbindungen SOLLTEN restriktiv erfolgen. 

Zusätzlich zu sicherheitsrelevanten Ereignissen (siehe OPS.1.1.5.A3 *Konfiguration der Protokollierung auf System- und Netzebene*) SOLLTE eine zentrale Protokollierungsinfrastruktur auch allgemeine Betriebsereignisse protokollieren, die auf einen Fehler hindeuten, z. B.: 

* Ausbleiben von Protokollierungsdaten bzw. Nichterreichbarkeit eines protokollierenden IT-Systems,
* Betriebsereignisse, die auf eine außergewöhnliche Auslastung bzw. Beanspruchung einzelner Dienste hindeuten.
Die Protokollierungsinfrastruktur SOLLTE ausreichend dimensioniert sein, sodass eine Skalierung im Sinne einer erweiterten Protokollierung berücksichtigt werden kann. Dafür SOLLTEN genügen technische, finanzielle und personelle Ressourcen verfügbar sein. Falls die Protokollierungsinfrastruktur extern aufgebaut und betrieben werden soll, SOLLTE ein spezialisierter Dienstleister beauftragt werden. 

#### OPS.1.1.5.A7 Sichere Administration von Protokollierungsservern

Der Logserver-Verbund SOLLTE ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden. Für die Administrationszugriffe SOLLTE ein Berechtigungskonzept erstellt werden. Es SOLLTEN nur Administratoren auf die Protokollierungsserver zugreifen können, die speziell dafür verantwortlich sind (siehe* *OPS.1.1.5.A2 *Festlegung von Rollen und Verantwortlichkeiten*).

#### OPS.1.1.5.A8 Archivierung von Protokollierungsdaten

Für Protokollierungsdaten SOLLTE ein Archivierungskonzept erstellt werden. Dabei SOLLTEN die gesetzlich vorgeschriebenen Regelungen berücksichtigt und im Konzept dokumentiert werden (siehe auch OPS.1.2.2 *Archivierung*).

#### OPS.1.1.5.A9 Bereitstellung von Protokollierungsdaten für die Auswertung

Die gesammelten Protokollierungsdaten SOLLTEN mithilfe einer Protokollierungsanwendung gefiltert, normalisiert, aggregiert und korreliert werden. Die so bearbeiteten Protokollierungsdaten SOLLTEN geeignet verfügbar gemacht werden, damit sie ausgewertet werden können. Damit sich die Daten automatisiert auswerten lassen, SOLLTEN die Protokollanwendungen über entsprechende Schnittstellen für die Auswertungsprogramme verfügen. Es SOLLTE sichergestellt sein, dass bei der Auswertung die in der Protokollierungsrichtlinie definierten Sicherheitsanforderungen eingehalten werden. Auch wenn die Daten bereitgestellt werden, SOLLTEN betriebliche und interne Vereinbarungen berücksichtigt werden. Die Protokollierungsdaten SOLLTEN in Originalform aufbewahrt werden.

#### OPS.1.1.5.A10 Zugriffsschutz für Protokollierungsdaten

Alle Protokollierungsdaten SOLLTEN so gespeichert werden, dass keine Unbefugten darauf zugreifen können. Es SOLLTE zudem ein Zugriffskonzept erstellt werden, das regelt, wer auf welche protokollierten Daten zugreifen darf. Dabei SOLLTEN die Berechtigungen so restriktiv wie möglich vergeben werden. 

Es SOLLTE sichergestellt sein, dass auf die Protokollierungsdaten grundsätzlich nur zugegriffen wird, wenn sicherheitsrelevante Vorfälle aufzuklären sind. Dabei SOLLTE nach der im Baustein DER.1 *Detektion von sicherheitsrelevanten Ereignissen* festgelegten Methode vorgegangen werden. Ein solcher Zugriff SOLLTE dokumentiert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.1.5.A11 Steigerung des Protokollierungsumfangs(CIA)

Bei erhöhtem Schutzbedarf von Anwendungen oder IT-Systemen SOLLTE die Menge und Art der protokollierten Ereignisse erweitert werden, sodass sicherheitsrelevante Vorfälle möglichst lückenlos nachvollziehbar sind. 

Um eine Echtzeitauswertung der Protokollierungsdaten zu ermöglichen, SOLLTEN in verkürzten Zeitabständen die Protokollierungsdaten von den protokollierenden IT-Systemen und Anwendungen zentral gespeichert werden (siehe auch OPS.1.1.5.A6 *Aufbau einer zentralen Protokollierungsinfrastruktur*). Die Protokollierung SOLLTE eine Auswertung über den gesamten Informationsverbund ermöglichen.

Anwendungen und IT-Systeme, mit denen eine zentrale Protokollierung nicht möglich ist, SOLLTEN bei einem erhöhten Schutzbedarf NICHT eingesetzt werden.

#### OPS.1.1.5.A12 Verschlüsselung(CI)

Um Protokollierungsdaten sicher übertragen zu können, SOLLTEN sie verschlüsselt werden. Weiterhin SOLLTEN alle gespeicherten Protokolle digital signiert werden. Auch archivierte und außerhalb der Protokollierungsinfrastruktur gespeicherte Protokollierungsdaten sollten immer verschlüsselt gespeichert werden. Weitere Hinweise und Anforderungen dazu führt Baustein CON.1 *Kryptokonzept* auf. 

#### OPS.1.1.5.A13 Hochverfügbare Protokollierungssysteme [Informationssicherheitsbeauftragter (ISB)](A)

Bei erhöhtem Schutzbedarf SOLLTE eine hochverfügbare Protokollierungsinfrastruktur aufgebaut werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Protokollierung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Protokollierung" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

