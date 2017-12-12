1 Beschreibung
--------------

### 1.1 Einleitung

Der Einsatz von IT zur Aufgabenbewältigung setzt voraus, dass die maschinelle Datenverarbeitung soweit wie möglich fehlerfrei arbeitet, da die Einzelergebnisse in den meisten Fällen nicht mehr kontrolliert werden können. Im Zuge der Software-Tests wird deshalb überprüft, ob die betrachtete Software fehlerfrei arbeitet. Hierfür muss die Software die erforderliche Funktionalität zuverlässig bereitstellen und darf darüber hinaus keine unerwünschten Nebeneffekte haben. Mit der anschließenden Freigabe der Software durch die fachlich zuständige Organisationseinheit wird die grundsätzliche Erlaubnis erteilt, die Software produktiv in der Institution zu nutzen. Gleichzeitig übernimmt diese Organisationseinheit damit auch die Verantwortung für das IT-Verfahren, das durch die Software unterstützt wird.

Software kann an unterschiedlichen Stellen des Lebenszyklus einer Software getestet werden. So können Software-Tests bereits bei der Entwicklung, vor der Freigabe für den Produktivbetrieb oder im Zuge des Patch- und Änderungsmanagements notwendig werden. Die Software-Tests und -Freigaben sind sowohl für Eigenentwicklungen als auch beim Einsatz von Standard-Software durchzuführen.

Dieser Baustein beschreibt den Test- und Freigabeprozess für selbst entwickelte oder angepasste Software sowie für Standardsoftware. Der Test- und Freigabeprozess zeichnet sich dadurch aus, dass dieser je nach Ergebnis mehrmals durchlaufen werden kann.

### 1.2 Zielsetzung

Mit der Umsetzung dieses Bausteins sorgt die Institution dafür, dass eingesetzte Software den technischen und organisatorischen Anforderungen sowie dem vorliegenden Schutzbedarf der gesamten Institution oder einzelner Organisationseinheiten entspricht. Ein wesentlicher Teilaspekt ist dabei, dass sicherheitskritische Software auf bestehende Schwachstellen systematisch und methodisch überprüft wird.

### 1.3 Abgrenzung

Während der Baustein CON.3 *Softwareentwicklung* auf den Softwareentwicklungsprozess und die darin enthaltenen Software-Tests, die während des Entwicklungsprozesses notwendig sind, eingeht, beschreibt dieser Baustein die speziellen Anforderungen, die an ein Test- und Freigabemanagement gestellt werden. Dabei bezieht sich dieses Test- und Freigabemanagement nicht ausschließlich auf selbst oder im Kundenauftrag entwickelte Software, sondern auch auf das Testen und die Freigabe von CON.4 *Auswahl und Einsatz von Standsoftware *und APP.1.1 *Office-Produkte*. 

Für die Software-Tests werden unterschiedliche fachliche Methoden eingesetzt. Die Vorgehensweise bei Penetrationstests ist im Baustein DER.3.3 *Penetrationstests* genauer beschrieben.

Software-Tests können auch Bestandteil des Patch- oder Änderungsmanagements werden. Dieses ist im Baustein OPS.1.1.3 *Patch- und Änderungsmanagement* näher spezifiziert.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Software-Tests und -Freigaben von besonderer Bedeutung:

### 2 1 Unvollständige Umsetzung von Anforderungen des Auftraggebers

Werden die Anforderungen unvollständig oder fehlerhaft eingearbeitet oder kommunizieren die an der Software-Entwicklung oder -Beschaffung beteiligten Parteien (z. B. Auftraggeber und Auftragnehmer) unzureichend miteinander, könnten die Anforderungen des Auftraggebers nur unvollständig erfüllt werden. Hieraus können Schwachstellen in der Software entstehen. Müssen beispielsweise die Anforderungen des Auftragnehmers nachträglich eingearbeitet werden, können sich Software-Entwicklungsprojekte verzögern und dadurch finanzielle Schäden entstehen.

### 2 2 Unzureichende Schulung der Entwickler und Software-Tester

Es wird häufig davon ausgegangen, dass ausgebildete Entwickler und Software-Tester aufgrund ihrer Ausbildung über ein ausreichendes Wissen für das Testen und Freigeben von Software verfügen. Entsprechend werden Entwickler und Software-Tester häufig zu wenig zu Neuerungen ihres Themengebiets oder zum Einsatzgebiet der Software geschult. Diese Unkenntnis kann zu gravierenden Sicherheitsproblemen führen, wenn z. B. Funktionen oder Methoden in der Programmierung verwendet werden, die bereits als unsicher eingestuft sind, dies aber bei den Entwicklern noch nicht bekannt ist.

### 2 3 Software-Test mit Produktivdaten

Software-Tests mit Produktivdaten oder im Produktivbetrieb sind notwendig, denn nur mit den Produktivdaten kann die Funktion und die Performance des Produktes beurteilt werden. Oft haben auch Entwickler einen anderen Blick auf das entwickelte Produkt, beispielsweise haben sie ein anderes Sicherheitsbewusstsein, vertrauen der entwickelten Software zu sehr und können mögliche Auswirkungen von Problemen nicht richtig deuten. 

Obwohl Software-Tests mit Produktivdaten notwendig sind, können hierdurch Sicherheitsprobleme entstehen. Insbesondere vertrauliche Produktivdaten können für die Software-Tests so von unbefugten Mitarbeiter oder Dritten eingesehen werden, die mit dem jeweiligen Software-Test beauftragt wurden.

Durch Software-Tests im Produktivbetrieb könnte der Betrieb massiv gestört werden. Fehlfunktionen der zu testenden Software können Auswirkungen auf andere Anwendungen und IT-Systeme haben, die dadurch massiv gestört werden. Wird mit den "originalen" Produktivdaten im Produktivbetrieb getestet und nicht mit Kopien von den Daten, könnten diese ungewollt geändert oder gelöscht werden.

### 2 4 Fehlendes oder unzureichendes Testverfahren

Wird neue Software nicht oder nur unzureichend getestet und ohne Installationsvorschriften freigegeben, können Fehler in der Software unerkannt bleiben. Ebenso ist es möglich, dass dadurch erforderliche und einzuhaltende Installationsparameter nicht erkannt oder beachtet werden.

Diese Software- oder Installationsfehler, die aus einem fehlenden oder unzureichenden Software-Testverfahren resultieren, stellen eine erhebliche Gefährdung für den IT-Betrieb der Institution dar. So können beispielsweise Daten verloren gehen, wenn ein Update eines Datenbankmanagementsystems ohne vorherigem Test eingespielt wird.

### 2 5 Fehlendes oder unzureichendes Freigabeverfahren

Ein fehlendes oder unzureichendes Freigabeverfahren kann dazu führen, dass Software eingesetzt wird, die von der fachlichen Seite nicht abgenommen wurde. So kann die Software Funktionalitäten aufweisen, die sie nicht aufweisen sollte, oder Funktionalitäten können fehlen. Außerdem kann die Software zu anderen Anwendungen inkompatibel sein.

### 2 6 Fehlende oder unzureichende Dokumentation der Tests und Testergebnisse

Eine Software-Freigabe kann in der Regel erteilt werden, sobald alle Tests durchgeführt wurden und keine Abweichungen gefunden wurden. Sollte die Dokumentation der Software-Tests jedoch unvollständig sein, ist nachträglich nicht erkennbar, was getestet wurde. Wurden erkennbare Softwarefehler oder fehlende Funktionen ungenügend dokumentiert und damit bei der Freigabe nicht berücksichtigt, können durch diese Abweichungen die zu verarbeitenden Produktivdaten ungewollt gelöscht oder verändert sowie andere IT-Systeme und Anwendungen gestört werden. 

### 2 7 Fehlende oder unzureichende Dokumentation der Freigabekriterien

Wenn Freigabekriterien nicht klar kommuniziert werden, kann dies dazu führen, dass die Freigabe voreilig erteilt wird oder keine Freigabe erfolgt, obwohl diese erteilt werden könnte. Dadurch können zum einen Versionen mit nicht erkannten Softwarefehlern freigegeben werden, die den Produktivbetrieb stören können und zum anderen kann dies zu einem Projektverzug mit finanziellen Schäden führen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Software-Tests und -Freigabe aufgeführt. Grundsätzlich ist der Leiter IT für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.1.6.A1 Planung der Software-Tests

Bevor die Software-Tests durchgeführt werden können, MÜSSEN die Rahmenbedingungen dafür innerhalb der Institution entsprechend der Schutzbedarfe, Organisationseinheiten, technischen Möglichkeiten und Test-Umgebungen festlegt sein. Die Software-Tests MÜSSEN auf den Angaben des Pflichtenhefts basieren.

Bei der Auswahl der Testfälle MUSS darauf geachtet werden, dass diese möglichst repräsentativ für die zu testenden Funktionen sind.

#### OPS.1.1.6.A2 Durchführung von funktionalen Software-Tests [Tester]

Funktionale Software-Tests MÜSSEN durchgeführt werden, um die ordnungsgemäße und vollständige Funktion der Software zu überprüfen. Die funktionalen Software-Tests MÜSSEN derart durchgeführt werden, dass diese den Produktivbetrieb nicht beeinflussen.

#### OPS.1.1.6.A3 Auswertung der Testergebnisse [Tester]

Die Ergebnisse der Software-Tests MÜSSEN ausgewertet werden. Es SOLLTE ein Soll- und Ist-Vergleich über den Abgleich mit definierter Vorgaben durchgeführt werden. Die Auswertung MUSS dokumentiert werden.

#### OPS.1.1.6.A4 Freigabe der Software [Fachverantwortliche]

Die fachliche Organisationseinheit MUSS die Software freigeben, sobald die Software-Tests erfolgreich durchgeführt wurden. Die Freigabe MUSS in Form einer Freigabeerklärung dokumentiert werden.

Die freigebende Organisationseinheit MUSS überprüfen, ob die Software gemäß den Anforderungen getestet wurde. Die Ergebnisse der Software-Tests MÜSSEN mit den vorher festgelegten Erwartungen übereinstimmen. Auch MUSS überprüft werden, ob die Einhaltung rechtlicher oder organisatorischer Vorgaben sichergestellt ist.

#### OPS.1.1.6.A5 Durchführung nicht-funktionaler Software-Tests [Tester]

Es MÜSSEN nicht-funktionale Tests durchgeführt werden. Insbesondere SOLLTEN sicherheitsspezifische Software-Tests durchgeführt werden, wenn die Anwendung sicherheitskritische Funktionen mitbringt. Die durchgeführten Testfälle als auch die Testergebnisse SOLLTEN dokumentiert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Software-Tests und -Freigaben. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.1.6.A6 Geordnete Einweisung der Software-Tester [IT-Betrieb, Fachverantwortliche]

Ein Software-Tester SOLLTE über die durchzuführenden Testarten und die zu testenden Bereiche einer Software vom IT-Betrieb informiert werden. Darüber hinaus SOLLTE der Software-Tester über die Anwendungsfälle und mögliche weitere Anforderungen der Software informiert werden. 

#### OPS.1.1.6.A7 Personalauswahl der Software-Tester [Personalabteilung]

Bei der Auswahl der Software-Tester SOLLTEN gesonderte Auswahlkriterien berücksichtigt werden. Die Personen SOLLTEN über die erforderliche berufliche Qualifikation verfügen. Es SOLLTEN ausreichende Kenntnisse der zu testenden Programmiersprache, Entwicklungsumgebung und den einzusetzenden Testmethoden vorhanden sein.

In öffentlichen Einrichtungen und geheimschutzbetreuten Institutionen SOLLTE geprüft werden, ob eine Sicherheitsüberprüfung erforderlich ist.

#### OPS.1.1.6.A8 Fort- und Weiterbildung der Software-Tester [Leiter Personal]

Die Software-Tester SOLLTEN entsprechend dem Baustein OPS.3 Sensibilisierung und Schulung geschult werden. Es SOLLTEN Verfahren etabliert werden, mit denen die Software-Tester über Neuerungen informiert werden, die für ihr jeweiliges Aufgabenspektrum relevant sind.

#### OPS.1.1.6.A9 Beschaffung von Test-Software [Tester, IT-Betrieb]

Die zu beschaffende Test-Software SOLLTE laut einem Anforderungskatalog beschafft werden. Sie SOLLTE ebenfalls dem Test- und Freigabeprozess unterzogen werden. Es SOLLTEN überprüft werden, ob die Hilfestellungs- und Supportleistungen des Softwareherstellers ausreichend sind. 

#### OPS.1.1.6.A10 Erstellung eines Abnahmeplans

Im Abnahmeplan SOLLTEN die durchzuführenden Testarten, Testfälle und die erwarteten Ergebnisse dokumentiert sein. Außerdem SOLLTE der Abnahmeplan die Freigabekriterien beinhalten. Es SOLLTE die Vorgehensweise für die Ablehnung einer Freigabe definiert werden.

#### OPS.1.1.6.A11 Verwendung von anonymisierten oder pseudonymisierten Testdaten [Tester, Datenschutzbeauftragter]

Es SOLLTEN nur anonymisierte oder pseudonymisierte Testdaten für Software-Tests verwendet werden. Sofern die Produktivdaten einen Personenbezug aufweisen, SOLLTEN Institutionen ausschließlich anonymisierte Testdaten verwenden. Wenn ein Personenbezug von den Testdaten abgeleitet werden könnte, SOLLTEN der Datenschutzbeauftragte und unter Umständen die Personalvertretung hinzugezogen werden.

#### OPS.1.1.6.A12 Durchführung von Regressionstests [Tester]

Wenn Software-Tests nach einer Änderung der Software durchgeführt werden sollen, SOLLTEN Regressionstests durchgeführt werden. Regressionstests SOLLTEN vollständig durchgeführt werden. Die Auslassung von Testfällen SOLLTE begründet und dokumentiert werden. Die durchgeführten Testfälle und die Testergebnisse SOLLTEN dokumentiert werden.

#### OPS.1.1.6.A13 Trennung von Test- und Qualitätsmanagement-Umgebung von der Produktivumgebung [IT-Betrieb]

Software SOLLTE nur in einer hierfür vorgesehenen Test- und Qualitätsmanagement-Umgebung getestet werden. Die Test- und Qualitätsmanagement-Umgebungen SOLLTEN von der Produktivumgebung getrennt betrieben werden. Die in der Testlandschaft verwendeten Architekturen und Mechanismen SOLLTEN dokumentiert werden. Die Qualititätsmanagement-Umgebung SOLLTE der Produktivumgebung angepasst sein. Es SOLLTEN Verfahren dokumentiert werden, wie mit der Testlandschaft nach Abschluss des Software-Tests zu verfahren ist.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.1.6.A14 Durchführung von Penetrationstests [Tester](CIA)

Es SOLLTEN für Anwendungen beziehungsweise IT-Systeme mit erhöhtem Schutzbedarf Penetrationstests als Testmethode durchgeführt werden. Es SOLLTE ein Penetrationstest-Konzept erstellt werden. Im Penetrationstest-Konzept SOLLTEN neben den zu verwendeten Testmethoden auch die Erfolgskriterien dokumentiert werden.

Der Penetrationstest SOLLTE nach den Rahmenbedingungen des Penetrationstest-Konzepts erfolgen. Die durch den Penetrationstest aufgefundenen Sicherheitslücken SOLLTEN klassifiziert und dokumentiert sein.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Software-Tests und -Freigaben" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [29119] ISO/IEC 29119-2:2013-09

  

 Software and systems engineering - Software testing, ISO, 09.2013  
 [http://www.iso.org/iso/catalogue\_detail.htm?csnumber=56736](http://www.iso.org/iso/catalogue_detail.htm?csnumber=56736)

 
* #### [BSIPEN] BSI Studie "Durchführungskonzept für Penetrationstests

  

 Bundesamt für Sicherheit in der Informationstechnik, 11.2013  
 [https://www.bsi.bund.de/DE/Publikationen/Studien/Pentest/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/Pentest/index_htm.html)

 
* #### [BSIWEB] BSI-Leitfäden zur Entwicklung sicherer Webanwendungen

  

 Bundesamt für Sicherheit in der Informationstechnik, 2013  
 [https://www.bsi.bund.de/DE/Publikationen/Studien/Webanwendungen/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/Webanwendungen/index_htm.html)

 
* #### [CVSS] Common Vulnerability Scoring System

  

 CVSS, (zuletzt abgerufen am 28.09.2017)  
 <https://www.first.org/cvss>

 
* #### [GLEN] The Art of Software Testing

  

 Glenford J. Myers, Corey Sandler, Tom Badgett, Todd M. Thomas John Wiley & Sons, 2004 

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Software-Tests und -Freigaben" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

