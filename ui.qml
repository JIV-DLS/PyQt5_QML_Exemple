import QtQuick 2.6
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

ColumnLayout {
    id: root
    anchors.fill: parent
    property int current_model_size : current_model_size_from_model
    Component {
            id: personneDelegate
            Item {
                width: 500
                height: 55
                RowLayout {
                    width: 500
                    height: 55
                    Column {
                                Text { text: '<b>Title:</b> ' + name }
                                Text { text: '<b>Age:</b> ' + age }
                                Text { text: '<b>Wage:</b> ' + wage }
                            }
                    Image {
                        objectName: "cardLeft"
                        id: cardLeft
                        Layout.fillWidth: true
                        Layout.maximumHeight: 50
                        Layout.minimumHeight: parent.height
                        Layout.margins: 20
                        source: image
                        fillMode: Image.PreserveAspectFit
                        }
                    Button {
                        text: "Increase Wage Of 500"
                        onClicked: {
                            PersonModel.increaseWageOf(index,500)
                        }
                    }
                    Button {
                        text: "Delete"
                        onClicked: {
                            PersonModel.delete(index)
                            --root.current_model_size
                            }
                    }
                }
        }
    }
    Button {

        height:20
        text: "Add to top"
        
        onClicked: PersonModel.addToTop('inserted_top_jon_'+(++root.current_model_size),20+root.current_model_size%20,5000)

    }
    Button {

        height:20
        text: "Add to bottom"
        onClicked: PersonModel.addToBottom('inserted_bottom_jon_'+(++root.current_model_size),20+root.current_model_size%20,5000)

    }
    ListView {
        id: listExample
        Layout.fillWidth: true
        Layout.fillHeight: true
        model: PersonModel
        delegate: personneDelegate
        focus: true
        flickableDirection: Flickable.AutoFlickDirection
    }
}

