1 Beschreibung
--------------

### 1.1 Einleitung

Zur Grundausstattung in Büros gehören typischerweise Kopierer, Drucker und Multifunktionsgeräte. Sehr häufig ist es aber nicht effizient, jeden einzelnen Arbeitsplatz mit einem Drucker auszustatten. Daher werden oft zentrale Netzdrucker, Kopierer oder Multifunktionsgeräte eingesetzt, auf denen die Mitarbeiter ihre Dokumente ausdrucken oder vervielfältigen können.

Da es einige Nachteile hat, wenn Aufträge vom Arbeitsplatz-PC direkt an einen Netzdrucker verschickt werden, setzen die meisten Institutionen einen zentralen Druckserver ein, der die Aufträge annimmt und auf die verfügbaren Drucker verteilt. 

Die Integration der papierverarbeitenden Geräte in ein Netz ist in vielen Fällen nicht nur auf Drucker beschränkt. Netzfähige Dokumentenscanner können beispielsweise für eine Vielzahl von Benutzern bereitgestellt werden, damit diese Papierdokumente digitalisieren können. In Verbindung mit einem Drucker kann ein Scanner beispielsweise wie ein Kopierer betrieben werden.

Als Multifunktionsgeräte werden in diesem Baustein Geräte bezeichnet, die mehrere verschiedene papierverarbeitende Funktionen bieten, etwa Drucken, Kopieren und Scannen oder auch Fax-Dienste. Aus Gründen der Lesbarkeit werden nicht alle Gerätetypen überall einzeln benannt. Da aber beispielsweise für digitale Kopierer ähnliche Sicherheitsempfehlungen wie für Netzdrucker zu beachten sind, gelten für sie die Anforderungen analog.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Der Einsatz von Netzdruckern, Kopierern und Multifunktionsgeräten muss sorgfältig geplant werden (siehe SYS.4.1.M1 *Erstellung eines Basis-Konzepts für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten *sowie SYS.4.1.M3 *Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten*). Im Kapitel 3.1.2 *Verwaltung von Druckern* dieser Umsetzungshinweise sind vertiefende Informationen dazu beschrieben, woraus typische Druckerlandschaften bestehen und wie sie gestaltet sind. Die Sicherheitsanforderungen an Netzdrucker müssen in die allgemeine Sicherheitsstrategie der Institution integriert sein.

Viele Probleme mit Druckern, Kopierern und Multifunktionsgeräten können nicht immer mit technischen Maßnahmen gelöst werden. Die Benutzer müssen über eine sicherheitsbewusste Bedienung der Geräte informiert und hierauf verpflichtet werden (siehe SYS.4.1.M5 *Erstellung von* *Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten*).

Es sollten auch die speziellen Anforderungen bestimmter Gerätearten berücksichtigt werden. Hierzu gehören beispielsweise Multifunktionsgeräte (siehe SYS.4.1.M10 *Netztrennung beim Einsatz von Multifunktionsgeräten*) und Dokumentenscanner (siehe SYS.4.1.M9 *Einsatz von netzfähigen Dokumentenscannern*). 

**Beschaffung**

Anhand der Einsatzszenarien sind die Anforderungen an die zu beschaffenden Produkte zu formulieren und basierend darauf geeignete Produkte auszuwählen. Wissenswertes dazu ist im Kapitel 3.1.1 *Kriterien für die Beschaffung und geeignete Auswahl von Druckern, Kopierern und Multifunktionsgeräten *zu finden. 

**Umsetzung**

Sind alle Planungsschritte durchlaufen, geht es um die Inbetriebnahme der Geräte. Dabei kommt es auch darauf an, wo die Geräte positioniert werden (siehe SYS.4.1.M2 *Geeignete Aufstellung von Druckern, Kopierern und Multifunktionsgeräten*) und wie der Zugriff auf die Geräte beschränkt wird (siehe SYS.4.1.M6 *Beschränkung der Zugriffe auf Drucker, Kopierer und Multifunktionsgeräte*).

Wie jedes IT-System sollten auch netzfähige Drucker, Kopierer und Multifunktionsgeräte vor unberechtigter Nutzung geschützt werden (siehe SYS.4.1.M13 *Authentisierung bei Druckern, Kopierern und Multifunktionsgeräten*). Aber auch die Medien, auf denen die (digitalen) Informationen übertragen und abgelegt werden, müssen angemessen abgesichert werden (siehe SYS.4.1.M14 *Informationsschutz bei Druckern, Kopierern und Multifunktionsgeräten*).

Neben der Druckhardware sind die Softwarekomponenten, wie Druckserver oder -clients, für einen sicheren Betrieb wichtig. In Abhängigkeit vom eingesetzten Betriebssystem und Drucksystem sind entsprechende Anforderungen und Bausteine umzusetzen, wie SYS.4.1.M4 *Sicherer Einsatz von CUPS* oder APP.3.4 *Samba*.

**Betrieb**

Im Regelbetrieb ist neben der Protokollierung wichtiger Ereignisse (siehe SYS.4.1.M8 *Protokollierung bei Druckern, Kopierern und Multifunktionsgeräten*) auch die Versorgung der Geräte mit Verbrauchsgütern (siehe SYS.4.1.M7 *Versorgung und Kontrolle der Verbrauchsgüter*) von hoher Bedeutung. 

**Aussonderung**

Sehr oft sind im Speicher der Drucker, Kopierer und Multifunktionsgeräte schutzbedürftige Informationen abgelegt. Wenn die Geräte entsorgt werden, muss SYS.4.1.M12 *Sichere Außerbetriebnahme von Druckern, Kopierern und Multifunktionsgeräten* berücksichtigt werden.

**Notfallvorsorge**

Aspekte der Notfallplanung für vernetzte Drucker, Kopierer und Multifunktionsgeräte werden in SYS.4.1.M15 *Notfallvorsorge bei Druckern, Kopierern und Multifunktionsgeräten* thematisiert. 

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Drucker, Kopierer und Multifunktionsgeräte" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### SYS.4.1.M1 Erstellung eines Basis-Konzepts für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten [Leiter IT]

Eine grundlegende Voraussetzung für den sicheren Einsatz von Druckern, Kopierern und Multifunktionsgeräten ist eine angemessene Planung im Vorfeld. Der Einsatz der Geräte kann in mehreren Schritten nach dem Prinzip des Top-Down-Entwurfs geplant werden: Ausgehend von einem Grobkonzept für das Gesamtsystem werden konkrete Planungen für Teilkomponenten in spezifischen Teilkonzepten festgelegt (siehe dazu auch *SYS.4.1.M3 Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten*). Im Grobkonzept sollten beispielsweise folgende Schwerpunkte behandelt werden:

* Zunächst muss geregelt werden, wo Drucker, Kopierer und Multifunktionsgeräte aufgestellt werden sollen und wer diese Räume betreten bzw. auf die Geräte zugreifen darf.
* Weiterhin muss geregelt werden, wer welche Zugriffsberechtigungen auf welche Netzgeräte für welche Aufgaben erhält.
* Die Drucker, Kopierer und Multifunktionsgeräte müssen vor Angriffen geschützt werden. 

 
	+ Durch entsprechende Maßnahmen sollte physischen Manipulationen entgegengewirkt werden. Werden beispielsweise Schlösser oder Siegel an Wartungszugängen, wie Zugangsklappen angebracht, können unautorisierte Veränderungen erschwert oder zumindest erkannt werden.
	+ Ebenso sollten Angriffe über Netze erschwert werden. Hierzu gehören beispielsweise unberechtigte Zugriffe auf Schnittstellen zur Fernadministration über das LAN. 
	+ Außerdem müssen die elektronischen Informationen geschützt werden, sowohl bei der Übertragung zu den Geräten als auch bei der weiteren Verarbeitung. Beispielsweise sollte überlegt werden, alle Dokumente, die auf den Festplatten der Geräte (eventuell nur temporär) abgespeichert werden, zu verschlüsseln. Alle Entscheidungen, die in der Planungsphase getroffen wurden, müssen so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Dabei ist darauf zu achten, dass sie passend strukturiert und verständlich sind. 
	  

 
#### SYS.4.1.M2 Geeignete Aufstellung von Druckern, Kopierern und Multifunktionsgeräten

Um zu verhindern, dass Drucker, Kopierern oder Multifunktionsgeräte manipuliert werden oder die Druckausgaben von Unbefugten kopiert oder mitgelesen werden können, sollten die Geräte so aufgestellt werden, dass nur berechtigte Mitarbeiter Zugang zu ihnen haben. Zumindest sollten die Geräte nicht in Bereichen aufgestellt werden, in denen sich häufig externe Personen aufhalten, insbesondere also nicht in der Nähe von Besprechungs-, Veranstaltungs- oder Schulungsräumen. Hiervon ausgenommen sind lediglich solche Geräte, die speziell für diese Bereiche vorgesehen sind, beispielsweise in Schulungsräumen.

Häufig stehen in Druckerräumen auch Kopierer. Aus Sicherheitssicht ist zu hinterfragen, ob hierdurch die Gefahr steigt, dass herumliegende Ausdrucke kopiert werden können. Um solche Probleme zu vermeiden, ist es sinnvoll, Drucker und Kopierer so aufzustellen, dass sie vom eigenen Personal gut eingesehen werden können. Besser ist es jedoch, die Geräte in einem geschlossenen Raum aufzustellen, zu dem nur Berechtigte Zutritt haben. Das ist besonders bei höherem Schutzbedarf zu empfehlen.

Noch besser istkann es bei großen Druckern sein, wenn die Ausdrucke durch eine vertrauenswürdige Person in nur für den jeweiligen Empfänger zugängliche Fächer verteilt werden. Druckerausgaben müssen daher mit dem Namen des Empfängers gekennzeichnet sein. Das kann automatisch durch die Druckprogramme erfolgen. Bei hohem Schutzbedarf sollte geprüft werden, ob diese Lösung geeignet ist.

Benutzer stellen häufig erst am Drucker fest, dass sie das falsche Dokument ausgedruckt haben oder dass noch eine Kleinigkeit geändert werden muss. Solche Ausdrucke werden dann häufig direkt beim Drucker in einen offenen Papierkorb geworfen. Da damit auch vertrauliche Dokumente in falsche Hände geraten können, empfiehlt es sich, einen Vernichter direkt neben Netzdruckern aufzustellen. Ersatzweise müssen die Benutzer darauf hingewiesen werden, dass solche Dokumente nicht liegengelassen werden dürfen und anderweitig zu vernichten sind.

#### SYS.4.1.M3 Regelmäßige Aktualisierung

Es muss regelmäßig überprüft werden, ob die Drucker, Kopierer und Multifunktionsgeräte auf dem aktuellen Stand sind. Wenn Sicherheitslücken identifiziert werden, müssen diese so schnell wie möglich behoben werden. Vorhandene Patches und Updates müssen sofort eingespielt werden oder anderweitige Sicherheitsmaßnahmen ergriffen werden, wenn keine Patches zur Verfügung stehen. Generell muss darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden.

Vertiefende Informationen sind in OPS.1.2.1. Patch- und Änderungsmanagement zu finden.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Drucker, Kopierer und Multifunktionsgeräte".

#### SYS.4.1.M4 Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten [Leiter IT]

Aufbauend auf einem Grobkonzept für das Gesamtsystem (siehe *SYS.4.1.M1 Erstellung eines Basis-Konzepts für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten)* sollten konkrete Planungen für Teilkomponenten in spezifischen Teilkonzepten festgelegt werden. Die Planung betrifft dabei nicht nur Aspekte, die klassischerweise mit dem Begriff Sicherheit verknüpft werden, sondern auch normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen können. 

Die folgenden Teilkonzepte sollten bei der Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten berücksichtigt werden:

* Allgemeine Aspekte: 

 
	+ **Kauf oder Mieten:** In einigen Fällen kann es sinnvoll sein, die benötigten Geräte nicht zu kaufen, sondern zu mieten. Werden sie gemietet, muss sichergestellt werden, dass eventuell im Speicher abgelegte Dokumente sicher gelöscht werden, damit diese nicht vom nächsten Kunden, der das Gerät mietet, wieder hergestellt werden können. Hierbei muss vorab überprüft werden, ob die Geräte ohne Speicher zurückgegeben werden können oder ob die Speicherbereiche zuverlässig gelöscht werden können, ohne diese physisch zu zerstören.
	+ **Lokale oder netzfähige Drucker:** Es ist zu entscheiden, wo lokale und wo netzfähige Drucker eingesetzt werden sollen. Häufig bietet auch eine Zwischenlösung Vorteile: Benutzer, die oft sensible Informationen ausdrucken müssen, erhalten für diese Ausdrucke einen lokalen Drucker. Für die Ausdrucke der restlichen Benutzer oder für Ausdrucke von Informationen mit einem geringeren Schutzbedarf sind bei der Zwischenlösung leistungsfähigere, zentrale Drucker verfügbar.
	+ **Druckserver:** Netzdrucker können direkt von den Arbeitsplatzrechnern oder über einen (oder mehrere) Druckserver angesteuert werden. Ein Druckserver nimmt die Druckaufträge von den IT-Systemen an und leitet sie an die gewünschten Drucker weiter. Neben einer zentralen Verwaltung und Protokollierung können die Drucker so effizienter gegen Angriffe geschützt werden, wenn nur noch die Druckserver auf die Netzdrucker zugreifen dürfen. Es ist eine geeignete Lösung auszuwählen.
	+ **Richtlinien für die Nutzung:** Um Drucker, Kopierer und Multifunktionsgeräte sicher und effektiv in Institutionen einsetzen zu können, müssen hierfür Sicherheitsvorgaben erstellt werden, die auf den vorhandenen Sicherheitszielen basieren sowie die Anforderungen aus den geplanten Einsatzszenarien einbeziehen. Diese spezifischen Sicherheitsvorgaben müssen mit dem übergreifenden Sicherheitskonzept der Institution abgestimmt sein.  
	 Darauf aufbauend ist die sichere Nutzung dieser Geräte zu regeln, und es müssen Sicherheitsrichtlinien dafür erarbeitet werden (siehe SYS.4.1.M5 Erstellung von *Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten*). Es ist darauf zu achten, dass Drucker, Multifunktionsgeräte und ähnliche Geräte in Sicherheitsaudits einbezogen werden und dass auch bei diesen Geräten regelmäßig kontrolliert wird, ob die Sicherheitsvorgaben umgesetzt sind.
	+ **Verteilung von Privilegien:** Es muss entschieden werden, ob bestimmte Funktionen eines Druckers, Kopierers oder Multifunktionsgerätes auf ausgewählte Benutzer beschränkt werden sollen. 
	+ **Nachfüllen von Verbrauchsgütern:** Bei Druckern, Kopierern und Multifunktionsgeräten müssen regelmäßig Verbrauchsgüter wie Tinte, Toner oder Papier nachgefüllt werden. Es sind Regelungen zu treffen, wer hierfür zuständig ist und welche Abläufe dabei eingehalten werden müssen (siehe SYS.4.1.M7 *Versorgung und Kontrolle der Verbrauchsgüter*).
	  

 
* **Regelungen des Dokumentenzugriffs:** Es müssen Maßnahmen ergriffen werden, die den Zugriff auf fremde Dokumente erschweren: 

 
	+ **Sicherheitskritische Informationen:** Werden an Netzdruckern häufig sicherheitskritische Informationen ausgedruckt, muss sichergestellt werden, dass nur befugte Personen auf die Ausdrucke zugreifen können. Hierfür können beispielsweise Netzdrucker und Kopierer eingesetzt werden, bei denen sich die Benutzer für einen Ausdruck direkt am Gerät authentisieren müssen (siehe SYS.4.1.M13 *Authentisierung bei Druckern, Kopierern und Multifunktionsgeräten*). Alternativ könnte auch der Zutritt zum Drucker auf wenige vertrauenswürdige Personen beschränkt werden, die die Ausdrucke an die jeweiligen Empfänger verteilen. 
	+ **Weitere Restriktionen:** Es ist zu klären, ob und welche Restriktionen für Druckerzugriffe gelten sollen. Beispielsweise ist es normalerweise nicht sinnvoll, dass Mitarbeiter, die sich von außerhalb ins Netz einwählen, auf entfernte Drucker ausdrucken können, da sie ihre Ausdrucke nicht direkt abholen können. Auch für die Zeiten, in denen normalerweise nicht gedruckt wird, können entsprechende Restriktionen umgesetzt werden. 
	  

 
* **Schutz der Geräte:** Der Zugriff auf die Netzdrucker sollte beschränkt werden (siehe SYS.4.1.M6 *Beschränkung der Zugriffe auf Drucker, Kopierer und Multifunktionsgeräte*): 

 
	+ **Administration:** Damit unberechtigten Personen Druckereinstellungen nicht verändern können, sind entsprechende Schutzmaßnahmen für Netzdrucker umzusetzen. 
	+ **Physischer Schutz:** Es sollte überlegt werden, Maßnahmen gegen Manipulationen direkt am Gerät zu ergreifen. Hierzu gehören eine geeignete Aufstellung der Drucker sowie der Schutz der Schnittstellen.
	+ **Netzspezifischer Schutz:** Bei netzfähigen Komponenten sind Mechanismen zum Schutz vor Angriffen aus dem Netz einzurichten. Wenn IEEE 802.1X oder ähnliche Verfahren zur netztechnischen Zugangskontrolle von den Netzdruckern und der Netzinfrastruktur unterstützt werden, sollten diese auch verwendet werden. Damit wird verhindert, dass IT-Systeme unberechtigt an das Netz angeschlossen werden. Weiterhin sollten Druckserver keine Verbindungen zu anderen IT-Systemen außer zu den voreingestellten Druckern aufbauen können. 
	  

 
* **Verfügbarkeit: **Es wird empfohlen,müssen Vorkehrungen gegen einen Ausfall der Druckserver oder einzelner Geräte zu treffen. Durch entsprechende Wartungsverträge kann beispielsweise die Ausfallzeit reduziert werden, wenn technische Defekte auftreten (siehe SYS.4.1.M15 *Notfallvorsorge bei Druckern, Kopierern und Multifunktionsgeräten*). 
* **Verschlüsselung: **In der Anforderung SYS.4.1.M14 *Informationsschutz bei Druckern, Kopierern und Multifunktionsgeräten* werden unter anderem folgende Fragestellungen betrachtet, die bei der Planung eine wichtige Rolle spielen: 

 
	+ **Festplattenverschlüsselung:** Viele Drucker und digitale Kopiergeräte besitzen eingebaute Speichermedien, auf denen Informationen abgelegt werden. Falls das Gerät hierfür eine Verschlüsselung unterstützt, sollte diese benutzt werden. 
	+ **Verschlüsselung der Kommunikation:** Es sollte überlegt werden, die Kommunikation zwischen den Arbeitsplatzrechnern und den Druckservern sowie zwischen den Druckservern und den Druckern zu verschlüsseln. 
	  

 
* **Löschen des Gerätespeichers: **Als Zwischenspeicher für die temporäre Ablage der zu druckenden Informationen werden bei größeren Geräten häufig Festplatten verwendet. Je nach Konfiguration werden die Informationen im Zwischenspeicher nicht nur temporär, sondern permanent gespeichert. Es sollte gewährleistet werden, dass die Informationen nach dem Ausdruck aus dem Zwischenspeicher gelöscht werden. Hierfür besitzen viele Kopierer eine Löschfunktion. Wenn sich die Dokumente nicht automatisch löschen lassen, sollten alle Benutzer darauf hingewiesen werden, diese Funktion konsequent zu benutzen (siehe SYS.4.1.M5 *Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten*).
Alle Entscheidungen, die in der Planungsphase getroffen wurden, müssen so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. 

#### SYS.4.1.M5 Erstellung von Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten

Drucker, Kopierer und Multifunktionsgeräte lassen sich nicht allein mit technischen Maßnahmen absichern. Zusätzlich müssen entsprechende Sicherheitsrichtlinien für die Administratoren und die Benutzer festgelegt werden. In der Administrationsrichtlinie sollten alle umzusetzenden Sicherheitsmechanismen für Drucker, Kopierer und Multifunktionsgeräte beschrieben sein. Dieses Dokument richtet sich an das Fachpersonal der Institution.

Die Sicherheitsrichtlinien für die Benutzer sollten in einem übersichtlichen Merkblatt zusammengefasst werden. Dieses Merkblatt sollte an allen Aufstellungsorten der Geräte aufgehängt werden.

Es sind folgende Aspekte zu berücksichtigen:

* **Zutritt zu den Kopier- und Druckerräumen:** Wenn möglich, sollte der Zutritt zu Räumen mit Druckern, Kopierern und Multifunktionsgeräten beschränkt werden (siehe auch SYS.4.1.M2 *Geeignete Aufstellung von Druckern, Kopierern und Multifunktionsgeräten*). Es bietet sich an, den Zutritt beispielsweise auf die Mitarbeiter einer Abteilung oder auf die Benutzer einer Etage einzugrenzen. Die Benutzer sind über die Zutrittsbeschränkungen und die zugelassenen Personenkreise zu unterrichten.
* **Behandlung nicht abgeholter Dokumente:** Häufig werden ausgedruckte Dokumente nicht abgeholt, gedruckte Fax-Sendeberichte vergessen oder Fehldrucke nicht entsorgt. Alle Benutzer müssen darüber informiert sein, dass sie ihre Ausdrucke zeitnah abholen müssen. Dokumente, die keinem Benutzer zugeordnet werden können, sollten eingesammelt oder besser direkt mit einem Schredder vernichtet werden.
* **Umgang mit sensiblen Dokumenten:** Als "hoch vertraulich" klassifizierte Informationen sollten nicht an allgemein zugänglichen Druckern ausgedruckt bzw. Kopierern vervielfältigt werden. Amtlich geheim zu haltende Dokumente (Verschlusssachen) müssen gemäß der geltenden Vorschriften und Anweisungen geschützt werden.
* **Authentisierung am Gerät:** Soll eine Authentisierung direkt am Drucker, Kopierer oder Multifunktionsgerät erfolgen (siehe SYS.4.1.M13 *Authentisierung bei Druckern, Kopierern und Multifunktionsgeräten*), müssen die Benutzer in dieses Verfahren eingewiesen werden.
* **Verteilung von Ausdrucken:** Werden an Netzdruckern oft sicherheitskritische Informationen ausgedruckt, sollte überlegt werden, die Ausdrucke an die jeweiligen Empfänger durch vertrauenswürdige Personen verteilen zu lassen. Dieser Ansatz ist eine Alternative zur Authentisierung am Gerät und hat den Vorteil, dass nur diese Personen Zutritt zu den jeweiligen Druckern benötigen.
* **Auswahl eines Standarddruckers:** Bei mehreren verfügbaren Druckern oder Multifunktionsgeräten können die Benutzer auf ihrem Client meist für alle Applikationen einen Standarddrucker vorauswählen. Als Standarddrucker sollte ein logisches (virtuelles) Gerät wie ein Druckvorschau-Programm oder ein PDF-Generator gewählt werden. Das schützt davor, dass Informationen unbemerkt ausgedruckt werden, beispielsweise weil unbeabsichtigt die Drucken-Schaltfläche in einer Applikation betätigt wurde.
* **Löschen des Kopierspeichers durch den Benutzer:** Ein Vorteil von digitalen Kopierern ist, dass ein einmal eingescanntes Dokument beliebig oft ausgedruckt werden kann. Damit Unbefugte nicht auf solche Informationen zugreifen können, muss der hierfür verwendete temporäre Speicher nach der Benutzung gelöscht werden. Bei vielen Kopierern können die Benutzer das nur manuell veranlassen, daher müssen entsprechende Hinweise und Anweisungen an den Geräten angebracht werden.Jeder Benutzer sollte sich mit dem Merkblatt zum sicheren Umgang mit Druckern, Kopierern und Multifunktionsgeräten vertraut machen.
#### SYS.4.1.M6 Sicherer Einsatz von CUPS

Bei Unix-Systemen wird häufig das netzfähige Drucksystem *Common Unix Printing System* (CUPS) verwendet (siehe [CUPS]). CUPS ist zu vielen anderen Drucksystemen kompatibel, wie *Common Internet File System/ Server Message Block* (CIFS/SMB), das Datei- und Druckerfreigaben unter Windows ermöglicht.

Folgende Aspekte müssen berücksichtigt werden, wenn CUPS eingesetzt wird.

**Allgemeine Aspekte**

* Lokaler Betrieb oder zentraler Druckserver  
 CUPS kann als verteilte Anwendung (Client auf Arbeitsplatz-PC mit entferntem Server) oder lokal betrieben werden. Entsprechend muss bei der Konfiguration unterschieden werden, ob sich der CUPS-Client und der CUPS-Server auf demselben IT-System oder auf verschiedenen IT-Systemen befinden. Wenn sie sich auf verschiedenen IT-Systemen befinden, ist die IP-Adresse oder der Rechnername des jeweiligen Servers in der Konfigurationsdatei (*client.conf*) des CUPS-Clients festzulegen. Bei einer lokalen Nutzung muss dort hingegen die Loopback-Adresse (*127.0.0.1*) oder der Rechnername *localhost* eingetragen werden. Der CUPS-Server muss bei lokaler Nutzung mithilfe des Konfigurationseintrages *Listen* in der Datei *cupsd.conf* an die Loopback-Adresse gebunden werden, damit der Dienst nicht aus dem Netz erreichbar ist. Unabhängig davon, ob nur lokale IT-Systeme auf den Drucker zugreifen dürfen, kann CUPS zentral administriert werden. Dienste wie SSH oder der CUPS-Webserver (siehe Abschnitt zur Administration) ermöglichen es weiterhin, Einstellungen über das Netz vorzunehmen.
* Verwaltungs- und Statusinformationen  
 Die Clients müssen regelmäßig über die verfügbaren Drucker und deren Status informiert werden. Beim *Broadcasting* sendet der Server in regelmäßigen Abständen unaufgefordert eine Nachricht an alle Druckclients und beim *Polling* ruft der Druckclient die Informationen vom Server ab.  
 Soll die Informationsverteilung über die verfügbaren Drucker nicht mit *Polling* oder *Broadcasting*, sondern über manuelle Einträge erfolgen, ist dies durch den Eintrag *Browsing* in der *cupsd.conf* auszuschalten (*off*). Soll *Browsing* genutzt werden, ist der Zugriff nur auf die zwingend benötigten Rechner oder, wenn nötig, auf Netze zu beschränken.
* Verschlüsselung  
 Wenn die Druckaufträge oder Statusabfragen verschlüsselt übertragen werden sollen, muss ein Protokoll eingesetzt werden, das dies unterstützt. Das bei CUPS voreingestellte *Internet Printing Protocol* (IPP) kann durch den optionalen Einsatz von TLS/SSL (Transport Layer Security / Secure Sockets Layer) verschlüsselt kommunizieren.  
 Für die Verschlüsselung ist in der Konfigurationsdatei des CUPS-Clients (*client.conf*) der Eintrag *Encryption* erforderlich. Es wird empfohlen, diesen Wert möglichst auf *Always* zu setzen. Zusätzlich müssen hierfür TLS/SSL-Zertifikate und kryptografische Schlüssel auf dem CUPS-Server bereitgestellt werden.
* Hochverfügbarkeit  
 CUPS kann als Bestandteil eines hochverfügbaren Drucksystems betrieben werden. Das bedarf einer detaillierten Planung der damit verbundenen organisatorischen und technischen Aspekte. Insbesondere muss festgelegt werden, welcher grundlegende Ansatz verfolgt wird, um das angestrebte Verfügbarkeitsniveau zu erreichen, beispielsweise *failover-switching* oder *load-balancing*. Für *failover-switching* müssen in der Konfigurationsdatei *cupsd.conf* sogenannte implizite Druckklassen definiert werden (Konfigurationseintrag *ImplicitClasses On*). Vertiefende Informationen dazu sind in der Dokumentation von CUPS zu finden.
**Zugriff auf Drucker**

* Benutzerverwaltung  
 Auf Druckserver sollten nur berechtigte Benutzer zugreifen können. Die dafür benötigte Rechteverwaltung kann entweder auf dem Druckserver selbst gepflegt werden, oder es kann ein vorhandener Authentisierungsdienst eingebunden werden. Normale Benutzer sollten auf einem Druckserver nur die Drucker-Applikation benutzen können und keinen Zugriff auf die Dateien und Verzeichnisse dieses Servers haben.  
 Da in der Regel die Benutzer den Druckserver nur zum Drucken nutzen sollen und sich nicht direkt auf diesem Server anmelden sollen, beispielsweise mit SSH, sollte die Systembenutzergruppe von der Druckerbenutzergruppe getrennt werden. Druckerbenutzer sollten so angelegt werden, dass sie bis auf das Drucken keine weiteren Rechte auf dem Druckserver besitzen. Beispielsweise können mit dem Programmaufruf *lppasswd -a benutzername* Druckerbenutzer angelegt werden.  
 Die Zuordnung, welche Benutzer auf welche Drucker zugreifen dürfen, kann in der Datei *cupsd.conf* vorgenommen werden. Auch hier gilt der Grundsatz, dass Benutzern möglichst nur die tatsächlich erforderlichen Zugriffsrechte eingeräumt werden sollten.  
 Die Einstellung, dass alle Benutzer auf alle Drucker zugreifen dürfen, sollte vermieden werden. Eine Ausnahme in dieser Hinsicht ist der Betrieb von lokalen Druckern. Wenn es nur wenige Druckerbenutzer für ein IT-System gibt und wenn alle Druckerbenutzer ohnehin auch gleichzeitig Systembenutzer sind, brauchen keine separaten Druckerbenutzer angelegt zu werden.
* Authentisierungsverfahren:  
 CUPS unterstützt verschiedene Verfahren zur Authentisierung, wie HTTP-Basic, HTTP-Digest oder Authentisierung anhand von Zertifikaten. Das Authentisierungsverfahren kann über den Eintrag *AuthType* in der Konfigurationsdatei *cupsd.conf* festgelegt werden. Da bei HTTP-Basic Benutzernamen und Passwörter im Klartext übertragen werden, sollte dieses Verfahren nicht ohne zusätzliche Sicherheitsvorkehrungen eingesetzt werden. Stattdessen sollten Zertifikate oder HTTP-Digest als Authentisierungsmethode verwendet werden.
**Administration**

CUPS darf nur von autorisierten Personen administriert werden. Diese lassen sich in der Sektion */admin* der Konfigurationsdatei *cupsd.conf* festgelegen.

Bei CUPS können zahlreiche Konfigurationseinstellungen über einen mitgelieferten Webserver durchgeführt werden. Die Zugriffsmöglichkeiten auf den Webserver über Netze sind auf das erforderliche Mindestmaß zu beschränken. In der Konfigurationsdatei *cupsd.conf* in der Sektion */admin* können die Rechner eingetragen werden, die auf den Webserver zugreifen dürfen. Alternativ kann ein lokaler Paketfilter eingesetzt werden, um die Zugriffsmöglichkeiten auf den Webserver zu beschränken.

**Protokollierung **

CUPS bietet vielfältige Möglichkeiten zur Protokollierung von Ereignissen. Viele Aspekte, die in der Anforderung SYS.4.1.M8 *Protokollierung bei Druckern, Kopierern und Multifunktionsgeräten* erläutert sind, können durch entsprechende Einträge in der Konfigurationsdatei *cupsd.conf* umgesetzt werden. Der Detaillierungsgrad der Protokolle kann beispielsweise durch den Eintrag *LogLevel* festgelegt werden.

**Archivierung**

CUPS bietet Funktionen zur elektronischen Archivierung von ausgedruckten Dokumenten im Dateisystem des Druckservers. Hierzu dient der Konfigurationseintrag *PreserveJobs* in der Datei *cupsd.conf*. Als Option kann dabei auch die maximale Anzahl der archivierten Dokumente festgelegt werden. Ältere Einträge werden in diesem Fall von neuen Dokumenten überschrieben. Wenn Archive angelegt werden sollen, müssen die archivierten Dokumente durch entsprechende Mechanismen vor unbefugtem Zugriff und vor Datenverlusten geschützt werden. Weitere Hinweise finden sich im Baustein OPS.1.2.2 *Archivierung*.

#### SYS.4.1.M7 Beschränkung der Administrationszugriffe auf Drucker, Kopierer und Multifunktionsgeräte

Um Angriffe auf Drucker, Kopierer und Multifunktionsgeräte zu erschweren, muss der Zugriff auf diese Geräte beschränkt werden. Im Folgenden werden einige Aspekte beschrieben, die für den sicheren Betrieb von Druckern und Kopierern berücksichtigt werden sollten:

* Beschränkung auf notwendige Zugriffsrechte:  
 Wenn möglich, sollten nur so wenig Administratoren wie nötig den vollständigen Zugriff erhalten. Dabei sollten immer nur die Zugriffsrechte vergeben werden, die für die Aufgabenwahrnehmung notwendig sind.
* Absicherung der Administrationszugriffe:  
 Auf administrative Bereiche und die Konfiguration sollten nur autorisierte Personen zugreifen dürfen. Der Zugriff sollte erst nach einer Authentisierung, beispielsweise durch ein Passwort oder eine PIN, möglich sein. Falls Drucker, Kopierer oder Multifunktionsgeräte über ein Netz administriert werden, muss sichergestellt sein, dass sich die Administratoren hierfür ebenfalls authentisieren müssen. Wenn systemseitig keine Authentisierung unterstützt wird, müssen geeignete Ersatzmaßnahmen ergriffen werden.
* Absicherung der Administration bei Fernzugriff:  
 Alle Administrationszugriffe sollten möglichst nur über einen verschlüsselten Kanal stattfinden, damit keine Passwörter oder andere schutzbedürftige Informationen mitgehört werden können. Beispielsweise kann bei einigen Gerätetypen die Übertragung der Konfigurationsdaten über HTTPS oder SNMPv3 verschlüsselt werden. In diesem Fall sollte die unverschlüsselte Kommunikation unterbunden werden, indem beispielsweise die HTTP-Schnittstelle für die Konfiguration deaktiviert wird.
* Verzicht auf nicht benötigte Funktionen:  
 Drucker, Kopierer und Multifunktionsgeräte bieten oft mehr Funktionen, als im normalen Betrieb benötigt werden. Dadurch können sich unnötige Risiken ergeben. Daher sollten alle nicht benötigten Funktionen deaktiviert bzw. deren Nutzung so weit wie möglich eingeschränkt werden.
* Paketfilter:  
 In einigen Druckern sind Paketfilter integriert, über die Verbindungen anhand von IP-Adressen oder Portnummern gefiltert werden können. Alle Ports, die nicht für den Druckbetrieb und zur Konfiguration des Druckers benötigt werden, sind möglichst zu blockieren. Unterstützt das Gerät eine verschlüsselte Kommunikation, sollte die unverschlüsselte Kommunikation mit dem Gerät so weit wie möglich unterbunden werden, beispielsweise über die entsprechenden Portnummern.  
 Werden Druckserver eingesetzt, ist darauf zu achten, dass nur von diesen Servern eine Verbindung zu den Druckern aufgebaut werden darf. Hierdurch wird der Verbindungsaufbau von unautorisierten IT-Systemen zu den Druckern erschwert. Eine Ausnahme bilden allerdings Systeme, von denen aus Drucker konfiguriert werden sollen. Diese Systeme müssen natürlich ebenfalls auf den Drucker zugreifen können.  
 Die Paketfilter sind generell so restriktiv wie möglich zu konfigurieren. Das gilt auch für den Verbindungsaufbau von den Netzdruckern zu anderen IT-Systemen. Beispielsweise sollten die Paketfilter so konfiguriert werden, dass Netzdrucker keine Verbindungen zu einem IT-System außerhalb des LANs aufbauen können. Das erschwert den ungewollten Datenaustausch mit externen IT-Systemen, beispielsweise mit Computern im Internet. Unabhängig von lokalen Paketfiltern muss am zentralen Sicherheitsgateway die Kommunikation zwischen den Druckern und externen Netzen blockiert werden.
* Netzsegmentierung:  
 Oft ist es empfehlenswert, alle Drucker, Kopierer und Multifunktionsgeräte in einem logischen Netz zusammenzufassen. Das erleichtert es in vielen Fällen, sie zu konfigurieren und zu administrieren. Wird das konsequent umgesetzt, kann auf den zuständigen Routern und Gateways die Kommunikation zwischen den Druckern und anderen Netzsegmenten gezielt kontrolliert werden (sowohl Empfang als auch Versand von IP-Paketen).
#### SYS.4.1.M8 Versorgung und Kontrolle der Verbrauchsgüter [Innerer Dienst, Benutzer]

Drucker, Kopierer und Multifunktionsgeräte sind auf bestimmte Verbrauchsgüter (z. B. Papier, Toner, Tinte) angewiesen, um zu funktionieren. Daher muss die Versorgung mit Verbrauchsgütern vor Ort sichergestellt sein. Es sollten klare und eindeutige Regelungen existieren, welche Verbrauchsgüter von wem nachgefüllt bzw. bestellt werden.

Bestimmte Ressourcen dürfen nicht von jedem Mitarbeiter nachgefüllt oder beschafft werden, sondern nur von autorisierten Personen, beispielsweise sehr teure Produkte.

Alle Benutzer sollten informiert sein, wer zu benachrichtigen ist, wenn Verbrauchsgüter nachbeschafft oder aufgefüllt werden müssen. Für jede Sorte von Verbrauchsmaterial sollte jemand benannt werden, der für Versorgung und Kontrolle verantwortlich ist. Dieser Verantwortliche sorgt dafür, dass

* regelmäßig geprüft wird, ob ausreichende Vorräte vorhanden sind und ob vor Ort nachgefüllt werden muss,
* die Beschaffungsstelle rechtzeitig benachrichtigt wird, wenn Verbrauchsmaterial nachbestellt werden muss,
* verbrauchte oder leere Verbrauchsmaterialien geeignet entsorgt werden und
* die Verbrauchsmaterialien am Gerät ausgetauscht werden, falls das nicht durch die Benutzer erfolgen soll.
Die Versorgung mit Verbrauchsgütern ist von der Beschaffungsstelle ausreichend sicherzustellen.

#### SYS.4.1.M9 Protokollierung bei Druckern, Kopierern und Multifunktionsgeräten

Die Aktivitäten an Druckern, Kopierern und Multifunktionsgeräten sollten aus vielen Gründen überwacht und protokolliert werden. Zum einen hilft eine aktivierte Protokollierung, potenzielle Schwachstellen möglichst frühzeitig zu erkennen und zu beseitigen. Zum anderen dient sie dazu, Verstöße gegen die Sicherheitsrichtlinie zu erkennen oder Nachforschungen über einen Sicherheitsvorfall anzustellen. Außerdem kann die Überwachung meist auch genutzt werden, um frühzeitig zu erkennen, ob Verbrauchsmaterialien nachgefüllt werden müssen.

Folgende zentrale Fragen sollten bei der Protokollierung an Druckern, Kopierern und Multifunktionsgeräten mindestens beantwortet werden:

* Welche Informationen sollen protokolliert werden?
* Wie soll protokolliert werden?
* Wer ist berechtigt bzw. zuständig, die Protokolle auszuwerten?
* Wie und wann werden die Protokolle ausgewertet?
* Wer soll wie benachrichtigt werden, wenn bestimmte Ereignisse eintreten?
* Wie lange müssen und dürfen die Protokolldaten aufbewahrt werden und wie erfolgt die Löschung?
Es muss sorgfältig ausgewählt werden, welche Informationen protokolliert werden sollen. Werden zu viele Informationen gespeichert, könnten bei der Auswertung wichtige Ereignisse übersehen werden. Wird zu wenig protokolliert, werden eventuell wichtige Informationen nicht erfasst. 

Aus Sicherheitssicht haben sich die folgenden Ereignisse als besonders relevant für die Protokollierung erwiesen, die Aufzählung ist dabei absteigend nach der Priorität sortiert:

* Änderungen der Konfigurationseinstellungen sind immer zu protokollieren.
* Es sollten fehlgeschlagene und bei einem höheren Schutzbedarf zusätzlich auch erfolgreiche Authentisierungsvorgänge protokolliert werden. Das betrifft sowohl lokale Anmeldungen als auch Zugriffe über das Netz.
* Die Systemressourcen und Messwerte zur Betriebssicherheit sind immer auf kritische Werte hin zu überwachen. Hierzu gehören beispielsweise Informationen über die Temperatur, die Auslastung und den freien Speicherplatz.
* Um Engpässe bei der Versorgung zu vermeiden, sollten Informationen zum Verbrauch von Papier und Toner protokolliert und ausgewertet werden.
* Einträge, wer zu welcher Uhrzeit gedruckt oder das Gerät benutzt hat, können eventuell ebenfalls aufgezeichnet werden, könnten aber zu datenschutzrechtlichen Problemen führen.
Je nach Gerät und Anwendungsfall kann es zweckmäßig sein, den Protokollierungsumfang anders festzulegen oder zusätzliche Ereignisse zu betrachten, beispielsweise wann ein Gerät ein- oder ausgeschaltet wurde. Der Protokollierungsumfang hängt in der Praxis auch davon ab, inwieweit der jeweilige Gerätetyp die Protokollierung der unterschiedlichen Ereignisse technisch unterstützt.

Generell sollten nur berechtigte Personen auf die protokollierten Informationen zugreifen können. Es sollte verhindert werden, dass z.B. auf den Displays der Geräte oder in Druckerwarteschlagen angezeigt wird, wer wann welches Dokument ausdrucken, scannen oder versenden wird oder bereits ausgedruckt, gescannt oder versendet hat.

Nachdem festgelegt wurde, welche Informationen protokolliert werden sollen, muss geklärt werden, wo die Protokolldaten abgelegt werden. Falls möglich, sollten hierfür zentrale Protokollierungsserver genutzt werden. Ansonsten müssen die Protokolldateien lokal auf den einzelnen Geräten gespeichert werden. 

Für die Protokollierung bei vernetzten IT-Systemen sollte eine Zeitsynchronisation eingesetzt werden. Sie dient dazu, die Ereignisse zuverlässig mit den zu protokollierenden Informationen von anderen Systemen vergleichen zu können.

Protokolldaten müssen nicht nur gespeichert, sondern auch systematisch ausgewertet werden. Auch hierfür muss festgelegt werden, wer zuständig ist und welche Vorgehensweise einzuhalten ist. Empfehlungen dazu finden sich im Baustein OPS.1.1.6 *Protokollierung*.

Wenn unerwartete oder auffällige Ereignisse in den Protokollen auftreten, muss entsprechend reagiert werden. Viele fehlerhafte Authentisierungsversuche können beispielsweise auf einen Angriff oder auf nicht ausreichend informierte Benutzer hindeuten. Aber auch normale Ereignisse können eine Reaktion erforderlich machen: Erreichen beispielsweise Verbrauchsmaterialien einen minimalen Füllstand, muss rechtzeitig für Ersatz gesorgt werden. Daher sollte der zuständige Administrator beziehungsweise Verantwortliche für die Verbrauchsmaterialien zeitnah informiert werden. 

Sofern personenbezogene Daten archiviert werden, müssen die hierfür geltenden Gesetze und Vorschriften eingehalten werden. Dazu gehören vor allem das Bundesdatenschutzgesetz (BDSG) und die entsprechenden Gesetze der Länder. Weitere Informationen hierzu sind im Baustein OPS.1.1.6 *Protokollierung* zu finden.

#### SYS.4.1.M10 Einsatz von netzfähigen Dokumentenscannern

Über Dokumentenscanner können analoge Informationen digitalisiert werden, beispielsweise um ein Papierdokument auf IT-Systeme zu kopieren, zu archivieren oder weiter zu bearbeiten. Statt an jedem Arbeitsplatz-PC einen lokalen Scanner zu installieren, ist es meist wirtschaftlicher, einen oder mehrere zentrale Scanner zur Verfügung zu stellen. Um geeignete Sicherheitsmaßnahmen auszuwählen, muss zwischen Scan-PCs und netzfähigen Dokumentenscannern unterschieden werden.

Ein Scan-PC ist ein Standard-PC, der oft an ein LAN angebunden ist und an den ein lokaler Scanner angeschlossen ist. Scan-PCs werden häufig in ähnlichen Räumlichkeiten wie Netzdrucker betrieben und können von diversen Mitarbeitern benutzt werden. Außerdem ist auf Scan-PCs üblicherweise Software installiert, mit der die eingescannten Informationen nachbearbeitet werden können, also beispielsweise OCR- oder Bildbearbeitungsprogramme.

Netzfähige Dokumentenscanner (*Büroscanner*) sind Kompaktgeräte, an denen Papierdokumente und Ähnliches ohne größeren Aufwand eingelesen und zur weiteren Bearbeitung über ein LAN an den Benutzer übertragen werden können, beispielsweise per E-Mail. Diese Funktion ist häufig auch in Faxgeräten integriert. Der Funktionsumfang von netzfähigen Dokumentenscannern ist meist deutlich geringer als bei Scan-PCs. 

**Scan-PC **

Wird ein Standard-PC zum Scannen verwendet, so sind die Empfehlungen aus den Baustein SYS.2.1. Allgemeiner Client und den zutreffenden betriebssystemspezifischen Client-Bausteinen des IT-Grundschutz-Kompendiums umzusetzen. 

Scan-PCs können im Produktivnetz, in einem Testnetz oder auch als Stand-Alone-System ohne einen Netzanschluss betrieben werden. Sie sollten so konfiguriert sein, dass sich die Benutzer authentisieren müssen. Die eingescannten Daten können über das Netz oder über transportable Datenträger zu den Arbeitsplatz-PCs übertragen werden. 

Die analogen Scan-Vorlagen sollten nicht unbeaufsichtigt beim Gerät verbleiben. Auch die digitalen Scan-Ergebnisse sollten nach der Übertragung auf das gewünschte Zielsystem, zum Beispiel auf den Arbeitsplatz-PC des jeweiligen Benutzers, aus allen allgemein zugreifbaren Verzeichnissen gelöscht werden.

**Netzfähige Dokumentenscanner**

Mit diesen Geräten können auch ohne einen angeschlossenen PC Dokumente gescannt werden. Dabei werden die Dokumente in Bild-Dateien mit gängigen Dateiformaten umgewandelt.

Zur weiteren Bearbeitung müssen die Geräte die eingescannten Dokumente an andere IT-Systeme im Netz versenden. Folgende Übertragungs- und Speicherverfahren werden in der Regel unterstützt:

* Ablage auf Netzlaufwerke.  
 Die eingescannten Dokumente werden direkt über ein Netzprotokoll auf einen Datei-Server übertragen. Unterstützt werden in der Regel NFS- und SMB-Freigaben oder die Übertragung mittels FTP. Grundsätzlich muss sichergestellt werden, dass der Personenkreis, der Zugriff auf die Zielverzeichnisse mit den eingescannten Daten hat, so klein wie möglich ist. Bei erhöhtem Schutzbedarf ist es eventuell erforderlich, dass nur der Benutzer, der die Informationen eingescannt hat, auch auf die Scan-Ergebnisse zugreifen kann. Nicht alle Scanner ermöglichen es, die erzeugten Dateien in benutzerspezifischen Bereichen der Server zu speichern. Wenn hierfür nur ein allgemein zugreifbares Verzeichnis gewählt werden kann, müssen die Dokumente so schnell wie möglich aus diesen öffentlichen Verzeichnissen gelöscht werden. Die Benutzer müssen entsprechend angewiesen werden. Zusätzlich sollten diese Verzeichnisse einmal täglich automatisch gelöscht werden. Der Zeitpunkt muss den Benutzern bekannt gegeben werden und ist so zu wählen, dass zu diesen Zeiten keine Benutzer mit den Scannern arbeiten.
* Scan-to-Mail:  
 Hierbei hat der Benutzer beim Scannen die Möglichkeit, eine E-Mail-Adresse oder eine Benutzer-Kennung, der eine E-Mail-Adresse zugeordnet ist, anzugeben. An diese E-Mail-Adresse wird die erzeugte Datei über einen voreingestellten SMTP-Server übermittelt. Da auf diese Weise vertrauliche Informationen anonym das Netz verlassen könnten, sollte darauf geachtet werden, dass keine externen E-Mail-Adressen eingegeben werden können. Besser ist es, auch den SMTP-Server so zu konfigurieren, dass von den netzfähigen Dokumentenscannern keine E-Mails an externe E-Mail-Adressen versendet werden können.
* Scan-to-Print:  
 Hier wird das Dokument direkt an einen Drucker gesendet, also die Scanner-Drucker-Kombination als digitaler Kopierer eingesetzt. Sind beide Geräte räumlich voneinander getrennt, besteht die Gefahr, dass während des Scannens die Dokumente unbefugt vom Drucker entfernt werden. Daher sollten die Systeme in diesem Fall möglichst so konfiguriert werden, dass der Ausdruck erst erfolgt, wenn alle Seiten des jeweiligen Dokuments vollständig eingescannt sind. Anderenfalls vergeht zwischen dem Scannen der ersten Seite und dem Abholen am Drucker unter Umständen zu viel Zeit.
* Scan-to-Fax:  
 Das Verfahren Scan-to-Fax erlaubt es, eingescannte Dokumente direkt per Fax zu versenden. Hierfür wird beim Scannen eine Fax-Nummer angegeben. Das erzeugte Dokument wird dann entweder über ein integriertes Modem versendet, oder der Scanner baut über das LAN eine Verbindung zu einem Fax-Server auf.  
 Beim Einsatz von Scannern, die über eingebaute Fax- oder Modem-Schnittstellen verfügen, müssen besondere Sicherheitsvorkehrungen getroffen werden, damit über diese Schnittstellen keine unerwünschten Kommunikationsverbindungen mit externen Netzen aufgebaut werden. Entsprechende Empfehlungen sind in der Anforderung SYS.4.1.M10 *Netztrennung beim Einsatz von Multifunktionsgeräten* beschrieben.  
 Wenn möglich, sollte ein zentraler Fax-Server als Schnittstelle zwischen Scanner und Telefonnetz agieren. In diesem Fall sind insbesondere die Maßnahmen-Empfehlungen, die im Baustein NET.4.3 *Fax* aufgeführt sind, anzuwenden. 
Wenn die eingesetzten Komponenten dies unterstützen, sollten die Kommunikationsverbindungen möglichst verschlüsselt werden, um zu erschweren, dass Angreifer die übertragenen Informationen abhören. Hinweise, wie die Übertragung geschützt werden kann, sind unter anderem auch in der Anforderung SYS.4.1.M14 *Informationsschutz bei Druckern, Kopierern und Multifunktionsgeräten* zu finden.

Scanner sollten auch vor Angriffen aus dem Netz geschützt werden. Hierfür sollte die Anforderung SYS.4.1.M6 *Beschränkung der Zugriffe auf Drucker, Kopierer und Multifunktionsgeräte* berücksichtigt werden. 

Nach dem Scannen dürfen keine Restinformationen auf dem System verbleiben. Die Dokumentenspeicher des Geräts sollten möglichst automatisch gelöscht werden, wenn der Scan-Vorgang abgeschlossen ist. Ist das nicht realisierbar, müssen die Benutzer darauf hingewiesen werden, dass sie die Dokumentenspeicher des Geräts nach der Benutzung manuell löschen müssen, damit nachfolgende Benutzer die eingescannten Informationen nicht einsehen können. Entsprechende Sicherheitsvorkehrungen müssen auch für sonstige Speicherbereiche getroffen werden, die im Rahmen des Scan-Vorgangs verwendet werden, beispielsweise für die dabei benutzten Netzlaufwerke.

#### SYS.4.1.M11 Netztrennung beim Einsatz von Multifunktionsgeräten

Häufig ist es unter wirtschaftlichen oder praktischen Gesichtspunkten nicht zweckmäßig, separate Geräte zum Drucken, Scannen, Kopieren und Fax-Versand/Empfang einzusetzen. Als Alternative sind Multifunktionsgeräte, die auch als All-in-One-Geräte bezeichnet werden, erhältlich, die mehrere oder sogar alle diese Funktionen in einem Gerät unterstützen. Teilweise bieten diese Geräte auch zusätzliche Kommunikationsschnittstellen, beispielsweise für Webzugriffe.

Multifunktionsgeräte haben meist gegenüber Einzelgeräten einen geringeren Administrationsaufwand und benötigen weniger Anschlussleitungen (Energie- und eventuell auch Datenleitungen). Multifunktionsgeräte können in der Regel direkt oder über ein LAN an Arbeitsplatzrechner angeschlossen werden. 

Einige Geräte bieten eine Fax- und Modem-Funktionalität, die den Anschluss an ein Telefonnetz voraussetzt, sodass über die Kopplung mit anderen IT-Systemen eine physische Verbindung zwischen dem LAN und dem Telefonnetz entstehen kann. Falls diese Verbindung nicht von einem Sicherheitsgateway kontrolliert wird, sind hierüber unter Umständen unkontrollierte Internet-Zugriffe möglich, sodass beispielsweise Angreifer von außen auf das LAN zugreifen könnten. Der unberechtigte Aufbau von Datenverbindungen sowie ungewollten Fernwartungen muss in jedem Fall unterbunden werden. 

Eine Ausnahme sind Multifunktionsgeräte mit Fax-Funktionalität, die nicht an ein Telefonnetz angeschlossen werden müssen. Diese Geräte scannen Dokumente ein und senden sie über eine Datenverbindung an einen zentralen Fax-Server, der sich typischerweise ebenfalls im LAN befindet. Erst der Fax-Server, der an das Telefonnetz angeschlossen ist, versendet das Fax an den eigentlichen Empfänger. Wird ein Fax-Server verwendet, sind die im Baustein NET.4.3 *Fax* empfohlenen Maßnahmen umzusetzen. 

Wenn Multifunktionsgeräte an ein Telefonnetz angeschlossen werden können, muss zunächst entschieden werden, ob dieser Anschluss tatsächlich erforderlich ist, das heißt, ob die entsprechende Fax- oder Modem-Funktionalität benötigt wird. Falls auf den Anschluss an das Telefonnetz verzichtet werden kann, sind möglichst folgende Schutzmaßnahmen zu ergreifen:

* Die Fax- bzw. Modem-Funktionalität ist auf dem Gerät zu deaktivieren.
* Das Kabel für den Anschluss an das Telefonnetz ist zu entfernen. Keinesfalls darf das Kabel in die Telefondose eingesteckt werden.
* Wenn sich das Gerät an einem frei zugänglichen Ort befindet, sollten möglichst die Telefondosen in dem jeweiligen Raum deaktiviert oder die Schnittstelle zum Telefonnetz aus dem Gerät ausgebaut werden. Ist beides nicht möglich, sollte regelmäßig kontrolliert werden, ob nicht unbefugt die Verbindung zum Telefonnetz hergestellt worden ist.
Wenn die Fax- oder Modem-Funktionalität des Multifunktionsgerätes genutzt werden soll, muss sichergestellt sein, dass der hierfür erforderliche Anschluss an das Telefonnetz nicht zu unkontrollierten Datenverbindungen zwischen dem LAN und Fremdnetzen führen kann. Folgende Ansätze sind möglich:

* Das Multifunktionsgerät wird an einen Stand-Alone-PC angeschlossen, das heißt an einen Rechner, der nicht mit dem LAN verbunden ist. Nachteilig bei diesem Ansatz ist, dass Daten in vielen Fällen mithilfe von Datenträgern zwischen dem Stand-Alone-PC und dem LAN transportiert werden müssen (siehe auch SYS.3.4 Mobile Datenträger).
* Eine Alternative ist, das Multifunktionsgerät oder den Rechner, an dem das Gerät angeschlossen ist, mithilfe eines zusätzlichen Sicherheitsgateways vom LAN zu trennen. 
* Eine weitere Alternative ist, das Multifunktionsgerät oder den Rechner, an dem das Multifunktionsgerät angeschlossen ist, in einer demilitarisierten Zone (DMZ) eines bestehenden Sicherheitsgateways zu platzieren. 
Alle genannten Lösungsansätze müssen systematisch im Sicherheitskonzept berücksichtigt werden und erfordern zusätzliche Sicherheitsmaßnahmen, beispielsweise zum Schutz vor schädlichem Code.

#### SYS.4.1.M12 Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln [Leiter Haustechnik, Benutzer]

Betriebsmittel (z. B. Papier, Festplatten, Flash-Speicher oder -karten, aber auch spezielle Tonerkassetten) werden irgendwann nicht mehr benötigt oder müssen aufgrund von Defekten ausgesondert werden. Wenn sie schützenswerte Daten enthalten, müssen sie so entsorgt werden, dass keine Rückschlüsse auf vorher gespeicherte Daten möglich sind. Bei funktionstüchtigen Datenträgern, die sich in Druckern, Kopierern und Multifunktionsgeräten befinden, sollten die Daten physisch gelöscht werden. Nicht funktionierende Datenträger müssen mechanisch zerstört werden (siehe OPS.1.18 *Löschen und Vernichten*).

Die Art der Entsorgung schutzbedürftigen Materials sollte in einer speziellen Sicherheitsrichtlinie geregelt werden. In der Institution müssen die dafür benötigten Entsorgungseinrichtungen vorhanden sein, z. B. Aktenvernichter.

Wird schutzbedürftiges Material erst gesammelt und dann entsorgt, so ist die Sammlung unter Verschluss zu halten und vor unberechtigtem Zugriff zu schützen.

Soweit sich in der Institution keine umweltgerechte und sichere Entsorgung durchführen lässt, sind damit beauftragte Unternehmen darauf zu verpflichten, die erforderlichenr Sicherheitsmaßnahmen einzuhalten. Ein Mustervertrag findet sich unter den Hilfsmitteln zum IT-Grundschutz auf den BSI-Webseiten. Es sollte regelmäßig geprüft werden, ob der Entsorgungsvorgang verlässlich ist.

#### SYS.4.1.M13 Sichere Außerbetriebnahme von Druckern, Kopierern und Multifunktionsgeräten

Sollen Drucker, Kopierer, Multifunktionsgeräte oder einzelne Komponenten solcher Geräte außer Betrieb genommen oder ersetzt werden, müssen alle sicherheitsrelevanten Informationen von den Geräten gelöscht werden (siehe OPS.1.18 Löschen und Vernichten). Dies gilt besonders dann, wenn die Komponenten ausgesondert und an Dritte weitergegeben werden. Beispiele hierfür sind Verkauf, Rückgabe nach Leasing, Austausch durch den Hersteller und Reparatur durch eine Service-Firma. Aber selbst dann, wenn die Geräte intern weiter verwendet oder verschrottet werden, müssen alle schutzbedürftigen Informationen auf den Geräten gelöscht werden.

Handelt es sich um Miet- oder Leihgeräte, ist im Vorfeld vertraglich zu klären, ob die Datenträger mit den Geräten zurückgegeben werden müssen beziehungsweise wie die Daten auf den Datenträgern zuverlässig gelöscht werden können.

Je nach Einsatzzweck und Gerätetyp können beispielsweise folgende sicherheitsrelevante Informationen gespeichert sein:

* **Zwischengespeicherte Informationen:** Bei digitalen Kopierern wird in der Regel erst das gesamte Dokument eingescannt, bevor es ausgedruckt wird. Auch bei Druckern wird das Dokument erst zwischengespeichert. Dazu sind in den Geräten Speicherkomponenten eingebaut, meist in Form von Festplatten. Unter Umständen können die zwischenzeitlich gelöschten Dokumente wieder hergestellt werden. Einige Geräte bieten eine Funktion, um den Inhalt des Speichers zu löschen.
* **Konfigurationseinstellungen:** Besonders bei netzfähigen Geräten geben die Konfigurationseinstellungen, wie IP-Adressen, eventuell Hinweise auf die Netzstruktur. Die Konfigurationseinstellungen sollten daher gelöscht oder in den Lieferzustand zurückgesetzt werden. Viele Geräte bieten hierfür entsprechende Funktionen.
* **Passwörter:** Bei vielen Geräten ist eine Passwort- oder Token-basierte Authentisierung vorgesehen, bei einigen allerdings nur für die Administration. Es gibt jedoch auch Geräte, bei denen für alle Benutzerzugriffe eine Authentisierung aktiviert werden kann. Alle Passwörter sollten auf den Lieferzustand zurückgesetzt werden.
* **Zertifikate:** Einige Geräte können eine zertifikatsgestützte Authentisierung einbinden, beispielsweise über IEEE 802.1X. Alle Zertifikate sollten auf den Lieferzustand zurückgesetzt werden.
* **Weitere Restinformationen:** Unter Umständen kann über Verbrauchsmaterialien, wie Toner-Trommeln, auf die ausgedruckten Dokumente geschlossen werden. Bei höherem Schutzbedarf sollte anhand einer Risikoabschätzung entschieden werden, ob benutzte Verbrauchsmaterialien vernichtet werden müssen.
Bevor Geräte außer Betrieb genommen oder an Dritte weitergegeben werden, muss der interne Speicher gelöscht werden. Wenn die Festplatte ausgebaut werden kann, wird empfohlen, diese separat zu löschen. Nachdem der Speicher gelöscht wurde, muss überprüft werden, ob das auch erfolgreich war.

Die Vorgehensweise hängt dabei stark von der Art und vom Verwendungszweck des jeweiligen Gerätes ab. Sind auf dem Gerät besonders sicherheitskritische Informationen gespeichert und kann nicht mit hinreichender Sicherheit gewährleistet werden, dass die Daten wirklich gelöscht sind, so kann es erforderlich sein, den Speicher physisch zu zerstören bzw. unbrauchbar zu machen.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.4.1.M14 Authentisierung bei Druckern, Kopierern und Multifunktionsgeräten(CI)

Im normalen Büroalltag ist es oft einfach, Ausdrucke vertraulicher Dokumente direkt am Drucker einzusehen, solange diese noch nicht abgeholt wurden. Daher müssen Maßnahmen ergriffen werden, die den Zugriff auf fremde Dokumente erschweren.

Generell sollten nur berechtigte Personen auf die ausgedruckten oder kopierten Dokumente zugreifen können. Der Kreis der berechtigten Personen ist so klein wie möglich zu halten.

Kann der Zugang zu einem Netzdrucker nicht beschränkt werden, sollte überlegt werden, Geräte einzusetzen, die eine Authentisierungsfunktion für Benutzer bieten. Ist diese Funktion aktiviert, wird das Dokument erst ausgedruckt, nachdem sich der Benutzer, der den entsprechenden Druckauftrag abgesendet hat, am Gerät identifiziert und authentisiert hat. In der Praxis werden zur Authentisierung häufig Chipkarten oder PINs verwendet. Dabei können PINs je nach Gerätetyp benutzer- oder dokumentenspezifisch festgelegt werden. Bei letzterer Variante wird eine PIN festgelegt, wenn der Druckauftrag abgesendet wird. Erst nachdem diese PIN am Gerät eingegeben wurde, wird das Dokument, das der PIN zugeordnet ist, ausgedruckt. Druckaufträge, die zwar abgesendet, aber nicht abgeholt wurden, müssen regelmäßig gelöscht werden. Die Drucker sollten möglichst so konfiguriert werden, dass bei mehrmaliger Eingabe einer falschen PIN der Druckauftrag automatisch gelöscht wird. 

Ein weiterer Sicherheitsgewinn kann erzielt werden, wenn das zu druckende Dokument vom Arbeitsplatz-PC verschlüsselt zum Drucker übertragen und verschlüsselt zwischengespeichert wird. Erst nach einer erfolgreichen Authentisierung direkt am Drucker wird das Dokument entschlüsselt und ausgedruckt.

Es gibt auch Kopierer, die eine ähnliche Authentisierungsfunktion bieten, meist als optionale Erweiterung. Erst nachdem eine Chipkarte eingelesen oder eine PIN eingegeben wurde, können die Benutzer kopieren. Obwohl diese Authentisierungsfunktionen hauptsächlich für Kostenabrechnungen angeboten werden, können Angreifer durch diese Erweiterungen schwerer unberechtigt Kopien erstellen. 

Wenn an Netzdruckern oder Kopierern häufig hochvertrauliche Dokumente gedruckt beziehungsweise vervielfältigt werden müssen, sollte überlegt werden, hierfür Geräte mit Authentisierungsmöglichkeit einzusetzen.

#### SYS.4.1.M15 Informationsschutz bei Druckern, Kopierern und Multifunktionsgeräten(CI)

Damit ein Ausdruck erstellt werden kann, müssen die erforderlichen Informationen vom Arbeitsplatzrechner zum Drucker übertragen werden. Bei Kopierern findet das meist intern zwischen Scannereinheit und Speicher statt. Ein Angreifer könnte versuchen, auf den Speicher zuzugreifen oder die Informationen bei der Übertragung zum Drucker abzuhören. 

Es sollte gewährleistet werden, dass die Informationen nach dem Ausdruck aus dem Zwischenspeicher gelöscht werden (siehe SYS.4.1.M5 *Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten* und *SYS.4.1.M3 Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten*). Falls häufig Informationen mit einem höheren Schutzbedarf ausgedruckt oder kopiert werden, ist zu beachten, dass einfaches Löschen nicht ausreicht, um zu verhindern, dass gelöschte Daten wiederhergestellt werden können (siehe OPS.1.18 Löschen und Vernichten). Einige Geräte besitzen hierfür Mechanismen zum *sicheren Löschen*. Hierbei handelt es sich um eine Löschfunktion, welche die Daten zusätzlich überschreibt. Falls eine solche Funktion vorhanden ist, muss sie aktiviert werden. Andernfalls müssen adäquate Alternativlösungen gefunden werden.

Wenn möglich, sollten auch Maßnahmen ergriffen werden, die es einem Angreifer erschweren, auf den Speicher physisch zuzugreifen bzw. die Festplatten auszubauen. Um erkennen zu können, ob versucht wurde, den internen Speicher auszubauen oder zu manipulieren, sollten die Geräte versiegelt werden. Generell sollten Drucker, Kopierer und Multifunktionsgeräte so aufgestellt werden, dass sich niemand unbeobachtet an ihnen zu schaffen machen kann. 

Als zusätzlicher Schutz wird empfohlen, die Informationen in den internen Speichern verschlüsselt zu speichern. Zahlreiche Drucker, Kopierer und Multifunktionsgeräte bieten diese Funktion an. Wenn das eingesetzte Gerät eine verschlüsselte Speicherung unterstützt, sollte diese Funktion aktiviert werden. 

Die Kommunikation zwischen Arbeitsplatzrechnern, Druckservern und Netzdruckern erfolgt meist über ein Datennetz, für das die gleichen Gefährdungen wie bei anderen Datenverbindungen zu beachten sind. Damit diese Kommunikation nicht abgehört werden kann, sollten daher die Druckaufträge möglichst verschlüsselt übertragen werden. 

Einige Druckprotokolle, wie das besonders bei Unix-Systemen weit verbreitete LPR/LPD-Protokoll (Line Printer Remote / Line Printer Daemon), unterstützen keine Verschlüsselung. Ähnlich ist die Situation bei SMB/CIFS (Server Message Block / Common Internet File System) unter Windows. 

Daher sollte ein Protokoll wie IPP (Internet Printing Protocol) gewählt werden, das eine Verschlüsselung unterstützt, beispielsweise TLS/SSL (Transport Layer Security / Secure Sockets Layer) in Verbindung mit IPP. 

Unter Unix-Systemen sollte beispielsweise das Common Unix Printing System (CUPS) eingesetzt werden, das bei neueren Versionen in der Voreinstellung zur Kommunikation zwischen Client und Druckserver das Protokoll IPP verwendet. Durch eine entsprechende Konfiguration kann dabei TLS/SSL aktiviert werden.

#### SYS.4.1.M16 Notfallvorsorge bei Druckern, Kopierern und Multifunktionsgeräten

Fallen Drucker, Kopierer und Multifunktionsgeräte länger aus, ist das für die meisten Institutionen nicht tolerierbar. Besonders durch einen Ausfall zentraler Komponenten, die für die gesamte Drucker-Infrastruktur erforderlich sind, werden Geschäftsprozesse erheblich beeinträchtigt. Je nach Verfügbarkeitsanforderungen sind daher geeignete Maßnahmen zu ergreifen, um die Ausfallzeit beziehungsweise deren Auswirkungen zu verringern.

Es ist darauf zu achten, dass immer genügend Verbrauchsmaterial verfügbar ist, z. B. Toner und Papier. Ab einer bestimmten Restmenge, die vom Verbrauch abhängig ist, muss neues Verbrauchsmaterial beschafft und bereitgestellt werden. 

An jedem Kopierer, Drucker und Multifunktionsgerät sowie auch an anderen Komponenten des Drucksystems müssen diverse Konfigurationseinstellungen vorgenommen werden. Um diese Einstellungen nach einem Ausfall oder Austausch schnell wieder korrekt einrichten zu können, müssen die Konfigurationen systematisch dokumentiert werden. 

Je weniger Geräte verfügbar sind, desto gravierender ist es, wenn ein einzelnes ausfällt. Der Ausfall eines Druckservers ist besonders problematisch, da diese Geräte oft nur einmal oder wenige Male vorhanden sind. 

Um auf Notfälle reagieren zu können, sollte zwischen zentralen Komponenten einerseits und Druckern, Kopierern und Multifunktionsgeräten andererseits unterschieden werden. Bei einem höheren Schutzbedarf bezüglich der Verfügbarkeit sollte überlegt werden, zentrale Komponenten, wie Druckserver, redundant auszulegen. Wenn der einzige zentrale Server ausfällt, könnte sonst eventuell im gesamten LAN nicht mehr gedruckt werden.

Dezentrale Komponenten, wie Drucker, sind häufig auf mehreren Etagen oder in verschiedenen Büros eines Gebäudes zu finden. Generell sollte die Druckerlandschaft so gestaltet werden, dass die Benutzer beim Ausfall eines Druckers problemlos einen anderen Drucker verwenden können.

* Es sollte überlegt werden, für lokale Drucker, die einen höheren Schutzbedarf bezüglich der Verfügbarkeit haben und direkt an einen Arbeitsplatz angeschlossen werden, Ersatzgeräte bereitzustellen (*Cold Standby*). Bei einem Ausfall könnte der defekte Drucker zeitnah gegen das Ersatzgerät ausgetauscht werden.
* Für große Kopierer, Drucker und Multifunktionsgeräte die von mehreren Personen benutzt werden, sollten Wartungsverträge mit einer dem Schutzbedarf angemessenen Reaktionszeit abgeschlossen werden.
* Es sollte eine Liste von Fachhändlern geführt werden, bei denen unproblematisch neue Geräte beschafft werden können.
* Bei Bedarf können Ersatzteile gelagert werden, die häufig benötigt werden. Das ist allerdings nur sinnvoll, wenn entsprechendes Fachwissen vorhanden ist, um die Ersatzteile selbstständig austauschen zu können.
3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

**3.1.1 Kriterien für die Beschaffung und geeignete Auswahl von Druckern, Kopierern und Multifunktionsgeräten**

Wenn neue Drucker, Kopierer oder Multifunktionsgeräte beschafft werden, können diese von vornherein so ausgewählt werden, dass im späteren Betrieb mit geringem personellen und organisatorischen Zusatzaufwand ein hohes Maß an Sicherheit erreicht werden kann.

Viele Drucker und Kopierer sind modular aufgebaut. Das Grundgerät kann um zusätzliche Funktionen erweitert werden. Hierzu gehören beispielsweise auch zusätzliche Sicherheitsmechanismen, wie die Unterstützung einer Authentisierung über PINs oder Chipkarten. Bevor Drucker, Kopierer und ähnliche Geräte beschafft werden, sind daher neben den allgemeinen Anforderungen auch die Sicherheitsanforderungen festzulegen. Die Anforderungen und die auf dieser Basis getroffenen Entscheidungen sind zu dokumentieren. Nachfolgend werden einige grundsätzliche Anforderungen bei der Beschaffung von Druckern aufgelistet:

* Grundlegende funktionale Anforderungen 

 
	+ Sollen netzfähige Geräte beschafft werden?
	+ Ist die Leistungsfähigkeit des Geräts der Größe des Benutzerkreises angemessen?
	+ Was für ein Druckertyp mit welchem Druckverfahren soll angeschafft werden?
	+ Kann das Gerät nachträglich durch zusätzliche Funktionen erweitert werden?  
	 Viele Geräte können durch entsprechendes Zubehör beispielsweise Netzfähigkeit, Duplexdruck, zusätzliche Papierschächte und eine Authentisierung nachgerüstet werden.
	+ Kann akzeptiert werden, dass auf den Ausdrucken Wasserzeichen hinterlassen werden, die eine Zuordnung eines Ausdrucks zu einem konkreten Drucker zulassen ("Yellow Dots")?
	  

 
* Allgemeine Sicherheit 

 
	+ Unterstützt das System sichere Protokolle zur Administration?  
	 Damit die Geräte von zentraler Stelle aus administriert werden können, müssen netzfähige Geräte sichere Protokolle zur Administration unterstützen, bei einer Browser-basierten Konfiguration beispielsweise SSL/TLS.
	+ Können Informationen verschlüsselt gespeichert werden?  
	 Um nach einem (unberechtigten) Ausbau der Festplatte den Zugriff auf die Daten zu verhindern, legen einige Geräte die Informationen verschlüsselt auf der Festplatte ab.
	+ Ist eine Möglichkeit der Authentisierung direkt am Gerät vorgesehen (z. B. über Passwort- oder PIN-Eingaben oder Chipkarten) oder kann diese Funktion nachträglich eingebaut werden?  
	 Bei vielen Geräten ist eine Authentisierung vorgesehen, bei einigen allerdings nur für die Administration, um Zugriffe auf die Konfiguration abzusichern. Es gibt jedoch auch Geräte, bei denen sich alle Benutzerzugriffe absichern lassen, sodass Informationen erst ausgedruckt werden, wenn sich der Benutzer am Gerät authentisiert hat. Das dient als Schutz davor, dass an einen Netzdrucker übertragene oder an einem Kopierer eingescannte Informationen von Unberechtigten ausgedruckt werden können. Eine solche Funktion kann auch für eine Kostenkontrolle verwendet werden.
	+ Sind Ösen oder andere Möglichkeiten vorhanden, um die Geräte physisch vor Diebstahl zu schützen?
	+ Können Manipulationen an der Hardware durch Gehäuseschlösser oder ähnliche Vorkehrungen erschwert werden?  
	 Häufig kommt es beispielsweise vor, dass Speichermodule aus Druckern, Kopierern oder Multifunktionsgeräten können beispielsweise gestohlen werden. 
	  

 
* Sicheres Löschen des Speichers 

 
	+ Kann nach jedem Kopiervorgang der Speicher durch die Benutzer gelöscht werden?  
	 In vielen Geräten sind Speicher, meist in der Form von Festplatten, eingebaut. Wenn Daten dort unverschlüsselt gespeichert werden, können diese eventuell von Unbefugten ausgelesen werden. Außerdem besteht die Gefahr, dass Angreifer die im Gerät gespeicherten Seiten erneut ausdrucken lassen. Einige Geräte bieten daher Funktionen zum Löschen des Speichers. Wenn möglich, sollten sie so eingestellt werden können, dass automatisch nach jedem Kopiervorgang gelöscht wird.
	+ Ist es möglich, die gesamte Festplatte zu löschen?  
	 Für eine spätere Entsorgung sollte die gesamte Festplatte durch Überschreiben gelöscht werden können. Dies sollte nur nach Eingabe eines entsprechenden Löschbefehls durch einen Berechtigten möglich sein. Alternativ sollte der Speicher ausgebaut und separat gelöscht werden können.
	+ Werden Informationen zum Löschen auf dem Display angezeigt?  
	 Auf dem Display des Geräts sollte es möglichst angezeigt werden, wenn die zuletzt gespeicherten Daten oder die gesamte Festplatte durch Überschreiben gelöscht wird.
	  

 
* Netztechnische Sicherheit 

 
	+ Besitzt das Gerät netztechnische Schutzmechanismen, wie IP- und Portfilter? 
	+ Muss das Gerät WLAN- oder Bluetooth-fähig sein oder ist ein kabelgebundener Anschluss ausreichend?  
	 Der Einsatz von Funktechniken ist mit höheren Sicherheitsrisiken verbunden als der Anschluss über Kabel. Bei funkbasierten Lösungen müssen deshalb meist zusätzliche Sicherheitsmaßnahmen ergriffen werden.
	+ Unterstützt das Gerät die Verschlüsselung der Druckerkommunikation?  
	 Werden die auszudruckenden Informationen über ein Netz übertragen, sollte verhindert werden, dass sie mitgelesen oder verändert werden können. Darum sollten Netzprotokolle eingesetzt werden, die eine Verschlüsselung der Informationen unterstützen. Ein Beispiel hierfür ist das Internet Printing Protokoll (IPP) in Verbindung mit SSL (Secure Sockets Layer) bzw. TLS (Transport Layer Security).
	+ Kann das Gerät in eine vorhandene IEEE 802.1X-Umgebung integriert werden?  
	 IEEE 802.1X ermöglicht die Authentisierung der Endgeräte am Netz. Dies schützt davor, dass IT-Systeme unerlaubt am LAN betrieben werden.
	  

 
* Wartbarkeit 

 
	+ Bietet der Hersteller regelmäßige Updates und schnell verfügbare Sicherheitspatches an?  
	 Es ist besonders wichtig, dass der Hersteller zeitnah auf bekannt gewordene Sicherheitsmängel reagiert.
	+ Können für das Produkt Wartungsverträge abgeschlossen werden?  
	 Oft ist der Zugriff auf Updates und Unterstützungsleistungen des Herstellers nur in Verbindung mit einem gültigen Wartungsvertrag möglich. Können im Rahmen der Wartungsverträge maximale Reaktionszeiten für die Problembehebung festgelegt werden?  
	 Ein Wartungsvertrag ist nur dann geeignet, wenn mit den garantierten Reaktions- und Wiederinbetriebnahmezeiten die festgelegten Anforderungen an die Verfügbarkeit der Geräte abgedeckt werden können. 
	+ Bietet der Händler oder Hersteller einen technischen Kundendienst (Hotline) an, der in der Lage ist, sofort bei Problemen zu helfen?  
	 Dieser Aspekt sollte Bestandteil eines Wartungsvertrags sein. Beim Abschluss des Vertrags ist darauf zu achten, dass die Hotline- bzw. Support-Mitarbeiter auch die Sprache der Personen sprechen, die in der Regel dort anrufen werden.
	  

 
* Kosten 

 
	+ Wie hoch sind die Anschaffungskosten der Geräte? 
	+ Wie hoch sind die voraussichtlichen laufenden Kosten, einschließlich Wartung, Betrieb und Support?Diese Kosten sollten bereits in der Beschaffungsphase mit berücksichtigt werden. Der Inhalt der Wartungs- und Supportverträge sollte geprüft werden, beispielsweise im Hinblick auf Reaktionszeiten, Hotline und Qualifikation des Personals.
	  

 
**3.1.2 Verwaltung von Druckern**

Institutionen benötigen oft sehr viele Drucker für ihre unterschiedlichen Einsatzzwecke. Hierfür müssen geeignete Geräte ausgewählt werden. Außerdem ist festzulegen, wo die Hardware-Komponenten aufgestellt werden.

Im Folgenden werden typische Drucksysteme, deren Bestandteile und Kommunikationsbeziehungen vorgestellt. Drucksysteme bestehen in der Regel aus Client- und Server-seitigen Software-Komponenten.

**Drucksysteme**

In den seltensten Fällen sendet eine Anwendung den Druckauftrag direkt an einen Drucker, sondern zwischen der Anwendung und dem Drucker wird ein Drucksystem betrieben. Hierbei ist es oft erforderlich, dass diese Drucksysteme netzfähig sind und mehrere Clients auf einen Drucker zugreifen können. Auch bei einer ausschließlich lokalen Installation wird ein Drucksystem benötigt. Hierbei sendet der Client intern den Druckauftrag an den Druckserver.

Ein Drucksystem kann unter anderem folgende Aufgaben erfüllen:

* Annahme des Druckauftrags von der Anwendung,
* Verwaltung der Druckaufträge in einer Warteliste (Spooling),
* Ergänzung um zusätzliche Informationen, wie Trennseiten, Papierformat oder andere Eigenschaften,
* Umwandlung in ein dem Drucker verständliches Datenformat, wie PostScript oder PCL,
* Verwaltung von logischen und physischen Druckern,
* Benutzerverwaltung und
* Protokollierung.
Unterschiedliche Betriebssysteme favorisieren unterschiedliche Drucksysteme. Besonders bei heterogenen IT-Landschaften ist es entscheidend, dass die Drucksysteme miteinander kompatibel sind. Viele Systeme bieten Schnittstellen zu anderen Drucksystemen. Dadurch kann beispielsweise ein Unix-System auf einen Drucker zugreifen, der von einem Windows-System verwaltet wird. 

Abhängig vom Betriebssystem sind folgende Drucksysteme am weitesten verbreitet:

* Berkeley Printing System,
* Common Unix Printing System (CUPS) und
* Druckerfreigaben auf der Basis von SMB unter Windows.
Bei heterogenen Netzlandschaften ist möglichst ein Drucksystem auszuwählen, das von allen Betriebssystemen unterstützt wird. Als Alternative kann es zweckmäßig sein, mehrere verschiedene Drucksysteme einzusetzen, die unter Umständen untereinander kommunizieren können. Die Entscheidung über die zu nutzenden Drucksysteme ist zu begründen und zu dokumentieren.

**Bestandteile**

Der Druckauftrag, der von einer Anwendung erstellt wurde und an einen Drucker ausgegeben werden soll, muss mehrere Zwischenschritte durchlaufen. Für diese Schritte sind jeweils einzelne Komponenten zuständig, die im folgenden vorgestellt werden.

* **Druckclient**  
 Bei einem Druckclient handelt es sich um eine Softwarekomponente, die auf dem Arbeitsplatz-PC installiert ist. In der Regel empfängt der Druckclient eine entsprechende Anweisung von einer Anwendung und sendet den Druckauftrag an den Druckserver weiter.   
 Mit der Auswahl eines Druckernamens kann in vielen Fällen der Zieldrucker ausgewählt werden. Eine Ausnahme ist der Ausdruck in Druckerpools, bei denen für jeden Druckauftrag ein anderer Drucker vom Druckserver bestimmt werden kann.  
 Häufig können weitere Funktionen, wie Duplexdruck und Heften, durch den Druckclient festgelegt werden. Hierfür sendet der Druckclient die Druckdaten an den Druckserver. Wie der Drucker angesteuert werden kann und welche Formate er beherrscht, wird in der Regel bei der Installation des Druckers dem Drucksystem bekannt gemacht.
* **Druckserver**  
 Der Druckserver empfängt die Druckaufträge der Clients und verwaltet sie. Die Aufträge werden in eine Warteliste eingefügt und anschließend an den Drucker übertragen. Je nach Konfiguration wird bei mehreren Druckaufträgen das zuerst empfangene Dokument als erstes an den Drucker weitergeleitet oder durch eine entsprechende Priorität bevorzugt behandelt. In einigen Fällen lassen sich auch spezielle Zeiträume festlegen, in denen Druckaufträge ausgeführt werden.
* Das Dokument wird meistens direkt auf dem Druckserver aufbereitet. Dafür benötigt das Drucksystem die gerätespezifischen Druckerinformationen und Filter. Beispielsweise können diese Druckerinformationen als PPD (PostScript Printer Description) definiert sein. Verallgemeinert handelt es sich dabei um eine Spezifikation, welche Formate und Funktionen vom Drucker beherrscht werden. Beispiele für die spezifizierten Parameter sind Papierformate, Rasterauflösungen, Schriftarten, Duplex, Heften, Lochen und Farbdruck. Anhand dieser Spezifikation kann die Druckanweisung, die an den Drucker übermittelt wird, generiert werden.
* Der Druckserver bereitet den Druckauftrag auf. Dazu konvertiert er ihn in ein Datenformat, das vom jeweiligen Drucker unterstützt wird. Ist das Eingangsformat beispielsweise PostScript, muss das Dokument in ein für diesen Drucker verständliches Ausgangsformat konvertiert werden, wenn der Drucker nicht PostScript-fähig ist. Beispiele für Ausgangsformate sind PDF, PCL und PostScript.
* **Drucker**  
 Der Drucker empfängt das vorbereitete Dokument vom Druckserver und gibt es aus. Es kann zwischen logischen und physischen Druckern unterschieden werden. Folgende Anschlussarten werden in der Praxis für physische Drucker eingesetzt:  
   
 

 
	+ Lokale Drucker: Diese Drucker verfügen in der Regel über eine USB-Schnittstelle und werden direkt an ein Client-System angeschlossen.
	+ Netzdrucker: Der Drucker wird über ein Netz angesprochen.
	+ Druckserver mit lokalen Druckern: Der Drucker wird lokal an einen Druckserver, der über einen Netzanschluss verfügt, angeschlossen. Dabei kann der Druckserver in Form einer Appliance oder als klassischer Server realisiert sein. Bei diesem Ansatz muss der Druckserver häufig zwischen Netz und lokalem Anschluss konvertieren, beispielsweise als USB-Ethernet-Bridge. 
	  

 
* Logische Drucker können innerhalb des Drucksystems unterschiedliche Aufgaben haben. Die folgenden Szenarien sind in der Praxis häufig anzutreffen:  
 

 
	+  
	
	 
		- Mehrere physische Drucker werden über einen logischen Drucker angesprochen. Neben dem Vorteil einer höheren Druckleistung (es kann parallel gedruckt werden), kann ohne größeren Konfigurationsaufwand auf einen anderen Drucker zugegriffen werden, wenn einer ausfällt. Es wird empfohlen, nur Geräte mit ähnlichen Eigenschaften in einer Klasse zusammenzufassen. 
		- Ein physischer Drucker wird von mehreren logischen Druckern, die jeweils auf unterschiedlichen Druckservern installiert sind, angesprochen. Das bietet sich an, wenn mehrere Druckserver eingesetzt werden. Fällt ein Druckserver aus, kann einfach auf einen anderen Druckserver gewechselt werden, sodass der Druckbetrieb ohne größeren Konfigurationsaufwand fortgesetzt werden kann.
		- Des Weiteren können logische Drucker verwendet werden, um einem physischen Drucker mit mehreren verschiedenen Einstellungen jeweils einen eigenen Druckernamen zuzuordnen. Beispielsweise können für einen physischen Drucker zwei logische Drucker definiert werden: einer für Simplex- und einer für Duplex-Druck. Alle logischen Drucker sind zu dokumentieren. 
		  
	
	 
	  

 
**Kommunikationsbeziehungen**

Zwischen den einzelnen Komponenten eines Drucksystems entstehen unterschiedliche Kommunikationsverbindungen.

* **Kommunikation zwischen Druckclient und Druckserver**  
 Die Kommunikationsverbindung kann zwischen einem Druckclient und dem Druckserver sowie zwischen verschiedenen Druckservern aufgebaut werden. Je nach Szenario werden die Druckinformationen über ein Netz oder lokal ausgetauscht.   
 Je nach Drucksystem können folgende Protokolle eingesetzt werden: 

 
	+ HTTP (Hypertext Transfer Protocol),
	+ IPP (Internet Printing Protocol),
	+ LPR/LPD (Line Printer Remote / Line Printer Daemon),
	+ SMB (Server Message Block) und
	+ Appletalk beziehungsweise Bonjour.
	  Abhängig von den eingesetzten Druckern und vom gewählten Drucksystem sind geeignete Protokolle auszuwählen. Innerhalb eines Netzes sollten möglichst wenig unterschiedliche Druck-Protokolle eingesetzt werden. Die Entscheidung ist zu dokumentieren.   
 Auch für die Verwaltung müssen bei einigen Drucksystemen Informationen ausgetauscht werden. Die Clients müssen beispielsweise regelmäßig über die verfügbaren Drucker und deren Status informiert werden. Dabei können, je nach Drucksystem, folgende Strategien verfolgt werden: 

 
	+ Broadcasting: In regelmäßigen Abständen sendet der Server unaufgefordert eine Nachricht an alle Clients in der Broadcast-Domäne. 
	+ Polling: Der Druckclient fragt die Informationen vom Server ab.
	  Broadcasting vereinfacht die Administration, ist aber mit weiteren Problemen verbunden. Befinden sich die Clients und Server in verschiedenen Broadcast-Domänen, erreichen die Pakete nicht alle Clients. In der Praxis können auch Probleme auftreten, wenn der Druckserver mehrere Netzschnittstellen hat und die Broadcast-Pakete an die falschen Schnittstellen sendet. Für die Konfiguration ist ein Verfahren auszuwählen und zu dokumentieren. 

 
* **Kommunikation zwischen Druckserver und Drucker**  
 Für die Kommunikation mit den Druckern werden ebenfalls entsprechende Protokolle benötigt. Diese hängen von den Druckerspezifikationen und von der Anschlussart ab. Beispielsweise gibt es Protokolle für 

 
	+ die Kommunikation über die parallele Schnittstelle,
	+ den Anschluss über USB,
	+ den Betrieb über die serielle Schnittstelle und
	+ die netzbasierte Kommunikation mit den Druckern, beispielsweise über das HP JetDirect Protokoll oder über IPP (Internet Printing Protocol).
	  Einige Druckersysteme ermöglichen auch die Konfiguration der Drucker über den Druckserver. Neben proprietären Protokollen wird hier oft das Simple Network Management Protocol (SNMP) eingesetzt.  
 Es müssen Protokolle ausgewählt werden, die für die Anforderungen der Institution und für die einzusetzenden Komponenten geeignet sind. Die Entscheidungen sind zu dokumentieren.

 
**Design der Druckerlandschaft**

Neben der Auswahl des Drucksystems spielt die Anordnung der einzelnen Bestandteile, wie Clients, Server und Drucker, eine wichtige Rolle. Grob können folgende Ansätze für die Druckerarchitektur unterschieden werden:

* Lokale Drucker: Sowohl die Anwendung, die den Druckauftrag generiert, als auch der Druckserver und der Druckclient werden gemeinsam auf einem IT-System betrieben. Der Drucker ist über die USB-, parallele oder serielle Schnittstelle an das IT-System angeschlossen.
* Arbeitsplatz-PC mit Netz-Drucker: Auf einem oder mehreren IT-Systemen befinden sich neben der sendenden Anwendung auch der Druckclient und der Druckserver. Die Druckserver der einzelnen IT-Systeme senden die Druckaufträge an einen netzfähigen Drucker.
* Zentraler Druckserver: Auf den Arbeitsplatzsystemen sind nur die Druckclients installiert. Diese nehmen den Druckauftrag an und leiten ihn über ein Netz an einen zentralen Druckserver weiter.  
 Auf diesem Druckserver werden die Druckaufträge verwaltet. Der Druckserver sendet die Aufträge an lokale oder netzbasierte Drucker weiter, wo sie ausgegeben werden.
* Kombinationen: Es sind zahlreiche Kombinationen aus den oben genannten Anordnungen möglich. Ein Beispiel ist der Anschluss eines lokalen Druckers am Arbeitsplatz-PC für kleinere Druckaufträge und der parallele Betrieb eines zentralen Druckservers für umfangreiche Ausdrucke.
Die getroffenen Entscheidungen zum Aufbau der Druckerlandschaft sind zu dokumentieren.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Drucker, Kopierer und Multifunktionsgeräte" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ACSD] Datenschutz und Sicherheit in Druckinfrastrukturen

  

 mc² management consulting GmbH, 12.2016 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161219\_mc2\_drucker\_sicherheit.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/partner/161219_mc2_drucker_sicherheit.pdf)

 
* #### [CERT] Informationen zu Schwachstellen und Sicherheitslücken von Druckern und zugehörigen Diensten, Warn- und Informationsdienst

  

 CERT-Bund, (zuletzt abgerufen am 28.09.2017)   
 <https://www.cert-bund.de/search>

 
* #### [CSE015] Netzwerk-verbundene Bürogeräte

  

 CSE 015, V1.0, Allianz für Cyber-Sicherheit, 10.2012 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_015.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_015.html)

 
* #### [CSE069] Sichere Passwörter in Embedded Devices

  

 CSE 069, V1.0, Allianz für Cyber-Sicherheit vom 12.2013 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_069.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_069.html)

 
* #### [CUPS] Common Unix Printing System

  

 (zuletzt abgerufen 05.10.2017)  
 <https://www.cups.org/>

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [PP0058] IEEE Standard Protection Profile for Hardcopy Devices in IEEE Std 2600-2008

  

 Operational Environment B, IEEE Std 2600.2-2009, IEEE Computer Society, Information Assurance (C/IA) Committee, BSI-CC-PP-0058-2010, 07.2010   
 [https://www.bsi.bund.de/SharedDocs/Zertifikate\_CC/PP/aktuell/PP\_0058.html](https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/aktuell/PP_0058.html)

 
