import React, {useState} from 'react';
import { View, TextInput, StyleSheet, TouchableOpacity, Text, Button} from 'react-native';
import Firebase from '../config/firebase';
import * as firebase from 'firebase';
import ImagePicker from '../components/ImagePicker'
import Card from '../components/Card'

const SignUp = props => {
    
  const [name, setName] = useState('');
  const [carname, setCarName] = useState('');
  const [license, setLicense] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [selectedImage, setselectedImage] = useState();

  const signUphandler = () => {
      Firebase.auth().createUserWithEmailAndPassword(email, password).then(()=>{props.navigation.navigate('Main')}).catch(error => console.log(error))
      
  }

  const imageTakenHandler = imagePath => {
    setselectedImage(imagePath);
  }
    
  return(
    <View style={styles.container}>
      <Card style={styles.inputContainer}>
                <TextInput style={styles.inputBox} placeholder="Full Name" onChangeText={(value) => {
                  setName(value);
                }}  />
                <TextInput style={styles.inputBox} placeholder="Car Name" onChangeText={(value) => {
                  setCarName(value);
                }}  />
                <TextInput style={styles.inputBox} placeholder="License" onChangeText={(value) => {
                  setLicense(value);
                }}  />
                <TextInput style={styles.inputBox} placeholder="Email" autoCapitalize='none' onChangeText={(value) => {
                  setEmail(value);
                }}  />
                <TextInput style={styles.inputBox} placeholder="Password" secureTextEntry={true} onChangeText={(value) => {
                  setPassword(value);
                }}  />
                
                <View><ImagePicker onImageTake={imageTakenHandler} /></View>
                <TouchableOpacity style={styles.button} onPress={signUphandler}>
                    <Text style={styles.buttonText}>Signup</Text>
                </TouchableOpacity>
                <Button title="Go Back" onPress={() => {props.navigation.navigate('Login')}} />
        </Card>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 50,
    alignItems: 'center',
    justifyContent: 'center'
},
inputContainer: {
  padding: 15,
  width: 500,
  maxWidth: '98%',
  alignItems: 'center',
},
inputBox: {
    width: '98%',
    margin: 10,
    fontSize: 16,
    padding: 10,
    paddingBottom: 0,
    borderColor: 'rgba(0,0,0,0.05)',
    borderBottomWidth: 1,
    textAlign: 'center'
},
button: {
    marginTop: 30,
    marginBottom: 20,
    paddingVertical: 5,
    alignItems: 'center',
    backgroundColor: '#006400',
    borderColor: '#006400',
    borderWidth: 1,
    borderRadius: 5,
    width: 200
},
buttonText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff'
},
buttonSignup: {
    fontSize: 12
}
});

export default SignUp;