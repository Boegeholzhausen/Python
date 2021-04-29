import re

text = '''
Video bietet eine leistungsstarke Möglichkeit zur Unterstützung Ihres Standpunkts. Wenn Sie auf "Onlinevideo" klicken, können Sie den Einbettungscode für das Video einfügen, das hinzugefügt werden soll. Sie können auch ein Stichwort eingeben, um online nach dem Videoclip zu suchen, der optimal zu Ihrem Dokument passt.
Damit Ihr Dokument ein professionelles Aussehen erhält, stellt Word einander ergänzende Designs für Kopfzeile, Fußzeile, Deckblatt und Textfelder zur Verfügung. Beispielsweise können Sie ein passendes Deckblatt mit Kopfzeile und Randleiste hinzufügen. Klicken Sie auf "Einfügen", und wählen Sie dann die gewünschten Elemente aus den verschiedenen Katalogen aus.
Designs und Formatvorlagen helfen auch dabei, die Elemente Ihres Dokuments aufeinander abzustimmen. Wenn Sie auf "Entwurf" klicken und ein neues Design auswählen, ändern sich die Grafiken, Diagramme und SmartArt-Grafiken so, dass sie dem neuen Design entsprechen. Wenn Sie Formatvorlagen anwenden, ändern sich die Überschriften passend zum neuen Design.
Sparen Sie Zeit in Word dank neuer Schaltflächen, die angezeigt werden, wo Sie sie benötigen. Zum Ändern der Weise, in der sich ein Bild in Ihr Dokument einfügt, klicken Sie auf das Bild. Dann wird eine Schaltfläche für Layoutoptionen neben dem Bild angezeigt Beim Arbeiten an einer Tabelle klicken Sie an die Position, an der Sie eine Zeile oder Spalte hinzufügen möchten, und klicken Sie dann auf das Pluszeichen.
Auch das Lesen ist bequemer in der neuen Leseansicht. Sie können Teile des Dokuments reduzieren und sich auf den gewünschten Text konzentrieren. Wenn Sie vor dem Ende zu lesen aufhören müssen, merkt sich Word die Stelle, bis zu der Sie gelangt sind – sogar auf einem anderen Gerät.
'''

letterRegex = re.compile(r'\w')
var = letterRegex.findall(text)

print(var)








# var = ["a","b","c","d","e"]
# for i in range(0, 5):
#     print(var[i])