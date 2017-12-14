1 Beschreibung
--------------

### 1.1 Einleitung

Unter Standardsoftware wird Software verstanden, die auf dem Markt angeboten und meistens über den Fachhandel bezogen wird, zum Beispiel über Kataloge oder Onlineportale. Sie zeichnet sich dadurch aus, dass sie der Anwender selbst installieren und mit wenig Aufwand anpassen kann.

In diesen Umsetzungshinweisen zum entsprechenden Baustein wird dargestellt, wie Institutionen unter Sicherheitsgesichtspunkten mit Standardsoftware umgehen sollten. So müssen Institution einen Anforderungskatalog für Standardsoftware erstellen, ein geeignetes Produkt auswählen, es sicher installieren, die Lizenzen geeignet verwalten und das Produkt auch wieder sicher deinstallieren können.

### 1.2 Lebenszyklus

**Planung und Konzeption** 

In der Planungs- und Konzeptionsphase sollte ein für die Beschaffung der Standardsoftware verantwortlicher Mitarbeiter benannt werden (siehe CON.4.M4 *Festlegung der Verantwortlichkeiten im Bereich Standardsoftware*). Die Anforderungen an die zu beschaffende Standardsoftware sollten analysiert und in einem Anforderungskatalog festgehalten werden (CON.4.M5 *Erstellung eines Anforderungskatalogs für Standardsoftware*). Danach kann ein geeignetes Produkt ausgewählt werden (CON.4.M6 *Auswahl eines geeigneten Softwareproduktes*). Bei erhöhtem Schutzbedarf sollte zusätzlich entschieden werden, ob und wie eine zu beschaffende Anwendung zertifiziert sein sollte, um ein gewisses Sicherheitsniveau nachzuweisen (siehe CON.4.M11 *Nutzung zertifizierter Standardsoftware*). 

**Beschaffung** 

Bei der Beschaffung von Standardsoftware sollte definiert werden, wie mit deren Lieferungen verfahren wird. So sollte bei jeder Lieferung überprüft werden, ob sie vollständig ist (siehe CON.M7 *Überprüfung der Lieferung von Standardsoftware*). 

**Umsetzung** 

Vor dem Einsatz von Standardsoftware sollte sichergestellt werden, dass die Integrität der Installationssoftware gewährleistet ist (siehe CON.4.M1 *Sicherstellen der Integrität von Standardsoftware*). Darüber hinaus sollte Standardsoftware sicher installiert und danach konfiguriert werden (siehe CON.4.M3 *Sichere Installation und Konfiguration von Standardsoftware*). Für jede Anwendung ist außerdem eine Installationsanweisung zu erstellen (siehe CON.4.M2 *Entwicklung der Installationsanweisung für Standardsoftware*). 

**Betrieb** 

Es sollte sichergestellt werden, dass ausschließlich lizenzierte Standardsoftware eingesetzt wird (siehe CON.4.M8 *Lizenzverwaltung und Versionskontrolle von Standardsoftware*). Bei erhöhtem Schutzbedarf sollten gegebenenfalls ergänzende Sicherheitsfunktionen implementiert werden (siehe CON.4.M10 *Implementierung zusätzlicher Sicherheitsfunktionen*). Auch sollten dann Verschlüsselung, Checksummen oder digitale Signaturen eingesetzt werden (siehe CON.4.M12 *Einsatz von Verschlüsselung, Checksummen oder digitalen Signaturen*).

**Aussonderung** 

Wenn Standardsoftware deinstalliert wird, sollte dafür gesorgt werden, dass alle (System-)Dateien der Anwendung gelöscht werden (siehe CON.4.M9 *Deinstallation von Standardsoftware*). 

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Auswahl und Einsatz von Standardsoftware" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### CON.4.M1 Sicherstellen der Integrität von Standardsoftware

Es ist sicherzustellen, dass freigegebene Standardsoftware nur vom Originaldatenträgern oder von geprüften identischen Kopien des originalen Installationsprogramms installiert wird. Damit soll verhindert werden, dass gewollte oder ungewollte Veränderungen vorgenommen werden können, z. B. durch Malware, Bitfehler aufgrund technischer Fehler oder manipulierten Konfigurationsdateien.

Die Installation darf daher ausschließlich von Originaldatenträgern bzw. geprüften identischen Kopien des originalen Installationsprogramms erfolgen. Alternativ kann eine freigegebene Version über ein lokales Netz installiert werden. Dabei sollte sichergestellt sein, dass nur berechtigte Personen darauf zugreifen können.

Von den Originaldatenträgern sollten Sicherungskopien angefertigt und geprüft werden. Originaldatenträger und alle Kopien müssen vor unberechtigtem Zugriff geschützt aufbewahrt werden. Die angefertigten Kopien sollten nummeriert und in Bestandsverzeichnisse aufgenommen werden. Kopien, die nicht mehr benötigt werden, sollten gelöscht oder vernichtet werden. Auch Originaldatenträger und originale Installationsprogramme müssen vor der ersten Verwendung auf Schadprogramme geprüft werden.

Optional kann über die Originaldatenträger oder über eine während des Tests installierte Referenzversion eine Checksumme gebildet werden. Anhand dieser kann vor der Installation die Integrität der dafür eingesetzten Datenträger bzw. der in lokalen Netzen hinterlegten Versionen oder die korrekte Installation überprüft werden. Darüber hinaus können installierte Programme zusätzlich zum Schutz vor unberechtigten Veränderungen der freigegebenen Konfiguration mit Checksummen versehen werden. Auf diese Weise können auch Infektionen mit bisher unbekannter Schadsoftware erkannt werden. So kann auch festgestellt werden, ob eine Vireninfektion vor oder nach der Installation stattgefunden hat.

#### CON.4.M2 Entwicklung der Installationsanweisung für Standardsoftware

Nachdem sich die Institution für ein Produkt entschieden hat, muss dafür eine Installationsanweisung erstellt werden. Während des Testens wurde diejenige Konfiguration des Produktes ermittelt, die einen sicheren und effizienten Produktionsbetrieb erlaubt (siehe CON.4.M6 *Auswahl einer geeigneten Standardsoftware*). Damit sollte sichergestellt werden, dass die Software benutzerfreundlich, ordnungsmäßig und sicher am Arbeitsplatz funktioniert.

Um die geeignete Konfiguration des Produktes im Produktivbetrieb sicherzustellen, müssen bestimmte Parameter vorgegeben werden. Teilweise muss dies durch organisatorische Regelungen begleitet werden.

Für einige Eigenschaften eines Produktes wird im folgenden beispielhaft aufgezeigt, was in einer Installationsanweisung vorgegeben werden kann.

**Beispiel:** 

Benutzerfreundlichkeit:

* Mit dem Produkt sind die jeweiligen Treiber zu installieren, um eine für den Benutzer akzeptable Arbeitsumgebung zu schaffen, z. B. Bildschirm flimmerfrei, genügende Druckaufbereitung. 
* Einstellungen, bei denen die Funktionen die größte Verarbeitungsgeschwindigkeit haben, sind vorzuziehen, wenn nicht andere Kriterien wie Sicherheit dagegen sprechen (Beispiel: eine Datensicherung sollte verifiziert werden, obwohl die Verifikation zusätzlichen Zeitaufwand erfordert). 
Sicherheit:

* Die Parameter für Sicherheitsfunktionen sind voreinzustellen, z. B. die Mindestlänge von Passwörtern oder die tägliche Erstellung von Datensicherungen. 
* Werden mehrere sicherheitsrelevante Verfahren unterstützt (z. B. Verschlüsselungsalgorithmus, Hash-Funktionen), sind diejenigen auszuwählen, mit denen ein angemessenes Schutzniveau erreicht wird. 
Funktion:

* Nur die benötigten Programmfunktionen sind zu aktivieren, unerwünschte oder nicht benötigte Funktionen sind abzuschalten. 
* Die Funktion zur automatischen Speicherung ist mit dem Parameter "alle x Minuten" zu aktivieren. 
Organisation:

* Ausschließlich ein Administrator darf die Software installieren. 
* Es müssen Regelungen für den Betrieb erlassen werden, z. B. Datensicherungen sind eigenverantwortlich vom Benutzer durchzuführen, Passwörter müssen nach x Tagen gewechselt werden. 
Randbedingungen:

* Die Konfiguration der Plattform, auf der das Standardsoftwareprodukt eingesetzt werden soll, muss insbesondere dann beschrieben und vorgegeben werden, wenn systembedingte Schwachstellen der Plattform damit beseitigt werden. 
#### CON.4.M3 Sichere Installation und Konfiguration von Standardsoftware

Die Standardsoftware sollte entsprechend der Installationsanweisung (siehe CON.4.M2 *Entwicklung der Installationsanweisungen für Standardsoftware*) auf den vorgesehenen IT-Systemen installiert werden. Die Installationsanweisung beinhaltet neben den zu installierenden Programmen auch Konfigurationsparameter und die Einrichtung der Hardware- und Softwareumgebung.

Abweichungen von der Installationsanweisung müssen vom Vorgesetzten bzw. vom Mitarbeiter, der für den Freigabeprozess verantwortlich ist, genehmigt werden. 

Da Standardsoftware für viele Einsatzfelder entwickelt wird, enthält sie meist mehr Funktionen als für die Fachaufgaben benötigt werden. Damit es zu weniger Problemen und Fehlern kommt, dürfen nur die tatsächlich benötigten Funktionen installiert werden. Funktionen, die zu Sicherheitsproblemen führen können, dürfen nicht freigegeben werden.

Sowohl vor als auch nach der Installation von Software sollte eine vollständige Datensicherung durchgeführt werden. Die erste Datensicherung kann benutzt werden, wenn es während der Installation zu Fehlern kommt. Mit der zweiten Datensicherung lässt sich bei späteren Problemen der Zustand nach der erfolgreichen Installation des Produktes wiederherstellen.

Die erfolgreiche Installation muss an die zuständige Stelle für den Produktivbetrieb gemeldet werden.

Beim Einsatz eines neuen Produktes müssen eventuell Datenbestände migriert werden, die mit einem Vorgängerprodukt erzeugt wurden. Hat sich bei den Tests gezeigt, dass es dabei zu Schwierigkeiten kommen kann, sind Hilfestellungen für die Benutzer zu erarbeiten. Alternativ kann auch geschultes Personal die alten Datenbestände zentral migrieren. 

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Auswahl und Einsatz von Standardsoftware".

#### CON.4.M4 Festlegung der Verantwortlichkeiten im Bereich Standardsoftware [Fachabteilung]

Vor der Einführung von Standardsoftware müssen eine Reihe von Verantwortlichkeiten geregelt werden, z. B.:

* Wer erstellt einen Anforderungskatalog? 
* Wer wählt Produkte aus? 
* Wer testet? Wer ist für die Freigabe zuständig? 
* Wer installiert die Software? 
Nachfolgend wird aufgezeigt, wie sich diese Verantwortlichkeiten sinnvoll verteilen lassen. Da jedoch die Bezeichnungen in den meisten Institutionen voneinander abweichen, werden vorab einige Instanzen anhand ihrer Aufgaben definiert, denen anschließend die einzelnen Verantwortlichkeiten zugeordnet werden können:

* Der Fachbereich ist der Anwender der Standardsoftware. Er äußert den Bedarf an neuer Software und stößt damit den Beschaffungsprozess an. Er wird bei Vorauswahl und Test beteiligt, um die Anforderungen der Benutzer einzubringen. 
* Die Leitung der Institution ist dafür verantwortlich, Standardsoftware freizugeben. Diese Verantwortung wird meist an den Leiter der Fachabteilung delegiert. Damit geht nach der Freigabe die Verantwortung für den korrekten Einsatz der Standardsoftware auf die Fachabteilung über. 
* Der IT-Bereich hat die Aufgabe, IT-Lösungen bereitzustellen, mit denen die Fachabteilungen ihre Aufgaben erfüllen können. Außerdem muss er den sicheren und zuverlässigen Betrieb der IT gewährleisten. 
* Die Beschaffungsstelle muss sicherstellen, dass die Standardsoftware interoperabel und kompatibel ist. Auch muss sie dafür sorgen, dass Hausstandards und gesetzliche Vorschriften eingehalten werden. Oft gibt es in den einzelnen Fachabteilungen IT-Koordinatoren, die Teile der Aufgaben der Beschaffungsstelle für die Fachabteilung beratend wahrnehmen und eventuell auch die Haushaltsmittel der Fachabteilung koordinieren. 
* Der Haushalt ist verantwortlich für das Rechnungswesen, die IT-Budgetverwaltung und für die Bereitstellung der benötigten Haushaltsmittel. 
* Der IT-Sicherheitsbeauftragte muss überprüfen, ob mit den eingesetzten oder zu beschaffenden Produkten ein angemessenes Sicherheitsniveau gewährleistet werden kann. Im Rahmen des Sicherheitsmanagements muss er die Informationssicherheit im laufenden Betrieb sicherstellen. 
* Der Datenschutzbeauftragte muss sicherstellen, dass die datenschutzrechtlichen Bestimmungen eingehalten werden und personenbezogene Daten ausreichend geschützt sind. 
* Der Personal- bzw. Betriebsrat muss in vielen Fällen bei der Auswahl neuer Standardsoftware beteiligt werden, insbesondere wenn damit größere Änderungen im Arbeitsablauf verbunden sind oder wenn die zu beschaffende Software zur Leistungskontrolle geeignet ist. 
Im Gesamtprozess „Standardsoftware“ muss für jeden einzelnen Schritt festgelegt werden, welche der zuvor beschriebenen Instanzen für die Durchführung verantwortlich sind und welche Instanzen dabei beteiligt werden müssen. Die nachfolgende Tabelle zeigt, wie Verantwortung sinnvoll verteilt werden kann. 

Die getroffenen Zuordnungen sind verbindlich festzuschreiben und es ist regelmäßig zu kontrollieren, ob sie eingehalten werden.

#### CON.4.M5 Erstellung eines Anforderungskatalogs für Standardsoftware [Fachabteilung]

Der Markt bietet meist viele gleichartige Standardsoftwareprodukte an. In ihrer Grundfunktion vergleichbar, unterscheiden sie sich jedoch in Kriterien wie Anschaffungs- und Betriebskosten, Zusatzfunktionen, Kompatibilität, Administration, Ergonomie und Informationssicherheit.

**Anforderungskatalog** 

Für die Auswahl eines geeigneten Produktes sollte daher zunächst ein Anforderungskatalog erstellt werden, der z. B. Aussagen zu den folgenden Punkten Aussagen enthalten kann:

* Funktionale Anforderungen, die das Produkt erfüllen muss, um die Fachabteilung geeignet zu unterstützen. Die für die Fachaufgabe relevanten Funktionen sollten hervorgehoben werden. Beispiel: 

 
	+ Textverarbeitung mit den Zusatzfunktionen: Einbinden von Grafiken, Makro-Programmierung, Rechtschreibprüfung und Silbentrennung. Makro-Programmierung muss abschaltbar sein, Rechtschreibprüfung muss in Englisch, Französisch und Deutsch verfügbar sein. Die spezifizierten Textformate müssen im- und exportiert werden können.
	  

 
* IT-Einsatzumgebung: Diese wird einerseits beschrieben durch die Rahmenbedingungen, die durch die vorhandene oder geplante IT-Einsatzumgebung vorgegeben werden, und andererseits durch die Leistungsanforderungen, die das Produkt an die Einsatzumgebung stellt. Beispiel: 

 
	+ Erforderliche IT-Einsatzumgebung und Leistungsanforderungen: Betriebssystem, Prozessor, Hauptspeicher, Festplattenkapazität, Schnittstellen für externe Datenträger und für Vernetzung.
	  

 
* Kompatibilitätsanforderungen zu anderen Programmen oder IT-Systemen, also Migrationsunterstützung und Aufwärts- und Abwärtskompatibilität. Beispiel: 

 
	+ Die Funktionen A, B, C müssen bei Versionswechseln erhalten bleiben.
	  

 
* Performance-Anforderungen beschreiben die erforderlichen Leistungen hinsichtlich Durchsatz und Laufzeitverhalten. Für die geforderten Funktionen sollten möglichst genaue Angaben über die maximal zulässige Bearbeitungszeit getroffen werden.Beispiel: 

 
	+ Andere gleichzeitig verarbeitete Prozesse dürfen durch das Produkt maximal um 30 % verlangsamt werden.
	  

 
* Interoperabilitätsanforderungen, d. h. die Zusammenarbeit mit anderen Produkten über Plattformgrenzen hinweg muss möglich sein. Beispiel: 

 
	+ Ein Textverarbeitungsprogramm sollte für Windows-, Unix- und macOS-Plattformen verfügbar sein. Dokumente sollen auf einem Betriebssystem erstellt und auf einem anderen weiterverarbeitet werden können.
	  

 
* Zuverlässigkeitsanforderungen betreffen die Stabilität des Produktes, also Fehlererkennung und Toleranz sowie Ausfall- und Betriebssicherheit.Beispiel: 

 
	+ Fehleingaben des Benutzers müssen erkannt werden und dürfen nicht zum Programmabbruch oder Systemabsturz führen.
	  

 
* Konformität zu Standards, das können internationale Normen, De-facto-Standards oder auch Hausstandards sein. Beispiel: 

 
	+ Das Produkt muss der EU-Bildschirmrichtlinie 90/270/EWG entsprechen.
	  

 
* Einhaltung von internen Regelungen und gesetzlichen Vorschriften. Beispiel: 

 
	+ Da personenbezogene Daten verarbeitet werden, müssen die Bestimmungen des Bundesdatenschutzgesetzes mit den verfügbaren Funktionen erfüllt werden können.
	  

 
* Anforderungen an die Benutzerfreundlichkeit, die durch die leichte Bedienbarkeit, Verständlichkeit und Erlernbarkeit gekennzeichnet ist, also insbesondere durch die Güte der Benutzeroberfläche sowie die Qualität der Benutzerdokumentation und der Hilfefunktionen. Beispiel: 

 
	+ Die Benutzeroberfläche muss so gestaltet sein, dass ungelernte Kräfte innerhalb von zwei Stunden in die Benutzung eingewiesen werden können.
	  

 
* Anforderungen an die Wartung ergeben sich für den Anwender hauptsächlich aus der Fehlerbehandlung des Produktes.Beispiel: 

 
	+ Der Administrationsaufwand darf X Stunden pro Monat nicht überschreiten.
	  

 
* Die Obergrenze für Kosten. Dabei müssen nicht nur die unmittelbaren Beschaffungskosten für das Produkt selber einbezogen werden, sondern auch Folgekosten, wie z. B. eine Aufrüstung der Hardware, Personalkosten oder notwendige Schulungen. 
* Aus den Anforderungen an die Dokumentation muss hervorgehen, welche Dokumente in welcher Güte (Vollständigkeit, Verständlichkeit) erforderlich sind.Beispiele: 

 
	+ Die Benutzerdokumentation muss leicht nachvollziehbar und zum Selbststudium geeignet sein. Die gesamte Funktionalität des Produktes ist zu beschreiben.
	  

 
* Bezüglich der Softwarequalität können Anforderungen gestellt werden, die von Herstellererklärungen zum eingesetzten Qualitätssicherungsverfahren, über ISO 9000 ff. Zertifikate bis hin zu unabhängigen Softwareprüfungen nach ISO/IEC 25051 reichen. Beispiel: 

 
	+ Der Software-Herstellungsprozess des Herstellers muss nach ISO 9001 zertifiziert sein.
	  

 
* Sollen durch das Produkt selbst Sicherheitsaufgaben erfüllt werden, sind diese in Form von Sicherheitsanforderungen zu formulieren. Dies wird im Folgenden erläutert. 
**Sicherheitsanforderungen** 

Typische Sicherheitsanforderungen, die ein Produkt erfüllen kann, werden im Folgenden kurz erläutert. Weitere Ausführungen dazu sind in den Common Criteria (CC) zu finden.

* Identifizierung und Authentisierung: Zu vielen Produkten wird es Anforderungen geben, diejenigen Benutzer zu bestimmen und zu überwachen, die Zugriff auf das Produkt haben. Dazu muss nicht nur die Identität des Benutzers überprüft, sondern auch nachgeprüft werden, ob der Benutzer tatsächlich die Person ist, die er zu sein vorgibt. Das geschieht, indem der Benutzer dem Produkt Informationen liefert, die fest mit dem betreffenden Benutzer verknüpft sind. 
* Zugriffskontrolle: Bei vielen Produkten wird es erforderlich sein, sicherzustellen, dass Benutzer daran gehindert werden, auf Informationen zuzugreifen, für die sie kein Zugriffsrecht haben oder auf die sie nicht zugreifen sollen. Weiterhin wird es eventuell erforderlich sein, zu verhindern, dass Benutzer unbefugt Informationen erzeugen, ändern oder löschen. 
* Beweissicherung: Bei vielen Produkten muss sichergestellt werden, dass die Handlungen der Benutzer aufgezeichnet werden. So können die Folgen später dem betreffenden Benutzer zugeordnet werden und der Benutzer kann für seine Handlungen verantwortlich gemacht werden. 
* Protokollauswertung: Bei vielen Produkten wird sicherzustellen sein, dass sowohl über gewöhnliche Vorgänge als auch über außergewöhnliche Vorfälle ausreichend Informationen aufgezeichnet werden, damit später festgestellt werden kann, ob tatsächlich Sicherheitsverletzungen vorgelegen haben und welche Informationen oder sonstigen Betriebsmittel davon betroffen waren. 
* Unverfälschbarkeit: Bei vielen Produkten wird es erforderlich sein, sicherzustellen, dass bestimmte Beziehungen zwischen unterschiedlichen Daten korrekt bleiben und dass Daten zwischen einzelnen Prozessen ohne Änderungen übertragen werden. Daneben müssen auch Funktionen bereitgestellt werden, die es bei der Übertragung von Daten zwischen einzelnen Prozessen, Benutzern und Objekten ermöglichen, Verluste, Ergänzungen oder Veränderungen zu entdecken bzw. zu verhindern, und die es unmöglich machen, die angebliche oder tatsächliche Herkunft bzw. Bestimmung der Datenübertragung zu ändern. 
* Zuverlässigkeit: Bei vielen Produkten wird es erforderlich sein, sicherzustellen, dass zeitkritische Aufgaben genau zu dem Zeitpunkt durchgeführt werden, zu dem es erforderlich ist, also nicht früher oder später. Auch wird sicherzustellen sein, dass zeitunkritische Aufgaben nicht in zeitkritische umgewandelt werden können. Desgleichen wird es bei vielen Produkten erforderlich sein sicherzustellen, dass ein Zugriff im erforderlichen Moment möglich ist und Betriebsmittel nicht unnötig angefordert oder zurückgehalten werden. 
* Übertragungssicherheit: Dieser Begriff umfasst alle Funktionen, die für den Schutz der Daten während der Übertragung über Kommunikationskanäle vorgesehen sind: Authentisierung, Zugriffskontrolle, Datenvertraulichkeit, Datenintegrität, Sende- und Empfangsnachweis. Einige dieser Funktionen werden mittels kryptografischer Verfahren realisiert. 
Darüber hinaus können weitere Sicherheitsanforderungen an Standardsoftware konkretisiert werden.

* Datensicherung: An die Verfügbarkeit der mit dem Produkt verarbeiteten Daten werden besondere Anforderungen gestellt. Darunter fallen im Produkt integrierte Funktionen, die Datenverlusten vorbeugen sollen, z. B. die automatische Speicherung von Zwischenergebnissen oder die automatische Erstellung von Sicherungskopien, bevor größere Änderungen durchgeführt werden. 
* Verschlüsselung: Bei vielen Produkten wird es erforderlich sein, Nutzdaten vor einer Übertragung oder nach der Bearbeitung zu verschlüsseln und sie nach Empfang oder vor der Weiterverarbeitung wieder zu entschlüsseln. Hierzu ist ein anerkanntes Verschlüsselungsverfahren zu verwenden. Es ist sicherzustellen, dass die zur Entschlüsselung benötigten Parameter (z. B. Schlüssel) geeignet geschützt sind. 
* Funktionen zur Wahrung der Datenintegrität: Für Daten, deren Integritätsverlust zu Schäden führen kann, können Funktionen eingesetzt werden, die Fehler erkennen lassen oder mittels Redundanz korrigieren können. Meist werden Verfahren zur Integritätsprüfung eingesetzt, die zuverlässig aufdecken können, ob ein Produkt oder die damit erstellten Daten absichtlich manipuliert oder Daten unbefugt wieder eingespielt wurden. 
* Datenschutzrechtliche Anforderungen: Wenn mit dem Produkt personenbezogene Daten verarbeitet werden sollen, sind über die genannten Sicherheitsfunktionen hinaus zusätzliche spezielle technische Anforderungen zu stellen, um den Datenschutzbestimmungen genügen zu können. 
Sicherheitsfunktionen werden durch Mechanismen umgesetzt. Je nach Einsatzzweck müssen diese Mechanismen eine unterschiedliche Stärke besitzen, mit der sie Angriffe abwehren können. Die erforderliche Stärke der Mechanismen ist im Anforderungskatalog anzugeben. Bei Anwendung der Common Criteria (CC) wird die Angriffsresistenz eines IT-Produktes bewertet, das in einer bestimmten Einsatzumgebung betrieben wird. Kriterien für die Bewertung sind die in den Sicherheitsvorgaben oder in einem Schutzprofil definierten Bedrohungen der zu schützenden Datenobjekte. Die geforderte Prüftiefe beinhaltet die Festlegung der Angriffsresistenz und richtet sich nach dem Schutzbedarf und dem Einsatzzweck des Produktes. Die Prüftiefe wird anhand eines Kataloges (siehe CC, Teil 3) meist mittels vordefinierter Evaluierungsstufen (EAL 1 bis 7) festgelegt.

Für die Bewertung der Angriffsresistenz werden die für das Einsatzszenario relevanten Angriffe nach dem Stand der Technik bis zu einer bestimmten Stärke unter Berücksichtigung der erforderlichen Angriffszeit, technischen Expertise des Angreifers, Kenntnissen über das Produkt, Gelegenheit zum Angriff und benötigten Hilfsmittel analysiert. Die Bestätigung der Angriffsresistenz im Rahmen der Zertifizierung erfolgt dabei dann in den Abstufungen niedrig (basic), erweitert (enhanced basic), mittel (moderate) und hoch (high). Basic bedeutet Schutz gegen öffentlich bekannte Angriffe und gegen Angreifer mit sehr begrenzten Fähigkeiten und Möglichkeiten. Hoch bedeutet, dass ein erfolgreicher Angriff sehr gute Fachkenntnisse, Produktkenntnisse, Gelegenheiten und Betriebsmittel erfordert, und damit insgesamt als extrem aufwändig gilt.

#### CON.4.M6 Auswahl einer geeigneten Standardsoftware [Fachabteilung, Beschaffungsstelle]

Um ein geeignetes Softwareprodukt auswählen zu können, muss die IT-Abteilung in Zusammenarbeit mit der Beschaffungsstelle zuerst anhand des Anforderungskatalogs (siehe CON.4.M5 *Erstellung eines Anforderungskatalogs für Standardsoftware*) eine Marktanalyse durchführen und diese möglichst tabellarisch aufbereiten. In dieser Tabelle müssen für die infrage kommenden Produkte Aussagen zu den im Anforderungskatalog festgehaltenen Punkten gemacht werden.

Die Marktübersicht sollte mithilfe von Produktbeschreibungen, Herstelleraussagen, Fachzeitschriften oder Händlerauskünften erstellt werden. Alternativ ist eine Ausschreibung möglich und in einigen Fällen vorgegeben. Die Grundlage dafür ist der Anforderungskatalog, sodass anhand der eingehenden Angebote eine vergleichbare Marktübersicht erstellt werden kann.

Anschließend müssen die in der Marktübersicht erfassten Produkte bewertet werden. Hierzu sollte eine Bewertungsskala erarbeitet werden. Anhand der vorliegenden Informationen wird nun festgestellt, welche der geforderten Eigenschaften das Produkt aufweist. Fehlen zwingend notwendige Eigenschaften, muss es verworfen werden. Über die Bewertung der einzelnen Eigenschaften jedes Produktes wird eine Summe gebildet. Im Ergebnis liegt nun eine Rangliste der infrage kommenden Softwareprodukte vor.

Die folgende Tabelle zeigt ein Beispiel für ein solches Vorgehen. Die im Anforderungskatalog geforderten und bewerteten Eigenschaften für ein Komprimierungsprogramm werden wie folgt gewichtet:

Im Ergebnis zeigt sich, dass Produkt 3 herausfällt, da eine notwendige Eigenschaft fehlt. Ansonsten wird die Liste angeführt von Produkt 2, gefolgt von den Produkten 1 und 4.

Die erstellte Liste muss zusammen mit der Marktübersicht der Beschaffungsstelle vorgelegt werden, damit diese überprüfen kann, inwieweit die dort aufgeführten Produkte den internen Regelungen und gesetzlichen Vorgaben entsprechen. Dabei muss die Beschaffungsstelle auch darauf achten, dass die anderen Stellen, deren Vorgaben eingehalten werden müssen, wie der Datenschutzbeauftragte, der IT-Sicherheitsbeauftragte oder der Personal- bzw. Betriebsrat, rechtzeitig beteiligt werden.

Es muss entschieden werden, wie viele und welche Kandidaten getestet werden sollen. Sinnvollerweise sollten die ersten zwei oder drei Kandidaten ausgewählt werden und daraufhin getestet werden, ob sie die wichtigsten Kriterien des Anforderungskatalogs auch tatsächlich erfüllen. Dies ist insbesondere für die notwendigen Anforderungen wichtig. Hierfür sollten Testlizenzen beschafft werden und, wie in Baustein* *OPS.1.1.7* Software-Tests und -Freigaben* beschrieben, Tests durchgeführt werden.

Neben den Kriterien des Anforderungskatalogs sollten für die Entscheidung noch die folgenden Punkte berücksichtigt werden:

**Referenzen** 

Kann der Hersteller oder Vertreiber für sein Produkt Referenzinstallationen angeben, so können die dort gemachten Erfahrungen hinterfragt und in die Produktbeurteilung einbezogen werden.

Liegen externe Testergebnisse oder Qualitätsaussagen für das zu testende Softwareprodukt vor (z. B. Testergebnisse in Fachzeitschriften, Konformitätstests nach proprietären Standards, Prüfungen und Zertifikate nach einschlägigen Standards und Normen wie ISO 9001), so sollten auch diese Ergebnisse bei der Auswahl berücksichtigt werden.

**Verbreitungsgrad des Produktes** 

Bei einem hohen Verbreitungsgrad hat der einzelne Anwender üblicherweise wenig oder keinen Einfluss auf den Hersteller des Produkts, wenn es darum geht, Fehler zu beheben oder bestimmte Funktionen zu implementieren. Er kann aber eher davon ausgehen, dass ein solches Produkt kontinuierlich weiterentwickelt wird. In einigen Fällen gibt es externe Tests, die durch den Hersteller beauftragt oder von Fachzeitschriften durchgeführt wurden. Bei Produkten mit hohem Verbreitungsgrad ist im Allgemeinen mehr über Schwachstellen bekannt, sodass der Anwender davon ausgehen kann, dass die wesentlichen Schwachstellen bereits bekannt sind, bzw. dass das Wissen über Schwachstellen schnell verbreitet wird und diese zeitnah geschlossen werden, nachdem sie bekanntgeworden sind.

Bei einem niedrigen Verbreitungsgrad kann ein Anwender eventuell mehr Einfluss auf den Hersteller nehmen. Externe Tests liegen hier jedoch oft nicht vor, da sie für Produkte kleiner Hersteller zu aufwendig und zu teuer sind. Produkte mit niedrigem Verbreitungsgrad enthalten meist nicht mehr oder weniger Schwachstellen als solche mit hohem Verbreitungsgrad. Nachteil ist hier, dass diese eventuell nicht so schnell bekannt und damit behoben werden können. Wenn es sich um Sicherheitslücken handelt, sind diese aber wahrscheinlich auch potenziellen Angreifern nicht bekannt bzw. keine lohnenden Angriffsziele.

**Wirtschaftlichkeit / Kosten für Kauf, Betrieb, Wartung, Schulung** 

Vor der Entscheidung für ein Produkt sollte immer die Frage stehen, ob die Kosten für das Produkt in einem angemessenen Verhältnis zu dem damit erzielbaren Nutzen stehen. In die Rechnung sind neben den unmittelbaren Anschaffungskosten auch alle Folgekosten für Betrieb, Wartung und Schulung einzubeziehen. Dazu muss zum Beispiel geklärt werden, ob die IT-Infrastruktur aufgerüstet werden muss oder ob für Installation und Betrieb Schulungen erforderlich sind.

Nach Abschluss aller Tests müssen die Testergebnisse der Beschaffungsstelle vorgelegt werden. Die Entscheidung für ein Produkt sollte die Beschaffungsstelle unter Beteiligung der anfordernden Fachabteilung und des IT-Bereichs aufgrund der Testergebnisse treffen. Auch sollten der Kaufpreis sowie zusätzliche Funktionen der Produkte, die nicht im Anforderungskatalog aufgeführt wurden, aber dennoch für den Einsatz sinnvoll sind, bei der Entscheidung berücksichtigt werden.

#### CON.4.M7 Überprüfung der Lieferung von Standardsoftware [Fachabteilung]

Nach Eingang einer Lieferung ist anhand der vorhandenen Unterlagen zu überprüfen,

* ob die Lieferung bestellt wurde, 
* für wen sie bestimmt ist, 
* ob Transportschäden zu erkennen sind und 
* ob sie vollständig ist, das heißt ob einerseits alle bestellten Komponenten und andererseits alle gemäß Produktbeschreibung zum Lieferumfang des Produktes gehörenden Komponenten vorhanden sind. 
Die Ergebnisse dieser Prüfungen sind in einem Wareneingangsverzeichnis zu dokumentieren, zusammen mit:

* Produktname und Version, 
* Produktart, 
* Lieferumfang, also Beschreibung der einzelnen Komponenten inklusive Anzahl und Lieferform (zum Beispiel Buch, Datenträger), 
* Lieferdatum, 
* Lieferart, 
* wer es in Empfang genommen hat, 
* Aufbewahrungsort und 
* an wen es weitergegeben wurde. 
Danach müssen die gelieferten Produkte an die IT-Abteilung weitergegeben werden, damit sie funktionale Tests durchführt und das Produkt formell freigeben, installieren und konfigurieren kann. 

Werden die Produkte nur vorübergehend eingesetzt oder zur Verfügung gestellt (zum Beispiel für einen Test) müssen zumindest die Seriennummer und andere produktspezifische Identifizierungsmerkmale in entsprechenden Bestandsverzeichnissen vermerkt werden. Wenn die gelieferten Produkte dauerhaft genutzt werden sollen, sind sie mit eindeutigen Identifizierungsmerkmalen (z. B. gruppierten fortlaufenden Inventarnummern) zu kennzeichnen. Anschließend müssen sie in ein Bestandsverzeichnis aufgenommen werden. Dieses muss Auskunft geben können über:

* Identifizierungsmerkmale, 
* Beschaffungsquellen, Lieferzeiten, 
* Verbleib, 
* Freigabedatum, 
* Installationsdatum und Konfigurationsbesonderheiten und 
* Wartungsverträge, Wartungsintervalle. 
#### CON.4.M8 Lizenzverwaltung und Versionskontrolle von Standardsoftware

Ohne eine geeignete Versions- und Lizenzkontrolle werden auf einem IT-System oder innerhalb einer Organisationseinheit erfahrungsgemäß schnell verschiedene Software-Versionen verwendet, von denen eventuell einige ohne Lizenz benutzt werden.

Auf allen IT-Systemen einer Institution darf ausschließlich lizenzierte Software eingesetzt werden. Diese Regelung muss allen Mitarbeitern bekanntgemacht werden. Die Administratoren der verschiedenen IT-Systeme müssen sicherstellen, dass nur lizenzierte Software eingesetzt wird. Dafür müssen sie mit geeigneten Werkzeugen zur Lizenzkontrolle ausgestattet und im Umgang damit geschult werden.

Häufig werden in einer Institution verschiedene Versionen einer Anwendung eingesetzt. Durch eine Lizenzkontrolle muss es möglich sein, einen Überblick über alle eingesetzten Software-Versionen zu erhalten. Damit sollte gewährleistet werden, dass alte Versionen durch neuere ersetzt werden, sobald das notwendig ist und dass bei der Rückgabe von Lizenzen alle Versionen gelöscht werden.

Darüber hinaus sollten die verschiedenen Konfigurationen der installierten Software dokumentiert werden. Damit muss es möglich sein, sich einen Überblick zu verschaffen, an welchem IT-System welche sicherheitsrelevanten Einstellungen eines Produktes durch die Freigabe vorgegeben und welche tatsächlich installiert wurden. Damit kann zum Beispiel schnell geklärt werden, an welchen Clients bei einem bestimmten Produkt Makro-Programmierung installiert worden ist und an welchen nicht.

Damit Lizenzen bei Hardware-Defekten nicht ungültig werden, sollten Hardware-unabhängige Lizenzen eingesetzt werden. So kann ein IT-System mit weniger Aufwand ersetzt werden, wenn die Hardware ausfällt. Ist das nicht möglich, sind geeignete Vorkehrungen für einen Ausfall zu treffen, etwa Vereinbarungen mit dem Hersteller bezüglich einer Lizenzübertragung.

Wenn es notwendig ist, ein Produkt online über einen Lizenzierungsserver des Herstellers zu aktivieren, kann die Lizenz nachträglich verfallen und das Produkt deaktiviert werden. Wenn möglich, sollten Produkte gewählt werden, die nicht online aktiviert werden müssen. Auch hier sind Vorkehrungen für einen Ausfall zu treffen.

Wenn es möglich und wirtschaftlich sinnvoll ist, sollten unbefristete Lizenzen bevorzugt werden. Damit kann eine Funktionseinschränkung verhindert werden, wenn die Lizenz abgelaufen ist oder die Systemzeit stark abweicht.

#### CON.4.M9 Deinstallation von Standardsoftware

Bei der Deinstallation von Standardsoftware sind grundsätzlich die Vorgaben des Bausteins OPS.1.1.8* Löschen und Vernichten von Daten* zu beachten. Darüber hinaus gelten einige Besonderheiten.

Bei der Deinstallation von Software müssen alle Dateien entfernt werden, die für den Betrieb der Software auf dem IT-System angelegt worden sind. Auch müssen alle Einträge in Systemdateien, die bezüglich des Produktes vorgenommen wurden, gelöscht werden. Bei vielen Softwareprodukten werden während der Installation in diversen Verzeichnissen auf dem IT-System Dateien angelegt oder bestehende Dateien verändert. In der Regel wird der Benutzer nicht über alle durchgeführten Veränderungen am IT-System informiert.

Um Standardsoftware wieder vollständige deinstallieren zu können, ist es daher hilfreich, die bei der Installation durchgeführten Systemänderungen entweder manuell oder mithilfe von speziellen Tools zu dokumentieren. Anderenfalls kann es sein, dass ein Produkt nicht komplett deinstalliert wird. 

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.4.M10 Implementierung zusätzlicher Sicherheitsfunktionen(CIA)

Manchmal ist es notwendig, dass ergänzend zur Standardsoftware selbst Sicherheitsfunktionen wie eine Zugangskontrolle, eine Zugriffsrechteverwaltung und -prüfung oder eine Protokollierung genutzt und eventuell implementiert werden müssen:

* Reichen die Protokollierungsmöglichkeiten des IT-Systems einschließlich zusätzlich eingesetzter Sicherheitsprodukte nicht aus, um eine ausreichende Beweissicherung zu gewährleisten, so müssen diese geeignet implementiert werden. 
* Reicht die Granularität der Zugriffsrechte des IT-Systems einschließlich zusätzlich eingesetzter Sicherheitsprodukte nicht aus, um einen ordnungsgemäßen Betrieb zu gewährleisten, so muss eine Zugriffsrechteverwaltung und -kontrolle implementiert werden. 
* Ist es mit dem IT-System einschließlich zusätzlich eingesetzter Sicherheitsprodukte nicht möglich, den Administrator daran zu hindern auf bestimmte Daten zuzugreifen oder zumindest diesen Zugriff zu protokollieren und zu kontrollieren, dann muss dies bei Bedarf durch zusätzliche Sicherheitsfunktionen implementiert werden. Zum Beispiel kann mit einer Verschlüsselung der Daten verhindert werden, dass der Administrator diese Daten im Klartext liest, wenn er den zugehörigen Schlüssel nicht besitzt. 
Diese zusätzlichen Anforderungen an Standardsoftware müssen schon in der Planung und bei der Auswahl berücksichtigt werden, da eine nachträgliche Implementierung meist unwirtschaftlich oder nicht einfach möglich ist. 

#### CON.4.M11 Nutzung zertifizierter Standardsoftware(CIA)

Bei einem hohen Schutzbedarf kann die Vertrauenswürdigkeit von Standardsoftware hinsichtlich der Informationssicherheit nur dadurch gewährleistet werden, dass unabhängige Prüfstellen die Produkte untersuchen und bewerten. Darauf aufbauend kann dann ein Zertifikat erteilt werden.

**Zertifizierung von Produkten** 

Allgemein anerkannte Grundlage der Evaluierung und Zertifizierung von Produkten bilden seit 1991 die europaweit harmonisierten „Kriterien für die Bewertung der Sicherheit von Systemen der Informationstechnik (ITSEC)“ und seit 1998 die weltweit angestimmten „Gemeinsamen Kriterien für die Prüfung und Bewertung der Sicherheit von Informationstechnik“, kurz Common Criteria (CC). In Deutschland führt das BSI solche Zertifizierungen durch. Bei positivem Evaluationsergebnis und bei Einhaltung der Rahmenbedingungen von ITSEC bzw. der Common Criteria wird für das untersuchte Produkt vom BSI als Zertifizierungsstelle ein Sicherheitszertifikat erteilt.

Aus dem dazugehörenden Zertifizierungsdokument geht hervor, welche Funktion mit welcher Prüftiefe untersucht wurde und welche Bewertung vorgenommen wurde. Dabei reicht die Prüftiefe von Evaluationsstufe E 1 (geringste Prüftiefe) bis Evaluationsstufe E 6 (höchste Prüftiefe) bei den ITSEC bzw. von Vertrauenswürdigkeitsstufe EAL 1 (geringste Prüftiefe) bis Vertrauenswürdigkeitsstufe EAL 7 (höchste Prüftiefe) bei den CC. Dabei entspricht die Evaluationsstufe E 1 der ITSEC in etwa der Vertrauenswürdigkeitsstufe EAL 2 der CC usw. Zusätzlich wird die geprüfte Mechanismenstärke der Implementation der Sicherheitsfunktionen angegeben, die ein Maß für den Aufwand darstellt, der erforderlich ist, um die Sicherheitsfunktionen zu überwinden. ITSEC und CC unterscheiden hier die Mechanismenstärken niedrig, mittel und hoch. Darüber hinaus werden Hinweise gegeben, welche Randbedingungen beim Einsatz des Produktes beachtet werden müssen.

Stehen bei der IT-Beschaffung mehrere Produkte mit angemessenem Preis-/Leistungsverhältnis zur Auswahl, sollten nur solche mit Sicherheitszertifikat berücksichtigt werden. Hierbei sollten Sicherheitszertifikate insbesondere dann berücksichtigt werden, wenn der evaluierte Funktionsumfang die Mindestfunktionalität (weitestgehend) umfasst und die Mechanismenstärke dem Schutzbedarf entspricht. Je höher dann die im Zertifikat angegebene Prüfungstiefe ist, desto mehr Vertrauen in Wirksamkeit und Korrektheit der Sicherheitsfunktionen kann dem Produkt entgegengebracht werden.

**Übersichten zertifizierter Produkte** 

Die Zertifizierungsstellen geben regelmäßig Übersichten heraus, welche Produkte ein Zertifikat erhalten haben. Eine Zusammenstellung der vom BSI zertifizierten IT-Produkte findet sich auf der BSI-Website. Weiterhin veröffentlicht das BSI neu erteilte Zertifikate in der Zeitschrift <kes> - Die Zeitschrift für Informations-Sicherheit. Diese Informationen lassen sich ebenfalls von den Internetseiten des BSI abrufen.

#### CON.4.M12 Einsatz von Verschlüsselung, Checksummen oder digitalen Signaturen(CI)

Werden vertrauliche Informationen oder Informationen mit hohem Integritätsanspruch übertragen, sollte ein kryptografisches Verfahren zum Schutz der Daten für den Transport oder die Übermittlung eingesetzt werden.

**Vertraulichkeitsschutz durch Verschlüsselung** 

Das entscheidende Merkmal eines Verschlüsselungsverfahrens ist die Güte des Algorithmus sowie der Schlüsselauswahl. Ein anerkannter Algorithmus ist beispielsweise der Advanced Encryption Standard (AES).

Um die Vertraulichkeit der zu übertragenden Informationen zu gewährleisten, müssen die IT-Systeme des Absenders und des Empfängers den Zugriff auf das Verschlüsselungsprogramm ausreichend schützen. Gegebenenfalls sollte dieses Programm auf einem auswechselbaren Datenträger gespeichert, in der Regel verschlossen aufbewahrt und nur bei Bedarf eingespielt und genutzt werden.

**Integritätsschutz durch Checksummen, Verschlüsselung oder digitaler Signaturbildung** 

Ist für den Datenaustausch lediglich die Integrität der zu übermittelnden Daten sicherzustellen, muss unterschieden werden, ob ein Schutz nur gegen zufällige Veränderungen, z. B. durch Übertragungsfehler, oder auch gegen Manipulationen realisiert werden soll. Sollen ausschließlich zufällige Veränderungen erkannt werden, können Checksummen-Verfahren (z. B. Cyclic Redundancy Checks) oder fehlerkorrigierende Codes eingesetzt werden. Schutz gegenüber Manipulationen bieten darüber hinaus Verfahren, die unter Verwendung eines symmetrischen Verschlüsselungsalgorithmus (z. B. Triple-DES) aus der zu übermittelnden Information einen sogenannten Message Authentication Code (MAC) erzeugen. Andere Verfahren bedienen sich eines asymmetrischen Verschlüsselungsalgorithmus (z. B. RSA) in Kombination mit einer Hashfunktion und erzeugen eine digitale Signatur. Die jeweiligen erzeugten Fingerabdrücke (Checksumme, fehlerkorrigierende Codes, MAC, digitale Signatur) werden zusammen mit der Information an den Empfänger übertragen und können von diesem überprüft werden.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Auswahl und Einsatz von Standardsoftware" finden sich unter anderem in folgenden Veröffentlichungen:

*  

 #### [27001A12.1.1] ISO/ IEC 27001:2013 - Annex A.12.1.1 Documented operating procedures

  

 Insbesondere Annex A, A.12.1.1 Documented operating procedures, (zuletzt abgerufen 05.10.2017)  
 <https://www.iso.org/home.html>

  

 
*  

 #### [27001A12.1.2] ISO/IEC 27001:2013 - Annex A.12.1.2 Change management

  

 Insbesondere Annex A, A.12.1.2 Change management, (zuletzt abgerufen 05.10.2017)  
 [www.iso.org/home.html](www.iso.org/iso/home/standards/management-standards/iso27001.htm)

  

 
*  

 #### [27001A12.6.2] ISO/ IEC 27001:2013 - Annex A.12.6.2 Restriction of software installation

  

 Insbesondere Annex A, A.12.6.2 Restriction of software installation, (zuletzt abgerufen 05.10.2017)  
 <https://www.iso.org/home.html>

  

 
*  

 #### [27001A8.1.1.] ISO/ IEC 27001:2013 - Annex A.8.1.1. Inventory of assets

  

 Insbesondere Annex A, A.8.1.1 Inventory of assets, (zuletzt abgerufen 05.10.2017)  
 [www.iso.org/home.html](www.iso.org/iso/home/standards/management-standards/iso27001.htm)

  

 
*  

 #### [27001A8.1.3] ISO/ IEC 27001:2013 - Annex A.8.1.3 Acceptable use of assets

  

 Insbesondere Annex A, A.8.1.3 Acceptable use of assets, (zuletzt abgerufen 05.10.2017)  
 <www.iso.org/iso/home/standards/management-standards/iso27001.htm>

  

 
*  

 #### [27001A8.1.4] ISO/ IEC 27001:2013 - Annex A.8.1.4 Return of assets

  

 Insbesondere Annex A.8.1.4 Return of assets, (zuletzt abgerufen 05.10.2017)  
 <https://www.iso.org/home.html>

  

 
*  

 #### [CC] Common Criteria for Information Technology Security Evaluation (CC)

  

 erschienen in der Normenreihe ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (zuletzt abgerufen am 28.09.2017)  
 <www.commoncriteriaportal.org>

  

 
*  

 #### [ISFBA] The Standard of Good Practice - Area BA - Business Application Management

  

 insbesonder Area BA - Business Application Management, Information Security Forum (ISF), 06.2016

  

 
*  

 #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

  

 
*  

 #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

  

 
