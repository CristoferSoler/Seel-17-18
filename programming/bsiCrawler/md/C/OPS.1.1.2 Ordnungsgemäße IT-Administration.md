1 Beschreibung
--------------

### 1.1 Einleitung

Die fortlaufende Administration von IT-Systemen und -Komponenten ist für den IT-Betrieb grundlegend. Die Systemadministratoren richten dabei IT-Systeme und Anwendungen ein, beobachten den Betrieb und reagieren mit Maßnahmen, die die Funktion und die Leistungsfähigkeit der Systeme erhalten, oder sie passen die Systeme an die veränderten Bedürfnisse an. Dabei erfüllen sie auch eine Reihe von Aufgaben für die Sicherheit: Sie sorgen nicht nur dafür, dass die Systeme verfügbar bleiben, sondern setzen auch Sicherheitsmaßnahmen um und überprüfen, ob sie wirksam sind. Dazu verfügen sie über sehr weitreichende Berechtigungen, sodass es für die Sicherheit des Informationsverbunds auch sehr wichtig ist, die Systemadministration vor unbefugten Zugriffen selbst abzusichern. 

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, aufzuzeigen, wie mit einer ordnungsgemäßen IT-Administration die Sicherheitsanforderungen von IT-Anwendungen, -Systemen und Netzen erfüllt werden.

Mit der Umsetzung dieses Bausteins sorgt die Institution einerseits dafür, dass die für die Sicherheit des Informationsverbunds erforderlichen Tätigkeiten in der Systemadministration ordnungsgemäß und systematisch durchgeführt werden. Andererseits reagiert die Institution damit auch auf die besonderen Gefährdungen, die sich aus dem Umgang mit Administrationsprivilegien und aus dem Zugang zu schützenswerten Bereichen der Institution zwangsläufig ergeben.

### 1.3 Abgrenzung

Der Baustein beschreibt allgemeine Sicherheitsanforderungen an eine ordnungsgemäße IT-Administration. Er betrachtet dabei laufende administrative Tätigkeiten, die vom dafür vorgesehenen Personal an den Standorten der Institution durchgeführt werden. Er ist abzugrenzen gegen eine Fernadministration von IT-Systemen über externe Schnittstellen, sowie von der Fernwartung von Geräten und Komponenten durch die jeweiligen Hersteller oder Zulieferer, die im Baustein *OPS.2.4 Fernwartung* betrachtet wird.

Gegenstand des Bausteins sind übergreifende Anforderungen an den Administrationsprozess als solchen. Spezifische Anforderungen an das Management einzelner IT-Systeme und -Komponenten werden im Baustein *OPS.1.1.2 Netz- und Systemmanagement *behandelt. Dort finden sich entsprechend Anforderungen, wie Systeme installiert und in Betrieb genommen werden, wie Änderungen und Wartungsarbeiten durchgeführt oder Systeme ausgesondert werden.

Die weiteren Bausteine des Bereichs *OPS.1.1 Kern-IT-Betrieb* beschreiben Aspekte des IT-Betriebs, die zusätzlich zum vorliegenden Baustein relevant sind. Sie sollen daher in Ergänzung zu diesem Baustein zusätzlich betrachtet und modelliert werden.

Eine besondere Sicherheitsrelevanz hat in einer Institution die ordnungsgemäße Administration von Benutzern und Rechten. Deshalb wird dieses Thema ebenfalls in einem eigenen Baustein* *behandelt (siehe *ORP.4 Identitäts- und Berechtigungsmanagement)*.

Die im vorliegenden Baustein beschriebenen Anforderungen sind auch dann anzuwenden, wenn administrative Aufgaben durch Dritte durchgeführt werden. Besondere Anforderungen für solche Fälle werden zusätzlich in den Bausteinen *OPS.2.1 Outsourcing für Kunden und OPS.3.1 Outsourcing für Dienstleister *beschrieben.

Weiterhin bezieht sich der Baustein Ordnungsgemäße IT-Administration auf den Regelbetrieb. In Ausnahmesituationen, insbesondere bei einem möglichen IT-Angriff und der Kompromittierung von Systemen, sind abweichende Anforderungen zu beachten, die in den entsprechenden Bausteinen aus dem Bereich *DER.2 Security Incident Management *beschrieben werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich ordnungsgemäße IT-Administration von besonderer Bedeutung:

### 2 1 Versäumnisse durch ungeregelte Zuständigkeiten

Sofern die IT-Organisation die administrativen Zuständigkeiten, z. B. in den Bereichen Planung, Installation, Dokumentation, Patch-Management und Überwachung nicht klar geregelt hat oder die Regelungen den beteiligten Mitarbeitern nicht bekannt und verständlich sind, kann das zur Folge haben, dass sicherheitsrelevante Aufgaben aus diesen Bereichen nicht oder nicht systematisch durchgeführt werden. Typische Beispiele sind eine unklare Abgrenzung der Zuständigkeiten zwischen IT und Telekommunikationstechnik, zwischen Büro-IT und Fertigungsanlagen oder zwischen Anwendungs- und Plattformbetrieb.

### 2 2 Personalausfall von Kernkompetenzträgern

Auch Administratoren können ungeplant oder längerfristig ausfallen. Ohne eingearbeitete Vertreter ist nicht sichergestellt, dass die von ihnen betreuten Systeme und Anwendungen ordnungsgemäß und sicher weiterbetrieben werden können. Administratoren bauen zum Teil sehr umfangreiches Detailwissen zu den von ihnen betreuten Systemen und Anwendungen auf, das einerseits die eingesetzten Produkte und Lösungen, andererseits aber gerade auch Besonderheiten der Einsatzumgebung und der spezifischen Konfiguration umfasst. Mit diesem Wissen können sie Fehlersituationen schnell erkennen und Anforderungen einfacher umsetzen, was häufig dazu führt, dass gerade bei komplexen Systemen die Administration durch einzelne Personen erfolgt. Fällt diese Person aus, ist auch das Wissen für die Institution nicht mehr verfügbar.

### 2 3 Missbrauch von administrativen Berechtigungen

Administrative Berechtigungen erlauben es, umfassend auf Dokumente, Kommunikationsinhalte und Datenbanken zuzugreifen. Administratoren können diese weitreichenden Berechtigungen nicht nur dazu benutzen, die ihnen übertragenen Aufgaben zu erfüllen, sondern auch für eigene Zwecke oder im Sinne von Dritten. So könnten sie z. B. Personalunterlagen einsehen oder Kommunikationsvorgänge von Kollegen mitlesen. Weiterhin könnten auch Dritte durch Druck oder andere Anreize auf Administratoren einwirken, um mit ihrer Hilfe missbräuchlich auf Daten oder Systeme zuzugreifen. 

### 2 4 Erleichterung von Angriffen

Die privilegierten Systemzugänge der Administratoren stehen häufig im Fokus von Angreifern. Werden administrative Aufgaben nicht ordnungsgemäß wahrgenommen, so können dadurch Angriffe auf den Informationsverbund erheblich erleichtert werden. So können durch Fahrlässigkeit Fehler in der Konfiguration entstehen, vorgesehene Schutzmaßnahmen nicht oder nur unzulänglich umgesetzt oder auftretende Verdachtsmomente nicht verfolgt werden. Ursachen dafür sind z. B. ein fehlendes Sicherheitsbewusstsein, hoher Zeitdruck oder fehlende Prozesse und Verfahrensweisen. Daraus können sich Schwachstellen ergeben, die von Angreifern ausgenutzt werden könnten. 

### 2 5 Störung des Betriebs

Administrative Tätigkeiten beeinflussen unmittelbar den Betrieb von IT-Systemen und Anwendungen. So können zum Beispiel laufende Benutzersitzungen abgebrochen werden, wenn IT-Systeme neu gestartet werden, oder berechtigte Zugriffe verhindert werden, wenn ein Firewall-Regelwerk angepasst wird. Werden solche Vorgänge ausgeführt, ohne zu berücksichtigen, wie sie sich auf die Benutzer auswirken und ohne sie mit den betroffenen Bereichen abzustimmen, kann der Betrieb erheblich gestört werden.

### 2 6 Fehlende Aufklärungsmöglichkeiten für Vorfälle

Mängel in der Dokumentation des IT-Betriebs oder fehlende Aufzeichnungen können dazu führen, dass IT-Sicherheitsvorfälle nicht aufgeklärt oder nachverfolgt werden können. Da bei Sicherheitsvorfällen häufig nicht einfach erkennbar ist, wie z. B. der Angriff abgelaufen ist, welches Ausmaß er hatte oder wie manipuliert wurde, muss das erst durch geeignete Untersuchungen ermittelt werden. Das setzt jedoch voraus, dass beispielsweise der Sollzustand von Systemen vor dem Sicherheitsvorfall dokumentiert und prüfbar ist, oder dass ordnungsgemäße von unbefugten Änderungen an Systemen anhand geeigneter Aufzeichnungen unterschieden werden können. Fehlen entsprechende Informationen, so können Vorfälle nur schwer oder überhaupt nicht mehr aufgeklärt werden. Auch eine gerichtsfeste Beweisführung gegenüber den Tätern ist in solchen Fällen nicht mehr möglich.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Ordnungsgemäße IT-Administration aufgeführt. Grundsätzlich ist der Leiter IT für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.1.2.A1 Personalauswahl für administrative Tätigkeiten [Leiter Personal]

Wenn Mitarbeiter administrative Aufgaben innerhalb der IT-Umgebung übernehmen sollen, MÜSSEN sie unter Berücksichtigung der Sicherheitsanforderungen der von ihnen betreuten Systeme und Anwendungen folgende Kriterien erfüllen:

* Die Mitarbeiter MÜSSEN über die notwendige fachliche Qualifikation verfügen, um die ihnen übertragenen Aufgaben ordnungsgemäß bewältigen zu können. Es MÜSSEN weiterhin ausreichende Kenntnisse zu den jeweils betreuten IT-Systemen, Anwendungen und Plattformen vorhanden sein. Die Mitarbeiter MÜSSEN die in der Institution für die Dokumentation verwendete Sprache beherrschen und über ausreichende Englischkenntnisse zum Verständnis typischer IT-Dokumentationen verfügen.
* Die Mitarbeiter MÜSSEN die ihnen übertragenen Aufgaben zuverlässig und sorgfältig erledigen können. 
* Es MUSS eine Rollentrennung von administrativen und kontrollierenden Rollen (z.B. Revision) vorgenommen werden.
Die Administratoren und deren Vertreter MÜSSEN ausreichend Zeit zur sorgfältigen Erfüllung ihrer Aufgaben haben. Alle Administratoren und deren Vertreter MÜSSEN ausreichend Möglichkeiten zur Fortbildung erhalten

Diese Anforderungen MÜSSEN auch dann erfüllt werden, wenn administrative Aufgaben an Dritte übertragen werden.

#### OPS.1.1.2.A2 Vertretungsregelungen und Notfallvorsorge

Für alle administrativen Aufgaben und Verantwortlichkeiten MÜSSEN Vertretungsregelungen getroffen werden.

Es MUSS sichergestellt sein, dass benannte Vertreter auf die zu betreuenden IT-Systeme zugreifen können. Um auch in Notfallsituationen administrativ auf Systeme und Anwendungen zugreifen zu können, SOLLTEN entsprechende Notfalluser mit Administrationsrechten eingerichtet werden.

#### OPS.1.1.2.A3 Geregelte Einstellung von IT-Administratoren [Leiter Personal]

Wenn Mitarbeiter administrative Aufgaben innerhalb der IT-Umgebung übernehmen, MÜSSEN sie in ihre Tätigkeit, insbesondere in die vorhandene IT-Architektur und die von ihnen zu betreuenden IT-Systeme und Anwendungen eingewiesen werden. Die in der Institution gültigen und für ihre Tätigkeit relevanten Sicherheitsbestimmungen MÜSSEN den IT-Administratoren bekannt gemacht werden. Auch MÜSSEN sie dazu verpflichtet werden, die relevanten Datenschutzgesetze und andere gesetzliche und betriebliche Regelungen einzuhalten.

Diese Anforderungen MÜSSEN auch dann erfüllt werden, wenn administrative Aufgaben an Dritte übertragen werden.

#### OPS.1.1.2.A4 Beendigung der Tätigkeit als IT-Administrator [Leiter Personal]

Wenn IT-Administratoren von ihren Aufgaben wieder entbunden werden, MÜSSEN alle ihnen zugewiesenen persönlichen Administrationskennungen gesperrt werden. Es MUSS geprüft werden, welche Passwörter die ausscheidenden Mitarbeiter darüber hinaus noch kennen, z. B. Superuser-Zugänge, Notfalluser, WLAN-Passwörter. Solche Passwörter MÜSSEN geändert werden. Den Mitarbeitern ausgehändigte Geräte, Speichermedien und Zugangsmittel (z. B. Token, Chipkarten) MÜSSEN vollständig zurückgegeben werden. 

Weiterhin MUSS geprüft werden, ob die ausscheidenden Mitarbeiter gegenüber Dritten als Ansprechpartner benannt wurden. z. B. in Verträgen oder als Admin-C-Eintrag bei Internet-Domains. In diesem Fall MÜSSEN die betroffenen Parteien informiert und neue Ansprechpartner festgelegt werden. Die Benutzer der betroffenen IT-Systeme und Anwendungen MÜSSEN darüber informiert werden, dass der bisherige IT-Administrator ausgeschieden ist.

Diese Anforderungen MÜSSEN auch dann erfüllt werden, wenn administrative Aufgaben an Dritte übertragen wurden und die dort beschäftigten Mitarbeiter aus ihrer Tätigkeit ausscheiden.

#### OPS.1.1.2.A5 Administrationskennungen

Jeder Administrator und jeder Vertreter eines Administrators MUSS eine eigene, eindeutige Administratorkennung haben. Die vergebenen Administrationsrechte MÜSSEN sich aus den Erfordernissen der jeweils übernommenen IT-Administrationsaufgaben ableiten.

Administratoren DÜRFEN unter diesen Kennungen nur administrative Arbeiten durchführen. Sie DÜRFEN NICHT für Routinetätigkeiten benutzt werden, für die keine erweiterten Berechtigungen erforderlich sind, z. B. E-Mail-Kommunikation, Informationsrecherche im Internet. Für solche Aufgaben MÜSSEN den IT-Administratoren zusätzlich persönliche, nicht-privilegierte Konten eingerichtet werden.

#### OPS.1.1.2.A6 Schutz administrativer Kennungen

Administrationskennungen MÜSSEN durch geeignete Authentisierungsmechanismen angemessen geschützt sein. Werden dafür Passwörter benutzt, DÜRFEN gleichartige Passwörter NICHT für IT-Systeme in anderen Schutzzonen verwendet werden.

Für Administrationszugriffe MÜSSEN sichere Protokolle verwendet werden, wenn dies nicht über eine lokale Konsole erfolgt. Diese MÜSSEN sicherstellen, dass die Kommunikation nach dem Stand der Technik verschlüsselt ist.

Jeder Anmeldevorgang über eine Administrationskennung (Login) MUSS protokolliert werden, sodass nachvollziehbar ist, wann, auf welchem Weg und unter welcher Nutzerkennung auf das System zugegriffen wurde.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Ordnungsgemäße IT-Administration. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.1.2.A7 Regelung der IT-Administrationstätigkeit [Leiter Personal]

Die Befugnisse, Aufgaben und Pflichten der IT-Administratoren SOLLTEN in einer Arbeitsanweisung oder Richtlinie verbindlich festgeschrieben werden. Die Aufgabenverteilung zwischen den einzelnen Administratoren SOLLTE so vorgenommen werden, dass einerseits Überschneidungen in den Zuständigkeiten vermieden werden und andererseits keine Administrationslücken entstehen. Die Regelungen SOLLTEN regelmäßig aktualisiert werden. Die Vorgaben SOLLTEN insbesondere eigenmächtige Änderungen der IT-Administratoren im Informationsverbund ausschließen, soweit diese über die ihnen explizit übertragenen Aufgaben hinausgehen und nicht notwendig sind, um einen Sicherheitsvorfall oder Störfall abzuwenden.

#### OPS.1.1.2.A8 Administration von Fachanwendungen [IT-Betrieb]

Die in diesem Baustein aufgeführten Basisanforderungen SOLLTEN auch für Mitarbeiter mit administrativen Aufgaben für einzelne Fachanwendungen durchgängig umgesetzt werden. Die Aufgabenteilung zwischen Anwendungs- und Systemadministration SOLLTE klar definiert und schriftlich festgehalten werden. Zwischen den Verantwortlichen für die System- und Fachanwendungsadministration SOLLTEN Schnittstellen definiert sein (z. B. Ansprechpartner, Kommunikationswege, regelmäßiger Austausch).

Wenn administrativ in den Anwendungsbetrieb eingegriffen wird (z. B. Versionswechsel, Wartungsfenster), SOLLTE das im Vorfeld mit dem Fachbereich abgestimmt sein und die Bedürfnisse des Fachbereichs berücksichtigen.

#### OPS.1.1.2.A9 Ausreichende Ressourcen für den IT-Betrieb

Es SOLLTEN ausreichende Personal- und Sachressourcen bereitgestellt werden, um die anfallenden administrativen Aufgaben ordnungsgemäß zu bewältigen. Dabei SOLLTE berücksichtigt werden, dass auch für unvorhersehbare Tätigkeiten entsprechende Kapazitäten vorhanden sein müssen, insbesondere um sicherheitsrelevante Ereignisse zu behandeln und aufzuklären.

Die Ressourcenplanung SOLLTE in regelmäßigen Zyklen, z. B. jährlich, geprüft und den aktuellen Erfordernissen angepasst werden.

#### OPS.1.1.2.A10 Fortbildung und Information [Leiter Personal]

Für die eingesetzten IT-Administratoren SOLLTEN geeignete Fort- und Weiterbildungsmaßnahmen ergriffen werden, damit sie immer auf dem aktuellen Stand der Technik sind. Dabei SOLLTEN auch technische Entwicklungen berücksichtigt werden, die noch nicht eingesetzt, aber für die Institution in absehbarer Zeit wichtig werden könnten. Die Fortbildungsmaßnahmen SOLLTEN durch einen Schulungsplan untersetzt werden und das gesamte Team berücksichtigen, sodass alle erforderlichen Qualifikationen im Team mehrfach vorhanden sind.

Administratoren SOLLTEN sich regelmäßig über die Sicherheit der von ihnen betreuten Systeme, Dienste und Protokolle informieren, vor allem über aktuelle Gefährdungen und Sicherheitsmaßnahmen.

#### OPS.1.1.2.A11 Dokumentation von IT-Administrationstätigkeiten [IT-Betrieb]

Systemänderungen SOLLTEN in geeigneter Form nachvollziehbar dokumentiert werden. Aus der Dokumentation SOLLTE hervorgehen,

* welche Änderungen erfolgt sind,
* wann die Änderungen erfolgt sind,
* wer die Änderungen durchgeführt hat,
* auf welcher Grundlage bzw. aus welchem Anlass die Änderungen erfolgt sind.
#### OPS.1.1.2.A12 Regelungen für Wartungs- und Reparaturarbeiten [IT-Betrieb]

IT-Systeme SOLLTEN regelmäßig gewartet werden. Es SOLLTE geregelt sein, welche Sicherheitsaspekte bei Wartungs- und Reparaturarbeiten zu beachten sind und wer für die Wartung oder Reparatur von Geräten verantwortlich ist. Mitarbeiter SOLLTEN wissen, dass Wartungspersonal bei Arbeiten im Haus beaufsichtigt werden muss. Durchgeführte Wartungsarbeiten SOLLTEN dokumentiert werden.

#### OPS.1.1.2.A13 Absicherung von Fernwartung [IT-Betrieb, Informationssicherheitsbeauftragter (ISB)]

Fernwartung SOLLTE nur durchgeführt werden, wenn angemessene Sicherheitsmaßnahmen ergriffen wurden. Es SOLLTE sichergestellt werden, dass Fernwartungszugriffe immer nur vom lokalen IT-System initiiert werden können. Die Durchführung der Fernwartung SOLLTE ausreichend protokolliert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.1.2.A14 Sicherheitsüberprüfung von Administratoren(CIA)

Im Hochsicherheitsbereich SOLLTE eine zusätzliche Sicherheitsüberprüfung durchgeführt werden um die Vertrauenswürdigkeit von Mitarbeitern zu bestätigen.

#### OPS.1.1.2.A15 Aufteilung von Administrationstätigkeiten(CI)

Es SOLLTEN unterschiedliche Administrationsrollen für Teilaufgaben eingerichtet werden. Bei der Abgrenzung der Aufgaben SOLLTEN die Art der Daten und die vorhandene Systemarchitektur berücksichtigt werden.

#### OPS.1.1.2.A16 Zugangsbeschränkungen für administrative Zugänge(CIA)

Bei erhöhtem Schutzbedarf SOLLTE der Zugang zu administrativen Oberflächen oder Schnittstellen mit Filter- und Separierungsmaßnahmen technisch beschränkt werden, d. h. sie SOLLTEN für Personen außerhalb der zuständigen IT-Administrationsteams nicht erreichbar sein. Administrative Zugriffe auf IT-Systeme in anderen Schutzzonen SOLLTEN stets mittelbar über einen Sprungserver in der jeweiligen Sicherheitszone erfolgen. Zugriffe von anderen Systemen oder aus anderen Sicherheitszonen heraus SOLLTEN abgewiesen werden.

#### OPS.1.1.2.A17 IT-Administration im Vier-Augen-Prinzip(CI)

Bei besonders sicherheitskritischen Systemen SOLLTE der Zugang zu Kennungen mit administrativen Berechtigungen so realisiert werden, dass dafür zwei Mitarbeiter erforderlich sind. Dabei SOLLTE jeweils ein IT-Administrator die anstehenden administrativen Tätigkeiten ausführen, während er von einem weiteren IT-Administrator kontrolliert wird.

#### OPS.1.1.2.A18 Durchgängige Protokollierung administrativer Tätigkeiten(CI)

Administrative Tätigkeiten SOLLTEN möglichst protokolliert werden. Bei besonders sicherheitskritischen Systemen SOLLTEN alle administrativen Zugriffe durchgängig und vollständig protokolliert werden. Die ausführenden IT-Administratoren SOLLTEN dabei selbst keine Berechtigung haben, die aufgezeichneten Protokolldateien zu verändern oder zu löschen. Die Protokolldateien SOLLTEN für eine Zeitdauer aufbewahrt werden, die dem Schutzbedarf angemessen ist und die es ermöglicht, nachträgliche Eingriffe in das System aufzuklären. 

#### OPS.1.1.2.A19 Berücksichtigung von Hochverfügbarkeitsanforderungen [Informationssicherheitsbeauftragter (ISB)](A)

Die IT-Administratoren SOLLTEN analysieren, für welche der von ihnen betreuten Systeme und Netze Hochverfügbarkeitsanforderungen bestehen. Für diese Bereiche SOLLTEN sie sicherstellen, dass die eingesetzten Komponenten und Architekturen sowie die zugehörigen Betriebsprozesse geeignet sind, um diese Anforderungen zu erfüllen. Dies erfordert im Regelfall eine umfassende Hochverfügbarkeitsplanung. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Ordnungsgemäße IT-Administration" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [HVK] Hochverfügbarkeitskompendium

  

 BSI, (zuletzt abgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Hochverfuegbarkeit/HVKompendium/hvkompendium_node.html)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Ordnungsgemäße IT-Administration" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.35 Nötigung, Erpressung oder Korruption
* G 0.37 Abstreiten von Handlungen
* G 0.42 Social Engineering
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

