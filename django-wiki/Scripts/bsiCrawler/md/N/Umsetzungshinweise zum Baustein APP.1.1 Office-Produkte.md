1 Beschreibung
--------------

### 1.1 Einleitung

Office-Produkte sind seit Langem fester Bestandteil der Standardausstattung der IT im Büroumfeld. Schriftstücke digital zu bearbeiten und Kalkulationen sowie Präsentationen am PC zu erstellen, hat den Büroalltag stark verändert. Entsprechend betrachten die meisten Mitarbeiter Office-Produkte als Grundausstattung der IT. Gerade wegen der großen Verbreitung von Office-Produkten werden diese auch als Angriffsweg genutzt, beispielsweise um mittels Makros in Office-Dokumenten Schadsoftware zu verbreiten.

Daher sollten für einen sicheren Einsatz von Office-Produkten Sicherheitsmaßnahmen geplant und umgesetzt werden, die dem Schutzbedarf der Institution angemessen sind.

Die nachfolgenden Umsetzungshinweise beziehen sich in einigen Beispielen, falls nicht anders erwähnt, auf Microsoft Office ab Version 2007 und LibreOffice ab Version 5.1. Ältere Versionen von Microsoft Office und LibreOffice werden von den Herstellern nicht mehr mit Updates versorgt und sollten daher nicht mehr im produktiven Betrieb eingesetzt werden.

### 1.2 Lebenszyklus

**Planung und Konzeption** 

In der Planungs- und Konzeptionsphase sollen Grundsätze definiert werden, wie Office-Produkte in der Institution zu verwenden sind und welche Anforderungen die Institution an Office-Produkte hat. Damit sollen für die Institution und die Anforderungen der Mitarbeiter passende Office-Produkte ausgewählt werden (siehe APP.1.1.M5 Auswahl geeigneter Office-Produkte). Ebenso sollte bereits in der Planungs- und Konzeptionsphase definiert werden, wie mit Aktiven Inhalten (z. B. Makros) in Office-Dokumenten umgegangen werden soll (siehe APP.1.1.M2 Einschränken von Aktiven Inhalten) und ob Erweiterungen der ausgewählten Office-Produkte eingesetzt werden sollen (APP.1.1.M11 Geregelter Einsatz von Erweiterungen für Office-Produkte).

**Beschaffung** 

Bei der Beschaffung von Office-Produkten spielt die Lizenzverwaltung eine große Rolle. Die Hersteller bieten meist mehrere Lizenzmodelle an, von denen je nach Umfang der benötigten Installationen für die Institution andere Modelle sinnvoll sind (siehe APP.1.1.M8 Versionskontrolle von Office-Produkten).

**Umsetzung** 

Vor dem Einsatz in der Institution sollten neue Versionen von Office-Produkten getestet werden (siehe APP.1.1.M6 Testen neuer Versionen von Office-Produkten), um zu gewährleisten, dass bestehende Arbeitsmittel der Institution (z. B. Dokumentvorlagen oder Formblätter) auch mit der neuen Version korrekt funktionieren. Je nach den festgelegten Grundsätzen, wie innerhalb der Institution mit Office-Produkten gearbeitet werden soll, muss die eingesetzte Software anders konfiguriert werden. Bei der Konfiguration sollte sichergestellt sein, dass auf allen Arbeitsplätzen der Institution eine möglichst einheitliche Konfiguration der Office-Produkte eingespielt ist.

**Betrieb** 

Um die Sicherheitsanforderungen der Institution im täglichen Einsatz von Office-Produkten zu erfüllen, müssen die Benutzer der Office-Produkte mit eingebunden werden. So müssen sie über Sicherheitsmaßnahmen informiert werden, die nicht rein technisch umgesetzt werden können und die Mitwirkung der Benutzer benötigen. Relevante Themen sind hierbei das Öffnen von Office-Dokumenten aus externen Quellen, der Umgang mit Meta- oder Restinformationen in Office-Dokumenten, der Umgang mit Möglichkeiten zur Cloud-Speicherung sowie die Integritätsprüfung von Office-Dokumenten und der Umgang mit signierten oder passwortgeschützten Office-Dokumenten, siehe z. B. APP.1.1.M9 Beseitigung von Restinformationen vor Weitergabe von Dokumenten und APP.1.1.M12 Verzicht auf Cloud-Speicherung.

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Office-Produkte" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### APP.1.1.M1 Sicherstellen der Integrität von Office-Produkten

Office-Produkte sollte grundsätzlich nur aus bekannten Quellen, wie Originaldatenträgern oder der Webseite des Herstellers, bezogen werden. Es sollte dokumentiert werden, welche Quelle für die eingesetzten Office-Produkte gewählt wird und wie der Prozess zur Integritätssicherung der Installationsquellen gestaltet ist. 

In der Vergangenheit kam es immer wieder zu Vorfällen, bei denen Angreifer Softwarepakete auf den Downloadseiten von Softwareherstellern manipulieren konnten. Um zu verhindern, dass manipulierte Software in der Institution ausgerollt wird, sollte die Authentizität von Softwarepaketen der eingesetzten Office-Produkte streng überprüft werden.

Um zu verhindern, dass unberechtigt modifizierte Versionen der Office-Produkte in der Institution installiert werden, sollte die Software vor der Installation auf Integrität und Authentizität geprüft werden. Für diese Prüfung stellen viele Hersteller signierte Prüfsummen zur Verfügung, mittels derer verifiziert werden kann, dass die Software ausschließlich durch den Hersteller verändert wurde. 

Die Authentizität von Microsoft Office wird beim Installieren durch den Installationsagenten sichergestellt. Zusätzlich kann die Signatur über die Dateieigenschaften der Softwarepakete unter *Digitale Signaturen | Details* überprüft werden. Microsoft bietet außerdem das Kommandozeilenprogramm SignTool an, mit dem Signaturen von Programmen überprüft werden können. Wird Microsoft Office über den Windows-Update-Mechanismus aktuell gehalten, wird die Signatur bei Aktualisierungen automatisch geprüft.

Für LibreOffice sind mehrere Methoden verfügbar, um die Integrität der Softwarepakete zu prüfen:

Wird die Integrität der Office-Produkte manuell geprüft, sollte die Prüfung auf einem gehärteten System erfolgen. Die Programme, mit denen die Integrität geprüft wird, sollten vor Manipulation geschützt werden.

Das gewählte Vorgehen für die Integritätsprüfung der Office-Produkte sollte an geeigneter Stelle (beispielsweise im Betriebshandbuch) für Dritte nachvollziehbar dokumentiert werden. Bei hohen Anforderungen an die Integrität der Office-Produkte kann es Sinn machen, die Protokolle über die durchgeführten Integritätsprüfungen aufzubewahren.

#### APP.1.1.M2 Einschränken von Aktiven Inhalten [Benutzer]

Office-Produkte bieten häufig die Möglichkeit, Dokumente um Aktive Inhalte zu erweitern. Aktive Inhalte sind beispielsweise Makros, mit denen aufwändigere Berechnungen durchgeführt werden oder Aktive-X-Steuerelemente, mit denen in Office-Dokumenten umfangreiche Formulare eingebettet werden können. In integrierten Programmierumgebungen der Office-Produkte können Aktive Inhalte mit beliebig komplexen Funktionen entwickelt werden. 

Allerdings werden Aktive Inhalte auch sehr häufig genutzt, um Schadcode in Office-Dokumente einzubetten und so zu verbreiten. Daher sollte das automatische Ausführen von Aktiven Inhalten in den Einstellungen der Office-Produkte verhindert werden.

In Microsoft Office kann der Umgang mit Aktiven Inhalten im Sicherheitscenter konfiguriert werden. Das Sicherheitscenter ist zu finden unter *Datei | Optionen | Sicherheitscenter | Einstellungen für das Sicherheitscenter*. Dort kann konfiguriert werden, wie Microsoft Office mit Makros und Aktive-X-Komponenten umgehen soll.

In LibreOffice kann in den Optionen eingestellt werden, wie Aktive Inhalte behandelt werden. Die Sicherheitsoptionen zu den Makros sind zu finden unter *Extras | Optionen | LibreOffice | Sicherheit | Makrosicherheit*.

Bei manchen Office-Produkten besteht die Möglichkeit, digital signierte Aktive Inhalte, die von vertrauenswürdigen Quellen stammen, zu aktivieren. Diese Funktion ist vor allem dann sinnvoll, wenn Makros in organisationseigenen Office-Dokumenten benötigt werden. So werden Benutzer nicht unnötig oft mit der Warnung vor Aktiven Inhalten konfrontiert, was der Sensibilisierung der Benutzer zugute kommt.

Zudem müssen Benutzer auf die Gefahren, die sich durch Aktive Inhalte ergeben, hingewiesen werden. Keinesfalls dürfen die Benutzer die Aktiven Inhalte beim Öffnen leichtfertig aktivieren. Im Zweifel sollten die Benutzer sich an den IT Service Desk der Institution wenden, der gemeinsam mit dem IT-Betrieb entscheiden kann, wie mit den Dokumenten zu verfahren ist. Beispielsweise ist es möglich, Dokumente mit Aktiven Inhalten in abgeschotteten IT-Umgebungen zu prüfen.

Auch Aktive Inhalte in PDF-Dateien eröffnen Sicherheitsrisiken, werden aber nur selten tatsächlich benötigt. Daher sollte die automatische Ausführung solcher Inhalte in den PDF-Anzeige-Programmen deaktiviert werden.

#### APP.1.1.M3 Öffnen von Dokumenten aus externen Quellen

Office-Dokumente, die aus externen Quellen stammen (z. B. von Webseiten heruntergeladen, von externen Mitarbeitern oder Geschäftspartnern erhalten) müssen mit besonderer Vorsicht behandelt werden. Es dürfen keine Dokumente geöffnet werden, die unerwartet erhalten wurden oder deren Absender bzw. Herkunft unbekannt ist. Grundsätzlich müssen Office-Dokumente aus externen Quellen wie ausführbare Dateien behandelt werden und vor dem ersten Öffnen zumindest auf Schadsoftware geprüft werden.

Microsoft hat mit Microsoft Office 2007 das Open XML Dateiformat als Standard eingeführt. Dateien im Open XML Dateiformat, die Makros enthalten, sind mit einem „M“ in der Dateiendung gekennzeichnet. Beispielsweise haben Word-Dokumente mit Makros die Endung .DOCM statt .DOCX. Enthält eine Office Open XML Datei Makros, ohne entsprechend gekennzeichnet zu sein, so verweigert Microsoft Office, die Datei zu öffnen (beispielsweise wenn Makros in einer Datei mit der Endung .DOCX enthalten sind). Ältere Dokumentenformate (z. B. .DOC) können grundsätzlich Makros enthalten und werden von Microsoft Office ab Version 2007 gemäß der Einstellungen im Sicherheitscenter behandelt (siehe APP.1.1.M2 Einschränken von Aktiven Inhalten). In der folgenden Auflistung sind Dokumententypen von Microsoft Office aufgeführt, die Makros enthalten können und daher besonders aufmerksam behandelt werden sollten:

* .DOC 
* .DOT 
* .DOCM 
* .DOTM 
* .XLA 
* .XLS 
* .XLT 
* .XLSB 
* .XLSM 
* .XLTM 
* .XLAM 
* .PPT 
* .PPTM 
* .POTM 
* .PPSM 
* .PPAM 
* .PPA 
Bei Microsoft Office kann zusätzlich die Office-Dateiüberprüfung aktiviert werden. Dabei werden ältere Office-Dateiformate beim Öffnen gegen ein Binärschema verglichen, um mögliche Angriffe auf noch unbekannte Softwarefehler in Microsoft Office zu erkennen. Entspricht die geöffnete Datei nicht dem bekannten Binärschema, wird eine Warnung ausgegeben. Bei strengeren Sicherheitsanforderungen kann die Office-Dateiüberprüfung so konfiguriert werden, dass Dokumente, die die Prüfung nicht bestehen, nicht geöffnet werden können.

Betriebssystem, Webbrowser und E-Mail Client sollten so konfiguriert werden, dass vor dem Öffnen von Dateien aus externen Quellen (z. B. USB-Sticks von Dritten, Downloads von Websites, oder E-Mails) die Überprüfung auf Schadsoftware obligatorisch ist (siehe Baustein OPS.1.1.4 Schutz vor Schadprogrammen).

Auch bei im alltäglichen Einsatz weniger geläufigen Dateiformaten ist Vorsicht geboten. Beispielsweise ist das im Druckumfeld nach wie vor verbreitete PostScript neben einer Seitenbeschreibungssprache, die beschreibt, wie Informationen exakt auf Papier oder in entsprechenden Anzeige-Programmen dargestellt werden sollen, auch eine vollständige Programmiersprache. So kann es zu Problemen ähnlich wie bei Makro-Viren kommen.

#### APP.1.1.M4 Absichern des laufenden Betriebs von Office-Produkten

Die meisten Hersteller von Office-Anwendungen bieten auf ihren Webseiten Empfehlungen für eine sichere Konfiguration der Produkte sowie über den Umgang mit identifizierten Sicherheitslücken. Diese sollten genutzt werden. Verfügbare Patches und Updates sollten zeitnah eingespielt werden.

Office-Software und andere Standardsoftware sollte nie mit Administratorrechten gestartet werden. Es sollten nur solche Dateien direkt in den Anwendungen geöffnet werden, deren Herkunft als vertrauenswürdig eingeschätzt wird. Bevor Dateien aus externen Quellen geöffnet werden, müssen sie vorab durch ein aktuelles Virenschutzprogramm überprüft werden.

Standardsoftware ist im Allgemeinen nicht auf ein hohes Sicherheitsniveau ausgelegt. Alle Mitarbeiter sollten daher darauf hingewiesen werden, dass besonders schutzbedürftige Informationen nicht beliebig auf einem Standard-Büroarbeitsplatz verarbeitet werden sollten. Einige Standardprodukte bieten eine Reihe von Sicherheitsfunktionen an, die aber meist deutlich weniger Sicherheit bieten als spezielle Sicherheitsprodukte für den erhöhten Schutzbedarf. Die Benutzer sollten über diese Sicherheitsfunktionen und deren Wirksamkeit informiert werden. Dabei ist vor allen Dingen sicherzustellen, dass die Benutzer sich nicht in einer falschen, trügerischen Sicherheit wiegen und dass die Nutzung dieser Sicherheitsfunktionen keine Sicherheitslücken öffnet. Benutzer sollten darüber informiert werden, dass Office-Produkte nicht für jeden beliebigen Einsatzzweck geeignet sind.

Für die Weitergabe von Dokumenten an Externe sollten bevorzugt Dateiformate verwendet werden, die weniger Restinformationen enthalten und mit denen die nachträgliche Änderungen bzw. auszugsweise Weiterverarbeitung erschwert werden kann. Hierfür können z. B. PDF-Dateien verwendet werden, die über die Sicherheitsoptionen der erstellenden Anwendung entsprechend eingeschränkt wurden.

Auch PDF-Dateien können Schadcode enthalten, der Sicherheitslücken ausnutzt. In PDF-Dateien lassen sich Funktionen wie Programmaufrufe einbetten, die ein Sicherheitsrisiko für die Dateien des lokalen IT-Systems darstellen. Häufig wird für solche Angriffe JavaScript verwendet. Vor allem ältere Versionen von PDF-Anwendungen sind für eine solche Infiltration anfällig. Häufig werden die Benutzer dafür auf eine manipulierte Webseite gelockt, wo dann eine präparierte PDF-Datei im Hintergrund geladen wird. Mit dem in der Datei versteckten Code wird Schadsoftware auf dem Rechner des Benutzers installiert. Dafür muss die Datei nicht einmal manuell geöffnet werden.

Antiviren-Programme erkennen infizierte PDF-Datei in vielen, aber nicht in allen Fällen, da die Angreifer den Schadcode ständig variieren. Umso wichtiger ist es, die eingesetzten Anwendungen regelmäßig auf Aktualität zu prüfen und Sicherheitsupdates schnell zu installieren.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Office-Produkte".

#### APP.1.1.M5 Auswahl geeigneter Office-Produkte

Die Funktionen der Office-Produkte sollten sich an den Bedürfnissen der Benutzer orientieren. Um dies zu gewährleisten, sollten die zukünftigen Benutzer der Office-Produkte in den Auswahlprozess in geeigneter Form eingebunden werden. So ist es beispielsweise sinnvoll, dass die Kriterien für die Auswahl der Office-Produkte gemeinsam von IT-Betrieb und Anwendern aufgestellt werden. Bei einer Neubeschaffung sollte hierfür vorab eine Marktanalyse durch die IT-Abteilung durchgeführt werden, um eine Vorauswahl zu definieren.

Auf Basis der Marktanalyse und der Erfahrungen der Benutzer sollte ein Anforderungskatalog erstellt werden, der die Auswahl der passenden Office-Produkte unter den verschiedenen Alternativen unterstützt. Die Anforderungen können hierbei in die beiden Klassen MUSS-Anforderungen und SOLL-Anforderungen gegliedert werden. MUSS-Anforderungen sind von dem zur Auswahl stehenden Office-Produkt zwingend zu erfüllen, um in die nähere Betrachtung zu kommen. SOLL-Anforderungen sind optional, dienen aber dazu, zwischen mehreren Office-Produkten in der näheren Auswahl zu entscheiden. SOLL-Anforderungen können zudem mit einem Gewichtungsfaktor versehen werden, um die Rangfolge der Anforderungen anzugeben. So können die Office-Produkte ausgewählt werden, die alle MUSS-Anforderungen erfüllen und die meisten Punkte in den SOLL-Anforderungen erzielen.

Die nachfolgende Tabelle zeigt eine beispielhafte Auswertung der Anforderungsanalyse.

In obigem Beispiel scheidet Office-Produkt 2 aus, da eine MUSS-Anforderung nicht erfüllt ist. Office-Produkt 1 und Office-Produkt 3 erfüllen alle MUSS-Anforderungen, wobei Office-Produkt 1 die meisten Zusatzpunkte aufgrund der SOLL-Anforderungen erhält.

Die am meisten verbreitete Anwendungen zur Arbeit mit PDF-Dateien sind Adobe Reader bzw. Adobe Acrobat. An Marktführern orientieren sich auch Schadsoftware-Entwickler. Daher kann es sinnvoll sein, weniger verbreitete PDF-Betrachter einzusetzen oder zumindest vorzuhalten, um bei akuten Warnmeldungen ausweichen zu können.

#### APP.1.1.M6 Testen neuer Versionen von Office-Produkten

Für einen geordneten Betriebsübergang von Office-Produkten und bei wesentlichen Änderungen ist ein geeignetes Vorgehen bei Test und Freigabe erforderlich. Die Tests dienen dazu, Probleme mit neuen Versionen von Office-Produkten frühzeitig zu erkennen. Für die Planung und Umsetzung von Tests sowie der darauf basierenden Freigabe sind üblicherweise die folgenden Ebenen zu berücksichtigen, bei denen jeweils andere Funktionsträger mit ihrer fachlichen Perspektive einzubeziehen sind:

* die fachliche Ebene (Vertreten durch Fachverantwortliche) 
* die Ebene des IT-Betriebs (Vertreten durch den IT-Leiter) 
* die Ebene der Informationssicherheit (Vertreten durch den Informationssicherheitsbeauftragten) 
Für alle genannten Ebenen sind Test- und Überprüfungsszenarien sowie Kriterien für die Freigabe zu entwickeln. Hierbei sollte Berücksichtigung finden:

* Auf der fachlichen Ebene muss geprüft werden, ob die neue Version des Office-Produkts mit den etablierten Arbeitsmitteln (wie Dateiformate, Standardvorlagen, Formulare und Auswertungsbögen) kompatibel ist. 
* Der IT-Betrieb sollte sicherstellen, dass neue Versionen der Office-Produkte in die IT-Infrastruktur und die IT-Betriebsabläufe integriert werden können. 
* Konzeption und Betrieb der Office-Produkte müssen konform mit dem Regelwerk (Leitlinien, Richtlinien), den Konzepten (z. B. Kryptokonzept) und den Best Practices zur Informationssicherheit sein. Es ist insbesondere darauf zu achten, dass die benötigten Sicherheitsfunktionen umgesetzt wurden und einwandfrei funktionieren. 
Vor der Durchführung von Tests sollte die Art und Weise der Ergebnissicherung und -auswertung festgelegt werden, insbesondere im Hinblick auf die Wiederholbarkeit von Prüfungen. Es muss geklärt werden, welche Daten während und nach der Prüfung festzuhalten sind.

Für die Tests der Office-Produkte sollten vor der Testdurchführung die Testfälle definiert werden. Dabei sollten die folgenden Kategorien berücksichtigt werden:

* Standardfälle sind Fälle, mit denen die korrekte Verarbeitung der definierten Funktionalitäten überprüft werden soll. 
* Fehlerfälle sind Fälle, in denen versucht wird, mögliche Fehlermeldungen der Office-Produkte zu provozieren. 
* Ausnahmefälle sind Fälle, bei denen die Office-Produkte ausnahmsweise anders reagieren müssen als bei Standardfällen. Es muss daher überprüft werden, ob das Programm diese Fälle als solche erkennt und korrekt bearbeitet. 
Auf der fachlichen Ebene können pro zu prüfendem Arbeitsmittel für jede Kategorie Testfälle definiert werden. Beispielsweise können für einen Auswertungsbogen als Standardfälle Eingabedaten und erwartete Auswertungsergebnisse vorab definiert werden.

Zur Testdurchführung sollte der IT-Betrieb eine geeignete Testumgebung zur Verfügung stellen. Die Umgebung sollte möglichst nahe an der Arbeitsumgebung sein, in der die Office-Produkte eingesetzt werden.

Die Durchführung der Tests muss anhand des Testplans erfolgen. Jede Aktion sowie die Testergebnisse müssen ausreichend dokumentiert und bewertet werden. Insbesondere wenn Fehler auftreten, sind diese derart zu dokumentieren, dass sie reproduziert werden können. Die für den späteren Produktionsbetrieb geeigneten Betriebsparameter müssen ermittelt und für die spätere Erstellung einer Installationsanweisung festgehalten werden.

Zeigt sich bei Bearbeitung einzelner Testinhalte, dass eine oder mehrere Anforderungen des Anforderungskataloges nicht konkret genug waren, sind diese gegebenenfalls zu konkretisieren.

Anhand der festgelegten Entscheidungskriterien sind die Testergebnisse zu bewerten, alle Ergebnisse zusammenzuführen und mit der Testdokumentation den Testverantwortlichen vorzulegen.

Nach Abschluss der Tests ist ein Pilotbetrieb der neuen Version der Office-Produkte sinnvoll, also ein Einsatz unter realen Bedingungen. Erfolgt der Pilotbetrieb in der Produktionsumgebung mit Echtdaten, muss vorab durch eine ausreichende Anzahl von Tests die korrekte und fehlerfreie Funktionsweise der Office-Produkte bestätigt worden sein, um die Integrität der Produktionsumgebung nicht zu gefährden. Dabei kann das Produkt beispielsweise bei ausgewählten Benutzern installiert werden, die es dann für einen gewissen Zeitraum im echten Produktionsbetrieb einsetzen.

Werden in der Testphase Inkompatibilitäten mit den Arbeitsmitteln der Institution erkannt, sollte entschieden werden, wie damit verfahren wird. Hierfür ist es sinnvoll, Fehlerklassen zu definieren, nach denen eingestuft werden kann, ob der Fehler den flächendeckenden Einsatz der neuen Version der Office-Produkte verhindert oder ob für eine Übergangsfrist die Inkompatibilitäten akzeptiert werden können. Für die Fehlerbehebung sollte definiert werden, welche Anpassungen an den Arbeitsmitteln für die neue Version der Office-Produkte erforderlich sind. Für die Umsetzung der Änderungen siehe Maßnahme APP.1.1.M10 Regelung der Software-Entwicklung durch Endbenutzer.

#### APP.1.1.M7 Installation und Konfiguration von Office-Produkten

Um eine standardisierte Installation der Office-Produkte zu gewährleisten, sollte eine Installations- und Konfigurationsanleitung erstellt werden, die auch die nötigen Schritte zur Anpassung der Konfiguration enthält. Die Office-Produkte sollten ausschließlich nach der dokumentierten Anleitung auf den dafür vorgesehenen IT-Systemen installiert und konfiguriert werden. Idealerweise erfolgt die Konfiguration über zentralisierte Verfahren.

Abweichungen von der Installationsanweisung und insbesondere der dort angegebenen Standardkonfiguration müssen in jedem Fall genehmigt und dokumentiert werden.

Wenn die Benutzer die Software selbst installieren sollen, sollte mindestens die Pilot-Installation durch einen ausgewählten typischen Benutzer durch die IT-Abteilung begleitet werden, um die Verständlichkeit der Installationsanweisung zu überprüfen. Anhand der Erkenntnisse aus der Pilot-Installation sowie weiterer Rückmeldungen der Benutzer sollte die Installationsanweisung aktualisiert und verbessert werden.

Sowohl vor als auch nach der Installation von Software sollte eine vollständige Datensicherung durchgeführt werden. Die erste Datensicherung kann bei nachfolgenden Problemen während der Installation zur Wiederherstellung eines konsolidierten Aufsetzpunktes verwendet werden. Nach der erfolgreichen Installation sollte erneut eine vollständige Datensicherung durchgeführt werden, damit bei späteren Problemen wieder auf den Zustand nach der erfolgreichen Installation des Produktes aufgesetzt werden kann.

Da Office-Produkte meist auf fast allen Arbeitsplätzen einer Institution installiert sind, empfiehlt es sich, die Konfiguration zentral zu verwalten. Hierfür existieren je nach eingesetztem Betriebssystem auf den Arbeitsplätzen mehrere Möglichkeiten:

* Im Windows-Umfeld kann die einheitliche Konfiguration der Office-Produkte in der Regel per Gruppenrichtlinien auf die Arbeitsplätze verteilt werden. 
* Im Mac OS- und Unix-Umfeld kann eine einheitliche Konfiguration mit Anwendungen zum Konfigurations-Management verwaltet werden. 
Die Standardkonfiguration der Office-Produkte sollte in regelmäßigen Abständen überprüft und bei Bedarf angepasst werden. Die angepasste Standardkonfiguration sollte anschließend auf den Arbeitsplätzen der Institution ausgerollt werden.

#### APP.1.1.M8 Versionskontrolle von Office-Produkten

Es sollte erfasst werden, welche Versionen von Office-Produkten in der Institution installiert sind und in welcher Konfiguration diese vorliegen. Werden verschiedene Versionen von Office-Produkten eingesetzt, kann es zu Kompatibilitätsproblemen beim Bearbeiten von Dokumenten kommen, und die Wartung und Pflege wird erschwert. Die Dokumentation der ausgerollten Versionen und Konfigurationen von Office-Produkten kann bei der schnellen Fehlerbehebung sehr hilfreich sein. Für die Übersicht der Konfigurationen kann eine Dokumentation der Standardkonfiguration erstellt werden (beispielsweise im Betriebs- oder Installationshandbuch der Office-Produkte). So müssen nur noch Abweichungen von der Standardkonfiguration gesondert dokumentiert werden. Bei jeder Änderung der Standardinstallation oder Standardkonfiguration sollte die Dokumentation angepasst werden. Wird eine Konfiguration eingespielt, die von der Standardkonfiguration abweicht, sollte die abweichende Konfiguration, der Grund dafür sowie der Arbeitsplatz dokumentiert werden, auf dem die abweichende Konfiguration vorhanden ist. 

Es sollten regelmäßige Kontrollen erfolgen, bei denen geprüft wird, ob die eingesetzten Versionen der offiziell freigegebenen Standardversion der Institution entsprechen.

Die konkrete Ausgestaltung der Bestandsführung und der Kontrollen richtet sich nach dem Umfang der Installationen und der Größe der Institution. So können für kleinere Organisationen mit wenigen Installationen von Office-Produkten einfache Listen ausreichten, die manuell in Stichproben gegen die tatsächlichen Installationen von Office-Produkten geprüft werden. In größeren Institutionen ist eine Bestandsführungssoftware sinnvoll, mit der es möglich ist, automatisierte Kontrollen der eingesetzten Versionen durchzuführen.

#### APP.1.1.M9 Beseitigung von Restinformationen vor Weitergabe von Dokumenten [Benutzer]

Office-Dokumente können in der Regel um eine Vielzahl an Meta-Informationen angereichert werden. Diese umfassen beispielsweise Angaben zum Autor, zur letzten Freigabe oder zur Version des Dokuments. Sie können aber auch schützenswerte Informationen enthalten. Bei der Veröffentlichung von Office-Dokumenten oder der Weitergabe an Dritte ist es daher erforderlich, nicht erwünschte Restinformationen zu entfernen.

Es sollte genau überlegt werden, welche Metadaten die Datei enthalten soll. Hier kann es beispielsweise erwünscht sein, einer Datei eine Vielzahl von Metadaten mitzugeben, damit diese über Suchmaschinen gefunden werden kann. Es kann aber auch sinnvoll sein, keine Metadaten weiterzugeben. Beispielsweise sollte der Name des Autors entfernt werden, wenn ein Dokument anonymisiert weitergegeben werden soll.

Hier ist es sinnvoll, den Benutzern eine Checkliste an die Hand zu geben, die ihnen ermöglicht, unerwünschte Restinformationen zu identifizieren und nach einem definierten Prozess zu löschen.

Beispielhafte Checkliste:

Viele Office-Produkte bieten Funktionen, mit denen die Prüfung auf Restinformationen weitestgehend automatisiert erfolgen kann oder in gewissem Umfang vor vorhandenen Restinformationen gewarnt wird. Für speziellere Überprüfungen kann auch auf Zusatzsoftware oder Eigenentwicklungen zurückgegriffen werden.

Beispielsweise können in LibreOffice Warnungen zu Restinformation in Dokumenten aktiviert werden. Die Einstellungen hierzu sind zu finden unter *Extras | Optionen | LibreOffice | Sicherheit | Sicherheitsoptionen und -warnungen*.

In Microsoft Office können Warnungen zu Restinformationen im Sicherheitscenter aktiviert werden. Optionen hierzu sind unter *Datei | Optionen | Sicherheitscenter | Einstellungen für das Sicherheitscenter* zu finden. Hier können Warnungen unter Datenschutzoptionen im Bereich Dokumentspezifische Einstellungen aktiviert werden. Außerdem stellt Microsoft Office eine Prüffunktion bereit. Diese kann unter *Datei | Informationen | Auf Probleme überprüfen | Dokument prüfen* durchgeführt werden. Bei der Prüffunktion werden bestimmte Restinformationen im Dokument automatisch geprüft und in einem Bericht angezeigt, der gleichzeitig Optionen zum Bereinigen bietet. Bei der Prüffunktion sollte definiert werden, welche Prüfungen sinnvoll sind und welche Bereinigungen durchgeführt werden können.

Häufig sollen in einem Dokument vor dessen Veröffentlichung zudem einzelne Passagen unkenntlich gemacht werden. Abhängig vom Dateiformat sind geeignete Methoden zu ergreifen. Eine beliebte, aber extrem fehlerträchtige Methode ist es, Textpassagen elektronisch zu "schwärzen". Die so übermalten Informationen sind allerdings in vielen Fällen einfach auslesbar. Daher ist dies unbedingt zu unterlassen.

Ein weiteres Beispiel für mögliche Restinformationen ist OLE (Object Linking And Embedding, Dienst zum Verknüpfen und Einbetten von Objekten). Über OLE-Funktionen können Objekte in Dateien eingebettet werden. Diese werden in vielen Office-Produkten benutzt, um Informationen anderen Programmen zur Verfügung zu stellen. Hierüber kann beispielsweise eine in Excel erstellte Tabelle in einem Word-Dokument eingebettet werden. Damit werden aber nicht nur die in dem Tabellenausschnitt dargestellte Informationen, sondern unter Umständen alle in der Excel-Datei enthaltenen Informationen in die Word-Datei übertragen. Wenn die Word-Datei dann weitergegeben wird, kann der Empfänger dann auch die Excel-Datei einsehen und sogar verändern, auch wenn diese durch ein Passwort lese- oder schreibgeschützt war. Um dies zu verhindern, sollte in diesem Beispiel die Tabelle als Text in die Word-Datei kopiert werden. Nur wenn die Ursprungs-Excel-Datei keine anderen Informationen enthält, als solche, die weitergegeben werden sollen, sollte sie in einer andere Datei eingebettet werden. Dies kann z. B. durch Anlegen einer neuen Excel-Datei erreicht werden.

Der Umgang mit Restinformationen in Office-Dokumenten sollte Teil der Anwenderschulungen sein. Insbesondere sollte der Umgang mit Software zur automatisierten Entfernung von Restinformationen geschult werden, falls diese eingesetzt wird. In Sensibilisierungskampagnen sollte zusätzlich auf die Gefahren durch Restinformationen hingewiesen werden.

#### APP.1.1.M10 Regelung der Software-Entwicklung durch Endbenutzer [Benutzer]

In Office-Dokumenten kann unter anderen mit Makros in Dokumenten oder Berechnungen und Zellenbezügen in Tabellenkalkulationen umfangreiche und komplexe Programmlogik implementiert werden. Dabei besteht die Gefahr, dass solche Office-Dokumente von Benutzern in Fachabteilungen als Werkzeuge immer weiterentwickelt werden, aber weder eine nachvollziehbare Dokumentation erstellt wird, noch Funktionstests durchgeführt werden. So werden eigenentwickelte Makros oder Programme auf Basis von Office-Anwendungen im schlimmsten Fall unerlässliche Werkzeuge in der Abteilung, können aber nicht mehr gewartet werden oder enthalten gar unentdeckte Fehler.

Um dies zu verhindern, sollte vom Management entschieden werden, in welchem Umfang solche Softwareentwicklungen durch die Endbenutzer in der Institution zulässig sind. Bei der Entscheidung sollte der Schutzbedarf der zu verarbeitenden Daten einbezogen werden. So kann es sinnvoll sein, ein Schutzbedarfslimit zu definieren, bis zu dem die Daten in Eigenentwicklungen verarbeitet werden können. Übersteigt der Schutzbedarf der Daten dieses Limit, sind Eigenentwicklungen in zentral durch den IT-Betrieb verwaltete Lösungen zu migrieren.

Werden Eigenentwicklungen grundsätzlich erlaubt, sollte definiert werden, wie diese zu dokumentieren und zu testen sind und welche Qualitätsanforderungen für Eigenentwicklungen in Form von Office-Dokumente bzw. Werkzeugen gelten. Hierfür ist es empfehlenswert, die Eigenentwicklungen je Abteilung in einem Katalog bzw. einer Liste zu erfassen und je Anwendung/Office-Werkzeug einen Verantwortlichen mit Vertreter zu benennen. Dieser Verantwortliche ist für die Einhaltung der Qualitätsanforderungen sowie Pflege, Dokumentation und Tests seiner Werkzeuge verantwortlich. Weitere Hinweise zu Tests von Office-Produkten finden sich in Maßnahme APP.1.1.M6 Testen neuer Versionen von Office-Produkten.

#### APP.1.1.M11 Geregelter Einsatz von Erweiterungen für Office-Produkte

Viele Office-Produkt können mit Erweiterungen an die Bedürfnisse der Institution angepasst werden. Diese Erweiterungen können nicht ohne die zugehörigen Office-Produkte verwendet werden, stellen aber aufgrund ihrer Komplexität eigene Softwareprodukte dar. Daher müssen eingesetzte Erweiterungen ebenso wie die Office-Produkte selbst in geregelter Form eingesetzt werden. Hierzu zählen:

* Geregelte Auswahl geeigneter Erweiterungen 
* Bezug der Erweiterungen aus offiziellen Quellen 
* Nach Möglichkeit Überprüfung der Prüfsummen bzw. der Signaturen der Erweiterungen bei der Installation 
* Patch-Management der Erweiterungen 
* Dokumentation der Konfiguration der Erweiterungen 
* Testen der Erweiterungen auf Kompatibilität mit den eingesetzten Versionen der Office-Produkte 
Besonderer Fokus liegt hierbei auf dem Testen der Erweiterungen auf Kompatibilität mit der eingesetzten Version. Hierbei ist zu beachten, dass sich die Entwicklungszyklen von Office-Produkten und deren Erweiterungen unterscheiden und so möglicherweise sehr viel häufiger neue Versionen der Erweiterungen erscheinen, als es neue Versionen der Office-Produkte gibt.

Die Tests der Erweiterungen sollten wie für die Office-Produkte selbst auf isolierten Testsystemen nach klar dokumentierten Testabläufen mit Ergebnisdokumentation durchgeführt werden. Hierbei sollten die Hinweise zum Testen der Software aus APP.1.1.M6 Testen neuer Versionen von Office-Produkten beachtet werden.

In Microsoft-Office besteht die Möglichkeit, nur signierte Erweiterungen (Add-Ins) von vertrauenswürdigen Herausgebern zu erlauben. Diese Funktion kann im Sicherheitscenter aktiviert werden. Zu finden ist die Funktion unter *Datei | Optionen | Sicherheitscenter | Einstellungen für das Sicherheitscenter… | Add-Ins*.

#### APP.1.1.M12 Verzicht auf Cloud-Speicherung [Benutzer]

In einigen Office-Produkten sind Funktionen integriert, die es ermöglichen, Dokumente direkt online zu speichern, zu synchronisieren und für Dritte freizugeben. Diese Funktionen können für den Privatanwender durchaus komfortabel sein, stellen im geschäftlichen Einsatz allerdings mehr Gefahr als Nutzen dar. So können beispielsweise schützenswerte Daten ungewollt veröffentlicht werden, wenn die Funktion unbedarft benutzt wird.

Alle Funktionen von Office-Produkten zur Cloud-Speicherung von Dokumenten sollten daher deaktiviert werden.

Der Bedarf für einen Austausch und eine gemeinsame Bearbeitung von Dokumenten sollte dabei nicht komplett ignoriert werden. Dies führt meist dazu, dass die Benutzer sich selbst helfen und nicht freigegebene Software oder unerlaubte Cloud-Lösungen nutzen. Daher sollten die Benutzer in Schulungen auf die in der Institution erlaubten Möglichkeiten zum Backup von Dokumenten, zum Datenaustausch mit Externen und zur Nutzung von Cloud-Diensten hingewiesen werden. Um Dokumente für Dritte zur Sichtung oder Bearbeitung freizugeben, sollten beispielsweise geeignete Kollaborationsplattformen eingesetzt werden, die über Sicherheitsfunktionen wie eine verschlüsselte Datenablage und -versendung und ein geeignetes System zur Benutzer- und Rechteverwaltung verfügen. 

In Microsoft Office 2013 ist die Cloud-Speicher-Option SkyDrive integriert. Um diese zu deaktivieren, sollte bei der Installation darauf geachtet werden, dass die Komponente „Microsoft SkyDrive Pro“ in den Installationsoptionen deaktiviert ist. Zusätzlich sollten unter *Datei | Optionen | Speichern* die Punkte *„Backstage beim Öffnen oder Speichern von Dateien nicht anzeigen“* und „*Standardmäßig auf Computer speichern“* markiert werden. Der Punkt *„Zusätzliche Speicherorte anzeigen, auch wenn eine Anmeldung erforderlich ist“* sollte deaktiviert werden. Die Cloud-Speicherung kann auch über eine Gruppenrichtlinie deaktiviert werden. Dazu ist die Option „*Show SkyDrive Sign In*“ in *User Configuration | Administrative Templates | Microsoft Office 2013 | Miscellaneous* auf „*Disabled*“ zu setzen.

#### APP.1.1.M13 Verwendung von Viewer-Funktionen [Benutzer]

Dokumente aus potentiell unsicheren Quellen, wie dem Internet oder E-Mails, können Schadsoftware enthalten, die beim Öffnen ausgeführt wird. Dies können sowohl Makros sein, als auch Code der Schwachstellen der eingesetzten Office-Produkt-Versionen ausnutzt. Um diese Gefahr zu reduzieren, sollten Viewer eingesetzt werden.

Das können einerseits gesonderte Anwendungen sein, die speziell für den Zweck entwickelt wurden, Office-Dokumente ausschließlich anzuzeigen. Viele Office-Produkte beinhalten aber auch einen sogenannten geschützten Modus, bei dem nur ein geringer Teil der Funktionen des Office-Produkts aktiviert ist.

Je nach Einsatzbereich und Schutzbedarfsanforderungen sollte abgewogen werden, welche Alternative zweckmäßig ist. In Bereichen mit erhöhten Sicherheitsanforderungen ist es stets empfehlenswert, gesonderte Viewer-Anwendungen einzusetzen.

Microsoft bietet beispielsweise für Word, Excel, PowerPoint und Visio dedizierte Viewer-Programme im Download Center zum Herunterladen an.

Die Einstellungen für den integrierten geschützten Modus kann bei Microsoft Office unter *Datei | Optionen | Sicherheitscenter | Einstellungen für das Sicherheitscenter… | Geschützte Ansicht* verwaltet werden. Die Einstellungen sollten möglichst zentral per GPO gesteuert werden. Microsoft stellt hierfür für jede Microsoft Office Version Administrative Vorlagendateien für Gruppenrichtlinien zur Verfügung.

Im Adobe Reader ab Version Zehn (Adobe Reader X) ist eine Sandbox (oder "Geschützter Modus") integriert, um Angriffen entgegen zu wirken. Daher sollten Anwender, die zur Betrachtung und Bearbeitung von PDF-Dokumenten Adobe Reader nutzen, Adobe Reader X oder neuer einsetzen und den "Geschützten Modus" nutzen.

#### APP.1.1.M14 Schutz gegen nachträgliche Veränderungen von Informationen [Benutzer]

Viele Anwendungsprogramme bieten Sicherheitsmechanismen an, um den weiteren Umgang mit den erstellten Dateien einzuschränken. Da die Sicherheitsmechanismen der verschiedenen Anwendungsprogramme sehr unterschiedlich ausgeprägt sind und teilweise sogar von Version zu Version variieren, ist es wichtig, die Mitarbeiter darüber zu informieren, wie diese zu benutzen sind und welche Schritte vor der Weitergabe von elektronischen Dokumenten zu beachten sind. Es ist häufig sinnvoll, einen Mitarbeiter (plus Vertreter) gründlich hierzu auszubilden. Dieser sollte dann alle weiterzugebenden Dokumente entsprechend der Sicherheitsvorgaben bearbeiten oder als Ansprechpartner zur Verfügung stehen.

Im Folgenden werden einige solcher Sicherheitsmechanismen am Beispiel von PDF-Dateien vorgestellt. 

 **Schutz von PDF-Dokumenten** 

Mit Adobe Acrobat, also der verbreitetsten Anwendung, mit der PDF-Dateien erstellt und nachbearbeitet werden können, ist die Vergabe von zwei Arten von Passwörtern möglich. Die einen werden zum Öffnen des Dokuments, die anderen zum Ändern der Sicherheitsattribute benötigt. Bei der Vergabe eines Passwortes wird zunächst danach gefragt, zu welchen Programmversionen die Schutzfunktion kompatibel sein soll. Bis zur Version "Adobe 5.0 und höher" ist dabei nur eine 40-Bit-Verschlüsselung mit RC4 möglich, ab "Adobe 5.0 und höher" ist eine 128-Bit-Verschlüsselung mit RC4 und ab "Adobe 7.0 und höher" ist eine 128-Bit-Verschlüsselung mit AES vorgesehen. Es sollte darauf geachtet werden, mindestens mit 128 Bit zu verschlüsseln, da der Dokumentenschutz sonst einfach ausgehebelt werden kann.

Über die Sicherheitsattribute können unter anderem folgende Funktionen eingeschränkt werden:

* Öffnen des Dokuments 
* Drucken 
* Ändern des Dokuments 
* Kopieren von Texten, Bildern oder anderen Inhalte 
* Zugriff auf Metadaten eines Dokuments 
* Notizen und Formularfelder hinzufügen oder ändern 
So können sehr einfach die Rechte beschränkt werden, so dass niemand mit Cut and Paste die Inhalte einer Veröffentlichung übernehmen kann. Wenn im Extremfall sogar das Ausdrucken verhindert wird, kann die Datei nur online gelesen werden.

Leider bietet dies nur einen rudimentären Schutz, da PDF-Dateien (abhängig von der Programmversion, mit der sie erstellt wurden) auch mit Programmen geöffnet werden können, die diese Sicherheitsattribute ignorieren. Solange z. B. Drucken erlaubt wird, kann das Dokument sogar jederzeit wieder in eine PDF-Datei ohne jegliche Einschränkungen verwandelt werden.

Es können PDF-Sicherheitsrichtlinien erstellt werden. Diese kann jeder Benutzer für sich erstellen oder es können von der Institution vorgegebene Sicherheitsrichtlinien verwendet werden, hierfür ist ein Adobe Policy Server erforderlich.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.1.1.M15 Einsatz von Verschlüsselung und Digitalen Signaturen(CI)

Bei erhöhten Anforderungen an die Authentizität, Integrität und Vertraulichkeit von Office-Dokumenten sollten Digitale Signaturen eingesetzt werden, um die Authentizität und Integrität sicherzustellen. Zudem sollten die Dokumente verschlüsselt werden, um die Vertraulichkeit zu gewährleisten. Entscheidend für die Sicherheit der Signatur- und Verschlüsselungsverfahrens ist die Güte des verwendeten Algorithmus und die Schlüsselauswahl. 

 **Hohe Integritätsanforderungen:** 

Bestehen hohe Anforderungen an die Integrität der Office-Dokumente, beispielsweise um die Nicht-Abstreitbarkeit zu gewährleisten, können digitale Signaturen eingesetzt werden. Beim Einsatz von digitalen Signaturen, die in die Office-Dokumente eingebettet werden, sollte beachtet werden, dass die eingesetzte Methode zum Kryptokonzept (siehe Baustein CON.1 Kryptokonzept) der Institution passt. Es kann erforderlich sein, das Kryptokonzept um die Methode zum Signieren der Office-Dokumente zu erweitern. In der Regel muss eine institutionsweite Schlüsselverwaltung etabliert sein, um die Signaturfunktionen sinnvoll zu nutzen. Falls zudem Benutzer außerhalb der Institution mit den signierten Dokumenten arbeiten, muss außerdem beachtet werden, dass die eingesetzte Lösung einen etablierten Standard implementiert, der auch von weiteren Institutionen problemlos genutzt werden kann.

In Microsoft Office können Dokumente mit einer integrierten Funktion signiert werden. Diese ist zu finden unter *Datei | Informationen | Dokument schützen | Digitale Signatur* hinzufügen. Damit wird dem Dokument eine Digitale Signatur zugewiesen, die beim Öffnen in Microsoft Office geprüft werden kann. Zusätzlich ist es möglich, ein im Dokument sichtbares Signaturfeld einzufügen. Das ist über *Einfügen | Signaturzeile* möglich. Um das Dokument zu signieren, muss der Unterzeichner seine Signatur über Rechtsklick auf die jeweilige Signaturzeile im Kontextmenü im Punkt *„Signieren...“ *einfügen. 

In LibreOffice ist es ebenfalls möglich, ein Dokument digital zu signieren. Hier findet sich die Funktion unter *Datei | Digitale Signaturen*. Die Digitalen Signaturen werden nach der XML Signature Spezifikation erzeugt und in die LibreOffice Dokumente eingebettet.

 **Hohe Vertraulichkeitsanforderungen:** 

Office-Dokumente mit hohen Anforderungen an die Vertraulichkeit sollten bei der Übertragung verschlüsselt werden. Teilweise bieten Office-Produkte integrierte Funktionen zur Verschlüsselung von Dokumenten. Integrierte Verschlüsselungsfunktionen von Office-Produkten sollten allerdings nicht ohne vorherige Analyse eingesetzt werden. So sollte sicherstellt werden, dass die angebotene Verschlüsselungsfunktion auch die Anforderungen der Institution erfüllt (siehe Baustein CON.1 Kryptokonzept). Es muss bereits in der Planung darauf geachtet werden, dass Algorithmen und Verfahren eingesetzt werden, die aktuell dem Stand der Technik entsprechen, auch noch auf absehbare Zeit einen angemessenen Schutz bieten können. Zudem ist zu beachten, dass je nach eingesetzten Office-Produkten Meta-Informationen nicht mit verschlüsselt werden. Falls die integrierten Verschlüsselungsfunktionen der Office-Produkte den Ansprüchen der Institution nicht genügen, sollten alternative Möglichkeiten eingesetzt werden.

Microsoft-Office Dokumente können über die Funktion *Datei | Informationen | Dokument schützen | Mit Kennwort verschlüsseln* verschlüsselt werden. Microsoft Office setzt seit Version 2007 AES mit einer Schlüssellänge von 128 Bit im CBC-Modus ein. Versionen vor Microsoft Office 2007 setzen standardmäßig schwächere Algorithmen mit kürzeren Schlüssellängen ein. Die integrierte Verschlüsselungsfunktion dieser Versionen sollte daher nicht genutzt werden.

LibreOffice-Dokumente können über die Funktion *Datei | Eigenschaften | Sicherheit | Schützen* verschlüsselt werden. Alternativ kann der Haken bei der Option „Mit Kennwort speichern“ im Speichern-Dialogfenster gesetzt werden. LibreOffice setzt in der aktuellen Version standardmäßig AES mit einer Schlüssellänge von 256 Bit im CBC-Modus ein. In früheren Versionen wurden ebenfalls Blowfish sowie AES mit Schlüssellängen von 128 und 192 Bit eingesetzt.

#### APP.1.1.M16 Integritätsprüfung von Dokumenten(I)

Dokumente, für die hohe Anforderungen an die Integrität bestehen, sollten bei der Übertragung mittels Prüfsummen (beispielsweise CRC, MD5 Hash oder SHA Hash) oder digitalen Signaturen (siehe Maßnahme APP.5.2.M15 Einsatz von Verschlüsselung und Digitalen Signaturen) abgesichert werden. Wichtig zu beachten ist dabei, dass nur digitale Signaturen zuverlässig absichtliche Veränderungen erkennen lassen. 

Für unbeabsichtigte Änderungen (Bitfehler etc.) stellen viele Office-Produkte automatisierte Reparaturfunktion zur Verfügung, mit denen defekte Office-Dokumente teilweise wiederhergestellt werden können. Hierbei ist zu beachten, dass die Möglichkeit Dokumente wiederherzustellen, abhängig vom Dateiformat des Office-Dokuments ist. So besteht für Office-Dokumente, die im Office Open XML Format (ab Office 2007) gespeichert wurden, eine größere Wahrscheinlichkeit zur Wiederherstellung nach Integritätsverlusten. 

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

**Lizenzverwaltung**  
 Auf allen IT-Systemen der Institution müssen korrekt lizenzierte Office-Produkte eingesetzt werden. Daher sollten die Lizenzen der Installationen regelmäßig kontrolliert werden. Es ist sinnvoll, die Bestandsführung der Software-Lizenzen im Rahmen der Versionskontrolle vorzunehmen.

Werden Office-Produkte ohne gültige Lizenz eingesetzt, kann das im schlimmsten Fall Strafzahlungen und Kosten für die Nachlizenzierung zur Folge haben. Daher muss eine Übersicht erstellt werden, aus der ersichtlich ist, wie viele Lizenzen für die eingesetzten Office-Produkte vorhanden sind und wie viele Lizenzen bereits verbraucht wurden. Diese Übersicht hilft ebenfalls bei der Planung für künftig benötigte Lizenzen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Office-Produkte" finden sich unter anderem in folgenden Veröffentlichungen:

*  

 #### [CS004] Einsatz und Konfiguration des Adobe Readers X und XI

  

 Allianz für Cyber-Sicherheit, BSI-CS 004, Version 1.10, 10.2014  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_004.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_004.html)

  

 
*  

 #### [KB2501584] Microsoft-Sicherheitsempfehlung

  

 Microsoft Office-Dateiüberprüfung für Office 2003, 2007 Office und Office 2010, 04.2011  
 <https://support.microsoft.com/de-de/kb/2501584>

  

 
*  

 #### [LODS] Digitale Signaturen anwenden

  

 LibreOffice, (zuletzt abgerufen am 05.10.2017)  
 [https://help.libreoffice.org/Common/Applying\_Digital\_Signatures/de](https://help.libreoffice.org/Common/Applying_Digital_Signatures/de)

  

 
*  

 #### [LORP] Libre Office Release Plan

  

 The Document Foundation, (zuletzt abgerufen am 05.10.2017)  
 <https://wiki.documentfoundation.org/ReleasePlan>

  

 
*  

 #### [MS35554] Office 2013 Administrative Template files (ADMX/ADML) and Office Customization Tool

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=35554>

  

 
*  

 #### [MS49030] Office 2016 Administrative Template files (ADMX/ADML) and Office Customization Tool

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=49030>

  

 
*  

 #### [MSD10] Excel Viewer

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=10>

  

 
*  

 #### [MSD13] PowerPoint Viewer

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=13>

  

 
*  

 #### [MSD35811] Visio Viewer

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=35811>

  

 
*  

 #### [MSD4] Word Viewer

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/en-us/download/details.aspx?id=4>

  

 
*  

 #### [MSDN338205] Introducing the Office (2007) Open XML File Formats

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://msdn.microsoft.com/en-us/library/aa338205.aspx>

  

 
*  

 #### [MSDN368289] Digital Signatures and Windows Installer

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://msdn.microsoft.com/en-us/library/windows/desktop/aa368289.aspx>

  

 
*  

 #### [MSDN380259] Cryptography Tools

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://msdn.microsoft.com/en-us/library/aa380259.aspx>

  

 
*  

 #### [MSDN387764] SignTool

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://msdn.microsoft.com/en-us/library/aa387764.aspx>

  

 
*  

 #### [MSFSD] Office 2013 - can I disable the "SkyDrive" save option under Word

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 [http://answers.microsoft.com/en-us/office/forum/office\_2013\_release-word/office-2013-can-i-disable-the-skydrive-save-option/e358c2e0-0c10-4251-b1b5-aabe59407ed7](http://answers.microsoft.com/en-us/office/forum/office_2013_release-word/office-2013-can-i-disable-the-skydrive-save-option/e358c2e0-0c10-4251-b1b5-aabe59407ed7)

  

 
*  

 #### [MSODS] Hinzufügen oder Entfernen einer digitalen Signatur in Office-Dateien

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://support.office.com/de-de/article/Hinzuf%C3%BCgen-oder-Entfernen-einer-digitalen-Signatur-in-Office-Dateien-70d26dc9-be10-46f1-8efa-719c8b3f1a2d>

  

 
*  

 #### [MSS2488] Microsoft Support Lifecycle Office 2003

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://support.microsoft.com/de-de/lifecycle?p1=2488>

  

 
*  

 #### [MSS8753] Microsoft Support Lifecycle Office 2007

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://support.microsoft.com/de-de/lifecycle?p1=8753>

  

 
*  

 #### [TN179125] Plan cryptography and encryption settings for Office 2013

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://technet.microsoft.com/de-de/library/cc179125.aspx>

  

 
*  

 #### [TN194021] Guide to Office 2013 Security

  

 Microsoft, (zuletzt abgerufen am 05.10.2017)  
 <https://technet.microsoft.com/en-us/library/dn194021.aspx>

  

 
*  

 #### [TN797428] File format reference for Word 2013, PowerPoint 2013, and Excel 2013

  

 Microsoft Technet, (zuletzt abgerufen am 05.10.2017)  
 <https://technet.microsoft.com/de-de/library/dd797428.aspx>

  

 
*  

 #### [TN857087] Plan Protected View Settings for Office 2013

  

 Microsoft Technet, (zuletzt abgerufen am 05.10.2017)  
 <https://technet.microsoft.com/en-us/library/ee857087.aspx>

  

 
*  

 #### [XMLDSIG] XML Signature Syntax and Processing (Second Edition)

  

 W3C, (zuletzt abgerufen am 05.10.2017)  
 <https://www.w3.org/TR/xmldsig-core/>

  

 
