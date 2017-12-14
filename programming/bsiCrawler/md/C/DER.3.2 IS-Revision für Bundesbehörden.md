1 Beschreibung
--------------

### 1.1 Einleitung

Im "Umsetzungsplan für die Gewährleistung der IT-Sicherheit in der Bundesverwaltung" (UP Bund) wird festgelegt, dass Bundesbehörden den IT-Grundschutz vollständig umsetzen müssen. Auch sind sie verpflichtet, mindestens alle 3 Jahre eine umfassende Informationssicherheitsrevision (IS-Revision) durchzuführen. Allerdings sind Behörden davon befreit, wenn sie ein ISO 27001-Zertifikat auf der Basis von IT-Grundschutz besitzen.

IS-Revisionen sind grundlegend für jedes erfolgreiche Informationssicherheitsmanagement. Nur wenn etablierte Sicherheitsmaßnahmen und -prozesse regelmäßig überprüft werden, ob sie wirksam, vollständig, angemessen und noch aktuell sind, lässt sich der Gesamtzustand der Informationssicherheit beurteilen. IS-Revisionen sind somit ein Werkzeug, um ein angemessenes Sicherheitsniveau festzustellen, zu erreichen und aufrechtzuerhalten. Durch sie ist es möglich, Fehlentwicklungen und bestehende Sicherheitsmängel zu erkennen und entsprechende Gegenmaßnahmen einzuleiten. 

### 1.2 Zielsetzung

Der Baustein definiert Anforderungen an die IS-Revision für Bundesbehörden mit dem Ziel, die Informationssicherheit in einer Behörde zu verbessern, Fehlentwicklungen auf diesem Gebiet zu vermeiden und die Sicherheitsmaßnahmen und -prozesse zu optimieren.

### 1.3 Abgrenzung

Der Baustein beschreibt, wie sich IS-Revisionen in Bundesbehörden anhand des "*Leitfadens für Informationssicherheitsrevision*" planen, durchführen und nachbereiten lassen. Der Baustein stellt jedoch nur die Pflichten im Rahmen der IS-Revision zusammen. Das für die IS-Revision verbindliche Regelwerk ist der "*Leitfaden für die Informationssicherheitsrevision*" in der jeweils aktuellen Version

Audits und Revisionen im Rahmen des Informationssicherheits-Managementsystems (ISMS) werden im Baustein DER.3.1 *Audit und Revision* betrachtet und sind somit nicht Bestandteil dieses Bausteins. Auch wird nicht berücksichtigt, wie sich die IS-Revision in eine bereits bestehende, übergeordnete Prüforganisation einer Behörde (zum Beispiel interne Revision) integrieren lässt. 

Der Baustein richtet sich insbesondere an Bundesbehörden. Grundsätzlich können die Inhalte jedoch auch für weitere Behörden (z. B. Landesbehörden), Unternehmen oder andere Organisationen relevant sein. Sofern diese nicht durch gesetzliche, vertragliche oder anderweitige Regelungen ebenfalls zur IS-Revision verpflichtet sind, sind die Inhalte des vorliegenden Bausteins als Empfehlungen anzusehen. Beispielsweise könnte eine IS-Revision im Sinne dieses Bausteins auch für andere Institutionen als Bundesbehörden für die Vorbereitung einer ISO 27001-Zertifizierung auf der Basis von IT-Grundschutz sinnvoll sein.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich *IS-Revision für Bundesbehörden* von besonderer Bedeutung:

### 2 1 Verstoß gegen die Vorgaben des UP Bund

Der UP Bund sieht unter anderem vor, dass sich alle Bundesbehörden, die noch keine vollumfängliche ISO 27001-Zertifizierung auf der Basis von IT-Grundschutz haben, einer regelmäßigen IS-Revision unterziehen. Führen Bundesbehörden nicht regelmäßig IS-Revisionen durch, verstoßen sie gegen diese Vorgaben.

### 2 2 Außer Kraft setzen von Sicherheitsmaßnahmen

Das Sicherheitsniveau einer Behörde hängt davon ab, dass Sicherheitsmaßnahmen vollständig und korrekt umgesetzt werden. Insbesondere in der kritischen Phase von Projekten oder unter bestimmten Rahmenbedingungen kann es vorkommen, dass Sicherheitsmaßnahmen temporär ausgesetzt werden. Teilweise wird jedoch vergessen, sie wieder zu reaktivieren, sodass ein zu niedriges Sicherheitsniveau entsteht. 

### 2 3 Wirkungslose oder nicht wirtschaftliche Umsetzung von Sicherheitsmaßnahmen

Werden Sicherheitsmaßnahmen umgesetzt, ohne dabei bestimmte Praxisaspekte zu berücksichtigen, sind die Maßnahmen eventuell wirkungslos. Beispielsweise ist es sinnlos, den Eingangsbereich mit Drehkreuzen abzusperren, wenn die Mitarbeiter das Gebäude einfach durch einen offenen Seiteneingang betreten können. 

Ebenso können Einzelmaßnahmen ergriffen werden, die wirtschaftlich nicht sinnvoll sind. So ist für den Schutz von Informationen mit einer normalen Vertraulichkeit ein sauber implementiertes Rechte- und Rollenkonzept sinnvoller und wirtschaftlicher als eine Certificate Authority und die anschließende zertifikatsbasierte Verschlüsselung des Fileservers aufzubauen.

### 2 4 Unzureichende Umsetzung des Informationssicherheitsmanagementsystems

In vielen Behörden überprüft der Informationssicherheitsbeauftragte selbst, ob Sicherheitsmaßnahmen umgesetzt wurden. Oft wird darüber die Prüfung des eigentlichen ISMS vergessen. Insbesondere da dies durch einen unabhängigen Dritten erfolgen sollte. Hierdurch besteht die Gefahr, dass die Prozesse eines ISMS ineffizient sind oder nicht angemessen umgesetzt wurden. In der Folge ist das Sicherheitsniveau der Institution beeinträchtigt.

### 2 5 Unzureichende Qualifikation des Prüfers

Ist ein IS-Revisor nicht ausreichend qualifiziert oder bereitet er sich ungenügend auf die Prüfungen vor, schätzt er während der IS-Revision eventuell den Sicherheitszustand einer Behörde falsch ein. Dadurch veranlasst er in seinem Prüfbericht nicht die nötigen oder sogar die falschen Korrekturmaßnahmen. Im schlimmsten Fall hat das eine zu hohe und damit nicht wirtschaftliche bzw. zu niedrige und damit sehr risikobehaftete Absicherung von Informationen zur Folge.

### 2 6 Fehlende langfristige Planung

Werden IS-Revisionen nicht langfristig und zentral geplant, kann es passieren, dass einzelne Bereiche einer Behörde sehr häufig und andere überhaupt nicht geprüft werden. Dadurch ist es nur sehr schwer oder gar nicht möglich, den Sicherheitszustand des Informationsverbunds einzuschätzen. 

### 2 7 Fehlende Planung und Abstimmung bei der Durchführung von IS-Revisionen

Wenn eine IS-Revision mangelhaft geplant und nicht mit allen betroffenen Mitarbeitern der Behörde abgestimmt wurde, sind während der Vor-Ort-Prüfung eventuell nicht die benötigten oder die falschen Ansprechpartner verfügbar. Dadurch lassen sich dann möglicherweise einzelne Bereiche überhaupt nicht prüfen. Auch wenn der IS-Revisor die Termine für die einzelnen Bereiche zu eng gesetzt hat, besteht die Gefahr, dass die geplante Untersuchung nur oberflächlich durchgeführt wird, da zu wenig Zeit verfügbar ist.

### 2 8 Fehlende Abstimmung mit der Personalvertretung

In IS-Revisionen können auch Aspekte geprüft werden, aus denen sich Rückschlüsse auf die Leistung von Mitarbeitern ziehen lassen. Somit könnten diese Prüfungen als Leistungsbeurteilung gewertet werden. Wird die Personalvertretung nicht beteiligt, kann dies zu Verstößen gegen das geltende Mitbestimmungsrecht führen. 

### 2 9 Absichtliches Verschweigen von Abweichungen oder Problemen

Mitarbeiter könnten befürchten, dass bei einer IS-Revison Fehler aufgedeckt werden, und darum versuchen, Sicherheitsprobleme zu kaschieren und ein falsches Bild über den tatsächlichen Status Quo zu vermitteln.

### 2 10 Vertraulichkeitsverlust von schützenswerten Informationen

Während einer IS-Revision werden diverse vertrauliche Informationen durch die Revisoren erhoben. Auch werden Defizite in der Informationssicherheit der geprüften Behörde benannt. Werden diese Mängel jedoch unberechtigten Dritten bekannt, könnten sie dazu benutzt werden, die Behörde anzugreifen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich IS-Revision für Bundesbehörden aufgeführt. Grundsätzlich ist der Verantwortliche für die IS-Revision für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### DER.3.2.A1 Definition von Verantwortlichkeiten für die IS-Revision

Die Institution MUSS einen Verantwortlichen benennen, der IS-Revisionen plant, initiiert und die Ergebnisse nachverfolgt.

#### DER.3.2.A2 Erstellung eines IS-Revisionshandbuches

Es MUSS ein IS-Revisionshandbuch erstellt werden. Das Handbuch MUSS von der Leitungsebene verabschiedet werden.

#### DER.3.2.A3 Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas [IS-Revisionsteam]

Die Prüfungsgrundlagen für die IS-Revision MÜSSEN der UP Bund, der Leitfaden für die Informationssicherheitsrevision, die BSI-Standards zur Informationssicherheit sowie das IT-Grundschutz-Kompendium sein. Dies MUSS zudem allen Beteiligten bekannt sein. Für die Bewertung der Maßnahmenumsetzung MUSS das Bewertungsschema aus *Informationssicherheitsrevision - Ein Leitfaden für die IS-Revision auf Basis von IT-Grundschutz* - benutzt werden (siehe 4. *Weiterführende Informationen*).

#### DER.3.2.A4 Erstellung einer Planung für die IS-Revision

Bundesbehörden, die noch keine ISO 27001-Zertifizierung auf der Basis von IT-Grundschutz haben, MÜSSEN mindestens alle 3 Jahre eine umfassende IS-Revision durchführen lassen. Darüber hinaus SOLLTEN weitere Revisionen für kritische Geschäftsprozesse eingeplant werden. Der Verantwortliche für die IS-Revision SOLLTE daher eine mehrjährige Grobplanung (sinnvollerweise über mindestens 3 Jahre) für das Revisionsvorhaben anhand des Leitfadens für die Informationssicherheitsrevision erstellen. Diese SOLLTE dann durch eine jährliche Detailplanung konkretisiert werden.

#### DER.3.2.A5 Auswahl eines geeigneten IS-Revisionsteams

Für IS-Revisionen MUSS ein geeignetes Team zusammengestellt oder beauftragt werden. Dem IS-Revisionsteam MUSS ein uneingeschränktes Informations- und Einsichtnahmerecht für seine Tätigkeit eingeräumt werden.

#### DER.3.2.A6 Vorbereitung einer IS-Revision [IS-Revisionsteam]

Die Behördenleitung MUSS das IS-Revisionsverfahren durch Auftragserteilung an das IS-Revisionsteam initiieren. 

Für die Dokumentenprüfung MUSS die zu prüfende Behörde die erforderlichen Referenzdokumente entsprechend dem Leitfaden für die Informationssicherheitsrevision an das IS-Revisionsteam übergeben.

#### DER.3.2.A7 Durchführung einer IS-Revision [IS-Revisionsteam]

Bei einer IS-Kurzrevision MUSS die verbindliche Prüfthemenliste aus *Verbindliche Prüfthemen für die IS-Kurzrevision* (siehe 4. *Weiterführende Informationen*) verwendet werden. Alle erstellten Grundlagen müssen während der IS-Revision fortgeschrieben und bei Bedarf angepasst werden.

Es MUSS im Rahmen einer IS-Revision sowohl eine Dokumentenprüfung als auch eine Inspektion vor Ort durchgeführt werden. Sämtliche Ergebnisse der beiden Phasen MÜSSEN schriftlich dokumentiert und in einem IS-Revisionsbericht zusammengefasst werden. 

#### DER.3.2.A8 Aufbewahrung von IS-Revisionsberichten

Der IS-Revisionsbericht und die diesem zugrunde liegenden Referenzdokumente MÜSSEN von der geprüften Behörde mindestens für 10 Jahre ab Zustellung des Berichts revisionssicher aufbewahrt werden, sofern keine anders lautenden Gesetze oder Verordnungen gelten. Hierbei MUSS sichergestellt werden, dass lediglich berechtige Personen auf die IS-Revisionsberichte und die Referenzdokumente zugreifen können.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich IS-Revision für Bundesbehörden. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.3.2.A9 Integration in den Informationssicherheitsprozess [Informationssicherheitsbeauftragter (ISB)]

Es SOLLTE sichergestellt werden, dass IS-Revisionen ein Teil des Sicherheitsprozesses sind und durch diesen initiiert werden. Außerdem SOLLTEN die Ergebnisse von IS-Revisionen in das ISMS zurückfließen und zu dessen Verbesserung beitragen.

Weiter SOLLTEN die IS-Revisionen, die Ergebnisse sowie die Aktivitäten zur Mängelbeseitigung und Qualitätsverbesserung in den regelmäßigen Bericht des ISB an die Behördenleitung aufgenommen werden.

#### DER.3.2.A10 Kommunikationsabsprache

Es SOLLTEN klare Regelungen getroffen werden, wie zwischen dem IS-Revisionsteam und der zu prüfenden Bundesbehörde Informationen auszutauschen sind. So SOLLTE durch geeignete Maßnahmen sichergestellt werden, dass die bei einer IS-Revision ausgetauschten Informationen auch vertraulich und integer bleiben. 

#### DER.3.2.A11 Durchführung eines Auftaktgeprächs für eine Querschnittsrevision [IS-Revisionsteam]

Für eine Querschnittsrevision SOLLTE zwischen dem IS-Revisionsteam und den Ansprechpartnern ein Auftaktgespräch durchgeführt werden. Darin SOLLTEN folgenden Inhalte besprochen werden:

* Erläuterung und Darstellung des IS-Revisionsverfahrens,
* Vorstellung der Institution: Erläuterung der Aufgabenschwerpunkte und Überblick über die eingesetzte IT,
* Übergabe der Referenzdokumente an das IS-Revisionsteam.
#### DER.3.2.A12 Erstellung eines Prüfplans [IS-Revisionsteam]

Vor einer IS-Revision SOLLTE das IS-Revisionsteam einen IS-Prüfplan erstellen, der den gesamten zeitlichen und organisatorischen Ablauf der Prüfung sowie alle zugehörigen Tätigkeiten und Regelungen koordiniert und beschreibt. Ist es während der IS-Revision notwendig, die geplanten Abläufe zu erweitern oder anderweitig anzupassen, SOLLTE der IS-Prüfplan entsprechend angepasst werden. Der Prüfplan SOLLTE zudem Teil des abschließenden IS-Revisionsberichts sein.

Bei der IS-Kurzrevision SOLLTE die verbindlich festgelegte Prüfthemenliste aus *Verbindliche Prüfthemen für die IS-Kurzrevision* (siehe 4. *Weiterführende Informationen*) an die Stelle des Prüfplans treten.

#### DER.3.2.A13 Sichtung und Prüfung der Dokumente [IS-Revisionsteam]

Die Dokumentenprüfung SOLLTE auf Basis der im Prüfplan festgelegten Maßnahmen erfolgen. Das IS-Revisionsteam SOLLTE überprüfen, ob alle relevanten Dokumente aktuell und vollständig sind. Bei der Prüfung der Aktualität SOLLTE die Granularität der Dokumente berücksichtigt werden. Bei der Prüfung der Vollständigkeit SOLLTE darauf geachtet werden, dass alle wesentlichen Aspekte erfasst wurden bzw. dass die geeigneten Rollen zugewiesen wurden.

Weiter SOLLTE geprüft werden, ob die vorliegenden Dokumente und die darin getroffenen Entscheidungen nachvollziehbar sind. Die Ergebnisse der Dokumentenprüfung SOLLTEN dokumentiert werden und soweit sinnvoll in die Vor-Ort-Prüfung einfließen.

#### DER.3.2.A14 Auswahl der Zielobjekte und Maßnahmen [IS-Revisionsteam]

In einer IS-Querschnittsrevision oder IS-Partialrevision SOLLTE das IS-Revisionsteam anhand der Ergebnisse der Dokumentenprüfung die Baustein-Zielobjekte für die Vor-Ort-Prüfung auswählen. Der Baustein zum Informationssicherheitsmanagement (siehe ISMS.1 *Sicherheitsmanagement*) einschließlich aller zugehörigen Anforderungen SOLLTE jedoch immer vollständig geprüft werden. Weitere Bausteinzielobjekte SOLLTEN risikoorientiert nach dem im *Leitfaden für die Informationssicherheitsrevision* definierten Verfahren ausgewählt werden. Die Auswahl SOLLTE nachvollziehbar schriftlich dokumentiert werden.

Darüber hinaus SOLLTEN bei der Auswahl die bemängelten Anforderungen aus vorhergehenden IS-Revisionen berücksichtigt werden. Alle Maßnahmen mit schwerwiegenden Sicherheitsmängeln aus vorhergehenden IS-Revisionen SOLLTEN berücksichtigt werden.

#### DER.3.2.A15 Auswahl von geeigneten Prüfmethoden [IS-Revisionsteam]

Es SOLLTE sichergestellt werden, dass geeignete Methoden eingesetzt werden, um die jeweiligen Sachverhalte zu ermitteln. Außerdem SOLLTEN grundsätzlich alle Prüfungen verhältnismäßig sein.

#### DER.3.2.A16 Ablaufplan der Vor-Ort-Prüfung [IS-Revisionsteam]

Gemeinsam mit dem Ansprechpartner der zu prüfenden Behörde SOLLTE das IS-Revisionsteam einen Ablaufplan für die Vor-Ort-Prüfung erarbeiten. Die Ergebnisse SOLLTEN im IS-Prüfplan dokumentiert werden.

#### DER.3.2.A17 Durchführung der Vor-Ort-Prüfung [IS-Revisionsteam]

Die Vor-Ort-Prüfung SOLLTE sicherstellen, dass durch die gewählten Maßnahmen die Informationssicherheit in angemessener und praxistauglicher Form gewährleistet wird. Die Prüfung SOLLTE mit einem Eröffnungsgespräch beginnen.

Danach SOLLTEN alle Maßnahmen des Prüfplans bzw. alle Themenfelder der Prüfthemenliste getestet werden. Dafür SOLLTEN, sofern sinnvoll, die vorgesehenen Prüfmethoden benutzt werden. Stellt das IS-Revisionsteam bei einer ausgewählten Stichprobe Abweichungen zum dokumentierten Status fest, SOLLTE die Stichprobe bedarfsorientiert erweitert werden, bis der Sachverhalt geklärt ist.

Während der Vor-Ort-Prüfung SOLLTEN die IS-Revisoren niemals selbst aktiv in Systeme eingreifen und auch keine Handlungsanweisungen zu Änderungen am Revisionsgegenstand erteilen. 

Alle wesentlichen Sachverhalte und Angaben über Quellen-, Auskunfts- und Vorlage-Ersuche sowie durchgeführte Besprechungen SOLLTEN schriftlich festgehalten werden.

Das IS-Revisionsteam SOLLTE den Ansprechpartnern der geprüften Behörde die getroffenen Feststellungen in einem Abschlussgespräch kurz darstellen. Dabei SOLLTE keine konkrete Bewertung erfolgen, aber ein Hinweis auf etwaige Mängel und den weiteren Verfahrensgang. Auch dieses Abschlussgespräch ist zu protokollieren. 

#### DER.3.2.A18 Durchführung von Interviews [IS-Revisionsteam]

Interviews SOLLTEN strukturiert erfolgen. Fragen SOLLTEN knapp, präzise und leicht verständlich formuliert werden. Zudem SOLLTEN geeignete Fragetechniken eingesetzt werden.

#### DER.3.2.A19 Überprüfung des Risikobehandlungsplans [IS-Revisionsteam]

Das IS-Revisionsteam SOLLTE prüfen, ob die verbleibenden Restrisiken für den Informationsverbund angemessen und tragbar sind und verbindlich durch die Behördenleitung getragen werden. Maßnahmen, die grundlegend zur Informationssicherheit der gesamten Bundesbehörde beitragen, DÜRFEN NICHT in die Risikoübernahme einfließen.

Das IS-Revisionsteam SOLLTE stichprobenartig verifizieren, ob bzw. wie weit die im Risikobehandlungsplan festgelegten Maßnahmen umgesetzt sind.

#### DER.3.2.A20 Nachbereitung der Vor-Ort-Prüfung [IS-Revisionsteam]

Nach der Vor-Ort-Prüfung SOLLTEN die erhobenen Informationen weiter konsolidiert und ausgewertet werden. Nachdem die eventuell nachgeforderten Dokumentationen und zusätzlichen Informationen ausgewertet wurden, SOLLTEN die geprüften Maßnahmen endgültig bewertet werden. 

Um die nachgeforderten Dokumentationen bereitzustellen, SOLLTE ein ausreichendes Zeitfenster gewährt werden. Dokumente, die bis zum vereinbarten Enddatum nicht eingegangen sind, SOLLTEN als nicht existent gewertet werden.

#### DER.3.2.A21 Erstellung eines IS-Revisionsberichts [IS-Revisionsteam]

Das IS-Revisionsteam SOLLTE die gewonnenen Ergebnisse in einen IS-Revisionsbericht überführen und dort nachvollziehbar dokumentieren.

Eine Entwurfsversion des Berichts SOLLTE der geprüften Bundesbehörde vorab übermittelt werden, um zu verifizieren, ob die durch das Prüfteam festgestellten Sachverhalte richtig aufgenommen wurden. Es SOLLTE überlegt werden, dass das IS-Revisionsteam den Verantwortlichen die Ergebnisse der IS-Revision in einer Präsentation erläutert.

Die geprüfte Bundesbehörde SOLLTE sicherstellen, dass alle betroffenen Stellen in der Bundesbehörde innerhalb einer angemessenen Frist die für sie wichtigen und notwendigen Passagen des IS-Revisionsberichts erhalten. Insbesondere SOLLTEN die Inhalte an die Behördenleitung, an den Verantwortlichen für die IS-Revision sowie den ISB kommuniziert werden.

IS-Revisionsberichte SOLLTEN mindestens als Verschlusssache "Nur für den Dienstgebrauch" (VS-NfD) eingestuft werden.

#### DER.3.2.A22 Nachbereitung und Einleitung des Follow-up [Informationssicherheitsbeauftragter (ISB)]

Die im IS-Revisionsbericht festgestellten Abweichungen SOLLTEN in einer angemessenen Zeit abgestellt werden. Die durchzuführenden Korrekturmaßnahmen SOLLTEN mit Zuständigkeiten, Umsetzungstermin und dem jeweiligen Status dokumentiert sein. Die Umsetzung SOLLTE kontinuierlich nachverfolgt und der Umsetzungsstatus fortgeschrieben werden.

Grundsätzlich SOLLTE geprüft werden, ob ergänzende IS-Revisionen notwendig sind. Der Verantwortliche für die IS-Revision SOLLTE die Grob- und Detailplanung zur IS-Revision anpassen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.3.2.A23 Sicherheitsüberprüfung der IS-Revisoren(CI)

Sofern die IS-Revisoren auf besonders schützenswerte Informationen zugreifen, SOLLTEN Nachweise über ihre Integrität und Reputation eingefordert werden, zum Beispiel ein polizeiliches Führungszeugnis oder Referenzen.

Handelt es sich dabei um nach Geheimschutz klassifizierte Verschlusssachen, SOLLTEN sich die IS-Revisoren einer Sicherheitsüberprüfung nach Sicherheitsüberprüfungsgesetz (SÜG) unterziehen. Diesbezüglich SOLLTE der ISB den Geheimschutzbeauftragten bzw. Sicherheitsbevollmächtigten seiner Behörde einbeziehen.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "IS-Revision für Bundesbehörden" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISKR] Verbindliche Prüfthemen für die IS-Kurzrevision

  

 BSI, Version 1.1, 11.2010  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Pruefthemen\_IS-Kurzrevision\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Pruefthemen_IS-Kurzrevision_pdf.pdf)

 
* #### [ISR] Informationssicherheitsrevision

  

 Ein Leitfaden für die IS-Revision auf Basis von IT-Grundschutz, BSI, Version 2.0, 03.2010  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Leitfaden\_IS-Revision-v1\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Leitfaden_IS-Revision-v1_pdf.pdf)

 
* #### [RH] Revisionshandbuch zur Informationssicherheit nach UP Bund (Muster)

  

 BSI, Version 1.0, 09.2008  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Muster\_ISRevisionshandbuch-v1\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Muster_ISRevisionshandbuch-v1_pdf.pdf)

 
* #### [VSA] Allgemeine Verwaltungsvorschrift des Bundesministerium des Inneren zum materiellen und organisatorischen Schutz von Verschlußsachen

  

 (VS-Anweisung - VSA), 31.03.2006 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "IS-Revision für Bundesbehörden" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

