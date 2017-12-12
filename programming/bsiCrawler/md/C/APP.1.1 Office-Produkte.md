1 Beschreibung
--------------

### 1.1 Einleitung

Die Gruppe der Office-Produkte umfasst alle Anwendungen, die dazu dienen, Dokumente zu erstellen, zu bearbeiten und zu betrachten. Dazu zählen unter anderem die freie Anwendung LibreOffice und die proprietäre Anwendung Microsoft Office, die in vielen Institutionen genutzt werden. Office-Produkte gehören für die meisten Institutionen zur notwendigen IT-Grundausstattung. Sie umfassen unter anderem Programme zur Textverarbeitung, Tabellenkalkulation und Erstellung von Präsentationen sowie Zeichenprogramme und einfache Datenbanksysteme. Die Nutzung von Office-Anwendungen ermöglicht und vereinfacht es, Informationen zu erheben und zu verarbeiten. 

### 1.2 Zielsetzung

Ziel des vorliegenden Bausteins ist der Schutz der Informationen, die bei der Nutzung von Office-Produkten verarbeitet und genutzt werden. Dazu werden spezielle Anforderungen an die Funktionsweise der Komponenten von Office-Produkten gestellt. Der Baustein zeigt Anforderungen auf, die zur Absicherung von Office-Produkten vor spezifischen Gefährdungen umgesetzt werden sollten.

### 1.3 Abgrenzung

Dieser Baustein betrachtet den Einsatz von Office-Produkten aus Sicht des IT-Betriebs und gibt Hinweise für Benutzer, wie Office-Produkte eingesetzt werden sollten. Es werden spezifische Anforderungen gestellt, die beim Einsatz von Office-Produkten zu beachten sind. Ergänzend zu den Anforderungen dieses Bausteins muss die Umsetzung der Anforderungen des übergeordneten Bausteins CON.4 *Auswahl und Einsatz von Standardsoftware* gewährleistet werden. E-Mail- und PIM-Anwendungen werden in diesem Baustein ausgeklammert, die entsprechenden Anforderungen sind im Baustein APP.1.4 *Groupware* dokumentiert. Bei E-Mail- und PIM-Anwendungen der Firma Microsoft ist zusätzlich der Baustein APP.1.1 *Microsoft Exchange/Outlook *zu beachten. Bei der Verwendung von integrierten Datenbanksystemen wie Base in LibreOffice oder Access in Microsoft Office muss der Baustein APP.4.3 *Datenbank* berücksichtigt werden. Ebenfalls im vorliegenden Baustein ausgenommen sind reine Cloud-Office-Anwendungen wie Googles G Suite (Docs, Sheets und so weiter). Anforderungen an Cloud-Anwendungen sind in den Bausteinen OPS.2.2 *Cloud-Nutzung *und* *APP.5.3 *Cloud-Anwendungen aus Client-Sicht *festgelegt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich von Office-Produkten von besonderer Bedeutung:

### 2 1 Fehlende Anpassung der Office-Produkte an den Bedarf der Institution

Durch mangelnde Beachtung von Anforderungen an Office-Produkte bei der Beschaffung oder beim Anpassen der Software kann der Betrieb erheblich gestört werden. Gründe hierfür können beispielsweise fehlende Kompatibilität mit vorhandenen Vorlagen und Dokumenten, mangelnder Funktionsumfang der eingesetzten Version oder fehlende Interoperabilität mit Anwendungen von Geschäftspartnern sein. Sollten Office-Produkte nicht an den Bedarf der Institution angepasst werden, kann dies zu Performance-Verlusten, Störungen oder Fehlern innerhalb der Geschäftsprozesse führen.

### 2 2 Fehlendes oder unzureichendes Test- und Freigabeverfahren bei Office-Produkten

Werden neue Office-Produkte sowie ihre Integration in die Institution nicht oder nur unzureichend getestet und ohne Installationsvorschriften freigegeben, kann es vorkommen, dass Fehler nicht erkannt werden oder dass die notwendigerweise einzuhaltenden Installationsparameter nicht erkannt bzw. nicht beachtet werden. Fehler in Office-Produkten, die aus einem fehlenden oder unzureichenden Test- und Freigabeverfahren resultieren, stellen eine erhebliche Gefährdung für den IT-Betrieb dar. Arbeitsabläufe können durch Office-Produkt-Fehler maßgeblich behindert werden. Fehlerhafte Updates der Office-Produkte können zu Datenverlusten führen oder die Verfügbarkeit von genutzten Datenbanken einschränken. 

### 2 3 Schützenswerte Daten in Restinformationen in Office-Dokumenten

Office-Dokumente speichern in der Regel Meta-Informationen zum Dokument selbst, sowie Informationen zum Autor und zur Institution. Diese Meta-Informationen lassen sich um beliebige, benutzerdefinierte Einträge erweitern, unterstützen die Arbeitsabläufe der Geschäftsprozesse und sorgen für eine geeignete Transparenz. Zusätzlich bieten Office-Produkte die Möglichkeit, Kommentare im Dokument anzulegen und im Überarbeiten-Modus Informationen hinzuzufügen oder zu ändern. Diese und weitere Restinformationen können vertrauliche Informationen enthalten, die Dritten nicht zugänglich gemacht werden dürfen. Dies kann andernfalls zu einem Verlust der Vertraulichkeit und zur späteren Verfälschung der Restinformationen führen und finanzielle, prozessuale und Image-Schäden verursachen. 

### 2 4 Bezug von Office-Produkten und Updates aus unzuverlässiger Quelle

Werden Installationsquellen oder Updates von Office-Produkten aus inoffiziellen Quellen bezogen, besteht keine Garantie, dass die Software einwandfrei funktioniert und frei von Schadcode ist. Das gilt sowohl für die Office-Produkte an sich, als auch für Funktionen, die als Plug-in bzw. Add-on oder als Makro in Dokumenten vorliegen. Dies kann dazu führen, dass Berechnungen falsche Ergebnisse liefern oder die Integrität und Verfügbarkeit von Systemen beeinträchtigt wird. 

### 2 5 Manipulation von Office-Dokumenten

Unter der Manipulation von Office-Dokumenten ist die Veränderung von Informationen zu verstehen. Office-Dokumente können in der Regel verschiedene Aktive Inhalte enthalten, die mitunter für komplexe Automatisierungen genutzt werden. Aktive Inhalte können aber auch Schadcode enthalten, der beim Öffnen des Dokuments mit den Rechten des Benutzers ausgeführt wird. Solche Schadprogramme in Office-Dokumenten können neben Manipulationen des betroffenen Dokumentes weitere Dokumente unerkannt verändern oder sich in weitere Dokumente verbreiten. Alle betroffenen Geschäftsprozesse der Institution können in ihren Funktionen gestört oder blockiert werden. Im schlimmsten Fall bleibt die Manipulation unerkannt und führt zu Sicherheitslücken und zur Verarbeitung von verfälschten Informationen.

### 2 6 Mangelnde Verbindlichkeit von Office-Dokumenten

Je nach Einsatzzweck kann es notwendig sein, Office-Dokumente verbindlich einem oder mehreren Autoren zuordnen zu können oder nachweisen zu können, dass jemand ein Dokument zur Kenntnis genommen hat. Kann diese Funktion leicht umgangen werden bzw. ist sie gar nicht vorgesehen oder entspricht sie nicht den gesetzlichen Anforderungen, können ungültige Verträge entstehen oder die Rechtmäßigkeit bestehender Verträge angefochten werden. 

### 2 7 Integritätsverlust von Office-Dokumenten

Die Integrität von Office-Dokumenten kann durch unbeabsichtigte Änderungen oder durch vorsätzliche Manipulationen der Dokumenteninhalte verfälscht werden. Durch einen unbedachten Umgang mit Office-Produkten oder durch Unkenntnis der Benutzer im Umgang mit Office-Dokumenten kann es zu unerkannten Änderungen an Dokumenten kommen. Dies ist dann besonders problematisch, wenn es sich um Dokumente im produktiven Einsatz handelt. Wird mit Dokumenten weitergearbeitet, die unerkannt verfälscht wurden, werden möglicherweise falsche geschäftliche Entscheidungen getroffen oder es kann ein Image-Schaden für die Institution entstehen.

### 2 8 Software-Schwachstellen in Office-Produkten

Software-Schwachstellen in Office-Produkten werden trotz intensiver Tests meist nicht vollständig vor der Auslieferung an die Kunden entdeckt. Werden diese Software-Schwachstellen nicht rechtzeitig erkannt, können Abstürze und Fehler der Anwendungen resultieren. Zu den Folgen nicht behobener Fehler können unter anderem falsche Berechnungsergebnisse oder Integritätsverlust in Dokumenten gehören. Durch Software-Schwachstellen bzw. -fehler kann es außerdem zu schwerwiegenden Sicherheitslücken in Office-Produkten kommen. Solche Sicherheitslücken können unter Umständen von Angreifern ausgenutzt werden, um Schadcode einzuschleusen.

### 2 9 Einsatz von unlizenzierten Office-Produkten

Unlizenzierte Office-Produkte sind eine mögliche finanzielle Gefahrenquelle für Institutionen. Werden Office-Produkte ohne gültige Software-Lizenz eingesetzt, weil beispielsweise das Lizenzvolumen unbemerkt überschritten wurde, kann dies bei Bekanntwerden Vertragsstrafen zur Folge haben. Umgekehrt werden möglicherweise zu hohe Lizenzkosten entrichtet, da Office-Produkte an Arbeitsplätzen installiert sind, an denen sie nicht benötigt werden.

### 2 10 Datenverlust durch Passwortschutz von Office-Dokumenten

Datenverluste bei Office-Dokumenten können Geschäftsprozesse blockieren. In der Regel bieten Office-Produkte die Möglichkeit, Dokumente beim Speichern mit einem Passwort zu versehen, welches für das Öffnen oder Bearbeiten des Dokuments benötigt wird. Bei unvorsichtigem Einsatz dieser Funktion ist es möglich, dass vergebene Dokumenten-Passwörter nicht mehr bekannt oder nicht mehr auffindbar sind. Dadurch können wichtige Dokumente nicht mehr gelesen oder nur mit erhöhtem Aufwand weiter bearbeitet werden. Dieser Mehraufwand muss technisch und organisatorisch kompensiert werden, was wiederum zu einer erhöhten Arbeitslast führt.

### 2 11 Unerlaubtes Ausüben von Rechten bei Office-Produkten

Zugriffsrechte werden als organisatorische Maßnahmen eingesetzt, um Informationen, Geschäftsprozesse und IT-Systeme vor unbefugtem Zugriff zu schützen. Wenn unautorisierte Personen durch falsch gesetzte Berechtigungen auf Office-Produkte zugreifen können, kann dies die Vertraulichkeit und Integrität der Informationen gefährden, indem Informationen verändert, gelöscht oder unsachgemäß erstellt werden. Solche Sicherheitslücken entstehen meist durch fehlerhafte Rechtevergaben. Betroffene Geschäftsprozesse können korrumpiert werden sowie unbeabsichtigt fehlerhafte Informationen verarbeiten oder schützenswerte Informationen offenlegen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Office-Produkten aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.1.1.A1 Sicherstellen der Integrität von Office-Produkten

Bei der Installation von Office-Produkten MUSS sichergestellt werden, dass ausschließlich unveränderte Kopien der freigegebenen Originalsoftware verwendet werden. Updates MÜSSEN ausschließlich aus sicheren Quellen bezogen werden. Falls zu einem Office-Produkt Prüfsummen angeboten werden, SOLLTEN diese vor der Installation überprüft werden. Falls zu einem Office-Produkt digitale Signaturen verfügbar sind, SOLLTEN diese vor der Installation des Pakets überprüft werden. Die Administratoren SOLLTEN über die Bedeutung und Aussagekraft von Prüfsummen und digitalen Signaturen informiert werden. Ebenso wie bei einer Neuinstallation MUSS bei der Installation von Updates sichergestellt werden, dass die Update-Pakete unverändert sind.

#### APP.1.1.A2 Einschränken von Aktiven Inhalten [Benutzer]

Das automatische Ausführen von eingebetteten Aktiven Inhalten, wie beispielsweise Makros oder ActiveX-Elementen, MUSS in den Einstellungen aller verwendeten Office-Produkte deaktiviert werden. Ist die Ausführung Aktiver Inhalte für einen Geschäftsprozess notwendig, MUSS darauf geachtet werden, dass nur Aktive Inhalte von vertrauenswürdigen Quellen ausgeführt werden. Alle Benutzer MÜSSEN in Schulungen bezüglich der Gefährdungen durch Aktive Inhalte sensibilisiert werden und hinsichtlich der Funktionen zum Einschränken Aktiver Inhalten eingewiesen werden. 

#### APP.1.1.A3 Öffnen von Dokumenten aus externen Quellen

Alle aus externen Quellen bezogenen Dokumente MÜSSEN vor dem Öffnen auf Schadsoftware überprüft werden. Alle als problematisch eingestuften und zusätzlich alle innerhalb der Institution nicht benötigten Dateiformate MÜSSEN verboten werden. Die Benutzer MÜSSEN zum Umgang mit Dokumenten aus externen Quellen geschult und sensibilisiert werden. Die Prüfung von Dokumenten aus externen Quellen SOLLTE durch technische Maßnahmen erzwungen werden.

#### APP.1.1.A4 Absichern des laufenden Betriebs von Office-Produkten

IT-Betrieb und ISB MÜSSEN sich regelmäßig über bekannt gewordene Sicherheitslücken der Office-Produkte informieren. Vorhandene Patches MÜSSEN zeitnah eingespielt werden.

Die Benutzer SOLLTEN über die Möglichkeiten und Grenzen von Sicherheitsfunktionen der eingesetzten Software und der genutzten Speicherformate informiert werden. Die Vorgaben für die sichere Nutzung von Office-Produkten SOLLTEN in der Sicherheitsrichtlinie integriert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Office-Produkte. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.1.1.A5 Auswahl geeigneter Office-Produkte

Im Rahmen der Beschaffung von Office-Anwendungen SOLLTEN die Anforderungen der Institution an Office-Produkte durch die Fach- und IT-Abteilung erhoben werden. Diese sollten in einem Anforderungskatalog dokumentiert werden. Sind alle Anforderungen an das zu beschaffende Office-Produkt dokumentiert, SOLLTEN die am Markt erhältlichen Produkte dahingehend untersucht werden, inwieweit sie diese Anforderungen der Institution erfüllen. Bei der Auswahl zwischen mehreren Alternativen SOLLTEN auch zusätzliche Aufwände berücksichtigt werden; zu diesen zählen beispielsweise Mehraufwänden für die Schulung von Administratoren und Benutzern oder für die Migration.

#### APP.1.1.A6 Testen neuer Versionen von Office-Produkten

Neue Versionen von Office-Produkten SOLLTEN vor dem produktiven Einsatz auf Kompatibilität mit etablierten Arbeitsmitteln (z. B. Dokumentenvorlagen, Formulare) der Institution geprüft werden. Zu diesem Zweck SOLLTEN Testmethoden für die Einzeltests (Testarten, -verfahren und -werkzeuge) entwickelt und freigegeben werden. Es SOLLTE sichergestellt sein, dass wichtige Arbeitsmittel auch mit der neuen Software-Funktion einwandfrei funktionieren. Bei entdeckten Inkompatibilitäten SOLLTE ein Migrationsplan für die betroffenen Dokumente erstellt werden.

#### APP.1.1.A7 Installation und Konfiguration von Office-Produkten

Für die eingesetzten Office-Produkte SOLLTE eine an den Bedarf der Institution angepasste Standardkonfiguration erstellt und genutzt werden. Diese Konfiguration SOLLTE in einer Installations- und Konfigurationsanweisung dokumentiert werden. Die Installation und Konfiguration SOLLTE gemäß der Anweisung erfolgen und die Standardeinstellungen anwenden. Alle notwendigen Abweichungen von der definierten Standardkonfiguration SOLLTEN nachvollziehbar dokumentiert werden und bedürfen für den Gebrauch einer Zustimmung durch eine geeignete Freigabeinstanz. Im Falle von Pilot-Installationen gilt, dass diese immer durch die IT-Abteilung begleitet werden SOLLTEN. Vor und nach den Installationen SOLLTEN Datensicherungen der Office-Produkte auf allen betroffenen IT-Systemen durchgeführt werden.

#### APP.1.1.A8 Versionskontrolle von Office-Produkten

Es SOLLTE eine regelmäßige Kontrolle der installierten Versionen von Office-Produkten erfolgen. Diese Bestandsführung der Software-Lizenzen SOLLTE bei jeder Installation oder Deinstallation aktualisiert werden. Darüber hinaus SOLLTEN die verschiedenen Konfigurationen der installierten Office-Produkte dokumentiert werden.

#### APP.1.1.A9 Beseitigung von Restinformationen vor Weitergabe von Dokumenten [Benutzer]

Vor der Weitergabe von Dokumenten an Dritte SOLLTEN alle nicht benötigten und vertraulichen Restinformationen aus Office-Dokumenten entfernt werden. Zusätzlich SOLLTEN die Metadaten bereinigt werden. Alle Benutzer SOLLTEN bezüglich der Risiken durch Restinformationen sowie der Möglichkeiten zur Beseitigung in den eingesetzten Office-Produkten sensibilisiert und geschult werden. Die Übermittlung von Dokumenten SOLLTE in einem nicht-veränderbaren Format erfolgen, falls eine Bearbeitung durch den Empfänger nicht erforderlich ist. 

#### APP.1.1.A10 Regelung der Software-Entwicklung durch Endbenutzer [Benutzer]

Es SOLLTEN verbindliche Regelungen für die Softwareentwicklung auf Basis von Office-Anwendungen (z. B. Makros, Tabellenkalkulation) durch Endbenutzer getroffen werden, siehe auch APP.5.2.A2 Einschränken von Aktiven Inhalten. Zunächst SOLLTE in jeder Institution die Grundsatz-Entscheidung getroffen werden, ob solche Eigenentwicklungen erwünscht sind oder nicht. Die Entscheidung SOLLTE in den betroffenen Sicherheitsrichtlinien dokumentiert werden. Werden Eigenentwicklungen erlaubt, SOLLTE ein Verfahren für den Umgang mit entsprechenden Funktionen der Office-Produkte für die Endbenutzer entwickelt werden. Verantwortlichkeiten SOLLTEN klar definiert werden. Alle Informationen über die erstellten Anwendungen SOLLTEN dokumentiert werden. Aktuelle Versionen SOLLTEN allen betroffenen Benutzern zeitnah zugänglich gemacht werden.

#### APP.1.1.A11 Geregelter Einsatz von Erweiterungen für Office-Produkte

Alle Erweiterungen von Office-Produkten SOLLTEN vor dem produktiven Einsatz analog zum Testvorgehen von neuen Versionen getestet werden. Die durchzuführenden Tests SOLLTEN ausschließlich auf isolierten Testsystemen durchgeführt werden. Die Tests SOLLTEN prüfen, dass Erweiterungen keine negativen Auswirkungen für die Office-Produkte und laufenden IT-Systeme haben. Die Tests der eingesetzten Erweiterungen SOLLTEN einem definierten Testplan folgen, der die Nachvollziehbarkeit für Dritte gewährleistet.

#### APP.1.1.A12 Verzicht auf Cloud-Speicherung [Benutzer]

Die in einigen Office-Produkten integrierten Cloud-Speicher-Funktionen SOLLTEN grundsätzlich deaktiviert werden. Alle Cloud-Laufwerke SOLLTEN deaktiviert werden. Alle Dokumente SOLLTEN auf zentral verwalteten File-Servern der Institution gespeichert werden. Um Dokumente für Dritte zur Sichtung oder Bearbeitung freizugeben, SOLLTEN spezialisierte Anwendungen wie beispielsweise geeignete Datenräume eingesetzt werden, die über Sicherheitsfunktionen wie eine verschlüsselte Datenablage und -versendung und ein geeignetes System zur Benutzer- und Rechteverwaltung verfügen. 

#### APP.1.1.A13 Verwendung von Viewer-Funktionen [Benutzer]

Daten aus potentiell unsicheren Quellen wie dem Internet oder Anhänge von E-Mail-Nachrichten SOLLTEN automatisch in einem geschützten Modus geöffnet werden, in dem sie nicht unmittelbar bearbeitet werden können. Nur eine allgemeine Navigation SOLLTE ermöglicht werden. Diese Funktion SOLLTE NICHT durch den Benutzer deaktivierbar sein. Es SOLLTEN entsprechende Viewer-Anwendungen verwendet werden, wenn diese verfügbar sind. Es kann eine Liste vertrauenswürdiger Orte definiert werden, von denen Inhalte unmittelbar geöffnet und bearbeitet werden können. 

#### APP.1.1.A14 Schutz gegen nachträgliche Veränderungen von Informationen [Benutzer]

In Abhängigkeit vom geplanten Verwendungszweck von Dokumenten SOLLTEN die in Anwendungsprogrammen vorhandenen Sicherheitsmechanismen genutzt werden, um den weiteren Umgang mit den erstellten Dateien einzuschränken. Die Mitarbeiter SOLLTEN darauf hingewiesen werden, wie diese Sicherheitsmechanismen funktionieren und wie sie anzuwenden sind.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.1.1.A15 Einsatz von Verschlüsselung und Digitalen Signaturen(CI)

Daten mit erhöhtem Schutzbedarf SOLLTEN vor einer Übertragung oder Speicherung verschlüsselt werden, um die Vertraulichkeit sicherzustellen. Vor der Nutzung eines in ein Office-Produkt integrierten Verschlüsselungsverfahrens SOLLTE geprüft werden, ob es einen ausreichenden Schutz bietet, das gilt besonders für ältere Produktversionen. Die IT-Systeme von Absender und Empfänger SOLLTEN den Zugriffsschutz auf die verwendete Methode zur Verschlüsselung gewährleisten. Benutzer SOLLTEN im Umgang mit den Verschlüsselungsfunktionen geschult und sensibilisiert werden. Zusätzlich SOLLTE ein Verfahren eingesetzt werden, mit dem Makros und Dokumente digital signiert werden können. Die Gültigkeit der verwendeten Zertifikate SOLLTE zeitlich begrenzt werden. 

#### APP.1.1.A16 Integritätsprüfung von Dokumenten(I)

Zum Schutz vor zufälliger Veränderung von Daten mit erhöhtem Schutzbedarf bei einer Übertragung und/oder Speicherung SOLLTEN Prüfsummen-Verfahren eingesetzt werden. Es SOLLTE ein Verfahren ausgewählt werden, das dazu in der Lage ist, die Daten selbstständig zu korrigieren. Zum Schutz vor Manipulation SOLLTEN darüber hinaus kryptographische Prüfsummen-Verfahren eingesetzt werden. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Office-Produkte" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [LIBRE] LibreOffice

  

 The Document Foundation - LibreOffice, (zuletzt abgerufen am 28.09.2017)  
 <https://de.libreoffice.org>

 
* #### [MSTN] Microsoft Technet

  

 Microsoft, (zuletzt abgerufen am 28.09.2017)  
 <https://technet.microsoft.com/de-de>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Office-Produkte" von Bedeutung.

* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.37 Abstreiten von Handlungen
* G 0.39 Schadprogramme
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

