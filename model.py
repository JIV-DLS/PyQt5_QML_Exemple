from PyQt5.QtCore import QAbstractListModel, Qt, pyqtSlot, QModelIndex

class PersonModel(QAbstractListModel):

    #Les rôles permettent de retirer les attributs afficher sur la ListView
    NameRole = Qt.UserRole + 1
    AgeRole = Qt.UserRole + 2
    ImageRole = Qt.UserRole + 3
    WageRole = Qt.UserRole + 4
    def __init__(self, parent=None):
        super().__init__(parent)
        #generation de 5000 données
        self.persons = [
            {'name': 'jon'+str(i),
             'age': 20+i%20, 
             'image':'https://www.gettyimages.fr/gi-resources/images/500px/983794168.jpg' \
                 if i%1000==0 and i>0 else \
                     'https://d1fmx1rbmqrxrr.cloudfront.net/cnet/optim/i/edit/2019/04/eso1644bsmall__w770.jpg',
             'wage': 5000} for i in range(5000)
        ]

    #Chargement du bon élément de la liste en fonction de l'index
    #cette méthode est appelée pour ne charger que les éléments visibles
    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == PersonModel.NameRole:
            return self.persons[row]["name"]
        if role == PersonModel.AgeRole:
            return self.persons[row]["age"]
        if role == PersonModel.ImageRole:
            return self.persons[row]["image"]
        if role == PersonModel.WageRole:
            return self.persons[row]["wage"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.persons)

    #Affectation des rôles aux attributs
    def roleNames(self):
        return {
            PersonModel.NameRole: b'name',
            PersonModel.AgeRole: b'age',
            PersonModel.ImageRole: b'image',
            PersonModel.WageRole: b'wage'
        }

    #Ajout d'une personne en début de liste
    @pyqtSlot(str, str, int)
    def addToTop(self, name, age,wage):
        self.beginInsertRows(QModelIndex(), 0, 0)
        self.persons.insert(0,{'name': name, 
        'age': age,
        'image':  'https://www.gettyimages.fr/gi-resources/images/500px/983794168.jpg' \
            if self.rowCount()%1000==0 and self.rowCount()>0 else \
                'https://d1fmx1rbmqrxrr.cloudfront.net/cnet/optim/i/edit/2019/04/eso1644bsmall__w770.jpg',
        'wage': wage})
        self.endInsertRows()

    #Ajout d'une personne en fin de liste
    @pyqtSlot(str, str, int)
    def addToBotom(self, name, age,wage):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.persons.append({'name': name, 
        'age': age,
        'image':  'https://www.gettyimages.fr/gi-resources/images/500px/983794168.jpg' \
            if self.rowCount()%1000==0 and self.rowCount()>0 else\
                 'https://d1fmx1rbmqrxrr.cloudfront.net/cnet/optim/i/edit/2019/04/eso1644bsmall__w770.jpg',
        'wage': wage})
        self.endInsertRows()

    #Modification d'un attribut
    @pyqtSlot(int, int)
    def increaseWageOf(self, row, increseValue):
        ix = self.index(row, 0)
        self.persons[row]['wage'] = self.persons[row]['wage'] + increseValue
        self.dataChanged.emit(ix, ix, self.roleNames())

    #Suppression d'un élément
    @pyqtSlot(int)
    def delete(self, row):
        self.beginRemoveColumns(QModelIndex(), row, row)
        del self.persons[row]
        self.endRemoveRows()
