import React, { useState } from 'react';
import { View, Text, StyleSheet, Alert, TouchableOpacity, StatusBar} from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import * as firebase from 'firebase';

const ImgPicker = props => {
  const [pickedImage, setPickedImage] = useState('');

  const verifyPermissions = async () => {
    const result = await Permissions.askAsync(Permissions.CAMERA_ROLL, Permissions.CAMERA);
    if (result.status !== 'granted') {
      Alert.alert(
        'Insufficient permissions!',
        'You need to grant camera permissions to use this app.',
        [{ text: 'Okay' }]
      );
      return false;
    }
    return true;
  };

  const takeImageHandler = async () => {
    const hasPermission = await verifyPermissions();
    if (!hasPermission) {
      return;
    }
    const image = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      quality: 0.5
    });

    if(!image.cancelled){
      setPickedImage(image.uri);
      props.onImageTake(image.uri);
      uploadImage(image.uri, "test-image" + Date.now().toString()).then(()=>{console.log("Success")}).catch(
        (error) => {console.log(error)})
    }
  };

  const uploadImage = async (uri, fileName) => {
    const response = await fetch(uri);
    const blob = await response.blob()    
    var ref = firebase.storage().ref().child("images/" + fileName)
    return ref.put(blob);
  }

  return (
    <View style={styles.imagePicker}>
      <TouchableOpacity style={styles.button} onPress={takeImageHandler}  >
        <Text style={styles.buttonText}>Take Image from Camera</Text>
        <StatusBar barStyle="default" />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  imagePicker: {
    alignItems: 'center',
    marginTop: 15
  },
  imagePreview: {
    width: '100%',
    height: 200,
    marginBottom: 10,
    justifyContent: 'center',
    alignItems: 'center',
    borderColor: '#ccc',
    borderWidth: 1
  },
  image: {
    width: '100%',
    height: '100%'
  },
  button: {
    paddingVertical: 5,
    paddingHorizontal: 10,
    alignItems: 'center',
    backgroundColor: '#800000',
    borderColor: '#800000',
    borderWidth: 0.2,
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#fff'
},
});

export default ImgPicker;