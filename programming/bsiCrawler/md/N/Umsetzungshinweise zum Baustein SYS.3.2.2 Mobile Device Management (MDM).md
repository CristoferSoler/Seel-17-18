1 Beschreibung
--------------

### 1.1 Einleitung

In einer ständig stärker digitalisierten Arbeitsumgebung stellen Institutionen ergänzend oder sogar ablösend zum Notebook ihren Mitarbeitern durch mobile Endgeräte (Mobile Devices) weitergehende Möglichkeiten zum mobilen Arbeiten zur Verfügung. Damit einher geht meist, dass die Mitarbeiter sich auch von unterwegs permanenten Zugriff auf interne und externe Informationsquellen wünschen und die Geräte auch zur Entspannung und Weiterbildung benutzen wollen.

Ob sich eine Institution mit den Chancen und Risiken mobiler Endgeräte auseinandersetzen möchte, ist heutzutage nicht mehr relevant. Denn mit hoher Priorität muss die Frage beantwortet werden, ob diese Auseinandersetzung nicht schon erfolgt ist oder wann das geschieht. Sollte sich eine Institution grundsätzlich gegen mobile Endgeräte entscheiden, so sind zumindest die Risiken zu beachten, die durch Verwendung von und Interaktion mit privaten Geräten entstehen könnten.

Mobile Endgeräte sind in Beschaffung, Betrieb und Benutzung grundlegend anders als ein Arbeitsplatz-PC oder Server. Um solche Geräte sicher betreiben zu können, ist es unumgänglich diese Unterschiede zu verstehen und dieses Verständnis in die Entscheidungen über Prozesse und Verfahren mit einfließen zu lassen.

So können beispielsweise Arbeitsplatz-PCs und Server gekauft und danach mit einem beliebigen Betriebssystem ausgestattet werden. Die Administratoren können somit die Geräte vollständig anpassen. Das ist bei mobilen Endgeräten anders. Hier wird die Hardware zusammen mit einem Betriebssystem erworben, und bis auf wenige Ausnahmen funktioniert nur das vom Hersteller gelieferte Betriebssystem auf diesen Geräten. Somit kann die Institution die mobilen Endgeräte nicht wie gewohnt kontrollieren. Selbst wenn ein Mobile-Device-Management-(MDM)-System eingesetzt wird, hat letztlich immer auch der Hersteller eine gewisse Kontrolle über das Gerät, da er das Betriebssystem kontrolliert.

Ebenfalls neu für die Betriebsprozesse ist, dass nicht mehr der Anwender allein über die Durchführung von Updates bestimmen kann, da der Hersteller des Geräts diesen Prozess kontrolliert. Bei Android-basierten Geräten ist häufig auch der Mobilfunkanbieter in diesen Prozess eingebunden, da er die Updates des Herstellers oft noch anpasst und erst danach an seine Kunden weitergibt.

Der Mobilfunkanbieter ist für den Betrieb der mobilen Endgeräte ein wichtiger Partner. Er kontrolliert nicht nur die Datenverbindung zu den Geräten, sondern je nach Vertrag oder Endgerät konfiguriert er sie auch. Jedes mobile Endgerät mit einer SIM-Karte ist somit durch den Mobilfunkanbieter potenziell ferngesteuert.

Für die Abbildung der unterschiedlichen Umsetzungsempfehlungen wird in diesem Dokument auf die folgenden drei fiktiven Szenarien zurückgegriffen.

**1. Szenario**

* Die Benutzer telefonieren hauptsächlich mit ihren Geräten und versenden E-Mails.
* Die Benutzer können nicht auf interne Kollaborations- und Dokumentenmanagementsysteme zugreifen.
* Die Informationen sind nicht als vertraulich klassifiziert.
**2. Szenario** 

* Die Benutzer telefonieren mit ihren Geräten, versenden E-Mails und bearbeiten geschäftliche Dokumente.
* Die Benutzer können auf interne Kollaborations- und Dokumentenmanagementsysteme zugreifen.
* Teilweise sind die Informationen als vertraulich klassifiziert.
**3. Szenario**

* Die Benutzer telefonieren mit ihren Geräten, versenden E-Mails und bearbeiten geschäftliche Dokumente.
* Die Benutzer können auf interne Kollaborations- und Dokumentenmanagementsysteme, Finanzdaten oder kritische Systeme der Institution zugreifen.
* Teilweise sind die Informationen als streng vertraulich klassifiziert.
### 1.2 Lebenszyklus

**Planung und Konzeption**

In der Planungs- und Konzeptionsphase sollen alle eventuellen Nutzungsszenarien, z. B. Einbindung in eine Kollaborations-Lösung, Zugriff auf Warenwirtschaftssysteme sowie der maximal umzusetzende Schutzbedarf, in die Auswahl der zentralen Managementlösung einfließen (siehe SYS.3.2.2.M1 Festlegung einer Strategie für das Mobile Device Management). Müssen private und geschäftliche Bereiche strikt getrennt werden, empfiehlt es sich gegenüberzustellen, ob dies mittels Betriebssystemmechanismen wie Managed Apps und Managed Open-in, durch eine Containerlösung oder auch durch virtualisierte Benutzerumgebungen erreichbar ist. Ebenso sollte in dieser Phase überprüft werden, wie die mobilen Endgeräte benutzerbezogen in die Informations- und Kommunikationsinfrastruktur integriert werden können. Aus den Ergebnissen lassen sich neue Anforderungen an die bisherigen Netzsegmentierungen, die Sicherheitsgateway-Infrastrukturen und deren Funktionen ableiten.

In der Planungs- und Konzeptionsphase muss die Institution entscheiden, welches Betriebsmodell oder welche Kombination aus den beiden Modellen realisiert werden soll: *an die Mitarbeiter ausgegebene Geräte* oder *Bring Your Own Device (BYOD). *Auf dieser Grundlage werden die Sicherheitsvorgaben für mobile Endgeräte technisch und organisatorisch umgesetzt.

Eine weitere sehr wichtige Frage ist, inwieweit die Benutzer eigene Apps auf ihrem mobilen Endgerät installieren dürfen oder müssen, ob die Mitarbeiter selbst zusätzliche Apps für die private Nutzung hinzufügen dürfen und ob sie einen Teil der Administration selbst übernehmen.

Auf Basis des Schutzbedarfes der Informationen (vergleiche auch die drei fiktiven Szenarien) und den Möglichkeiten des IT-Betriebs sollte eine MDM-Lösung gewählt werden (siehe SYS.3.2.2.M3 Auswahl eines MDM-Produkts), die sicherstellt, dass die Daten der Institution gemäß den intern dokumentierten Vorgaben gesichert sind.

Das Betriebsmodell der zukünftigen MDM-Lösung ist abhängig vom Schutzbedarf der mobilen Geräte auszuwählen. Ein eigener Betrieb, bei dem die Server der MDM-Lösung in den eigenen Räumlichkeiten aufgestellt sind und somit inklusive der enthaltenen Daten unter der eigenen Kontrolle der Institution stehen, ist bei allen Lösungen möglich. Fast alle MDM-Anbieter bieten ihre Lösungen auch als Cloud-Variante an, bei der die Software auf den Servern des jeweiligen Anbieters betrieben wird und der Kunde einen Webzugang erhält, mit dem er die Anwendungen und verknüpften mobilen Endgeräte verwalten kann.

**Beschaffung**

Bei der Beschaffung einer MDM-Lösung sowie bei der Auswahl von mobilen Endgeräten und des Mobilfunkproviders sollten neben den wirtschaftlichen Gesichtspunkten auch sicherheitstechnische Aspekte einfließen. Hier ist vieles möglich, beispielsweise ein Full-Service-Angebot mit einem Mobilfunkanbieter, das Geräte, Mobilfunkvertrag und Mobile Device Management umfasst, oder der schlichte Kauf der Geräte und ein vollständig selbst administrierter Betrieb.

Die Angebote der Mobilfunkanbieter sind für die Sicherheit der Geräte insofern interessant, als es hier möglich ist, die Geräte in einer geschlossenen Benutzergruppe zu betreiben. Die mobilen Endgeräte erhalten dann über Mobilfunk keinen regulären Internetzugriff, sondern werden vom Mobilfunkanbieter in einem Netz zusammengefasst, in dem nur die Geräte der Institution sind.

Sofern Mitarbeiter mobile Endgeräte von der Institution erhalten, sollten diese zentral beschafft werden und interne Sicherheitsvorgaben ausreichend erfüllen.

**Umsetzung**

Je nachdem was im Konzept festgelegt ist, muss den Mitarbeitern ein Self-Service-Kiosk zur selbständigen Einrichtung der Endgeräte zugänglich sein, oder die Administratoren der Institution konfigurieren die mobilen Endgeräte vollständig für die Mitarbeiter.

In Kapitel 2 werden Maßnahmenempfehlungen anhand der drei einleitend definierten Szenarien aufgezeigt. Unabhängig davon, mit welcher Methode die Konfigurationsprofile auf die verwalteten Endgeräte ausgerollt werden, muss sichergestellt sein, dass die Benutzer nicht ohne Autorisierung die Absicherungsprofile löschen können.

**Betrieb**

Damit mobile Endgeräte ordnungsgemäß und zuverlässig benutzt werden können, muss die eingesetzte MDM-Lösung technische Sicherheitsvorgaben an die Geräte übergeben (siehe SYS.3.2.2.M4 Verteilung der Grundkonfiguration auf mobile Endgeräte). Die wichtigsten Aufgaben für die Verantwortlichen sind regelmäßige sicherheitsrelevante Wartungsmaßnahmen durchzuführen sowie Benutzerkonten und Berechtigungen sicher zu administrieren. Zusätzlich sollten die Systeme der MDM-Lösung gezielt überwacht werden, um Verfügbarkeitsprobleme und Sicherheitsvorfälle schnell erkennen zu können.

Wie für alle IT-Systeme ist auch für die Server der MDM-Lösung ein funktionierendes Änderungsmanagement ein zentrales Element, um die Systemsicherheit zu erhalten.

**Aussonderung**

Die MDM-Lösung darf nicht ohne vorherige Ankündigung abgeschaltet werden. Wenn sie außer Betrieb genommen werden soll, müssen die betroffenen Benutzer rechtzeitig informiert werden.

Bei der Aussonderung des Servers der MDM-Lösung ist außerdem darauf zu achten, dass keine schützenswerten Informationen mehr auf den Festplatten vorhanden sind. Dazu genügt es nicht, die Festplatten einfach neu zu formatieren, sondern sie müssen mindestens einmal vollständig überschrieben werden. Bei Flashspeichern können die internen Speicherblöcke bauartbedingt nicht direkt adressiert werden. Das bedeutet, um die Daten zu löschen, müssen die zurücksetzenden Funktionen des Controllers genutzt werden. Sollten auf dem Server der MDM-Lösung Informationen mit hohem Schutzbedarf verarbeitet oder gespeichert worden sein, ist wahrscheinlich die Zerstörung des Flashspeichers nach DIN 66399 "Vernichten von Datenträgern" die sichere Methode.

Die Aussonderung eines Servers oder der kompletten MDM-Lösung muss dokumentiert werden. Bestandsverzeichnisse und Netzpläne sind zu aktualisieren. Sofern sich durch die Aussonderung der Informationsverbund strukturell ändert, sollte auch das Sicherheitskonzept entsprechend angepasst werden.

**Notfallvorsorge**

Wie für alle anderen zentralen IT-Systeme muss auch für eine MDM-Lösung eine geeignete Notfallplanung erstellt werden. Ein zentrales Element der Notfallvorsorge ist die Datensicherung, die auch relevante Bereiche des Betriebssystems und Sicherheitsmanagements einbeziehen sollte. Bei erhöhten Anforderungen an die Verfügbarkeit der MDM-Lösung kann zusätzlich über Redundanzen vorgesorgt werden. 

Im Zuge der Notfallvorsorge sollten bei einer Cloud-Lösung mit den Vertragspartnern entsprechende Vereinbarungen hinsichtlich der eingesetzten MDM-Lösung getroffen werden.

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Mobile Device Management (MDM)" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### SYS.3.2.2.M1 Festlegung einer Strategie für das Mobile Device Management

Grundlage aller weiteren Schritte ist die Definition einer Strategie, die anhand der zu verarbeitenden Informationen und deren Schutzbedarf festlegt, wie Mitarbeiter mobile Endgeräte benutzen dürfen und wie die Geräte in die internen Strukturen der Institution integriert sind. Eine solche Strategie sollte mindestens die folgenden Punkte beinhalten. 

**Darf das MDM als Cloud-Dienst betrieben werden?**

Wenn Cloud-Dienste eingesetzt werden, sind immer dann rechtliche Aspekte zu beachten, wenn personenbezogene Daten im Sinne des Bundesdatenschutzgesetzes (BDSG, § 3 Absatz 1) übergeben werden. Eine solche Auftragsdatenverarbeitung ist, abhängig vom tatsächlichen Speicherort der Daten, nur unter bestimmten Voraussetzungen möglich (§ 11 BDSG) und zudem an einen schriftlichen Auftrag gebunden. Halten sich Institutionen nicht daran, verstoßen sie gegen bestehendes Recht. Dadurch schädigen sie nicht nur ihren Ruf, sondern können sich auch Schadenersatzansprüchen oder Bußgeldern gegenübersehen.

Sind die datenschutzrechtlichen Anforderungen durch den Dienstleister und die Institution erfüllbar, sollte geprüft werden, ob bei einer Cloud-Lösung auch die internen betriebswirtschaftlichen und sicherheitsrelevanten Anforderungen erfüllt werden können. Hierbei ist u. a. der Standort des MDM-Anbieters zu berücksichtigen.

**Soll das MDM durch die Institution selbst betrieben werden?**

Um diese Frage beantworten zu können, empfiehlt es sich im ersten Schritt, über die wirtschaftlichen, sicherheitstechnischen und datenschutzrechtlichen Anforderungen den eigenen Bedarf zu ermitteln. Ebenfalls mit hoher Priorität muss die Frage beantwortet werden, wie kritisch es für die Institution ist, wenn das MDM teilweise oder komplett ausfällt. Wäre ein solcher Notfall beherrschbar? Können Sicherheitsvorfälle erkannt und kann ihnen professionell begegnet werden?

Im nächsten Schritt sollte entschieden werden, ob ein interner Verzeichnisdienst integriert werden soll und welche Anforderungen erfüllt sein müssen.

**Welche Compliance-Anforderungen müssen durchgesetzt werden?**

Sollen Verstöße gegen interne Regelungen der Institution erkannt und dagegen automatisiert Aktionen ausgeführt werden, müssen Compliance-Anforderungen auf den mobilen Endgeräten der Institution durchgesetzt werden. Die Reaktion auf Compliance-Verstöße kann unterschiedlich ausfallen, da diese abhängig vom Schutzbedarf der Informationen und der Implementierungsvariante (*Geräte der Institution* oder *BYOD*) ist. Wurde der Bedarf ermittelt, sollte in der Strategie eine entsprechende technische Umsetzung, mit der Compliance-Anforderungen eingehalten werden, für die Beschaffung und Konzeption formuliert werden.

**Welche mobilen Geräte und welche Betriebssysteme muss das MDM unterstützen?**

Um eine hohe Produktivität zu erzielen und den sicherheitsbewussten Umgang der Benutzer zu unterstützen, empfiehlt es sich, auf die bereits vorhandenen Erfahrungen der Mitarbeiter mit mobilen Endgeräten der Institution zurückzugreifen. Die folgenden Fragen sollen die Verantwortlichen dabei unterstützen, den Bedarf für die Strategie festzulegen: 

* Sollen die Benutzer von mobilen Endgeräten mit dem bevorzugten Gerät auf Informationen der Institution zugreifen können? Soll das unabhängig davon erfolgen können, unter welchem Betriebssystem es betrieben wird?
* Sollen die Benutzer im eigenen App-Store der Institution Anwendungen suchen und eigenständig installieren dürfen, mit denen sie auf vertrauliche Informationen zugreifen können?
* Sollen private und geschäftliche Informationen der Institution auf dem mobilen Endgerät getrennt und auch verwaltet werden? Soll das erfolgen, ohne die bereits vorhandenen Erfahrungen der Mitarbeiter mit mobilen Endgeräten der Institution zu beeinträchtigen?
* Sollen hoch effektive Sicherheitsmaßnahmen implementiert werden, die für den Benutzer des mobilen Endgerätes unsichtbar sind?
* Sollen die Benutzer bei der Einhaltung der Anforderungen der Institution durch frei wählbare mobile Endgeräte und der damit einhergehenden besseren Akzeptanz von implementierten technischen Absicherungsmaßnahmen unterstützt werden?
* Wie hoch ist der Administrationsaufwand, wenn Betriebssysteme von unterschiedlichen Herstellern in diversen Versionen unterstützt werden?
**Muss die MDM-Lösung mandantenfähig sein?**

Eine mandantenfähige MDM-Lösung wird wahrscheinlich nicht für kleinere Umgebungen mit wenigen Benutzern notwendig sein. Ab einer größeren Anzahl von Benutzern kann aus unterschiedlichen Gründen jedoch schnell der Wunsch nach getrennten Mandanten entstehen. Ob eine mandantenfähige MDM-Lösung notwendig ist, hängt davon ab, wie umfangreich komplexe Berechtigungsstrukturen innerhalb der Lösung abgebildet werden können. Für den Benutzer eines mobilen Endgeräts ist ohne diese Möglichkeit eventuell die beste MDM-Lösung wertlos, da jede eingereichte Berechtigung sich automatisch auf alle vererbt und somit dem Maximumprinzip folgt. Wenn Organisationsstrukturen abgebildet werden sollen, ist das ein eindeutiges Indiz für den Bedarf einer mandantenfähigen MDM-Lösung. Damit sie zukunftsfähig ist, sollte die Lösung dann in der gehosteten Variante ebenso wie in der Cloud-Variante funktionieren.

Eine mandantenfähige Lösung kann sich auch empfehlen, wenn Zugänge auf das Backend der MDM-Lösung für unterschiedliche Interessengruppen bereitgestellt werden sollen, z. B. für verantwortliche Administratoren, Auditoren, die interne Revision oder für das Controlling.

**Müssen Cloud-Dienste eingebunden werden?**

Bei der Nutzung von Online-Speicherdiensten (z. B. Cloud-Dienste von Microsoft, Google oder Apple, Dropbox und ähnliche) kann zwischen verschiedenen Varianten unterschieden werden. Das Online-Backup, bei dem Daten einmalig oder in regelmäßigen Abständen über das Internet gespeichert werden, um nach einem Datenverlust wieder abgerufen werden zu können, stellt dabei die einfachste Form der Nutzung dar. Bei der sogenannten Online-Festplatte sind je nach Dienstleister neben der reinen Datenspeicherung auch zusätzliche Funktionen verfügbar. Beispielsweise können Daten und Dokumente mit Mitarbeitern oder Geschäftspartnern geteilt oder gemeinsam bearbeitet sowie über verschiedene Endgeräte synchronisiert werden.

Kann nicht auf die Daten der Institution zugegriffen werden, weil der Onlinespeicher-Dienst aufgrund eines Ausfalls des Dienstleisters oder der Verbindung zum Dienst nicht verfügbar ist, kann das die Geschäftsprozesse stören oder sie können komplett ausfallen. Wichtig sind hierbei insbesondere die Schutzbedarfsanforderungen an die betroffenen Informationen. Sofern die Prozesse hochverfügbar sein müssen, drohen bei längeren Ausfallzeiten des Onlinedienstes finanzielle Verluste oder auch Imageschäden. Neben der Verfügbarkeit des Onlinespeichers und der darin abgelegten Informationen hat vor allem die Vertraulichkeit der Informationen einen hohen Stellenwert. Gelingt es Angreifern auf vertrauliche Informationen der Institution zuzugreifen und diese z. B. einem breiteren Personenkreis zugänglich zu machen, drohen Imageverlust sowie rechtliche Konsequenzen und finanzielle Einbußen.

Wenn Informationen über das Netz übertragen, bearbeitet oder abschließend gespeichert werden, können Integritätsprobleme auftreten, die bis hin zum Totalverlust führen können. Das gilt auch für verschlüsselte Daten. Solche Probleme wirken sich ähnlich aus wie der Verlust der Vertraulichkeit.

Werden bei Vertragsende die Informationen der Institution durch den Anbieter des Onlinespeichers nicht ordnungsgemäß gelöscht, besteht die Gefahr, dass Unbefugte auf diese Informationen zugreifen können.

**Müssen Dokumentenmanagementsysteme eingebunden werden?**

Die Frage, ob Dokumentenmanagementsysteme eingebunden werden sollen, hängt eng zusammen mit der Anforderung an die Mandantenfähigkeit der MDM-Lösung. Für die Strategie bedeutet das, dass die MDM-Lösung Informationen an andere Enterprise-Systeme übergeben können muss, z. B. über Web-Services. Hier ist darauf zu achten, dass dies skalierbar und unabhängig von der Anzahl der anderen eingebundenen Systeme möglich ist.

**Müssen zusätzlich zu den mobilen Endgeräten auch Peripherie-Geräte eingebunden und verwaltet werden?**

Wenn mobile Endgeräte eingeführt werden, müssen durch die Verantwortlichen auch die datenschutzrechtlichen, sicherheitstechnischen und betrieblichen Anforderungen für die Einbindung von Peripherie-Geräten definiert werden. Beispielsweise ist es oft alles andere als einfach, eine Strategie zum mobilen Drucken innerhalb der Institution zu implementieren und dabei die unterschiedlichen Einsatzorte von mobilen Endgeräten zu berücksichtigen. Ursache hierfür ist, dass innerhalb der meisten Institutionen eine breite Palette von Hardware, Software und Serviceangeboten je nach Drucker und zugrunde liegender Druckerinfrastruktur berücksichtigt werden muss.

Im Betriebssystem integrierte Lösungen zu benutzen, wird umso schwieriger, je mehr mobile Plattformen zu unterstützen sind. Sollen z. B. bereits bestehende Netzdrucker über die mobilen Endgeräte erreichbar sein, müssen meist Partner-Lösungen der MDM-Anbieter integriert oder cloudbasierte Lösungen benutzt werden. Die Evaluierung, welche Lösung die Sicherheitsstrategie der Institution am besten unterstützt, sollte ein fester Bestandteil der Planungs- und Konzeptionsphase sein. Wird das an dieser Stelle vergessen, ist damit zu rechnen, dass die Benutzer von mobilen Endgeräten sich „Workarounds“ aufbauen, die die etablierten Sicherheitsmaßnahmen umgehen.

**Welche Betriebsmodell soll für mobile Endgeräte in Betracht kommen?**

Eine der wichtigsten Fragen beim Einsatz von mobilen Endgeräten ist, welches Betriebsmodell eingeführt werden soll. Zwei Betriebsmodelle oder eine Kombination beider Modelle stehen zur Auswahl:

* An die Mitarbeiter ausgegebene GeräteIn diesem Modell beschafft die Institution die Geräte selbst und stellt sie den Benutzern zur Verfügung, entweder als personalisierte Einzelgeräte oder als gemeinsam genutzte Endgeräte.
* Bring Your Own Device (BYOD)Die Mitarbeiter der Institution nutzen bereits vorhandene private mobile Endgeräte, um auf Informationen der Institution zuzugreifen.
Ob BYOD innerhalb der Institution freigegeben werden kann, sollte anhand der nachfolgenden Fragen hinsichtlich eines akzeptablen Risikos beantwortet und bewertet werden.

* Sind die rechtlichen Konflikte bei der dienstlichen Nutzung von privaten mobilen Endgeräten bezüglich des Softwarelizenzrechts geklärt oder ausgeräumt, z. B. dienstliche Nutzung privater Lizenzen oder private und dienstliche Nutzung von dienstlichen Lizenzen?
* Sind im Rahmen des Notfallmanagements Maßnahmen hinsichtlich der Löschung des gesamten Datenbestands mit den Besitzern der mobilen Endgeräte vereinbart worden?
* Sind die Verantwortlichen der IT-Abteilung in der Lage, jedes einzelne private Gerät daraufhin zu prüfen, ob es geeignet ist, im institutionellen Umfeld eingesetzt zu werden?
* Sind Möglichkeiten evaluiert, wie interne Datenschutz- und Sicherheitsanforderungen ausreichend umgesetzt werden können?
* Ist sichergestellt, dass bei Reparatur- und Wartungsarbeiten an privaten mobilen Endgeräten unberechtigte Dritte nicht auf Informationen der Institution zugreifen können?
* Ist sichergestellt, dass nachdem ein Arbeitsverhältnis beendet wurde, der ehemalige Mitarbeiter nicht mehr auf Informationen der Institution zugreifen kann und alle dienstlichen Informationen auf dem mobilen Endgerät gelöscht werden können?
* Ist sichergestellt, dass jederzeit genug Ressourcen für die Benutzerunterstützung vorhanden sind?
Sollte eine der Fragen nicht umsetzbar sein, also mit Nein beantwortet werden, ist vom Einsatz von BYOD mindestens für die eingangs aufgeführten Szenarien 2 und 3 abzuraten.

Die Strategie für das Mobile Device Management muss schriftlich fixiert und vom ISB freigegeben werden. Sie sollte regelmäßig aktualisiert werden.

#### SYS.3.2.2.M2 Festlegen erlaubter mobiler Endgeräte

Grundsätzlich müssen alle in einer Institution eingesetzten mobilen Endgeräte die Anforderungen der MDM-Strategie erfüllen. Das bedeutet, sie müssen alle technischen Sicherheitsmaßnahmen, die die Institution bereits implementiert hat oder in absehbarer Zeit bereitstellen möchte, unterstützen. Für die Beschaffung von mobilen Endgeräten, deren Displays und Batterien erfahrungsgemäß stark beansprucht werden, sollte ein Gerätelebenszyklus von etwa zwei Jahren veranschlagt werden. Wenn Geräte unterschiedlicher Hersteller und mit verschiedenen Betriebssystemen bereitgestellt werden, muss sichergestellt sein, dass nicht durch unterschiedliche Konfigurationsprofile die Sicherheit des Informationsverbundes und der verarbeiteten Informationen gefährdet wird.

Das MDM darf nur den mobilen Endgeräten Zugriff auf interne Netze gewähren, die den Freigabe- und Absicherungsprozess durchlaufen haben. Es muss eine Übersicht der mobilen Endgeräte und Betriebssystemvarianten geben, die in der Institution zugelassen sind. 

#### SYS.3.2.2.M3 Auswahl einer MDM-Produkts

Es gibt eine Vielzahl von MDM-Produkten auf dem Markt. Es muss ein MDM-Produkt ausgewählt werden, dass die definierten Anforderungen der MDM-Strategie unterstützt. Es ist sicherzustellen, dass nur MDM-Software genutzt oder beschafft wird, die alle technischen und organisatorischen Sicherheitsmaßnahmen umsetzen kann und alle freigegebenen mobilen Endgeräte unterstützt.

#### SYS.3.2.2.M4 Verteilung der Grundkonfiguration auf mobile Endgeräte

Die Verantwortlichen müssen sicherstellen, dass alle mobilen Endgeräte unabhängig vom Hersteller, Modell und dem eingeführten Betriebsmodell umgehend über das MDM die gewählten Konfigurationen erhalten, inklusive der Sicherheitseinstellungen. Um zu gewährleisten, dass alle Informationen der Institution auf dem Gerät durch die Absicherungsmaßnahmen geschützt sind, sollten sich alle mobilen Endgeräte im Werkszustand befinden.

Die zu beachtenden Anforderungen und Empfehlungen für die Grundkonfiguration und Integration der mobilen Endgeräte können den Umsetzungshinweisen der folgenden Bausteine entnommen werden:

* SYS.3.2.1 Smartphone/Tablet
* SYS.3.2.3 iOS (for Enterprise)
* SYS.3.2.4 Android
* SYS.3.2.5 Windows
* SYS.3.2.6 BlackBerry
#### SYS.3.2.2.M5 Sichere Grundkonfiguration für mobile Endgeräte

Die Grundkonfiguration der Geräte muss dem zu erfüllenden Schutzbedarf angemessen sein und wird meist in einem spezifischen Gerätebaustein definiert. Die zu beachtenden Anforderungen und Empfehlungen für die Grundkonfiguration und Integration der mobilen Endgeräte können den Umsetzungshinweisen der folgenden Bausteine entnommen werden:

* SYS.3.2.1 Smartphone/Tablet
* SYS.3.2.3 iOS (for Enterprise)
* SYS.3.2.4 Android
* SYS.3.2.5 Windows
* SYS.3.2.6 BlackBerry
Unter Berücksichtigung der etablierten Prozesse für die Inbetriebnahme von mobilen Endgeräten und der Übergabe an die späteren Benutzer sollte sichergestellt sein, dass der MDM-Client bereits auf den Geräten vorhanden ist oder es den Benutzern möglich ist, ihn selbst zu installieren.

#### SYS.3.2.2.M6 Protokollierung

Um eine Protokollierung in einem Informationsverbund zu realisieren, muss geplant werden, wie diese technisch und organisatorisch aufgebaut wird. Auch muss dazu ein Sicherheitskonzept erstellt werden. Ist bereits ein Sicherheitskonzept für die Protokollierung vorhanden, sollten die Anforderungen für das MDM dort integriert werden. Ebenfalls muss geregelt sein, wie die Zugriffsrechte auf Protokollierungsdienste und Protokolldaten des MDM vergeben werden.

Wenn zentral protokolliert wird, ist zu überlegen, wie der zentrale Protokollierungsserver in die Netzinfrastruktur des Informationsverbundes integriert werden kann oder der Zugriff bei einer Cloud-Lösung erfolgen soll. In den folgenden Tabellen wird aufgezeigt, mit welchen Einstellungsempfehlungen die Protokollierung im MDM für die mobilen Endgeräte abgebildet werden könnte.

Tabelle : Protokollierung im MDM - Bereich Sicherheit

Tabelle : Protokollierung im MDM - Bereich App-Verwaltung

Tabelle : Protokollierung im MDM - Bereich Inhalteverwaltung

Tabelle : Protokollierung im MDM - Bereich Geräteeinschränkungen

Tabelle : Protokollierung im MDM – Fehlerbehebung und Überwachung

Tabelle : Protokollierung im MDM – Mobile-Device-Enrollment

Das MDM muss ebenfalls alle sicherheitsrelevanten Aktionen und Konfigurationsänderungen am MDM selbst protokollieren. Die Protokolldateien dürfen nicht von Unbefugten eingesehen werden und auch nicht verändert werden können. Bei der Protokollierung müssen gesetzliche und interne Regelungen eingehalten werden.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Mobile Device Management (MDM)".

#### SYS.3.2.2.M7 Auswahl und Freigabe von Apps

Der Mehrwert eines mobilen Endgeräts ist erst erkennbar, wenn es integraler Bestandteil der Infrastruktur der Institution wird und den Benutzern einen umfänglichen Zugang zu den Informationen ermöglicht. Das bedeutet, dass interne und/oder vertrauliche Informationen den Benutzern auch außerhalb der Institutionsinfrastruktur zur Verfügung gestellt werden. Im Rahmen des Freigabeprozesses für Apps sollten deshalb mindestens die folgenden Kriterien geprüft und als Basis für eine Ablehnung oder Freigabe dienen:

Alle freigegebenen Anwendungen (Apps) sollten in einem Standardkatalog den Benutzern intern zur Verfügung gestellt und somit veröffentlicht werden. Bietet der Hersteller eines mobilen Endgeräts für seine Plattform Volumenlizenzprogramme an, sollte dieses Programm in die Softwareverteilungsprozesse integriert werden.

Unter Berücksichtigung der Ergebnisse des Freigabeprozesses können mittels der nachfolgenden Empfehlungen die Sicherheitsziele je Szenario unterstützt werden.

Tabelle : Einbindung des App-Store und Freigabe von Apps

#### SYS.3.2.2.M8 Festlegung erlaubter Informationen auf mobilen Endgeräten

Die Institution sollte festlegen, unter welchen Bedingungen die mobilen Endgeräte welche Informationen verarbeiten dürfen. Die Definition muss sich auf die Klassifikation bzw. Schutzbedarf der Informationen oder auf deren zugrunde liegende Prozesse beziehen und die Bedingungen zur Verarbeitung klar regeln, wie z. B. Verschlüsselung, Container oder freigegeben für die Cloud. Diese Definition ist als Grundlage für die Konfiguration der mobilen Endgeräte durch das MDM und für die eventuell benötigte Einbindung von zusätzlichen Sicherheitsinfrastrukturen heranzuziehen. Alle Regelungen sollten für die Benutzer dokumentiert und in einer geeigneten Form übergeben werden. Um Sicherheitsvorfälle automatisiert zu erkennen, sollten soweit möglich technische Maßnahmen implementiert werden, mit denen sich die aufgestellten internen Regeln durchsetzen lassen.

#### SYS.3.2.2.M9 Auswahl von Sicherheits-Apps

Der vielleicht wichtigste Aspekt bei der Auswahl von Sicherheits-Apps ist die Benutzerfreundlichkeit. So sollen die Benutzer sich schnell authentisieren und schnell auf Apps und Informationen der Institution über ein mobiles Endgerät zugreifen können. Alle Anwendungen, die die Sicherheit des Gerätes selbst oder der dort gespeicherten Informationen erhöhen, werden der Kategorie Sicherheits-Apps zugeordnet. Die wichtigste Sicherheits-App ist der Client des Mobile-Device-Management-Systems. Abhängig vom gewählten Betriebssystem und dem Sicherheitsframework des Herstellers gibt es weitere Apps dieser Kategorie, deren Funktion teilweise Bestandteil des MDM-Clients sein kann:

* Apps zur Lokalisierung des Gerätes im Falle des Verlusts,
* Antiviren-Apps,
* Apps für die kryptografische Absicherung von einzelnen Daten oder Ordnern,
* Apps für die Bereitstellung von Arbeitsumgebungen mittels einer Container-Isolierungstechnik sowie
* Apps, die den Zugriff auf andere Apps zusätzlich regeln.
Auf Basis der gewählten Strategie muss die Auswahl von Sicherheits-Apps verbindlich formuliert und geregelt sein. Die Auswahl muss für jedes eingesetzte Betriebssystem der Geräte geeignete Apps aufführen. Das MDM muss die Installation dieser Apps erzwingen.

#### SYS.3.2.2.M10 Sichere Anbindung der mobilen Endgeräte an die Institution

Wird mobilfunkbasiert ein institutionsbezogener Zugangspunkt (Access Point Name, APN) benutzt, kann dieser die Grundlage dafür bilden, den erlaubten Gerätepool einzugrenzen. Alle mobilen Endgeräte der Institution, die diesen APN verwenden, erhalten vom Mobilfunkprovider einen mit der Institution abgestimmten IP-Adressenbereich. Um Sicherheitsvorfälle zu vermeiden, die durch zu kurze Passwörter für die Authentisierung verursacht werden, sollte ein komplexes Passwort (bis maximal 64 und mindestens 10 Stellen) mit dem Mobilfunkprovider vereinbart werden. Beim Einsatz eines institutionsbezogenen APN sollte zudem mit dem Protokoll CHAP authentisiert werden.

Die sichere Anbindung der mobilen Endgeräte an die Institution sollte mit einem VPN erfolgen, da so die Vertraulichkeit und Integrität der zwischen den mobilen Endgeräte und dem IT-Netz der Institution übertragenen Informationen gewahrt wird. Für die Konfiguration der VPN-Verbindungen zu den Servern von beispielsweise *Aruba VIA*, *Check Point Mobile VPN*, *Cisco AnyConnect*, *F5 SSL*, *Juniper SSL*, *SonicWALL Mobile Connect*, *NCP*, *genua* oder *SINA* bieten die MDM-Anbieter häufig mit den VPN-Herstellern abgestimmte Einstellungen an. Jedoch müssen neben dem Konfigurationsprofil für die VPN-Verbindung oft noch zusätzlich die Apps der VPN-Server-Hersteller aus dem jeweiligen App-Store installiert werden. Im Dokument *Technische Richtlinie TR-02102* des BSI werden Empfehlungen für die Verwendung von IPSec und SSL/TLS ausgesprochen (siehe Kapitel 3.2 der TR).

Bei der Implementierung eines VPN ist es unabhängig vom genutzten Algorithmus und Protokoll möglich, ein VPN permanent, nur bei Bedarf oder für einzelne verwaltete Apps zu konfigurieren.

**Permanentes VPN**

Ein permanentes VPN ermöglicht es, alle Kommunikationsverbindungen zu kontrollieren. Die Verantwortlichen in der Institution können so den Datenverkehr zu und vom mobilen Endgerät vollständig überwachen und falls erforderlich filtern. Damit lassen sich die Informationen der Institution schützen und der Zugriff der Geräte auf das Internet kann entsprechend den internen Anforderungen reguliert werden.

**VPN On-Demand**

Mit VPN On-Demand können mobile Endgeräte automatisch eine VPN-Verbindung in die Institution herstellen. Die hinterlegten Regelungen für das Erkennen des Bedarfs durch das mobile Endgerät erfolgen meist in zwei Etappen, der Netzerkennung und der Verbindungsevaluierung.

**VPN auf App-Basis**

Ein VPN auf App-Basis wird je nach Betriebssystem und MDM-Hersteller unterschiedlich umgesetzt. Allen Lösungen gemeinsam ist, dass diese Apps verwaltbar sein müssen. Alle nicht verwalteten Apps dürfen den VPN-Tunnel in die Institution nicht benutzen. Ein weiteres Merkmal für verwaltete Apps ist, dass unterschiedliche VPN-Verbindungen konfiguriert werden können, um Informationen noch differenzierter zu schützen. Um ein VPN auf App-Basis zu realisieren, muss die verwaltete App über Standardnetz-APIs angesprochen werden können oder vom MDM-Hersteller durch einen zusätzlichen Layer gekapselt werden.

Welche der beschriebenen VPN-Varianten eingesetzt wird, hängt vom Schutzbedarf, den genutzten Algorithmen und Authentisierungsmethoden sowie der vorhandenen DNS-Struktur ab.

#### SYS.3.2.2.M11 Berechtigungsmanagement im MDM

Berechtigungen dürfen nur eingeschränkt und aufgabenbezogen nach dem Prinzip der geringsten Berechtigungen eingerichtet werden. Durch ein Identitäts- und Berechtigungsmanagement im MDM wird sichergestellt, dass Benutzern von mobilen Endgeräten und Administratoren nur die notwendigen Berechtigungen zugeordnet werden. Eine dokumentierte Vorgehensweise, um Berechtigungen zuzuweisen, zu verändern und wieder zu entziehen, ermöglicht es zu steuern, wie auf Informationen zugegriffen wird. Mit entsprechenden Hintergrundsystemen können außerdem stattgefundene Aktivitäten gespeichert und ausgewertet werden. Im Schadensfall oder aufgrund rechtlicher Anforderungen können so Aktivitäten ausgewertet und den hierfür Verantwortlichen zugeordnet werden.

Zunächst ist zu ermitteln, wie die administrativen Aufgaben organisiert werden sollen, beispielsweise Support durch einen Helpdesk, eigenständige Benutzerregistrierung oder Gerätekonfigurationsmanagement. Die Verantwortlichen müssen die für den MDM-Einsatz ermittelten Funktionen dokumentieren. Im Anschluss ist die Funktionstrennung festzulegen und zu begründen, d. h. welche Funktionen nicht miteinander vereinbar sind und nicht mit dem hierfür eingerichteten Benutzerkonto gleichzeitig wahrgenommen werden dürfen. 

Um die benötigten Funktionstrennungen und Berechtigungen zu ermitteln, können folgende Beispielfragen herangezogen werden: 

* Wie viele Ebenen des Supports werden im Helpdesk benötigt?
* Welche Benutzer mit welchen mobilen Endgeräten werden durch welche Gruppe von Administratoren verwaltet?
* Wer entwickelt und verwaltet die institutionseigenen Apps?
* Wer verwaltet die Richtlinien- und Konfigurationsprozesse?
* Auf welche Informationen des mobilen Endgeräts oder der darauf befindlichen Informationen können die Administratoren zugreifen?
* Müssen die interne Revision oder externe Auditoren immer auf die MDM-Lösung zugreifen können?
* Muss das Sicherheitsmanagement immer auf die MDM-Lösung zugreifen können?
Vorgaben hierfür können aus den Aufgaben selbst oder aus gesetzlichen oder internen Anforderungen resultieren. Das etablierte Berechtigungsmanagement ist regelmäßig darauf zu kontrollieren, ob die zugeteilten Rechte noch den Aufgaben entsprechen.

#### SYS.3.2.2.M12 Abgesicherte MDM-Betriebsumgebung

Eine MDM-Lösung wird auf IT-Systemen betrieben, die entweder in der alleinigen Verantwortung der Institution sind oder die ein Outsourcing-Partner im Auftrag der Institution betreibt. In beiden Fällen ist die Institution dafür verantwortlich, die MDM-Komponenten abzusichern und Netzsegmente schutzbedarfsgerecht zuzuweisen. Auch müssen die Verantwortlichen dafür sorgen, dass die unterstützenden IT-Systeme für das MDM entsprechend dem ermittelten Schutzbedarf ausreichend abgesichert sind. Dabei muss beachtet werden, dass die Sicherheit der mobilen Endgeräte direkt von der Sicherheit des MDM abhängig ist. Um einen angemessenen Schutz zu gewährleisten, sollten die folgenden Anforderungen erfüllt sein:

* das Betriebssystem der MDM-Lösung ist gehärtet,
* die administrativen Zugriffe werden kontrolliert,
* ein missbräuchlicher Zugriff wird erkannt und es werden entsprechende Gegenmaßnahmen eingeleitet,
* die Absicherung der Client-Server Kommunikation entspricht dem benötigten Schutzbedarf,
* die Anmeldeinformationen der Benutzer sind dem benötigten Schutzbedarf entsprechend abgesichert,
* es ist ein kontinuierliches Vulnerability-Assessment etabliert,
* die MDM-Lösung ist in die etablierten Aktualisierungs- und Änderungsmanagement-Prozesse vollständig integriert.
### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.2.2.M13 Einschränkung der App-Installation mittels Whitelist(CIA)

Bei erhöhtem Schutzbedarf sollten die Benutzer der mobilen Endgeräte ausschließlich solche Apps installieren dürfen, die von der Administration und dem Sicherheitsmanagement der Institution untersucht und freigegeben wurden (siehe SYS.3.2.2.M7 *Auswahl und Freigabe von Apps*). Das MDM sollte die Installation anderer Apps verhindern oder alternativ unbefugt installierte Apps sofort wieder entfernen.

#### SYS.3.2.2.M14 Benutzung externer Reputation-Services für Apps(CI)

Ein Reputation-Service ist ein externer Dienst, der Apps nach bestimmten Kriterien untersucht und die Ergebnisse bereitstellt. Die Funktionsweise des Reputation-Services basiert meist auf den folgenden drei Phasen.

**Katalogisieren der Apps**

Der App-Reputation-Service sammelt und katalogisiert Millionen von Apps aus den Stores der Hersteller, von Websites von Drittanbietern, von App-Sharing-Dienstleistungen sowie von strategischen Partnern der App-Reputation-Dienstleister.

**Analyse der Apps**

Über einen mehrstufigen, üblicherweise größtenteils automatisierten Analyseprozess werden detaillierte Informationen zum Verhalten der Apps erhoben.

**Klassifizierung und Bewertung der Apps**

Jede App wird klassifiziert und bewertet. Im Anschluss wird der ausgewerteten App durch den Reputation-Service-Anbieter eine Bewertung (Score) zugewiesen. Zur leichteren Beurteilung der App wird diese häufig einer der folgenden feingranularen Kategorien zugeordnet:

* bösartig (Malicious),
* unerwünscht (Unwanted),
* verdächtig (Suspicious),
* maßvoll (Moderate),
* gutartig (Benign) oder
* vertrauenswürdig (Trustworthy)
Wenn die Benutzer Apps installieren dürfen und die verantwortlichen Administratoren nicht selbst eine Whitelist mit erlaubten Apps erstellen können, ist es durch einen Reputation-Service möglich, Apps wenigstens auf Kategorienbasis einzuschränken. Dabei müssen sich die Verantwortlichen jedoch eng mit dem Sicherheitsmanagement der Institution abstimmen.

#### SYS.3.2.2.M15 Nutzung von PIM-Containern(CI)

Um zu verhindern, dass Spionage-Apps oder unberechtigte Dritte die Personal-Information-Manager-(PIM)-Daten (wie Exchange, Domino, Groupwise) auf dem mobilen Endgerät unbefugt einsehen oder verändern können, sollte ein PIM-Container eingesetzt werden. Ein solcher Container kapselt die PIM-Daten und Funktionen der zu schützenden Anwendung vor anderen Apps auf dem mobilen Endgerät. Der Container muss durch ein eigenes Passwort abgesichert werden und eine vom Betriebssystem unabhängige Verschlüsselung der Daten sowie eine Transportverschlüsselung beinhalten. Wenn ein PIM-Container eingesetzt wird, müssen die Verantwortlichen der Institution nach Möglichkeit sicherstellen, dass das Betriebssystem des mobilen Endgeräts keine Sicherheitslücken aufweist, die die benötigte Sicherheit beeinträchtigen.

#### SYS.3.2.2.M16 Nutzung von getrennten Arbeitsumgebungen(CI)

Einen besonders hohen Schutz der Informationen vor Gefahren, die durch die private Nutzung des Gerätes entstehen, bieten getrennte Arbeitsumgebungen. Wenn ein hoher Schutzbedarf besteht und die Benutzer unterschiedliche Apps verwenden, die mit den IT-Systemen der Institution auf unterschiedlichen Wegen kommunizieren müssen, sollte eine getrennte Arbeitsumgebung eingesetzt werden. Da diese Umgebungen oft über einen eigenen verschlüsselten Speicher und VPN-Kanal verfügen, bieten sie den Apps einen Bereich, in dem der Schutz der Daten von der Arbeitsumgebung bereitgestellt wird. So können auch eventuell unsichere Apps eingesetzt werden. Getrennte Arbeitsumgebungen sind besonders zu empfehlen, wenn Apps auf dem Gerät eine Interaktion mit anderen Apps benötigen, da jede Kommunikation zwischen den einzelnen Apps eventuell auch von anderen Apps ausgenutzt wird und so zum Einfallstor für Angreifer werden kann.

Bei der Auswahl der getrennten Arbeitsumgebung ist auf entsprechende Zertifizierungen (z. B. Common Criteria oder FIPS 140-2) oder Qualitätszeichen wie „IT Security made in Germany“ zu achten. Auch sollte die Hardware des mobilen Endgerätes die benötigten Sicherheitsmaßnahmen selbst unterstützen.

#### SYS.3.2.2.M17 Kontrolle der Nutzung von mobilen Endgeräten(I)

Mit MDM-Lösungen lässt sich überwachen, wie mobile Endgeräte benutzt werden. Sie sollten nach verschiedenen zuvor definierten Kriterien überwacht werden, zum Beispiel: 

* Aktualität des Betriebssystems des mobilen Endgeräts,
* Aktualität der installierten Anwendungen (Apps),
* letzte Synchronisation mit dem MDM,
* Einhalten von hinterlegten Data-Loss-Policies,
* Nutzung von Cloud-Diensten,
* Infektion mit Malware, unter Berücksichtigung des Betriebssystems des mobilen Endgeräts und dessen Sicherheitsframeworks, sowie
* Zugriff auf den derzeitigen Aufenthaltsort.
Bei der Überwachung der Geräte und des Benutzerverhaltens müssen gesetzliche und interne Regelungen beachtet werden.

#### SYS.3.2.2.M18 Besonders abgesicherte Betriebssysteme(CIA)

Auf dem Markt gibt es mehrere Anbieter von besonders abgesicherten mobilen Endgeräten, die teilweise zertifiziert sind für die Verarbeitung von Informationen mit hohem Schutzbedarf oder zugelassen sind für die Verarbeitung von amtlich geheimgehaltener Informationen (Geheimschutz), also als Verschlusssache eingestuft worden sind. Bei hohem Schutzbedarf sollte die Institution ein solches besonders abgesichertes mobiles Endgerät und auch ein damit korrespondierendes MDM einsetzen.

#### SYS.3.2.2.M19 Geofencing(CI)

Geofencing ist ein Kunstwort aus den englischen Worten "geographic" und "fence" und bezeichnet das virtuelle Einzäunen eines geographischen klar umrissenen Gebietes. Über MDM-Systeme ist es mittels Geofencing-Richtlinien möglich, bestimmte Funktionen oder Apps auf mobilen Endgeräten nur an vorher definierten Orten zu erlauben oder auch zu verbieten. 

Bei höherem Schutzbedarf sollten mit Hilfe einer Schutzbedarfsanalyse Bereiche identifizieren werden, an denen diese zusätzlichen Sicherheitsmaßnahmen nötig sind. Anschließend sollten entsprechend Beschränkungen unter Beachtung gesetzlicher und interner Regelungen über Geofencing-Richtlinien konfiguriert werden.

Die folgenden Beispiele zeigen Einsatzmöglichkeiten für Geofencing auf.

**Beispiel 1**

In diesem Beispiel wird angenommen, dass die eingesetzten Geräte das Gelände der Institution nicht verlassen dürfen. Wenn sich die Geräte außerhalb eines definierten Bereichs befinden, wird an den Benutzer, an die verantwortlichen Administrationen sowie an das Sicherheitsmanagement ein Warnhinweis gesendet. Damit der Benutzer auch wieder zurück auf das erlaubte Gelände gehen kann, sollte eine zeitliche Verzögerung hinterlegt werden, bevor die Informationen auf dem Gerät gelöscht werden. Durch die aktive Benachrichtigung des Sicherheitsmanagements kann das Gerät den Sicherheitsvorfall erkennen und bei einem Diebstahl sicherstellen, dass relevante Informationen das Gelände der Institution nicht verlassen. Es kann die Information darüber hinaus nutzen, um zu entscheiden, ob Sensibilisierungsmaßnahmen erforderlich sind, damit die Vorschrift künftig besser beachtet wird. Geofencing könnte auch auf gesetzliche Territorien angewendet werden, um Informationen mit hohem Schutzbedarf abzusichern, z. B. den Bereich des Bundesdatenschutzgesetzes oder des europäischen Datenschutzraums.

**Beispiel 2**

In einem als vertrauenswürdig festgelegten Bereich wird die automatische Sperre des Gerätes nicht aktiviert. Das bedeutet jedoch nicht, dass das Gerät automatisch entsperrt wird, sondern nur, dass es nach einer bestimmten Zeit der Nichtbenutzung nicht wieder gesperrt wird.

**Beispiel 3**

In einem fest hinterlegten geografischen Bereich wird die Kamera des Endgeräts deaktiviert oder gesperrt, z. B. innerhalb des Firmengeländes oder an Plätzen mit vertraulichen Informationen.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Mobile Device Management (MDM)" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_052.pdf)

 
* #### [BYOD] Überblickspapier Consumerisation und BYOD

  

 BSI, Version 1.2, 07.2013  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier\_BYOD\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier_BYOD_pdf.pdf)

 
* #### [CC] Common Criteria for Information Technology Security Evaluation (CC)

  

 erschienen in der Normenreihe ISO 15408: Information technology- Security techniques- Evaluation criteria for IT security, Version 3.1, (zuletzt abgerufen am 28.09.2017)  
 <www.commoncriteriaportal.org>

 
* #### [DIN66399] DIN 66399- Büro- und Datentechnik - Vernichten von Datenträgern

  

 Beuth Verlag

 
* #### [FIPS1402] FIPS PUB 140-2: Security Requirements for Cryptographic Modules

  

 Federal Information Processing Standard (FIPS) Publication, National Institute of Standards and Technology (NIST), 2001  
 <http://csrc.nist.gov/groups/STM/cmvp/standards.html>

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015   
 [https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf ](https://nccoe.nist.gov/sites/default/files/nccoe/NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013  
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf ](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
