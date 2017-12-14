1 Beschreibung
--------------

### 1.1 Einleitung

Bei Advanced Persistent Threats (APT) handelt es sich um zielgerichtete Cyber-Angriffe auf ausgewählte Institutionen und Einrichtungen, bei denen sich ein Angreifer dauerhaften Zugriff zu einem Netz verschafft und diesen in der Folge auf weitere IT-Systeme ausweitet. Die Angriffe zeichnen sich durch einen sehr hohen Ressourceneinsatz und erhebliche technische Fähigkeiten aufseiten der Angreifer aus und sind in der Regel schwierig zu detektieren.

Nachdem ein APT-Angriff entdeckt wurde, stehen die Verantwortlichen in den betroffenen Institutionen vor der Herausforderung, eine Bereinigung durchführen zu müssen, die über das übliche Vorgehen zur Behandlung von IT-Sicherheitsvorfällen hinausgeht. Denn es ist davon auszugehen, dass die entdeckten Angreifer bereits seit geraumer Zeit auf die betroffene IT-Infrastruktur zugreifen können und komplexe Angriffswerkzeuge benutzen, um die Standard-Sicherheitsmechanismen zu umgehen und diverse Hintertüren zu etablieren. Außerdem besteht die Gefahr, dass die Angreifer die infizierte Umgebung genau beobachten und auf Bereinigungsversuche reagieren, indem sie ihre Spuren verwischen und die Untersuchung sabotieren.

Allgemein geht der Baustein von einer hohen Bedrohungslage durch einen gezielten, motivierten Angreifer mit überdurchschnittlichen Ressourcen aus. Grundsätzlich sollte bei einem solchen Vorfall immer auch ein (zertifizierter) Forensikdienstleister hinzugezogen werden, wenn die Institution selbst nicht über entsprechende eigene Forensik-Experten verfügt. Forensik-Dienstleister sollten dabei bereits in der Phase der forensischen Analyse herangezogen werden, der Dienstleister sollte jedoch auch bei der Bereinigung zumindest beratend hinzugezogen werden

### 1.2 Zielsetzung

Dieser Baustein beschreibt, wie eine Institution vorgehen sollte, um nach einem APT-Angriff die IT-Systeme zu bereinigen und den regulären und sicheren Betriebszustand des Informationsverbunds wiederherzustellen. 

### 1.3 Abgrenzung

Ein Informationsverbund kann nur bereinigt werden, wenn der APT-Vorfall vorher erfolgreich detektiert und forensisch analysiert wurde. Detektion und Forensik sind jedoch nicht Thema dieses Bausteins, sondern werden in DER.1 *Detektion von sicherheitsrelevanten Ereignissen* und DER.2.2 *Vorsorge für die IT-Forensik* behandelt.

Im vorliegenden Baustein wird ausschließlich die Bereinigung von APT-Vorfällen betrachtet. Übliche Vorfälle werden im Baustein DER.2.1 *Incident Management* behandelt. Auch beschreibt der Baustein nicht, wie sogenannte Indicators of Compromise (IOCs), also Einbruchsspuren, abzuleiten sind und wie diese benutzt werden können, um wiederkehrende Angreifer zu erkennen. Ebenso wird nicht darauf eingegangen, wie sich eventuell bei der Analyse und Bereinigung übersehene Hintertüren finden lassen. Weiterhin ist der Baustein abzugrenzen vom übergeordneten Incident-Management-Prozess (siehe DER.2.1 *Incident Management*), in den die Bereinigung eingebettet ist.

Außerdem werden keine Angriffe betrachtet, mit denen sich Angreifer physischen Zugriff auf eine IT-Umgebung verschaffen. So fallen Angriffsformen wie in Rechenzentren einbrechen, Administratoren bestechen, neu beschaffte Hardware abfangen und manipulieren oder elektromagnetische Strahlung abhören nicht in diesen Baustein. Es werden ausschließlich Cyber-Angriffe berücksichtigt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Bereinigung weitreichender Sicherheitsvorfälle von besonderer Bedeutung:

### 2 1 Unvollständige Bereinigung

APT-Angreifer wollen üblicherweise einen Informationsverbund dauerhaft infiltrieren. Sie verfügen über die dafür notwendigen Ressourcen und sind in der Lage, langfristige Angriffskampagnen durchzuführen. Dafür benutzen sie Werkzeuge und Methoden, die auf ein Angriffsziel abgestimmt sind. Auch wenn ein APT-Vorfall entdeckt wird, kann nicht davon ausgegangen werden, dass sämtliche Zugangswege der Angreifer gefunden, alle Infektionen und Kommunikationswege von Schadsoftware beseitigt und alle Hintertüren entfernt wurden. Bei einer unvollständigen Bereinigung ist es jedoch sehr wahrscheinlich, dass ein Angreifer zu einem späteren Zeitpunkt, z. B. nach einer längeren Ruhephase, erneut auf die IT-Systeme zugreift und seinen Zugang wieder ausbaut. Das kann er beispielsweise, indem er Hintertüren nicht nur in Betriebssystemen und Anwendungssoftware platziert, sondern auch hardwarenahe Komponenten, wie etwa Firmware, manipuliert. Solche Modifikationen sind nur sehr schwierig zu identifizieren und das notwendige Wissen, um sie zu extrahieren und zu analysieren, ist nur wenig verbreitet. Versuchen die Verantwortlichen z. B., die IT-Komponenten zu bereinigen, indem sie die Firmware überschreiben oder aktualisieren, kann es trotzdem passieren, dass der Angreifer auch die Update-Routinen modifiziert hat und somit auf diesem Weg wieder ins System kommt.

### 2 2 Vernichtung von Spuren

Nach einem APT-Vorfall werden IT-Systeme oft neu installiert oder ganz ausgemustert. Wurde jedoch zuvor von den IT-Systemen keine forensische Kopie angefertigt, können Spuren vernichtet werden, die für eine weitere Aufklärung des Vorfalls oder sogar für ein Gerichtsverfahren notwendig wären.

### 2 3 Vorzeitige Alarmierung des Angreifers

Üblicherweise wird vor der Bereinigung eines APT-Vorfalls der Angriff über längere Zeit hinweg beobachtet und forensisch analysiert, um so alle Zugangswege und verwendeten Werkzeuge und Methoden zu identifizieren. Bemerkt der Angreifer während dieser Phase, dass er entdeckt wurde, greift er eventuell zu Gegenmaßnahmen. Beispielsweise kann er versuchen, seine Spuren zu verwischen oder er sabotiert noch schnell weitere IT-Systeme. Auch könnte er aufhören oder weitere Hintertüren einrichten, um einfach später den Angriff fortzuführen. 

Da bei einem APT-Angriff grundsätzlich davon ausgegangen werden muss, dass die gesamte IT-Infrastruktur der Institution kompromittiert wurde, ist das Risiko hoch, dass der Angreifer die Bereinigungsaktivitäten entdeckt. Das gilt insbesondere, wenn die kompromittierte IT-Infrastruktur benutzt wird, um die Bereinigung zu planen und zu koordinieren. Finden die wesentlichen Schritte zur Bereinigung nicht in der korrekten Reihenfolge statt bzw. werden kritische Maßnahmen nicht gleichzeitig und aufeinander abgestimmt durchgeführt, erhöht sich die Gefahr, dass der Angreifer alarmiert wird. Isolieren die Verantwortlichen beispielsweise das Netz schrittweise statt auf einmal, wird der Angreifer eventuell gewarnt, bevor sein Zugriff effektiv beendet ist.

### 2 4 Datenverlust und Ausfall von IT-Systemen

Bei der Bereinigung eines APT-Vorfalls werden verschiedene IT-Systeme neu installiert und auch Netze temporär isoliert. Hierdurch fallen zwangsweise IT-Systeme aus und Dienste sind damit z. B. nur noch eingeschränkt oder gar nicht mehr verfügbar. Dauert die Bereinigung sehr lange, kann es hierdurch zu erheblichen Produktivitätsausfällen kommen. Das kann wiederum signifikante wirtschaftliche Einbußen zur Folge haben, die sogar die Unternehmensexistenz bedrohen können. Dies ist auch insbesondere dann der Fall, wenn keine oder keine ausreichende Dokumentation für einen Wiederaufbau verfügbar ist.

### 2 5 Fehlender Netzumbau nach einem APT-Angriff

Bei einem APT-Angriff erlangt der Angreifer detaillierte Kenntnisse darüber, wie die Zielumgebung aufgebaut und konfiguriert ist. Zum Beispiel kennt er die existierenden Netzsegmente, Namensschemata für IT-Systeme, Benutzer- und Dienstkonten, eingesetzte Software und Services. Durch dieses Wissen kann sich derselbe Angreifer unter Umständen nach einer Bereinigung erneut Zugang auf die Zielumgebung verschaffen. Somit kann er sich sehr gezielt, effizient und unauffällig innerhalb des Netzes bewegen und in kurzer Zeit erneut einen hohen Infektionsgrad erreichen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Bereinigung weitreichender Sicherheitsvorfälle (APT-Responder) aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### DER.2.3.A1 Einrichtung eines Leitungsgremiums [Informationssicherheitsbeauftragter (ISB)]

Um einen APT-Vorfall zu bereinigen, MUSS ein Leitungsgremium eingerichtet werden, dass alle notwendigen Aktivitäten plant, koordiniert und überwacht. Dem Gremium MÜSSEN alle für die Aufgaben erforderlichen Weisungsbefugnisse übertragen werden. 

Wenn ein solches Leitungsgremium bereits eingerichtet wurde, als der APT-Vorfall detektiert und klassifiziert wurde, SOLLTE dasselbe Gremium auch die Bereinigung planen und leiten. Wurde schon ein spezialisierter Forensik-Dienstleister hinzugezogen, um den APT-Vorfall zu analysieren, SOLLTE auch dieser bei der Vorfallsbereinigung miteinbezogen werden. 

Ist die IT zu stark kompromittiert oder sind die notwendigen Bereinigungsmaßnahmen sehr umfangreich, SOLLTE geprüft werden, ob ein Krisenstab eingerichtet werden soll. In diesem Fall MUSS das Leitungsgremium die Bereinigungsmaßnahmen überwachen. Das Leitungsgremium MUSS dann dem Krisenstab berichten. 

#### DER.2.3.A2 Entscheidung für eine Bereinigungsstrategie [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Bevor ein APT-Vorfall tatsächlich bereinigt wird, MUSS das Leitungsgremium eine Bereinigungsstrategie festlegen. Hierbei MUSS insbesondere entschieden werden, ob die Schadsoftware von kompromittierten IT-Systemen entfernt werden kann, ob IT-Systeme neu installiert werden müssen oder ob IT-Systeme inklusive der Hardware komplett ausgetauscht werden sollen. Weiterhin MUSS festgelegt werden, welche IT-Systeme bereinigt werden. Grundlage für diese Entscheidungen MÜSSEN die Ergebnisse einer zuvor durchgeführten forensischen Untersuchung sein.

Es SOLLTEN alle betroffenen IT-Systeme neu installiert werden. Danach MÜSSEN die Wiederanlaufpläne der Institution benutzt werden. Bevor jedoch Backups wieder eingespielt werden, MUSS durch forensische Untersuchungen sichergestellt sein, dass hierdurch keine manipulierten Daten oder Programme auf das neu installierte IT-System übertragen werden.

Entscheidet sich eine Institution dagegen alle IT-Systeme neu zu installieren, MUSS eine gezielte APT-Bereinigung umgesetzt werden. Um das Risiko übersehener Hintertüren zu minimieren, MÜSSEN nach der Bereinigung die IT-Systeme gezielt daraufhin überwacht werden, ob sie noch mit dem Angreifer kommunizieren.

#### DER.2.3.A3 Isolierung der betroffenen Netzabschnitte

Die von einem APT-Vorfall betroffenen Netzabschnitte MÜSSEN vollständig isoliert werden (Cut-Off). Insbesondere DÜRFEN die betroffenen Netzabschnitte NICHT mit dem Internet verbunden sein. Um den Angreifer effektiv auszusperren und zu verhindern, dass er seine Spuren verwischt oder noch IT-Systeme sabotiert, MÜSSEN die Netzabschnitte auf einen Schlag isoliert werden.

Welche Netzabschnitte isoliert werden müssen, MUSS vorher durch eine forensische Analyse bestimmt werden. Es MÜSSEN dabei sämtliche betroffenen Abschnitte identifiziert werden. Kann das nicht sichergestellt werden, MÜSSEN alle verdächtigen sowie alle auch nur theoretisch infizierten Netzabschnitte isoliert werden. 

Um Netzabschnitte effektiv isolieren zu können, MÜSSEN sämtliche lokalen Internetanschlüsse, z. B. zusätzliche DSL-Anschlüsse in einzelnen Subnetzen, möglichst vollständig erfasst und mitberücksichtigt werden.

#### DER.2.3.A4 Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln

Da davon ausgegangen werden muss, dass der Angreifer sich sämtliche auf den kompromittierten IT-Systemen vorhandenen Zugangsdaten angeeignet hat, MÜSSEN alle Zugangsdaten geändert werden, nachdem das Netz isoliert wurde. Weiterhin MÜSSEN auch zentral verwaltete Zugangsdaten zurückgesetzt werden, z. B. in Active-Directory-Umgebungen oder wenn das Lightweight DirectoryAccess Protocol (LDAP) benutzt wurde. 

Ist der zentrale Authentisierungsserver (Domaincontroller oder LDAP-Server) kompromittiert, MÜSSEN sämtliche dort vorhandenen Zugänge gesperrt und ihre Passwörter ausgetauscht werden. Dies MÜSSEN erfahrene Administratoren umsetzen, falls erforderlich mithilfe interner oder externer Forensikexperten. 

Wurden TLS-Schlüssel oder eine interne Certification Authority (CA) durch den APT-Angriff kompromittiert, MÜSSEN entsprechende Schlüssel und Infrastrukturen neu erzeugt und verteilt werden. Auch MÜSSEN die kompromittierten Schlüssel zuverlässig gesperrt werden.

#### DER.2.3.A5 Schließen des initialen Einbruchswegs

Wurde durch eine forensische Untersuchung herausgefunden, dass der Angreifer durch eine technische Schwachstelle in das Netz der Institution eingedrungen ist, MUSS diese Schwachstelle geschlossen werden. Konnten die Angreifer die IT-Systeme durch menschliche Fehlhandlungen kompromittieren, MÜSSEN organisatorische, personelle und technische Maßnahmen ergriffen werden, um ähnliche Vorfälle zukünftig zu verhindern. 

#### DER.2.3.A6 Rückführung in den Produktivbetrieb

Nachdem das Netz erfolgreich bereinigt wurde, MÜSSEN die IT-Systeme geordnet in den Produktivbetrieb zurückgeführt werden. Dabei MÜSSEN sämtliche zuvor angeschafften IT-Systeme und installierten Programme, mit denen der Angriff beobachtet und analysiert wurde, entweder entfernt oder aber in den Produktivbetrieb überführt werden. Dasselbe MUSS mit Kommunikations- und Kollaborationssystemen erfolgen, die für die Bereinigung angeschafft wurden. Beweismittel und ausgesonderte IT-Systeme MÜSSEN entweder sicher gelöscht bzw. vernichtet oder aber geeignet archiviert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Bereinigung weitreichender Sicherheitsvorfälle. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.2.3.A7 Gezielte Systemhärtung

Nach einem APT-Angriff SOLLTEN alle betroffenen IT-Systeme gehärtet werden. Grundlage hierfür SOLLTEN die Ergebnisse der forensischen Untersuchungen sein (siehe DER.2.X *IT-Forensische Analysen*). Zusätzlich SOLLTE erneut geprüft werden, ob die betroffene Umgebung noch sicher ist, z. B. mit den Ergebnissen der ausführlichen forensischen Analysen.

Wenn möglich, SOLLTEN IT-Systeme bereits während der Bereinigung gehärtet werden. Maßnahmen, die sich nicht kurzfristig durchführen lassen, SOLLTEN in einen Maßnahmenplan aufgenommen und mittelfristig umgesetzt werden. Der ISB SOLLTE dafür verantwortlich sein, den Plan aufzustellen und zu prüfen, ob er korrekt umgesetzt wurde. 

#### DER.2.3.A8 Etablierung sicherer, unabhängiger Kommunikationskanäle

Es SOLLTEN sichere Kommunikationskanäle für das Leitungsgremium und die mit der Bereinigung beauftragen Mitarbeiter etabliert werden. Es SOLLTE darauf geachtet werden, dass ein möglichst sicherer Kommunikationskanal ausgewählt wird.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.2.3.A9 Hardwaretausch betroffener IT-Systeme(CIA)

Bei IT-Systemen mit hohem Schutzbedarf SOLLTE erwogen werden, nach einem APT-Vorfall die Hardware komplett auszutauschen. Auch wenn nach einer Bereinigung bei einzelnen IT-Systemen noch verdächtiges Verhalten beobachtet wird, z. B. unerklärlicher Netzverkehr, SOLLTE das betroffene IT-System ausgetauscht werden. 

#### DER.2.3.A10 Umbauten zur Erschwerung eines erneuten Angriffs durch denselben Angreifer(CI)

Damit derselbe Angreifer nicht noch einmal einen APT-Angriff auf die IT-Systeme der Institution durchführen kann, SOLLTE der interne Aufbau der Netzumgebung abgeändert werden. Außerdem SOLLTEN Mechanismen etabliert werden, mit denen sich ein wiederkehrender Angreifer schnell detektieren lässt.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Bereinigung weitreichender Sicherheitsvorfälle" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [CS072] Erste Hilfe bei einem APT Angriff

  

 Bundesamt für Sicherheit in der Informationstechnik, Version 3.0, 01.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_072\_TLP-White.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_072_TLP-White.pdf)

 
* #### [DRP] Data Breach Response Guide

  

 Experian Data Breach Resolution, 2013  
 <https://www.experian.com/assets/data-breach/brochures/response-guide.pdf>

 
* #### [KGT] Protection from Kerberos Golden Ticket

  

 CERT-EU, 06.2014  
 [https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP\_14\_07\_PassTheGolden\_Ticket\_v1\_1.pdf](https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP_14_07_PassTheGolden_Ticket_v1_1.pdf)

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote-Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
* #### [SANS1] When Breaches Happen: Top Five Questions to Prepare For

  

 SANS Institute, 2000  
 <https://www.sans.org/reading-room/whitepapers/analyst/breaches-happen-top-questions-prepare-35220>

 
* #### [SANS2] Detection and Recovery from a Major security Breach

  

 SANS Institute, 2000  
 <https://giac.org/paper/gcux/50/detection-recovery-major-security-breach/100810>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Bereinigung weitreichender Sicherheitsvorfälle" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

